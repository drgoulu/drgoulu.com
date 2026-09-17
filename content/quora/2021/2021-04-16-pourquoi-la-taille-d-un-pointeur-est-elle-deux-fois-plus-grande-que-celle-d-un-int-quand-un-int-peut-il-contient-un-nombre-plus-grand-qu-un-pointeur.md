---
title: Pourquoi la taille d'un pointeur est-elle deux fois plus grande que celle d'un int, quand un int peut-il contient un nombre plus grand qu'un pointeur ?
slug: pourquoi-la-taille-d-un-pointeur-est-elle-deux-fois-plus-grande-que-celle-d-un-int-quand-un-int-peut-il-contient-un-nombre-plus-grand-qu-un-pointeur
date: '2021-04-16'
draft: true
categories:
- Pourquoi
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Pourquoi-la-taille-d-un-pointeur-est-elle-deux-fois-plus-grande-que-celle-d-un-int-quand-un-int-peut-il-contient-un-nombre-plus-grand-qu-un-pointeur/answer/Dr-Goulu)*

un pointeur a la taille d'une adresse en mémoire (32 ou 64 bits)

un int fait normalement 16 bits (15 s'il est signé), un long 32 bits et un long long 64 bits.

[https://fr.wikipedia.org/wiki/Ty...](w:Types_de_donnée_du_langage_C)
