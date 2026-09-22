---
title: Peut-on obtenir 1000 entiers consécutifs dont aucun n'est premier ?
slug: peut-on-obtenir-1000-entiers-consecutifs-dont-aucun-n-est-premier
date: '2022-11-16'
draft: false
categories:
- Quora
tags:
- mathematiques
- nombres-naturels
- suite-d-entiers
- theorie
- nombres
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Peut-on-obtenir-1000-entiers-cons%C3%A9cutifs-dont-aucun-nest-premier/answer/Dr-Goulu)*

Oui, voir [Écart entre nombres premiers — Wikipédia](w:Écart_entre_nombres_premiers) .

les nombres premiers dont l'écart au suivant est plus grand que les précédents sont listés dans [A002386 - OEIS](https://oeis.org/A002386) où vous trouverez plein de liens utiles

Je vous ai fait ce petit python vite fait:

```
from Goulib.math2 import primes_gen
pp=1
record=1
for p in primes_gen():
    gap=p-pp
    if gap>record:
        record=gap
        print(record,pp,p)
    pp=p

```

qui produit ça :

```
2 3 5
4 7 11
6 23 29
8 89 97
14 113 127
18 523 541
20 887 907
22 1129 1151
34 1327 1361
36 9551 9587
44 15683 15727
52 19609 19661
72 31397 31469
86 155921 156007
96 360653 360749
112 370261 370373
114 492113 492227
118 1349533 1349651
132 1357201 1357333
148 2010733 2010881
154 4652353 4652507
180 17051707 17051887
210 20831323 20831533
220 47326693 47326913

```

après ça devient de plus en plus lent, on devrait arriver à 1000 dans quelques mois …

les trois colonnes sont :

- le gap record ([A005250 - OEIS](https://oeis.org/A005250) )
- le premier premier auquel ce gap apparaît ( [A002386 - OEIS](https://oeis.org/A002386) )
- le premier suivant ( [A000101 - OEIS](https://oeis.org/A000101) )
