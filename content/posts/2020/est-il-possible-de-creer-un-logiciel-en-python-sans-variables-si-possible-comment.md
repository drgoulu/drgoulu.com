---
title: Est-il possible de créer un logiciel en Python sans variables ? Si possible comment ?
slug: est-il-possible-de-creer-un-logiciel-en-python-sans-variables-si-possible-comment
date: '2020-06-29'
draft: true
categories:
- Comment
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Est-il-possible-de-cr%C3%A9er-un-logiciel-en-Python-sans-variables-Si-possible-comment/answer/Dr-Goulu)*

Il n'y a pas de variables en Python, il n'y a que des références à des objets[[1]](#XOhDb).

Donc même si vous écrivez par exemple

```
print(sum(range(100)))

```

en réalité vous passez des références à des objets de classe fonction

D'ailleurs :

```
a=print
b=sum
c=range
a(b(c(100)))
4950

```

Notes de bas de page

[[1]](#cite-XOhDb)[Valeurs et références en Python](http://sametmax.com/valeurs-et-references-en-python/)
