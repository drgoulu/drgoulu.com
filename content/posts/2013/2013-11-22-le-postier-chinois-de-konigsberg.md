---
title: "Le postier chinois de Königsberg"
slug: "le-postier-chinois-de-konigsberg"
date: 2013-11-22
categories: 
  - "cat1"
tags: 
  - "casse-tetes"
  - "graphes"
  - "maths"
  - "traduction"
  - "tsp"
coverImage: "ed585263c3bf0d48232cff6a3fd994f1.jpg"
---

### Les ponts de Königsberg

_(Ce paragraphe d'introduction est une traduction de l'article "[Maths in a minute: The bridges of Königsberg](http://plus.maths.org/content/maths-minute-bridges-konigsberg)" paru sur Plus Maths)_

Au 18ème siècle, la ville que nous connaissons sous le nom de Kaliningrad s'appelait Königsberg et se trouvait en Prusse. Comme beaucoup d'autres grandes villes, Königsberg se trouve sur une rivière, la Pregel. Elle comportait deux îles et il y avait sept ponts reliant les différentes terres. Un fameux casse-tête de l'époque était de trouver un chemin à travers la ville qui passait une seule fois par chaque pont. Plusieurs personnes disaient avoir trouver un tel chemin, mais lorsqu'on leur demandait de le reproduire, personne n'y arrivait. En 1735 le mathématicien suisse [Leonhard Euler](https://fr.wikipedia.org/wiki/Leonhard_Euler) expliqua pourquoi : il démontra qu'un tel chemin n'existait pas.

La solution d'Euler est étonnamment simple, une fois que vous considérez le problème sous le bon angle. Le truc est d'éliminer toute information inutile. Le chemin parcouru sur terre n'a pas d'importance. La forme de ces terres n'a pas d’importance, ni le trajet de la rivière ou la forme des ponts. Donc vous pouvez simplement représenter chaque terre par un point et chaque pont par une ligne liant deux points. Vous n'avez pas du tout besoin de respecter la géographie : aussi longtemps que vous ne modifiez pas la connectivité des points, lequel est connecté auxquels, vous pouvez déformer votre dessin autant que vous voulez sans changer le problème.

