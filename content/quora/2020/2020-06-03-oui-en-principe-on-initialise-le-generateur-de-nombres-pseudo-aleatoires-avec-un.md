---
title: Oui en principe on initialise le générateur de nombres pseudo-aléatoires avec un...
slug: oui-en-principe-on-initialise-le-generateur-de-nombres-pseudo-aleatoires-avec-un
date: '2020-06-03'
draft: false
categories:
- Quora
tags:
- philosophie
- hasard
- simulation-par-ordinateur
- machine
- action-de-causer-et-causalite
- probabilite-statistiques
- les-machines
- simulation
- causalite
- philosophie-des-sciences
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Comment-une-machine-peut-elle-simuler-du-hasard-Et-le-hasard-existe-t-il-vraiment-Tout-nest-il-pas-que-lien-de-causalité/answer/Dr-Goulu)*

Oui en principe on initialise le générateur de nombres pseudo-aléatoires avec une "graine" dépendant de données physiques pour éviter de répéter les mêmes séquences. Mais ce n'est pas obligatoire. On peut écrire du code qui réinitialise le générateur avec la même graine autant de fois qu'on veut.

Les [Quantum Random Number Generation (QRNG) de ID Quantique](https://www.idquantique.com/random-number-generation/overview/) à Genève émettent des photons un à un vers une lame semi transparente qui a exactement une chance sur 2 de les laisser passer, ou de les réfléchir. Un détecteur fournit des bits 0/1 parfaitement aléatoires.
