---
title: "L’énergie de la foudre"
slug: "lenergie-de-la-foudre"
date: 2007-09-09
categories:
  - "Comment"
  - "Pourquoi"
tags: 
  - "electricite"
  - "energie"
  - "foudre"
  - "physique"
coverImage: "4333d9e2e65f2e1e7cd12e847855fead.jpg"
---

{{< figure src="images/1983bc74054465f58c98fe133b2f5120.jpg" link="http://flickr.com/photos/bonsaikiptb/200041749/" >}}

Incorrigible. Voilà le type de question que je me suis posé récemment  dans mon lit, pendant un bel orage nocturne : "Comment récupérer l'énergie de la foudre ?"

[Ce site](http://www.pfgtechnologie.be/Energie/Divers/Foudre/foudre.htm) fournit plein d'informations intéressantes comme:

- la puissance d'un éclair est d'environ 20 GigaWatts, soit 20 centrales nucléaires !
- mais il ne dure que 25 millisecondes, donc l'énergie n'est que de 140 kWh, soit Frs 30.- d'électricité à tout casser...
- Si on parvenait à capter l'énergie de tous les éclairs frappant la France, ça pourrait alimenter environ 5000 ménages. Seulement.

Bref, contrairement à une idée répandue que je partagais jusqu'ici, la foudre n'est pas une source d'énergie renouvelable potentielle et miraculeuse, même si [certains](http://peswiki.com/index.php/Directory:Lightning_Power) veulent y croire...

De plus, même si on le voulait, on ne sait pas comment injecter 20 GW d'un coup sur le réseau. En fait, ça arrive accidentellement lorsque la foudre touche une ligne à haute tension, et en général on se retrouve dans le noir grâce aux "fusibles" du réseau.

L'alternative consisterait à stocker l'énergie pour la restituer plus lentement, mais là encore, il n'y a aujourd'hui aucune technologie permettant de stocker 140 kWh en 25 millisecondes. On pourrait penser à:

1. des condensateurs, mais comment les charger sous la tension de 100'000'000 Volts typique d'un éclair sans qu'il ne claquent ?
2. un anneau supraconducteur. Sur [cette page](http://solaire2000.pagesperso-orange.fr/FAQ/FAQ_TRANSPORTS/SUPRACONDUCTIVITE.htm), on mentionne un anneau en développement qui serait capable de stocker 0,14 kWh en 1 seconde. Il faut encore gagner un facteur 1000 sur la capacité et 40 sur la vitesse. Ce n'est pas pour demain donc
3. une idée folle qui m'a traversé l'esprit, mais il faudrait faire des calculs pour évaluer son degré de folie : l'utilisation de [matériaux piezo-électriques](http://www.polytec-pi.fr/PI%20Universite/Page15%20.htm). Intuitivement l'idée est la suivante:
    1. foudroyer une tas de PZT, ce qui provoque une déformation mécanique très rapide (moins d'une milliseconde) : le matériau se comprime comme un ressort
    2. restituer l'énergie en laissant le piezo se relaxer lentement.
