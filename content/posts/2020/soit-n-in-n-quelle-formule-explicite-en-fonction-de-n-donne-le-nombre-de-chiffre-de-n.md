---
title: Soit $n\in\N^*$. Quelle formule explicite en fonction de $n$ donne le nombre de chiffre de $n$ ?
slug: soit-n-in-n-quelle-formule-explicite-en-fonction-de-n-donne-le-nombre-de-chiffre-de-n
date: '2020-07-23'
draft: true
categories:
- Quora
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Soit-ninN-Quelle-formule-explicite-en-fonction-de-n-donne-le-nombre-de-chiffre-de-n/answer/Dr-Goulu)*

en python:

```
from math import log10, ceil
def ndigits(n):
  return ceil(log10(n+1))

```

ça renvoie 0 pour n=0, mais vous avez dit $\N^*$ …
