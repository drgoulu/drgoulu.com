---
title: Comment intégrer 4000 points équidistants sur la carte de France de façon à déterminer quelle serait la distance entre chacun de ces points ?
slug: comment-integrer-4000-points-equidistants-sur-la-carte-de-france-de-facon-a-determiner-quelle-serait-la-distance-entre-chacun-de-ces-points
date: '2021-09-23'
draft: false
categories:
- Comment
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Comment-int%C3%A9grer-4000-points-%C3%A9quidistants-sur-la-carte-de-France-de-fa%C3%A7on-%C3%A0-d%C3%A9terminer-quelle-serait-la-distance-entre-chacun-de-ces-points/answer/Dr-Goulu)*

Fondamentalement c'est un problème de "packing de cercles" ( [Circle packing - Wikipedia](w:en:Circle_packing) ) dans un polygone compliqué… Il n'y a pas de méthode générale à ma connaissance .

Personnellement j'attaquerais le problème à l'envers : je ferais un réseau de points répartis sur un réseau hexagonal de taille de maille d quelconque, j'en placerai un au [Centre de la France](w:) de votre choix, puis je compterais combien de points N se retrouvent à l'intérieur des frontières, ce qui permet de tenir compte de contraintes non spécifiés comme les lacs, les îles, la distance à la frontière acceptable etc.

Si N est plus grand que 4000, on augmente d, si N est plus petit on diminue d et on recommence. Quand on arrive très près de 4000, on peut essayer de décaler un peu l'origine et/ou de tourner le réseau de quelques degrés pour trouver une configuration avec exactement 4000 points et le d maximal.

En Python ça devrait me prendre 1h. Vous payez combien ?
