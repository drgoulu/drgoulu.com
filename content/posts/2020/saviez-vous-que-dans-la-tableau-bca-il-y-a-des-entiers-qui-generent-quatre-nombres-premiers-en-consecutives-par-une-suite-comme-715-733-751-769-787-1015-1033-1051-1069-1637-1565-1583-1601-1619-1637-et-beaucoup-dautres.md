---

title: Saviez-vous que dans la tableau (BCA) il y a des entiers qui génèrent quatre nombres premiers en consécutives par une suite comme 715, 733,751, 769,787** 1015, 1033, 1051, 1069,1637 ** 1565,1583,1601,1619,1637 ** -et beaucoup d’autres ?
slug: saviez-vous-que-dans-la-tableau-bca-il-y-a-des-entiers-qui-generent-quatre-nombres-premiers-en-consecutives-par-une-suite-comme-715-733-751-769-787-1015-1033-1051-1069-1637-1565-1583-1601-1619-1637-et-beaucoup-dautres
date: '2020-03-19'
draft: true
categories:
- Quora
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Saviez-vous-que-dans-la-tableau-BCA-il-y-a-des-entiers-qui-g%C3%A9n%C3%A8rent-quatre-nombres-premiers-en-cons%C3%A9cutives-par-une-suite-comme-715-733751-769787-1015-1033-1051-10691637/answer/Dr-Goulu)*

Je peux immédiatement vous dire que c'est faux, parce que certains de vos nombres "premiers" finissent par un 5, donc ils sont divisibles par 5.

En plus je peux vous dire que même si c'était juste, ça n'a rien d'étonnant parce que si vous faites un tableau des nombres qui ne sont ni multiples de 2 de 3 de 5 ou de 7 et que vous affichez les suites d'au moins 5 nombres premiers consécutifs qu'il contient, ça donne ça : (jusqu'à 1000)

[11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]

[149, 151, 157, 163, 167]

[223, 227, 229, 233, 239, 241]

[257, 263, 269, 271, 277, 281, 283]

[409, 419, 421, 431, 433]

[739, 743, 751, 757, 761]

[821, 823, 827, 829, 839]

[1039, 1049, 1051, 1061, 1063]

[1087, 1091, 1093, 1097, 1103, 1109]

[1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307]

[1423, 1427, 1429, 1433, 1439]

[1471, 1481, 1483, 1487, 1489, 1493, 1499]

[1543, 1549, 1553, 1559, 1567, 1571]

[1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627]

[1861, 1867, 1871, 1873, 1877, 1879, 1889]

[1993, 1997, 1999, 2003, 2011, 2017]

[2081, 2083, 2087, 2089, 2099]

[2129, 2131, 2137, 2141, 2143]

[2333, 2339, 2341, 2347, 2351]

[2371, 2377, 2381, 2383, 2389, 2393, 2399]

[2539, 2543, 2549, 2551, 2557]

[2671, 2677, 2683, 2687, 2689, 2693, 2699]

[2789, 2791, 2797, 2801, 2803]

[3449, 3457, 3461, 3463, 3467, 3469]

[3527, 3529, 3533, 3539, 3541, 3547]

[3907, 3911, 3917, 3919, 3923, 3929, 3931]

[4637, 4639, 4643, 4649, 4651, 4657]

[4783, 4787, 4789, 4793, 4799, 4801]

[5639, 5641, 5647, 5651, 5653, 5657, 5659, 5669]

[5839, 5843, 5849, 5851, 5857, 5861]

[6197, 6199, 6203, 6211, 6217, 6221]

[6563, 6569, 6571, 6577, 6581]

[6823, 6827, 6829, 6833, 6841]

[7669, 7673, 7681, 7687, 7691]

[8999, 9001, 9007, 9011, 9013]

Le code python correspondant est ici :

```
from Goulib.math2 import is_prime

consecutif=[] # liste de nombres premiers consecutifs
for n in range(10000):
    if n%2==0:continue
    if n%3==0:continue
    if n%5==0:continue
    if n%7==0:continue
    # on va dire que n est un nombre du fameux tableau
    if is_prime(n):
        consecutif.append(n)
    else:
        if len(consecutif)>=5:
            print(consecutif)
        consecutif=[]

```

Comme je vous l'ai dit dans un autre message, on connaît des dizaines de suites qui génèrent des candidats nombres premiers.

Donc je me répète : c'est un sujet passionnant, mais commencez par étudier ce qui a été fait depuis quelques millénaires avant de croire que vous avez fait une découverte…
