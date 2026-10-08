---
title: La somme de ces nombres est 1634 + 8208 + 9474 = 19316.Trouver la somme de tous les nombres qui peuvent être écrits comme la somme des puissances cinquièmes de leurs chiffres?
slug: la-somme-de-ces-nombres-est-1634-8208-9474-19316-trouver-la-somme-de-tous-les-nombres-qui-peuvent-etre-ecrits-comme-la-somme-des-puissances-cinquiemes-de-leurs-chiffres
date: '2019-12-05'
draft: false
categories:
- Quora
tags:
- sciences
- mathematiques
- nombres
- questions
- maths
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/La-somme-de-ces-nombres-est-1634-8208-9474-19316-Trouver-la-somme-de-tous-les-nombres-qui-peuvent-%C3%AAtre-%C3%A9crits-comme-la-somme-des-puissances-cinqui%C3%A8mes-de-leurs-chiffres/answer/Dr-Goulu)*

C'est le [Problème 30 du Project Euler](https://projecteuler.net/problem=30) , très mal exprimé.

Ma solution en python est:

```
def problem_030():
    """Find the sum of all the numbers that can be written as the sum of fifth powers of their digits."""
    candidates = range(2, 6*(9**5))
    return sum(n for n in candidates if sum(x**5 for x in digits(n)) == n)

```

la fonction digits étant dans ma librairie [Goulib.math2](https://web.archive.org/web/20230925195105/https://goulib.readthedocs.io/en/latest/_modules/Goulib/math2.html#digits) .

[Programmer pour le fun - Pourquoi Comment Combien](/2009/02/24/project_euler/)
