---
title: Quelle est la somme de tous les diviseurs positifs de $20!$ ?
slug: quelle-est-la-somme-de-tous-les-diviseurs-positifs-de-20
date: '2020-08-21'
draft: false
categories:
- Quora
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Quelle-est-la-somme-de-tous-les-diviseurs-positifs-de-20/answer/Dr-Goulu)*

```
>>> from Goulib.math2 import *
>>> sum(divisors(factorial(20)))
13891399238731734720

```

du moins avec ma [Goulib.math2.divisors](https://goulib.readthedocs.io/en/latest/_modules/Goulib/math2.html#divisors) qui inclut le 1 et le N = 20! dans le cas particulier.

Cette fonction commence par factoriser en facteurs premiers et puissances:

```
>>> list(factorize(factorial(20)))
[(2, 18), (3, 8), (5, 4), (7, 2), (11, 1), (13, 1), (17, 1), (19, 1)]

```

puis renvoie tous les produits cartésiens possibles en utilisant [itertools.product](https://docs.python.org/3/library/itertools.html#itertools.product).

Je vois à l'instant que mon résultat se retrouve dans [A062569 - OEIS](https://oeis.org/A062569), donc ça doit être juste ;-)

Par contre je n'ai pas trouvé pour quel problème vous cherchez ça… Euler ?
