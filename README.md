# Team KGB: Radio Russia

Radio Russia is een project dat probeert om een zo goed mogelijke verdeling van zendmasten te creëren voor de provincies van de landen Oekraïne, de Verenigde Staten, China en Rusland.
Er zijn 7 type zendmasten mogelijk.

<img src="http://heuristieken.nl/wiki/images/2/26/Rr_ukraine.png" width = "400" height = "274"/>  
Afbeelding 1: De verdeling van provincies van Oekraïne.  

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


Voorlopige resultaten: uit 100.000 iteraties bleek dat bij ons kostenschema 2 altijd het goedkoopst was. Dit hoeft natuurlijk niet altijd zo te zijn. Als je de kosten van de verschillende types van elk schema bij elkaar optelt (zie hieronder) is schema 2 ook het goedkoopst, wat lijkt te bevestigen dat bij ons dit schema het meest voordelig is. Dit geldt ook als de goedkoopste 4, 5, of 6 types bij elkaar opgeteld worden.

Totaal som alle types per kostenschema:
1: 212, **2: 194**, 3: 246, 4: 254

Omdat bij ons kostenschema 2 het goedkoopst was, zijn de kosten die in de resultaten staan altijd de kosten van dit schema.

## Statespace en heuristieken

### Statespace
De statespace van dit probleem is r^n, waarbij r het aantal types zendmasten is, en n het aantal regio's. Zo is voor Oekraïne bijvoorbeeld de statespace 7^27. 

