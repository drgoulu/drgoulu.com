---
title: Soit (2^q) *(3^p) <= n, determiner p et q. C'est impossible à faire non ?
slug: soit-2-q-3-p-n-determiner-p-et-q-c-est-impossible-a-faire-non
date: '2021-03-02'
draft: false
categories:
- Quora
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Soit-2-q-3-p-n-determiner-p-et-q-C-est-impossible-%C3%A0-faire-non/answer/Dr-Goulu)*

on passe en [logs](w:Logarithme):

ln(2^q)+ln(3^q) <= ln(n)

q*ln(2)+p*ln(3) <= ln(n)

vous avez une équation du type a.x+b.y <= c

les solutions sont donc tous les points (x,y) situées sous la droite y=(c-a.x)/b

donc dans notre cas (x=q et y=p), tous les (p,q) tels que p<=(ln(n)-ln(2)*q)/ln(3)

par exemple pour n=1 tous les (p,q) tels que p<= - q*ln(3)/ln(2)

vérifions : si je prends q=10 et p=-16, j'ai bien

2^10*3^(-16) < 1

si vous cherchez des (p,q) positifs, vous devez prendre un n>1, par exemple pour n=10 vous avez p<= ln(10) - q*ln(3)/ln(2)

et par exemple pour q=1, je dois avoir p<ln(10) - ln(3)/ln(2)

donc p< 0.71762259227

test : 2^1 * 3^0.71762259227 = 4.4, qui est bien < 10
