---
title: "2017 et les triplets pythagoriciens"
slug: "2017-et-les-triplets-pythagoriciens"
date: 2017-01-02
categories:
  - "Combien"
tags: 
  - "annee"
  - "oeis"
  - "pythagore"
  - "python"
coverImage: "./images/artmaths0202.gif"
---

Au moment d'envoyer un mot à Franck à propos de son livre [[1]](#ref-1), je me suis rappelé qu'il était à l'origine de [ce billet](/2012/04/28/un-peu-de-pedagogie-grace-a-pythagore/) sur la pédagogie appliquée au théorème de Pythagore (et aussi de [celui-ci](/2013/12/15/comment-expliquer-la-relativite-aux-enfants/) sur la Relativité).  J'ai ainsi découvert celle des [453 propriétés de 2017 répertoriées dans l'OEIS](https://oeis.org/search?q=seq%3a2017&fmt=short) sur laquelle baser mes vœux pour cette nouvelle année :

## Bonne et Heureuse Année $\sqrt{792^2+1855^2}$ !

En effet, 2017 est un "nombre hypotenuse" ([A009003](https://oeis.org/A009003)), l'hypoténuse du triangle rectangle correspondant au [triplet pythagoricien](w:) (792,1855,2017). C'est même un triplet pythagoricien "primitif" car ces 3 entiers sont [premiers entre eux](w:), donc 2017 est un "nombre hypoténuse primitif" ([A008846](https://oeis.org/A008846)).

{{< figure src="./images/artmaths0202.gif" alt="(3,4,5), le premier et le plus célèbre des triplets pythagoriciens" caption="(3,4,5), le premier et le plus célèbre des triplets pythagoriciens" width="312" >}}

Car comme on le voit dans [cette liste](https://web.archive.org/web/20161204152220/http://www.tsm-resources.com/alists/trip.html), il existe deux sortes de triplets pythagoriciens: les [primitifs](w:Triplet_pythagoricien#Triplets_primitifs) et les composés, qui sont des multiples de triplets plus petits, par exemple (6,8,10) obtenu en doublant (3,4,5). Ca va avoir de l'importance plus bas.

### Comment générer les triplets pythagoriciens

Il existe plusieurs algorithmes simples pour générer des triplets pythagoriciens. Ils sont tous mauvais. Ceux qui utilisent deux boucles imbriquées voire trois sont lents, ceux qui calculent la racine carrée en nombres flottants sont imprécis, et tous sont limités par une longueur maximale des côtés recherchés.  [Mon propre code](https://gist.github.com/goulu/21c67590c5fa96d1c7b95e3c425c90f1) écrit pour résoudre [un problème facile](https://projecteuler.net/problem=9) du [Project Euler](/2009/02/23/project_euler/) ne faisait pas exception.

J'ai depuis découvert l'existence d'une méthode beaucoup plus efficace, mais pas simple. Quelques millénaires après [Pythagore](w:) et la [corde à 13 nœuds des égyptiens](w:Corde_à_nœuds#Composition_de_la_corde_à_13_nœuds), en 1934 pour être précis, un matheux nommé Berggren a démontré que chaque triplet primitif pouvait être généré à partir de (3,4,5) en le multipliant par une combinaison de ces 3 petites matrices [[2]](#ref-2):

$R_1 =\begin{pmatrix} 1 & -2 & 2 \\\\ 2 & -1 & 2 \\\\ 2 & -2 & 3 \\\\ \end{pmatrix}$ $R_2 =\begin{pmatrix} 1 & 2 & 2 \\\\ 2 & 1 & 2 \\\\ 2 & 2 & 3 \\\\ \end{pmatrix}$ $R_3 =\begin{pmatrix} -1 & 2 & 2 \\\\ -2 & 1 & 2 \\\\ -2 & 2 & 3 \\\\ \end{pmatrix}$

Un autre matheux nommé Barning ayant montré en 1963\*\* que chaque triplet n'est ainsi produit que d'une et une seule manière [[3]](#ref-3), il suffit de parcourir l'[arbre ternaire](w:en:Tree_of_primitive_Pythagorean_triples) formé en multipliant chaque nœud par chacune de ces 3 matrices pour générer l'un après l'autre tous les triplets primitifs:

![](./images/1000px-Pythagorean.tree_.svg_.png)

Ensuite, un autre bout de code peut multiplier chaque triplet primitif par 2,3,4,... pour ajouter les triplets composés et produire ainsi tous les triplets pythagoriciens l'un après l'autre. C'est ce que fait très efficacement ce [code Python de Kyle Guillon trouvé sur StackOverflow](https://web.archive.org/web/20160728111451/http://stackoverflow.com/questions/575117/generating-unique-ordered-pythagorean-triplets/8263898#8263898).

### Oui mais dans l'ordre svp

Une difficulté supplémentaire apparaît si on veut obtenir les triplets triés dans un ordre croissant, par exemple de leur hypoténuse, puis du long côté comme dans [la liste](https://web.archive.org/web/20161204152220/http://www.tsm-resources.com/alists/trip.html) ou dans [A020882](https://oeis.org/A020882) et d'autres séries de l'OEIS. Evidemment, si on ne s'intéresse qu'aux N premiers triplets, on peut toujours les générer, et les trier ensuite. Mais si on veut chercher par exemple le plus petit triplet dont la longueur de hypoténuse est un carré ainsi que la somme des côtés\*, on ne  connait a priori pas N...

Pour générer les triplets dans un ordre croissant, j'ai incorporé le tri aux fonctions précédentes à l'aide de [listes triées](w:), mais je ne vais pas accentuer votre mal de cheveux annuel en vous détaillant ça ici. Pour ceux que ça intéresse, [le résultat se trouve dans le module math2](https://web.archive.org/web/20160529185958/http://goulib.readthedocs.io/en/latest/modules/Goulib.math2.html#Goulib.math2.primitive_triples) de ma librairie Goulib dont je vous reparlerai très bientôt, et [aussi sur StackOverflow](https://web.archive.org/web/20170102/http://stackoverflow.com/a/41146390/1395973) où vous pouvez voter pour moi...

Mais bon, juste parce que j'en suis assez content, en testant mon code j'ai découvert une erreur dans [A121727](https://oeis.org/A121727) : le 20ème terme de la série est 145, pas 142. Et j'ai ainsi pu constater que l'OEIS est un bon site scientifique car il est doté d'un système rigoureux mais efficace de correction des erreurs.

Pour terminer, à tous ceux qui se demandent à quoi peut bien servir tout ça, je recommande la lecture de [[4]](#ref-4) auquel je n'ai pas tout compris (séquelles du champagne je suppose), mais qui propose une nouvelle méthode de cryptographie basée sur les triplets pythagoriciens.

Comme quoi les années passent, mais les bonnes idées restent et construisent inéluctablement un monde plus intéressant à découvrir.

Mes chers lecteurs, je vous souhaite à tous l'indispensable Santé, le très important Bonheur, et l'Etonnement qu'apportent la curiosité, la découverte et la compréhension de ce monde étrange.

### Notes:

\* C'est (4565486027761, 1061652293520, 4687298610289=21650172), découvert en 1643 par [Fermat](w:). [Un autre de ses calculs](/2012/04/15/comment-produire-des-nombres-premiers/) (edit du 9.1.2016 :) dont je n'ai aucune idée de comment il a fait à l'époque spectaculaires, d'autant que la recherche avec le générateur proposé dans cet article prend des plombes... [L'approche mathématique](https://www.ilemaths.net/sujet-une-sacree-hypotenuse-623061.html) vaut décidément bien mieux, et en plus indique [comment Fermat a fait](http://gallica.bnf.fr/ark:/12148/bpt6k62145354/f382.image) .

\*\* Excellente année aussi...

### Références:

1. <span id="ref-1"></span>{{< openbook booknumber="OLID:OL26208349M" templatenumber="5" >}}
2. <span id="ref-2"></span>Berggren, "Pytagoreiska trianglar", 1934, Tidskrift för elementär matematik, fysik och kemi, vol. 17, p. 129-139.
3. <span id="ref-3"></span>Barning, F. J. M. "Over pythagorese en bijna-pythagorese driehoeken en een generatieproces met behulp van unimodulaire matrices", 1963 Math. Centrum Amsterdam Afd. Zuivere Wisk. ZW-011: 37, ([pdf](https://web.archive.org/web/20160928225445/http://oai.cwi.nl/oai/asset/7151/7151A.pdf))
4. <span id="ref-4"></span>Spezeski, W. J. "[Rethinking Pythagorean Triples](https://www.pvamu.edu/mathematics/wp-content/uploads/sites/49/Spezeski-AAM-R50-WS-080207-Final-_9_-6-13-08.pdf)", 2008, Applications and Applied Mathematics: An International Journal, 3(1), 100–112. Retrieved from http://pvamu.edu/aam
