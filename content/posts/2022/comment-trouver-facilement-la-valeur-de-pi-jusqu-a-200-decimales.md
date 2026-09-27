---
title: Comment trouver facilement la valeur de pi jusqu'à 200 décimales ?
slug: comment-trouver-facilement-la-valeur-de-pi-jusqu-a-200-decimales
date: '2022-03-26'
draft: false
categories:
- Comment
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Comment-trouver-facilement-la-valeur-de-pi-jusqu-%C3%A0-200-d%C3%A9cimales/answer/Dr-Goulu)*

Ce minuscule programme en C calcule [15'000 décimales de pi](/2004/06/28/pi-en-c/)en une fraction de seconde:

```
int a[52514],b,c=52514,d,e,f=1e4,g,h;main()
{for(;b=c-=14;h=printf("%04d",e+d/f)) for(e=d%=f;g=--b*2;d/=g)
d=d*b+f*(h?a[b]:f/5),a[b]=d%--g;}

```

Si vous connaissez un tout petit peu C, vous remarquerez que ce programme n'utilise que des nombres entiers ! N'est-ce pas incroyable de pouvoir calculer les décimales d'un nombre non seulement irrationnel, mais transcendant en ne manipulant que de petits nombres entiers.

L’algorithme utilisé s’appelle “[spigot](http://www.wikipedia.org/search-redirect.php?language=en&go=Go&search=Spigot_algorithm)” et il est du à Rabinowitz and Wagon. La référence suivante explique son fonctionnement

Jeremy Gibbons “[Unbounded spigot algorithms for the digits of pi](http://www.cs.ox.ac.uk/jeremy.gibbons/publications/spigot.pdf)” (2006), The American Mathematical Monthly 4 (113) p. 318-328 DOI>[10.1007/978-3-319-32377-0_16](https://doi.org/10.1007/978-3-319-32377-0_16)
