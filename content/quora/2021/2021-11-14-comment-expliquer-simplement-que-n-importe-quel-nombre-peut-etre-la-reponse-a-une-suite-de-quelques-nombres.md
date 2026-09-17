---
title: Comment expliquer simplement que n'importe quel nombre peut être la réponse à une suite de quelques nombres ?
slug: comment-expliquer-simplement-que-n-importe-quel-nombre-peut-etre-la-reponse-a-une-suite-de-quelques-nombres
date: '2021-11-14'
draft: false
categories:
- Comment
tags:
- mathematiques
- raisonnement-logique
- theorie-des-nombres
- suites-mathematiques
- logique-mathematiques
- equations-mathematiques
- questions-mathematiques
- education-mathematique
- mathematiques-simples
- solutions-mathematiques
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Comment-expliquer-simplement-que-nimporte-quel-nombre-peut-%C3%AAtre-la-r%C3%A9ponse-%C3%A0-une-suite-de-quelques-nombres/answer/Dr-Goulu)*

$1, 2, 3, 5, 8, 13$

Vous croyez que c'est la suite de Fibonacci ?

Peut-être, mais ce sont aussi les solutions de l équation

$x^6 - 32 x^5 + 376 x^4 - 2066 x^3 + 5575 x^2 - 6974 x + 3120 = 0$

que l'on peut factoriser ainsi :

$(x-1)(x-2)(x-3)(x-5)(x-8)(x-13)=0$

(oui vous avez deviné, j'ai fait l'inverse…)

Alors pour n'importe quel nombre "suivant" $a$ je peux vous fabriquer l'équation

$$x^7-(32+a)x^6 + (376+32 a) x^5 - (2066+376 a) x^4 + (5575+2066 a) x^3 - (6974+5575 a) x^2 + (3120+6974 a) x - 3120 a  =0$$

dont les solutions sont $1, 2, 3, 5, 8, 13, a$

Et je peux recommencer à l'infini sans jamais faire référence à Fibonacci.
