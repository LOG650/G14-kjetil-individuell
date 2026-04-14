# Arbeidslogg – Claude-sesjon 14. april 2026

## Hva ble gjort i denne sesjonen

### 1. Fortsatt fra forrige sesjon (12. april)
Sesjonen tok utgangspunkt i arbeidslogen fra 12. april og gjenopptok rapporten der den sto.
Status ved start: Innledning, Casebeskrivelse og Data (Kap. 5.2) var ferdigskrevet. Kap. 3, 5.1, 6, 7 og 8 var stubber.

### 2. Fikset tabellnummerering
Oppdaget og rettet duplikat «Tabell 2» i datarensingseksjonen (kap. 5.2):

| Gammel betegnelse | Ny betegnelse | Innhold |
|-------------------|---------------|---------|
| Tabell 2 (kap 5.2) | Tabell 3 | Identifiserte og korrigerte registreringsfeil |
| Tabell 3 | Tabell 4 | Deskriptiv statistikk – GM |
| Tabell 4 | Tabell 5 | Deskriptiv statistikk – HK |
| Tabell 5 | Tabell 6 | Deskriptiv statistikk – LM |
| Tabell 6 | Tabell 7 | Deskriptiv statistikk – MH |

Tilhørende kryssreferanser i brødtekst ble oppdatert.

### 3. Runde 2 – Skrevet Kap. 3, 5.1, 6, 7 og 8

#### Kap. 3 Teori
- 3.1 Tidsrekker og stasjonæritet (ADF-test, differensiering)
- 3.2 ARIMA-modellen (AR, I, MA med formler)
- 3.3 SARIMA med sesongkomponent (formel, s = 7)
- 3.4 AIC som informasjonskriterium for modellvalg
- 3.5 Sikkerhetslager og servicegrad (klassisk formel + KI-tilnærming)

#### Kap. 5.1 Metode
- Begrunnelse for SARIMA: ADF-test → ikke-stasjonæritet (d = 1), ACF lag-7 signifikant for French, Hotdog, Kebaba, Salad
- Beskrivelse av auto_arima-oppsett (søkerom, AIC, stepwise)
- Trenings-/valideringsopplegg: dag 1–94 trening, dag 95–101 validering
- Sikkerhetslagerformel direkte fra 95 %-konfidensintervall

#### Kap. 6 Modellering
- Matematisk SARIMA-formulering med operator-notasjon
- Beskrivelse av automatisk parametertilpasning
- **Tabell 8**: Komplett oversikt over alle 32 SARIMA-modeller (ordre + AIC)
- Beregningsmetode for sikkerhetslager og anbefalt ordre

#### Kap. 7 Analyse
- **Tabell 9**: MAPE-matrise per produkt × utsalgssted
- 24 av 32 modeller har MAPE < 8 % – vurdert som god prognoseytelse
- Sesongkomponent bekreftet i alle 32 modeller
- French og Hotdog: heterogen ytelse avhengig av utsalgssted
- MH-trendeffekt: oppadgående salgstendens i slutten av observasjonsperioden fanges ikke fullt ut av SARIMA

#### Kap. 8 Resultat
- **Tabell 10**: Anbefalt lagernivå GM – totalt 78 460 enheter/uke
- **Tabell 11**: Anbefalt lagernivå HK – totalt 85 725 enheter/uke
- **Tabell 12**: Anbefalt lagernivå LM – totalt 99 433 enheter/uke
- **Tabell 13**: Anbefalt lagernivå MH – totalt 84 077 enheter/uke
- Oppsummering: Ice Cream og Soda enklest å styre, French fries krever størst sikkerhetslager

---

## Ordtelling ved sesjonsslutt

| Mål | Verdi |
|-----|-------|
| Rå ordtelling (wc -w) | 6 754 |
| Estimert løpende prosaord | ~5 800–6 200 |
| Mål for innlevering | 9 000–11 000 |
| Estimert gjenstår | ~2 500–3 500 |

---

## Status ved sesjonsslutt

| Leveranse | Status |
|-----------|--------|
| Proposal | ✅ Ferdig |
| Prosjektplan | ✅ Ferdig |
| Datainnsamling og rensing | ✅ Ferdig |
| core.json / requirements.json | ✅ Ferdig |
| SARIMA-modellering | ✅ Ferdig |
| Kap. 1 Innledning | ✅ Ferdig |
| Kap. 4 Casebeskrivelse | ✅ Ferdig |
| Kap. 5.2 Data | ✅ Ferdig |
| Kap. 3 Teori | ✅ Ferdig |
| Kap. 5.1 Metode | ✅ Ferdig |
| Kap. 6 Modellering | ✅ Ferdig |
| Kap. 7 Analyse | ✅ Ferdig |
| Kap. 8 Resultat | ✅ Ferdig |
| Kap. 2 Litteratur | ⏳ Runde 3 |
| Kap. 9 Diskusjon | ⏳ Runde 3 |
| Kap. 10 Konklusjon | ⏳ Runde 3 |
| Sammendrag / Abstract | ⏳ Oppdateres sist |

---

## Neste steg – Runde 3

- **Kap. 2 Litteratur** – gjennomgang av relevante studier som benytter SARIMA for etterspørselsprognoser og lageroptimalisering
- **Kap. 9 Diskusjon** – viktigste tema å dekke:
  - MH-trendeffekten og SARIMA-modellens begrensning ved akselererende vekst
  - Simulert vs. reell data – overføringsverdi
  - SARIMA-forutsetninger (normalfordelte feil, stasjonæritet)
  - Alternativ tilnærming (f.eks. eksponentiell utjevning, maskinlæring)
- **Kap. 10 Konklusjon** – besvare problemstillingen direkte, peke på videre arbeid
- Oppdatere Sammendrag/Abstract når alt innhold er på plass

---

## Nøkkelfiler

```
013 fase 3 - review/
  Rapport prosjekt LOG650 v2.md        Hoveddokument – 6 754 råord (14. april)
  Arbeidslogg - Claude sesjon 2026-04-12.md
  Arbeidslogg - Claude sesjon 2026-04-14.md   Denne filen

005 report/
  sarima_results.json                  32 modellresultater
  sarima_model.py                      Python-script
  plots/                               32 PNG-plott
  core.json                            Prosjektkjerne og statistikk
  requirements.json                    Krav K1–K7
```
