---
title: Comment peut-on inverser une liste en Python ?
slug: comment-peut-on-inverser-une-liste-en-python
date: '2019-04-04'
draft: true
categories:
- Comment
tags: []
coverImage: ./images/quora.png
---

*Article initialement publié sur [Quora](https://fr.quora.com/Comment-peut-on-inverser-une-liste-en-Python/answer/Dr-Goulu)*

```
l.reverse()

```

inverse la liste en place.

```
l[::-1]

```

renvoie la liste inversée (slice du début à la fin, par pas de -1)

```
for x in reversed(l):

```

itère la liste (ou n'importe quel objet itérable) à l'envers. Et permet de quitter la boucle si une condition sur x est remplie sans tout inverser. Bref, les iterateurs c'est le pied.

[How to Reverse a List in Python – dbader.org](https://dbader.org/blog/python-reverse-list)
