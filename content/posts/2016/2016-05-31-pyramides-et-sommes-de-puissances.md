---
title: "Pyramides et sommes de puissances"
slug: "pyramides-et-sommes-de-puissances"
date: 2016-05-31
categories: 
  - "cat1"
tags: 
  - "maths"
  - "nombres"
coverImage: "Pyramid_of_35_spheres_animation_original.gif"
---

![pyramid-spheres](images/pyramid-spheres.png)En essayant de comprendre quelque chose aux [courbes elliptiques](https://fr.wikipedia.org/wiki/courbe_elliptique) je suis tombé [là](https://jeremykun.com/2014/02/10/elliptic-curves-as-elementary-equations/) sur un problème d'apparence tout simple qui m'a fait découvrir les [nombre pyramidaux](https://fr.wikipedia.org/wiki/nombre_pyramidal) et l'intéressant problème du calcul des [sommes de puissances d'entiers](https://fr.wikipedia.org/wiki/sommes_de_puissances_d'entiers).

Le problème tout simple concerne une pyramide de boulets comme celle ci-contre. Combien de boulets contient une pyramide de n étages ? Il est égal à $1+4+9+16+...+n^2 = \sum_{k=1}^{n}k^2$ , la somme des carrés des n premiers nombres entiers que nous allons noter $S_n^2$.

Sur internet on trouve facilement que $S_n^2= n(n+1)(2n+1) / 6$ mais ce n'est [pas évident](https://fr.wikipedia.org/wiki/Somme_\(arithmétique\)#Somme_des_premières_puissances) de retrouver cette formule sur une île déserte déconnectée.

### Somme de puissances

D'autre part, en regardant $S_n^2$ de plus près, on voit un truc marrant:

- La somme des n premiers nombres entiers (à la puissance 1)\* $S_n^1 = \sum_{k=1}^{n} k = n(n+1) / 2$ est un facteur de $S_n^2$.
- et la somme des n premiers nombres entiers à la puissance zéro $S_n^0 = \sum_{k=1}^{n} k^0 = n$ est un facteur de $S_n^1$.

Alors est-ce que la somme des carrés $S_n^2$ se retrouverait dans la somme des cubes $S_n^3 = \sum_{k=1}^{n} k^3$ ?

Surprise : non. En fait $S_n^3 = (n(n+1)/2)^2 = (S_n^1)^2$ : la somme des cubes est égale à la somme des nombres élevée au carré. On appelle parfois ceci "théorème de [Nicomaque](https://fr.wikipedia.org/wiki/Nicomaque_de_Gérase)"

Par contre dans $S_n^4$ on retrouve $S_n^2$ : $S_n^4 = (3n^2+3n-1).S_n^2$. Etrange non ?

Celui qui a mis un peu d'ordre dans cette étrangeté s'appelle [Johann Faulhaber](https://fr.wikipedia.org/wiki/Johann_Faulhaber). Au début du XVIIème siècle, ce professeur de [René Descartes](https://fr.wikipedia.org/wiki/René_Descartes) a établi une méthode générale et calculé à la main les formules pour les sommes des puissances d'entiers jusqu'à la puissance 17, puis il est mort. Un siècle plus tard, [Jacques Bernoulli](https://fr.wikipedia.org/wiki/Jacques_Bernoulli) a ramené la méthode générale de Faulhaber à une seule équation connue aujourd'hui sous le nom  de [Formule de Faulhaber](https://fr.wikipedia.org/wiki/Formule_de_Faulhaber):

$S_n^p = \sum_{k=1}{n}k^p = {1 \over p+1} \sum_{j=0}^p {p+1 \choose j} B_j n^{p+1-j}$ où:

- ${p+1 \choose j}$ est un [coefficient binomial](https://fr.wikipedia.org/wiki/coefficient_binomial), bien connu
- $B_j$ est le j-ème [Nombre de Bernoulli](https://fr.wikipedia.org/wiki/Nombre_de_Bernoulli), moins connus mais que l'on retrouve dans des choses comme la [Formule d'Euler-Maclaurin](https://fr.wikipedia.org/wiki/Formule_d'Euler-Maclaurin) ou la [Fonction zêta de Riemann](https://fr.wikipedia.org/wiki/Fonction_zêta_de_Riemann), un point chaud des maths.

Je n'en suis pas encore là. Pour l'instant je me suis limité à immortaliser la formule de Faulhaber et les Nombres de Bernoulli en quelques lignes de Python qui pourraient être utile un jour, pour un [problème Euler](https://projecteuler.net/problem=545)\*\* ou l'autre

\[gist id="5bbf24a3e2e25070904b79f49020448f" file="faulhaber.py"\]

### Du haut de ces pyramides...

Revenons à notre problème initial de pyramide à base carrée. Carrée ? Pourquoi se limiter à un carré ? D'ailleurs les faces de notre pyramide sont triangulaires... et même qu'elles ont 1+2+3+ ... n boulets, et revoici notre $S_n^1$ ! Pas pour rien qu'on appelle les nombres 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ... (suite [A000217](https://oeis.org/A000217 "oeis:A000217") de l'OEIS) "[Nombres triangulaires](https://fr.wikipedia.org/wiki/Nombre_triangulaire)", ce qui est d'autant plus logique que 1, 4, 9, 16, 25, 36, ... ([A000290](https://oeis.org/A000290 "oeis:A000290")) sont les "[carrés](https://fr.wikipedia.org/wiki/Carré_parfait)".

{{< figure src="images/Pyramid_of_35_spheres_animation_original.gif" alt="Image Wikimedia Commons : Rendered by Blotwell using POV-Ray" caption="Image Wikimedia Commons : Rendered by Blotwell using POV-Ray" link="https://commons.wikimedia.org/wiki/File:Pyramid_of_35_spheres_animation_original.gif" align="alignright" width="400" >}}

En empilant des boulets sur une base triangulaire, on obtient les [nombres tétraédriques](https://fr.wikipedia.org/wiki/nombre_tétraédrique) 1, 4, 10, 20, 35, 56, 84, 120, 165, 220, ...  ( [A000292](https://oeis.org/A000292 "oeis:A000292") ) donnés par la formule

$P_n^3=\frac{n(n+1)(n+2)}6={n+2 \choose 3}$

En 1850, un dénommé Sir Frederick [Pollock conjectura](https://fr.wikipedia.org/wiki/Conjectures_de_Pollock) que tout nombre entier peut être écrit comme la somme de 5 nombres tétraédriques au maximum. De fait, on ne connait aujourd'hui que 241 petits nombres qui nécessitent 5 termes ([A000797](https://oeis.org/A000797)), mais personne n'a jusqu'ici démontré qu'il en n'en existe pas d'autre. Ou que si. C'est pourquoi la Conjecture de Pollock est toujours une [conjecture](https://fr.wikipedia.org/wiki/conjecture)...

On peut évidemment considérer des bases définies par d'autres [nombres polygonaux](https://fr.wikipedia.org/wiki/nombre_polygonal), sur lesquels construire des [nombres pyramidaux](https://fr.wikipedia.org/wiki/Nombre_pyramidal) donnés par cette formule toute simple, mise ici au cas où elle se révélerait utile  à quelque chose un jour :

$P_n^r=\frac{n(n+1)}2\frac{(r-2)n-(r-5)}3$

### Notes

- et $S_n^1 = n(n+1) / 2$ est facile à retrouver si on l'écrit $S_n^1=(1+n)+(2+n-1)+(3+n-2)+...$
- \*\* auquel je n'ai pas compris grand chose non plus...

### Références

1. <span id="ref-1"></span>Charles-É. Jean "[nombres figurés](http://www.recreomath.qc.ca/dict_figure_nombre.htm)" Dictionnaire de mathématiques récréatives "[Récréomath](http://www.recreomath.qc.ca)"
