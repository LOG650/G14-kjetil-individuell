"""
BiteBurst Lageroptimalisering – SARIMA-modellering
===================================================
Leser salgsdata fra 004 data/, tilpasser SARIMA(p,d,q)(P,D,Q,7) per produkt
per butikk via auto_arima, og beregner:
  - 7-dagers etterspørselsprognose
  - Sikkerhetslager ved 95 % servicegrad
  - Anbefalt ukentlig bestillingsmengde
  - Ljung-Box residualdiagnostikk (lag 7 og 14)
  - Naiv baselineprognosens MAPE til sammenligning

Resultater skrives til:
  sarima_results.json   – fullstendige tall og modellparametere
  plots/                – tidsserieplott med prognose og prediksjonsintervall
"""

import csv
import json
import os
import warnings

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
from pmdarima import auto_arima
from scipy import stats
from statsmodels.stats.diagnostic import acorr_ljungbox

warnings.filterwarnings("ignore")

# ---------------------------------------------------------------------------
# Konfigurasjon
# ---------------------------------------------------------------------------
BASE_DIR     = os.path.dirname(os.path.abspath(__file__))
DATA_DIR     = os.path.join(BASE_DIR, "..", "004 data")
PLOTS_DIR    = os.path.join(BASE_DIR, "plots")
RESULTS_FILE = os.path.join(BASE_DIR, "sarima_results.json")

os.makedirs(PLOTS_DIR, exist_ok=True)

STORES        = ["GM", "HK", "LM", "MH"]
PRODUCTS      = ["Pizza", "Salad", "French", "Burger", "Hotdog", "Soda", "Ice Cream", "Kebaba"]
FORECAST_DAYS = 7          # planleggingshorisont (én uke)
SERVICE_LEVEL = 0.95       # ønsket servicegrad
Z             = stats.norm.ppf(SERVICE_LEVEL)   # 1.645

# ---------------------------------------------------------------------------
# Datainnlasting
# ---------------------------------------------------------------------------
def load_store(store: str) -> dict[str, list[int]]:
    """Returnerer dict {produkt: [daglig salg dag 1..101]}."""
    path = os.path.join(DATA_DIR, f"BiteBurst {store}.csv")
    with open(path, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f, delimiter=";"))

    data = {}
    for p in PRODUCTS:
        vals = [int(r[p].strip()) for r in rows
                if r.get(p, "").strip().lstrip("-").isdigit()]
        if vals:
            data[p] = vals
    return data


# ---------------------------------------------------------------------------
# SARIMA-tilpasning og prognose
# ---------------------------------------------------------------------------
def fit_and_forecast(series: list[int], store: str, product: str) -> tuple:
    """
    Deler serien i trenings- og valideringssett (siste 7 dager).
    Tilpasser SARIMA automatisk med auto_arima (sesong s=7).
    Beregner Ljung-Box residualdiagnostikk og naiv baseline-MAPE.
    Returnerer (result_dict, train, test, fc_point, fc_upper).
    """
    arr   = np.array(series, dtype=float)
    train = arr[:-FORECAST_DAYS]
    test  = arr[-FORECAST_DAYS:]

    model = auto_arima(
        train,
        start_p=0, max_p=3,
        start_q=0, max_q=3,
        d=None,                 # auto-velg differensieringsgrad
        seasonal=True, m=7,
        start_P=0, max_P=2,
        start_Q=0, max_Q=2,
        D=None,
        information_criterion="aic",
        stepwise=True,
        suppress_warnings=True,
        error_action="ignore",
        trace=False,
    )

    fc, ci = model.predict(
        n_periods=FORECAST_DAYS,
        return_conf_int=True,
        alpha=1 - SERVICE_LEVEL,    # 95 % PI
    )
    fc = np.maximum(fc, 0)

    # --- Nøkkeltall ---
    # Dataene er rullerende 7-dagerssummer fra spillet ("sold last 7 days").
    # Det 7. prognosesteget gir direkte den predikerte 7-dagerssummen for
    # de neste 7 dagene – det er dette vi vil bestille.
    fc_sum   = float(fc[-1])                   # 7. steg = prognose neste 7 dager
    fc_upper = float(ci[-1, 1])                # øvre PI for samme steg

    # Sikkerhetslager = øvre PI-grense minus punktprognose (7-dagersnivå)
    safety_stock = max(fc_upper - fc_sum, 0)

    # Anbefalt bestillingsmengde = punktprognose + sikkerhetslager
    recommended = fc_sum + safety_stock        # = fc_upper (ved 95 %)

    # MAPE på valideringssettet
    mape = float(np.mean(np.abs((test - fc) / np.where(test == 0, 1, test))) * 100)

    # --- Ljung-Box residualdiagnostikk ---
    # H0: ingen autokorrelasjon i residualene (ønsket: p > 0.05)
    residuals = model.resid()
    lb = acorr_ljungbox(residuals, lags=[7, 14], return_df=True)
    lb_pvalue_lag7  = round(float(lb["lb_pvalue"].iloc[0]), 4)
    lb_pvalue_lag14 = round(float(lb["lb_pvalue"].iloc[1]), 4)
    lb_stat_lag7    = round(float(lb["lb_stat"].iloc[0]), 2)
    lb_stat_lag14   = round(float(lb["lb_stat"].iloc[1]), 2)

    # --- Naiv baselineprognose ---
    # Siste observerte verdi brukes som prognose for alle 7 steg
    naive_fc   = np.full(FORECAST_DAYS, train[-1])
    naive_mape = float(np.mean(
        np.abs((test - naive_fc) / np.where(test == 0, 1, test))
    ) * 100)

    result = {
        "arima_order":          str(model.order),
        "seasonal_order":       str(model.seasonal_order),
        "aic":                  round(model.aic(), 2),
        "validation_mape_pct":  round(mape, 1),
        "naive_baseline_mape_pct": round(naive_mape, 1),
        "ljung_box_lag7_stat":  lb_stat_lag7,
        "ljung_box_lag7_pvalue": lb_pvalue_lag7,
        "ljung_box_lag14_stat": lb_stat_lag14,
        "ljung_box_lag14_pvalue": lb_pvalue_lag14,
        "forecast_daily":       [round(v, 1) for v in fc.tolist()],
        "forecast_sum_7d":      round(fc_sum, 0),
        "forecast_ci_lower_7d": round(float(ci[:, 0].sum()), 0),
        "forecast_ci_upper_7d": round(fc_upper, 0),
        "safety_stock":         round(safety_stock, 0),
        "recommended_order_7d": round(recommended, 0),
        "actual_last_7d":       [int(v) for v in test.tolist()],
        "service_level":        SERVICE_LEVEL,
    }

    return result, train, test, fc, ci


