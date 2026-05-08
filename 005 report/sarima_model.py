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
    Rolling-origin validering med to vinduer:
      W1: treningsdata dag 1-87, validering dag 88-94
      W2: treningsdata dag 1-94, validering dag 95-101  (primær, brukes til anbefalinger)
    Tilpasser SARIMA automatisk med auto_arima (sesong s=7) for hvert vindu.
    Beregner Ljung-Box residualdiagnostikk og naiv baseline-MAPE.
    Returnerer (result_dict, train_w2, test_w2, fc_w2, ci_w2).
    """
    arr = np.array(series, dtype=float)

    # Primær trenings-/valideringssplit (W2): dag 1-94 / dag 95-101
    train = arr[:-FORECAST_DAYS]
    test  = arr[-FORECAST_DAYS:]

    # Ekstra valideringsvindu (W1): dag 1-87 / dag 88-94
    train_w1 = arr[:-2 * FORECAST_DAYS]
    test_w1  = arr[-2 * FORECAST_DAYS:-FORECAST_DAYS]

    arima_kwargs = dict(
        start_p=0, max_p=3,
        start_q=0, max_q=3,
        d=None,
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

    # --- Primær modell (W2) ---
    model = auto_arima(train, **arima_kwargs)
    fc, ci = model.predict(
        n_periods=FORECAST_DAYS,
        return_conf_int=True,
        alpha=1 - SERVICE_LEVEL,
    )
    fc = np.maximum(fc, 0)

    # --- Ekstra modell (W1) – kun for MAPE-beregning ---
    model_w1 = auto_arima(train_w1, **arima_kwargs)
    fc_w1, _ = model_w1.predict(
        n_periods=FORECAST_DAYS,
        return_conf_int=True,
        alpha=1 - SERVICE_LEVEL,
    )
    fc_w1 = np.maximum(fc_w1, 0)

    # --- Nøkkeltall fra primær modell ---
    fc_sum   = float(fc[-1])
    fc_upper = float(ci[-1, 1])
    safety_stock = max(fc_upper - fc_sum, 0)
    recommended  = fc_sum + safety_stock

    # --- MAPE per vindu og gjennomsnitt ---
    mape_w2  = float(np.mean(np.abs((test    - fc)    / np.where(test    == 0, 1, test)))    * 100)
    mape_w1  = float(np.mean(np.abs((test_w1 - fc_w1) / np.where(test_w1 == 0, 1, test_w1))) * 100)
    mape_avg = (mape_w1 + mape_w2) / 2

    # --- Ljung-Box residualdiagnostikk (primær modell) ---
    residuals = model.resid()
    lb = acorr_ljungbox(residuals, lags=[7, 14], return_df=True)
    lb_pvalue_lag7  = round(float(lb["lb_pvalue"].iloc[0]), 4)
    lb_pvalue_lag14 = round(float(lb["lb_pvalue"].iloc[1]), 4)
    lb_stat_lag7    = round(float(lb["lb_stat"].iloc[0]), 2)
    lb_stat_lag14   = round(float(lb["lb_stat"].iloc[1]), 2)

    # --- Naiv baselineprognose (W2) ---
    naive_fc   = np.full(FORECAST_DAYS, train[-1])
    naive_mape = float(np.mean(
        np.abs((test - naive_fc) / np.where(test == 0, 1, test))
    ) * 100)

    result = {
        "arima_order":               str(model.order),
        "seasonal_order":            str(model.seasonal_order),
        "aic":                       round(model.aic(), 2),
        "validation_mape_pct":       round(mape_w2, 1),       # W2: dag 95-101
        "validation_mape_w1_pct":    round(mape_w1, 1),       # W1: dag 88-94
        "rolling_mape_avg_pct":      round(mape_avg, 1),      # gjennomsnitt W1+W2
        "naive_baseline_mape_pct":   round(naive_mape, 1),
        "ljung_box_lag7_stat":       lb_stat_lag7,
        "ljung_box_lag7_pvalue":     lb_pvalue_lag7,
        "ljung_box_lag14_stat":      lb_stat_lag14,
        "ljung_box_lag14_pvalue":    lb_pvalue_lag14,
        "forecast_daily":            [round(v, 1) for v in fc.tolist()],
        "forecast_sum_7d":           round(fc_sum, 0),
        "forecast_ci_lower_7d":      round(float(ci[:, 0].sum()), 0),
        "forecast_ci_upper_7d":      round(fc_upper, 0),
        "safety_stock":              round(safety_stock, 0),
        "recommended_order_7d":      round(recommended, 0),
        "actual_last_7d":            [int(v) for v in test.tolist()],
        "service_level":             SERVICE_LEVEL,
    }

    return result, train, test, fc, ci


# Norske produktnavn for plott-titler
_PRODUCT_LABELS = {
    "Pizza": "Pizza", "Salad": "Salat", "French": "Pommes frites",
    "Burger": "Hamburger", "Hotdog": "Pølse", "Soda": "Brus",
    "Ice Cream": "Iskrem", "Kebaba": "Kebab",
}
_STORE_NAMES = {
    "GM": "Garment District", "HK": "Hell's Kitchen",
    "LM": "Lower Manhattan",  "MH": "Murray Hill",
}

# ---------------------------------------------------------------------------
# Plott
# ---------------------------------------------------------------------------
def make_plot(store, product, train, test, fc, ci, info):
    prod_label  = _PRODUCT_LABELS.get(product, product)
    store_label = _STORE_NAMES.get(store, store)

    n  = len(train)
    xt = range(1, n + 1)
    xf = range(n + 1, n + FORECAST_DAYS + 1)

    all_vals = np.concatenate([train, test, fc])
    ymin = min(all_vals) * 0.93
    ymax = max(all_vals) * 1.08

    fig, ax = plt.subplots(figsize=(16, 6))

    # Valideringssone: grå bakgrunn for V2 (dag 95-101)
    ax.axvspan(n + 0.5, n + FORECAST_DAYS + 0.5,
               color="#dddddd", alpha=0.45, zorder=0, label="Valideringssone (dag 95–101)")
    ax.axvline(x=n + 0.5, color="#999999", ls=":", lw=1.0)

    ax.plot(xt, train, color="#4C72B0", lw=1.2, label="Historisk salg (treningsdata)")
    ax.plot(xf, test,  color="#333333", lw=2,   ls="--", label="Faktisk salg (validering)")
    ax.plot(xf, fc,    color="#DD8452", lw=2.5, marker="o", ms=6, label="SARIMA-prognose")
    ax.fill_between(
        xf, ci[:, 0], ci[:, 1],
        color="#DD8452", alpha=0.22,
        label=f"{int(SERVICE_LEVEL*100)} % prediksjonsintervall",
    )

    ax.set_title(f"{prod_label} – {store_label}", fontsize=14, fontweight="bold")
    ax.set_xlabel("Dag", fontsize=13)
    ax.set_ylabel("Salgsvolum (rullerende 7-dagers sum)", fontsize=13)
    ax.set_ylim(ymin, ymax)
    ax.tick_params(axis="both", labelsize=12)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
    ax.legend(fontsize=11, loc="upper left")
    ax.grid(True, alpha=0.25)

    # Modellinfo som liten fotnote nederst i figuren
    mape_w1 = info.get("validation_mape_w1_pct", "–")
    mape_w2 = info.get("validation_mape_pct", "–")
    note = (f"SARIMA{info['arima_order']}×{info['seasonal_order']}  "
            f"| AIC = {info['aic']}  "
            f"| MAPE V1 = {mape_w1} %  V2 = {mape_w2} %  "
            f"| Naiv = {info['naive_baseline_mape_pct']} %")
    ax.annotate(note, xy=(0.01, 0.02), xycoords="axes fraction",
                fontsize=9, color="#555555", va="bottom",
                bbox=dict(boxstyle="round,pad=0.3", fc="white", alpha=0.75, ec="none"))

    plt.tight_layout()
    out = os.path.join(PLOTS_DIR, f"{store}_{product.replace(' ', '_')}.png")
    plt.savefig(out, dpi=180)
    plt.close()


# ---------------------------------------------------------------------------
# Sammendragstabell per butikk
# ---------------------------------------------------------------------------
def summary_table(store: str, store_results: dict) -> str:
    lines = [
        f"\n{'='*105}",
        f"  {store} – Anbefalt bestilling neste 7 dager (servicegrad {int(SERVICE_LEVEL*100)} %)",
        f"{'='*105}",
        f"  {'Produkt':<12} {'Prognose':>10} {'Sikkerl.':>10} {'Bestilling':>10} "
        f"{'W1%':>7} {'W2%':>7} {'Snitt%':>7} {'Naiv%':>7}  {'LB-p(7)':>9}  Modell",
        f"  {'-'*101}",
    ]
    for p, r in store_results.items():
        lb_flag = "*" if r["ljung_box_lag7_pvalue"] < 0.05 else " "
        lines.append(
            f"  {p:<12} {r['forecast_sum_7d']:>10,.0f} "
            f"{r['safety_stock']:>10,.0f} "
            f"{r['recommended_order_7d']:>10,.0f} "
            f"{r['validation_mape_w1_pct']:>7.1f} "
            f"{r['validation_mape_pct']:>7.1f} "
            f"{r['rolling_mape_avg_pct']:>7.1f} "
            f"{r['naive_baseline_mape_pct']:>7.1f}  "
            f"{r['ljung_box_lag7_pvalue']:>8.4f}{lb_flag}  "
            f"SARIMA{r['arima_order']}×{r['seasonal_order']}"
        )
    lines.append(f"  W1=dag 88-94  W2=dag 95-101  * = LB p < 0.05")
    lines.append(f"{'='*105}")
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
