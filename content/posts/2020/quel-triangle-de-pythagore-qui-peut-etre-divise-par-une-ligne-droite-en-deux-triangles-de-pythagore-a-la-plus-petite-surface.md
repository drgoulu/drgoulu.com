---
title: Quel triangle de Pythagore, qui peut être divisé par une ligne droite en deux triangles de Pythagore, a la plus petite surface ?
slug: quel-triangle-de-pythagore-qui-peut-etre-divise-par-une-ligne-droite-en-deux-triangles-de-pythagore-a-la-plus-petite-surface
date: '2020-08-27'
draft: false
categories:
- Quora
tags:
- mathematiques
- questions
- geometrie
- probleme
- enigmes
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Quel-triangle-de-Pythagore-qui-peut-%C3%AAtre-divis%C3%A9-par-une-ligne-droite-en-deux-triangles-de-Pythagore-a-la-plus-petite-surface/answer/Dr-Goulu)*

N'importe quel triangle rectangle coupé par la hauteur donne deux triangles rectangles, donc satisfaisant le Théorème de Pythagore.

Vous avez oublié de préciser que les côtés devaient être des nombres entiers, je parie…

Bon dans ce cas, on cherche le plus petit Triplet pythagoricien dont la hauteur ab/c soit entière.

```
from Goulib.math2 import triples
for a, b, c in triples() :
  if a*b % c ==0:
    print(a, b, c)
    break

```

dit que c'est (15,20,25), de hauteur 12, donc de surface 25*12/2 = 150 et qui se coupe en deux triangles rectangles (9,12,15) et (12,16,20)

[2017 et les triplets pythagoriciens - Pourquoi Comment Combien](/2017/01/02/2017-et-les-triplets-pythagoriciens/)
