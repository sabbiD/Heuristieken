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
while read requirement; do conda install --yes $requirement; done < requirements.txt 2>error.log
```

### Structuur (Structure)

Alle Python scripts staan in de folder Code. In de map Data zitten alle input waardes en in de map resultaten worden alle resultaten opgeslagen door de code.

### Test (Testing)

Om de code te draaien met de standaardconfiguratie (bv. brute-force en voorbeeld.csv) gebruik de instructie:

```
python main.py
```

In main.py kun je eerst een land kiezen, waarna hiervoor de datastructurr aangemaakt wordt. Vervolgens kun je een bepaald algoritme runnen voor dit land, waarna de ingekleurde map wordt getoond. Vervolgens kan het algoritme een x aantal keer gerund worden, waarna een CSV bestand met de resultaten wordt aangemaakt en een histogram met de kostenverdeling getoond wordt. 

### Results

Er zijn 5 algoritmes mogelijk om de verdeling van zendmasten voor een bepaald land te maken: randomizer (met constraints), radio, greedy, depth-first en hill-climber.
Per algoritme volgt eerst een uitleg, waarna twee voorbeelden van het algoritme worden getoond (N.B. alle andere CSV files die gegenereerd kunnen worden per algoritme zijn te vinden in de map Results). Hierna volgt een vergelijking van de algoritmes m.b.v. een tabel per land. 

#### Algoritme testcases

##### Randomizer (met constraints)

##### Radio functie

##### Greedy

##### Depth-first

##### Hill-climber

#### Vergelijking algoritmes


## Auteurs (Authors)

* Kajsa Rosenblad, Sebile Demirtas, Sammy Heutz

## Dankwoord (Acknowledgments)

* Angelo Groot
* Wouter Vrielink
* Daan van den Berg
* StackOverflow
