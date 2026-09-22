---
title: Existe-t-il une suite qui correspond aux nombres premiers ?
slug: existe-t-il-une-suite-qui-correspond-aux-nombres-premiers
date: '2019-05-14'
draft: false
categories:
- Quora
tags:
- sciences
- mathematiques
- theorie
- nombres
- nombres-premiers
coverImage: ./images/quora.png
---

*Article initialement publié sur [Quora](https://fr.quora.com/Existe-t-il-une-suite-qui-correspond-aux-nombres-premiers/answer/Dr-Goulu)*

oui, elle s’appelle [A000040](https://oeis.org/A000040) :-)

Et contrairement à ce que beaucoup de gens pensent, il existe une formule qui dit si un nombre est premier ou pas:

$f(n) = \left\lfloor \frac{n! \bmod (n+1)}{n} \right\rfloor (n-1) + 2$

Par le [Théorème de Wilson](w:), $n+1$ est premier si et seulement si $n!{\bmod {(}}n+1)=n$. Donc quand $n+1$ est premier, le premier facteur du produit vaut 1, et la formule produit le nombre premier $n+1$. Mais quand $n+1$ n’est pas premier, ce facteur devient 0 et la formule produit le nombre premier 2.

Cette formule n’est pas efficace du tout pour calculer les nombres premiers, mais elle existe …
