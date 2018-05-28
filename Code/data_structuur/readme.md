# Data structuur

In deze map staat de code die gebruikt is om de data structuur aangemaakt.

country.py gebruikt shapefiles om een dictionary te maken waarin de keys de regio's zijn en de values een lijst met de buren van deze regio.

data_structure.py zet alle keys en values om naar Regio objecten, waarin de regio en het zendmast type wordt aangegeven. De uiteindelijke dictionary
voor een land bestaat dus uit Regio objecten als keys en een lijst van buur Regio objecten als values.
