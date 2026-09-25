---
title: Comment trouvez-vous les valeurs intégrales de n pour que 6n ^ 2 + 3 soit un carré parfait ?
slug: comment-trouvez-vous-les-valeurs-integrales-de-n-pour-que-6n-2-3-soit-un-carre-parfait
date: '2020-08-28'
draft: false
categories:
- Comment
tags:
- mathematiques
- probleme
- equations
- resolutions
- algebre
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Comment-trouvez-vous-les-valeurs-int%C3%A9grales-de-n-pour-que-6n-2-3-soit-un-carr%C3%A9-parfait/answer/Dr-Goulu)*

je pense que vous voulez dire valeurs entières.

je fais un programme python:

```
from Goulib.math2 import is_square
for n in range(10000000):
    if is_square(6*n**2+3):
         print(n,',',end="")

```

il imprime : 1 ,11 ,109 ,1079 ,10681 ,105731 ,1046629

je coupe/colle dans [The On-Line Encyclopedia of Integer Sequences® (OEIS®)](http://oeis.org/) et je trouve que la série [A054320](http://oeis.org/A054320) correspond, avec plein de formules pour la générer par récurrence, ou directement le n-ième élément

$a(n) =\frac{(\sqrt{6}-2)(5+2\sqrt{6})^n-(\sqrt{6}+2)(5-2\sqrt{6})^n}{4}$
