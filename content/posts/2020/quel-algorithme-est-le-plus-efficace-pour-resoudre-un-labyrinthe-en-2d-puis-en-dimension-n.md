---
title: Quel algorithme est le plus efficace pour résoudre un labyrinthe (en 2D puis en dimension n) ?
slug: quel-algorithme-est-le-plus-efficace-pour-resoudre-un-labyrinthe-en-2d-puis-en-dimension-n
date: '2020-04-24'
draft: false
categories:
- Quora
tags:
- informatique
- intelligence-artificielle
- probleme
- dimensions
- algorithmes
coverImage: ./images/qimg-56ad525eca780c9344e43b4f3d8958ab.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Quel-algorithme-est-le-plus-efficace-pour-r%C3%A9soudre-un-labyrinthe-en-2D-puis-en-dimension-n/answer/Dr-Goulu)*

Ca dépend si vous "voyez" tout le labyrinthe ou juste là où vous êtes.

Si vous connaissez tout le labyrinthe, vous pouvez construire un graphe de toutes les "portes" et culs de sac :

![](./images/qimg-56ad525eca780c9344e43b4f3d8958ab.png)

puis recherche le chemin minimal entre votre position et la sortie avec un [Algorithme de Dijkstra](w:). Comme vous le voyez, cette méthode marche quel que soit le nombre de dimensions du labyrinthe.

Si vous n'avez qu'une vue locale, vous allez devoir explorer le labyrinthe… L'algorithme de la main gauche ne marche qu'en 2D et si le labyrinthe n'a pas d'île qui vous fait tourner en rond …

L'algorithme de Trémaux est celui qui marche le mieux à ma connaissance. Comme il n'était décrit qu'en anglais sur la Wikipédia, je viens de le traduire en français : [Résolution de labyrinthe - Algorithme de Trémaux — Wikipédia](w:Résolution_de_labyrinthe). Je en mets ici que la petite animation qui l'illustre :

![](./images/qimg-cff6e2d70a94ac664e5f9245a5268d74.gif)

Je ne suis pas absolument certain que ça marche en N dimension, mais au pif je dirais que oui ….

autre page intéressante [Modélisation mathématique de labyrinthe — Wikipédia](w:Modélisation_mathématique_de_labyrinthe)
