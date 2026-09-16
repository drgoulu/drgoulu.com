---
title: Le nombre Pi est-il le fruit du hasard ?
slug: le-nombre-pi-est-il-le-fruit-du-hasard
date: '2019-06-24'
draft: false
categories:
- Quora
tags:
- mathematiques
- hasard
- pi
- nombre
- theorie-des-nombres
- geometrie
- philosophie-des-mathematiques
- sciences-mathematiques
- geometrie-des-cercles
coverImage: ./images/quora.png
---

*Article initialement publié sur [Quora](https://fr.quora.com/Le-nombre-Pi-est-il-le-fruit-du-hasard/answer/Dr-Goulu)*

Absolument pas.

$\pi$ est aussi bien défini et déterminé que $2\sqrt{2}$ qui est le rapport du périmètre d'un carré par sa diagonale, et qui a aussi un développement décimal infini.

Une "preuve" est qu'on peut écrire un petit programme de 133 caractères en C:

```
int a[52514],b,c=52514,d,e,f=1e4,g,h;main()
{for(;b=c-=14;h=printf("%04d",e+d/f)) for(e=d%=f;g=--b*2;d/=g)
d=d*b+f*(h?a[b]:f/5),a[b]=d%--g;}

```

qui génère 15'000 décimales de pi*. Ca signifie qu'on peut "comprimer" pi d'un facteur 112 (au moins) alors qu'on ne peut pas comprimer une séquence aléatoire de chiffres.

note* : en n'utilisant que des nombres entiers ! voir [http://www.cs.ox.ac.uk/jeremy.gi...](http://www.cs.ox.ac.uk/jeremy.gibbons/publications/spigot.pdf)
