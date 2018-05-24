# Team KGB: Radio Russia

Radio Russia is een project dat probeert om een zo goed mogelijke verdeling van zendmasten te creëren voor de provincies van de landen Oekraine, de Verenigde Staten, China en Rusland.
Er zijn 7 type zendmasten mogelijk.

<img src="http://heuristieken.nl/wiki/images/2/26/Rr_ukraine.png" width = "400" height = "274"/>
Afbeelding 1: De verdeling van provincies van Oekraine./


De eerste stap is om een verdeling te maken voor deze vier landen met zo min mogelijk verschillende types zendmasten.
Hierbij is de vereiste dat een provincie niet hetzelfde type zendmast mag hebben als een naburige provincie.
Een meer evenredige verdeling (waarbij er een evenredig aantal van alle types gebruikt wordt) is hierbij voordeliger.

De volgende stap is om met behulp van onderstaand kostenschema (Tabel 1) de voordeligste inrichting van zendmasten te bepalen.

Tabel 1: Kostenschema 

| Zendertype     | Kosten 1      | Kosten 2  | Kosten 3 | Kosten 4 |
|:--------------:|:-------------:|:---------:| :-------:| :-------:|
| A              | 12            | 19        | 16       | 3        |
| B              | 26            | 20        | 17       | 34       |
| C              | 27            | 21        | 31       | 36       |
| D              | 30            | 23        | 33       | 39       |
| E              | 37            | 36        | 36       | 41       |
| F              | 39            | 37        | 56       | 43       |
| G              | 41            | 38        | 57       | 48       |


## Statespace en heuristieken

### Statespace
De statespace van dit probleem is r^n, waarbij r het aantal types zendmasten is, en n het aantal regio's. Zo is voor Oekraïne bijvoorbeeld de statespace 7^27. 

