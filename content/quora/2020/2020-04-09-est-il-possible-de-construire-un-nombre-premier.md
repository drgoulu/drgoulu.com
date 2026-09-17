---
title: Est-il possible de construire un nombre premier?
slug: est-il-possible-de-construire-un-nombre-premier
date: '2020-04-09'
draft: false
categories:
- Quora
tags:
- mathematiques
- nombres-naturels
- theorie-des-nombres-premiers
- nombres-mathematiques
- nombres-composes
- sciences-mathematiques
- theorie-analytique-des-nombres
- theorie-des-nombres
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Est-il-possible-de-construire-un-nombre-premier/answer/Dr-Goulu)*

Vous voulez dire utiliser des opérations arithmétiques pour fabriquer un nombre qui sera premier à coup sur ?

Non. Tôt ou tard vous devrez utiliser un [Test de primalité](w:) pour vérifier par de (nombreux) tests que votre nombre est premier.

Mais les tests de primalité modernes sont si rapides que ça prend un temps minuscule d'obtenir un nombre premier très grand.

Par exemple ma fonction Python [Goulib.math2.random_prime](https://goulib.readthedocs.io/en/latest/_modules/Goulib/math2.html#random_prime) génère un nombre premier de 512 bits en 90 millisecondes environ :

```
from Goulib.math2 import random_prime
print(random_prime(512)) # nombre premier de 512 bits
11966091219040191487555704318380503808675320479409291237155451396388172809464310317140318617428324168640936877089298988764736967644218465456289306462851649

```

[Comment trouver des nombres premiers - Pourquoi Comment Combien](https://www.drgoulu.com/2012/04/15/comment-produire-des-nombres-premiers/#.Xo9vZMiiGCo)
