---
title: Qu'est-ce qu'un algorithme utile pour générer des décimales de π?
slug: qu-est-ce-qu-un-algorithme-utile-pour-generer-des-decimales-de
date: '2019-04-14'
draft: false
categories:
- Quora
tags:
- informatique
- pi
- mathematiques
- representation-decimale-de-pi
- algorithmes
- analyse-numerique
- nombres-mathematiques
- sciences-informatiques
- calcul-de-pi
- algorithmes-numeriques
coverImage: ./images/quora.png
---

*Article initialement publié sur [Quora](https://fr.quora.com/Quest-ce-quun-algorithme-utile-pour-g%C3%A9n%C3%A9rer-des-d%C3%A9cimales-de-%CF%80/answer/Dr-Goulu)*

le plus incroyable est le “spigot”, en 133 caractères de C :

```
int a[52514],b,c=52514,d,e,f=1e4,g,h;main()
{for(;b=c-=14;h=printf("%04d",e+d/f)) for(e=d%=f;g=--b*2;d/=g)
d=d*b+f*(h?a[b]:f/5),a[b]=d%--g;}

```

il génère 15000 décimales correctes de pi, et si vous le regardez bien vous verrez qu’il ne travaille qu’avec des nombres entiers !

description et explication ici :

Jeremy Gibbons “[Unbounded spigot algorithms for the digits of pi](http://www.cs.ox.ac.uk/jeremy.gibbons/publications/spigot.pdf)” (2006), The American Mathematical Monthly 4 (113) p. 318-328 DOI>[10.1007/978-3-319-32377-0_16](https://doi.org/10.1007/978-3-319-32377-0_16)
