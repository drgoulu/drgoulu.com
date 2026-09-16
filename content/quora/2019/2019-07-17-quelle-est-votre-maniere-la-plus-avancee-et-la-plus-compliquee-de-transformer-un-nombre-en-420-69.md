---
title: Quelle est votre manière la plus avancée et la plus compliquée de transformer un nombre en 420.69?
slug: quelle-est-votre-maniere-la-plus-avancee-et-la-plus-compliquee-de-transformer-un-nombre-en-420-69
date: '2019-07-17'
draft: false
categories:
- Quora
tags:
- mathematiques
- culture-internet
- nombres-decimaux
- problemes-mathematiques
- nombres-mathematiques
- calcul-mathematique
- solutions-mathematiques
- enigmes-mathematiques
- questions-de-mathematiques
- chiffres-decimaux
coverImage: ./images/qimg-d65fba6ef779404f4a4eafda7397d6f2.gif
---

*Article initialement publié sur [Quora](https://fr.quora.com/Quelle-est-votre-mani%C3%A8re-la-plus-avanc%C3%A9e-et-la-plus-compliqu%C3%A9e-de-transformer-un-nombre-en-420-69/answer/Dr-Goulu)*

- utiliser le génial "[inverseur de Plouffe](http://wayback.cecm.sfu.ca/cgi-bin/isc/lookup?number=420.69&lookup_type=simple)" pour trouver la formule la plus compliquée pour un nombre ayant les décimales entre 420685 et 420695 .
- Il y a sum(1/(17/6*n^3-33/2*n^2+107/3*n-13)*C(3*n,n)),n=1..inf) qui me plait bien… dans [Wolfram|Alpha](https://www.wolframalpha.com/input/?i=sum(1/(17/6*n^3-33/2*n^2+107/3*n-13)/C(3*n,n)),n=1..inf) ça donne :

![](./images/qimg-d65fba6ef779404f4a4eafda7397d6f2.gif)

- on voit qu'il faut multiplier par 10'000 pour obtenir la valeur cherchée

![](./images/qimg-bb7215145cb958075bab10a5358acdc6.gif)

- pour que la valeur soit exactement égale à 420.69, il faudrait prendre la valeur entière supérieure à 100x cette formule, et diviser l'entier ainsi obtenu par 100, je vous laisse ça en exercice …

Pour ceux qui ne connaissent pas C(3n, n), c'est la [Formule du binôme](w:Formule_du_binôme_de_Newton), qu'on pourrait évidemment aussi développer en factorielles pour compliquer encore la formule …
