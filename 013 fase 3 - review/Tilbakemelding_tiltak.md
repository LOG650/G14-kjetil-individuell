# Tiltak fra peer review – LOG650

Basert på tilbakemeldinger fra Lotte Picard (gjennomgått av Claude og Gemini), 7. mai 2026.
Alle endringer gjøres i `005 report/Rapport prosjekt LOG650 v3.md`.

---

## Høy prioritet – substansielle metodiske poeng

| # | Punkt | Kilde | Status |
|---|-------|-------|--------|
| 1 | **Rullerende 7-dagerssum og prediksjonsintervaller** – Overlappende summer bryter formelt SARIMA-antagelsen om uavhengige residualer, noe som kan gi for smale prediksjonsintervaller og undervurdert sikkerhetslager. Adresseres i kap. 5.1 og 9.4. | Claude | ✅ Ferdig |
| 2 | **Kun ett valideringsvindu** – MAPE-verdier basert på ett holdout-sett er statistisk upålitelige. Løst med rolling-origin-validering over to vinduer (V1: dag 88–94, V2: dag 95–101). Nye tabeller 9a–9c i kap. 7.1. | Claude | ✅ Ferdig |
| 3 | **Høy MAPE-produkter mangler operasjonell vurdering** – GM Pølse (19,9 %) og MH Pommes frites (21,6 %) er i kategorien utilstrekkelig for direkte bruk. Kvantifisert erfaringspåslag (15–20 %) lagt inn i kap. 7.1, 8.1 og 8.4. | Claude + Gemini | ✅ Ferdig |

---

## Middels prioritet – innhold som kan forbedres

| # | Punkt | Kilde | Status |
|---|-------|-------|--------|
| 4 | **Litteratur: kun lærebøker, ingen fagartikler** – Fem peer-reviewede artikler lagt til: Arunraj & Ahrens (2015), Arunraj et al. (2016), Babai et al. (2013), Gilbert (2005), Fattah et al. (2018). | Claude | ✅ Ferdig |
| 5 | **Alternativer (Holt-Winters, SARIMAX, ML) nevnes for sent** – Ny kap. 2.4 introduserer alternativene i litteraturkapittelet. Eksplisitt begrunnelse for SARIMA-valget lagt til i kap. 5.1. Kap. 9.6 trimmet til resultatstyrt diskusjon. | Claude | ✅ Ferdig |
| 6 | **Figurer: ACF/PACF og residualplott mangler** – Rapporten har kun 4 figurer. Diagnostiske plott ville styrket den empiriske argumentasjonen i kap. 5.1 og 7.5. | Claude | ⬜ Gjenstår |
| 7 | **Bidragets egenart er uklar** – Simulerte spilldata bør rammesettes som et bevisst metodisk valg (testbenk for logistikkmetodikk), ikke kun som pragmatisk løsning. Gjelder innledning og litteraturkapittel. | Claude | ⬜ Gjenstår |

---

## Lav prioritet – formelle og kosmetiske

| # | Punkt | Kilde | Status |
|---|-------|-------|--------|
| 8 | **Forsideopplysninger mangler** – Studiepoeng, veileder, antall sider og dato på publiseringsavtalen er tomme felter. Må fylles inn før innlevering. | Claude | ⬜ Gjenstår |
| 9 | **Tabell-kolonnejustering** – Inkonsistent kolonnejustering for produktnavn av ulik lengde i tabellene 4–7 og 10–13. | Claude | ⬜ Gjenstår |
| 10 | **Engelske begreper** – «likelihooden» (kap. 3.4, 6.1), «random walk» (kap. 6.3), «baselines» (kap. 7.1, 9.6). Vurder norske alternativer. | Lotte (manuell merknad) | ⬜ Gjenstår |
| 11 | **Tabell 9-referanse** – Kap. 7.1 refererte opprinnelig til «tabell 9» uten spesifisering av hvilken subtabell. Nå løst av redesign med tabeller 9a–9e. | Lotte (manuell merknad) | ✅ Ferdig (bieffekt av punkt 2) |
| 12 | **Mangler figurliste og tabelliste** – For en rapport med 12+ tabeller og 4 figurer anbefales figurliste og tabelliste etter innholdsfortegnelsen. | Claude | ⬜ Gjenstår |
