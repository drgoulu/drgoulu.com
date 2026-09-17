---
title: Comment trouvez-vous des numéros en double dans un tableau s'il contient plusieurs doublons ?
slug: comment-trouvez-vous-des-numeros-en-double-dans-un-tableau-s-il-contient-plusieurs-doublons
date: '2020-07-14'
draft: true
categories:
- Comment
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Comment-trouvez-vous-des-num%C3%A9ros-en-double-dans-un-tableau-s-il-contient-plusieurs-doublons/answer/Dr-Goulu)*

en Python :

```
from random import randint

liste=[randint(0,10) for _ in range(20)]

print('liste',liste)

vus=set()
doublons=set()

for n in liste:
    if n in vus:
        doublons.add(n)
    else:
        vus.add(n)

print('doublons',doublons)
print('uniques',set(liste)-doublons)

```

donne

liste [7, 7, 8, 4, 1, 4, 8, 1, 9, 5, 0, 4, 7, 6, 10, 6, 10, 1, 10, 7]

doublons {1, 4, 6, 7, 8, 10}

uniques {0, 9, 5}
