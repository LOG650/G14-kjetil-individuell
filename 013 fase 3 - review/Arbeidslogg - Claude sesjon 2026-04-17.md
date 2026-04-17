# Arbeidslogg – Claude-sesjon 17. april 2026

## Hva ble gjort i denne sesjonen

### 1. Fortsatt fra forrige sesjon (14. april)
Sesjonen tok utgangspunkt i arbeidslogen fra 14. april og gjenopptok rapporten der den sto.
Status ved start: Kap. 2 (Litteratur), 9 (Diskusjon) og 10 (Konklusjon) var stubber.

### 2. Skrevet Kap. 2 Litteratur

#### Kap. 2 Litteratur
- 2.1 ARIMA og SARIMA i etterspørselsprognoser (Box et al., Hyndman & Athanasopoulos, auto_arima)
- 2.2 Lagerstyring og sikkerhetslager (Silver et al., Chopra & Meindl)
- 2.3 Integrering av prognose og lagerstyring – KI-basert sikkerhetslager som alternativ til generisk σ-tilnærming

### 3. Skrevet Kap. 9 Diskusjon

#### Kap. 9 Diskusjon
- 9.1 Modellnøyaktighet og praktisk implikasjon (24/32 < 8 % MAPE)
- 9.2 SARIMA-modellens begrensning ved trendende etterspørsel (MH-effekten)
- 9.3 Heterogen modellytelse for French fries og Hotdog
- 9.4 Sikkerhetslagerberegningens validitet (normalfordelingsantagelsen)
- 9.5 Simuleringens overføringsverdi til reelle data (metodikk vs. data)
- 9.6 Alternative metoder (Holt-Winters, SARIMAX, maskinlæring)

### 4. Skrevet Kap. 10 Konklusjon
- Direkte svar på problemstillingens to delspørsmål
- Konkrete lagertall oppsummert per utsalgssted
- Forbehold om MH og trendeffekten
- Videre arbeid: reelle data, SARIMAX, rullerende treningsvindu

---

## Ordtelling ved sesjonsslutt

| Mål | Verdi |
|-----|-------|
| Rå ordtelling (wc -w) | 8 691 |
| Estimert løpende prosaord | ~7 400–7 800 |
| Mål for innlevering | 9 000–11 000 |
| Estimert gjenstår | ~1 000–2 500 |

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
| Kap. 2 Litteratur | ✅ Ferdig |
| Kap. 9 Diskusjon | ✅ Ferdig |
| Kap. 10 Konklusjon | ✅ Ferdig |
| Sammendrag / Abstract | ⏳ Oppdateres etter peer review |

---

## Neste steg – Runde 4 / Peer review

Rapporten er nå komplett som utkast. Gjenstående arbeid:

- **Peer review**: send til medstudent for gjennomlesing
- **Etter review**: oppdater/juster kapitler basert på tilbakemelding
- **Sammendrag/Abstract**: oppdater med endelige tall og konklusjoner
- **Formalia**: fyll inn «Totalt antall sider», «Studiepoeng», «Veileder», dato
- **Ordtelling**: vurder om noen kapitler bør utvides for å nå 9 000+ prosaord

---

## Nøkkelfiler

```
013 fase 3 - review/
  Rapport prosjekt LOG650 v2.md        Hoveddokument – 8 691 råord (17. april)
  Arbeidslogg - Claude sesjon 2026-04-12.md
  Arbeidslogg - Claude sesjon 2026-04-14.md
  Arbeidslogg - Claude sesjon 2026-04-17.md   Denne filen

005 report/
  sarima_results.json                  32 modellresultater
  sarima_model.py                      Python-script
  plots/                               32 PNG-plott
  core.json                            Prosjektkjerne og statistikk
  requirements.json                    Krav K1–K7
```
