---
title: "Calcul Distribué avec BOINC"
slug: "calcul-distribue-avec-boinc"
date: 2007-01-20
categories: 
  - "cat2"
tags: 
  - "futur"
coverImage: "c14e7902a08802229cdbcba55f05a6ef.gif"
---

Les millions d'ordinateurs interconnectés sour internet font à 90% la même chose : RIEN.

Utiliser la fabuleuse puissance de calcul de ces machines pendant que leur utilisateur n'y a pas recours, c'est le principe du [calcul distribué, ou calcul réparti](http://fr.wikipedia.org/wiki/Calcul_r%C3%A9parti).

Le désormais célèbre projet [SETI@Home](http://setiathome.berkeley.edu/) a été le premier a appliquer cette idée dès 1998 pour identifier des signaux extraterrestres intelligents dans les ondes recues du Cosmos, sans succès car comme je le démontre dans le "[Principe de Saturation Cubique](/1999/10/23/psc/)", des extraterrestres intelligents font très attention de ne pas émettre de signaux.

Mais il existe heureusement des projets plus constructifs :

- [GIMPS](http://www.mersenne.org/) recherche de très grands [nombres premiers](/2007/01/20/les-nombres-premiers/) et les trouve ! Tous les nombres premiers record depuis 1996 ont été trouvés grâce à ce projet. Si par chance le premier nombre premier de plus de 10 millions de décimales est trouvé sur votre ordinateur, vous empocherez les [$100'000 de récompense offerts par l'Electronic Frontier Fundation](http://www.eff.org/awards/coop).
- [Folding@Home](http://folding.stanford.edu/) qui calcule la façon dont les protéines se plient, susceptible de causer certaines maladies comme Alzheimer, et éventuellement de les soigner un jour.
- et les nombreux projets "BOINC"

![](images/c14e7902a08802229cdbcba55f05a6ef.gif)Depuis quelques temps, une plate-forme logicielle commune à de nombreux projets s'impose : [BOINC](http://boinc.berkeley.edu/).

Pour chaque propriétaire de PC, il suffit d'installer un seul logiciel pour offrir la puissance de son ordinateur à plusieurs projets à but non lucratif de son choix, par exemple:

- [Rosetta@Home](http://boinc.bakerlab.org/rosetta/), un projet concurrent (ou complémentaire ?) à Folding@Home.
- [MalariaControl.net](http://www.malariacontrol.net/) est un projet d'origine Suisse qui réalise des simulations épidémiologique de la malaria pour définir une stratégie de combat contre la maladie
- [ClimatePrediction.net](http://climateprediction.net/) calcule l'évolution climatique
- [PrimeGrid](http://primegrid.com/) recherche les grands nombres premiers mais avec moins de succès que GIMPS jusqu'ici. Par contre, le sous projet [Twin Prime Search](http://www.twinprimesearch.org/) a permis de trouver les plus grands [nombres premiers jumeaux](/2007/01/20/les-nombres-premiers/) connus
- [SETI@Home](http://setiathome.berkeley.edu/), qui s'est mis à utiliser BOINC depuis 2005, si vous voulez vraiment que votre processeur chauffe à chercher des signaux qui n'existent pas ...
- [Einstein@Home](http://einstein.phys.uwm.edu/) , qui recherche des siganux provenant d'étoiles à neutrons en rotation dans des mesures d'ondes gravitationnelles, et là, on devrait en trouver un jour.
- et il existe encore de très nombreux autres projets basées sur BOINC

Comme BOINC tourne sur le PC en "basse priorité", il n'interfère donc pas avec le travail habituel. Certains projets BOINC offrent en prime un économiseur d'écran qui affiche des infos sur le calcul effectué sur votre ordinateur, mais jusqu'ici je n'en ai pas trouvé qui puisse rivaliser avec [Electric-Sheep.](http://electricsheep.org/)