Het probleem is te vergelijken met het colouring probleem, waarbij de landen van een map worden ingekleurd en naburige landen ook niet dezelfde kleur mogen krijgen. Volgens de four colour theorem (https://en.wikipedia.org/wiki/Four_color_theorem) is elke map in te kleuren met maximaal 4 kleuren. Dus, de statespace zou verkleind kunnen worden tot 4^n. 

Het blijkt in de praktijk echter moeilijk te zijn om met simpele algoritmes een map in te kleuren met maar 4 kleuren.
### BRON
Vaak is 5 een makkelijker aantal.

Bij ons is ook gebleken dat het niet in alle gevallen mogelijk was om maar 4 types zendmasten te gebruiken. Vooral voor Rusland, een land met 83 regio's en maximaal 9 buren, bleek dit erg lastig te zijn.

### Heuristieken

Wij hebben de volgende heuristieken toegepast op ons probleem:

Het aantal stations: bij een aantal algoritmes (random, hill-climber) kan het aantal zendmasten dat gebruikt wordt gekozen worden. Het algoritme wordt dan gedwongen om dat aantal zendmasten te gebruiken. Zoals hierboven vermeld, betekent dit dat in sommige gevallen geen oplossing gevonden kan worden met het aantal zendmasten dat gekozen is.

Volgorde: bij het kleuren van een map is het belangrijk in welke volgorde de regio's ingekleurd worden. We hebben ervoor gekozen om bij de radio, greedy en de depth-first 2 types volgorden te hanteren: een random volgorde, waarbij telkens een willekeurige regio wordt ingekleurd, en largest degree ordering (LDO), waarbij de regio's op volgorde van het aantal buren (meeste buren eerst) worden ingekleurd.

Greedy: het greedy principe probeert steeds de goedkoopst mogelijk zendmast te plaatsen, om de kosten zo laag mogelijk te houden. Dit principe hebben wij toegepast op al onze algoritmes.

## Aan de slag (Getting Started)

### Vereisten (Prerequisites)

Deze codebase is volledig geschreven in [Python3.6.3](https://www.python.org/downloads/). In requirements.txt staan alle benodigde packages om de code succesvol te draaien. Deze zijn gemakkelijk te installeren via pip dmv. de volgende instructie:

```
pip install -r requirements.txt
```

Als dit niet werkt, installeer dan Anaconda of Miniconda en installeer de packages met:

```
while read requirements; do conda install --yes $requirement; done < requirements.txt 2>error.log
```

### Structuur (Structure)

Alle Python scripts staan in de folder Code. In de map Data zitten alle input waardes en in de map Results worden alle resultaten opgeslagen door de code.

In het mapje test_code staan nog 4 algoritmes die uiteindelijk niet gebruikt zijn in main.py en voor de vergelijkingen. kajsa_search, sebile_search en sebile_search_2.0 zijn (semi-zelfbedachte, op depth-first gebaseerde) werkende algoritmes om een verdeling te maken. simulated_annealing is een niet-werkend simulated-annealing algoritme waar we helaas geen tijd meer voor hadden om het werkend te krijgen.

### Test (Testing)

Om de code te draaien met de standaardconfiguratie (bv. brute-force en voorbeeld.csv) gebruik de instructie:

```
python main.py
```

In main.py kun je eerst een land kiezen, waarna hiervoor de datastructuur aangemaakt wordt. Vervolgens kun je een bepaald algoritme runnen voor dit land, waarna de ingekleurde map wordt getoond. Vervolgens kan het algoritme een x aantal keer gerund worden, waarna een CSV bestand met de resultaten wordt aangemaakt en een histogram met de kostenverdeling getoond wordt. Hierna kun je kiezen of je nog een algoritme voor een land wilt runnen. Zo nee, kun je een ander land kiezen of stoppen. 

## Results

Er zijn 5 algoritmes mogelijk om de verdeling van zendmasten voor een bepaald land te maken: randomizer (met constraints), radio, greedy, depth-first en hill-climber.
Per algoritme volgt eerst een uitleg. Vervolgens worden de kosten-resultaten van dit algoritme getoond voor de verschillende versies van het algoritme (bijvoorbeeld het aantal stations of de volgorde waarin de regios bepaald worden) voor de US, voor 100.000 iteraties. Daarna worden twee voorbeelden van het algoritme gegeven, waarbij de resultaten getoond worden van 100.000 iteraties (N.B. alle andere CSV files die gegenereerd kunnen worden per algoritme zijn te vinden in de map Results). Hierna volgt een vergelijking van de algoritmes m.b.v. een tabel per land. 

N.B.1: Bij 100.000 iteraties was kostenschema 2 altijd het voordeligst. De kosten die weergegeven worden zijn dus altijd berekend met schema 2.

N.B.2: Uitleg verdelingsscores: voor een bepaalde verdeling (b.v. een verdeling met 4 zendertypes voor Oekraine (27 provincies), is er een "ultiem" verdelingspercentage, waarbij alle zendertypes evenredig verdeeld zijn. Om de evenredigheid van een bepaalde verdeling te berekenen, hebben we een scorefunctie gemaakt, waarbij de echte verdeling wordt vergeleken met de ultieme verdeling. Hierbij wordt de afwijking van het ultieme percentage opgeteld, waardoor er een score ontstaat. Hoe lager de score, hoe dichter bij de ultieme verdeling.

### Algoritmes

#### Randomizer (met constraints)
De randomizer genereert een random verdeling van zendmasten, met de constraint dat een regio niet hetzelfde type zendmast mag hebben als een naburige regio. Je kan kiezen met hoeveel zendmasten het algoritme wordt uitgevoerd (4, 5, 6 of 7). Dit algoritme resulteert niet in 100% van de gevallen in een geldige verdeling. Als er geen goede verdeling gevonden kon worden, wordt dit gezien als een "fail".

Kostenverdeling US:

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/comparison/randomizer.png" width = "750" height = "500"/>

In bovenstaande grafiek is de verdeling van de kosten voor de US te zien voor 4, 5 of 7 zenders met het randomizer algoritme. Hierin is te zien dat, hoewel minder zendmasten leidt tot lagere kosten, er ook veel meer fails zijn en het algoritme bij 4 zendmasten vrijwel nooit werkt. 

##### Voorbeeld 1: Oekraïne
Aantal zendmasten: 4  

Minimale kosten: 544  
Maximale kosten: 558  

Minimale verdeling: 8.05  
Maximale verdeling: 12.55  

Tijd per succesvolle iteratie (ms): 0.8  

Percentage fails: 92%  

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/ukraine_random_4.png"/>

##### Voorbeeld 2: Rusland
Aantal zendmasten: 5  

Minimale kosten: 1848  
Maximale kosten: 1964  

Minimale verdeling:  
Maximale verdeling:  

Tijd per succesvolle iteratie (ms):  10 ms  
Percentage fails: 93%  

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/russia_random_5.png"/>

#### Radio functie
De radio functie is ons eerste, zelfbedachte algoritme. Hierbij wordt het "vergelijkstation" op 1 gezet. Hierna wordt voor elke regio dit vergelijkstation vergeleken met de stations van de naburige regios. Als het vergelijkstation hetzelfde is als een van de buren, wordt er 1 opgeteld bij het vergelijkstation. Zodra het vergelijkstation niet meer hetzelfde is als een van de buren, krijgt de regio het vergelijkstation. Dit algoritme heeft erg veel weg van het greedy algoritme, waarbij telkens de laagst mogelijke zender gekozen wordt (zie hieronder voor een uitgebreidere uitleg over greedy).

Dit algoritme geeft altijd een goeie verdeling. Er zijn dus geen fails. Wel is het aantal zendtypes dat gebruikt wordt variabel.

Bij de radio functie is het van belang in welke volgorde de zendmasten van de regios geplaats worden. Er zijn twee volgorde-mogelijkheden: random en largest degree ordering. Bij een random volgorde wordt de lijst met regios van te voren geshuffeld, waarna de verdeling gemaakt wordt. Bij largest degree ordering (LDO), wordt de volgorde bepaald op basis van het aantal buren van een regio. De regio met de meeste buren wordt als eerste behandeld, waarna de regio met de op een na meeste buren wordt behandeld enzovoort. 

Kostenverdeling US:

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/comparison/radio.png" width = "750" height = "500"/>

In de bovenstaande grafiek is de verdeling van de kosten voor de US te zien voor het radio algoritme met random en LDO volgorde. LDO volgorde leidt meestal tot een goedkopere oplossing.

##### Voorbeeld 1: China
Volgorde: Random  
Aantal zendmasten: 4: 12%, 5: 78%, 6: 10%, 7: 0.01%  

Minimale kosten: 622  
Maximale kosten: 714  

Minimale verdeling:  
Maximale verdeling:  

Tijd per succesvolle iteratie (ms):  1 ms  
Percentage fails: 0%  

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/china_radio_random.png"/>

#### Voorbeeld 2: US
Volgorde: LDO  
Aantal zendmasten: 4: 59%, 5: 41%, 6: 0%, 7: 0%  

Minimale kosten: 1120  
Maximale kosten: 1167  

Minimale verdeling:  
Maximale verdeling:  

Tijd per succesvolle iteratie (ms):  4 ms  
Percentage fails: 0%  

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/us_radio_ldo.png"/>

#### Greedy
Het greedy algoritme probeert een verdeling te maken die de kosten zo laag mogelijk houdt. Het algoritme geeft eerst de eerste regio de goedkoopste zendmast, waarna voor alle andere regio's de goedkoopst mogelijke (dus zonder dat een regio dezelfde zendmast als een van de buren heeft) zendmast geplaatst wordt. 

Dit algoritme geeft altijd een goeie verdeling. Er zijn dus geen fails. Wel is het aantal zendtypes dat gebruikt wordt variabel.

Bij de greedy functie is het van belang in welke volgorde de zendmasten van de regios geplaats worden. Er zijn twee volgorde-mogelijkheden: random en largest degree ordering. Bij een random volgorde wordt de lijst met regios van te voren geshuffeld, waarna de verdeling gemaakt wordt. Bij largest degree ordering (LDO), wordt de volgorde bepaald op basis van het aantal buren van een regio. De regio met de meeste buren wordt als eerste behandeld, waarna de regio met de op een na meeste buren wordt behandeld enzovoort. 

Kostenverdeling US:

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/comparison/greedy.png" width = "750" height = "500"/>

In bovenstaande grafiek is de verdeling van de kosten voor de US te zien voor de twee volgorde mogelijkheden van het greedy algoritme. Hierin is te zien dat de LDO volgorde meestal tot een goedkopere verdeling leidt dan een random volgorde. 

##### Voorbeeld 1: China
Volgorde: Random  
Aantal zendmasten: 4: 12%, 5: 78%, 6: 10%, 7: 0.01%  

Minimale kosten: 622  
Maximale kosten: 714  

Minimale verdeling:  
Maximale verdeling:  

Tijd per succesvolle iteratie (ms):  1 ms  
Percentage fails: 0%  

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/china_greedy_random.png"/>

#### Voorbeeld 2: Oekraine
Volgorde: LDO  
Aantal zendmasten: 4: 86%, 5: 14%, 6: 0%, 7: 0%  

Minimale kosten: 549  
Maximale kosten: 586  

Minimale verdeling:  
Maximale verdeling:  

Tijd per succesvolle iteratie (ms):  1 ms  
Percentage fails: 0%  

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/ukraine_greedy_ldo.png"/>

#### Depth-first
### UITLEG DEPTH FIRST!

Het Depth-first algoritme geeft niet in alle gevallen een goeie verdeling. Deze worden gemarkeerd als fails. Verder is het aantal types zendmasten variabel.

Bij de radio functie is het van belang in welke volgorde de zendmasten van de regios geplaats worden. Er zijn twee volgorde-mogelijkheden: random en largest degree ordering. Bij een random volgorde wordt de lijst met regios van te voren geshuffeld, waarna de verdeling gemaakt wordt. Bij largest degree ordering (LDO), wordt de volgorde bepaald op basis van het aantal buren van een regio. De regio met de meeste buren wordt als eerste behandeld, waarna de regio met de op een na meeste buren wordt behandeld enzovoort. 

Kostenverdeling US:

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/comparison/dept-first.png" width = "750" height = "500"/>

In bovenstaande grafiek is de kostenverdeling voor de US voor het depth-first algoritme te zien met random en LDO volgorde. Omdat LDO begint met het land met de meeste buren en er maar twee landen met het hoogste aantal buren zijn, zijn er maar 2 verschillende verdelingen. Hierdoor zijn de kosten van de random verdeling over het algemeen lager, omdat bij een random verdeling n aantal volgordes mogelijk zijn, waarbij n het aantal landen is. 

##### Voorbeeld 1: Rusland
Volgorde: Random  
Aantal zendmasten: 4: 0%, 5: 66%, 6: 30%, 7: 0%  

Minimale kosten: 1697  
Maximale kosten: 1782  

Minimale verdeling:  
Maximale verdeling:  

Tijd per succesvolle iteratie (ms):  10 ms  
Percentage fails: 4%  

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/russia_depth_random.png"/>

#### Voorbeeld 2: US
Volgorde: LDO  
Aantal zendmasten: 4: 0%, 5: 50%, 6: 50%, 7: 0%  

Minimale kosten: 1162  
Maximale kosten: 1170  

Minimale verdeling:  
Maximale verdeling:  

Tijd per succesvolle iteratie (ms):  6 ms  
Percentage fails: 0%  

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/us_depth_ldo.png"/>


#### Hill-climber
Het hill-climber algoritme werkt als volgt: er wordt een initiële (random) verdeling van zendmasten gemaakt. Daarna wordt er geteld hoeveel regios een conflict hebben (dus hoeveel regios een zendmast hebben die hetzelfde is als een van de buurregio's). Hierna wordt er uit de conflict regio's een random regio gekozen, waarvan het station zo wordt aangepast dat dit conflict opgelost wordt. Vervolgens wordt er geteld of het totale aantal conflicten nu minder is dan voorheen. Zo ja, wordt de nieuwe staat aangenomen en wordt het volgende random conflict station aangepast. Zo nee, wordt de nieuwe staat niet aangenomen en wordt met de oude staat verder gegaan. 

De hill-climber komt in sommige gevallen in een lokaal maximum terecht waarin geen oplossing mogelijk is. Als dit het geval is wordt het algoritme na 100 iteraties afgebroken en wordt dit geteld als een fail.

Verder kan je bij dit algoritme kiezen met hoeveel stations het gerund wordt (4, 5, 6 of 7).

N.B. Voor Rusland was in 100.000 iteraties geen oplossing mogelijk met 4, 5 of 7 stations. Voor de US was er alleen een verdeling mogelijk met 5 en 7 stations.

Kostenverdeling US:  

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/comparison/hill-climber.png" width = "750" height = "500"/>

In bovenstaande tabel is de kostenverdeling te zien voor de hill-climber voor de US met 5 en 7 zenders. Voor 4 zenders was in 100.000 iteraties geen oplossing te vinden. 5 zenders leidt tot een goedkopere oplossing, maar leidt ook tot veel meer fails.


##### Voorbeeld 1: Oekraine
Aantal zendmasten: 4  

Minimale kosten: 545  
Maximale kosten: 558  

Minimale verdeling:  
Maximale verdeling:  

Tijd per succesvolle iteratie (ms):  2 ms  
Percentage fails: 99.8%  

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/ukraine_hill_4.png"/>

#### Voorbeeld 2: China
Aantal zendmasten: 5  

Minimale kosten: 650  
Maximale kosten: 733  

Minimale verdeling:  
Maximale verdeling:  

Tijd per succesvolle iteratie (ms):  1.5 ms  
Percentage fails: 99.5%  

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/china_hill_5.png"/>

### Vergelijking algoritmes

Hieronder volgt per land een tabel met de resultaten van alle algoritmes, waarin de kosten, verdeling, tijd, aantal stations en fails met elkaar worden vergeleken.

Voor elk land wordt de kostenspace aangegeven om een beter beeld te geven van de resultaten:  
De absolute minimum kosten (zonder enige constraints)  
De absolute maximum kosten (zonder enige constraints)  
Een "middenweg" (waarbij uitgegaan wordt van een optimale evenredige verdeling met 4 types zendmasten, zonder constraints)  

#### Oekraïne
Oekraïne heeft 27 regio's. Het maximaal aantal buren is 7.

Absolute minimum kosten: 3 * 27 = **81**  
Absolute maximum kosten: 58 * 27 = **1566**  
Middenweg: 6.75 * 12 + 6.75 * 26 + 6.75 * 27 + 6.75 * 30 = **641.25**

#### China
China heeft 31 regio's. Het maximaal aantal buren is 8.

Absolute minimum kosten: 3 * 31 = **93**  
Absolute maximum kosten: 58 * 31 = **1798**  
Middenweg: 7.75 * 12 + 7.75 * 26 + 7.75 * 27 + 7.75 * 30 = **736.25**  

#### US
Us heeft 56 regio's. Het maximaal aantal buren is 8.

Absolute minimum kosten: 3 * 56 = **168**  
Absolute maximum kosten: 58 * 56 = **3248**  
Middenweg: 14 * 12 + 14 * 26 + 14 * 27 + 14 * 30 = **1330**  

#### Rusland
Rusland heeft 83 regio's. Het maximaal aantal buren is 9.

Absolute minimum kosten: 3 * 83 = **249**  
Absolute maximum kosten: 58 * 83 = **4814**  
Middenweg: 14.5 * 12 + 14.5 * 26 + 14.5 * 27 + 14.5 * 30 = **1377.50**  

### Conclusie


## Auteurs (Authors)

* Kajsa Rosenblad, Sebile Demirtas, Sammy Heutz

## Dankwoord (Acknowledgments)

* Angelo Groot
* Wouter Vrielink
* Daan van den Berg
* StackOverflow
