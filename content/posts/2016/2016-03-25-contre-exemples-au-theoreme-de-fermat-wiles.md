---
title: "\"Contre-exemples\" au théorème de Fermat-Wiles"
slug: "contre-exemples-au-theoreme-de-fermat-wiles"
date: 2016-03-25
categories: 
  - "cat2"
tags: 
  - "fermat"
  - "informatique"
  - "maths"
  - "programmation"
  - "python"
  - "simpson"
coverImage: "18-Homer-Simpson.jpg"
---

{{< figure src="images/simpson_fermat.gif" alt="simpson_fermat" >}}

[Andrew Wiles](https://fr.wikipedia.org/wiki/Andrew_Wiles) vient de remporter le [Prix Abel](https://fr.wikipedia.org/wiki/Prix_Abel) pour sa démonstration du [Grand théorème de Fermat](https://fr.wikipedia.org/wiki/Grand_théorème_de_Fermat) qui dit qu’il n’existe pas de solution de l’équation an+bn\=cn pour a,b,c,n entiers et n>2. Pourtant _<mauvaise foi=on>_ :

1. il a en réalité "seulement" démontré un cas particulier du [théorème de modularité](https://fr.wikipedia.org/wiki/théorème_de_modularité) (aussi appelé conjecture de Shimura-Taniyama-Weil) dont le théorème de Fermat résulte directement
2. quelques semaines après la publication des quelques 100 pages de la démonstration d'Andrew Wiles en 1995 [[1]](#ref-1), Homer Simpson se promène nonchalamment et en 3D devant un contre-exemple : 1782¹² + 1841¹² = 1922¹² [[2]](#ref-2)

Cette égalité est due à [David X. Cohen](https://fr.wikipedia.org/wiki/David_X._Cohen), matheux et co-scénariste de cette [série pleine de références scientifiques](/2010/03/07/20-ans-de-science-simpson/). Si on la vérifie sur une calculatrice standard, on trouve que le terme de gauche vaut 2.541210259e+39 et que celui de droite vaut... 2.541210259e+39 ! C'est un contre-exemple du Grand théorème de Fermat, et la démonstration d'Andrew Wiles ne vaut pas tripette! _<mauvaise foi=off>_ 

Mais en fait non:

- Avec plus de décimales ou Python, on voit que le terme de gauche vaut 2541210258614589176288669958142428526657 et celui de droite 2541210259314801410819278649643651567616. Ca fait une gigantesque différence de 700212234530608691501223040959, mais comme elle représente moins d'un milliardième des nombres précédents (2.75 10\-10 pour être précis), une bête calculatrice du siècle passé qui ne calculait qu'avec 9 chiffres significatifs ou en nombres flottants sur 32 bits pouvait considérer ce chiffre comme comparativement négligeable.
- {{< figure src="images/18-Homer-Simpson.jpg" alt="quatre grands problèmes scientifiques résolus sur un seul tableau !" caption="quatre grands problèmes scientifiques résolus sur un seul tableau !" width="420" >}}
    
    En y regardant de plus près, on voit tout de suite que l'égalité est fausse car comme 1782 est pair, 1782¹² l'est aussi et comme 1841¹² est impair pour les mêmes raisons, la somme 782¹² + 1841¹² est impaire. Or 1922¹²  est pair...

Informé de cette dernière objection, David X. Cohen a fait apparaître dans un autre épisode [[3]](#ref-3) le tableau noir suivant, sur lequel se trouve un autre faux contre-exemple : 3987¹² + 4365¹² = 4472¹². Belle conscience professionnelle, n'est-ce pas ?\*

Cette fois l'égalité proposée respecte la parité, et est "moins fausse" que la précédente puisque la différence ne représente que 1.89 10\-11 des termes.

Je me suis alors posé trois questions:

1.  y'a-t-il beaucoup de tels contre-exemples ?
2. y'a-t-il une raison particulière au fait  que les deux exemples de David X. Cohen utilisent la puissance 12 ?
3. peut-on en trouver qui sont encore moins faux que 1.89 10\-11 ?

J'ai donc écrit un [petit programme Python](https://gist.github.com/goulu/e92cd35c23c921e55c16)\*\* qui génère les triplets (a,b,c) tels que an+bn\=cn est juste à 10\-9 près, en balayant les nombres a et b entre 100 et 100'000 et incrémentant n à partir de 3. Ce programme s'est révélé productif au point de pouvoir répondre facilement à la question No 1 : oui, il y a des centaines de faux contre-exemples de la qualité de ceux des Simpson pour chaque p et 100 < a,b < 100'000.

Le plus petit faux contre-exemple trouvé donnant une différence inférieure à 10\-9 est **1295³ + 216³ = 1297³** . La différence entre les deux termes 2181825071 et 2181825073 n'est que de 2 !

Celui ayant la précision relative la plus élevée est  **487674 \+ 245764 \= 495354**  L'erreur relative n'est que de 5.1 10\-16 soit juste deux fois plus que la précision des nombres flottants sur 64 bits de la plupart des calculatrices actuelles.

A la puissance 5, le record de précision est 843855  + 834525 = 964035 (à 5.67 10\-15 près), ensuite la précision des contre-exemples les moins faux diminue lentement quand la puissance augmente. A la puissance 12 il y a 1931112 + 1882112 = 2021812 (1.95 10\-12) qui est meilleur que celui de David X. Cohen, qui s'est probablement limité aux nombres de 4 chiffres. Mais je n'ai rien remarqué de particulier pour n=12

Voilà Andrew, comme 99.99% de la population je n'ai rien compris à ta prodigieuse démonstration [[1]](#ref-1) qui a nécessité 20 ans de vérifications avant que tu reçoive enfin ce prix bien mérité. Je me joins à David et Homer pour te dire juste Bravo !

### Notes:

\* la dernière ligne du tableau concerne évidemment la topologie (et non, un donut n'est pas isomorphe à une sphère), mais quelqu'un sait-il à quoi correspondent les lignes 1 et 3 ? Je doute que Cohen ait sorti ces équations de nulle part...

\*\* pourquoi Python ? entre autres parce qu'il gère l'[arithmétique multiprécision](https://fr.wikipedia.org/wiki/arithmétique_multiprécision) de façon transparente : rien de spécial à faire pour manipuler des nombres énormes.

### Références

1. <span id="ref-1"></span>{{< altmetric doi="10.2307/2118559" float="right" >}} Andrew Wiles. "Modular elliptic curves and Fermat's Last Theorem", 1995, Annals of Mathematics 142 (3): 443–551. [doi:10.2307/2118559](http://www.jstor.org/stable/2118559). ([PDF text version](http://users.tpg.com.au/nanahcub/flt.pdf))
2. <span id="ref-2"></span>séquence "Homer³" dans "[Les Simpson Spécial Halloween VI](https://fr.wikipedia.org/wiki/Simpson_Horror_Show_VI)", épisode 6 saison 7, 1995
3. <span id="ref-3"></span>[La Dernière Invention d'Homer](https://fr.wikipedia.org/wiki/La_Dernière_Invention_d'Homer), Les Simpson épisode 2 saison 10, 1998
4. <span id="ref-4"></span>video "[Homer Simpson vs Pierre de Fermat](https://www.youtube.com/watch?v=ReOQ300AcSU)" de Numberphile sur ce sujet (en anglais)
