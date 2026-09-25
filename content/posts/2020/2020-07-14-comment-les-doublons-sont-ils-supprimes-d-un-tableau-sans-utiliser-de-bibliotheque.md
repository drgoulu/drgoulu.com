---
title: Comment les doublons sont-ils supprimés d'un tableau sans utiliser de bibliothèque ?
slug: comment-les-doublons-sont-ils-supprimes-d-un-tableau-sans-utiliser-de-bibliotheque
date: '2020-07-14'
draft: true
categories:
- Comment
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Comment-les-doublons-sont-ils-supprim%C3%A9s-d-un-tableau-sans-utiliser-de-biblioth%C3%A8que/answer/Dr-Goulu)*

```
# librairie juste pour créer le tableau
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
print('uniques',[x for x in liste if x not in doublons])

```

donne:

liste [3, 0, 8, 6, 1, 9, 4, 2, 1, 7, 8, 9, 9, 2, 5, 2, 1, 4, 0, 8]

doublons {0, 1, 2, 4, 8, 9}

uniques [3, 6, 7, 5]