# ---------------------------------------------------------------------------
# Plott
# ---------------------------------------------------------------------------
def make_plot(store, product, train, test, fc, ci, info):
    n  = len(train)
    xt = range(1, n + 1)
    xf = range(n + 1, n + FORECAST_DAYS + 1)

    fig, ax = plt.subplots(figsize=(13, 4))

    ax.plot(xt, train, color="#4C72B0", lw=0.9, label="Historisk salg (treningsdata)")
    ax.plot(xf, test,  color="#555555", lw=1.5, ls="--", label="Faktisk salg (validering)")
    ax.plot(xf, fc,    color="#DD8452", lw=2,   marker="o", ms=4, label="SARIMA-prognose")
    ax.fill_between(
        xf, ci[:, 0], ci[:, 1],
        color="#DD8452", alpha=0.2,
        label=f"{int(SERVICE_LEVEL*100)} % prediksjonsintervall",
    )

    title = (
        f"{store} – {product}  |  "
        f"SARIMA{info['arima_order']}×{info['seasonal_order']}  |  "
        f"AIC = {info['aic']}  |  "
        f"MAPE = {info['validation_mape_pct']} %  |  "
        f"Naiv = {info['naive_baseline_mape_pct']} %"
    )
    ax.set_title(title, fontsize=9.5)
    ax.set_xlabel("Dag")
    ax.set_ylabel("Salgsvolum")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
    ax.legend(fontsize=8, loc="upper left")
    ax.grid(True, alpha=0.25)

    plt.tight_layout()
    out = os.path.join(PLOTS_DIR, f"{store}_{product.replace(' ', '_')}.png")
    plt.savefig(out, dpi=130)
    plt.close()


# ---------------------------------------------------------------------------
# Sammendragstabell per butikk
# ---------------------------------------------------------------------------
def summary_table(store: str, store_results: dict) -> str:
    lines = [
        f"\n{'='*90}",
        f"  {store} – Anbefalt bestilling neste 7 dager (servicegrad {int(SERVICE_LEVEL*100)} %)",
        f"{'='*90}",
        f"  {'Produkt':<12} {'Prognose':>10} {'Sikkerl.':>10} {'Bestilling':>10} "
        f"{'MAPE%':>7} {'Naiv%':>7}  {'LB-p(7)':>9}  Modell",
        f"  {'-'*86}",
    ]
    for p, r in store_results.items():
        lb_flag = "*" if r["ljung_box_lag7_pvalue"] < 0.05 else " "
        lines.append(
            f"  {p:<12} {r['forecast_sum_7d']:>10,.0f} "
            f"{r['safety_stock']:>10,.0f} "
            f"{r['recommended_order_7d']:>10,.0f} "
            f"{r['validation_mape_pct']:>7.1f} "
            f"{r['naive_baseline_mape_pct']:>7.1f}  "
            f"{r['ljung_box_lag7_pvalue']:>8.4f}{lb_flag}  "
            f"SARIMA{r['arima_order']}×{r['seasonal_order']}"
        )
    lines.append(f"  {'*'} = LB p < 0.05: mulig gjenværende autokorrelasjon i residualene")
    lines.append(f"{'='*90}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Kjøring
# ---------------------------------------------------------------------------
def main():
    all_results = {}

    for store in STORES:
        print(f"\n>>> Behandler {store} ...")
        data = load_store(store)
        all_results[store] = {}

        for product in PRODUCTS:
            if product not in data:
                continue
            try:
                info, train, test, fc, ci = fit_and_forecast(
                    data[product], store, product
                )
                all_results[store][product] = info
                make_plot(store, product, train, test, fc, ci, info)
                print(
                    f"  {product:<12} SARIMA{info['arima_order']}×{info['seasonal_order']}"
                    f"  AIC={info['aic']:>8.1f}  MAPE={info['validation_mape_pct']:>5.1f}%"
                    f"  Naiv={info['naive_baseline_mape_pct']:>5.1f}%"
                    f"  LB-p7={info['ljung_box_lag7_pvalue']:.4f}"
                    f"  bestilling={info['recommended_order_7d']:>8,.0f}"
                )
            except Exception as e:
                print(f"  {product:<12} FEIL: {e}")

        print(summary_table(store, all_results[store]))

    # Lagre resultater
    with open(RESULTS_FILE, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)

    print(f"\nResultater lagret: {RESULTS_FILE}")
    print(f"Plott lagret:      {PLOTS_DIR}/")


if __name__ == "__main__":
    main()
