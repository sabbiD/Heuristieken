# Team KGB: Radio Russia

Radio Russia is een project dat probeert om een zo goed mogelijke verdeling van zendmasten te creëren voor de provincies van de landen Oekraine, de Verenigde Staten, China en Rusland.
Er zijn 7 type zendmasten mogelijk.

<img src="http://heuristieken.nl/wiki/images/2/26/Rr_ukraine.png" width = "400" height = "274"/>  
Afbeelding 1: De verdeling van provincies van Oekraine.  
  
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
(http://www.devx.com/dotnet/Article/32927)
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
while read requirement; do conda install --yes $requirement; done < requirements.txt 2>error.log
```

### Structuur (Structure)

Alle Python scripts staan in de folder Code. Deze is onderverdeeld in algorithms, data_structuur, experimentation en test_code. In de map Data zitten alle shapefiles en in de map Results staan alle resultaten.

In het mapje test_code staan nog 4 algoritmes die uiteindelijk niet gebruikt zijn in main.py en voor de vergelijkingen. kajsa_search, sebile_search en sebile_search_2.0 zijn (semi-zelfbedachte, op depth-first gebaseerde) werkende algoritmes om een verdeling te maken. simulated_annealing is een niet-werkend simulated-annealing algoritme waar we helaas geen tijd meer voor hadden om het werkend te krijgen.

### Test (Testing)

Om de code te draaien met de standaardconfiguratie (bv. brute-force en voorbeeld.csv) gebruik de instructie:

```
python main.py
```

In main.py kun je eerst een land kiezen, waarna hiervoor de datastructuur aangemaakt wordt. Vervolgens kun je een bepaald algoritme runnen voor dit land, waarna de ingekleurde map wordt getoond. Vervolgens kan het algoritme een x aantal keer gerund worden, waarna een CSV bestand met de resultaten wordt aangemaakt en een histogram met de kostenverdeling getoond wordt. Hierna kun je kiezen of je nog een algoritme voor een land wilt runnen. Zo nee, kun je een ander land kiezen of stoppen. 

## Results

Er zijn 5 algoritmes mogelijk om de verdeling van zendmasten voor een bepaald land te maken: randomizer (met constraints), radio, greedy, depth-first en hill-climber.  

Per algoritme volgt eerst een uitleg. Vervolgens worden de kosten-resultaten van dit algoritme getoond voor de verschillende versies van het algoritme (bijvoorbeeld het aantal stations of de volgorde waarin de regios bepaald worden) voor de US (100.000 iteraties).  

Daarna worden twee voorbeelden van het algoritme gegeven, waarbij een visualisatie van de map van een juiste verdeling getoond wordt. Hierbij worden vervolgens de resultaten getoond van 100.000 iteraties (N.B. alle andere CSV files die gegenereerd kunnen worden per algoritme zijn te vinden in de map Results).  

Hierna volgt een vergelijking van de verschillende algoritmes m.b.v. een tabel per land.  

N.B.1: Bij 100.000 iteraties was kostenschema 2 altijd het voordeligst. De kosten die weergegeven worden zijn dus altijd berekend met schema 2.  

N.B.2: Uitleg verdelingsscores: voor een bepaalde verdeling (b.v. een verdeling met 4 zendertypes voor Oekraine (27 provincies), is er een "ultiem" verdelingspercentage, waarbij alle zendertypes evenredig verdeeld zijn. Om de evenredigheid van een bepaalde verdeling te berekenen, hebben we een scorefunctie gemaakt, waarbij de echte verdeling wordt vergeleken met de ultieme verdeling. Hierbij wordt de afwijking van het ultieme percentage opgeteld, waardoor er een score ontstaat. Hoe lager de score, hoe dichter bij de ultieme verdeling.  

### Algoritmes

#### Randomizer (met constraints)
De randomizer genereert een random verdeling van zendmasten, met de constraint dat een regio niet hetzelfde type zendmast mag hebben als een naburige regio. Je kan kiezen met hoeveel zendmasten het algoritme wordt uitgevoerd (4, 5, 6 of 7). Dit algoritme resulteert niet in 100% van de gevallen in een geldige verdeling. Als er geen goede verdeling gevonden kon worden, wordt dit gezien als een "fail".  

**Kostenverdeling US:**

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/comparison/randomizer.png" width = "550" height = "300"/>

In bovenstaande grafiek is de verdeling van de kosten voor de US te zien voor 4, 5 of 7 zenders met het randomizer algoritme. Hierin is te zien dat, hoewel minder zendmasten leidt tot lagere kosten, er ook veel meer fails zijn en het algoritme bij 4 zendmasten vrijwel nooit werkt. 

##### Voorbeeld 1: Oekraïne
Aantal zendmasten: **4**  

Minimale kosten: **544**  
Maximale kosten: **558**  

Minimale verdeling: **1.5**  
Maximale verdeling: **11**  

Tijd per succesvolle iteratie (ms): **0.3**  

Percentage fails: **92%**  

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/ukrainemap_random_4.png"/>

##### Voorbeeld 2: Rusland
Aantal zendmasten: **5**  

Minimale kosten: **1848**  
Maximale kosten: **1964**  

Minimale verdeling: **2.4**  
Maximale verdeling: **21.6**  

Tijd per succesvolle iteratie (ms):  **3 ms**  
Percentage fails: **93%**  

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/russiamap_random_5.png"/>

#### Radio functie
De radio functie is ons eerste, zelfbedachte algoritme. Hierbij wordt het "vergelijkstation" op 1 gezet. Hierna wordt voor elke regio dit vergelijkstation vergeleken met de stations van de naburige regios. Als het vergelijkstation hetzelfde is als een van de buren, wordt er 1 opgeteld bij het vergelijkstation. Zodra het vergelijkstation niet meer hetzelfde is als een van de buren, krijgt de regio het vergelijkstation. Dit algoritme heeft erg veel weg van het greedy algoritme, waarbij telkens de laagst mogelijke zender gekozen wordt (zie hieronder voor een uitgebreidere uitleg over greedy).

Dit algoritme geeft altijd een goeie verdeling. Er zijn dus geen fails. Wel is het aantal zendtypes dat gebruikt wordt variabel.

Bij de radio functie is het van belang in welke volgorde de zendmasten van de regios geplaats worden. Er zijn twee volgorde-mogelijkheden: random en largest degree ordering. Bij een random volgorde wordt de lijst met regios van te voren geshuffeld, waarna de verdeling gemaakt wordt. Bij largest degree ordering (LDO), wordt de volgorde bepaald op basis van het aantal buren van een regio. De regio met de meeste buren wordt als eerste behandeld, waarna de regio met de op een na meeste buren wordt behandeld enzovoort. 

**Kostenverdeling US:**

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/comparison/radio.png" width = "550" height = "300"/>

In de bovenstaande grafiek is de verdeling van de kosten voor de US te zien voor het radio algoritme met random en LDO volgorde. LDO volgorde leidt meestal tot een goedkopere oplossing.

##### Voorbeeld 1: China
Volgorde: **Random**   
Aantal zendmasten: **4: 12%, 5: 78%, 6: 10%, 7: 0.01%**  

Minimale kosten: **622**  
Maximale kosten: **713**  

Minimale verdeling: **1.5**   
Maximale verdeling: **25**  

Tijd per succesvolle iteratie (ms):  **0.5 ms**   
Percentage fails: **0%**  

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/chinamap_radio_random.png"/>

#### Voorbeeld 2: US
1120	1167	1137.9684	14	34.8	22.84518	0.001395091	0	{4: 58500, 5: 41500, 6: 0, 7: 0}

Volgorde: **LDO**   
Aantal zendmasten: **4: 59%, 5: 41%, 6: 0%, 7: 0%**  

Minimale kosten: **1120**  
Maximale kosten: **1167**  

Minimale verdeling: **14**  
Maximale verdeling: **34.8**  

Tijd per succesvolle iteratie (ms):  **1 ms**  
Percentage fails: **0%**  

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/us_radio_ldo.png"/>

#### Greedy
Het greedy algoritme probeert een verdeling te maken die de kosten zo laag mogelijk houdt. Het algoritme geeft eerst de eerste regio de goedkoopste zendmast, waarna voor alle andere regio's de goedkoopst mogelijke (dus zonder dat een regio dezelfde zendmast als een van de buren heeft) zendmast geplaatst wordt. 

Dit algoritme geeft altijd een goeie verdeling. Er zijn dus geen fails. Wel is het aantal zendtypes dat gebruikt wordt variabel.

Bij de greedy functie is het van belang in welke volgorde de zendmasten van de regios geplaats worden. Er zijn twee volgorde-mogelijkheden: random en largest degree ordering. Bij een random volgorde wordt de lijst met regios van te voren geshuffeld, waarna de verdeling gemaakt wordt. Bij largest degree ordering (LDO), wordt de volgorde bepaald op basis van het aantal buren van een regio. De regio met de meeste buren wordt als eerste behandeld, waarna de regio met de op een na meeste buren wordt behandeld enzovoort. 

**Kostenverdeling US:**

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/comparison/greedy.png" width = "550" height = "300"/>

In bovenstaande grafiek is de verdeling van de kosten voor de US te zien voor de twee volgorde mogelijkheden van het greedy algoritme. Hierin is te zien dat de LDO volgorde meestal tot een goedkopere verdeling leidt dan een random volgorde. 

##### Voorbeeld 1: China
Volgorde: **Random**  
Aantal zendmasten: **4: 12%, 5: 78%, 6: 10%, 7: 0.01%**  

Minimale kosten: **622**  
Maximale kosten: **714**  

Minimale verdeling: **1.5**  
Maximale verdeling: **25**  

Tijd per succesvolle iteratie (ms):  **0.05 ms**  
Percentage fails: **0%**  

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/china_greedy_random.png"/>

#### Voorbeeld 2: Oekraine
Volgorde: **LDO**  
Aantal zendmasten: **4: 86%, 5: 14%, 6: 0%, 7: 0%**  

Minimale kosten: **549**  
Maximale kosten: **586**  

Minimale verdeling: **1.5**  
Maximale verdeling: **13.6**  

Tijd per succesvolle iteratie (ms):  **0.4 ms**  
Percentage fails: **0%**  

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/ukraine_greedy_ldo.png"/>

#### Depth-first
Het Depth-first algoritme wordt gebruikt om de datastructuur van het land te doorzoeken. Het algoritme begint bij een regio in de regio-lijst (de begin regio kan zelf worden aangegeven en heeft invloed op de resultaten) en kijkt welke zendmasten de buren van de regio hebben. Deze zendmasten worden uitgesloten voor keuze van zendmast voor de huidige regio waarna de goedkoopst mogelijke zendmast wordt gekozen. Deze regio wordt gemarkeerd zodat hier niet meer naar hoeft te worden gekeken. Daarna wordt hetzelfde gedaan voor een buur van de huidige regio. Als alle buren van een regio al zijn gemarkeerd kijkt het algoritme terug naar de vorige regio die is gemarkeerd en kijkt of er een andere buur is die nog niet is gemarkeerd om verder te gaan met die regio. Dit blijft doorgaan tot alle regio's zijn gemarkeerd en alle regio's een zendmast toegekend hebben gekregen.

Het Depth-first algoritme geeft niet in alle gevallen een goeie verdeling. Deze worden gemarkeerd als fails. Verder is het aantal types zendmasten variabel.

Bij de radio functie is het van belang in welke volgorde de zendmasten van de regios geplaats worden. Er zijn twee volgorde-mogelijkheden: random en largest degree ordering. Bij een random volgorde wordt de lijst met regios van te voren geshuffeld, waarna de verdeling gemaakt wordt. Bij largest degree ordering (LDO), wordt de volgorde bepaald op basis van het aantal buren van een regio. De regio met de meeste buren wordt als eerste behandeld. Omdat bij depth-first alleen de beginregio gekozen wordt, zijn er dus maar x mogelijke volgordes en dus verschillende oplossingen, waarbij x het aantal regio's met het maximaal aantal buren is. Oekraïne heeft bijvoorbeeld 3 regio's met 7 buren. Er zijn dus met een LDO volgorde 3 verschillende beginpunten mogelijk. 

**Kostenverdeling US:**

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/comparison/dept-first.png" width = "550" height = "300"/>

In bovenstaande grafiek is de kostenverdeling voor de US voor het depth-first algoritme te zien met random en LDO volgorde. Omdat LDO begint met het land met de meeste buren en er maar twee landen met het hoogste aantal buren zijn, zijn er maar 2 verschillende verdelingen. Hierdoor zijn de kosten van de random verdeling over het algemeen lager, omdat bij een random verdeling n aantal volgordes mogelijk zijn, waarbij n het aantal landen is. 

##### Voorbeeld 1: Rusland
Volgorde: **Random**  
Aantal zendmasten: **4: 0%, 5: 66%, 6: 30%, 7: 0%**  

Minimale kosten: **1697**  
Maximale kosten: **1782**  

Minimale verdeling:  **31.6**  
Maximale verdeling:  **53**  

Tijd per succesvolle iteratie (ms):  **9 ms**  
Percentage fails: **4%**  

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/russia_depth_random.png"/>

#### Voorbeeld 2: US  
Volgorde: **LDO**  
Aantal zendmasten: **4: 0%, 5: 50%, 6: 50%, 7: 0%**  

Minimale kosten: **1162**  
Maximale kosten: **1170**  

Minimale verdeling: **28.8**  
Maximale verdeling: **40**  

Tijd per succesvolle iteratie (ms): **3 ms**  
Percentage fails: **0%**  

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/us_depth_ldo.png"/>


#### Hill-climber
Het hill-climber algoritme werkt als volgt: er wordt een initiële (random) verdeling van zendmasten gemaakt. Daarna wordt er geteld hoeveel regios een conflict hebben (dus hoeveel regios een zendmast hebben die hetzelfde is als een van de buurregio's). Hierna wordt er uit de conflict regio's een random regio gekozen, waarvan het station zo wordt aangepast dat dit conflict opgelost wordt. Vervolgens wordt er geteld of het totale aantal conflicten nu minder is dan voorheen. Zo ja, wordt de nieuwe staat aangenomen en wordt het volgende random conflict station aangepast. Zo nee, wordt de nieuwe staat niet aangenomen en wordt met de oude staat verder gegaan. 

De hill-climber komt in sommige gevallen in een lokaal maximum terecht waarin geen oplossing mogelijk is. Als dit het geval is wordt het algoritme na 100 iteraties afgebroken en wordt dit geteld als een fail.

Verder kan je bij dit algoritme kiezen met hoeveel stations het gerund wordt (4, 5, 6 of 7).

N.B. Voor Rusland was in 100.000 iteraties geen oplossing mogelijk met 4, 5 of 7 stations. Voor de US was er alleen een verdeling mogelijk met 5 en 7 stations.

**Kostenverdeling US:**  

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/comparison/hill-climber.png" width = "550" height = "300"/>

In bovenstaande tabel is de kostenverdeling te zien voor de hill-climber voor de US met 5 en 7 zenders. Voor 4 zenders was in 100.000 iteraties geen oplossing te vinden. 5 zenders leidt tot een goedkopere oplossing, maar leidt ook tot veel meer fails.


##### Voorbeeld 1: Oekraine
Aantal zendmasten: **4**  

Minimale kosten: **543**  
Maximale kosten: **558**  

Minimale verdeling: **1.5**  
Maximale verdeling: **11**  

Tijd per succesvolle iteratie (ms):  **0.6 ms**   
Percentage fails: **85%**   

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/ukraine_hill_4.png"/>

#### Voorbeeld 2: China
Aantal zendmasten: **5**  

Minimale kosten: **645**  
Maximale kosten: **733**  

Minimale verdeling: **3.4**  
Maximale verdeling: **33**   

Tijd per succesvolle iteratie (ms):  **0.9 ms**  
Percentage fails: **35%**  

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

|_Oekraïne_   |Laagste kosten |Laagste evenredigheid     | Tijd in ms     |Fails      |Stations   |
|-------------|---------|-------------|-----------|-----------|---------|
|  ***Random***  |  |     |     |   |
|            4|544  |1.5      |3.69      |92.2%   ||
|            5|564  |2.4      |3.81      |38.88%  ||
|            7|597  |1.7      |3.71      |0.0063%  | |
|             |         |             |           |           |
| ***Radio***   |  |      |      |   ||
|       Random|541  |1.5      |3.44      |0%   |4: 32.2%, 5:66.1%, 6:1.7%|
|          LDO|549  |1.5     |4.16      |0%   |4:85.5%, 5:14.5%|
|             |         |             |           |           |
| ***Greedy***  |  |      |      |   ||
|       Random|541  |1.5      |3.64      |0%   |4:31.88%, 5:66.37%, 6: 1.75%|
|          LDO|549  |1.5      |4.17      |0%   |4:85.56%, 5:14.44%|
|             |         |             |           |           |
| ***Hill-Climber***|  |      |     |   ||
|            4|543  |1.5      |6.96      |84.74%   ||
|            5|562  |2.4      |5.81      |15.43%   ||
|            7|591  |1.7      |5.03      |0.00003%   ||
|             |         |             |           |           |
| ***Depth-first***|  |      |      |   ||
|       Random|542  |11.0      |9.18      |0%   |4:18.39%, 5:81.61%|
|          LDO|557  |12.4      |9.75      |0%   |5:100%|

Tabel 1: Samenvatting resultaten Oekraïne.

#### China
China heeft 31 regio's. Het maximaal aantal buren is 8.

Absolute minimum kosten: 3 * 31 = **93**  
Absolute maximum kosten: 58 * 31 = **1798**  
Middenweg: 7.75 * 12 + 7.75 * 26 + 7.75 * 27 + 7.75 * 30 = **736.25**  

|_China_   |Laagste kosten |Laagste evenredigheid     | Tijd in ms     |Fails      |Stations   |
|-------------|---------|-------------|-----------|-----------|---------|
|  ***Random***  |  |     |     |   |
|            4|625  |1.5      |5.94      |98.29%   ||
|            5|648  |1.6      |5.91      |60.92%  ||
|            7|710  |1.7      |5.90      |0.02%  | |
|             |         |             |           |           |
|  ***Radio***   |  |      |      |   ||
|       Random|622  |1.5      |5.44      |0%   |4:11.75%, 5:78.16%, 6:10%, 7:0.00017%|
|          LDO|623  |1.5     |6.5      |0%   |4:93.35%, 5:6.65%|
|             |         |             |           |           |
| ***Greedy***  |  |      |      |   ||
|       Random|622  |1.5      |5.69      |0%   |4:11.67%, 5:78.12%, 6:10.18%, 7:0.00018%|
|          LDO|623  |1.5      |6.68      |0%   |4:93.36%, 5:6.64%|
|             |         |             |           |           |
|***Hill-Climber***|  |      |     |   ||
|            4|625  |1.5      |13.4      |96.39%   ||
|            5|645  |1.6      |10.43      |34.68%   ||
|            7|691  |1.7      |9.0      |0.00078%   ||
|             |         |             |           |           |
| ***Depth-first***|  |      |      |   ||
|       Random|625  |9.5      |15.43      |3.25%   |4:6.41%, 5:90.33%|
|          LDO|647  |11.2      |17.09      |0%   |5:100%|
Tabel 2: Samenvatting resultaten China.

#### US
Us heeft 56 regio's. Het maximaal aantal buren is 8.

Absolute minimum kosten: 3 * 56 = **168**  
Absolute maximum kosten: 58 * 56 = **3248**  
Middenweg: 14 * 12 + 14 * 26 + 14 * 27 + 14 * 30 = **1330**  

|_US_   |Laagste kosten |Laagste evenredigheid     | Tijd in ms     |Fails      |Stations   |
|-------------|---------|-------------|-----------|-----------|---------|
|  ***Random***  |  |     |     |   |
|            4|1141  |0.0      |12.55      |99.78%   ||
|            5|1212  |1.6      |12.71      |73.53%  ||
|            7|1325  |0.0      |12.95      |2.27%  | |
|             |         |             |           |           |
|  ***Radio***   |  |      |      |   ||
|       Random|1115  |10.0      |12.22      |0%   |4:2.9%, 5:76.1%, 6:20.88%, 7:0.14%|
|          LDO|1120  |14.0     |13.95      |0%   |4:58.5%, 5:41.5%|
|             |         |             |           |           |
|   ***Greedy***  |  |      |      |   ||
|       Random|1114  |10.0      |12.74      |0%   |4:2.94%, 5:76.1%, 6:20.83%, 7:0.14%|
|          LDO|1120  |14.0      |14.28      |0%   |4:58.54%, 5:41.46%|
|             |         |             |           |           |
|***Hill-Climber***|  |      |     |   ||
|            4|1137  |0.0      |26.97      |99.43%   ||
|            5|1193  |1.6      |21.94      |48.37%   ||
|            7|1300  |2.0      |31.13      |0.00071%   ||
|             |         |             |           |           |
| ***Depth-first***|  |      |      |   ||
|       Random|1140  |27.2      |33.29      |12.35%   |5:60.96%, 5:26.7%|
|          LDO|1162  |28.8      |35.0      |0%   |5:49.95%, 6:50.05%|

Tabel 3: Samenvatting resultaten US.

#### Rusland
Rusland heeft 83 regio's. Het maximaal aantal buren is 9.

Absolute minimum kosten: 3 * 83 = **249**  
Absolute maximum kosten: 58 * 83 = **4814**  
Middenweg: 14.5 * 12 + 14.5 * 26 + 14.5 * 27 + 14.5 * 30 = **1377.50**  

|_Rusland_   |Laagste kosten |Laagste evenredigheid     | Tijd in ms     |Fails      |Stations   |
|-------------|---------|-------------|-----------|-----------|---------|
|   ***Random***  |  |     |     |   |
|            4|544  |1.5      |3.69      |92.2%   ||
|            5|564  |2.4      |3.81      |38.88%  ||
|            7|597  |1.7      |3.71      |0.0063%  | |
|             |         |             |           |           |
|  ***Radio***   |  |      |      |   ||
|       Random|541  |1.5      |3.44      |0%   |4: 32.2%, 5:66.1%, 6:1.7%|
|          LDO|549  |1.5     |4.16      |0%   |4:85.5%, 5:14.5%|
|             |         |             |           |           |
| ***Greedy***  |  |      |      |   ||
|       Random|541  |1.5      |3.64      |0%   |4:31.88%, 5:66.37%, 6: 1.75%|
|          LDO|549  |1.5      |4.17      |0%   |4:85.56%, 5:14.44%|
|             |         |             |           |           |
|***Hill-Climber***|  |      |     |   ||
|            4|543  |1.5      |6.96      |84.74%   ||
|            5|562  |2.4      |5.81      |15.43%   ||
|            7|591  |1.7      |5.03      |0.00003%   ||
|             |         |             |           |           |
| ***Depth-first***|  |      |      |   ||
|       Random|542  |11.0      |9.18      |0%   |4:18.39%, 5:81.61%|
|          LDO|557  |12.4      |9.75      |0%   |5:100%|

Tabel 4: Samenvatting resultaten Rusland

### Conclusie


## Auteurs (Authors)

* Kajsa Rosenblad, Sebile Demirtas, Sammy Heutz

## Dankwoord (Acknowledgments)

* Angelo Groot
* Wouter Vrielink
* Daan van den Berg
* StackOverflow
