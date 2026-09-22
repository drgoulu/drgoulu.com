---
title: Pourquoi la somme des nombres à l'infini est-elle égale à -1/12?
slug: pourquoi-la-somme-des-nombres-a-l-infini-est-elle-egale-a-1-12
date: '2021-11-11'
draft: false
categories:
- Pourquoi
tags:
- philosophie
- mathematiques
- theorie
- nombres
- infini
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Pourquoi-la-somme-des-nombres-%C3%A0-linfini-est-elle-%C3%A9gale-%C3%A0-1-12/answer/Dr-Goulu)*

Ce n'est pas la somme "normale" des entiers qui donne -1/12 mais leur [Sommation de Ramanujan](w:), que Ramanujan avait noté $(\Re)$ dans ses carnets, sans expliquer ce que c'était tant c'étai évident pour lui :

$$\sum_{k=1}^xf(k) = C + \int_0^x f(t)\,{\rm d}t + \frac12f(x) + \sum_{k=1}^{\infty}\frac{B_{2k}}{(2k)!}f^{(2k - 1)}(x)$$

si vous regardez l'équation pour la fonction identité f(x)=x, vous voyez qu'elle lie la somme des entiers à l'intégrale des entiers.

Comme le montre [David Louapre](https://fr.quora.com/profile/David-Louapre) à la fin de son super article, cette relation (que l'on retrouve en physique ! ) a une signification profonde :

> la somme 1 + 2 + 3 + 4 + … est bien infinie, mais -1/12 est ce qui la sépare de ∫xdx qui est aussi infini, est que l’on peut voir comme une base que l’on soustrait. Dans le cas de Casimir, il s’agit bien d’ailleurs du niveau énergétique « de base », quand les plaques sont très éloignées.
> Autre manière de le dire, on trouve que 1 + 2 + 3 + 4 + … est infini, mais égal à -1/12, modulo ∫xdx.

[https://scienceetonnante.com/201...](https://scienceetonnante.com/2013/05/27/1234567-112/)
