---
title: Quelles sont les limitations des dataclasses de Python 3.7 comparé aux classes classiques de Python ?
slug: quelles-sont-les-limitations-des-dataclasses-de-python-3-7-compare-aux-classes-classiques-de-python
date: '2019-06-12'
draft: false
categories:
- Quora
tags:
- langages-de-programmation
- developpement-logiciel
- classes
- python-3
- versions-de-python
- programmation-orientee-objet
- python-langage-de-programmation
- developpeurs-python
coverImage: ./images/quora.png
---

*Article initialement publié sur [Quora](https://fr.quora.com/Quelles-sont-les-limitations-des-dataclasses-de-Python-3-7-compar%C3%A9-aux-classes-classiques-de-Python/answer/Dr-Goulu)*

les [dataclasses](https://docs.python.org/fr/3/library/dataclasses.html) sont des classes classiques additionnées de "décorateurs" qui génèrent automatiquement le code du constructeur et de diverses autres "méthodes magiques" comme __str__

Si vous ne connaissez pas la notion de décorateur, commencez par ça parce que c'est absolument génial, et très simple en python[[1]](#eAGNb) . Et évidemment renseignez vous aussi sur les "méthodes magiques" si vous ne les connaissez pas.

Après ça les choses seront claires : vous ne pouvez pas (simplement) écrire votre propre constructeur ou méthode magique d'une dataclasse. Par contre vous pouvez lui ajouter plein d'autres méthodes comme une classe normale.

Notes de bas de page

[[1]](#cite-eAGNb)[les décorateurs, ou pourquoi j'aime toujours la programmation - Pourquoi Comment Combien](/2010/12/03/les-decorateurs-python/)
