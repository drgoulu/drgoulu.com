---
title: Comment calculer le polynôme caractéristique d'une matrice qui à 04 lignes et 04 colonnes ?
slug: comment-calculer-le-polynome-caracteristique-d-une-matrice-qui-a-04-lignes-et-04-colonnes
date: '2022-05-02'
draft: true
categories:
- Comment
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Comment-calculer-le-polyn%C3%B4me-caract%C3%A9ristique-d-une-matrice-qui-%C3%A0-04-lignes-et-04-colonnes/answer/Dr-Goulu)*

avec l'[Algorithme de Faddeev-Leverrier](w:). Il ne nécessite que de calculer des traces de matrices, ce qui permet de le calculer facilement à la main pour de petites matrices 4x4

Avec un ordinateur, on préfère calculer les valeurs propres en triangularisant la matrice, ce qui est plus rapide pour de grandes matrices.
