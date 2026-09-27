---
title: "Comment localiser les sondes spatiales"
slug: "comment-localiser-les-sondes-spatiales"
date: 2009-06-01
categories:
  - "Comment"
tags: 
  - "aerospace"
  - "pulsars"
coverImage: "./images/00215804ecc0102f0e333984c4c7439c.png"
---

Sur Terre, le [GPS](/2008/09/27/le-gps-pour-les-nuls-satellites-et-signaux/) permet désormais de diriger nos voitures jusqu'à destination, avec une prévision de quelques mètres. Mais comment fait-on la même chose avec des sondes spatiales envoyées à la rencontre d'astres très lointains ?

### Bonnes vieilles méthodes

Tant que la sonde reste en contact avec notre bonne vieille Terre, on peut mesurer le temps mis par un message radio pour aller jusqu'à la sonde et pour que sa réponse nous revienne, ce qui permet de déterminer la distance dans l'axe de visée avec une précision de 3 mètres [[1]](#ref-1). L'[effet Doppler](w:Effet_Doppler-Fizeau) permet même de déterminer la vitesse de la sonde avec la précision incroyable de 0.050 mm/s, mais toujours dans l'axe terre-sonde uniquement.

Dans les deux autres direction requises pour obtenir une position dans l'espace, on peut utiliser les caméras embarquées à bord. [Cassini](/tags/cassini/) peut ainsi se positionner dans un angle de 3 microradians par rapport à ce qu'il observe, donc à 3km près en orbitant à 1 million de km de Saturne.

La précision du positionnement peut encore être améliorée en tenant compte de [l'attraction des corps](/2008/11/16/le-probleme-a-n-corps/) célestes : en observant l'orbite de Cassini dans le système de Saturne, la position de la sonde est connue à moins d'1 km près, ce qui n'est pas mal si l'on considère qu'elle est à plus d'un milliard de kilomètres d'ici.

{{< figure src="./images/00215804ecc0102f0e333984c4c7439c.png" alt="position des 4 sondes ayant dépassé lorbite de Pluton" caption="position des 4 sondes ayant dépassé l" link="http://www.heavens-above.com/SolarEscape.aspx?lat=0&lng=0&loc=Unspecified&alt=0&tz=CET" align="aligncenter" width="400" >}}

### Vers un GPS galactique

Les méthodes actuelles donnent satisfaction dans le système solaire pour des sondes relativement lentes, mais il serait pratique de pouvoir s'affranchir de ces petites contraintes à l'avenir.

Une idée qui fait son chemin [[2]](#ref-2), [[3]](#ref-3), [[4]](#ref-4) serait d'utiliser une sorte de GPS naturel utilisant des [pulsars milliseconde](w:Pulsar_milliseconde) comme émetteurs. Ces résidus d'étoiles sont (probablement) des étoiles à neutrons qui, en s'effondrant, se sont mis à tourner sur eux-mêmes à la vitesse stupéfiante de centaines de tours par seconde, avec une régularité presque digne d'une horloge atomique.

On connait aujourd'hui environ 700 pulsars milliseconde dans notre Galaxie, dont 4 ont la bonne idée d'être "facilement" repérables dans les directions approximatives des sommets d'un tétraèdre, l'idéal pour un système de repérage. En utilisant leurs signaux un peu [comme nous le faisons avec les GPS](/2008/09/27/le-gps-pour-les-nuls-satellites-et-signaux/), il serait possible de déterminer la position d'un vaisseau spatial à 1 mètre près dans une bonne partie de la Voie Lactée, et accessoirement d'avoir l'heure exacte à 4 nanosecondes près [[4]](#ref-4).

### Références:

1. <span id="ref-1"></span>Jeremy Jones "[How do space probes navigate large distances with such accuracy](http://www.scientificamerican.com/article.cfm?id=how-do-space-probes-navig) ?", 2006, Scientific American
2. <span id="ref-2"></span>[Millisecond Pulsars for Starship Navigation](http://www.centauri-dreams.org/?p=8041) sur Centauri Dreams
3. <span id="ref-3"></span>Josep Sala et al, "[Feasibility Study for a Spacecraft Navigation System relying on Pulsar Timing Information](http://www.esa.int/gsp/ACT/doc/ARI/ARI%20Study%20Report/ACT-RPT-MAD-ARI-03-4202-Pulsar%20Navigation-UPC.pdf)",  2004, ESA, ARIADNA 03/4202 report
4. <span id="ref-4"></span>Bartolomé Coll and Albert Tarantola, "[Using Pulsars to Define Space-Time Coordinates](http://arxiv.org/PS_cache/arxiv/pdf/0905/0905.4121v1.pdf)", 2009
