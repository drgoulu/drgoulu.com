---
title: "Jeu-concours électrique"
slug: "jeu-concours-electrique"
date: 2010-05-17
categories: 
  - "cat2"
tags: 
  - "casse-tetes"
  - "energie"
  - "graphes"
  - "maths"
coverImage: "76fa5e4df5077431227511a63a9e6c9c1.png"
---

Amateurs de casse-têtes, de maths et d'algorithmes, oyez, oyez !

La [Fédération Française des Jeux Mathématiques](http://ffjm.org/) et la [Société de Calcul Mathématique SA](http://www.scmsa.eu) avec l'appui de Réseau de Transport d'Electricité organisent un concours doté de 2000 Euros de prix et ouvert jusqu'au 30 juin 2010.

Il s'agit de concevoir le réseau de lignes électriques nécessaires pour alimenter les villes d'un pays à partir de centrales :

{{< figure src="images/76fa5e4df5077431227511a63a9e6c9c.png" alt="Concours" caption="le pays du concours, carré malgré les apparences" link="images/76fa5e4df5077431227511a63a9e6c9c.png" align="aligncenter" width="528" >}}

Pour ne rien arranger, les centrales sont de puissances différentes et fournissent de la THT, et les villes consomment également des puissances différentes (listées dans la [donnée complète](http://www.ffjm.org/upload/fichiers/ConcoursSCM/jeu_FFJM_SCM_RTE_2010.pdf)), mais doivent être alimentées en HT via des transformateurs à placer à volonté, mais à au moins 1km des villes et pas dans les zones protégées marquées en pointillés.

Pour relier tout ceci, on peut construire des lignes THT de 1GW à 1M€/km (c'est même "obligatoire de mettre une ligne THT lorsque c'est possible", mais cette contrainte me parait peu claire). On doit utiliser des lignes HT de 1 GW à 300K€/km pour alimenter les villes, et dans les zones protégées, on n'a droit qu'à des lignes HT enterrées de 0.3 GW à 1 M€/km.

De plus le tout doit être résistant à une panne : si une centrale, une ligne ou un transfo flanche, les villes doivent toujours être alimentées.

Le vainqueur sera celui qui proposera le réseau satisfaisant à toutes ces contraintes et coutant le moins cher avant le 30 juin, mais mon petit doigt me dit qu'il ne faut pas attaquer le problème le 29...

Et avant de vous lancer dans de p'tits dessins ou de gros calculs, notez encore que tout ce qui précède peut être potentiellement faux et/ou incomplet (je décline toute responsabilité etc etc). Seul le [règlement officiel](http://www.ffjm.org/upload/fichiers/ConcoursSCM/jeu_FFJM_SCM_RTE_2010.pdf) fait foi.

Pour la petite histoire, j'ai trouvé ce concours sur "[Au delà des lignes](http://www.audeladeslignes.com/)", un blog intéressant découvert au moment de la rédaction de ["0.01 Ohm/km"](/2010/03/19/0-01-ohmkm/)
