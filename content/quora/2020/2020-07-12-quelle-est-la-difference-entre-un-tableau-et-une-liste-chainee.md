---
title: Quelle est la différence entre un tableau et une liste chaînée ?
slug: quelle-est-la-difference-entre-un-tableau-et-une-liste-chainee
date: '2020-07-12'
draft: false
categories:
- Quora
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Quelle-est-la-diff%C3%A9rence-entre-un-tableau-et-une-liste-cha%C3%AEn%C3%A9e/answer/Dr-Goulu)*

En principe un tableau est alloué en mémoire en un seul bloc, ce qui permet d'accéder instantanément (O(1)) au n-ème élément en calculant son adresse. Par contre l'agrandissement du tableau est coûteux car il faut allouer un autre bloc et copier le contenu.

La liste chaînée est constituée de plusieurs blocs alloués contenant quelques éléments voire un seul, et un pointeur vers le bloc suivant. L'accès au n-ème élément est plus lent (O(n)) mais l'agrandissement de la liste est rapide, surtout qu'en pratique on conserve toujours un pointeur vers le dernier bloc.
