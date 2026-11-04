---
title: Comment calculer pi avec des collisions
date: 2026-11-02
draft: false
tags:
  - maths
  - mécanique
  - algorithme
  - simulation
  - pi
  - python
  - javascript
categories:
  - Comment
slug: ''
coverImage: ./images/collisions-pi-3d.gif
---

PFC m'a soumis cette vidéo pour le moins étonnante :

{{< youtube "HEfHFsfGXjs" >}}

Elle provient de l'excellente [chaîne YouTube](https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw) de maths du blog de maths [3Blue1Brown.com](https://www.3blue1brown.com)  connu [même sur Wikipedia](w:3Blue1Brown) et montre quelque chose de très surprenant :

Si on fait glisser un chariot de masse M=1 vers un autre chariot de masse m=1 immobile qu'il percute dans un choc parfaitement élastique (= sans perte d'énergie) , et que ce chariot rebondit contre un mur parfaitement élastique (deuxième choc), il revient vers le chariot de masse M et le re-percute (troisième choc).  

Mais si on augmente la masse du premier chariot à M=2, le petit chariot de masse m=1 va faire deux  aller-retours entre le chariot de masse M et le mur : 5 chocs. Avec un cube de masse $M=8$ poussant un cube unité $m=1$ (comme dans l'animation 3D d' entête générée par le [`notebook Jupyter`](/posts/2026/collisions_pi.ipynb) ci-dessous), on obtient 9 chocs. Et intuitivement, on sent bien qu'en augmentant M, on aura de plus en plus de chocs.

La suite OEIS [A331859](https://oeis.org/A331859) donne le nombre de chocs en fonction de M, mais ne va pas assez loin pour voir LE phénomène intéressant découvert par Galperin en 2003 [1]:

- avec M=100, on obtient 31 chocs
- avec M=10'000 on obtient 314 chocs
- avec M=1'000'000 on obtient 3141 chocs
- avec M=100'000'000 on obtient 31415 chocs

et sous vos yeux émerveillés vous voyez apparaître une à une les décimales de Pi : pour M=100^n vous obtenez le n-ième terme de [A011545](https://oeis.org/A011545) \* !!!

Incroyable, non ? Testez vous-même avec la simulation interactive ci-dessous :

{{< collisions_pi M="8" >}}}

## Mais POURQUOI ???

Comme vous j'imagine, je n'ai absolument pas vu de relation entre ce petit problème de mécanique idéalisée et le plus célèbre des nombres transcendants.

C'est l'IA qui me l'a indiquée dans le petite équation de la conservation de l'énergie cinétique $e_c$:

$$ M.V^2 + m.v^2 = 2.e_c $$

qui sent bon l'équation paramétrique d'un cercle ($x^2+y^2 = r^2$)

En posant $x=\sqrt{M}.V$, $y=\sqrt{m}.v$ et $r=\sqrt{2.e_c}$, on s'aperçoit que  l'état de notre système défini par les vitesses $(V,v)$ se déplace sur un cercle de la manière suivante :

{{< figure align="aligncenter" caption="(source : [2])" src="images/mathematics-08-00509-g004.png" >}}

À chaque fois que le petit bloc tape le mur, sa vitesse s'inverse (changement de signe), ce qui correspond graphiquement à une réflexion verticale dans notre repère. À chaque fois que les deux blocs se rentrent dedans, le point se déplace sur le cercle d'un angle $\theta$ tel que $\arctan{\theta} = \sqrt{m/M}$

Et le processus se poursuit jusqu'à ce que la vitesse v soit trop petite pour rattraper V, près de l'axe x négatif (point 9 sur le dessin)

le nombre de collisions correspond donc au nombre de fois où on peut répéter l'angle $\theta$ dans $\pi$, qui est comme chacun sait la "bonne" [mesure d'angle](/2010/01/16/histoire-dangles/) correspondant à 180° (en fait c'est [plutôt $\tau/2$ ](/2016/03/14/adieu-3-14-16-le-26-juin-ce-sera-tau-day/)mais bon...)

donc on a $$collisions \approx \theta/\pi$$

## Reste le $100^n$ ...

Quand $M >> m, \theta$ devient très petit et on peut approximer $tan (\theta) \approx \theta$

et notamment pour $$\theta \approx \sqrt{1/100^n} = 1/10^n$$

on a $$ collisions  \approx {\pi\over {1/10^n} } = 10^n\pi $$

Comme le résume bien l'IA :

> C'est cette approximation géométrique ultra-précise qui "force" la physique macroscopique à énumérer textuellement une à une les décimales du nombre $\pi$

### Note:

\* dans les commentaires de  [A011545](https://oeis.org/A011545), on trouve ceci :

> À proprement parler, cette propriété, qui équivaut à affirmer que l'intervalle (m\*π, π/arctan(1/m)) ne contient aucun entier pour tout m ≠ 10ⁿ, n'est pas avérée. Autrement dit, on ne sait pas avec certitude que A332045 ne contient pas une puissance de 10. Ce point est abordé dans la vidéo de 3Blue1Brown de 2025 intitulée « Why colliding blocks compute pi », qui fait suite à la vidéo de 2019.

### Références :

1. Galperin G. A., Playing pool with _π_ (the number _π_ from a billiard point of view), Regular and Chaotic Dynamics, 2003, Volume 8, Number 4, pp. 375-394 {{< altmetric doi="10.1070/RD2003v008n04ABEH000252" >}}
2. Aretxabaleta, X.M.; Gonchenko, M.; Harshman, N.L.; Jackson, S.G.; Olshanii, M.; Astrakharchik, G.E. The Dynamics of Digits: Calculating Pi with Galperin’s Billiards. _Mathematics_ **2020**, _8_, 509. {{< altmetric doi="10.3390/math8040509" >}}

### Notebook Jupyter:

{{< notebook src="posts/2026/collisions_pi.ipynb" title="Simulation 3D des collisions (collisions_pi.ipynb)" source_url="/posts/2026/collisions_pi.ipynb" download_label="Télécharger le notebook" show_code="false" >}}}
