"""
BiteBurst – Supplementære visualiseringer for rapport
======================================================
Genererer fire figurer:

  fig_acf_pacf.png          – ACF og PACF for HK Pommes frites        (Figur 1)
  fig1_french_tidsserie.png – Pommes frites tidsserie, alle utsalgssteder (Figur 2)
  fig_residuals.png         – Residualdiagnostikk for LM Hamburger     (Figur 5)
  fig2_anbefalt_bestilling.png – Stablet søylediagram, alle anbefalinger (Figur 6)
"""

import csv
import json
import os
import sys
import warnings

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as mticker
import numpy as np
from scipy.stats import norm, shapiro
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

warnings.filterwarnings("ignore")

BASE_DIR     = os.path.dirname(os.path.abspath(__file__))
DATA_DIR     = os.path.join(BASE_DIR, "..", "004 data")
PLOTS_DIR    = os.path.join(BASE_DIR, "plots")
RESULTS_FILE = os.path.join(BASE_DIR, "sarima_results.json")

os.makedirs(PLOTS_DIR, exist_ok=True)

STORES   = ["GM", "HK", "LM", "MH"]
PRODUCTS = ["Pizza", "Salad", "French", "Burger", "Hotdog", "Soda", "Ice Cream", "Kebaba"]

PRODUCT_LABELS = {
    "Pizza": "Pizza", "Salad": "Salat", "French": "Pommes frites",
    "Burger": "Hamburger", "Hotdog": "Pølse", "Soda": "Brus",
    "Ice Cream": "Iskrem", "Kebaba": "Kebab",
}
STORE_COLORS = {
    "GM": "#4C72B0", "HK": "#DD8452", "LM": "#55A868", "MH": "#C44E52",
}

fmt_int = mticker.FuncFormatter(lambda x, _: f"{int(x):,}".replace(",", " "))


def load_series(store: str, product: str) -> list[int]:
    path = os.path.join(DATA_DIR, f"BiteBurst {store}.csv")
    with open(path, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f, delimiter=";"))
    return [int(r[product].strip()) for r in rows
            if r.get(product, "").strip().lstrip("-").isdigit()]


# ---------------------------------------------------------------------------
# Figur 1 – ACF og PACF for HK Pommes frites
# ---------------------------------------------------------------------------
print("Genererer Figur 1: ACF/PACF ...")

hk_french = np.array(load_series("HK", "French"), dtype=float)
# Første-ordens differanse for å vise stasjonær ACF/PACF (d=1 valgt av auto_arima)
hk_diff = np.diff(hk_french)

fig, axes = plt.subplots(2, 1, figsize=(14, 8))

plot_acf(hk_diff, lags=28, ax=axes[0], alpha=0.05,
         color="#4C72B0", vlines_kwargs={"colors": "#4C72B0"})
axes[0].set_title("Autokorrelasjonsfunksjon (ACF) – differensiert serie", fontsize=13)
axes[0].set_xlabel("Lag (dager)", fontsize=12)
axes[0].set_ylabel("ACF", fontsize=12)
axes[0].axvline(x=7,  color="#C44E52", ls="--", lw=1.4, label="Lag 7 (ukessyklus)")
axes[0].axvline(x=14, color="#C44E52", ls="--", lw=1.4, alpha=0.5)
axes[0].axvline(x=21, color="#C44E52", ls="--", lw=1.4, alpha=0.3)
axes[0].legend(fontsize=11)
axes[0].grid(True, alpha=0.25)

plot_pacf(hk_diff, lags=28, ax=axes[1], alpha=0.05, method="ywm",
          color="#4C72B0", vlines_kwargs={"colors": "#4C72B0"})
