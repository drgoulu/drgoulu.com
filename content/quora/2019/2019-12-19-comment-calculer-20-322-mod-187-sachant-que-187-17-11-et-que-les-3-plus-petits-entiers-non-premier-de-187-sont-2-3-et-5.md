---
title: Comment calculer 20^322 mod 187 sachant que 187 = 17*11 et que les 3 plus petits entiers non premier de 187 sont 2,3 et 5?
slug: comment-calculer-20-322-mod-187-sachant-que-187-17-11-et-que-les-3-plus-petits-entiers-non-premier-de-187-sont-2-3-et-5
date: '2019-12-19'
draft: true
categories:
- Comment
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Comment-calculer-20-322-mod-187-sachant-que-187-1711-et-que-les-3-plus-petits-entiers-non-premier-de-187-sont-23-et-5/answer/Dr-Goulu)*

Python dit ([fonction](https://docs.python.org/3.7/library/functions.html#pow) de base…)

```
>>> pow(20,322,187)
26

```

L'algo utilise l'[Exponentiation modulaire](w:).

Je suis sur que des matheux peuvent se casser la tête beaucoup plus longtemps en utilisant les propriétés de 187 que vous mentionnez …
