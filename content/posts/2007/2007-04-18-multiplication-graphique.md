---
title: "Multiplication graphique"
slug: "multiplication-graphique"
date: 2007-04-18
tags: 
  - "casse-tetes"
  - "humour"
  - "maths"
coverImage: "./images/image016.gif"
---

J'avais déjà vu cette vidéo qui montre une drôle de manière de multiplier deux nombres, mais Yves m'a demandé si "c'est un gag, ou il y a une once de vérité dans la méthode ?", alors je l'ai regardée encore une fois :

{{< youtube id="HK_Y0VhjWlY" width="640" >}}

En fait c'est tout bêtement une multiplication en colonne déguisée :

Dans le premier exemple 21 x 13, les intersections de gauche représentent le produit des dizaines (2x1), celles de droite le produit des unités (1x3) et celles du milieu les 2 produits dizaines x unités (1x3 + 1x1 ). On retrouve directement le principe de la multiplication à la main, d'autant qu'il n'y a pas de retenues:

```
   2  1
x  1  3
--------
2  1
+  6  3
--------
2  7  3
```

De même dans le second exemple 123 x 321 :

```
      1  2  3
   x  3  2  1
   ----------
3  6  9
+  2  4  6
+     1  2  3
-------------
3  8 14  8  3
```

qui sont les nombres d'intersections de chaque colonne du graphique. Reste à gérer les retenues, facile dans ce cas où il n'y a qu'un 1 à reporter à un endroit.

Au début j'ai pensé que la méthode est limitée aux petits chiffres comme 1,2,3 dont les produits sont inférieur à 10, mais il n'y a aucune raison : on peut très bien multiplier 978 par 689 ainsi. La connaissance du livret évite même de compter les points un à un... Il faut juste être prudent avec les 0, en les traçant quand même pour éviter les bulles, par exemple comme un trait pointillé dont toutes les intersections sont omises ...
