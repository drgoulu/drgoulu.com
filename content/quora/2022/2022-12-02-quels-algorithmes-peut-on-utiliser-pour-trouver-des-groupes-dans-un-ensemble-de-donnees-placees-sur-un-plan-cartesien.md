---
title: Quels algorithmes peut-on utiliser pour trouver des groupes dans un ensemble de données placées sur un plan cartésien ?
slug: quels-algorithmes-peut-on-utiliser-pour-trouver-des-groupes-dans-un-ensemble-de-donnees-placees-sur-un-plan-cartesien
date: '2022-12-02'
draft: false
categories:
- Quora
tags:
- sciences-informatiques
- statistiques
- clustering
- algorithmes
- classification-apprentissage-automatique
- analyse-des-donnees
- donnees
- science-des-donnees
- algorithmes-de-graphe
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Quels-algorithmes-peut-on-utiliser-pour-trouver-des-groupes-dans-un-ensemble-de-donn%C3%A9es-plac%C3%A9es-sur-un-plan-cart%C3%A9sien/answer/Dr-Goulu)*

Ça s'appelle [Partitionnement de données](w:)et l'algo le plus connu est les [K-moyennes](w:). Mais il faut prédéfinir le nombre de groupes (k) ou faire plusieurs calculs à tâtons pour trouver "le bon k".

J'ai utilisé [OPTICS](w:)dans un cas où il fallait déterminer k automatiquement.

En passant, ces algos sont indépendants du nombre de dimensions de vos données. Ça marche pour N dimensions cartésiennes, ou même pas cartésiennes. Tout ce qu'il faut, c'est une fonction donnant une distance entre 2 données.

Dans le cas mentionné plus haut, la distance était calculée entre des [Perceptual hash](w:en:Perceptual_hashing) d'images,
