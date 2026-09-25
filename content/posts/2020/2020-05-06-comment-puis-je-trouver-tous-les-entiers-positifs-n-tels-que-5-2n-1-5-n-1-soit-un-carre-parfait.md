---
title: Comment puis-je trouver tous les entiers positifs n tels que 5^(2n+1)-5^n+1 soit un carré parfait ?
slug: comment-puis-je-trouver-tous-les-entiers-positifs-n-tels-que-5-2n-1-5-n-1-soit-un-carre-parfait
date: '2020-05-06'
draft: true
categories:
- Comment
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Comment-puis-je-trouver-tous-les-entiers-positifs-n-tels-que-5-2n1-5-n1-soit-un-carr%C3%A9-parfait/answer/Dr-Goulu)*

Mon python

```
from Goulib.math2 import is_square
from itertools import count

for n in count(0):
    v=5**(2*n+1)-5**n+1
    if is_square(v):
        print(n,v)

```

me dit qu'il n'y en a pas d'autre que n=1 (v=121 = 11^2)

Qu'est-ce qui vous fait penser qu'il y en a d'autres ?

Si j'en avais trouvé 2 ou 3, j'aurais consulté [The On-Line Encyclopedia of Integer Sequences® (OEIS®)](http://oeis.org/) pour trouver éventuellement une méthode plus rapide …
