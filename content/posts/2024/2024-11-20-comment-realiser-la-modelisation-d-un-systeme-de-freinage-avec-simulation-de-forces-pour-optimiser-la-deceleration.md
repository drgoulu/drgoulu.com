---
title: Comment réaliser la modélisation d'un système de freinage avec simulation de forces pour optimiser la décélération ?
slug: comment-realiser-la-modelisation-d-un-systeme-de-freinage-avec-simulation-de-forces-pour-optimiser-la-deceleration
date: '2024-11-20'
draft: false
categories:
- Comment
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Comment-r%C3%A9aliser-la-mod%C3%A9lisation-d-un-syst%C3%A8me-de-freinage-avec-simulation-de-forces-pour-optimiser-la-d%C3%A9c%C3%A9l%C3%A9ration/answer/Dr-Goulu)*

Qu'appellez-vous "optimisier la décélération" ?

- Freiner le plus vite possible ? Mettez la force max F, calculez la décélération a=m/F, calculez le temps de freinage t=v/a et la distance de freinage d=a.t²/2
- Freiner en douceur ? Étudiez les [Lois de mouvement](w:Loi_de_mouvement). C'est la même chose que ci dessus avec diverses formes de a(t) donc de F(t). Plus ces fonctions sont lisses, plus c'est doux, mais plus lent.
- Si vous voulez freiner par rapport à un objectif, par exemple un autre véhicule devant le votre, c'est un peu plus futé… vous trouverez des dizaines de brevets sur "automatic braking" qui expliquent comment on peut faire, mais comment vous ne pouvez plus faire (commercialement) puisque c'est breveté…
