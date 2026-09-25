---
title: Comment avons-nous découvert toutes les décimales de pi ?
slug: comment-avons-nous-decouvert-toutes-les-decimales-de-pi
date: '2019-12-06'
draft: false
categories:
- Comment
tags:
- sciences
- histoire
- mathematiques
- decouvertes-scientifiques
- calcul
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Comment-avons-nous-d%C3%A9couvert-toutes-les-d%C3%A9cimales-de-pi/answer/Dr-Goulu)*

Il y a des programmes informatiques qui les calculent de façon très efficace.

mon préféré est un algorithme incroyable qui travaille uniquement en nombres entiers [[1]](#BJCec) !

Cette version Python se trouve dans ma [Goulib.math2](https://goulib.readthedocs.io/en/latest/_modules/Goulib/math2.html#pi_digits_gen) :

```
def pi_digits_gen():
''' generates pi digits as a sequence of INTEGERS ! using Jeremy Gibbons spigot generator
:see :http://www.cs.ox.ac.uk/people/jeremy.gibbons/publications/spigot.pdf  '''
# code from http://davidbau.com/archives/2010/03/14/python_pipy_spigot.html
	q, r, t, j = 1, 180, 60, 2
	while True:
		u, y = 3*(3*j+1)*(3*j+2), (q*(27*j-12)+5*r)//(5*t)
		yield y
		q, r, t, j = 10*q*j*(2*j-1), 10*u*(q*(5*j-2)+r-y*t), t*u, j+1

```

A vrai dire, il ne calcule "que" 15'000 décimales correctes (incroyablement vite) mais il en existe d'autres qui vont beaucoup, beaucoup plus loin

Il existe même des méthodes pour obtenir la n-ième décimale sans calculer les précédentes !

Voir [Pi Formulas, Algorithms and Computations](https://bellard.org/pi/)

Notes de bas de page

[[1]](#cite-BJCec)[http://www.cs.ox.ac.uk/people/je...](http://www.cs.ox.ac.uk/people/jeremy.gibbons/publications/spigot.pdf)
