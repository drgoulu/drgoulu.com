---
title: Tout nombre de la forme 6n±1 est premier s'il n'est pas le produit de 2 nombres premier ?
slug: tout-nombre-de-la-forme-6n1-est-premier-s-il-n-est-pas-le-produit-de-2-nombres-premier
date: '2020-07-23'
draft: false
categories:
- Quora
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Tout-nombre-de-la-forme-6n1-est-premier-s-il-n-est-pas-le-produit-de-2-nombres-premier/answer/Dr-Goulu)*

Non c'est faux.

```
from Goulib.math2 import omega, prime_factors
from itertools import count

def test(n):
    if omega(n)>2:
        print(n,list(prime_factors(n)))

for i in count(1):
    test(6*i-1)
    test(6*i+1)

```

génère les nombres de la forme donnée et leurs facteurs premiers uniques dès qu'il y en a plus de 2 (fonction [omega - Wikipedia](w:en:Prime_omega_function)) :

```
385 [5, 7, 11]
455 [5, 7, 13]
595 [5, 7, 17]
665 [5, 7, 19]
715 [5, 11, 13]
805 [5, 7, 23]
935 [5, 11, 17]
1001 [7, 11, 13]
1015 [5, 7, 29]
1045 [5, 11, 19]
1085 [5, 7, 31]
1105 [5, 13, 17]
1235 [5, 13, 19]
1265 [5, 11, 23]
1295 [5, 7, 37]

```

il y en a vraiment beaucoup…
