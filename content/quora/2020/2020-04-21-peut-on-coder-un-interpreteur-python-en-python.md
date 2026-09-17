---
title: Peut-on coder un interpréteur Python en Python ?
slug: peut-on-coder-un-interpreteur-python-en-python
date: '2020-04-21'
draft: false
categories:
- Quora
tags:
- informatique
- interpretes
- python-langage-de-programmation
- developpement-logiciel
- langages-de-programmation
- interprete-informatique
- science-de-l-informatique
- programmation-en-python
- creation-logicielle
- langage-de-programmation
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Peut-on-coder-un-interpr%C3%A9teur-Python-en-Python/answer/Dr-Goulu)*

Oui, regardez [A Python Interpreter Written in Python](https://www.aosabook.org/en/500L/a-python-interpreter-written-in-python.html) par exemple.

Pour ma part je me suis amusé à écrire [Goulib.expr](https://goulib.readthedocs.io/en/latest/_modules/Goulib/expr.html) qui permet de manipuler et représenter des fonctions mathématiques écrites en python sous forme symbolique en utilisant le module standard [ast - Abstract Syntax Trees](https://docs.python.org/3/library/ast.html)en interne.

Ca donne ça : [Jupyter Notebook](https://nbviewer.jupyter.org/github/Goulu/Goulib/blob/master/notebooks/expr.ipynb)

La limitation des fonctions autorisées dans les formules est nécessaire pour la sécurité, pensez-y. Faudrait pas qu’un petit malin vous mette un os.system(“format c:”) dans le code que vous allez interpréter, n’est-ce pas …
