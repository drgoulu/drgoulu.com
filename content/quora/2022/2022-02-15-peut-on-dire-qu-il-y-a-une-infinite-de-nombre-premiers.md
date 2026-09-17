---
title: Peut-on dire qu'il y a une infinité de nombre premiers ?
slug: peut-on-dire-qu-il-y-a-une-infinite-de-nombre-premiers
date: '2022-02-15'
draft: false
categories:
- Quora
tags:
- mathematiques
- nombres-naturels
- infinite-general
- theorie-des-nombres-premiers
- infini-mathematiques
- sciences-mathematiques
- theorie-des-nombres
- mathematiques-et-sciences
- theoreme-des-nombres-premiers
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Peut-on-dire-quil-y-a-une-infinit%C3%A9-de-nombre-premiers/answer/Dr-Goulu)*

Oui, on peut, et c'est même très facile à démontrer.

Si il y en avait une suite finie, en faisant le produit de tous les termes et en y ajoutant 1, on obtiendrait soit :

- un nombre premier
- un nombre pouvant être factorisé en facteurs premiers qui ne sont pas dans la suite.

On ajoute les nouveaux nombres premiers ainsi découverts à la suite, et on recommence à l'infini …

Je viens de faire un petit programme python (ci-dessous) qui produit cette suite :

2, 3, 7, 43, 13, 139, 3263443, 547, 607, 1033, 31051, 29881, …

et je découvre que c'est [A126263 - OEIS](https://oeis.org/A126263) , qui est la factorisation de la [Suite de Sylvester](w:), alors merci pour la question.

Le p'tit Python :

```
from Goulib.math2 import factors
suite = set()
prod = 1
def add(n):
    global prod
    if n in suite:
        return
    suite.add(n)
    prod = prod*n
    print(n, end=', ')
add(2)
while True:
    for n in factors(prod+1):
        add(n)

```
