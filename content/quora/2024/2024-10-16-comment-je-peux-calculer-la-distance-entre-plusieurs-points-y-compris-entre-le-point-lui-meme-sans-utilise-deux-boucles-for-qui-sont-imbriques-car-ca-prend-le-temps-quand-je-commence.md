---
title: Comment je peux calculer la distance entre plusieurs points y compris entre le point lui-même sans utilisé deux boucles for qui sont imbriqués car ça prend le temps quand je commence à avoir plusieurs points comme 2000 points en python ?
slug: comment-je-peux-calculer-la-distance-entre-plusieurs-points-y-compris-entre-le-point-lui-meme-sans-utilise-deux-boucles-for-qui-sont-imbriques-car-ca-prend-le-temps-quand-je-commence
date: '2024-10-16'
draft: false
categories:
- Comment
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Comment-je-peux-calculer-la-distance-entre-plusieurs-points-y-compris-entre-le-point-lui-m%C3%AAme-sans-utilis%C3%A9-deux-boucles-for-qui-sont-imbriqu%C3%A9s-car-%C3%A7a-prend-le-temps-quand-je-commence-%C3%A0/answer/Dr-Goulu)*

Vous avez vraiment besoin des distances entre tous les points ? Vous êtes sur ? C'est pour quoi ?

Parce que pour trouver par exemple le chemin le plus court entre deux points, on ne fait pas comme ça. On commence par mettre les points dans un graphe en ne reliant que les points les plus proches, par exemple avec une [Triangulation de Delaunay](w:)(exemple python [Delaunay graphs from geographic points](https://networkx.org/documentation/stable/auto_examples/geospatial/plot_delaunay.html)), puis on utilise un [Algorithme A*](w:)par exemple, tous deux disponibles dans la librairie python [NetworkX](https://networkx.org/), indispensable.

Si vous essayez plutôt de simuler un système gravitationnel, avec des points qui bougent etc., alors lisez ça, il y a plein de liens python et autres :

[https://drgoulu.com/2008/11/16/l...](https://drgoulu.com/2008/11/16/le-probleme-a-n-corps/)

Tous ces algorithmes sont O(n.log n) au lieu de O(n^2) comme les deux boucles imbriquées.

Dans votre cas ça veut dire 2000*11 opérations au lieu de 2000*2000. Environ 100× plus rapide. Et certaines librairies utilisent du code C compilé…
