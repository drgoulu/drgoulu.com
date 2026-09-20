---
title: Qu’est-ce que Nearest Prime et comment ça fonctionne ?
slug: quest-ce-que-nearest-prime-et-comment-ca-fonctionne
date: '2025-03-27'
draft: false
categories:
- Comment
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Qu-est-ce-que-Nearest-Prime-et-comment-%C3%A7a-fonctionne/answer/Dr-Goulu)*

En français c'est le "nombre premier le plus proche".

Vous partez d'un nombre N donné, vous vérifiez s'il est premier (avec un test de primalité rapide), et s'il ne l'est pas vous essayez avec le nombre impair directement supérieur à N, et aussi celui directement inférieur, et vous répétez jusqu'à trouver un nombre premier P, qui sera donc le plus proche de N.

C'est utilisé abondamment pour générer des clés de cryptage de longueur voulue, en partant de N = une séquence de bits aléatoires de longueur voulue.

[https://drgoulu.com/2012/04/15/c...](/2012/04/15/comment-produire-des-nombres-premiers/)
