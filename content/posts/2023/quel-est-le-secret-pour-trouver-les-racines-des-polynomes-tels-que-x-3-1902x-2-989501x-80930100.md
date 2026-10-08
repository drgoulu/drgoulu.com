---
title: Quel est le secret pour trouver les racines des polynômes tels que $x^3-1902x^2+989501x-80930100$ ?
slug: quel-est-le-secret-pour-trouver-les-racines-des-polynomes-tels-que-x-3-1902x-2-989501x-80930100
date: '2023-04-14'
draft: true
categories:
- Quora
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Quel-est-le-secret-pour-trouver-les-racines-des-polyn%C3%B4mes-tels-que-x-3-1902x-2989501x-80930100/answer/Dr-Goulu)*

On essaie de mettre ça sous la forme $(x-a)(x-b)(x-c)=0$

en développant $x^3 - (a+b+c)x^2 + (ab+ac+bc)x -abc=0$

donc ici on cherche les 3 nombres a,b,c tels que :

$a+b+c=1902$

$abc=80930100$

$ab+ac+bc = 989501$

et en farfouillant un peu on trouve $a=100, b=851, c=951$

Mais le plus simple, c'est de [demander à Wolfram|Alpha](https://web.archive.org/web/20230414/https://www.wolframalpha.com/input?i=x3−1902x2+989501x−80930100=0)
