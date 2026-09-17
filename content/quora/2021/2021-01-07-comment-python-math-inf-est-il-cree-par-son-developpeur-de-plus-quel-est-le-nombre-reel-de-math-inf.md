---
title: Comment Python math.inf est-il créé par son développeur ? De plus, quel est le nombre réel de «math.inf» ?
slug: comment-python-math-inf-est-il-cree-par-son-developpeur-de-plus-quel-est-le-nombre-reel-de-math-inf
date: '2021-01-07'
draft: true
categories:
- Comment
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Comment-Python-math-inf-est-il-cr%C3%A9%C3%A9-par-son-d%C3%A9veloppeur-De-plus-quel-est-le-nombre-r%C3%A9el-de-math-inf/answer/Dr-Goulu)*

Ce n'est pas propre à python mais défini dans la norme [IEEE 754](w:)sur la représentation des nombres flottants dans les processeurs, donc utilisable avec n'importe quel langage.

L'infini positif est représenté en double précision sur 64 bits par 7FF0000000000000 et l'infini négatif par FFF0000000000000, qui ne correspondent pas à des nombres autorisés dans ce format.
