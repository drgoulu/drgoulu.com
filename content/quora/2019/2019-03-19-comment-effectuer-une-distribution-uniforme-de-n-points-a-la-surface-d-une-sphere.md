---
title: Comment effectuer une distribution uniforme de n points à la surface d'une sphère ?
slug: comment-effectuer-une-distribution-uniforme-de-n-points-a-la-surface-d-une-sphere
date: '2019-03-19'
draft: false
categories:
- Comment
tags:
- mathematiques
- distribution
- simulation-par-ordinateur
- spheres
- algorithmes-d-optimisation
- geometrie-spherique
- algorithmes
- simulation-numerique
- geometrie
- post
coverImage: ./images/quora.png
---

*Article initialement publié sur [Quora](https://fr.quora.com/Comment-effectuer-une-distribution-uniforme-de-n-points-%C3%A0-la-surface-dune-sph%C3%A8re/answer/Dr-Goulu)*

Ah ça c’est une question intéressante… Qu’entendez-vous par “uniforme” ?

- vous voulez recouvrir complètement la sphère par des n disques de même rayon? Les disques sont donc forcés de se recouvrir partiellement. Mathématiquement on “minimise la distance maximale ‘d’ de tout point de la sphère à son voisin le plus proche”. C’est le problème du “**covering**”.
- le “**packing**” est une petite nuance consistant à “maximiser la distance minimale entre les points”. Autrement dit, l’optimum est atteint lorsqu’on ne peut plus écarter les deux points les plus proches car l’un se rapprocherait davantage d’un troisième point.
- le “**convex hull**” consiste à maximiser le volume du solide convexe défini par les N sommets
- la “**minimisation de l’énergie potentielle**” consiste à minimiser la somme de l’énergie qui serait accumulée dans des ressorts liant chaque paire de points. Les ressorts peuvent être soit linéaire (d’ordre 1), soit quadratiques (ordre 2) ce qui correspond au cas de la **répulsion électrostatique** de points supposés chargés électriquement.

Cela dit, pour certaines valeurs de N ces 4 problèmes fusionnent et il existe une solution exacte, voir [Spherical Codes with Icosahedral Symmetry](http://neilsloane.com/icosahedral.codes/)

Si vous ne cherchez pas l’optimum absolu il existe plusieurs heuristiques qui donnent rapidement des résultats très acceptables ( voir [Points on a sphere](http://www.softimageblog.com/archives/115) ). La méthode de la spirale d’or est celle que j’utilise dans la libraire Python [Goulib.graph.points_on_sphere](https://goulib.readthedocs.io/en/latest/_modules/Goulib/graph.html#points_on_sphere)

[comment placer N points “régulièrement” sur une sphère ? - Pourquoi Comment Combien](https://www.drgoulu.com/2007/01/31/comment-placer-n-points-regulierement-sur-une-sphere/#.XJFWeChsOCo)
