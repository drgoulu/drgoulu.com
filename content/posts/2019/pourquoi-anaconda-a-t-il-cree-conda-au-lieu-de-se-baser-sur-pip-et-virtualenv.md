---
title: Pourquoi Anaconda a-t-il créé Conda au lieu de se baser sur Pip et VirtualEnv ?
slug: pourquoi-anaconda-a-t-il-cree-conda-au-lieu-de-se-baser-sur-pip-et-virtualenv
date: '2019-08-10'
draft: true
categories:
- Pourquoi
tags: []
coverImage: ./images/quora.png
---

*Article initialement publié sur [Quora](https://fr.quora.com/Pourquoi-Anaconda-a-t-il-cr%C3%A9%C3%A9-Conda-au-lieu-de-se-baser-sur-Pip-et-VirtualEnv/answer/Dr-Goulu)*

Pip installe des packages python, éventuellement en appelant un compilateur C ou autre pour créer des librairies. Ca pose parfois des problèmes selon votre environnement.

Conda installe des packages écrits en n'importe quel langage, avec des modules binaires precompilés pour votre plate-forme.

Il y a d'autres différences mentionnées dans:

[Understanding Conda and Pip - Anaconda](https://web.archive.org/web/20190819012748/https://www.anaconda.com/understanding-conda-and-pip/)
