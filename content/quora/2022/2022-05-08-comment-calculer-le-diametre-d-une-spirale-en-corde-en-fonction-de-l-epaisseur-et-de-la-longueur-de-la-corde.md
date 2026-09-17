---
title: Comment calculer le diamètre d'une spirale en corde en fonction de l'épaisseur et de la longueur de la corde ?
slug: comment-calculer-le-diametre-d-une-spirale-en-corde-en-fonction-de-l-epaisseur-et-de-la-longueur-de-la-corde
date: '2022-05-08'
draft: false
categories:
- Comment
tags:
- mathematiques
- corde
- spirale
- longueur
- calcul
- millimetre
- geometrie
- formule-de-calcul
- centimetres
- diametre
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Comment-calculer-le-diam%C3%A8tre-dune-spirale-en-corde-en-fonction-de-l%C3%A9paisseur-et-de-la-longueur-de-la-corde/answer/Dr-Goulu)*

D'après [length of spiral - Wolfram|Alpha](https://www.wolframalpha.com/input?i=length+of+spiral) la longueur d'une[spirale d'Archimède](w:) de pas a est $s(t) = 1/2 a (\sqrt{t^2 + 1} t + sinh^{-1}t)$

ou t est l'angle en radians, donc si vous connaissez cette longueur L, vous pouvez obtenir l'angle en résolvant $s(t)=L$ mais c'est pas assez simple pour la version gratuite de WolframAlpha…

Une autre approche est de considérer que le n-ième tour de la spirale a une longueur $L_n=2\pi.a(n+n-1)/2$

qui est la moyenne des périmètres des cercles de rayon $n*a$ et $(n-1)*a$

donc la longueur totale est$L=\sum_{n=1}^{N} L_n + reste$

et calculer ainsi le nombre de tours entiers N par soustractions successives

Le rayon de votre spirale vaut alors N*a + un petit quelque chose en fonction du reste …

(pas mieux pour l'instant…)
