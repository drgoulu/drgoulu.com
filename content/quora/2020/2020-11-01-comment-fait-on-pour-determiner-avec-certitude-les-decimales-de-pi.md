---
title: Comment fait-on pour déterminer avec certitude les décimales de pi?
slug: comment-fait-on-pour-determiner-avec-certitude-les-decimales-de-pi
date: '2020-11-01'
draft: false
categories:
- Comment
tags:
- mathematiques
- nombres
- pi
- decimales
- calcul
- representation-decimale-de-pi
- geometrie-des-cercles
- nombres-irrationnels
- le-nombre-pi
- calcul-mathematique
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Comment-fait-on-pour-d%C3%A9terminer-avec-certitude-les-d%C3%A9cimales-de-pi/answer/Dr-Goulu)*

"déterminer avec certitude" est un pléonasme en mathématiques.

Il existe une quantité d'algorithmes fournissant les décimales de pi (voir [Approximation de π](w:)paragraphe algorithmes modernes")

Mon préféré est “[spigot](http://www.wikipedia.org/search-redirect.php?language=en&go=Go&search=Spigot_algorithm)”. Il s'écrit en 133 caractères de C et fournit (hyper rapidement) 15000 décimales de pi:

```
int a[52514],b,c=52514,d,e,f=1e4,g,h;main()
{for(;b=c-=14;h=printf("%04d",e+d/f)) for(e=d%=f;g=--b*2;d/=g)
d=d*b+f*(h?a[b]:f/5),a[b]=d%--g;}

```

Si vous le regardez de près, vous remarquerez qu'il n'utilise que des variables entières et des calculs sur des entiers ! Il écrit les décimales une à une !

Jeremy Gibbons “[Unbounded spigot algorithms for the digits of pi](http://www.cs.ox.ac.uk/jeremy.gibbons/publications/spigot.pdf)” (2006), The American Mathematical Monthly 4 (113) p. 318-328 DOI>[10.1007/978-3-319-32377-0_16](https://doi.org/10.1007/978-3-319-32377-0_16)
