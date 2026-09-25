---
title: Comment réaliser des opérations arithmétiques avec des nombres complexes dans Python ?
slug: comment-realiser-des-operations-arithmetiques-avec-des-nombres-complexes-dans-python
date: '2019-11-11'
draft: true
categories:
- Comment
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Comment-r%C3%A9aliser-des-op%C3%A9rations-arithm%C3%A9tiques-avec-des-nombres-complexes-dans-Python/answer/Dr-Goulu)*

[import cmath](https://docs.python.org/fr/3.7/library/cmath.html)

```
import cmath # et tout devient transparent
def quad(a, b, c):
''' solves quadratic equations ax^2+bx+c=0 '''
	discriminant = b*b - 4 *a*c
	d=cmath.sqrt(discriminant)
	return (-b + d) / (2*a), (-b - d) / (2*a)

```
