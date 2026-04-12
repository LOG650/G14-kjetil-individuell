Prosjektstyringsplan

for

«BiteBurst» lageroptimalisering

**2026-03-11**

Utarbeidet av:

Kjetil Tronstad Lund

Autorisert av:

Kjetil Tronstad Lund

**Innhold**

Contents

[Sammendrag 1](#_Toc222063428)

[Behov 1](#_Toc222063429)

[Sponsor 1](#_Toc222063430)

[Kunde 1](#_Toc222063431)

[Forretningscase 2](#_Toc222063432)

[Alternativer 2](#_Toc222063433)

[Forutsetninger 2](#_Toc222063434)

[Gevinster 2](#_Toc222063435)

[Kostnader 2](#_Toc222063436)

[Analyse 2](#_Toc222063437)

[Omfang 3](#_Toc222063438)

[Mål 3](#_Toc222063439)

[Krav 3](#_Toc222063440)

[Løsning 4](#_Toc222063441)

[Arbeidsnedbrytningsstruktur 4](#_Toc222063442)

[Omfangsverifikasjon 4](#_Toc222063443)

[Fremdrift 6](#_Toc222063444)

[Avhengighetsdiagram 6](#_Toc222063445)

[Gantt-plan 6](#_Toc222063446)

[Kritisk linje 6](#_Toc222063447)

[Milepæler 7](#_Toc222063448)

[~~Budsjett 8~~](#_Toc222063449)

[~~Kostnadsfordeling per leveranse 8~~](#_Toc222063450)

[~~Ressurskostnader 8~~](#_Toc222063451)

[~~Kostnadskurve 8~~](#_Toc222063452)

[Risiko 9](#_Toc222063453)

[Prosess for risikostyring 9](#_Toc222063454)

[Risikoregister 9](#_Toc222063455)

[Saker 11](#_Toc222063456)

[Interessenter 12](#_Toc222063457)

[Ressurser 13](#_Toc222063458)

[Prosjektteam 13](#_Toc222063459)

[Ressursbelastning 13](#_Toc222063460)

[Kritiske ressurser 14](#_Toc222063461)

[Kommunikasjon 15](#_Toc222063462)

[Ukentlige saksstatusmøter 15](#_Toc222063463)

[Månedlige prosjektgjennomganger 15](#_Toc222063464)

[Møter i endringskontrollstyret 16](#_Toc222063465)

[[Other Kommunikasjon] 16](#_Toc222063466)

[Kvalitet 17](#_Toc222063467)

[Fagfellevurderinger 17](#_Toc222063468)

[Uformelle fagfellevurderinger. 17](#_Toc222063469)

[Formelle fagfellevurderinger 18](#_Toc222063470)

[Brukerreviews 19](#_Toc222063471)

[Anskaffelser 21](#_Toc222063472)

[Endringskontrollprosess 22](#_Toc222063473)

# Sammendrag

Dette dokumentet utgjør prosjektstyringsplanen for «BiteBurst» lageroptimalisering-prosjektet. Det dokumenterer planbaselines for omfang, fremdrift, budsjett og risiko, og gir tilleggsinformasjon for å støtte prosjektleder og team i vellykket gjennomføring.

Dette prosjektet støtter følgende mål i prosjektorganisasjonen sin strategiske plan: «maksimere driftsmarginen gjennom optimalisert vareflyt og reduserte lagerkostnader på tvers av utsalgssteder».

Dette er et levende dokument, og skal oppdateres av prosjektleder ved behov gjennom prosjektets løpetid.

## Behov

Prosjektet adresserer utfordringen med ineffektiv lagerstyring i detaljhandel simulert gjennom dataspillet Big Ambitions og den fiktive bedriften «BiteBurst». Med fire utsalgssteder og begrenset lagerplass i utsalgsstedene er det kritisk å unngå både stockout og overlagring. Manuell lagerstyring er tidkrevende og feilbar. Det er behov for en AI-støttet modell som kan optimalisere lagerføring basert på historiske salgsdata.

## Sponsor

«BiteBurst» sin eier, Kjetil Tronstad Lund, er sponsor for dette prosjektet ansvarlig for prosjektbudsjettet og myndighet for godkjenning av denne prosjektplanen og eventuelle endringer under gjennomføring.

## Kunde

Den fiktive bedriften «BiteBurst» representerer sluttbrukerne av prosjektet, har deltatt i definisjon av prosjektomfanget og vil være ansvarlig for godkjenning av kravene og aksept av de endelige leveransene.

## Forretningscase

Forretningscase-analysen fra initieringen er revidert for å reflektere resultatene fra prosjektplanleggingen. Oppsummert indikerer analysen i planleggingsfasen at prosjektet er begrunnet med en positiv nytte-/kostnadsration (BCR), der gevinstene fra redusert kapitalbinding i lager og eliminering av stockouts overstiger prosjektkostnadene.

### Alternativer

Følgende alternativer ble vurdert:

#### a) Status quo: fortsette som før med ukjent lagerbehov og fare for stockouts. Alternativet er forkastet.
#### b) KI-støttet optimalisering: gjennomføre en analyse av historisk salgsdata med henblikk på å optimalisere lagerhold på utsalgssteder. Forslaget har en lav kostnad, med potensial for innsparinger. Forslaget er valgt.
#### c) Full simulering av all ERP-data med manuell modellering for optimal drift. Forslaget er forkastet som dyrt og tidkrevende.

### Forutsetninger

Forretningscaset er basert på følgende forutsetninger:

Simulering i Big Ambitions:

- Salgsdata fra Big Ambitions er stabile og representative nok til at KI kan analyser et mønster. Etterspørselslogikk er konsistent slik at salgsdata er representativ også for fremtidig etterspørsel.
- Manuell dataregistrering gir tilstrekkelig kvalitet og nøyaktighet.
- De fire utsalgsstedene følger et lignende mønster i trafikkscore (besøkskapasitet), at de selger de samme produktene og at det ikke er betydelig variasjon mellom disse. Ulikheter i utsalgspris forekommer, men innkjøpsprisen er identisk.
- Det forekommer ikke oppdateringer underveis som endrer simuleringen.

### Gevinster

Gevinstene forventes å være som følger:

- Redusert risiko for stockout i de fire utsalgsstedene.
- Minimere lagerbeholdningen på de fire utsalgsstedene for å frigjøre plass og unngå kapitalbinding ved overlagring.
- En skalerbar KI-modell som kan tilpasses endringer i sortiment, trafikkscore eller utsalgssted.

### Kostnader

Det forekommer ingen direkte økonomiske kostnader i prosjektet. Programvare for KI-modellering er enten gratisvare eller supplert av Høgskolen i Molde, dataspillet Big Ambitions er allerede anskaffet uavhengig av prosjektet, og den eneste andre ressursen er prosjektteamets tid.

### Analyse

Sammenligningen av gevinster og kostnader viser at det valgte alternativet har en positiv nytte-/kostnadsratio (BCR). Prosjektet har ingen direkte kostnader, og siden gevinstene er knyttet til kjernevirksomheten, har prosjektet en klar positiv BCR.

# Omfang

Denne seksjonen beskriver prosjektomfanget for «BiteBurst»-prosjektet, inkludert prosjektmål, forutsetninger, begrensninger, krav og arbeidsnedbrytningsstruktur som definerer alle leveranser som skal produseres i prosjektgjennomføring og avslutning. Den beskriver også prosessen som skal brukes for omfangsverifikasjon.

All planlegging av prosjektets fremdriftsplan, budsjett og risiko som beskrives i resten av dette dokumentet, er basert på denne omfangsdefinisjonen.

Aktuell status for omfangsfremdrift skal rapporteres hver måned til sponsor, kunde og andre relevante interessenter i den månedlige prosjektgjennomgangen beskrevet i seksjon 9 – Kommunikasjon.

Endringer i prosjektomfanget etter at denne planen er godkjent og etablert som baseline må gå gjennom den formelle endringskontrollprosessen beskrevet i seksjon 12 – Endringskontrollprosess.

## Mål

Prosjektmålet er å utvikle en KI-støttet modell som optimaliserer lagerbeholdning på tvers av fire utsalgssteder i dataspillet Big Ambitions, med mål om å minimere lagernivåene og samtidig unngå stockout over en syv-dagers periode.

Prosjektets forutsetninger er:

At salgsdata samles manuelt og er tilstrekkelig representative. Dataspillet Big Ambitions gir stabile og repeterbare salgsmønstre. De fire utsalgsstedene har en sammenlignbar trafikkscore og produkter, og at det ikke forekommer eksterne forstyrrelser i simuleringen (oppdateringer).

Prosjektets begrensninger er:

Prosjektgjennomføringen: Prosjektet gjennomføres av én student som innehar alle rollene, herunder prosjektleder*.* Studenten er også den som gjennomfører simuleringen i Big Ambitions.Tidsrammen er begrenset til semesteret januar–mai 2026.Viktige milepæler må overholdes og endelig rapport leveres i tide.

Simuleringen: Data er simulert fra et dataspill og må ikke forveksles med reelle forretningsdata, samtidig som innhenting skjer manuelt og begrenser tilgangen noe. Spillet er satt opp med begrensinger til ytre påvirkninger som konkurranse fra spillets KI-motstandere, at det ikke forekommer variasjoner eller kampanjer, utsalgsstedene er ikke optimalisert i forhold til åpningstider (alle fire er satt opp likt) eller annen spillfunksjonalitet som kan påvirke salgsdata (bruk av reklame). Salgsdata avhenger derfor i størst mulig grad kun av spillets innebygde simulering.

## Krav

«BiteBurst» sine prosjektkrav gir den omfangsdetaljen som trengs for å realisere prosjektmålet. Kravene beskriver hva prosjektet må oppfylle for å nå målet, ikke hvordan det skal gjøres. «Hvordan» vil bli definert under prosjektgjennomføringen etter hvert som detaljerte krav og designleveranser utvikles.

Krav er identifisert innen områdene modellens funksjonalitet, modellens kapasitet og datakvalitet fra simulering.

En fullstendig kravliste finnes i vedlegg A, sammen med kravets eier og foreløpig kobling (traceability) til leveranser og testtilfeller. Dette vil bli raffinert etter hvert som design- og testplanleggingen utvikles under gjennomføringen.

Kravene ble innhentet og etablert som baseline av «BiteBurst» sine forretningsanalytikere, basert på tidligere erfaring fra lignende prosjekter, omfattende intervjuer med kundens brukergrupper, og forskning på relevante standarder. Kravene har vært gjennom flere runder med gjennomgang for å sikre at de er komplette, konsistente og testbare, og er signert av de respektive eierne.

## Løsning

Løsningen som skal utvikles for å oppfylle prosjektmålet er å benytte KI-tjenester som Claude AI i samarbeid med Python/Node.js til å utvikle modell(er) for anbefalt lagerhold. Et overordnet diagram er gitt nedenfor.

![A horizontal flowchart with four dark teal rounded rectangles connected by rightward arrows. From left to right: - "Salgsdata (fra Big Ambitions)" - "Manuell registrering (.csv)" - "Modellering med KI" - "Prosjektrapport / anbefaling"](./BiteBurst%20Lageroptimalisering%20Prosjektplan%20LOG650_images/image_001.png)

Denne løsningsdefinisjonen ble utviklet med tilstrekkelig detaljnivå til at planleggingsteamet kunne utarbeide en prosjektplan med fremdrift ~~og budsjett~~ med en nøyaktighet estimert til +/- 10 % for sponsors gjennomgang og godkjenning for å gå videre til gjennomføringsfasen. Ytterligere definisjonsdetaljer som er nødvendige for å bygge den komplette løsningen, vil bli utviklet under prosjektgjennomføringen.

Prosjektet inneholder flere viktige leveranser som følges av en milepæl i Gantt-diagrammet. Det kan spesielt nevnes: levering og godkjenning av proposal, levering og godkjenning av prosjektplan, levering, peer-to-peer og godkjenning av foreløpig prosjektrapport, og til slutt levering av endelig rapport.

## Arbeidsnedbrytningsstruktur

«BiteBurst» sin arbeidsnedbrytningsstruktur (WBS) utgjør den formelle baselinen for hele prosjektets omfang. Prosjektleder og delprosjektledere gjennomførte flere planleggingsiterasjoner for å utarbeide WBS. WBS dokumenterer alle prosjektleveranser og fanger opp alt arbeid som skal utføres i prosjektet.

WBS er vist her:

![The image is a flowchart for a project called “BiteBurst lageroptimalisering” with five main stages: - Steg 1: Proposal → “Utarbeide og levere proposal” - Steg 2: Prosjektplan → “Utarbeide og levere prosjektplan + Gantt” - Steg 3: Gjennomføring → branches to “Teori og litteratursøk”, “Modellering med AI”, “Utarbeide utkast rapport” - Steg 4: Avslutning → “Sluttføre rapport” - Steg x: Simulering av data → branches to “Oppsett av Big Ambitions”, “Oppsett salgslogg”, “Simulering for data” It shows the main phases and sub-tasks in a project plan.](./BiteBurst%20Lageroptimalisering%20Prosjektplan%20LOG650_images/image_002.png)

Mer informasjon finnes også i WBS-ordlisten i vedlegg B, som gir beskrivelse og eier for hver leveranse.

Leveransene i arbeidsnedbrytningsstrukturen kan også finnes som flytskjema over rekkefølgen de utføres i, i seksjon 3.1 – Avhengighetsdiagram, og som planlagt over kalenderen i seksjon 3.2 – Gantt-plan.

## Omfangsverifikasjon

Alt arbeid som leveres inn i sluttproduktet skal verifiseres både av prosjekteamene som har produsert leveransene, og gjennom uavhengig verifikasjon fra QA-organisasjonen, for å sikre at leveransene er i samsvar med alle krav og er egnet for formålet – dvs. i stand til fullt ut å dekke behovet de var ment å tilfredsstille.

Før hver leveranse ferdigstilles skal prosjekteamene først verifisere eget arbeid for å sikre at det er feilfritt og oppfyller alle prosjektkrav, før det sendes videre til QA for verifikasjon. Leveranse-eierne skal ikke basere seg på QA-prosessen for å finne avvik og feil.

Kvalitetssikring (QA) skal deretter gjennomføre formell verifikasjon for å bekrefte at prosjektleveransene er korrekt bygget og konfigurert. Eventuelle avvik eller mangler skal dokumenteres, og korrigerende tiltak skal defineres av leveranse-eier. Korrigeringene skal gjennomføres så raskt som rimelig av leveranse-eierne, og deretter re-verifiseres av QA. En leveranse skal ikke passere verifikasjon før QA-organisasjonen formelt bekrefter at alle avvik er håndtert og at arbeidet er klart til å gå videre til neste steg.

Verifikasjoner kan gjennomføres gjennom inspeksjoner, demonstrasjoner, analyser eller tester, avhengig av hva som er hensiktsmessig. Verifikasjoner skal gjennomføres gjennom hele prosjektet etter hvert som enkeltdeler, utkast, versjoner, inkrementer eller sprinter ferdigstilles, for å avdekke avvik og muliggjøre korrigering lenge før endelig leveranse etableres som baseline.

Der det er mulig skal scenario-basert verifikasjon benyttes, der verifikasjonen gjennomføres i konteksten av et eksempel på faktisk bruk av leveransen. Dette gir mest mulig realistisk verifikasjon av at leveransen oppfyller kravene, og gjør det samtidig tydelig at arbeidet er egnet for formålet. De fremtidige forretningsprosessene (to-be) som utvikles som del av prosjektets første steg, vil være grunnlaget for disse scenarioene der det er relevant.

Der det er relevant skal terskler for avvik og feil etableres for å tillate at mindre avvik kan korrigeres i støtte-/driftsfasen, samtidig som arbeidet kan gå videre til neste steg. Når denne tilnærmingen vurderes som hensiktsmessig, skal QA samarbeide med prosjektgruppen og kunde-/brukergrupper for å etablere kriterier etter følgende struktur:

- Det må være null kategori 1-saker – som påvirker kjernefunksjonalitet.
- Det må være færre enn N (f.eks. 3) kategori 2-saker – der det finnes en workaround som er akseptabel for kunderepresentanten inntil saken er rettet innen rimelig tid.
- Det må være færre enn M (f.eks. 5) kategori 3-saker – mindre brukervennlighetsavvik som ikke hindrer bruk, og som kunderepresentanten godtar kan håndteres i støtte/driftsfasen eller i neste prosjektfase.

Der tersklene over vurderes som nyttige for vurdering av leveranser, skal de avtales og dokumenteres under testplanleggingen før leveransetesting starter.

# Fremdrift

Denne seksjonen dokumenterer fremdrifts-baselinen for «BiteBurst-prosjektet», der prosjektarbeidet definert i WBS mappes mot kalenderen for å fastslå prosjektets varighet og den kritiske linjen som styrer sluttdatoen.

Planlogikken er beskrevet i seksjon 3.1 – Avhengighetsdiagram. Avhengighetsdiagrammet, mappet mot kalenderen og med total prosjektvarighet, er gitt i seksjon 3.2 – Gantt-plan. Den kritiske linjen som styrer prosjektvarighet og sluttdato er gitt i seksjon 3.3 – Kritisk linje. Viktige milepæler er dokumentert i seksjon 3.4 – Milepæler.

Aktuell status for fremdriften skal rapporteres hver måned til sponsor, kunde og andre relevante interessenter i den månedlige prosjektgjennomgangen beskrevet i seksjon 9 – Kommunikasjon.

Endringer i fremdriftsplanen etter at denne planen er godkjent og etablert som baseline må gå gjennom den formelle endringskontrollprosessen beskrevet i seksjon 12 – Endringskontrollprosess.

## Avhengighetsdiagram

Avhengighetsdiagrammet for «BiteBurst» dokumenterer gjennomføringslogikken for prosjektet, ved å flytskjeme leveransene for å vise avhengigheter mellom dem og rekkefølgen prosjektarbeidet skal utføres i.

Prosjektleder og faglederne gjennomførte flere planleggingsiterasjoner for å etablere et komplett og korrekt avhengighetsdiagram som dokumenterer sammenhengene mellom alt prosjektarbeid.

Dette avhengighetsdiagrammet gir den logiske strukturen for prosjektarbeidet, som deretter mappes til kalenderen slik det fremgår av Gantt-planen i neste seksjon.

Avhengighetsdiagram er tilgjengelig i vedlagt Gantt-fil (MS Project).

## Gantt-plan

Delprosjektlederne utarbeidet detaljerte aktivitetsnedbrytninger for alle sine leveranser for å estimere varighet for alle arbeidselementer. Strukturen fra avhengighetsdiagrammet og disse estimatene ble deretter lagt inn i MS Project for å få en Gantt-plan som viser hvordan prosjektarbeidet mappes mot kalenderen, inkludert beregning av kritisk linje som styrer prosjektets sluttdato. Denne Gantt-planen utgjør den formelle fremdrifts-baselinen for «BiteBurst».

Se vedlagt Gantt-diagram i Microsoft Project.

## Kritisk linje

Et utdrag av «BiteBurst» sin Gantt-plan som viser kun leveransene på prosjektets kritiske linje, er vist nedenfor. Leveransene er listet i rekkefølge etter ferdigdato og viser arbeidet som driver prosjektets varighet og sluttdato i den kalenderrekkefølgen det er planlagt å fullføre.

Det er avgjørende å levere dette arbeidet i henhold til plan for å unngå forsinkelser i hele prosjektet, og dette skal være et særlig fokusområde for prosjektleder og delprosjektledere. Ressurser skal omdisponeres fra arbeid utenfor kritisk linje til leveranser på kritisk linje der det er praktisk mulig, dersom arbeidet på kritisk linje krever ekstra ressurser for å opprettholde planlagt fremdrift.

Kritisk sti i prosjektet er i hovedsak Proposal → prosjektplan → teori og litteratursøk → utarbeidelse av rapport → sluttføring → innlevering.

Det ligger noe slakk i planen da det må påberegnes venting på godkjenning og fagfellegodkjenning (pper-to-peer).

## Milepæler

«BiteBurst»-prosjektets milepæler markerer hendelser der viktige arbeidselementer fullføres og som i betydelig grad bringer prosjektet videre. Status for fremdrift mot milepælene vil bli presentert i hver månedlig prosjektgjennomgang, og vil ha særlig ledelsesoppmerksomhet.

Følgende milepæler ble definert av sponsor i prosjektcharteret fra initieringen:

- Godkjenning av proposal
- Godkjenning av prosjektplan og Gantt-diagram
- Endelig leveranse av prosjektrapport med modell.

De øvrige milepælene ble valgt av planleggingsteamet for å markere de mest betydningsfulle oppnådde punktene etter hvert som prosjektet utvikler seg.

En Gantt-plan som viser prosjektets milepæler slik de faller i kalenderen, er vist i figuren nedenfor:

*Se vedlagt fil for Gantt-diagram med milepæler.*

# ~~Budsjett~~

~~Denne seksjonen dokumenterer baselinet budsjett for [ABC] og beskriver alle kostnader som planlegges brukt i løpet av prosjektet.~~

~~Total planlagt kostnad for prosjektet er [$$$]. Ytterligere informasjon gis i de følgende seksjonene, inkludert en kostnadsfordeling per hovedleveranse, en oppsummering av ressurskostnader etter type, og en kostnadskurve som viser planlagt forbruk over tid.~~

~~Baseline-budsjettet oppfyller den økonomiske rammen spesifisert i prosjektcharteret fra initieringen ved å være mindre enn [$$$]:~~

~~Aktuell status for budsjettutviklingen skal rapporteres hver måned til sponsor, kunde og andre relevante interessenter i den månedlige prosjektgjennomgangen beskrevet i seksjon 9 – Kommunikasjon.~~

~~Endringer i prosjektbudsjettet etter at denne planen er godkjent og etablert som baseline må gå gjennom den formelle endringskontrollprosessen beskrevet i seksjon 12 – Endringskontrollprosess.~~

## ~~Kostnadsfordeling per leveranse~~

~~Delprosjektlederne utarbeidet en detaljert aktivitetsnedbrytning for hver av sine leveranser, inkludert alle ressurser, materiell og tjenester som kreves for å produsere leveransene, for å få komplette kostnadsestimater for alle arbeidselementer.~~

~~En fordeling av prosjektkostnaden per leveranse er gitt i tabellen nedenfor.~~

~~[En oversikt over kostnaden for hver leveranse. For større prosjekter med mange leveranser kan dette være på WBS-sammendragsnivå (som grupperer flere leveranser), med henvisning til kostnadskolonnen i Gantt-planen eller til vedlegg/vedlagt dokument for kostnadsfordelingen ned til enkeltleveransenivå.]~~

~~Kostnadskontoer som skal brukes til å spore alle kostnadsutgifter for hver leveranse ble tildelt av finansavdelingen, og kan finnes i kostnadskontokolonnen i WBS-ordlisten.~~

## ~~Ressurskostnader~~

~~En oversikt over kostnadene for ressursene som brukes i [ABC]-prosjektet er gitt i tabellen nedenfor, inkludert summering av kostnader per hovedressurstype. Satsen for personellressurser er fullt belastet midtpunkt for hver arbeidskategori, inkludert indirekte kostnader og overhead.~~

~~[Kostnad per enhet eller tid for de ulike ressursene som brukes i prosjektet.]~~

## ~~Kostnadskurve~~

~~En tidsfaset oppsummering av planlagt budsjettforbruk gjennom kalenderen er gitt nedenfor.~~

*~~[For større prosjekter, en graf som viser forventede utgifter over tid, noen ganger med eventuelle grenser for regnskapsåret.]~~*

# Risiko

Denne seksjonen beskriver risikostyringsprosessen for «BiteBurst» og gir en kopi av risikoregisteret som baseline. Totalt planlagt risikobudsjett er 10 dager og 0 NOK, og er inkludert i prosjektets baseline for budsjett og fremdrift.

## Prosess for risikostyring

Risikoregisteret og tilhørende risikobudsjett ble utarbeidet av prosjektleder og prosjektledere for delområder, og forbedret iterativt gjennom planleggingsfasen. Risikoer ble identifisert ved å gå gjennom alle punkter i vår standard risikosjekkliste, ved å se på risikoplanlegging og erfaringer fra tidligere lignende prosjekter, samt ved konsultasjon med prosjektgruppen. Risikoene ble kvantifisert, tiltak ble utarbeidet for å unngå eller redusere risikoene så langt som mulig, beredskapsplaner ble utarbeidet for å håndtere hendelsen dersom risikoen likevel inntraff, og et endelig kvantifisert risikobudsjett ble etablert som baseline.

Sannsynlighet og tidsestimater for risikoene ble utviklet av prosjektgruppen basert på tidligere erfaring og ved bruk av Delphi-estimering. Kostnadsestimatene ble utviklet gjennom en kostnadskonsekvensanalyse som funksjon av estimert forsinkelsestid, og med hensyn til andre relevante kostnader.

Prosjektleder for «BiteBurst» har ansvar for forvaltning av risikobudsjettet og for at prosjektet gjennomføres med ønsket resultat. Eierskap til enkeltstående risikoer er lagt til det nivået som er nærmest og best i stand til å håndtere risikoen. Risikoregisteret skal gjennomgås ved slutten av hvert ukentlig statusmøte. Risikoutløsere skal overvåkes av risiko-eierne, og tiltak skal iverksettes proaktivt for å unngå eller redusere risiko der det er mulig. Risikotiltaksplaner skal revideres og forbedres gjennom hele prosjektet ved behov. Midler skal tas fra risikobudsjettet for å finansiere proaktive tiltak som gir størst mulig risikoreduksjon så tidlig som mulig. Dersom det blir tydelig at en risiko ikke kan unngås, skal beredskapsplanene aktiveres.

Prosjektleder er autorisert signeringsmyndighet for uttak fra risikobudsjettet i kroner. For å hente midler fra budsjettet skal prosjektleder sende inn et begrunnelsesskjema for uttak til «BiteBurst» sin økonomicontroller, der status for den planlagte risikoen som midlene brukes til dokumenteres fullt ut, eller hvorfor midlene trengs for en uforutsett risiko, hvilke alternativer til uttak fra risikobudsjettet som er vurdert og funnet uegnet, samt begrunnelse for beløpet som tas ut. Beløp som overstiger 10 % av opprinnelig risikobudsjett-baseline krever i tillegg godkjenning fra finansdirektør (VP Finance).

Risikotidsbufferen er planlagt i henhold til prinsippene for Critical Chain Management, som én samlet buffer før den kritiske kundehendelsen hvis planlagte dato skal beskyttes mest. Denne hendelsen ble identifisert som rett før oppstart av pilotutrulling av den første produksjonslinjen.

Aktuell status for risikobudsjettet skal rapporteres hver måned til sponsor, kunde og andre relevante interessenter i den månedlige prosjektgjennomgangen beskrevet i seksjon 9 – Kommunikasjon.

Eventuelle økninger i risikobudsjettet etter at denne planen er godkjent og etablert som baseline må gå gjennom den formelle endringskontrollprosessen beskrevet i seksjon 12 – Endringskontrollprosess.

## Risikoregister

«BiteBurst» sitt risikoregister, som viser kjente prosjektrisikoer, estimerte konsekvenser for tid og kostnad, eier, utløsere, tiltak og beredskapsplan, finnes på de følgende sidene. Totalt planlagt risikobudsjett på 10 dager og 0 NOK er gitt i siste rad i risikoregisteret, som summerer beløpene som er estimert nødvendig for hver enkelt risiko.

Det fullstendige risikoregisteret gir også tilleggsinformasjon om kvantifiseringsvurderingen før risikotiltaksplanleggingen ble anvendt.

![The image shows a risk register table in Norwegian with columns: - ID - Risiko - Beskrivelse - Sannsynlighet - Konsekvens - Tiltak - Ansvarlig Rows R1 through R8 list risks such as: - data not representative for pattern recognition - errors and omissions in manual data registration - updates in Big Ambitions changing logic and mechanisms - technical tools unavailable - digital tools unavailable - delays in data collection - significant deficiencies found in peer review - approval not received in time Each row includes descriptions, likelihood, consequence, mitigation actions, and the responsible person named Kjetil Lund.](./BiteBurst%20Lageroptimalisering%20Prosjektplan%20LOG650_images/image_003.png)

# Saker

Nødvendige ressurser, fremdrift og budsjett for å håndtere alle forventede prosjektsaker er bygget inn i baselineplanen, med følgende saker fortsatt uavklart og som må løses under gjennomføringen.

Det er ingen kjente uavklarte saker på prosjektnivå ved planleggingens slutt.

# Interessenter

Denne seksjonen beskriver de viktigste interessentene for «BiteBurst»-prosjektet. Prosjektets interessenter påvirkes av og kan påvirke prosjektet, og er derfor inkludert i definisjon av prosjektomfang og utvikling av prosjektplanen, og vil inngå i regelmessig kommunikasjon etter hvert som prosjektet utvikler seg. De viktigste interessentene, med rolle, hovedbehov, prioriteringer og planlagt kommunikasjon, er beskrevet i interessentregisteret nedenfor.

[Avdelinger, organisasjoner og etater som kan påvirke eller påvirkes av prosjektet, med navn på én representant som er ansvarlig for koordinering med prosjektet, deres rolle, hovedbehov, prioriteringer (omfang, fremdrift, budsjett) og planlagt kommunikasjon. List også opp ansvar hos nøkkelinteressenter som må bidra til prosjektet – ressurser, finansiering, gjennomganger, sertifiseringer osv.]

- Restaurantsjef eller ordreansvarlig på hvert utsalgssted: representeres ved prosjekteier.
- Sentrallager for de fire utsalgsstedene
- Oppstrømsleverandør(er) og grossistledd
- Utsalgsstedenes kunder
-

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Interessent** | **Rolle** | **Behov, krav, forventing** | **Kommunikasjon** | **Ansvarlig** |
| Ordreansvarlig i restaurantene | Intern aktør, bruker av modell | Korrekt lageranbefaling | Motta lageranbefaling, bør inkluderes underveis for å sikre gjennomførbarhet i anbefaling | Prosjekteier |
| Sentrallager | Intern distributør og bestiller fra grossist | Effektiv vareflyt til utsalgssteder, samt optimalisere egen varebestilling fra grossist | Tilsvarende som ordreansvarlig | Prosjektleder |
| Grossist | Ekstern leverandør | Forutsigbar og jevn bestilling, ingen «bullwhip effect» | Kan inkluderes for å sikre gjennomførbarhet i bestillinger, ellers ingen | Leverandøransvarlig via prosjektleder. |
| Kunder | Sluttbruker | Tilgjengelighet av produkter (ingen stockout) | Ingen, fås indirekte via tilgjengelighet | Ingen |

Det eksisterer ikke aksjonærer eller andre eiere i det fiktive selskapet «BiteBurst». Det er heller ikke oppført representant siden dette er fiktive interessenter.

# Ressurser

Denne seksjonen beskriver prosjektteamet, gir en ressursbelastning over tid, og beskriver planene for håndtering av kritiske ressurser som kreves for å gjennomføre «BiteBurst»-prosjektet.

## Prosjektteam

Prosjektteamet som skal gjennomføre «BiteBurst»-prosjektet er vist i organisasjonskartet nedenfor.

![The image is a simple org chart with one person occupying four roles: - Top box: "Kjetil Tronstad Lund" with subtitle "Prosjektsponsor" - Middle box: "Kjetil Tronstad Lund" with subtitle "Prosjektleder" - Bottom left box: "Kjetil Tronstad Lund" with subtitle "Analytiker" - Bottom right box: "Kjetil Tronstad Lund" with subtitle "Datainnhenter"](./BiteBurst%20Lageroptimalisering%20Prosjektplan%20LOG650_images/image_004.png)

På grunn av den kritiske betydningen «BiteBurst»-prosjektet har for virksomheten, er de utpekte delprosjektlederne de mest senior og erfarne medarbeiderne fra hver avdeling. Delprosjektlederne rapporterer direkte til prosjektleder for gjennomføring av prosjektet, og har ansvar for å lede alt arbeid og teammedlemmer innen sitt fagområde. Leveransene som hver delprosjektleder er ansvarlig for, er listet i eier-kolonnen i WBS-ordlisten (WBS-ordliste).

De ulike arbeidsteamene på operativt nivå hentes fra matriseorganisasjonen, dvs. fra virksomhetens funksjonsavdelinger. For å sikre at det ikke oppstår forsinkelser, skal alle teammedlemmer være allokert på fulltid til dette prosjektet i periodene de trengs.

Roller og ansvar for prosjektsponsor, prosjektleder og delprosjektledere er beskrevet i tabellen nedenfor.

| **Name** | **Role** | **Responsibilities** |
| --- | --- | --- |
| Kjetil Tronstad Lund | Prosjektsponsor | • Godkjenning av prosjektplanen, omfang, fremdriftsplan, budsjett og risikobudsjett.  • Godkjenning av endringer i planens baseline når prosjektet er i gang.  • Lede de månedlige prosjektgjennomgangene.  • Sikre fortsatt støtte i virksomheten.  • Løse saker som prosjektleder ikke kan løse. |
| Kjetil Tronstad Lund | Prosjektleder | • Utarbeide en komplett, korrekt og realistisk prosjektplan.  • Lede prosjektet for å oppnå best mulig måloppnåelse mht. omfang, fremdrift, budsjett og risiko.  • Lede delprosjektlederne.  • Sikre at prosjektresultatet er egnet for formålet og fullt ut oppfyller interessentenes forventninger.  • Formell statusrapportering av prosjektets fremdrift én gang per måned.  • Gjennomføre de månedlige prosjektgjennomgangene og presentere prosjektstatus for sponsor og nøkkelinteressenter.  • Lede det ukentlige saksstatusmøtet. |
| Kjetil Tronstad Lund | Analytiker | * Analysere innkommet data og gjennomføre simulering med KI. |
| Kjetil Tronstad Lund | Datainnhenter | * Innhente nødvendig litteratur og data som er nødvendig for prosjektet. |

## Ressursbelastning

Følgende graf viser ressursbelastning målt i timer for arbeidskategoriene [kategorier] gjennom prosjektets løpetid.

Prosjektet har én ressurs ved Kjetil Tronstad Lund. Vedkommende innehar alle roller i prosjektet. Det estimeres med et gjennomsnitt på 20-30 timer per uke gjennom prosjektets levetid, hvor en høyere andel benyttes i kritiske faser som rett før innlevering av prosjektet og utkast til prosjektrapport. Se ellers vedlagt fil med Gantt-diagram.

## Kritiske ressurser

Følgende ressurser er vurdert som kritiske for suksess i «BiteBurst»-prosjektet:

- Big Ambitions: tilgang på spillet er kritisk for å fremskaffe salgsdata.
- Tilgang på KI-verktøy som Claude, Python/Node: kritisk for gjennomføring og implementering av modellering

# Kommunikasjon

Denne seksjonen beskriver planlagt formell kommunikasjon etter hvert som «BiteBurst»-prosjektet gjennomføres.

Formell prosjektkommunikasjon skal bestå av ukentlige saksstatusmøter, månedlige prosjektgjennomganger, møter i endringskontrollstyret. De følgende seksjonene gir mer informasjon.

## Ukentlige saksstatusmøter

Formålet med det ukentlige saksstatusmøtet er å gi et fast kommunikasjonspunkt for kjerneteamet, der man diskuterer prosjektets saker og risikoer, koordinerer videre tiltak ved behov, og opprettholder fremdrift og momentum i prosjektet.

Prosjektleder skal lede møtet. Deltakere skal inkludere delprosjektlederne. Møtet skal holdes hver mandag morgen kl. 09:00. Varighet skal være maks én time.

Faglederne skal gjennomgå risikoene på prosjektets saksliste for tiltak, oppdatering eller lukking ved behov. Nye saker skal registreres, og mulige løsninger diskuteres så langt tiden tillater. Prosjektkoordinator skal distribuere oppdatert liste til alle delprosjektledere ved avslutning av møtet. En kopi av malen for saksliste finnes i vedlegg C.

Ved slutten av hvert møte skal teamet også gjennomgå prosjektets risikoregister, gjøre nødvendige oppdateringer og koordinere videre tiltak ved behov.

## Månedlige prosjektgjennomganger

Formålet med de månedlige prosjektgjennomgangsmøtene er å gi en fast arena der prosjektleder kan gi en statusoppdatering til sponsor, kunde og interessenter hver måned, og samtidig gjøre det mulig for toppledelsen å gi nødvendig styring og retning.

Prosjektsponsor skal være møteleder. Prosjektleder skal gjennomføre møtet. Deltakere skal inkludere:

Prosjektleder, analytiker og datainnhenter, i tillegg til prosjektsponsor.

Møtet skal planlegges til én time, og holdes kl. 13:00 den første tirsdagen i hver måned i styrerommet (Executive boardroom).

Ved starten av hver måned skal prosjektleder, prosjektkoordinator og prosjektplanlegger samle inn aktuell status for prosjektets omfang, fremdrift, kostnader og risikoer for presentasjon i den månedlige gjennomgangen. Et én-sides rapportformat skal benyttes, slik som i vedlegg D. Gjeldende versjon av risikoregisteret skal også være tilgjengelig. Annen relevant informasjon skal gis etter behov og på forespørsel.

Prosjektleder vil presentere prosjektstatus for interessentene i den månedlige gjennomgangen. Prosjektleder skal så langt som mulig ta med alternativer og anbefalinger for å løse vesentlige saker og risikoer. Støtte og prioriteringsavklaringer skal innhentes ved behov. Planer for videre tiltak skal koordineres der det er nødvendig.

## Møter i endringskontrollstyret

Formålet med møter i endringskontrollstyret (Change Control Board, CCB) er å gjennomgå alle endringer i omfang, fremdriftsplan, budsjett eller tidligere baselinede og godkjente leveranser, slik som design og dokumentasjon, for å sikre at alle mulige konsekvenser identifiseres, at nødvendig godkjenning fra prosjektleder eller sponsor innhentes, og at godkjente endringer kommuniseres hensiktsmessig til alle berørte parter. Mer informasjon om prosessen finnes i seksjon 12 – Endringskontrollprosess.

## Annen kommunikasjon

Ingen.

# Kvalitet

Denne seksjonen beskriver tilnærmingen til kvalitetsstyring gjennom hele «BiteBurst»-prosjektet.

Kvaliteten på prosjektets leveranser er avgjørende for suksess, og vil være et hovedfokus for ledelsen og prosjektteamet gjennom hele gjennomføringen.

De fire kvalitetsprinsippene som ligger til grunn for dette prosjektet er oppsummert nedenfor:

## 1. Planlegging. «Kvalitet må planlegges inn, ikke inspiseres inn». Selv om alt prosjektarbeid skal inspiseres og testes ved ferdigstillelse, skal kvalitet bygges inn i arbeidet av teamene mens det utføres.
## 2. Gevinst. Kvalitetsmessig gode deler og prosesser reduserer samlet kostnad og tidsbruk, fordi de øker effektiviteten, reduserer behovet for testing, reduserer akseptanse- og sertifiseringsutfordringer, og reduserer uforutsette problemer når løsningen er i drift.
## 3. Kontinuerlig forbedring. The team will gather lessons learned throughout the prosjekt to continuously build on incremental improvement as the work progresses.
## 4. Egnet for formålet. Alle prosjektleveranser må være «egnet for formålet», dvs. faktisk kunne utføre jobben de er ment for og fullt ut tilfredsstille kundens behov. Dette kravet skal også inngå i de formelle vilkårene (Terms and Conditions) i alle leverandørkontrakter.

Alle prosjektmedlemmer skal bruke beste praksis og standarder innen sitt fag i gjennomføring av arbeidet. I tillegg er fagfellevurderinger og brukerreviews bygget inn i leveransearbeidet som viktige bidrag for å maksimere kvaliteten på resultatet. Mer informasjon om bruk av fagfellevurderinger og brukerreviews finnes i de følgende seksjonene.

## Fagfellevurderinger

Fagfellevurderinger er en av de mest effektive prosessene for å sikre at leveranser har høy kvalitet og er fullt ut egnet for formålet.

Det er to typer fagfellevurderinger som skal brukes i dette prosjektet: uformelle fagfellevurderinger som brukes for alle prosjektleveranser, og formelle fagfellevurderinger som kreves for leveranser med helse-, sikkerhets- eller juridisk sensitivitet. Mer informasjon følger nedenfor.

### Uformelle fagfellevurderinger.

Uformelle fagfellevurderinger har ikke den administrative overheaden som formelle fagfellevurderinger krever, men gir likevel viktig kvalitetssikring av arbeidet. Prosessen for uformelle fagfellevurderinger er oppsummert nedenfor:

#### 1. Eier av hver leveranse som overleveres til andre i prosjektet skal sikre at leveransen har vært gjennom en fagfellevurdering før den ferdigstilles.
#### 2. For store arbeidspakker skal det gjennomføres flere fagfellevurderinger gjennom utviklingsprosessen av leveransen, slik at hver enkelt review krever håndterlig innsats. Som tommelfingerregel bør hver review kreve høyst én time per reviewer.
#### 3. En fagfellevurdering bør inkludere to eller tre fagfeller for å gi en helhetlig vurdering fra mer enn ett perspektiv.
#### 4. Der det er mulig skal leveranse-eier holde ett konsolideringsmøte med alle fagfellene for å samle et konsolidert sett med kommentarer og for å legge til rette for at fagfellene kan kommentere på hverandres anbefalinger.
#### 5. Leveranse-eier kan stille oppfølgingsspørsmål for å avklare en kommentar, men skal avstå fra å diskutere/argumentere mot nøyaktigheten i kommentaren slik at konsolideringsmøtet forblir fokusert på å samle inn et komplett sett med kommentarer. For å sikre fokus på denne sentrale egenskapen ved uformelle fagfellevurderinger, skal leveranse-eier si «Takk» etter mottak av hver kommentar.
#### 6. Eier av leveransen kan deretter innarbeide kommentaren i en revisjon av leveransen, eller forkaste kommentaren etter eget faglig skjønn.
#### 7. Det kreves ingen formelle protokoller for uformelle fagfellevurderinger, men leveranse-eier må beholde en oversikt over fagfellenes kommentarer i egne arkiver til prosjektet er levert, i tilfelle dokumentasjonen senere skulle bli etterspurt.

### Formelle fagfellevurderinger

Formelle fagfellevurderinger er påkrevd for alle leveranser som har helse-, sikkerhets- eller juridiske krav, for å sikre at alle avvik blir løst før ferdigstillelse. Prosessen for formelle fagfellevurderinger er oppsummert nedenfor:

#### 1. QA-organisasjonen skal sikre at hver leveranse med helse-, sikkerhets- eller juridiske krav har gjennomført en formell fagfellevurdering før den ferdigstilles. En QA-representant skal administrere hver formelle fagfellevurderingsprosess.

#### 2. For store arbeidspakker skal det gjennomføres flere formelle fagfellevurderinger gjennom utviklingsprosessen av leveransen, slik at hver enkelt review krever håndterlig innsats fra hver reviewer.
#### 3. En formell fagfellevurdering bør omfatte tre til fem fagfeller for å gi en helhetlig vurdering fra mer enn ett perspektiv. Fagfellene bør så langt som mulig velges utenfor prosjektteamet for å sikre en full og upartisk vurdering.
#### 4. Kvalitetssikring (QA) skal innkalle til og lede ett konsolideringsmøte med alle fagfellene for å samle et konsolidert sett av avvik/punkter og for å legge til rette for kommentarer på hverandres anbefalinger. Det er ingen fast varighet for et slikt konsolideringsmøte ved formell fagfellevurdering. QA-representanten skal registrere og følge opp den konsoliderte listen fra kommentar til løsning.
#### 5. Leveranse-eier kan stille oppfølgingsspørsmål til en fagfelle for å avklare avvik, og kan gi tilleggsinformasjon dersom vedkommende mener at et punkt ikke er korrekt. Ved uenighet mellom leveranse-eier eller fagfeller om riktigheten av et punkt, skal QA-representanten be om avstemning blant fagfellene (uten leveranse-eier), der QA-representanten avgjør ved stemmelikhet. Stemmegivningen til hvert medlem i omstridte saker, uavhengig av om saken får flertall, skal registreres i avviksloggen for eventuell senere oppfølging. QA-representanten kan etter eget skjønn registrere et punkt for oppfølging dersom det vurderes som berettiget, selv om det ikke fikk flertall.
#### 6. Hvert punkt som er avtalt, vedtatt ved flertall, eller tatt inn etter QA-representantens skjønn, skal deretter vurderes av leveranse-eier og håndteres på en hensiktsmessig måte enten ved revisjon av leveransen eller ved å gi relevant tilleggsinformasjon som ikke var tilgjengelig under konsolideringsmøtet. Hver løsning/tilbakemelding skal gjennomgås av de opprinnelige fagfellene for godkjenning. QA-representanten vil normalt følge den opprinnelige fagfellens vurdering av om løsningen er tilstrekkelig. Dersom enighet ikke oppnås, kan QA-representanten likevel godkjenne et punkt som løst dersom dette vurderes som hensiktsmessig, forutsatt at beslutningen godkjennes av QA-direktøren.
#### 7. Formelle protokoller fra alle fagfellevurderinger og tilhørende løsnings-/korrigeringshandlinger skal arkiveres i QA-arkivet i minst fem år etter at prosjektet er avsluttet.

## Brukerreviews

Brukerreviews er også inkludert i prosjektplanen som viktige bidrag for å sikre at prosjektresultatet er egnet for formålet.

Nesten alt arbeidet i prosjektet er planlagt etter smidige prinsipper (agile), strukturert i en serie med inkrementer, utkast, versjoner eller sprinter med muligheter for gjennomgang, formell statusrapportering og tidlig justering ved behov for å sikre at prosjektet holder kursen og leverer forventede resultater etter hvert som inkrementene utvikles. Denne tilnærmingen gjelder ikke bare programvarearbeid, men også alt annet arbeid.

Brukerreviews er innarbeidet både i selve leveransearbeidet og i QA sine tester og inspeksjoner, for å presentere arbeidet som er fullført så langt til sluttbrukerne og få deres løpende vurdering, inkludert identifisering av eventuelle feil i omfang, mangler eller andre avvik, slik at dette kan justeres i neste inkrement.

Kunden er representert i dette prosjektet av følgende interessenter, som skal koordinere deltakelse fra de respektive brukergruppene, og bidra til å lede og delta i reviews som beskrevet nedenfor:

|  |  |  |
| --- | --- | --- |
| **Leder for brukergruppe** | **Lede Reviews** | **Delta i reviews** |
| Kjetil Tronstad Lund (I rollen som prosjekteier) | Gjennomgang av prosjektets anbefaling og modell sammen med relevante interne interessenter | Vurdering av modell og visualisering. |

Prosessen for gjennomføring av brukerreviews er oppsummert nedenfor:

### 1. Når leveranseutkast, bygg, versjoner, inkrementer eller sprinter ferdigstilles, skal det gjennomføres en brukerreview med aktuell brukergruppe. Leveranseteamet vil presentere arbeidet som er underveis til brukergruppen ved hjelp av presentasjoner, gjennomganger, demonstrasjoner, prototyper og mockups der det er hensiktsmessig.
### 2. Brukerkommentarer skal samles inn av brukergruppeleder i en review-tabell, for eksempel ved bruk av malen i vedlegg E.
### 3. Etter at alle kommentarer er samlet inn, under ledelse av brukergruppeleder, skal brukerne fylle inn kolonnen «Brukerprioritet» for å prioritere kommentarene sine ved hjelp av følgende kategorier:

1 = Kritisk for prosjektmålet.

2 = Verdifull kommentar, men anbefales gjennomført i neste prosjekt eller fase.

3 = For senere vurdering; utilstrekkelig informasjon tilgjengelig nå.

### 4. I et separat møte, ledet av leveranse-eier og med deltakelse fra delprosjektleder og prosjektleder ved behov, vil prosjektgruppen gjennomgå brukerprioriteringene og fylle inn kolonnen «Prosjektprioritet» etter samme prioritetsskala, for å bidra med prosjektets vurdering av beste prioritering sett i lys av sannsynlige omfangs-, fremdrifts- og budsjettkonsekvenser.
### 5. Prosjektgruppen skal levere brukertabellen tilbake til brukergruppeleder. Tilleggsdialog som kreves for å etablere (baseline) bruker- og prosjektprioriteringer skal gjennomføres ved behov. Tabellen skal deretter sendes til prosjektsponsor for å ferdigstille kolonnen «Sponsorbeslutning», som viser hvilke punkter som skal vurderes for mulig inkludering i prosjektet.
### 6. Prioritet 1-punktene som sponsoren identifiserer, skal deretter føres inn i endringskontrollprosessen for å gjennomføre en full konsekvensanalyse av foreslått endring. Endringen skal inkluderes i prosjektet, og arbeid igangsettes, bare dersom endringskontrollprosessen ender med en sponsorbeslutning om å implementere kommentaren med full forståelse av tids- og kostnadskonsekvenser, og nødvendig kommunikasjon til alle berørte parter er gjennomført.
### 7. Prosjektgruppen og brukergruppene skal gjennomføre hver iterasjon av brukerreview så raskt som mulig for å minimere konsekvensene av nødvendige endringer. Målet er å ha en ferdigstilt brukertabell for presentasjon til sponsor innen fire dager etter avsluttet review, og at analyse av endringskonsekvensene for sponsor-foreslåtte endringer er fullført innen åtte dager.

# Anskaffelser

Denne seksjonen beskriver tilnærmingen til anskaffelser i «BiteBurst»-prosjektet.

Prosjektet krever anskaffelse av følgende elementer:

*Ingen. Prosjektet har ingen anskaffelser knyttet til gjennomføring.*

# Endringskontrollprosess

Denne seksjonen beskriver prosessen som skal brukes for å sikre at alle foreslåtte endringer i «BiteBurst»-prosjektet håndteres kontrollert og med hensyn til alle konsekvenser av en potensiell endring.

Når denne prosjektplanen er godkjent av sponsor, skal alle endringer i omfang, fremdriftsplan, budsjett eller risikobudsjett gå gjennom den formelle endringskontrollprosessen beskrevet i seksjon 12 – Endringskontrollprosess.

I tillegg må enhver endring i en leveranse, etter at den er baselinet og godkjent under prosjektgjennomføring (for eksempel design og dokumentasjon), også gå gjennom den formelle endringskontrollprosessen, for å sikre at alle konsekvenser identifiseres og at alle berørte parter inkluderes i analysen og kommunikasjonen.

En oppsummering av endringskontrollprosessen er gitt nedenfor:

## 1. Først må endringen dokumenteres formelt i et endringsforespørselsskjema, hvor en kopi er gitt i vedlegg F for enkelhets skyld.
## 2. Dersom endringen er akutt nødvendig på grunn av umiddelbar risiko for prosjektets suksess eller umiddelbar påvirkning på helse, sikkerhet, sikring eller juridisk etterlevelse, kan prosjektleder autorisere endringen umiddelbart og deretter følge opp med en full konsekvensanalyse og kommunikasjon med sponsor, kunde og andre relevante parter så snart det er praktisk mulig.
## 3. Ellers skal det innkalles til et møte i endringskontrollstyret (CCB) for å evaluere endringen med bred deltakelse fra alle parter som kan være berørt, inkludert representanter fra alle prosjektets kjerne- og støttefunksjoner. Hovedformålet med dette første møtet er utelukkende å identifisere alle mulige påvirkningsområder. Prosjektleder skal lede møtet.
## 4. En person som er nærmest endringen skal deretter utpekes til å følge opp etter første møte for å fullføre en analyse og fastslå den samlede effekten av endringen på omfang, fremdriftsplan, budsjett, risiko, anskaffelser og andre berørte prosjektelementer. Muligheter og alternativer for å håndtere endringen skal vurderes. Oppdatert krav-baseline, arbeidsnedbrytningsstruktur (WBS), avhengighetsdiagram (precedence diagram), estimater, Gantt-plan og risikoregister skal utarbeides for endringen og eventuelle alternativer ved behov.
## 5. Endringskontrollstyret skal deretter samles på nytt for å vurdere konsekvensene av endringen og velge beste alternativ dersom mer enn én løsning er mulig.
## 6. Dersom endringskontrollstyret vurderer endringen som nødvendig eller på annen måte nyttig, og den ikke påvirker baselinet omfang, fremdriftsplan, budsjett eller risikobudsjett godkjent av sponsor, kan prosjektleder autorisere endringen.
## 7. Dersom endringen påvirker baselined omfang, fremdriftsplan, budsjett eller risikobudsjett som er godkjent av sponsor, skal endringskontrollstyret, etter godkjenning fra prosjektleder, utarbeide en anbefaling og sende den til sponsor for vurdering. Endringen skal ikke igangsettes før formell skriftlig godkjenning fra sponsor foreligger.
## 8. Når en endring i omfang medfører økning i baselinet fremdriftsplan og budsjett, skal det alltid vurderes alternativer for å fjerne kompenserende omfang for å minimere konsekvensene, og disse alternativene skal presenteres for sponsor og kunde der det er relevant.
## 9. Når det er fattet en beslutning om endringen, skal begrunnelsen for beslutningen og all relevant dokumentasjon lagres i endringsloggens (Change Control Log) arkiv. Hvis endringen godkjennes, skal all nødvendig prosjektdokumentasjon oppdateres, og alle relevante parter skal informeres i tide.

[replace-13-8]Vedlegg A - Krav

Dette vedlegget gir en oversikt over prosjektkravene for «BiteBurst», inkludert unik identifikator, type, eier av hvert krav og foreløpig sporbarhet til leveranser og testtilfeller som skal oppfylle kravene.

Sporbarheten mellom krav og leveranser vil bli raffinert til et mer detaljert nivå etter hvert som design utvikles under gjennomføringen. Tildelingen av testprosedyrer er for øyeblikket på prosedyrenivå, og vil bli raffinert til enkeltstående testtilfeller etter hvert som testdokumentasjonen utvikles.

| **ID** | **Type** | **Requirement** | **Owner** | **Leveranse** | **Test Case** |
| --- | --- | --- | --- | --- | --- |
| K1 | Funksjonalitet | Systemet skal samle inn og strukturere salgsdata fra fire utsalgssteder | Kjetil Lund | Strukturert datasett |  |
| K2 | Funksjonalitet | Optimeringsmodellen skal minimere lagerbeholdning per utsalgssted | Kjetil Lund | Optimaliserings-modell |  |
| K3 | Funksjonalitet | Modellen skal unngå stockout over en 7-dagers periode | Kjetil Lund | Optimaliserings-modell |  |
| K4 | Funksjonalitet | Resultatet skal være lett forståelig og presenteres ved dashboard/graf i tillegg til skriftlig rapport | Kjetil Lund | Visualisering |  |
| K5 | Datakvalitet | Salgsdata skal være komplett og uten mangler | Kjetil Lund | Strukturert datasett |  |
| K6 | Kapasitet | Modellen skal håndtere data fra flere utsalgssteder simultant | Kjetil Lund | Optimaliserings-modell |  |
| K7 | Dokumentasjon | Prosjektet skal dokumenteres i en avsluttende rapport | Kjetil Lund | Forskningsrapport |  |

Vedlegg B - WBS-ordliste

Dette vedlegget gir en WBS-ordliste (WBS-ordliste) med mer informasjon om leveransene som er dokumentert i seksjon 2.4 – Arbeidsnedbrytningsstruktur, inkludert unik identifikator, beskrivelse, eier og kostnadskonto.

| **WBS ID** | **Leveranse** | **Description** | **Owner** | **Cost Account** |
| --- | --- | --- | --- | --- |
| 1 | Prosjekt | Overordnet leveranse | Kjetil Lund |  |
| 1.1 | Steg 1: Proposal |  |  |  |
| 1.1.1 | Utarbeidelse og levering av proposal | Proposal utarbeides, kvalitetssikres og leveres | Kjetil Lund |  |
| 1.2 | Steg 2: Prosjektplan |  |  |  |
| 1.2.1 | Utarbeidelse og levering av prosjektplan | Prosjektplan og Gantt-diagram utarbeides, kvalitetssikres og leveres | Kjetil Lund |  |
| 1.3 | Steg 3: Gjennomføring |  |  |  |
| 1.3.1 | Teori og litteratursøk | Innhenting av relevant litteratur og teori, sammenstilling og uttrekk | Kjetil Lund |  |
| 1.3.2 | Modellering med KI | Modellering av salgsdata for å finne optimal lagermodell | Kjetil Lund |  |
| 1.3.3 | Utarbeidelse av rapport | Utkast til prosjektplan utarbeides, kvalitetssikres og sendes til peer-to-peer review | Kjetil Lund |  |
| 1.4 | Steg4: Avslutning |  |  |  |
| 1.4.1 | Sluttføring av rapport | Prosjektrapport sluttføres basert på tilbakemeldinger og nødvendige endringer gjøres. Prosjektrapport innleveres | Kjetil Lund |  |
| 1.5 | Simulering av data |  |  |  |
| 1.5.1 | Oppsett av Big Ambitions | Big Ambitions må settes opp med nødvendige utsalgssteder, produkter m.m for å kunne benyttes | Kjetil Lund |  |
| 1.5.2 | Oppsett av salgslogg | Opprettelse av salgslogg i csv-format for loggføring av data fra Big Ambitions | Kjetil Lund |  |
| 1.5.3 | Simulering av data | Gjennomføring av selve simuleringen i Big Ambitions for å få datagrunnlag til salgslogg. | Kjetil Lund |  |

Vedlegg C - Format for prosjektets saksliste

For enkel referanse gir dette vedlegget en kopi av formatet for Prosjektets saksliste (Saker List) som brukes til koordinering av det ukentlige saksstatusmøtet beskrevet i seksjon 9.1 – Ukentlige saksstatusmøter. Sakslisten skal spore sakens navn, status, ansvarlig og forventet dato for løsning for hver sak. Dette Microsoft Word-tabellformatet kan enkelt sorteres med kommandoen Layout / Sort etter at nye punkter er lagt til eller oppdatert, slik at sakene kan settes i ønsket rekkefølge etter Ansvarlig / Frist eller Frist / Ansvarlig.

-----

**Prosjekt ABC - Saksliste**

| **Issue** | **Status** | **Lead** | **Due** |
| --- | --- | --- | --- |
| Plassmangel | Ombygging av møterom 5 til arbeidsområde med skrivebord. | Andersen | 2050-01-15 |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

Bruk:

*\* Legg til rader for nye elementer etter behov, og samle deretter sammen etter Lead eller Forfallsdato med menyelementet Tabell / Sorter.*

*\* Skriv inn datoer i formatet ÅÅÅÅ-MM-DD slik at Layout / Sorter-kommandoen fungerer konsekvent.*

Vedlegg D - Format for månedlig prosjektrapport

Dette vedlegget gir formatet for én-sides rapporten som skal brukes i de månedlige prosjektgjennomgangene i seksjon 9.2 – Månedlige prosjektgjennomganger.

Et eksempel på én-sides rapportformat finnes nedenfor. Øvre venstre kvadrant viser et Gantt-utdrag som gir et øyeblikksbilde av status for omfang i forhold til plan. Øvre høyre kvadrant viser status for kostnadsutviklingen. Nedre venstre kvadrant viser status for de tre viktigste sakene og risikoene. Nedre høyre kvadrant gir annen relevant informasjon om status for kunde-/brukergruppene.

Ytterligere informasjon om prosjektets ytelse vil også bli gitt til den månedlige gjennomgangsgruppen ved behov og på forespørsel. En kopi av gjeldende risikoregister vil vanligvis også være tilgjengelig for gjennomgang.

![The image shows a project status/report screen. Left side: - a Gantt chart with task names like “Start,” “Kick-off,” “New Floor Plan 1st Draft,” “New Dept Processes 1st Draft,” “Executive Review & Comment,” and later “Implement New Floor Plan.” - task bars, milestones, and dependencies. Right side: - a milestone/cost summary table with rows “Milestone 1,” “Milestone 2,” “Milestone 3” and columns for CPI and SPI. - totals and earned value metrics like BAC = 7.4M, EAC = 7.8M, ETC = 3.2M, VAC = 0.4M. Bottom section: - text blocks labeled “Issues,” “Risks,” and “Customer,” each with bullet lines for notes and status items.](./BiteBurst%20Lageroptimalisering%20Prosjektplan%20LOG650_images/image_005.png)

Vedlegg E - Mal for brukerreview

For enkel referanse gir dette vedlegget en kopi av review-malen som brukes i review-prosessen oppsummert i seksjon 10.1.2 – Formelle fagfellevurderinger.

-----

**Brukeranmeldelse: [Leveranse ABC Draft 1]**

|  |  |  |  |
| --- | --- | --- | --- |
| **Problem** | **Bruker-prioritet** | **Prosjekt Team prioritet** | **Sponsor- beslutning** |
| Legg til dette... | 1 | 1 | 1 |
| Endre på dette... | 1 | 2 | 1 |
| Fjern dette... | 1 | 1 | 2 |
| Oppgrader dette... | 1 | 1 | 1 |
| Legg til dette... | 2 | 2 | 2 |
| Endre på dette... | 2 | 2 | 2 |
| Fjern dette... | 2 | 2 | 3 |
| Oppgrader dette... | 3 | 3 | 3 |
| Endre på dette... | 3 | 3 | 3 |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

Prioriteter:

1 = Kritisk for prosjektmålet; bør konsekvensanalyseres dersom dette blir sponsorens endelige beslutning.

2 = God idé, men anbefalt for neste prosjekt eller fase.

3 = Registrering for senere undersøkelse.

Vedlegg F - Skjema for endringsforespørsel

For enkel referanse gir dette vedlegget en kopi av det formelle skjemaet for endringsforespørsel som brukes i prosessen oppsummert i seksjon 12 – Endringskontrollprosess.

-----

**Endringsforespørsel**

**Instruksjoner: Dette skjemaet skal fylles ut for enhver forespurt endring i et baselinet og godkjent prosjektelement, inkludert omfang, fremdriftsplan, budsjett, risikobudsjett eller prosjektleveranser, uansett hvor liten endringen er, og sendes via prosjektleder for korrekt vurdering av alle konsekvenser og nødvendig kommunikasjon med alle berørte parter.**

| Prosjekt: |  |
| --- | --- |
| Forespørsel fra: |  |
| Dato for forespørsel: |  |

|  |  |
| --- | --- |
| Ønsket endring: |  |
| Begrunnelse / gevinst: |  |

|  |  |
| --- | --- |
| Kjente leveranser påvirket: |  |
| Kjente krav påvirket: |  |
| Kjente kontrakter påvirket: |  |
| Kjente fremdrift-påvirkninger: |  |
| Kjente kostnadspåvirkninger: |  |

|  |  |
| --- | --- |
| Andre kommentarer: |  |