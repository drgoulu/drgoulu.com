---
title: Jusqu’où peut-on aller de manière que le système $z+e+r+o = 0$, $u+n = 1$, $d+e+u+x = 2$, $t+r+o+i+s = 3$, $q+u+a+t+r+e = 4$, $c+i+n+q= 5$, $s+i+x = 6$, etc. ait une solution ? Les lettres sont les inconnues.
slug: jusquou-peut-on-aller-de-maniere-que-le-systeme-z-e-r-o-0-u-n-1-d-e-u-x-2-t-r-o-i-s-3-q-u-a-t-r-e-4-c-i-n-q-5-s-i-x-6-etc-ait-une-solution-les-lettres-sont-les-inconnues
date: '2021-10-13'
draft: false
categories:
- Quora
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Jusqu-o%C3%B9-peut-on-aller-de-mani%C3%A8re-que-le-syst%C3%A8me-zero-0-un-1-deux-2-trois-3-quatre-4-cinq-5-six-6-etc-ait-une-solution-Les-lettres-sont-les-inconnues/answer/Dr-Goulu)*

marrant votre problème…

A mon avis il faut tester le rang de la matrice A du système d'équations

$A_3.[z,e,r,o,u,n,d,x,t,i,s]^T = [0,1,2,3]$

les matrices $A_n$ indiquant quelles lettres/variables sont utilisées à chaque ligne en comptant jusqu'à n.

Dans l'exemple ci-dessus :

$$A_3 =  \begin{bmatrix} 1 & 1 & 1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\ 0 & 0 & 0 & 0 & 1 & 1 & 0 & 0 & 0 & 0 & 0\\ 0 & 1 & 0 & 0 & 1 & 0 & 1 & 1 & 0 & 0 & 0\\ 0 & 0 & 1 & 1 & 0 & 0 & 0 & 0 & 1 & 1 & 1 \end{bmatrix}$$

à partir de "seize" il y aura des 2 dans la matrice parce qu'il y a deux "e"

ce petit programme Python implante ceci :

```
from Goulib.math2 import get_cardinal_name, numbers_en
from Goulib.table import Table
from numpy.linalg import matrix_rank, lstsq
import numpy as np
n = 1000
a = Table()  # matrix
for i in range(n):
    s = get_cardinal_name(i, numbers_en)
    print(s)
    a.append([0]*a.ncols())
    for l in s:
        if not l.isalpha():
            continue
        if a._i(l) is None:
            a.addcol(l, 0)
        a.set(i, l, a.get(i, l)+1)
    r = matrix_rank(a)
    c = a.ncols()
    if r < c:
        print(i, r, '<', c, ': infinité de solutions')
    if r > c:
        print(i,  r, '>', c,  ': pas de solution')
        break
    if r == c:
        print(i,  r, '=', c,  ': SOLUTION UNIQUE !')
        x = lstsq(a,range(i+1))[0]
        print(dict(zip(a.titles, x)))
        break

```

en l'exécutant (avec une version de Goulib que je n'ai pas encore publiée…) on s'aperçoit qu'avec les noms des nombres en français, il y a toujours une infinité de solutions : il n'y a jamais autant, ou plus d'équations indépendantes que de variables.

Par contre avec les noms en anglais, il y a des solutions uniques à partir de 40 : la matrice a un rang de 17 pour 17 variables :

> {'z': -28.565629007518442, 'e': 5.492519298951488, 'r': 20.479707812617875, 'o': 2.593401895949113, 'n': -6.237873720737257, 't': 5.545726570947227, 'w': -6.912947270487035, 'h': -34.40263773290755, 'f': -5.454386582514031, 'u': -13.664110236616457, 'i': 15.615881716915215, 'v': -10.616900098066342, 's': 12.824348110337183, 'x': -22.48561693781589, 'g': 17.089554678267007, 'l': 12.18814906082626, 'y': 16.83555030299985}

(on peut vérifier que z+e+r+o = 0 à la précision des calculs près)

J'ai modifié le programme ci-dessus pour qu'il aille jusqu'à 9999 en résolvant le système à chaque augmentation du rang de la matrice (= nombre d'équations indépendantes) et j'ai obtenu ça :

> zero : rang = 1 < 4 : infinité de solutions
>
>
>
> one : rang = 2 < 5 : infinité de solutions
>
>
>
> two : rang = 3 < 7 : infinité de solutions
>
>
>
> three : rang = 4 < 8 : infinité de solutions
>
>
>
> four : rang = 5 < 10 : infinité de solutions
>
>
>
> five : rang = 6 < 12 : infinité de solutions
>
>
>
> six : rang = 7 < 14 : infinité de solutions
>
>
>
> seven : rang = 8 < 14 : infinité de solutions
>
>
>
> eight : rang = 9 < 15 : infinité de solutions
>
>
>
> nine : rang = 10 < 15 : infinité de solutions
>
>
>
> ten : rang = 11 < 15 : infinité de solutions
>
>
>
> eleven : rang = 12 < 16 : infinité de solutions
>
>
>
> thirteen : rang = 13 < 16 : infinité de solutions
>
>
>
> fourteen : rang = 14 < 16 : infinité de solutions
>
>
>
> fifteen : rang = 15 < 16 : infinité de solutions
>
>
>
> twenty : rang = 16 < 17 : infinité de solutions
>
>
>
> forty : rang = 17 = 17 : SOLUTION UNIQUE ! {'z': -28.565629007518442, 'e': 5.492519298951488, 'r': 20.479707812617875, 'o': 2.593401895949113, 'n': -6.237873720737257, 't': 5.545726570947227, 'w': -6.912947270487035, 'h': -34.40263773290755, 'f': -5.454386582514031, 'u': -13.664110236616457, 'i': 15.615881716915215, 'v': -10.616900098066342, 's': 12.824348110337183, 'x': -22.48561693781589, 'g': 17.089554678267007, 'l': 12.18814906082626, 'y': 16.83555030299985}
>
>
>
> one hundred : rang = 18 = 18 : SOLUTION UNIQUE ! {'z': -89.33220549779897, 'e': 57.7071448910051, 'r': 14.763270845231165, 'o': 16.86178976156269, 'n': -72.25847752796471, 't': -15.303450618366691, 'w': -9.155125041657492, 'h': -123.70812405972833, 'f': -56.08859041531002, 'u': 22.94944569671202, 'i': 97.86012085599826, 'v': -98.62183971862241, 's': 58.97722050441687, 'x': -158.82614832057527, 'g': -15.961395869170124, 'l': 14.212504085104046, 'y': 84.42804036217811, 'd': 99.11814151507092}
>
>
>
> one hundred and one : rang = 19 = 19 : SOLUTION UNIQUE ! {'z': -89.33220549779894, 'e': 57.707144891005186, 'r': 14.763270845231192, 'o': 16.86178976156268, 'n': -72.2584775279647, 't': -15.303450618366577, 'w': -9.155125041657707, 'h': -123.7081240597283, 'f': -56.08859041530995, 'u': 22.94944569671195, 'i': 97.86012085599822, 'v': -98.62183971862261, 's': 58.977220504416906, 'x': -158.82614832057533, 'g': -15.961395869170213, 'l': 14.212504085104163, 'y': 84.42804036217807, 'd': 99.11814151507089, 'a': -28.170121111709314}

Ca m'a étonné au début que les valeurs des différentes variables varient, mais en fait c'est normal : les noms des nombres sont très corrélés, tout ce qui change c'est le nombre d’occurrences des lettres …