[![Transformation du problème (source : Wikipédia)](images/ed585263c3bf0d48232cff6a3fd994f1.jpg "Transformation du problème (source : Wikipédia)")](https://fr.wikipedia.org/wiki/Probl%C3%A8me_des_sept_ponts_de_K%C3%B6nigsberg)

Une fois que vous avez représenté le problème de cette façon, ses caractéristiques sont bien plus simples à voir. Après avoir un peu joué avec, vous constaterez ceci : en arrivant sur un point, et à moins que ce soit la dernière étape de votre chemin, vous devrez repartir par une ligne différente de celle d'arrivée puisque c'est la règle du jeu. Ca signifie que chaque point à l'exception du départ et de l'arrivée de votre chemin doit avoir un nombre pair de lignes le connectant aux autres : pour chaque lien entrant il doit y en avoir un pour en repartir.

Donc pour qu'un chemin qui passe une et une seule fois par chaque ligne existe, il ne doit pas y avoir plus de deux points avec un nombre impair de lignes connectées. En fait il ne peut y avoir que deux points impairs ou pas du tout. Dans le premier cas les deux points impairs sont forcément les points de départ et d'arrivée, alors que dans le second, le chemin est un circuit fermé. Or dans le problème de Königsberg, tous les points ont un nombre impair de connexions, donc un chemin ne passant qu'une seule fois par chaque pont est impossible.

Ce résultat d'Euler marque le début de la [théorie des graphes](https://fr.wikipedia.org/wiki/théorie_des_graphes), l'étude de réseaux de points connectés par des liens. Euler a d'ailleurs aussi démontré que si la condition mentionnée plus haut est respectée, à savoir que le nombre de points avec un nombre impairs de liens est soit deux soit zéro, alors il existe toujours un chemin qui passe par chaque lien exactement une fois.

### Voyageur de commerce et postier chinois

_(à partir de là c'est du pur Dr. Goulu)_

A part dans les casse-tête, on trouve très souvent en pratique des problèmes pouvant être résolus grâce à la théorie des graphes. Par exemple, [avant de faire joli](/2010/06/14/optimisation-de-la-joconde/) avec le [problème du voyageur de commerce](https://fr.wikipedia.org/wiki/problème_du_voyageur_de_commerce) (TSP), j'avais eu l'occasion de le rencontrer dans l'optimisation des mouvements d'une machine à percer les circuits électroniques.

Dans le TSP, le but est de trouver le circuit (fermé) dit "[cycle hamiltonien](https://fr.wikipedia.org/wiki/cycle_hamiltonien)" passant par tous les points d'un graphe, et dont le coût soit minimum, en pratique celui dans lequel la distance totale à parcourir (ou mieux encore le temps nécessaire) est minimum. A Königsberg, un voyageur de commerce aurait l'embarras du choix d'un circuit lui permettant de visiter ses clients sur les 4 terres, mais s'il devait s'acquitter de péages différents selon les ponts, un petit calcul lui serait nécessaire. Pour des problèmes de taille réelle, trouver le minimum absolu est horriblement difficile voire impossible, mais il existe des méthodes itératives qui convergent assez rapidement vers des solutions raisonnablement proches de l'optimum.

[![Etapes de l'optimisation TSP du trajets d'une perceuse de circuits imprimés [[1]](#ref-1)](images/d7f65bac716c02c91473d8bc005d8224.jpg "Etapes de l'optimisation TSP du trajets d'une perceuse de circuits imprimés [[1]](#ref-1)")](http://www.sciencedirect.com/science/article/pii/S0924013604006727)Plus récemment j'ai rencontré le [problème du postier chinois](https://fr.wikipedia.org/wiki/problème_du_postier_chinois), ainsi nommé parce qu'il s'agit d'un problème que connaissent tous les postiers, mais qui a été étudié mathématiquement par un chinois, Mei-Ko Kwan en 1962. Il s'agit de trouver le plus court circuit qui permette à un postier de parcourir toutes les rues de sa zone au moins une fois. Il est clair que s'il existe un [cycle eulérien](https://fr.wikipedia.org/wiki/cycle_eulérien) permettant de ne passer qu'une et une seule fois par chaque ligne, ce circuit serait en même temps la solution du postier chinois. Mais quand ce n'est pas le cas, il faut forcément parcourir plusieurs fois certaines rues.

Si le postier doit desservir des échoppes situées sur chacun des ponts de Königsberg, combien de traversées de ponts au total sont nécessaires à sa tournée? Arrive-t-on à réduire ce nombre en employant deux postiers? Et si on construisait un nouveau pont? (Pas deux, ce serait trop facile.)

En gros j'ai ce problème avec environ 200 rues dispersées dans plusieurs villages, plusieurs postiers, et pour couronner le tout il y a du vent : il est plus facile de parcourir les rues dans un sens que dans l'autre. Mais avec Python, [NetworkX](http://networkx.github.io/) et un peu de lecture [[2]](#ref-2), je devrais m'en sortir...

### Références

1. <span id="ref-1"></span>E. Aoyama, T. Hirogaki, T. Katayama, and N. Hashimoto, "Optimizing drilling conditions in printed circuit board by considering hole quality" J. Mater. Process. Technol., vol. 155, pp. 1544–1550, 2004.
2. <span id="ref-2"></span>E. Benavent, A. Corberan, I. Plana, and J. M. Sanchis, "Min-Max k-vehicles windy rural postman problem" Networks, vol. 54, no. 4, pp. 216–226, Dec. 2009 [pdf](http://www.uv.es/sestio/TechRep/tr09-07.pdf)
3. <span id="ref-3"></span>Grötschel, M., & Yuan, Y."Euler, Mei-Ko Kwan, Königsberg, and a Chinese Postman", 2012 [pdf](http://www.math.uiuc.edu/documenta/vol-ismp/16_groetschel-martin-yuan-ya-xiang.pdf)
4. <span id="ref-4"></span>Grötschel, M. (Ed.) "Optimization Stories (Extra Volume)", 2012, 21st International Symposium on Mathematical Programmng (p. 460). Berlin: Documenta Mathematica: Journal der Deutschen Mathematiker-Vereinigung.  ISBN 3936609586 / 978-3936609585 (Excellent recueil d'articles sur l'histoire de la théorie des graphes) [pdf](https://www.zib.de/groetschel/publications/OptimizationStories.pdf)
