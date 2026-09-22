---
title: Peut-on dire qu’à partir d’un cahier des charges, avec deux langages différents, on obtiendra deux programmes compilés identiques, pour un même processeur ?
slug: peut-on-dire-qua-partir-dun-cahier-des-charges-avec-deux-langages-differents-on-obtiendra-deux-programmes-compiles-identiques-pour-un-meme-processeur
date: '2019-04-01'
draft: false
categories:
- Quora
tags:
- sciences
- informatique
- programmation
- langage
- architecture
coverImage: ./images/quora.png
---

*Article initialement publié sur [Quora](https://fr.quora.com/Peut-on-dire-qu-%C3%A0-partir-d-un-cahier-des-charges-avec-deux-langages-diff%C3%A9rents-on-obtiendra-deux-programmes-compil%C3%A9s-identiques-pour-un-m%C3%AAme-processeur/answer/Dr-Goulu)*

Non, c’est quasiment impossible d’obtenir deux programmes compilés identiques. Déjà il ne reste plus beaucoup de langages compilés actifs : C++, Go, Swift, Ada, et, il faut le dire, ces bon vieux Formol et Cobtran. Les autres (Python, Java, JavaScript etc.) font chacun leur “bytecode” interprété.

Les langages compilés et leurs compilateurs sont suffisamment différents dans la représentation des objets voire des chaines de caractères, le passage de paramètres etc et l’optimisation du code pour les processeurs actuels qu’ils vont produire du code différent, à part peut-être pour print(“Hello World!”).
