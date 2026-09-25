---
title: Vous jouez à un concours contre 100 personnes, sachant que le gagnant est celui qui donne le nombre entier le plus grand inférieur à 100 et unique. Si quelqu'un d'autre a donné le même nombre que vous, vous êtes éliminé. Quel nombre donneriez-vous ?
slug: vous-jouez-a-un-concours-contre-100-personnes
date: '2020-01-07'
draft: true
categories:
- Quora
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Vous-jouez-%C3%A0-un-concours-contre-100-personnes-sachant-que-le-gagnant-est-celui-qui-donne-le-nombre-entier-le-plus-grand-inf%C3%A9rieur-%C3%A0-100-et-unique-Si-quelqu-un-d-autre-a-donn%C3%A9-le-m%C3%AAme/answer/Dr-Goulu)*

Il faut jouer 1.

D'après ce petit programme Python qui simule 10'000 parties où les 100 joueurs jouent au hasard :

```
from random import randint

N = 100
score = [0] * N
for game in range(10000):
    play = [0] * N
    for player in range(N):
        n = randint(1,N-1)
        if play[n]: # already played
            play[n]=-1
        else:
            play[n]=1
    win=play.index(1)
    score[win]=score[win]+1
    best=score.index(max(score))
    # print(win,score[win],best)
print(score)

```

on gagne dans (environ) 1/3 des cas en jouant 1 et (environ) 1/4 des cas en jouant 2, et au dessus de 20 on a aucune chance de gagner

[0, 3679, 2338, 1415, 948, 597, 391, 226, 149, 98, 56, 41, 25, 15, 7, 5, 4, 2, 0, 1, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

Suis sur qu'un matheux va trouver la distribution correspondante …

Evidemment, on peut se dire que les joueurs ne jouent pas au hasard, mais comme il y en a beaucoup et qu'ils vont se dire que le but est de ne pas choisir un nombre choisi par un autre joueur, ils vont en moyenne jouer au hasard quand même.

C'est quand ils vont comprendre qu'il vaut mieux jouer les petits nombres que ça va se compliquer….