axes[1].set_title("Partiell autokorrelasjonsfunksjon (PACF) – differensiert serie", fontsize=13)
axes[1].set_xlabel("Lag (dager)", fontsize=12)
axes[1].set_ylabel("PACF", fontsize=12)
axes[1].axvline(x=7,  color="#C44E52", ls="--", lw=1.4, label="Lag 7 (ukessyklus)")
axes[1].axvline(x=14, color="#C44E52", ls="--", lw=1.4, alpha=0.5)
axes[1].axvline(x=21, color="#C44E52", ls="--", lw=1.4, alpha=0.3)
axes[1].legend(fontsize=11)
axes[1].grid(True, alpha=0.25)

fig.suptitle("Pommes frites – Hell's Kitchen (førstedifferensiert serie)",
             fontsize=14, fontweight="bold", y=1.01)
plt.tight_layout()
out_acf = os.path.join(PLOTS_DIR, "fig_acf_pacf.png")
plt.savefig(out_acf, dpi=180, bbox_inches="tight")
plt.close()
print(f"  Lagret: {out_acf}")


# ---------------------------------------------------------------------------
# Figur 2 – Pommes frites: rullerende 7-dagers salg, alle utsalgssteder
# ---------------------------------------------------------------------------
print("Genererer Figur 2: Pommes frites tidsserie ...")

fig, ax = plt.subplots(figsize=(16, 7))

all_french = {}
for store in STORES:
    vals = load_series(store, "French")
    all_french[store] = vals
    days = list(range(1, len(vals) + 1))
    ax.plot(days, vals, color=STORE_COLORS[store], lw=1.8, label=store)

# V1-valideringssone (dag 88–94): lys grå
ax.axvspan(87.5, 94.5, color="#cccccc", alpha=0.40, zorder=0, label="V1-validering (dag 88–94)")
# V2-valideringssone (dag 95–101): mørkere grå
ax.axvspan(94.5, 101.5, color="#aaaaaa", alpha=0.40, zorder=0, label="V2-validering (dag 95–101)")
ax.axvline(x=87.5, color="#999999", ls=":", lw=1.0)
ax.axvline(x=94.5, color="#666666", ls="--", lw=1.2)

# Bedre y-akse: ikke start på 0
all_vals_flat = [v for vals in all_french.values() for v in vals]
ax.set_ylim(min(all_vals_flat) * 0.88, max(all_vals_flat) * 1.06)

ax.set_xlabel("Dag", fontsize=13)
ax.set_ylabel("Enheter (rullerende 7-dagers sum)", fontsize=13)
ax.set_title("Pommes frites – rullerende 7-dagers salg per utsalgssted",
             fontsize=14, fontweight="bold")
ax.set_xlim(1, 101)
ax.yaxis.set_major_formatter(fmt_int)
ax.tick_params(axis="both", labelsize=12)
ax.legend(fontsize=12, loc="upper left", ncol=2)
ax.grid(True, alpha=0.25)

plt.tight_layout()
out1 = os.path.join(PLOTS_DIR, "fig1_french_tidsserie.png")
plt.savefig(out1, dpi=180)
plt.close()
print(f"  Lagret: {out1}")


# ---------------------------------------------------------------------------
# Figur 5 – Residualdiagnostikk for LM Hamburger
# ---------------------------------------------------------------------------
print("Genererer Figur 5: Residualer (krever modell-fitting) ...")

sys.path.insert(0, BASE_DIR)
from sarima_model import load_store, fit_and_forecast
from pmdarima import auto_arima

gm_data = load_store("GM")
gm_soda = np.array(gm_data["Soda"], dtype=float)
train_s = gm_soda[:-7]

# GM Brus: SARIMA(2,0,0)(2,0,0,7) – d=0 gir rene initialresidualer
model_s = auto_arima(
    train_s,
    start_p=0, max_p=3, start_q=0, max_q=3, d=None,
    seasonal=True, m=7,
    start_P=0, max_P=2, start_Q=0, max_Q=2, D=None,
    information_criterion="aic", stepwise=True,
    suppress_warnings=True, error_action="ignore", trace=False,
)
residuals = model_s.resid()
std_resid  = (residuals - residuals.mean()) / residuals.std()
n_res = len(std_resid)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 5))

