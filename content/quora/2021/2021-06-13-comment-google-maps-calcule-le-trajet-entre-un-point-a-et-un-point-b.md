---
title: Comment Google Maps calcule le trajet entre un point A et un point B ?
slug: comment-google-maps-calcule-le-trajet-entre-un-point-a-et-un-point-b
date: '2021-06-13'
draft: true
categories:
- Comment
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Comment-Google-Maps-calcule-le-trajet-entre-un-point-A-et-un-point-B/answer/Dr-Goulu)*

Google n'a jamais publié l'algorithme qu'ils utilisent.

Beaucoup de systèmes de routage utilisent l'

[https://fr.wikipedia.org/wiki/Al...](w:Algorithme_A*)

qui est une extension de l'[Algorithme de Dijkstra](w:) favorisant la recherche dans une bande entourant la ligne droite entre les deux points.

Ca le rend un peu plus efficace que Dijkstra (qui cherche en quelque sorte en cercles depuis A) dans les cas où il y a plusieurs routes parallèles.
