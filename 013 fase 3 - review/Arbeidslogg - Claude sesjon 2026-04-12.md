# Arbeidslogg – Claude-sesjon 12. april 2026

## Hva ble gjort i denne sesjonen

### 1. Konvertert mal til Markdown
- `000 templates/Mal prosjekt LOG650 v2.docx` → `000 templates/Mal prosjekt LOG650 v2.md`

### 2. Lest og forstått prosjektdokumentene
- **Proposal:** `011 fase 1 - proposal/Proposal LOG650 - G14 Kjetil individuell.md`
- **Prosjektplan:** `012 fase 2 - plan/BiteBurst Lageroptimalisering Prosjektplan LOG650.md`
- **Rapportmal:** `013 fase 3 - review/Rapport prosjekt LOG650 v2.md`

### 3. Generert core.json og requirements.json
Plassert i `005 report/`:
- **core.json** – prosjektinfo, simuleringsoppsett, salgstatistikk (mean/stdev/min/max) for alle 5 datakilder × 8 produkter
- **requirements.json** – krav K1–K7 med status, notater og datakvalitetsflagg

### 4. Datarensing og kvalitetssikring
Gjennomgått alle CSV-filer i `004 data/`:

**Identifiserte og rettede feil (av Kjetil):**
| Fil | Produkt | Problem |
|-----|---------|---------|
| LM | French | Ekstremverdi 23 330 (rettet) |
| LM | Kebaba | Ekstremverdi 22 360 (rettet) |
| HK | Hotdog | Ekstremverdi 18 235 (rettet) |
| GM | Kebaba | Minimumverdi 184 – trolig tastefeil (rettet) |
| MH | Kebaba | Minimumverdi 198 – trolig tastefeil (rettet) |
| GM | French | Minimumverdi 356 – trolig tastefeil (rettet) |
| HK | Kebaba | Dag 86 = 4 357 (z=8,0) – isolert utligger (rettet) |
| MH | Pizza | Dag 90 = 1 334 (z=3,9) – sjekket og rettet |

**Bekreftet korrekt:**
- Warehouse-topper dag 1–3 (Pizza, Soda, Ice Cream): innledende opplasting av lager ✓
- Warehouse dag 7 (Salad = 5 631, Kebaba = 10 929): bekreftet korrekt av Kjetil ✓
- Alle dagsrekker normalisert til dag 1–101 av Kjetil ✓

**Oppdaterte core.json og requirements.json** med korrigerte statistikker og K5-status endret til «Oppfylt».

### 5. EDA – ukesdageffekter og stasjonæritet
**Funn:**
- Ukesdageffektene i aggregerte tall er 0–3,5 % spread per produkt – men:
- ADF-test: de fleste serier er **ikke-stasjonære** → d=1 nødvendig
- ACF lag 1: ekstremt høy (0,77–0,99) for alle produkter → sterk autokorrelasjon
- ACF lag 7: signifikant (|r| > 0,2) for French, Hotdog, Kebaba, Salad på tvers av butikker → ukesssyklus eksisterer
- **Kjetil bekreftet:** onsdag lavest salg, lørdag høyest – prosjektplanens antagelse om «ingen sesongvariasjoner» var feil og skal korrigeres i rapporten

### 6. SARIMA-modellering
**Modellvalg:** SARIMA(p,d,q)(P,D,Q,7) via `auto_arima` fra pmdarima  
**Script:** `005 report/sarima_model.py`

**Resultater (32 modeller – alle 8 produkter × 4 butikker):**
- Lagret i `005 report/sarima_results.json`
- Plott lagret i `005 report/plots/` (32 PNG-filer)

**MAPE-oversikt (validering siste 7 dager):**

| Butikk | Beste | Svakeste | Kommentar |
|--------|-------|----------|-----------|
| GM | Kebaba 1,1% / Soda 1,3% | Hotdog 19,9% / French 16,0% | French og Hotdog har høy stdev |
| HK | Pizza 0,8% / Burger 0,8% | Salad 15,7% | |
| LM | Burger 0,8% / French 2,0% | Hotdog 7,3% | Beste butikk totalt |
| MH | Soda 0,8% | French 21,6% / Salad 16,4% | MH har mest oppadgående trend |

**Alle modeller fikk sesongkomponent (m=7)** – bekrefter at ukessyklus er statistisk relevant.

### 7. Presisering av problemstilling
Kjetil klargjorde at fokus er på **butikknivå**, ikke warehouse:
- Spørsmålet er: *Hvor mye varer må hvert utsalgssted ha på eget lager for å holde åpent i 7 dager uten levering fra sentrallager?*
- Svaret er direkte fra modellen: `recommended_order_7d` per produkt per butikk
  - = `forecast_sum_7d` (7-dagers etterspørselsprognose) + `safety_stock` (95 % servicegrad)

---

## Status ved sesjonsslutt

| Leveranse | Status |
|-----------|--------|
| Proposal | ✅ Ferdig |
| Prosjektplan | ✅ Ferdig |
| Datainnsamling og rensing | ✅ Ferdig |
| core.json / requirements.json | ✅ Ferdig |
| SARIMA-modellering | ✅ Ferdig |
| Rapport (Rapport prosjekt LOG650 v2.md) | ⏳ Ikke påbegynt |

---

## Neste steg

Begynne å fylle ut rapporten kapittel for kapittel.  
Naturlig startpunkt: **forside → egenerklæring → innledning → problemstilling → avgrensninger**,  
siden disse bygger direkte på proposal og prosjektplan.

Kapitler med mye innhold å hente fra eksisterende materiale:
- Casebeskrivelse → fra prosjektplan (BiteBurst / Big Ambitions)
- Metode og data → SARIMA-valg begrunnet av ADF/ACF-analyse
- Modellering → auto_arima, formler, parametre fra sarima_results.json
- Analyse + Resultat → direkte fra sarima_results.json og plottene
- Diskusjon → MAPE-analyse, ukesdagseffekt vs. prosjektplanantagelse, begrensninger

---

## Nøkkelfiler

```
004 data/
  BiteBurst GM.csv          Salgsdata, dag 1-101, 8 produkter
  BiteBurst HK.csv          Salgsdata, dag 1-101, 8 produkter
  BiteBurst LM.csv          Salgsdata, dag 1-101, 8 produkter
  BiteBurst MH.csv          Salgsdata, dag 1-101, 8 produkter
  BiteBurst Warehouse.csv   Lagerdata, dag 1-101, 8 produkter

005 report/
  core.json                 Prosjektkjerne og oppdatert statistikk
  requirements.json         Krav K1-K7 med status
  sarima_model.py           Python-script for SARIMA-modellering
  sarima_results.json       Resultater: prognose, sikkerhetslager, anbefaling
  plots/                    32 PNG-plott (ett per produkt per butikk)

013 fase 3 - review/
  Rapport prosjekt LOG650 v2.md   Rapportmal – skal fylles ut
  Arbeidslogg - Claude sesjon 2026-04-12.md   Denne filen
```
