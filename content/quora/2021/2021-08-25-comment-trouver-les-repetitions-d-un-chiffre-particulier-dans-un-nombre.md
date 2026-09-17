---
title: Comment trouver les répétitions d'un chiffre particulier dans un nombre ?
slug: comment-trouver-les-repetitions-d-un-chiffre-particulier-dans-un-nombre
date: '2021-08-25'
draft: true
categories:
- Comment
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Comment-trouver-les-r%C3%A9p%C3%A9titions-d-un-chiffre-particulier-dans-un-nombre/answer/Dr-Goulu)*

en Python, comme ça:

```
n=37864712646823700147178256780097682347589057816782648981234905
print(str(n).count('1'))

>>> 5

```

ou comme ça:

```
from Goulib.itertools2 import compress
from Goulib.math2 import digits
n=37864712646823700147178256780097682347589057816782648981234905
print(list(compress(sorted(digits(n)))))

>>> [(0, 6), (1, 5), (2, 6), (3, 4), (4, 6), (5, 4), (6, 7), (7, 10), (8, 10), (9, 4)]

```
