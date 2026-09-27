---
title: Comment calculer la puissance n ieme d’une matrice ?
slug: comment-calculer-la-puissance-n-ieme-dune-matrice
date: '2023-03-03'
draft: false
categories:
- Comment
tags:
- mathematiques
- calcul
- post
- puissance
- calculs-matriciels
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Comment-calculer-la-puissance-n-ieme-d-une-matrice/answer/Dr-Goulu)*

Pour n "grand", le mieux est d'utiliser l'[Exponentiation rapide](w:).

par exemple pour n=13,

on calcule $A^2=A\times A$, puis $A^4=A^2\times A^2$, puis$A^8=A^4\times A^4$

et là on s'arrête parce que 8 > 13/2

et yapluka calculer $A^{13}=A^8\times A^4\times A$

et on a le résultat en 5 multiplications au lieu de 13.

Ca paraît être une petite amélioration, mais pour$n=10^{19}$ il suffit de 63 multiplications …

C'est l'algo utilisé par des librairies comme NumPy ([numpy.linalg.matrix_power](https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_power.html)) mais comme il travaille en nombres flottants ils bute assez vite sur de grands nombres, donc j'ai implanté

[Goulib.math2 mod_mathpow](https://goulib.readthedocs.io/en/latest/modules/Goulib.math2.html#Goulib.math2.mod_matpow) pour [calculer le 10'000'000'000'000'000'000 ème terme de la suite de Fibonacci](/2017/04/25/comment-calculer-le-1e19-eme-terme-de-la-suite-de-fibonacci/#.ZAI6t3bMKCo) .

Ouais, parce que figurez vous qu'on peut calculer ce terme en 63 multiplications de matrices 2x2 …
