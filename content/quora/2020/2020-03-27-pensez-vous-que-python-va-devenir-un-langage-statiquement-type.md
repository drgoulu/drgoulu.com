---
title: Pensez-vous que Python va devenir un langage statiquement typé ?
slug: pensez-vous-que-python-va-devenir-un-langage-statiquement-type
date: '2020-03-27'
draft: false
categories:
- Quora
tags:
- informatique
- python-langage-de-programmation
- developpement-logiciel
- statique
- langages-de-programmation
- science-de-l-informatique
- programmation-en-python
- informatique-general
- langage-de-programmation
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Pensez-vous-que-Python-va-devenir-un-langage-statiquement-typ%C3%A9/answer/Dr-Goulu)*

Il l'est déjà : tout a strictement le type objet, même un bête entier :

```
>>> type(1)
<class 'int'>
>>> dir(1) # renvoie toutes les méthodes de l'objet "1"
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']

```

Plus sérieusement, ce serait vraiment dommage de casser la magnifique structure de base de Python en introduisant des types statiques.

MAIS c'est en effet une bonne idée de rendre les outils (IDE, vérificateur de syntaxe etc.) capables de vérifier des informations sur les types. C'est l'idée de la [PEP 484 -- Type Hint](https://www.python.org/dev/peps/pep-0484/)s qui a été implantée dans Python 3.5 en 2017, supportée par la librairie standard [typing - Support for type hints](https://docs.python.org/3/library/typing.html).

Vous avez donc déjà tous les avantages du typage statique, sans les inconvénients.

Moi qui me mets au [TypeScript](w:) ces temps ( coronavirus et [StencilJS](https://stenciljs.com/) oblige…) je vois que Python a fait la même chose avec une librairie plutôt qu'un nouveau langage, et sans nécessiter de "transpiler" le code. Wow.
