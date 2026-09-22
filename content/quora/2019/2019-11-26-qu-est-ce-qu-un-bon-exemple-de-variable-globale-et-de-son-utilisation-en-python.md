---
title: Qu'est-ce qu'un bon exemple de variable globale et de son utilisation en Python ?
slug: qu-est-ce-qu-un-bon-exemple-de-variable-globale-et-de-son-utilisation-en-python
date: '2019-11-26'
draft: false
categories:
- Quora
tags:
- programmation
- langage
- conseils
- python
- developpement-logiciel
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Quest-ce-quun-bon-exemple-de-variable-globale-et-de-son-utilisation-en-Python/answer/Dr-Goulu)*

il n'y a aucun bon exemple d'utilisation d'une variable globale dans aucun langage. Les variables globales, c'est le Mal.

En Python, les quelques variables globales indispensables sont rangées dans un dict retourné par la fonction globals():

```
>>> globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>}

```

Comme vous le voyez, toutes les variables globales ont un nom encadré par des __doubles__ , ce qui signifie qu'elles sont privées et ne doivent pas être utilisées, sauf par des adultes consentants.

quand vous faites

```
>>> a=1

```

vous polluez cette pure beauté minimaliste:

```
>>> globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'a': 1}

```

BEARK !
