---
title: Comment convertir un programme Python en code C ou C ++?
slug: comment-convertir-un-programme-python-en-code-c-ou-c
date: '2019-05-10'
draft: true
categories:
- Comment
tags: []
coverImage: ./images/quora.png
---

*Article initialement publié sur [Quora](https://fr.quora.com/Comment-convertir-un-programme-Python-en-code-C-ou-C/answer/Dr-Goulu)*

Il faut tout réécrire, c'est trop différent.

Ou écrire en C++ un programme qui interprète du Python. Mais ça existe déjà, il s'appelle python.exe…

Si votre code python a des problèmes de performance, isolez les 10% qui prennent 90% du temps, ne réécrivez que ça et utilisez [Cython](w:) pour linker au Python.
