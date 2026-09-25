---
title: Un dict est-il ordonné par défaut en Python ?
slug: un-dict-est-il-ordonne-par-defaut-en-python
date: '2020-11-06'
draft: false
categories:
- Quora
tags:
- informatique
- programmation
- langage
- python
- donnees
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Un-dict-est-il-ordonn%C3%A9-par-d%C3%A9faut-en-Python/answer/Dr-Goulu)*

Les dicts n'étaient pas ordonnés avant la version 3.5, puis ils l'étaient mais ce n'était pas une feature dans 3.5 et 3.6, et c'est une feature depuis 3.7.

Je ne vois pas vraiment la raison de ceci vu que la librairie standard [collections offrait déjà un OrderedDict](https://docs.python.org/3.8/library/collections.html#collections.OrderedDict) pour les cas où c'était nécessaire.

D'autant que les dicts sont des [tables de hachage](w:Table_de_hachage), les structures de données au cœur de Python, donc chaque nanoseconde compte …

Plus d'infos dans cette réponse à [How are Python's Built In Dictionaries Implemented?](https://stackoverflow.com/a/9022835/1395973) sur StackAdvisor

le code source est sur GitHub [python/cpython/objects/dictobject.c](https://github.com/python/cpython/blob/master/Objects/dictobject.c)
