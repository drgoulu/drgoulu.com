---
title: Est-ce quelqu'un peut m'aide à faire le fit en utilisant la methode des splines cubiques en fortran ?
slug: est-ce-quelqu-un-peut-m-aide-a-faire-le-fit-en-utilisant-la-methode-des-splines-cubiques-en-fortran
date: '2020-08-25'
draft: false
categories:
- Quora
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Est-ce-quelqu-un-peut-m-aide-%C3%A0-faire-le-fit-en-utilisant-la-methode-des-splines-cubiques-en-fortran/answer/Dr-Goulu)*

En FORTRAN ???

bon alors faites comme indiqué dans [Calling Python from Fortran (not the other way around)](https://www.noahbrenowitz.com/post/calling-fortran-from-python/)en appelant un programme Python qui appelle [SciPy.inetrpolate.CubicSpline](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.CubicSpline.html)

Après ça vous remplacerez tout votre code Fortran par du Python, et vous me remercierez de vous avoir propulsé au 21ème siècle.

De rien…

Mais si vous voulez rester au 20ème, ya une outil du 21ème qui s'appelle Google, et si on y cherche "Fortran cubic spline" on tombe sur [https://ww2.odu.edu/~agodunov/co...](https://ww2.odu.edu/~agodunov/computing/programs/book2/Ch01/spline.f90)

De rien non plus.
