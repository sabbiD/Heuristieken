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

Alle Python scripts staan in de folder Code. In de map Data zitten alle input waardes en in de map resultaten worden alle resultaten opgeslagen door de code.

### Test (Testing)

Om de code te draaien met de standaardconfiguratie (bv. brute-force en voorbeeld.csv) gebruik de instructie:

```
python main.py
```

In main.py kun je eerst een land kiezen, waarna hiervoor de datastructuur aangemaakt wordt. Vervolgens kun je een bepaald algoritme runnen voor dit land, waarna de ingekleurde map wordt getoond. Vervolgens kan het algoritme een x aantal keer gerund worden, waarna een CSV bestand met de resultaten wordt aangemaakt en een histogram met de kostenverdeling getoond wordt. Hierna kun je kiezen of je nog een algoritme voor een land wilt runnen. Zo nee, kun je een ander land kiezen of stoppen. 

### Results

Er zijn 5 algoritmes mogelijk om de verdeling van zendmasten voor een bepaald land te maken: randomizer (met constraints), radio, greedy, depth-first en hill-climber.
Per algoritme volgt eerst een uitleg. Vervolgens worden de kosten-resultaten van dit algoritme getoond voor de verschillende versies van het algoritme (bijvoorbeeld het aantal stations of de volgorde waarin de regios bepaald worden), voor 100.000 iteraties. Daarna worden twee voorbeelden van het algoritme gegeven, waarbij de resultaten getoond worden van 100.000 iteraties (N.B. alle andere CSV files die gegenereerd kunnen worden per algoritme zijn te vinden in de map Results). Hierna volgt een vergelijking van de algoritmes m.b.v. een tabel per land. 

N.B.1: Bij 100.000 iteraties was kostenschema 2 altijd het voordeligst. De kosten die weergegeven worden zijn dus altijd berekend met schema 2.

N.B.2: Uitleg verdelingsscores: voor een bepaalde verdeling (b.v. een verdeling met 4 zendertypes voor Oekraine (27 provincies), is er een "ultiem" verdelingspercentage, waarbij alle zendertypes evenredig verdeeld zijn. Om de evenredigheid van een bepaalde verdeling te berekenen, hebben we een scorefunctie gemaakt, waarbij de echte verdeling wordt vergeleken met de ultieme verdeling. Hierbij wordt de afwijking van het ultieme percentage opgeteld, waardoor er een score ontstaat. Hoe lager de score, hoe dichter bij de ultieme verdeling.

#### Algoritmes

##### Randomizer (met constraints)
De randomizer genereert een random verdeling van zendmasten, met de constraint dat een regio niet hetzelfde type zendmast mag hebben als een naburige regio. Je kan kiezen met hoeveel zendmasten het algoritme wordt uitgevoerd (4, 5, 6 of 7). Dit algoritme resulteert niet in 100% van de gevallen in een geldige verdeling. Als er geen goede verdeling gevonden kon worden, wordt dit gezien als een "fail".

--> Grafiekjes hier met de normale verdelingen. 
Klein uitlegje over grafiekjes + soort van tussen conclusie?

###### Voorbeeld 1: Oekraïne
Aantal zendmasten: 4

Minimale kosten: 544
Maximale kosten: 558

Minimale verdeling: 8.05
Maximale verdeling: 12.55

Tijd per succesvolle iteratie (ms): 0.8

Percentage fails: 92%

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/ukraine_random_4.png"/>

###### Voorbeeld 2: Rusland
Aantal zendmasten: 5

Minimale kosten: 1848
Maximale kosten: 1964

Minimale verdeling:
Maximale verdeling:

Tijd per succesvolle iteratie (ms):  10 ms
Percentage fails: 93%

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/russia_random_5.png"/>

##### Radio functie
De radio functie is ons eerste, zelfbedachte algoritme. Hierbij wordt het "vergelijkstation" op 1 gezet. Hierna wordt voor elke regio dit vergelijkstation vergeleken met de stations van de naburige regios. Als het vergelijkstation hetzelfde is als een van de buren, wordt er 1 opgeteld bij het vergelijkstation. Zodra het vergelijkstation niet meer hetzelfde is als een van de buren, krijgt de regio het vergelijkstation. Dit algoritme heeft erg veel weg van het greedy algoritme, waarbij telkens de laagst mogelijke zender gekozen wordt (zie hieronder voor een uitgebreidere uitleg over greedy).

Dit algoritme geeft altijd een goeie verdeling. Er zijn dus geen fails. Wel is het aantal zendtypes dat gebruikt wordt variabel.

Bij de radio functie is het van belang in welke volgorde de zendmasten van de regios geplaats worden. Er zijn twee volgorde-mogelijkheden: random en largest degree ordering. Bij een random volgorde wordt de lijst met regios van te voren geshuffeld, waarna de verdeling gemaakt wordt. Bij largest degree ordering (LDO), wordt de volgorde bepaald op basis van het aantal buren van een regio. De regio met de meeste buren wordt als eerste behandeld, waarna de regio met de op een na meeste buren wordt behandeld enzovoort. 

--> Grafiekjes hier met de normale verdelingen. 
Klein uitlegje over grafiekjes + soort van tussen conclusie?

###### Voorbeeld 1: China
Volgorde: Random
Aantal zendmasten: 4: 12%, 5: 78%, 6: 10%, 7: 0.01%

Minimale kosten: 622
Maximale kosten: 714

Minimale verdeling:
Maximale verdeling:

Tijd per succesvolle iteratie (ms):  1 ms
Percentage fails: 0%

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/china_radio_random.png"/>

##### Voorbeeld 2: US
Volgorde: LDO
Aantal zendmasten: 4: 59%, 5: 41%, 6: 0%, 7: 0%

Minimale kosten: 1120
Maximale kosten: 1167

Minimale verdeling:
Maximale verdeling:

Tijd per succesvolle iteratie (ms):  4 ms
Percentage fails: 0%

<img src="https://github.com/sabbiD/Heuristieken/blob/master/Results/us_radio_ldo.png"/>


##### Greedy

###### Voorbeeld 1: US

##### Voorbeeld 2: Oekraine


##### Depth-first

###### Voorbeeld 1: Rusland

##### Voorbeeld 2: US


##### Hill-climber

###### Voorbeeld 1: Oekraine

##### Voorbeeld 2: China

#### Vergelijking algoritmes

##### Oekraïne

##### China

##### US

##### Rusland

#### Conclusie


## Auteurs (Authors)

* Kajsa Rosenblad, Sebile Demirtas, Sammy Heutz

## Dankwoord (Acknowledgments)

* Angelo Groot
* Wouter Vrielink
* Daan van den Berg
* StackOverflow
