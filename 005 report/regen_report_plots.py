"""
Regenererer kun de to SARIMA-plottene som brukes i rapporten:
  HK_French.png og MH_French.png
Raskere enn å kjøre hele sarima_model.py.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from sarima_model import load_store, fit_and_forecast, make_plot

for store, product in [("HK", "French"), ("MH", "French")]:
    print(f"Fitter {store} {product} ...")
    data = load_store(store)
    info, train, test, fc, ci = fit_and_forecast(data[product], store, product)
    make_plot(store, product, train, test, fc, ci, info)
    print(f"  Lagret: {store}_{product}.png")

print("Ferdig.")
