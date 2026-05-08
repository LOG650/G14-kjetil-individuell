# Tiltak fra peer review – LOG650

Basert på tilbakemeldinger fra Lotte Picard (gjennomgått av Claude og Gemini), 7. mai 2026.
Alle endringer gjøres i `005 report/Rapport prosjekt LOG650 v3.md`.

---

## Høy prioritet – substansielle metodiske poeng

| # | Punkt | Kilde | Status |
|---|-------|-------|--------|
| 1 | **Rullerende 7-dagerssum og prediksjonsintervaller** – Overlappende summer bryter formelt SARIMA-antagelsen om uavhengige residualer, noe som kan gi for smale prediksjonsintervaller og undervurdert sikkerhetslager. Adresseres i kap. 5.1 og 9.4. | Claude | ✅ Ferdig |
| 2 | **Kun ett valideringsvindu** – MAPE-verdier basert på ett valideringssett er statistisk upålitelige. Løst med rullerende prognosevalidering over to vinduer (V1: dag 88–94, V2: dag 95–101). Nye tabeller 9a–9c i kap. 7.1. Begrunnet databegrensning for stopp på to vinduer. | Claude | ✅ Ferdig |
| 3 | **Høy MAPE-produkter mangler operasjonell vurdering** – Skiller nå mellom produkter der begge vinduer er høye (15–20 % påslag anbefalt) og produkter der kun V2 er høy (årvåkenhet, ikke fullt påslag). Kvantifiserte justeringer i kap. 7.1, 8.1 og 8.4. | Claude + Gemini | ✅ Ferdig |

---

## Middels prioritet – innhold som kan forbedres

| # | Punkt | Kilde | Status |
|---|-------|-------|--------|
| 4 | **Litteratur: kun lærebøker, ingen fagartikler** – Fem peer-reviewede artikler lagt til i kap. 2 og bibliografi: Arunraj & Ahrens (2015), Arunraj et al. (2016), Babai et al. (2013), Gilbert (2005), Fattah et al. (2018). APA 7 korrekt. | Claude | ✅ Ferdig |
| 5 | **Alternativer (Holt-Winters, SARIMAX, ML) nevnes for sent** – Ny kap. 2.4 introduserer alternativene med styrker/svakheter. Eksplisitt begrunnelse for SARIMA-valget lagt til i kap. 5.1. Kap. 9.6 trimmet til resultatstyrt diskusjon. | Claude | ✅ Ferdig |
| 6 | **Figurer mangler diagnostikk, og eksisterende figurer er rotete** – To nye figurer: Figur 1 (ACF/PACF, kap. 5.1) og Figur 5 (residualdiagnostikk, kap. 7.5). Eksisterende figurer overhalt: norske titler, y-akse skalert til data, valideringssoner fargekodet, modellinfo som fotnote. Totalt 6 figurer, kronologisk nummerert. | Claude | ✅ Ferdig |
| 7 | **Bidragets egenart er uklar** – Simuleringsdata rammesatt som bevisst testbenk (ikke pragmatisk løsning) i kap. 1 og kap. 4. Formålet splittet i substansielt og metodisk mål. Casebeskrivelsens avslutning skiller mellom ekstern validitet av funn vs. metodikkens overførbarhet. | Claude | ✅ Ferdig |

---

## Lav prioritet – formelle og kosmetiske

| # | Punkt | Kilde | Status |
|---|-------|-------|--------|
| 8 | **Forsideopplysninger mangler** – Studiepoeng, veileder, antall sider og dato på publiseringsavtalen er tomme felter. Fylles inn manuelt før innlevering. | Claude | ⬜ Gjenstår (bevisst utsatt) |
| 9 | **Tabell-kolonnejustering** – Produktkolonnen standardisert til 13 tegn («Pommes frites»-bredde) med konsistent separator i alle tabellene 4–7 og 10–13. | Claude | ✅ Ferdig |
| 10 | **Engelske begreper** – Erstattet: «likelihooden» → «likelihood-verdien», «baselines» → «referanseprognose», «pipeline» → «analyserekke», «holdout-sett» → «valideringssett». Beholdt: «random walk», «stepwise», «maksimum likelihood» (fagtermer). | Lotte (manuell merknad) | ✅ Ferdig |
| 11 | **Tabell 9-referanse** – Løst som bieffekt av punkt 2: tabellene er nå 9a–9e med tydelige undertitler. | Lotte (manuell merknad) | ✅ Ferdig (bieffekt av punkt 2) |
| 12 | **Mangler figurliste og tabelliste** – Figurliste (6 figurer) og tabelliste (17 tabeller inkl. 9a–9e) lagt inn etter innholdsfortegnelsen med lenker. | Claude | ✅ Ferdig |
