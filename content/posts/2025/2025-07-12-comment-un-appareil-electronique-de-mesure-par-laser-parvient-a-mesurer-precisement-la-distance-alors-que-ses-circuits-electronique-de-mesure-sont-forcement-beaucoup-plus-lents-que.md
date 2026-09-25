---
title: Comment un appareil électronique de mesure par laser parvient à mesurer précisément la distance alors que ses circuits électronique de mesure sont forcément (beaucoup) plus lents que la vitesse de la lumière réfléchie sur la cible ?
slug: comment-un-appareil-electronique-de-mesure-par-laser-parvient-a-mesurer-precisement-la-distance-alors-que-ses-circuits-electronique-de-mesure-sont-forcement-beaucoup-plus-lents-que
date: '2025-07-12'
draft: false
categories:
- Comment
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Comment-un-appareil-%C3%A9lectronique-de-mesure-par-laser-parvient-%C3%A0-mesurer-pr%C3%A9cis%C3%A9ment-la-distance-alors-que-ses-circuits-%C3%A9lectronique-de-mesure-sont-forc%C3%A9ment-beaucoup-plus-lents-que-la/answer/Dr-Goulu)*

Non. 1 GHz est une fréquence tout à fait courante en électronique, et pendant un milliardième de seconde la lumière parcourt 30 cm seulement.

Pour des mesures beaucoup plus précises on utilise l'[Interférométrie](w:) : un dispositif purement optique combine le faisceau "aller" (optionnellement modulé) avec le faisceau "retour" et l'électronique analyse le signal résultant. Il suffit parfois de compter le nombre d'impulsions reçues pendant un certain temps. Les compteurs actuels peuvent être extraordinairement rapides (centaines de GHz). Avec ça on arrive à mesurer des mouvements relatifs de l'ordre du nanomètre.

Les micropositionneurs de masques pour la gravure de puces fonctionnent comme ça.
