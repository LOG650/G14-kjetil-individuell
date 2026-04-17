"""
BiteBurst – Supplementære visualiseringer for rapport
======================================================
Genererer to figurer som ikke produseres av sarima_model.py:

  fig1_french_tidsserie.png   – French fries rullerende 7-dagers salg,
                                alle fire utsalgssteder på samme akse
  fig2_anbefalt_bestilling.png – Stablet søylediagram: prognose +
                                sikkerhetslager per produkt per utsalgssted
"""

import csv
import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as mticker
import numpy as np

BASE_DIR     = os.path.dirname(os.path.abspath(__file__))
DATA_DIR     = os.path.join(BASE_DIR, "..", "004 data")
PLOTS_DIR    = os.path.join(BASE_DIR, "plots")
RESULTS_FILE = os.path.join(BASE_DIR, "sarima_results.json")

STORES   = ["GM", "HK", "LM", "MH"]
PRODUCTS = ["Pizza", "Salad", "French", "Burger", "Hotdog", "Soda", "Ice Cream", "Kebaba"]

STORE_COLORS = {
    "GM": "#4C72B0",
    "HK": "#DD8452",
    "LM": "#55A868",
    "MH": "#C44E52",
}

fmt_int = mticker.FuncFormatter(lambda x, _: f"{int(x):,}".replace(",", " "))


def load_series(store: str, product: str) -> tuple[list[int], list[str]]:
    path = os.path.join(DATA_DIR, f"BiteBurst {store}.csv")
    with open(path, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f, delimiter=";"))
    values  = [int(r[product].strip()) for r in rows
               if r.get(product, "").strip().lstrip("-").isdigit()]
    weekday = [r["Ukedag"] for r in rows]
    return values, weekday


# ---------------------------------------------------------------------------
# Figur 1 – French fries: rullerende 7-dagers salg, alle utsalgssteder
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(13, 5))

for store in STORES:
    vals, _ = load_series(store, "French")
    days = list(range(1, len(vals) + 1))
    ax.plot(days, vals, color=STORE_COLORS[store], lw=1.6, label=store)

# Marker trenings-/valideringsgrense
ax.axvline(x=94.5, color="#888888", ls="--", lw=1.2, label="Trenings-/valideringsgrense (dag 94/95)")
ax.fill_betweenx(
    [0, ax.get_ylim()[1] if ax.get_ylim()[1] > 0 else 4000],
    94.5, 101.5,
    color="#f5f5f5", zorder=0, label="Valideringssett (dag 95–101)"
)

ax.set_xlabel("Dag", fontsize=10)
ax.set_ylabel("Enheter (rullerende 7-dagers sum)", fontsize=10)
ax.set_title(
    "Figur 1: French fries – rullerende 7-dagers salg per utsalgssted",
    fontsize=11, fontweight="bold"
)
ax.yaxis.set_major_formatter(fmt_int)
ax.legend(fontsize=9, loc="upper left")
ax.grid(True, alpha=0.25)
ax.set_xlim(1, 101)

plt.tight_layout()
out1 = os.path.join(PLOTS_DIR, "fig1_french_tidsserie.png")
plt.savefig(out1, dpi=130)
plt.close()
print(f"Lagret: {out1}")


# ---------------------------------------------------------------------------
# Figur 2 – Anbefalt ukentlig bestilling: stablet søylediagram
# ---------------------------------------------------------------------------
with open(RESULTS_FILE, encoding="utf-8") as f:
    results = json.load(f)

fig, axes = plt.subplots(2, 2, figsize=(14, 9))
axes = axes.flatten()

COLOR_FC = "#4C72B0"
COLOR_SS = "#DD8452"
x = np.arange(len(PRODUCTS))
prod_labels = [p if p != "Ice Cream" else "Ice\nCream" for p in PRODUCTS]

for idx, store in enumerate(STORES):
    ax = axes[idx]
    prognose = [results[store][p]["forecast_sum_7d"] for p in PRODUCTS]
    safety   = [results[store][p]["safety_stock"]    for p in PRODUCTS]

    bars1 = ax.bar(x, prognose, color=COLOR_FC, width=0.6, label="Prognose 7d")
    bars2 = ax.bar(x, safety,   color=COLOR_SS, width=0.6,
                   bottom=prognose, label="Sikkerhetslager")

    ax.set_title(store, fontsize=12, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(prod_labels, fontsize=8.5)
    ax.set_ylabel("Enheter per uke", fontsize=9)
    ax.yaxis.set_major_formatter(fmt_int)
    ax.grid(True, axis="y", alpha=0.25)

    # Vis totalt anbefalt ordre over hver søyle
    for xi, (fc, ss) in enumerate(zip(prognose, safety)):
        ax.text(xi, fc + ss + 15, f"{int(fc+ss):,}".replace(",", " "),
                ha="center", va="bottom", fontsize=7, color="#333333")

handles = [
    mpatches.Patch(color=COLOR_FC, label="Prognose 7d"),
    mpatches.Patch(color=COLOR_SS, label="Sikkerhetslager (95 % servicegrad)"),
]
fig.legend(handles=handles, loc="lower center", ncol=2, fontsize=10, frameon=True)
fig.suptitle(
    "Figur 2: Anbefalt ukentlig bestilling per produkt per utsalgssted (95 % servicegrad)",
    fontsize=12, fontweight="bold"
)
plt.tight_layout(rect=[0, 0.06, 1, 0.97])

out2 = os.path.join(PLOTS_DIR, "fig2_anbefalt_bestilling.png")
plt.savefig(out2, dpi=130)
plt.close()
print(f"Lagret: {out2}")
