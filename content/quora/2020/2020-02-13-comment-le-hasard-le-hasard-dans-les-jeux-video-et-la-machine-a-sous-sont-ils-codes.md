---
title: Comment le hasard, le hasard dans les jeux vidéo et la machine à sous sont-ils codés ?
slug: comment-le-hasard-le-hasard-dans-les-jeux-video-et-la-machine-a-sous-sont-ils-codes
date: '2020-02-13'
draft: false
categories:
- Comment
tags:
- informatique
- statistiques
- algorithmes
- sciences-informatiques
- probabilite-statistiques
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Comment-le-hasard-le-hasard-dans-les-jeux-vid%C3%A9o-et-la-machine-%C3%A0-sous-sont-ils-cod%C3%A9s/answer/Dr-Goulu)*

Dans les jeux vidéo, un [Générateur de nombres pseudo-aléatoires](w:) suffit largement. En gros on prend un nombre qui change souvent, comme le nombre de microsecondes depuis le démarrage de la machine, on le multiplie par un grand nombre premier, on ajoute un autre nombre premier et on garde le résultat modulo quelque chose comme nombre aléatoire (voir [Générateur congruentiel linéaire — Wikipédia](w:Générateur_congruentiel_linéaire))

Pour les machines à sous, poker en ligne etc, on utilise de plus en plus des [Générateur de nombres aléatoires matériel](w:) basés sur des principes physiques, notamment quantiques.
