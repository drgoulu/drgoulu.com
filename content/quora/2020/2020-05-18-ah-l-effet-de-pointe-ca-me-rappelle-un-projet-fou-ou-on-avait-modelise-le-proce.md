---
title: Ah l'effet de pointe… ça me rappelle un projet fou où on avait modélisé le proce...
slug: ah-l-effet-de-pointe-ca-me-rappelle-un-projet-fou-ou-on-avait-modelise-le-proce
date: '2020-05-18'
draft: true
categories:
- Quora
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Pourquoi-en-mathématiques-l-infini-est-accepté-mais-pas-en-physique/answer/Dr-Goulu)*

Ah l'effet de pointe… ça me rappelle un projet fou où on avait modélisé le processus d'[Électro-érosion](w:), où la probabilité d'amorçage d'une étincelle dépendait de la courbure locale du matériau usiné. Et l'étincelle creusait une calotte sphérique en faisant un bord bien anguleux….

Ca ne donnait pas du tout ce qu'on observait.

On a ajouté un petit
courbure:=min(courbure, n/rayon_d_un_atome);
avec un petit n et ça allait beaucoup mieux…
