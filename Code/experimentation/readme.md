# Experimentation

In deze map staat alle code die gebruikt is voor de visualisatie en experimentatie.

map.py maakt een map met een bepaalde verdeling van radiozendmasten. Deze gebruikt colours.py die de kleuren bepaald voor een bepaalde verdeling.

score.py berekent de verdeling van radiozendmasten voor een bepaalde verdeling en het aantal zend types dat gebruikt is.

costs.py berekent de kosten voor een bepaalde verdeling.

distribution.py geeft alle resultaten voor een bepaalde verdeling voor x iteraties: de verdelingen, de kosten, hoeveel types gebruikt zijn, de evenredigheids score, hoe vaak in x iteraties een x aantal types gebruikt zijn, de gemiddelde tijd per succesvolle iteratie en het aantal fails.

csv_writer.py maakt een csv waarin alle waarden worden opgeslagen voor x iteraties.

plot.py maakt een histogram van de kosten voor x iteraties.

costs_advanced.py bevat twee functies die ingaan op het advanced kostenschema waarbij de kosten van een zendmast type veranderen wanneer een mast van dit type geplaatst wordt.
