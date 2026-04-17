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

### 5. Oppdaget og rettet metodisk feil – rullerende 7-dagersdata

**Problemet:** Spillet viser «sold last 7 days» – en rullerende 7-dagers sum som oppdateres daglig.
Dataene i CSV-filene er altså ikke enkeltdagssalg, men rullerende 7-dagerssummer.

**Konsekvens for den opprinnelige koden:**
SARIMA-modellen predikerer neste rullerende 7-dagerssum. Det 7. prognosesteget (fc[-1]) gir direkte den predikerte 7-dagerssummen for de neste syv dagene – som er akkurat det vi vil bestille. Den gamle koden brukte `fc.sum()` (summen av alle 7 prognosetrinn), noe som teller 7 overlappende vinduer og gir ~7× feil svar.

**Kodefiks i `sarima_model.py`:**
```python
# Gammel (feil):
fc_sum   = float(fc.sum())
fc_upper = float(ci[:, 1].sum())

# Ny (riktig):
fc_sum   = float(fc[-1])       # 7. steg = prognose for neste 7 dager
fc_upper = float(ci[-1, 1])    # øvre KI for samme steg
```

**Oppdaterte lagertall (anbefalt ordre per uke):**

| Utsalgssted | Gammel (feil) | Ny (riktig) |
|-------------|--------------|-------------|
| GM          | 78 460       | 11 548      |
| HK          | 85 725       | 12 669      |
| LM          | 99 433       | 14 724      |
| MH          | 84 077       | 12 373      |

Alle tabeller (Tabell 2, 10–13) og tilhørende brødtekst i rapporten er oppdatert med nye tall.
Sikkerhetslageret ligger nå på 10–14 % av ukentlig prognose (mot feilaktige 6–9 % tidligere).

---

## Ordtelling ved sesjonsslutt

| Mål | Verdi |
|-----|-------|
| Rå ordtelling (wc -w) | 8 658 |
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
| SARIMA-modellering | ✅ Ferdig (kodefiks 17. april) |
| Kap. 1 Innledning | ✅ Ferdig |
| Kap. 4 Casebeskrivelse | ✅ Ferdig |
| Kap. 5.2 Data | ✅ Ferdig |
| Kap. 3 Teori | ✅ Ferdig |
| Kap. 5.1 Metode | ✅ Ferdig |
| Kap. 6 Modellering | ✅ Ferdig |
| Kap. 7 Analyse | ✅ Ferdig |
| Kap. 8 Resultat | ✅ Ferdig (tall oppdatert 17. april) |
| Kap. 2 Litteratur | ✅ Ferdig |
| Kap. 9 Diskusjon | ✅ Ferdig |
| Kap. 10 Konklusjon | ✅ Ferdig |
| Sammendrag / Abstract | ⏳ Oppdateres etter peer review |

---

## Neste steg – Runde 4 / Peer review

Rapporten er nå komplett som utkast med korrekte tall. Gjenstående arbeid:

- **Peer review**: send til medstudent for gjennomlesing
- **Etter review**: oppdater/juster kapitler basert på tilbakemelding
- **Sammendrag/Abstract**: oppdater med endelige tall og konklusjoner
- **Formalia**: fyll inn «Totalt antall sider», «Studiepoeng», «Veileder», dato
- **Ordtelling**: vurder om noen kapitler bør utvides for å nå 9 000+ prosaord

---

## Nøkkelfiler

```
013 fase 3 - review/
  Rapport prosjekt LOG650 v2.md        Hoveddokument – 8 658 råord (17. april, korrekte tall)
  Arbeidslogg - Claude sesjon 2026-04-12.md
  Arbeidslogg - Claude sesjon 2026-04-14.md
  Arbeidslogg - Claude sesjon 2026-04-17.md   Denne filen

005 report/
  sarima_results.json                  32 modellresultater (oppdatert 17. april)
  sarima_model.py                      Python-script (kodefiks 17. april)
  plots/                               32 PNG-plott
  core.json                            Prosjektkjerne og statistikk
  requirements.json                    Krav K1–K7
```
