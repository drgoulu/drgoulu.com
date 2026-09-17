---
title: Est-il vrai que la formule $p(n)=n^2+n+41+\sum_{k\geq 0}a_k\lfloor n/(40+6k)\rfloor$ donne uniquement des nombres premiers pour tout $n\geq 0$ et avec un choix approprié de la suite d’entiers naturels $\{a_k\}$, par exemple commençant par $\{a_k\}_{k\geq 0}=${8040, 0, 3900, 2730, 576, 7110, 300, 5394, 1020, 1080,…} ?
slug: est-il-vrai-que-la-formule-p-n-n-2-n-41-sum-k-geq-0-a-k-lfloor-n-40-6k-rfloor-donne-uniquement-des-nombres-premiers-pour-tout-n-geq-0-et-avec-un-choix-approprie-de-la-suite-dentiers
date: '2021-11-24'
draft: true
categories:
- Quora
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Est-il-vrai-que-la-formule-p-n-n-2n41sum-kgeq-0-a-klfloor-n-406k-rfloor-donne-uniquement-des-nombres-premiers-pour-tout-ngeq-0-et-avec-un-choix-appropri%C3%A9-de-la-suite-d-entiers-naturels-a-k/answer/Dr-Goulu)*

Oui, le tout est de choisir les $a_k$ pour que votre formule génère les nombres premiers …

J'ai une autre formule comme ça, beaucoup plus simple :

$p_{n+1} = 2 + \sum_{i=1}^n g_i$

avec g = [1, 2, 2, 4, 2, 4, 2, 4, 6, 2, 6, 4, 2, 4, 6, 6, 2, 6, 4, 2, 6, 4, 6, 8, 4, 2, 4, 2, 4, 14, …]
