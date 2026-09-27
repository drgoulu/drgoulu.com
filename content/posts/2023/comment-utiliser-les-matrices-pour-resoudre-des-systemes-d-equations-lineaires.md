---
title: Comment utiliser les matrices pour résoudre des systèmes d'équations linéaires ?
slug: comment-utiliser-les-matrices-pour-resoudre-des-systemes-d-equations-lineaires
date: '2023-02-10'
draft: false
categories:
- Comment
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Comment-utiliser-les-matrices-pour-r%C3%A9soudre-des-syst%C3%A8mes-d-%C3%A9quations-lin%C3%A9aires/answer/Dr-Goulu)*

votre système peut se mettre sous la forme matricielle $A.x=b$ où $A$ est une matrice carrée dans laquelle la i-ème ligne contient les coefficients $a_ij$des inconnues $x_j$ du vecteur colonne $x$, et $b_i$ le terme constant correspondant rangé dans le vecteur colonne $b$.

L'idée de base est de multiplier votre équation matricielle par la [matrice inverse](w:Matrice_inversible) $A^{-1}$ ce qui donne :

$A^{-1}.A.x=A^{-1}.b$ soit $I.x=A^{-1}.b$

où I est la [Matrice identité](w:)donc $x=A^{-1}.b$

: le vecteur x contenant les solutions de l'équation est obtenu en multipliant "simplement" les termes constants b par la [matrice inverse](w:Matrice_inversible) $A^{-1}$

Résoudre le système revient donc à inverser la matrice A, ce qui peut ne pas être trivial :

1. la matrice peut ne pas être inversible, ce qui correspond à un système sous-déterminé : certaines équations sont dépendantes les unes des autres et il y a une infinité de solutions x
2. Inverser une grosse matrice est très pénible. En général le prof vous en donne plein de 3x3 à inverser à la main, et une de 4x4 pour que vous n'ayez plus jamais envie de recommencer. Et si vous programmez la résolution d'un système par inversion de matrice, vous êtes une grosse brute parce que vous allez faire ramer votre machine dès une petite matrice de 100x100 de rien du tout. (et il y en a de BEAUCOUP plus grosses quand vous calculez par éléments finis notamment)

Donc en pratique on préfère "décomposer" la matrice A en un produit de matrices ayant des caractéristiques facilitant énormément l'inversion, voir [Décomposition LU](w:), [Décomposition QR](w:)ou [Factorisation de Cholesky](w:).

Dans beaucoup de problèmes pratiques comme les éléments finis, on peut tirer d'énormes avantages du fait que la matrice A contient plein de zéros, l'idéal étant quand on arrive à ordonner les équations pour que la matrice A ait une structure de bande, idéalement [tridiagonale](w:Matrice_tridiagonale).
