---
title: Lisp est-il un langage de programmation facile ?
slug: lisp-est-il-un-langage-de-programmation-facile
date: '2019-05-29'
draft: false
categories:
- Quora
tags:
- sciences
- theorie
- informatique
- programmation
- langage
coverImage: ./images/quora.png
---

*Article initialement publié sur [Quora](https://fr.quora.com/Lisp-est-il-un-langage-de-programmation-facile/answer/Dr-Goulu)*

Lots of Insipid and Stupid Parenthesis ? Non, pas facile du tout.

Au début ça va, si on a un IDE qui formate ça bien avec des parenthèses multicolores, ce qui n'est pas le cas ci-dessous:

```
(defun factorial (n &optional (acc 1))
"Calcule la factorielle de l'entier n."
(if (<= n 1)
	acc
	(factorial (- n 1) (* acc n))))

```

et puis ça donne des [choses comme ça](https://github.com/AeroNotix/lispkit/blob/master/browser.lisp) (un bout de browser en LISP trouvé sur GitHub) …

Sérieusement : dès que j'ai appris LISP en 1986, je me suis dépêché d'apprendre Prolog pour ce qu'on appelait intelligence artificielle à l'époque., et aujourd'hui les bonnes idées de LISP (car il y en a quand même…) se retrouvent beaucoup plus clairement dans des langages comme Python

voir [Python for Lisp Programmers](https://norvig.com/python-lisp.html)
