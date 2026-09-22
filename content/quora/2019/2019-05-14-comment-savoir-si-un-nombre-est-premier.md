---
title: Comment savoir si un nombre est premier ?
slug: comment-savoir-si-un-nombre-est-premier
date: '2019-05-14'
draft: false
categories:
- Comment
tags:
- mathematiques
- theorie
- nombres
- nombres-premiers
- nombres-naturels
coverImage: ./images/quora.png
---

*Article initialement publié sur [Quora](https://fr.quora.com/Comment-savoir-si-un-nombre-est-premier/answer/Dr-Goulu)*

Avec un [Test de primalité](w:). Il en existe deux types:

- les “déterministes”, qui donnent un résultat sur et certain, mais demandent beaucoup de temps pour de grands nombres N. Le plus simple est d’essayer de diviser N par tous les nombres premiers jusqu’à $\sqrt{N}$
- les “probabilistes” qui sont beaucoup, beaucoup plus rapides. Le plus simple est le [test de primalité de Fermat](w:). Plus moderne, le [test de primalité de Miller-Rabin](w:) est couramment utilisé en cryptographie pour déterminer en une fraction de seconde si un nombre de centaines de chiffres est premier.
Puisqu’ils sont “probabilistes” ces tests ont une toute petite probabilité de déclarer premier un nombre qui ne l’est pas. En pratique cette probabilité est plus basse que celle qu’un rayon cosmique fausse le résultat d’un test déterministe pendant son très long calcul, donc le test probabiliste est plus sur que le test déterministe !

Il y a aussi des tests spécialisés pour certains types de nombres, comme le [Test de primalité de Lucas-Lehmer pour les nombres de Mersenne](w:) qui est déterministe, mais ne marche que pour les nombres de Mersenne (raison pour laquelle le [Plus grand nombre premier connu](w:) est toujours un nombre de Mersenne).

[Comment trouver des nombres premiers - Pourquoi Comment Combien](/2012/04/15/comment-produire-des-nombres-premiers/)
