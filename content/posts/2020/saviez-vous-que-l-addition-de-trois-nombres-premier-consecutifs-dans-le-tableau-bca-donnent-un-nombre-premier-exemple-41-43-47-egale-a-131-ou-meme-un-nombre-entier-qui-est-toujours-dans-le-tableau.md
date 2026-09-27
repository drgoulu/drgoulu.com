---

title: Saviez-vous que l'addition de trois nombres premier consécutifs dans le tableau BCA donnent un nombre premier, exemple, 41+43+47 égale à 131 ,ou mémé un nombre entier qui est toujours dans le tableau ?
slug: saviez-vous-que-l-addition-de-trois-nombres-premier-consecutifs-dans-le-tableau-bca-donnent-un-nombre-premier-exemple-41-43-47-egale-a-131-ou-meme-un-nombre-entier-qui-est-toujours-dans-le-tableau
date: '2020-03-24'
draft: true
categories:
- Quora
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Saviez-vous-que-l-addition-de-trois-nombres-premier-cons%C3%A9cutifs-dans-le-tableau-BCA-donnent-un-nombre-premier-exemple-414347-%C3%A9gale-%C3%A0-131-ou-m%C3%A9m%C3%A9-un-nombre-entier-qui-est-toujours-dans/answer/Dr-Goulu)*

Oui, c'est le [Théorème de Vinogradov](w:).

Comme je vous aime bien [User-11268771547521209629](https://fr.quora.com/profile/User-11268771547521209629) , je vous ai fait ce petit programme python:

```
from Goulib.math2 import primes_gen, nextprime, is_prime
from Goulib.itertools2 import groups

def recurse(consecutifs):
    s = sum(consecutifs)
    if not is_prime(s):
        return []
    else:
        s1 = nextprime(s)
        s2 = nextprime(s1)
        return [s,s1,s2] + recurse([s, s1, s2])

lmax = 0
for consecutifs in groups(primes_gen(), 3, 1):
    l = recurse(consecutifs)
    if len(l) > lmax:
        print(list(consecutifs)+l)
        lmax = len(l)

```

il produit les suites de trois nombres premiers consécutifs, dont la somme est un nombre premier qui, avec les deux nombres premiers consécutifs a une somme qui est un nombre premier qui, avec les deux nombres premiers consécutifs a une somme qui etc.

Et comme il y en a beaucoup, le programme n'affiche que les suites de triplets plus longues que le précédentes (mises en forme à la main car j'avais la flemme de le faire en Python.

La première est

[5, 7, 11, 23, 29, 31, 83, 89, 97, 269, 271, 277]

parce que 5+7+11=23 qui puis 23+29+31 = 83, puis 83+89+97=269, puis 269+271+277= 817 qui n'est pas premier

les autres suites trouvées par mon programme sont :

[7, 11, 13, 31, 37, 41, 109, 113, 127, 349, 353, 359, 1061, 1063, 1069]

[2543, 2549, 2551, 7643, 7649, 7669, 22961, 22963, 22973, 68897, 68899, 68903, 206699, 206749, 206779, 620227, 620233, 620237]

[249217, 249229, 249233, 747679, 747713, 747731, 2243123, 2243161, 2243177, 6729461, 6729469, 6729473, 20188403, 20188451, 20188459, 60565313, 60565319, 60565327, 181695959, 181695961, 181695967]

[1783841, 1783843, 1783867, 5351551, 5351579, 5351581, 16054711, 16054721, 16054729, 48164161, 48164191, 48164201, 144492553, 144492563, 144492583, 433477699, 433477721, 433477729, 1300433149, 1300433153, 1300433171, 3901299473, 3901299497, 3901299511]

[2494517, 2494523, 2494537, 7483577, 7483601, 7483603, 22450781, 22450817, 22450849, 67352447, 67352449, 67352507, 202057403, 202057417, 202057423, 606172243, 606172253, 606172283, 1818516779, 1818516851, 1818516853, 5455550483, 5455550501, 5455550539, 16366651523, 16366651537, 16366651577]

tout ça sans mystérieux tableau BCA ;-)
