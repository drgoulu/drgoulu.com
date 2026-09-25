---
title: Svp qui peut résoudre cet exercice ? Ecrire un programme qui demande à l’utilisateur d’introduire deux nombres entiers et déduit si les deux nombres sont premiers entre eux et calcule le plus petit multiple commun.
slug: svp-qui-peut-resoudre-cet-exercice
date: '2022-10-15'
draft: true
categories:
- Quora
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Svp-qui-peut-r%C3%A9soudre-cet-exercice-Ecrire-un-programme-qui-demande-%C3%A0-l-utilisateur-d-introduire-deux-nombres-entiers-et-d%C3%A9duit-si-les-deux-nombres-sont-premiers-entre-eux-et-calcule-le/answer/Dr-Goulu)*

en Python:

```
from math import gcd # greatest common divisor, pgcd en français
a,b=1549,1729 # vos deux nombres
if gcd(a, b)==1:
  print('premiers entre eux')
print('ppcm=', a*b/gcd(a,b)) # je vous laisse démontrer

```
