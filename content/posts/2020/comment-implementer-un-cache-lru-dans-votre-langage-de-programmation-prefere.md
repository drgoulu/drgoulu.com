---
title: Comment implémenter un cache LRU dans votre langage de programmation préféré ?
slug: comment-implementer-un-cache-lru-dans-votre-langage-de-programmation-prefere
date: '2020-07-19'
draft: true
categories:
- Comment
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Comment-impl%C3%A9menter-un-cache-LRU-dans-votre-langage-de-programmation-pr%C3%A9f%C3%A9r%C3%A9/answer/Dr-Goulu)*

en python, c'est déjà disponible dans la librairie [functools sous la forme du décorateur lru_cache](https://docs.python.org/3.3/library/functools.html).

L'implantation en pur python est sur GitHub là : [python/cpython](https://github.com/python/cpython/blob/3.3/Lib/functools.py)

[les décorateurs, ou pourquoi j'aime toujours la programmation - Pourquoi Comment Combien](/2010/12/03/les-decorateurs-python/)
