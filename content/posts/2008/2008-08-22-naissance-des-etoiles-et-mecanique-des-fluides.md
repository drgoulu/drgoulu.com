---
title: "Naissance des étoiles et mécanique des fluides"
date: 2008-08-22
categories: 
  - "cat2"
  - "cat1"
tags: 
  - "astro"
  - "fluides"
  - "physique"
  - "simulation"
coverImage: "4f1be86001109ce9c5d5834c4b6bdfa2.gif"
---

[![](images/4f1be86001109ce9c5d5834c4b6bdfa2.gif)](http://drgoulu.local//HLIC/4f1be86001109ce9c5d5834c4b6bdfa2.gif)

Les méandres de la science et l'interconnexion des domaines me laissent souvent pantois. Hier soir par exemple, je m'intéressais à la simulation (qualitative) d'écoulement des fluides, [désormais possible en temps réel grâce à la puissance des cartes graphiques modernes](http://3dmon.wordpress.com/2008/08/21/fluides-en-temps-reel-aussi/).

La méthode utilisée ne se base pas sur l'intégration des [terribles équations de Navier Stokes](http://drgoulu.local/2007/04/14/les-problemes-mathematiques-difficiles/) ;  la "[Smoothed particle hydrodynamics](https://fr.wikipedia.org/wiki/Smoothed_particle_hydrodynamics)" (SPH) divise le fluide en sphères qui se déplacent et se modifient en fonction de leurs voisines les plus proches. Et ceci a visiblement donné une idée à [Matthew Bate](http://www.astro.ex.ac.uk/people/mbate/), chercheur en astrophysique à l'Université d'Exeter : la SPH ressemble drôlement à la résolution du [problème à N corps](https://fr.wikipedia.org/wiki/problème_à_N_corps), très utilisée pour simuler la trajectoire de nombreux corps célestes...

Mais en plus de simuler un amas d'étoiles qui se tournent autour, la SPH permet de représenter le gaz qu'elles dispersent dans l'espace en se frôlant, et qui en se re-condensant forme de nouvelles étoiles au sein de magnifiques nébuleuses:

{{< youtube id="GoQ08ONholQ" width="640" >}}

Matthew Bate a même simulé la formation d'un amas d'étoiles à partir d'un nuage de gaz initial presque homogène:

{{< youtube id="37b-sSyo0zE" width="640" >}}

Une telle simulation a tout de même nécessité plus de 1000h de calcul à 64 CPUs, donc ce n'est pas encore tout à fait du temps réel, mais [ça viendra.](http://3dmon.wordpress.com/2007/11/02/la-montee-en-puissance-des-gpus/)..