Dit probleem is te vergelijken met het map colouring probleem, waarbij de landen van een map worden ingekleurd en naburige landen ook niet dezelfde kleur mogen krijgen. Volgens de four colour theorem (https://en.wikipedia.org/wiki/Four_color_theorem) is elke map in te kleuren met maximaal 4 kleuren. Dus, de statespace zou verkleind kunnen worden tot 4^n. 

Het blijkt in de praktijk echter vrij moeilijk te zijn om een map in te kleuren met maar 4 kleuren.
(http://www.devx.com/dotnet/Article/32927)
Vaak is 5 een makkelijker aantal.

Bij ons is ook gebleken dat het niet in alle gevallen mogelijk was om maar 4 types zendmasten te gebruiken. Vooral voor Rusland, een land met 83 regio's en maximaal 9 buren, bleek dit erg lastig te zijn.

### Heuristieken

Wij hebben de volgende heuristieken toegepast op ons probleem:

Het aantal stations: bij een aantal algoritmes (random, hill-climber) kan het aantal zendmasten dat gebruikt wordt gekozen worden. Het algoritme wordt dan "gedwongen" om dat aantal zendmasten te gebruiken. Zoals hierboven vermeld, betekent dit dat in sommige gevallen geen oplossing gevonden kan worden met het aantal zendmasten dat gekozen is.

Volgorde: bij het kleuren van een map is het belangrijk in welke volgorde de regio's ingekleurd worden. We hebben ervoor gekozen om bij de radio, greedy en de depth-first algoritmes 2 verschillede volgordes te hanteren: een random volgorde, waarbij telkens een willekeurige regio wordt ingekleurd, en largest degree ordering (LDO), waarbij de regio's op volgorde van het aantal buren (meeste buren eerst) worden ingekleurd.

Greedy: het greedy principe probeert steeds de goedkoopst mogelijke zendmast te plaatsen, om de kosten zo laag mogelijk te houden. Dit principe hebben wij toegepast op al onze algoritmes.

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

In het mapje test_code staan nog 3 algoritmes die uiteindelijk niet gebruikt zijn in main.py en voor de vergelijkingen. kajsa_search en sebile_search (semi-zelfbedachte, op depth-first gebaseerde) werkende algoritmes om een verdeling te maken. simulated_annealing is een algoritme waar we helaas geen tijd meer voor hadden om het volledig werkend te krijgen.

### Test (Testing)

Om de code te draaien met de standaardconfiguratie (bv. brute-force en voorbeeld.csv) gebruik de instructie:

```
python main.py
```

In main.py kun je eerst een land kiezen, waarna hiervoor de datastructuur aangemaakt wordt. Vervolgens kun je een bepaald algoritme runnen voor dit land, waarna de ingekleurde map wordt getoond. Vervolgens kan het algoritme een x aantal keer gerund worden, waarna een CSV bestand met de resultaten wordt aangemaakt en een histogram met de kostenverdeling getoond wordt. Hierna kun je kiezen of je nog een algoritme voor een land wilt runnen. Zo nee, kun je een ander land kiezen of stoppen. 

## Results

Er zijn 5 algoritmes mogelijk om de verdeling van zendmasten voor een bepaald land te maken: randomizer (met constraints), radio, greedy, depth-first en hill-climber.  

Per algoritme volgt eerst een uitleg. Vervolgens worden de kosten-resultaten van dit algoritme getoond voor de verschillende versies van het algoritme (bijvoorbeeld het aantal stations of de volgorde waarin de regios bepaald worden) voor de US (vor 100.000 iteraties).  

Daarna worden twee voorbeelden van het algoritme gegeven, waarbij een visualisatie van de map van een juiste verdeling getoond wordt. Hierbij worden vervolgens de resultaten getoond van 100.000 iteraties (N.B. alle andere CSV files die gegenereerd kunnen worden per algoritme zijn te vinden in de map Results).  

Hierna volgt een vergelijking van de verschillende algoritmes m.b.v. een tabel per land. Daarna volgt nog een vergelijking van de evenredigheidsscore voor de US. 

Vervolgens volgt de kostenminimalisatie. Hierbij zijn twee algoritmes gebruikt om te kijken of we de kosten nog lager kunnen krijgen.

Ten slotte volgt de conclusie.

N.B.1: Zoals eerder vermeld, was bij 100.000 iteraties kostenschema 2 altijd het voordeligst. De kosten die weergegeven worden zijn dus altijd berekend met schema 2.  

N.B.2: Uitleg verdelingsscores: voor een bepaalde verdeling (b.v. een verdeling met 4 zendertypes voor Oekraine (27 provincies), is er een "ultiem" verdelingspercentage, waarbij alle zendertypes evenredig verdeeld zijn. Om de evenredigheid van een bepaalde verdeling te berekenen, hebben we een scorefunctie gemaakt, waarbij de echte verdeling wordt vergeleken met de ultieme verdeling. Hierbij wordt de afwijking van het ultieme percentage opgeteld, waardoor er een score ontstaat. Hoe lager de score, hoe dichter bij de ultieme verdeling.  

### Algoritmes

#### Randomizer 
##### (met constraints)
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

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/ukrainemap_random_4.png" width = "600" height = "500"/>

##### Voorbeeld 2: Rusland
Aantal zendmasten: **5**  

Minimale kosten: **1848**  
Maximale kosten: **1964**  

Minimale verdeling: **2.4**  
Maximale verdeling: **21.6**  

Tijd per succesvolle iteratie (ms):  **3 ms**  
Percentage fails: **93%**  

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/russiamap_random_5.png" width = "800" height = "500"/>

#### Radio functie
De radio functie is ons eerste, zelfbedachte algoritme. Hierbij wordt het "vergelijkstation" op 1 gezet. Hierna wordt voor elke regio dit station vergeleken met de stations van de naburige regios. Als het vergelijkstation hetzelfde is als een van de buren, wordt er 1 opgeteld bij het vergelijkstation. Zodra het vergelijkstation niet meer hetzelfde is als een van de buren, krijgt de regio het vergelijkstation. Dit algoritme heeft erg veel weg van het greedy algoritme dat [hierna](#greedy) besproken wordt, waarbij telkens de laagst mogelijke zender gekozen wordt. Er zijn twee volgorde-mogelijkheden: random en largest degree ordering ([zie Heuristieken](#heuristieken)).

Dit algoritme geeft altijd een goeie verdeling. Er zijn dus geen fails. Wel is het aantal zendtypes dat gebruikt wordt variabel.

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

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/chinamap_radio_random.png" width = "600" height = "500"/>

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

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/usmap_radio_ldo.png" width = "700" height = "500"/>

#### Greedy
Het greedy algoritme probeert een verdeling te maken die de kosten zo laag mogelijk houdt. Het algoritme geeft de eerste regio de goedkoopste zendmast, waarna voor alle andere regio's de goedkoopst mogelijke (dus zonder dat een regio dezelfde zendmast als een van de buren heeft) zendmast geplaatst wordt. Er zijn twee volgorde-mogelijkheden: random en largest degree ordering ([zie Heuristieken](#heuristieken)). 

Dit algoritme geeft altijd een goeie verdeling. Er zijn dus geen fails. Wel is het aantal zendtypes dat gebruikt wordt variabel.

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

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/chinamap_greedy_random.png" width = "600" height = "500"/>

#### Voorbeeld 2: Oekraine
Volgorde: **LDO**  
Aantal zendmasten: **4: 86%, 5: 14%, 6: 0%, 7: 0%**  

Minimale kosten: **549**  
Maximale kosten: **586**  

Minimale verdeling: **1.5**  
Maximale verdeling: **13.6**  

Tijd per succesvolle iteratie (ms):  **0.4 ms**  
Percentage fails: **0%**  

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/ukrainemap_greedy_ldo.png" width = "600" height = "500"/>

#### Depth-first
Het depth-first algoritme wordt gebruikt om de datastructuur van het land te doorzoeken. Het algoritme begint bij een regio in de regio-lijst (de begin regio kan zelf worden aangegeven en heeft invloed op de resultaten) en kijkt welke zendmasten de buren van de regio hebben. Deze zendmasten worden uitgesloten voor keuze van zendmast voor de huidige regio waarna de goedkoopst mogelijke zendmast wordt gekozen. Deze regio wordt gemarkeerd zodat hier niet meer naar hoeft te worden gekeken. Daarna wordt hetzelfde gedaan voor een buur van de huidige regio. Als alle buren van een regio al zijn gemarkeerd kijkt het algoritme terug naar de vorige regio die is gemarkeerd en kijkt of er een andere buur is die nog niet is gemarkeerd om verder te gaan met die regio. Dit blijft doorgaan tot alle regio's zijn gemarkeerd en alle regio's een zendmast toegekend hebben gekregen.

Het depth-first algoritme geeft niet in alle gevallen een goeie verdeling. Deze worden gemarkeerd als fails. Verder is het aantal types zendmasten variabel.

Bij dit algoritme kan er een keuze gemaakt worden tussen verschillende startpunten. Er zijn twee start-mogelijkheden: random en largest degree ordering. Bij een random volgorde wordt de lijst met regios van te voren geshuffeld, waarna het startpunt gekozen wordt. Bij largest degree ordering (LDO), wordt de volgorde bepaald op basis van het aantal buren van een regio. De regio met de meeste buren wordt als eerste behandeld. Omdat bij depth-first alleen de beginregio gekozen wordt, zijn er dus maar x mogelijke volgordes en dus verschillende oplossingen, waarbij x het aantal regio's met het maximaal aantal buren is. Oekraïne heeft bijvoorbeeld 3 regio's met 7 buren. Er zijn dus met een LDO volgorde 3 verschillende beginpunten mogelijk. Dit betekent dat er uiteindelijk ook maar 3 verschillende verdelingen te maken zijn met depth-first LDO.

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

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/russiamap_depth_random.png" width = "800" height = "500"/>

#### Voorbeeld 2: US  
Volgorde: **LDO**  
Aantal zendmasten: **4: 0%, 5: 50%, 6: 50%, 7: 0%**  

Minimale kosten: **1162**  
Maximale kosten: **1170**  

Minimale verdeling: **28.8**  
Maximale verdeling: **40**  

Tijd per succesvolle iteratie (ms): **3 ms**  
Percentage fails: **0%**  

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/usmap_depth_ldo.png" width = "700" height = "500"/>


#### Hill-climber
Het hill-climber algoritme werkt als volgt: er wordt een initiële (random) verdeling van zendmasten gemaakt. Daarna wordt er geteld hoeveel regio's een conflict hebben (dus hoeveel regio's een zendmast hebben die hetzelfde is als een van de buurregio's). Hierna wordt er uit de conflict regio's een random regio gekozen, waarvan de zendmast zo wordt aangepast dat dit conflict opgelost wordt. Hierbij wordt de laagst mogelijke zendmast gekozen. Vervolgens wordt er geteld of het totale aantal conflicten minder is dan voorheen. Zo ja, wordt deze nieuwe staat aangenomen en wordt het volgende random conflict station aangepast. Zo nee, wordt de nieuwe staat niet aangenomen en wordt met de oude staat verder gegaan. 

De hill-climber komt in sommige gevallen in een lokaal maximum terecht waarin geen oplossing mogelijk is. Als dit het geval is, komt het algoritme in een oneindige loop terecht. Daarom wordt het algoritme als er na 100 iteraties geen geldige oplossng is afgebroken en wordt dit geteld als een fail. 100 is gekozen als een veilige marge, omdat we hebben geteld hoe veel switches de hill climber bij Rusland (het grootste land) ongeveer nodig heeft om tot een geldige oplossing te komen, en dit lag 

Verder kan je bij dit algoritme kiezen met hoeveel stations het gerund wordt (4, 5, 6 of 7).

**Kostenverdeling US:**  

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/comparison/hill-climber.png" width = "550" height = "300"/>

In bovenstaande tabel is de kostenverdeling te zien voor de hill-climber voor de US. 4 zendmast types leidt tot de goedkoopste oplossing, maar bij 4 types failt het algoritme vrijwel altijd.


##### Voorbeeld 1: Oekraïne
Aantal zendmasten: **4**  

Minimale kosten: **543**  
Maximale kosten: **558**  

Minimale verdeling: **1.5**  
Maximale verdeling: **11**  

Tijd per succesvolle iteratie (ms):  **0.6 ms**   
Percentage fails: **85%**   

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/ukrainemap_hill_4.png" width = "600" height = "500"/>

#### Voorbeeld 2: China
Aantal zendmasten: **5**  

Minimale kosten: **645**  
Maximale kosten: **733**  

Minimale verdeling: **3.4**  
Maximale verdeling: **33**   

Tijd per succesvolle iteratie (ms):  **0.9 ms**  
Percentage fails: **35%**  

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/chinamap_hill_5.png" width = "600" height = "500"/>

### Vergelijking algoritmes

Hieronder volgt per land een tabel met de resultaten van alle algoritmes, waarin de kosten, verdeling, tijd, aantal stations en fails met elkaar worden vergeleken.

Voor elk land wordt de kostenspace aangegeven om een beter beeld te geven van de resultaten:  
De absolute minimum kosten (zonder enige constraints).  
De absolute maximum kosten (zonder enige constraints).  
Een "middenweg" (waarbij uitgegaan wordt van een optimale evenredige verdeling met kostenschema 2 met 4 types zendmasten, zonder constraints).  

#### Oekraïne
Oekraïne heeft 27 regio's. Het maximaal aantal buren is 7.

Absolute minimum kosten: 3 * 27 = **81**  
Absolute maximum kosten: 58 * 27 = **1566**  
Middenweg: 6.75 * 19 + 6.75 * 20 + 6.75 * 21 + 6.75 * 23 = **560.25**

|_Oekraïne_   |Laagste kosten |Laagste evenredigheid     | Tijd in ms     |Fails      |Stations   |
|-------------|---------|-------------|-----------|-----------|---------|
|  ***Random***  |  |     |     |   |
|            4|544  |1.5      |0.4      |92.2%   ||
|            5|564  |2.4      |0.4      |38.88%  ||
|            7|597  |1.7      |0.4      |0.63%  | |
|             |         |             |           |           |
| ***Radio***   |  |      |      |   ||
|       Random|541  |1.5      |0.3      |0%   |4: 32.2%, 5:66.1%, 6:1.7%|
|          LDO|549  |1.5     |0.4      |0%   |4:85.5%, 5:14.5%|
|             |         |             |           |           |
| ***Greedy***  |  |      |      |   ||
|       Random|541  |1.5      |0.4      |0%   |4:31.88%, 5:66.37%, 6: 1.75%|
|          LDO|549  |1.5      |0.4      |0%   |4:85.56%, 5:14.44%|
|             |         |             |           |           |
| ***Hill-Climber***|  |      |     |   ||
|            4|543  |1.5      |0.7      |84.74%   ||
|            5|562  |2.4      |0.6      |15.43%   ||
|            7|591  |1.7      |0.5      |0.003%   ||
|             |         |             |           |           |
| ***Depth-first***|  |      |      |   ||
|       Random|542  |11.0      |0.9      |0%   |4:18.39%, 5:81.61%|
|          LDO|557  |12.4      |1.0      |0%   |5:100%|

Tabel 2: Samenvatting resultaten Oekraïne.

#### China
China heeft 31 regio's. Het maximaal aantal buren is 8.

Absolute minimum kosten: 3 * 31 = **93**  
Absolute maximum kosten: 58 * 31 = **1798**  
Middenweg: 7.75 * 19 + 7.75 * 20 + 7.75 * 21 + 7.75 * 23 = **643.25**  

|_China_   |Laagste kosten |Laagste evenredigheid     | Tijd in ms     |Fails      |Stations   |
|-------------|---------|-------------|-----------|-----------|---------|
|  ***Random***  |  |     |     |   |
|            4|625  |1.5      |0.6      |98.29%   ||
|            5|648  |1.6      |0.6      |60.92%  ||
|            7|710  |1.7      |0.6      |2%  | |
|             |         |             |           |           |
|  ***Radio***   |  |      |      |   ||
|       Random|622  |1.5      |0.5      |0%   |4:11.75%, 5:78.16%, 6:10%, 7:0.017%|
|          LDO|623  |1.5     |0.7    |0%   |4:93.35%, 5:6.65%|
|             |         |             |           |           |
| ***Greedy***  |  |      |      |   ||
|       Random|622  |1.5      |0.6     |0%   |4:11.67%, 5:78.12%, 6:10.18%, 7:0.018%|
|          LDO|623  |1.5      |0.7     |0%   |4:93.36%, 5:6.64%|
|             |         |             |           |           |
|***Hill-Climber***|  |      |     |   ||
|            4|625  |1.5      |1.3      |96.39%   ||
|            5|645  |1.6      |1.0      |34.68%   ||
|            7|691  |1.7      |0.9      |0.078%   ||
|             |         |             |           |           |
| ***Depth-first***|  |      |      |   ||
|       Random|625  |9.5      |1.5      |3.25%   |4:6.41%, 5:90.33%|
|          LDO|647  |11.2      |1.7      |0%   |5:100%|

Tabel 3: Samenvatting resultaten China.

#### US
Us heeft 56 regio's. Het maximaal aantal buren is 8.

Absolute minimum kosten: 3 * 56 = **168**  
Absolute maximum kosten: 58 * 56 = **3248**  
Middenweg: 14 * 19 + 14 * 20 + 14 * 21 + 14 * 23 = **1162**  

|_US_   |Laagste kosten |Laagste evenredigheid     | Tijd in ms     |Fails      |Stations   |
|-------------|---------|-------------|-----------|-----------|---------|
|  ***Random***  |  |     |     |   |
|            4|1141  |0.0      |1.3      |99.78%   ||
|            5|1212  |1.6      |1.3      |73.53%  ||
|            7|1325  |0.0      |1.3      |2.27%  | |
|             |         |             |           |           |
|  ***Radio***   |  |      |      |   ||
|       Random|1115  |10.0      |1.2      |0%   |4:2.9%, 5:76.1%, 6:20.88%, 7:0.14%|
|          LDO|1120  |14.0     |1.4      |0%   |4:58.5%, 5:41.5%|
|             |         |             |           |           |
|   ***Greedy***  |  |      |      |   ||
|       Random|1114  |10.0      |1.3      |0%   |4:2.94%, 5:76.1%, 6:20.83%, 7:0.14%|
|          LDO|1120  |14.0      |1.5      |0%   |4:58.54%, 5:41.46%|
|             |         |             |           |           |
|***Hill-Climber***|  |      |     |   ||
|            4|1137  |0.0      |2.7      |99.43%   ||
|            5|1193  |1.6      |2.2      |48.37%   ||
|            7|1300  |2.0      |3.2      |0.071%   ||
|             |         |             |           |           |
| ***Depth-first***|  |      |      |   ||
|       Random|1140  |27.2      |3.3      |12.35%   |5:60.96%, 6:26.7%|
|          LDO|1162  |28.8      |3.5     |0%   |5:49.95%, 6:50.05%|

Tabel 4: Samenvatting resultaten US.

#### Rusland
Rusland heeft 83 regio's. Het maximaal aantal buren is 9.

Absolute minimum kosten: 3 * 83 = **249**  
Absolute maximum kosten: 58 * 83 = **4814**  
Middenweg: 14.5 * 19 + 14.5 * 20 + 14.5 * 21 + 14.5 * 23 = **1203.5**  

|_Rusland_   |Laagste kosten |Laagste evenredigheid     | Tijd in ms     |Fails      |Stations   |
|-------------|---------|-------------|-----------|-----------|---------|
|   ***Random***  |  |     |     |   |
|            4|1714  |5.0     |6.2      |99.99%   ||
|            5|1848  |2.4      |3.5      |93.19%  ||
|            7|2028  |1.7      |3.7      |8.7%  | |
|             |         |             |           |           |
|  ***Radio***   |  |      |      |   ||
|       Random|1676  |13.0      |3.5      |0%   |4: 0.09%, 5:65.11%, 6:34.7%, 7:0.08%|
|          LDO|1700  |23.2     |3.8      |0%   |5:100%|
|             |         |             |           |           |
| ***Greedy***  |  |      |      |   ||
|       Random|1675  |13.0      |3.7      |0%   |4:0.09%, 5:64.9%, 6: 34.9%, 7:0.07%|
|          LDO|1700  |23.2     |4.0      |0%   |5:100%|
|             |         |             |           |           |
|***Hill-Climber***|  |      |     |   ||
|            4|1705  |30     |6.5      |99.99%   ||
|            5|1816  |2.4      |5.7      |71.85%   ||
|            7|1962  |1.7      |4.4      |0.4%   ||
|             |         |             |           |           |
| ***Depth-first***|  |      |      |   ||
|       Random|1697  |31.6      |9.9      |3.5%   |5:66.1%, 6:30.37%|
|          LDO|1744  |37.6      |11.3      |0%   |5:100%|

Tabel 5: Samenvatting resultaten Rusland

### Evenredigheid

De gemiddelde evenredigheidsscore van de verschillende versies van de algoritmes voor de US zijn te zien in onderstaande afbeelding. Hierbij is de score van de radiofunctie verborgen achter die van het greedy algoritme, omdat deze dezelfde scores hebben.

Er is duidelijk te zien dat de randomizer en het hill-climber algoritme de beste verdelingsscore geven, terwijl de depth first een vrij slechte score geeft. Dit komt waarschijnlijk doordat de depth first een andere volgorde hanteert dan de andere algoritmes, waarbij wij alleen het startpunt bepalen i.p.v. de hele volgorde. Dat de randomizer een goede evenredigheidsscore geeft is logisch, omdat deze geen gebruik maakt van een greedy heuristiek, maar random een mogelijk type kiest. We weten niet zeker waarom de hill climber zo'n goede evenredigheidsscore gaf, omdat deze ook met het greedy heuristiek zendmasten plaatst. Dit zouden we graag in de toekomst verder onderzoeken.

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/comparison/evenredigheid.png" width = "550" height = "300"/>


### Kosten minimalisatie
#### Hill climber costs
Het hill climber costs algoritme is een hill climber algoritme dat de kosten probeert te minimaliseren. Dit algoritme werkt vrijwel op dezelfde manier als de [hill climber](#hill-climber), alleen gebruikt dit algoritme een geldige verdeling van radiozendmasten met x aantal types als beginpunt en in plaats van conflicten te minderen probeert het de kosten te verminderen. 

De begin verdeling wordt gemaakt met de [randomizer](#randomizer).  
Hierna gaat dit algoritme voor een random regio het zendmast type proberen te veranderen. Vervolgens wordt berekend of deze verandering tot lagere of hogere kosten leidt. Als de verandering tot lagere kosten leidt, wordt deze aangenomen als de nieuwe staat. Als de verandering niet tot lagere kosten leidt, wordt doorgegaan met de oude staat. Dit wordt 100 keer gedaan.  

Om te kijken of dit algoritme uiteindelijk tot lagere kosten leidt dan de random verdeling waarmee begonnen wordt, hebben we dit algoritme 100 keer gerund voor elk land met 4, 5 en 7 regio’s. Hierbij hebben we gekozen voor maar 100 iteraties, omdat dit algoritme uitgaat van een **geldige** random verdeling. De randomizer gaf bijvoorbeeld in het geval van Rusland voor 4 stations maar 1 keer in 100,000 iteraties een geldige oplossing. Hierdoor kan dit algoritme dus erg lang duren, omdat hij doorgaat tot er een geldige random oplossing is voor het aantal stations. Uitgaande van Rusland, zouden er bij 100,000 iteraties dus ongeveer 100,000 x 100,000 iteraties nodig zijn. Als 1 iteratie 1 milliseconde zou duren, zou dit ongeveer 115 dagen in beslag nemen.  

Omdat we uitgaan van een geldige verdeling en het vrij snel gaat, hebben wij daarom gekozen voor 100 iteraties om te kijken hoe de hill climber costs het doet tegenover de random verdeling.  

N.B. Dit algoritme begint met een random geldige verdeling met het aantal zenders dat gekozen wordt, en daarna probeert het de kosten te verminderen door een random regio te kiezen waarbij het laagst mogelijke station gekozen wordt. Hierdoor kan het zo zijn dat de uiteindelijke verdeling minder zendtypes gebruikt dan het gekozen aantal. Daarom wordt de verdeling in de tabel erbij vermeld.

In de tabel hieronder is de vergelijking van de hill climber costs tegenover de randomizer te zien.

|             |Randomizer |Hill climber costs     | Stations hill climber costs                | 
|-------------|-----------|-----------------------|--------------------------------------------|
|***Ukraine***|           |                       |                                            |      
|            4|544        |541                    |4: **100%**                                 | 
|            5|564        |542                    |4: **33%**, 5: **67%**                      | 
|            7|597        |542                    |4: **21%**, 5: **59%**, 6: **12%**, 7: **8%**| 
|             |           |                       |                                            | 
|***China***  |           |                       |                                            | 
|            4|625        |624                    |4: **100%**                                 | 
|            5|648        |629                    |4: **7%**, 5: **93%**                       | 
|            7|710        |627                    |4: **4%**, 5: **52%**, 6: **21%**, 7: **8%**| 
|             |           |                       |                                            | 
|***US***     |           |                       |                                            | 
|            4|1141       |1125                   |4: **100%**                                 | 
|            5|1212       |1146                   |4: **0%**, 5: **100%**                      | 
|            7|1325       |1155                   |4: **0%**, 5: **2%**, 6: **21%**, 7: **77%**| 
|             |           |                       |                                            | 
|***Rusland*** |          |                       |                                            | 
|            4|1714       |1683                   |4: **100%**                                 | 
|            5|1848       |1743                   |4: **0%**, 5: **100%**                      | 
|            7|2028       |1827                   |4: **0%**, 5: **0%**, 6: **2%**, 7: **98%** | 
|             |           |                       |                                            | 

Tabel 6: Vergelijking randomizer vs hill climber costs

In bovenstaande tabel is te zien dat de hill climber costs consequent een goedkopere indeling weet te genereren dan de laagst mogelijke kosten van de randomizer na 100,000 iteraties. Dit kan deels te maken hebben met het feit dat de hill climber costs in sommige gevallen minder zendtypes gebruikt dan het gekozen aantal, maar zelfs bij 4 stations (waarbij beide algoritmes altijd 4 stations gebruiken) zijn de kosten van de hill climber costs lager dan die van de randomizer. Dit algoritme kan dus een gegenereerde verdeling verbeteren en de kosten minimaliseren.

Een toekomstige stap zou zijn om dit algoritme ook te testen met een verdeling die gemaakt is door de andere algoritmes (radio, greedy, depth-first en de normale hill climber), om te kijken of de kosten hierbij ook geminimaliseerd zouden kunnen worden. 

#### Depth first limit

Het depth-first limit algoritme is ook een recursief algoritme net zoals de [depth-first](#depth-first) hierboven beschreven. 
Het verschil met dat algoritme is dat er nu per regio een limiet wordt gesteld aan de prijs van de zendmast die er geplaatst kan worden.

Op basis van het aantal buren van de regio wordt het kostenschema aangepast. Als er bijvoorbeeld 4 buren zijn dan wordt het limiet gebaseerd op de 4 laagste kosten uit het kostenschema, 7 buren de 7 laagste kosten uit het kostenschema wat in dit geval het hele schema is. Dit limiet zou er voor moeten zorgen dat de kosten laag worden gehouden.

Hierna worden alle prijzen van de zendmasttypes in dit nieuwe kostenschema bij elkaar opgeteld en gedeeld door het aantal buren van de regio. Dit is het limiet voor de regio.
Aan de hand van dit limiet wordt bij elke plaatsing van zendmast gekeken of dit limiet wordt overschreden. Als dit het geval is springt het algoritme naar een buur van de huidige regio, zonder de huidige regio een zendmast te geven en gaat daarna verder met de buur. Als dit limiet niet wordt overschreden krijgt de regio de goedkoopst mogelijke zendmast (mogelijkheid is gebaseerd op wat de buren hebben).

In de tabel hieronder is de vergelijking van de [depth-first](#depth-first) tegenover de depth-first limit te zien.

De resultaten hieronder gebaseerd op Oekraïne, laten zien dat de depth-first limit inderdaad voor een verlaging in de kosten zorgt vergeleken met de depth-first. Wat verder opvalt is dat ook de verdeling een verbetering is vergeleken met de depth-first en dat er ook verdelingen met 4 zendmasttypes worden gemaakt ipv. alleen met 5 zendmasttypes bij de depth-first. Echter lijkt de depth-first limit er wel 2 keer zo lang over te doen. Deze resultaten zijn vergelijkbaar met die van de rest van de landen. In de gevallen van China en Rusland leidt de depth-first limit tot een verlaging in de kosten (kosten van 645 en 1700 respectievelijk), en in het geval van de US blijven de kosten gelijk.

|Oekraïne|Depth-first (LDO) |Depth-first limit (LDO)|
|--------|------------------|-----------------------|
|Laagste kosten| 557| 542|
|Hoogste kosten| 572| 572|
|Laagste verdeling| 12.4| 7.0|
|Hoogste verdeling| 16.4| 16.4|
|Tijd in ms|1.0| 2.0|
|Fails| 0%| 0%|
|Stations| 5:100%| 4:12.35%, 5: 87.65%|

Tabel 7: Depth-first vs. depth-first limit

#### Advanced costs
We hebben nog een poging gedaan om het advanced kostenschema uit te werken. We hebben dit helaas nog niet kunnen runnen en we hebben hier geen resultaten voor, maar we hebben wel een functie die de kosten lineair af laat lopen en een die de kosten logaritmisch af laat lopen. 

Deze functies zijn te vinden in het mapje experimentation.

Onze verwachting is dat, terwijl kostenschema 2 bij ons altijd het goedkoopst was, bij de advanced functies (en dan vooral de logaritmische functie) een ander kostenschema wellicht goedkoper zal zijn. Daarbij verwachten we dat bij een lineair schema een minder evenredige verdeling goedkoper uit zou kunnen pakken.

### Conclusie
De beste kostendistributies worden door het greedy algoritme en de radio functie gegenereerd. De twee functies lijken veel op elkaar en er is ook maar een klein verschil tussen de resultaten van de twee algoritmes. De radio functie is onze eigen functie die we helemaal in het begin handmatig in elkaar hebben gezet. Uiteindelijk kwamen we erachter dat deze hetzelfde principe hanteert als een greedy algoritme, alleen op een andere manier geïmplementeerd. Toch is het leuk dat deze functie zo goed blijkt te presteren, omdat we tijdens het maken niet bezig waren met heuristieken of algoritmes, maar puur met het oplossen van het probleem en een juiste verdeling vinden.

Uit onze resultaten blijkt dat een algoritme dat word gerund met een random volgorde soms lagere kosten geeft, en ook een betere evenredigheid dan een largest degree order volgorde. Als je echter naar de kosten distributies kijkt zie je ook dat de LDO distributie vaker lagere kosten genereert dan de random versies. De randomizer geeft een enkele keer zeer lage kosten, maar over het algemeen presteert dit algoritme dus minder goed dan LDO.

Het is logisch dat de randomizer en hill-climber met 4 stations goede kosten genereren, omdat de kostenschemas lager zijn voor stations 1-4. Jammer genoeg doen de algoritmes dit zelden; ze failen bij de grotere landen 99.99 % van de keren. De hill climber doet het echter beter dan de randomizer met 5 stations, hij failt dan minder vaak dan de randomizer. De radio en greedy functies failen nooit maar zijn variabel in het aantal type zendmasten dat gebruikt wordt. Hierbij gebruiken ze vaak 5 stations en blijkt het dus moeilijk om een oplossing met 4 stations te genereren.

Zoals hierboven vermeld, is de evenredigheid het beste voor de hill climber en de randomizer, en het slechtste voor de depth first.

De kosten kunnen geminimaliseerd worden door de hill climber costs op een random verdeling toe te passen, en de depth first limit resulteert ook vaak in lagere kosten dan de normale depth first.

#### Toekomstig onderzoek
- Andere algoritmes: We zouden graag de simulated annealing werkend krijgen en de kajsa search en sebile search verder uitwerken.

- In plaats van de regio's inkleuren zou het interessant zijn om de buren van een regio in te kleuren, zoals in de kajsa search.

- We zouden graag meer experimenteren met de evenredigheidsverdeling en onze algoritmes aanpassen op het maken van een meer evenredige verdeling, omdat we nu vooral gefocust hebben op de kosten.

- De LDO van de depth first is nu zo geprogrammeerd dat hij zoveel verschillende mogelijkheden heeft als het aantal regio's met het maximaal aantal buren, waardoor er niet veel spreiding is. We zouden hier graag bij willen nadenken over een manier om de volgorde zo te bepalen dat er meer verschillende oplossingen mogelijk zijn. Bijvoorbeeld door de volgende buur te kiezen op basis van het aantal buren dat deze buur heeft, of door regio's met meer dan 5 buren als startpunt te nemen i.p.v. alleen die met het hoogste aantal buren.

- Andere volgordes: we zouden ook nog kunnen kijken naar andere volgordes dan de random en de LDO, bijvoorbeeld door bij de randen of juist het midden van de kaart te beginnen, of juist te beginnen bij regios met het minst aantal buren.

- We zouden de hill climber costs ook graag baseren op een beginstaat gegenereerd door de andere algoritmes, om te kijken of hier ook kosten minimalisatie mogelijk is. 

- We zouden ook willen kijken of we "algoritme op algoritme" kunnen laten runnen, bijvoorbeeld door de depth first search te laten beginnen op een geldige greedy verdeling. 

## Auteurs (Authors)

* Kajsa Rosenblad, Sebile Demirtaş, Sammy Heutz

## Dankwoord (Acknowledgments)

* Angelo Groot
* Wouter Vrielink
* Daan van den Berg
* StackOverflow
