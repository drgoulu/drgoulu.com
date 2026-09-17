---
title: Quelle est la stratégie optimale pour jouer à ce jeu ? Combien de suppositions faut-il pour toujours trouver un nombre entre 1 et 100 ? Et pouvez-vous implémenter cette stratégie dans votre code ?
slug: quelle-est-la-strategie-optimale-pour-jouer-a-ce-jeu
date: '2022-06-04'
draft: true
categories:
- Combien
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Quelle-est-la-strat%C3%A9gie-optimale-pour-jouer-%C3%A0-ce-jeu-Combien-de-suppositions-faut-il-pour-toujours-trouver-un-nombre-entre-1-et-100-Et-pouvez-vous-impl%C3%A9menter-cette-strat%C3%A9gie-dans-votre/answer/Dr-Goulu)*

quel jeu ? deviner un nombre entre 1 et 100 si l'autre répond "plus grand" ou "plus petit" ?

Il faut au maximum log2(100), donc 7 coups, en divisant toujours par 2 :

- 50 ? plus petit !
- 25 ? plus petit !
- 12.5 mais arrondissons à 13 ? plus grand !
- bon alors la moyenne (25+13)/2 = 19 ? plus grand !
- bon alors entre 25 et 19 il y a (25+19)/2 = 22 ? plus petit !
- entre 19 et 22, une chance sur deux … 21 ? non ! plus petit !
- alors ça ne peut être que 20. En 7 coups. CQFD.

Oui, je peux implémenter cette stratégie dans mon code, ça s'appelle une [Recherche dichotomique](w:), mais je ne vais pas faire votre devoir à votre place ;-)
