---
title: Comment justifier qu'il existe une liste de 100 entiers consécutifs (qu'on précisera) contenant exactement 5 nombres premiers ?
slug: comment-justifier-qu-il-existe-une-liste-de-100-entiers-consecutifs-qu-on-precisera-contenant-exactement-5-nombres-premiers
date: '2025-08-10'
draft: true
categories:
- Comment
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Comment-justifier-qu-il-existe-une-liste-de-100-entiers-cons%C3%A9cutifs-qu-on-pr%C3%A9cisera-contenant-exactement-5-nombres-premiers/answer/Dr-Goulu)*

D'après le [Théorème des nombres premiers](w:), il existe environ x/ln(x) nombres premiers inférieurs à x, donc environ x/ln(x)-(x-n)/ln(x-n) nombres premiers compris entre x-n et x

Selon

[Solve x/ln(x)-(x-100)/ln(x-100)=5 - Wolfram|Alpha](https://www.wolframalpha.com/input?i=Solve+x/ln(x)-(x-100)/ln(x-100)=5) ça se produit vers x=168808000, mais je n'ai pas de Python sous la main pour trouver la valeur exacte.