# Panel 1: Standardiserte residualer over tid
ax1.plot(range(1, n_res + 1), std_resid, color="#4C72B0", lw=1.0)
ax1.axhline(0,    color="#333333", lw=0.8, ls="-")
ax1.axhline( 2.0, color="#C44E52", lw=0.8, ls="--", alpha=0.7, label="±2 std.avvik")
ax1.axhline(-2.0, color="#C44E52", lw=0.8, ls="--", alpha=0.7)
ax1.set_title("Standardiserte residualer over tid", fontsize=13)
ax1.set_xlabel("Observasjon", fontsize=12)
ax1.set_ylabel("Standardiserte residualer", fontsize=12)
ax1.legend(fontsize=11)
ax1.grid(True, alpha=0.25)
ax1.tick_params(labelsize=11)

# Panel 2: ACF av residualer (skal vise hvit støy)
plot_acf(residuals, lags=21, ax=ax2, alpha=0.05,
         color="#4C72B0", vlines_kwargs={"colors": "#4C72B0"})
ax2.axvline(x=7,  color="#C44E52", ls="--", lw=1.2, alpha=0.6, label="Lag 7")
ax2.axvline(x=14, color="#C44E52", ls="--", lw=1.2, alpha=0.4)
ax2.set_title("ACF av residualer", fontsize=13)
ax2.set_xlabel("Lag (dager)", fontsize=12)
ax2.set_ylabel("ACF", fontsize=12)
ax2.legend(fontsize=11)
ax2.grid(True, alpha=0.25)
ax2.tick_params(labelsize=11)

fig.suptitle("Brus – Garment District  |  Residualdiagnostikk",
             fontsize=14, fontweight="bold")
plt.tight_layout()
out_res = os.path.join(PLOTS_DIR, "fig_residuals.png")
plt.savefig(out_res, dpi=180)
plt.close()
print(f"  Lagret: {out_res}")


# ---------------------------------------------------------------------------
# Figur 7 – Residualhistogram: GM Brus (stabil) vs. MH Pommes frites (volatil)
# ---------------------------------------------------------------------------
print("Genererer Figur 7: Residualhistogram ...")

# GM Brus: gjenbruk model_s fra Figur 5
resid_gm_soda = model_s.resid()
std_gm_soda = (resid_gm_soda - resid_gm_soda.mean()) / resid_gm_soda.std()
_, sw_p_gm = shapiro(std_gm_soda)

# MH Pommes frites: tilpass ny modell
mh_data = load_store("MH")
mh_french = np.array(mh_data["French"], dtype=float)
train_mh_f = mh_french[:-7]
model_mh_f = auto_arima(
    train_mh_f,
    start_p=0, max_p=3, start_q=0, max_q=3, d=None,
    seasonal=True, m=7,
    start_P=0, max_P=2, start_Q=0, max_Q=2, D=None,
    information_criterion="aic", stepwise=True,
    suppress_warnings=True, error_action="ignore", trace=False,
)
resid_mh_french = model_mh_f.resid()
std_mh_french = (resid_mh_french - resid_mh_french.mean()) / resid_mh_french.std()
_, sw_p_mh = shapiro(std_mh_french)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 5))

for ax, std_r, label, sw_p in [
    (ax1, std_gm_soda,   "Brus – Garment District",    sw_p_gm),
    (ax2, std_mh_french, "Pommes frites – Murray Hill", sw_p_mh),
]:
    x_range = np.linspace(std_r.min() - 0.5, std_r.max() + 0.5, 200)
    ax.hist(std_r, bins=15, density=True, color="#4C72B0", alpha=0.65,
            edgecolor="white", label="Standardiserte residualer")
    ax.plot(x_range, norm.pdf(x_range), color="#C44E52", lw=2.0, label="N(0, 1)")
    ax.set_title(label, fontsize=13, fontweight="bold")
    ax.set_xlabel("Standardiserte residualer", fontsize=12)
    ax.set_ylabel("Tetthet", fontsize=12)
    ax.annotate(f"Shapiro-Wilk  p = {sw_p:.3f}", xy=(0.97, 0.95),
                xycoords="axes fraction", ha="right", va="top", fontsize=11,
                color="#333333",
                bbox=dict(boxstyle="round,pad=0.3", fc="white", alpha=0.85, ec="#cccccc"))
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.25)
    ax.tick_params(labelsize=11)

