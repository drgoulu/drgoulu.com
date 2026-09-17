---
title: Comment comparez-vous les concepts de OOP avec "struct" en C ?
slug: comment-comparez-vous-les-concepts-de-oop-avec-struct-en-c
date: '2021-06-27'
draft: true
categories:
- Comment
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Comment-comparez-vous-les-concepts-de-OOP-avec-struct-en-C/answer/Dr-Goulu)*

Un objet est un struct contenant des pointeurs sur des fonctions (méthodes) qui reçoivent un pointeur sur le struct en paramètre (this).

Une classe se résume aux fonctions qui allouent un pointeur sur un struct /objet (constructeur) et le desallouent (destructeur)

Le premier compilateur C++ de [Bjarne Stroustrup](w:) générait du code C très instructif.
