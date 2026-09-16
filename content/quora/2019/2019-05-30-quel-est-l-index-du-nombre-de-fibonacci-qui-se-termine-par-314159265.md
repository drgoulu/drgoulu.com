---
title: Quel est l'index du nombre de Fibonacci qui se termine par 314159265?
slug: quel-est-l-index-du-nombre-de-fibonacci-qui-se-termine-par-314159265
date: '2019-05-30'
draft: false
categories:
- Quora
tags:
- mathematiques
- nombres
- suite-d-entiers
- sequence-de-fibonacci
- theorie-des-nombres
- suites-mathematiques
- nombres-naturels
- calcul-mathematique
- nombres-de-fibonacci
- suite-de-fibonacci
coverImage: ./images/quora.png
---

*Article initialement publié sur [Quora](https://fr.quora.com/Quel-est-lindex-du-nombre-de-Fibonacci-qui-se-termine-par-314159265/answer/Dr-Goulu)*

le premier est le 2769265 ème, qui a 578742 chiffres, commençant pas 642823662 et finissant par 314159265. Ce petit programme Python vous l'écrira en entier en 2 secondes environ:

```
n=314159265
m=10**int(len(str(n)))
from Goulib.math2 import fibonacci
i,a,b=2,1,1
while a!=n:
 a,b=(a+b)%m,a
 i+=1
print(i,n)
a=str(fibonacci(i))
print(len(a),a)

```

comme vous le voyez il calcule la suite de Fibonacci modulo m=10^9 (car il y a 9 chiffres dans 314159265), puisqu'on ne s'intéresse qu'aux derniers chiffres. Ca permet d'être rapide.

Ensuite il utilise ma fonction de calcul du ième terme par exponentiation rapide, décrite dans l'article ci-dessous pour l'afficher en entier.

[Comment calculer le 10'000'000'000'000'000'000 ème terme de la suite de Fibonacci - Pourquoi Comment Combien](https://www.drgoulu.com/2017/04/25/comment-calculer-le-1e19-eme-terme-de-la-suite-de-fibonacci/)
