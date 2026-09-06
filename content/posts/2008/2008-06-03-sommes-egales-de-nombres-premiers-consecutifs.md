---
title: "Sommes Egales de Nombres Premiers Consécutifs"
slug: "sommes-egales-de-nombres-premiers-consecutifs"
date: 2008-06-03
categories:
  - "Comment"
tags: 
  - "casse-tetes"
  - "google"
  - "maths"
  - "nombres-premiers"
  - "programmation"
coverImage: "0b7574cc4d97b1ba36b34b2b9797fc23.gif"
---

{{< figure src="images/389c66e7ddab342c9a24fd6e80fd3c65.jpg" >}}

Le quatrième et dernier problème de la [Google Treasure Hunt 2008](http://treasurehunt.appspot.com) mérite un article à lui tout seul. (J'ai parlé des trois autres dans [cet article et ses commentaires](/2008/05/17/recrutement-et-casse-tete/))

Il s'agit de trouver le plus petit [nombre premier](/2007/01/20/les-nombres-premiers/) P qui soit en même temps :

- la somme de 9 nombres premiers consécutifs
- la somme de 119 nombres premiers consécutifs
- la somme de 215 nombres premiers consécutifs
- et la somme de 675 nombres premiers consécutifs !

(les nombres 9, 119, 215 et 675 sont différents pour chaque concurrent...)

C'est étonnant, mais beaucoup de nombres premiers sont des sommes de nombres premiers consécutifs (abrégé SNPC ci après), par exemple :

5+7+11+13+17 = 53 7+11+13+17+19 =67 11+13+17+19+23 =83

De plus, il est fréquent qu'un même nombre premier soit égal à plusieurs SNPC. Par exemple sur [ce site](http://www.primepuzzles.net/puzzles/puzz_046.htm) on mentionne:

34421 = 269 + … + 709 (71 nombres premiers) 34421 = 1429 + … + 1571 (23 nombres premiers) 34421 = 3793 + … + 3853 (9 nombres premiers) 34421 = 4889 + … + 4937 (7 nombres premiers) 34421 = 11467 + … + 11483 (3 nombres premiers)

Le nombre P recherché n'est donc peut-être pas très grand, d'autant que la somme des 675 premiers nombres premiers ne vaut que 1'578'242. Il n'y a probablement pas besoin de calculer en "bigint", les entiers sur 32 bits, voire 64 disponibles avec n'importe quel langage de programmation devraient suffire. Par contre, il est pratique de disposer de fonctions prédéfinies pour manipuler des nombres premiers, c'est pourquoi j'ai choisi d'utiliser [Mathematica](w:).

Les fonctions suivantes suffisent pour résoudre le problème posé: _(code modifié le 4/6/8 suite aux commentaires de b0z0)_

{{< gist "" "0e35207dedf4e337c937" >}}

La fonction SCP (Sum of Consecutive Primes) renvoie la somme des n nombres premiers consécutifs en commençant par le i-ème nombre premier en utilisant la fonction prédéfinie Prime\[j\] qui renvoie directement le j-ème nombre premier.

Cette somme n'étant pas forcément un nombre premier, la fonction PSP (Prime Sum of Primes) appelle répétitivement SCP en augmentant i jusqu'à ce que la somme soit un nombre premier, vérifié grâce au test de primalité [PrimeQ](http://reference.wolfram.com/mathematica/ref/PrimeQ.html), une fonction non triviale bien utile ici. Pour une raison expliquée plus bas, PSP renvoie une paire de résultats : la somme, et l'indice du premier nombre premier de la somme.

Enfin, la fonction CPSP (Compound Prime Sum of Primes) implante l'algorithme que j'ai inventé pour la circonstance. Elle prend en paramêtre la liste des nombres de nombres premiers consécutifs sommés. Pour résoudre notre problème, on appellera  CPSP\[{675, 215, 119, 9}\]

1. on initialise une liste p avec les n résultats de PSP obtenus pour chacun des nombres de nombres premiers consécutifs à additioner. Ainsi, pour CPSP\[{675, 215, 119, 9}\], p est initialisé à {{1583291,2},{149993,15},{41641,10},{127,2}}. Autrement dit, 1583291 est le plus petit nombre premier qui soit la somme de 675 nombres premiers consécutifs, et cette somme commence avec le 2ème nombre premier. 149993 est le plus petit nombre premier qui soit la somme de 215 nombres premiers, en commençant par le 15ème, et ainsi de suite
2. par paresse (qualité indispensable chez les programmeurs...) , la détection de la fin de l'algorithme est réduite au minimum vital : dès que la liste p n'est plus modifiée par l'algorithme, on arrête
3. Pour chaque élément de la liste p en commençant par le deuxième, on regarde si la somme est inférieure à la somme du premier indice. Si c'est le cas, on calcule une somme supérieure en incrémentant l'indice correspondant, jusqu'à ce que la somme soit égale à la première, ou la dépasse. Après cette étape, la liste p devient {{1583291,10},{1600981,840},{1589563,1526},{1584829,15997}} : on voit que les sommes 2,3 et 4 ont dépassé la somme 1
4. Si la somme 1 est plus petite que la somme 2, on augmente la somme 1 jusqu'à ce que'elle atteigne ou dépasse la somme 2. On arrive ainsi à {{1623917,10},{1600981,840},{1589563,1526},{1584829,15997}}. On boucle au point 2

Les trois dernières boucles donnent les listes suivantes qui montrent bien le fonctionnement de l'algorithme:

{{8256361,1127},{8112103,3883},{8115539,6728},{8112787,71376}} {{8275409,1130},{8259353,3947},{8264171,6833},{8256383,72536}} {{8275409,1130},{8275409,3954},{8275409,6841},{8275409,72696}}

et voilà : 8'275'409 est égale à la somme des:

- 675 nombres premiers consécutifs à partir du 1130-ème (9109)
- 215 nombres premiers consécutifs à partir du 3954-ème (37339)
- 119 nombres premiers consécutifs à partir du 6841-ème (68821)
- 9 nombres premiers consécutifs à partir du 72696-ème (919421)

Quelques minutes pour choisir le bon outil (Mathematica) + quelques minutes de programmation + 30 secondes de calcul, c'est gagné !
