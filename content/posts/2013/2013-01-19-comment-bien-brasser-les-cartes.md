---
title: "Comment bien brasser les cartes"
slug: "comment-bien-brasser-les-cartes"
date: 2013-01-19
categories: 
  - "cat2"
tags: 
  - "algorithmes"
  - "informatique"
  - "tri"
  - "visualisation"
coverImage: "fdd88ca55a8f211b9fc8f978d988744c.jpg"
---

Les amateurs de jeux de cartes savent qu'il faut accorder beaucoup d'attention au brassage des cartes pour éviter la triche, mais qu'en est-il par exemple dans les jeux de poker en ligne ?

Les informaticiens se sont beaucoup [cassé la tête sur le tri des données](/tags/tri/), mais relativement peu sur les problèmes de brassage, moins fréquents et apparemment plus simples. Mais comme disait [M. Poisson](https://fr.wikipedia.org/wiki/Siméon_Denis_Poisson) : "il faut se méfier des appâts rances" ©...

Examinons pour commencer un algorithme tout bête que j'avoue avoir utilisé plusieurs fois  : on échange la première carte (ou donnée) avec une autre choisie au hasard parmi les N cartes\*, puis on fait de même pour la 2ème carte, la 3ème et ainsi de suite jusqu'à la N-ième. Cette méthode semble réunir toutes les caractéristiques d'un bon algorithme : simplicité, rapidité, et efficacité.

_(Si vous avez un vrai browser, [voyez cette animation de l'algo](http://jsfiddle.net/vhrQA/10). C'est ma première oeuvre faite avec [D3.js](http://d3js.org/), fortement inspirée de [[1]](#ref-1), et que j'essaie désespérément d'inclure directement dans cet article...)_

Et pourtant, un tel brassage s'avère "biaisé" : toutes les [permutations](https://fr.wikipedia.org/wiki/permutations) possibles n'ont pas la même probabilité d'être produites. Déjà en ne brassant que N=3 cartes par cette méthode, 3 des 6 permutations possibles sont nettement moins probables que les 3 autres  [[3]](#ref-3).

{{< figure src="images/fdd88ca55a8f211b9fc8f978d988744c.jpg" alt="biais naïve swap (i ↦ random)" caption="biais naïve swap (i ↦ random)" link="http://bost.ocks.org/mike/shuffle/compare.html" width="240" >}}

Avec N=60 cartes, ce biais est bien visible sur la figure ci-contre, produite par une autre [application D3.js](http://bost.ocks.org/mike/shuffle/compare.html)  en ligne [[2]](#ref-2). Elle effectue 10'000 mélanges avec le même algo, compte dans une matrice le nombre de fois ou la i-ième carte se retrouve à la j-ième position après le brassage, et représente les [biais](http://fr.wikipedia.org/wiki/Biais_\(statistique\)) positifs en vert et les négatifs en rouge.

La variante "swap (random ↦ random)" dans laquelle on échange N fois 2 cartes choisies au hasard n'est pas meilleure : elle présente un biais positif sur la diagonale (i=j) qui s'atténue si on effectue 2N échanges, et disparaît presque pour 3N échanges.

Signifierait-ce qu'il faut plus de N opérations pour obtenir un "bon" brassage de N cartes ? On pourrait le penser car il existe un algorithme tout simple sans biais : extraire successivement des cartes prises au hasard dans le tas pour en constituer un deuxième, mais il nécessite N.log(N) opérations\*\*\*, voire N² s'il est mal programmé [[1]](#ref-1). Or N.log(N) est la complexité des algorithmes de tri, donc on pourrait avoir l'idée aussi surprenante que séduisante de se faire un brassage en utilisant [quicksort](https://fr.wikipedia.org/wiki/tri_rapide) auquel on passe une fonction aléatoire comme critère de tri.

C'est tellement beau que j'exhibe même ici le petit bout de code Javascript qui fait ça:

\[source language="javascript"\] function shuffle(array) { array.sort(function() {return Math.random() - .5}); }\[/source\]

{{< figure src="images/4515a7fe42f5229307c0f50570d991ca.jpg" alt="biais sort (random comparator)" caption="biais sort (random comparator)" link="http://bost.ocks.org/mike/shuffle/compare.html" width="240" >}}

random() renvoie un nombre aléatoire entre 0 et 1, donc Math.random() - .5 tire à pile ou face si une carte est "plus grande" que l'autre lors du tri, ce qui est supposé mélanger au lieu de trier.

Cette méthode produit la matrice de biais ci-contre, dont la non-trivialité me laisse pantois.

Par contre, la variante dans laquelle on commence par générer un vecteur de nombres aléatoires, puis on "dé-trie" les données en utilisant ces nombres aléatoires pour les comparaisons donne un résultat non biaisé. (voir "sort (random order)" dans [[2]](#ref-2))

Et une fois qu'on est tout content d'avoir trouvé un algorithme de brassage non biaisé de complexité N.log(N), on découvre celui de [Fisher-Yates](https://fr.wikipedia.org/wiki/Permutation_aléatoire#Algorithme_de_Fisher-Yates) datant de 1938, non biaisé, assez simple : \[source language="javascript"\] function shuffle(array) { var j = array.length, t, i; while (j) { i = Math.floor(Math.random() \* j--); t = array\[j\]; array\[j\] = array\[i\]; array\[i\] = t; } }\[/source\] Les 3 dernières lignes échangent les cartes en i-ième et en j-ième position tout comme dans notre premier algorithme naïf, mais ici on ne choisit la carte à échanger que parmi celles qui n'ont pas encore été traitées. Et pour des raisons de simplicité du code, on mélange le tableau "depuis la fin".

Et le plus beau est que sa [complexité algorithmique](https://fr.wikipedia.org/wiki/complexité_algorithmique) est proportionnelle à N, ce qui est in exemple de plus de l’universalité du principe de Murphy de la thermodynamique de la tartine beurrée qui dit qu'il est toujours plus facile de générer du désordre que de l'ordre.

D'autre part, si vous devez brasser beaucoup de données de manière irréversible, je ne sais pas moi, pour une application de vote par internet par exemple, souvenez-vous de Fisher-Yates. Et utilisez un [vrai générateur de nombres aléatoires](http://www.idquantique.com/component/content/article/9.html) , car un [générateur de nombres pseudo-aléatoires](https://fr.wikipedia.org/wiki/générateur_de_nombres_pseudo-aléatoires) peut non seulement souffrir de biais, mais surtout être reproductible à partir de la "graine" et permettre ainsi d'inverser le brassage.

Bon, je voulais encore modéliser différentes techniques de brassage de vraies cartes en JavaScript pour déterminer combien d'opérations sont nécessaires pour obtenir un mélange sans biais, mais je préfère laisser ça en exercice pour ChipRaptor et d'autres.

{{< youtube id="UYmcmIgL1yA" width="640" >}}

### Notes:

Gag © Pierre-Alain de [WPanorama](http://www.wpanorama.com/)

\* et non N-1, car il faut garder une chance sur N que la carte soit "échangée avec elle même" et reste à sa place dans le tas.

\*\* félicitations au premier lecteur qui calculera les probabilités respectives de ces permutations et expliquera ainsi le biais...

\*\*\* parce qu'on doit alors forcément parcourir des [listes ou tableaux](https://fr.wikipedia.org/wiki/liste_(informatique))

### Références:

1. <span id="ref-1"></span>[Mike Bostock](http://bost.ocks.org/mike/),  "[Fisher–Yates Shuffle](http://bost.ocks.org/mike/shuffle/)", 14 janvier 2012
2. <span id="ref-2"></span>Mike Bostock,  "[Will it shuffle ?](http://bost.ocks.org/mike/shuffle/compare.html)", 21 janvier 2012
3. <span id="ref-3"></span>Jeff Atwood "[The danger of naïveté](http://www.codinghorror.com/blog/2007/12/the-danger-of-naivete.html)", 2007, Coding Horror
