---
title: Comment comprendre la méthode du pivot de Gauss sur le calcul de l’inverse d’une matrice ?
slug: comment-comprendre-la-methode-du-pivot-de-gauss-sur-le-calcul-de-linverse-dune-matrice
date: '2020-05-18'
draft: true
categories:
- Comment
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Comment-comprendre-la-m%C3%A9thode-du-pivot-de-Gauss-sur-le-calcul-de-l-inverse-d-une-matrice/answer/Dr-Goulu)*

La méthode de l' [Élimination de Gauss-Jordan](w:)permet de résoudre un système d'équations linéaires M.x=a.

En l'appliquant n fois pour a=vecteurs colonnes successifs de la matrice identité I, on obtient les n vecteurs x formant la matrice inverse de M.

Ceci prend O(n^4) opérations car Gauss Jordan en demande O(n^3).

C'est pour ça qu'on préfère la [Décomposition LU](w:), qui demande O(n^3) une seule fois, puis n fois O(n^2) opérations pour résoudre les n systèmes, donc O(2n^3) environ.