fig.suptitle("Residualfordeling – normalitetssjekk for to kontrasterende kombinasjoner",
             fontsize=14, fontweight="bold")
plt.tight_layout()
out_hist = os.path.join(PLOTS_DIR, "fig_residual_hist.png")
plt.savefig(out_hist, dpi=180)
plt.close()
print(f"  Lagret: {out_hist}")
print(f"  Shapiro-Wilk: GM Brus p={sw_p_gm:.4f}  |  MH Pommes frites p={sw_p_mh:.4f}")


# ---------------------------------------------------------------------------
# Figur 6 – Anbefalt ukentlig bestilling: stablet søylediagram
# ---------------------------------------------------------------------------
print("Genererer Figur 6: Anbefalt bestilling ...")

with open(RESULTS_FILE, encoding="utf-8") as f:
    results = json.load(f)

fig, axes = plt.subplots(2, 2, figsize=(18, 12))
axes = axes.flatten()

COLOR_FC = "#4C72B0"
COLOR_SS = "#DD8452"
x = np.arange(len(PRODUCTS))
prod_labels = [PRODUCT_LABELS[p].replace(" ", "\n") if len(PRODUCT_LABELS[p]) > 8
               else PRODUCT_LABELS[p] for p in PRODUCTS]

for idx, store in enumerate(STORES):
    ax = axes[idx]
    prognose = [results[store][p]["forecast_sum_7d"] for p in PRODUCTS]
    safety   = [results[store][p]["safety_stock"]    for p in PRODUCTS]
    mapes    = [results[store][p]["validation_mape_pct"] for p in PRODUCTS]

    ax.bar(x, prognose, color=COLOR_FC, width=0.6, label="Prognose 7d")
    ax.bar(x, safety,   color=COLOR_SS, width=0.6, bottom=prognose,
           label="Sikkerhetslager")

    # Totalt beløp over søyle; marker høy-MAPE-produkter med stjerne
    for xi, (fc, ss, mape) in enumerate(zip(prognose, safety, mapes)):
        label = f"{int(fc+ss):,}".replace(",", " ")
        if mape > 15:
            label += " *"
        ax.text(xi, fc + ss + 15, label,
                ha="center", va="bottom", fontsize=9, color="#333333")

    ax.set_title(store, fontsize=14, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(prod_labels, fontsize=11)
    ax.set_ylabel("Enheter per uke", fontsize=12)
    ax.tick_params(axis="y", labelsize=11)
    ax.yaxis.set_major_formatter(fmt_int)
    ax.grid(True, axis="y", alpha=0.25)

handles = [
    mpatches.Patch(color=COLOR_FC, label="Prognose 7d"),
    mpatches.Patch(color=COLOR_SS, label="Sikkerhetslager (95 % servicegrad)"),
]
fig.legend(handles=handles, loc="lower center", ncol=2, fontsize=12, frameon=True)
fig.text(0.5, 0.01,
         "* MAPE > 15 % i V2-valideringsvinduet – anbefalt ordre bør justeres manuelt",
         ha="center", fontsize=10, color="#555555")
fig.suptitle("Anbefalt ukentlig bestilling per produkt per utsalgssted (95 % servicegrad)",
             fontsize=14, fontweight="bold")
plt.tight_layout(rect=[0, 0.07, 1, 0.97])

out2 = os.path.join(PLOTS_DIR, "fig2_anbefalt_bestilling.png")
plt.savefig(out2, dpi=180)
plt.close()
print(f"  Lagret: {out2}")

print("\nAlle figurer generert.")
