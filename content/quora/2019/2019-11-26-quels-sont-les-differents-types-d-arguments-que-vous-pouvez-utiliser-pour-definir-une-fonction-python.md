---
title: Quels sont les différents types d'arguments que vous pouvez utiliser pour définir une fonction Python ?
slug: quels-sont-les-differents-types-d-arguments-que-vous-pouvez-utiliser-pour-definir-une-fonction-python
date: '2019-11-26'
draft: false
categories:
- Quora
tags:
- langages-de-programmation
- developpement-logiciel
- arguments-et-argumentation
- fonctions
- python-langage-de-programmation
- programmation-en-python
- fonctions-general
- langage-de-programmation
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Quels-sont-les-diff%C3%A9rents-types-darguments-que-vous-pouvez-utiliser-pour-d%C3%A9finir-une-fonction-Python/answer/Dr-Goulu)*

un seul : référence à un objet. ( [Python - Functions](https://www.tutorialspoint.com/python/python_functions.htm) )

il faut bien réaliser qu'en python, même les (petits) entiers sont des objets, par exemple :

```
>>> a=100
>>> (a+a) is 2*a
True

```

parce que l'objet 200 est le même des deux côtés du is, car prédéfini, mais

```
>>> a=1000
>>> (a+a) is 2*a
False

```

parce que là, Python construit deux instances d'objets 2000 distinctes.

donc même quand vous croyez passer un entier en paramètre à une fonction, vous passez en réalité une référence à un objet de classe int

```
>>> type(1)
<class 'int'>

```
