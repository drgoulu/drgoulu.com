---
title: Mouais, on peut jouer sur les mots, mais même sans passage d'argument, en fait l...
slug: mouais-on-peut-jouer-sur-les-mots-mais-meme-sans-passage-d-argument-en-fait-l
date: '2020-06-30'
draft: false
categories:
- Quora
tags:
- langages-de-programmation
- developpement-logiciel
- variables
- python-langage-de-programmation
- ingenierie-logicielle
- programmation-en-python
- creation-logicielle
- developpement-informatique
- developpement-de-logiciels
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Est-il-possible-de-créer-un-logiciel-en-Python-sans-variables-Si-possible-comment/answer/Dr-Goulu)*

Mouais, on peut jouer sur les mots, mais même sans passage d'argument, en fait les "variables" sont des clés des champs (…) dans un object dict :

>>> a=1548

>>> dir() # montre le dictionnaire global, avec la "variable" a:

['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a']

>>> b=a # référence le même objet. b n'est donc PAS une nouvelle "variable"

>>> a is b

True

>>> b=1549-1 # référence un nouvel objet ayant la même valeur que a

>>> a is b

False

Quand on passe des arguments, on passe en fait un dict, qui contient donc forcément des références
