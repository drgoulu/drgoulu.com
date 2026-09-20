---
title: Quelle est la proportion de nombres premiers parmi les nombres entiers de n chiffres quand n est grand ?
slug: quelle-est-la-proportion-de-nombres-premiers-parmi-les-nombres-entiers-de-n-chiffres-quand-n-est-grand
date: '2023-04-03'
draft: false
categories:
- Quora
tags:
- mathematiques
- proportion
- statistiques
- theorie-des-nombres-premiers
- probabilite-statistiques
- sciences-mathematiques
- theorie-du-nombre
- theorie-des-nombres
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Quelle-est-la-proportion-de-nombres-premiers-parmi-les-nombres-entiers-de-n-chiffres-quand-n-est-grand/answer/Dr-Goulu)*

D'après le [Théorème des nombres premiers](w:)la densité des nombres premiers autour de x est $\pi(x)/x \simeq 1/ln(x)$

pour x=10^n vous avez donc une densité d'environ $1/ln(10^n) = 1/n.ln(10) \simeq 2.30/n$

Ca peut donc surprendre, mais la densité diminue linéairement avec le nombre de chiffres

il n'y a que 10x plus de nombres premiers de 12 chiffres que de nombres premiers à 13 chiffres …Et il y en a beaucoup :

par exemple pour des nombres entiers de 512 bits, n=154 chiffres décimaux , la densité vaut 0.3% : 3 nombres de 154 chiffres sur 1000 sont premiers, et avec un test de primalité il est quasi instantané d'en trouver. Hop en v'là un : 95798693619967093628787644901385920724520224891681487012485117428228030029969

[https://www.drgoulu.com/2012/04/...](/2012/04/15/comment-produire-des-nombres-premiers/#.ZCsO9XaiGCo)
