---
title: Pensez-vous que Python va devenir un langage compilé ?
slug: pensez-vous-que-python-va-devenir-un-langage-compile
date: '2020-03-27'
draft: false
categories:
- Quora
tags:
- informatique
- interpretation
- python-langage-de-programmation
- developpement-logiciel
- compilateurs
- langages-de-programmation
- science-de-l-informatique
- programmation-en-python
- theorie-du-langage-de-programmation
- langage-de-programmation
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Pensez-vous-que-Python-va-devenir-un-langage-compil%C3%A9/answer/Dr-Goulu)*

Ce serait dommage pour sa magnifique structure, donc non.

Si vous avez besoin de performances Python peut interfacer des libraires compilées. [NumPy](https://numpy.org/) et [OpenCV](https://pypi.org/project/opencv-python/) sont des exemples typiques, mais il y en a plein d'autres.

Si vous voulez "juste" livrer un exécutable avec tout votre programme python, vous pouvez empaqueter tout ce qu'il faut avec [py2exe](http://py2exe.org/) ou [PyInstaller](http://www.pyinstaller.org/) que je préfère personnellement.

Si vous avez VRAIMENT besoin de compiler du python, vous pouvez regarder du côté de [Cython](w:), mais il vous faudra probablement réécrire votre code python "à la C". (oui, ça produit en effet du code python à la c…)
