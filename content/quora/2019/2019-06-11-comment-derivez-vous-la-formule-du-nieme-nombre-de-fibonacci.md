---
title: Comment dérivez-vous la formule du nième nombre de Fibonacci ?
slug: comment-derivez-vous-la-formule-du-nieme-nombre-de-fibonacci
date: '2019-06-11'
draft: false
categories:
- Comment
tags:
- mathematiques
- nombres
- algorithmes
- equations
- formules
coverImage: ./images/quora.png
---

*Article initialement publié sur [Quora](https://fr.quora.com/Comment-d%C3%A9rivez-vous-la-formule-du-ni%C3%A8me-nombre-de-Fibonacci/answer/Dr-Goulu)*

La méthode la plus rapide et qui ne fait pas intervenir les nombres réels (et leur perte de précision numérique en informatique) est d'utiliser l'idée d'un certain Brenner en 1951: écrire la récurrence de Fibonacci sous forme matricielle.

La matrice toute simple $Q=\begin{pmatrix}1&1\\1&0\end{pmatrix}$ permet d’obtenir un nouveau terme de la série de Fibonacci en la multipliant par un vecteur formé des deux termes précédents:

$$\begin{pmatrix}1&1\\1&0\end{pmatrix}\begin{pmatrix}\mathcal F_{n-1}\\\mathcal F_{n-2}\end{pmatrix}=\begin{pmatrix}\mathcal F_{n}\\\mathcal F_{n-1}\end{pmatrix}$$

En enchaînant les multiplications matricielles, on obtient le n-ième terme à partir des deux premiers (0,1) ainsi :

$$\begin{pmatrix}1&1\\1&0\end{pmatrix}^{n-1}\begin{pmatrix}1\\0\end{pmatrix}=\begin{pmatrix}\mathcal F_{n}\\\mathcal F_{n-1}\end{pmatrix}$$

En fait on retrouve les termes de la suite directement dans la matrice

$$Q^n = \begin{pmatrix}\mathcal F_{n+1}&\mathcal F_{n}\\\mathcal F_{n}&\mathcal F_{n-1}\end{pmatrix}$$

L’algorithme de l'[exponentiation rapide](http://www.wikipedia.org/search-redirect.php?language=fr&go=Go&search=exponentiation+rapide) permet d’élever la matrice Q à la puissance n en effectuant $log_2(n)$ multiplications de matrices 2×2, ce qui est hyper rapide.

En utilisant cette combine, mon [petit code python](https://gist.github.com/goulu/f56725fa32fbb4840c855a8309662c9d#file-fibonacci-py) permet de calculer le 10^19 ème terme de Fibonacci en un pouillème de seconde (ok, modulo quelque chose…)

[Comment calculer le 10'000'000'000'000'000'000 ème terme de la suite de Fibonacci - Pourquoi Comment Combien](/2017/04/25/comment-calculer-le-1e19-eme-terme-de-la-suite-de-fibonacci/)
