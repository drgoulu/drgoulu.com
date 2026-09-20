---
title: Comment est calculé le nombre Pi ?
slug: comment-est-calcule-le-nombre-pi
date: '2021-02-09'
draft: false
categories:
- Comment
tags:
- mathematiques
- pi
- circonference
- diametre
- formule-de-calcul
- geometrie-des-cercles
- le-nombre-pi
- constantes-mathematiques
- calcul-de-pi
- geometrie
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Comment-est-calcul%C3%A9-le-nombre-Pi/answer/Dr-Goulu)*

Il y a des centaines, des milliers de méthodes, voir [Pi — Wikipédia](w:Pi)

Pi n'est plus calculé dans les ordinateurs et calculatrices actuelles, il est mémorisé comme constante ( voir [Pi and e In Binary](https://www.exploringbinary.com/pi-and-e-in-binary/) pour les détails)

Mon algo préféré pour le calcul de pi est ce petit programme en C de 133 caractères

```
int a[52514],b,c=52514,d,e,f=1e4,g,h;main()
{for(;b=c-=14;h=printf("%04d",e+d/f)) for(e=d%=f;g=--b*2;d/=g)
d=d*b+f*(h?a[b]:f/5),a[b]=d%--g;}

```

qui produit [15000 décimales de Pi](/2004/06/28/pi-en-c/#.YCK6POhsOCo) en quelques millisecondes.

Les spécialistes remarqueront que tous les calculs se font sur des nombres entiers !!! et même de bons vieux int16 !

L’algorithme utilisé s’appelle “[Spigot](w:en:Spigot_algorithm)” et il est du à Rabinowitz and Wagon. La référence suivante explique son fonctionnement

1. Jeremy Gibbons “[Unbounded spigot algorithms for the digits of pi](http://www.cs.ox.ac.uk/jeremy.gibbons/publications/spigot.pdf)” (2006), The American Mathematical Monthly 4 (113) p. 318-328 DOI>[10.1007/978-3-319-32377-0_16](https://doi.org/10.1007/978-3-319-32377-0_16)
