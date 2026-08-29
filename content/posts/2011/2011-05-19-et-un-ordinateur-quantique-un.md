---
title: "Et un ordinateur quantique, un !"
slug: "et-un-ordinateur-quantique-un"
date: 2011-05-19
categories: 
  - "cat3"
  - "cat2"
  - "cat1"
tags: 
  - "feynman"
  - "informatique"
  - "quantique"
coverImage: "d_wave_one_system.jpg"
---

{{< figure src="images/d_wave_one_system.jpg" alt="Et en plus il a de la gueule. Enfin, autant qu'une boite noire éclairée par des LED bleues..." caption="Et en plus il a de la gueule. Enfin, autant qu'une boite noire éclairée par des LED bleues..." width="320" >}}

La vague idée de l'[ordinateur quantique](w:) est née dans les années 1970 à l'image d'une boutade de Richard Feynman:

> "Nature is not classic, dammit, and if you want to make a simulation of nature you'd better make it quantum mechanical and by golly it is a wonderful problem."

Ca paraissait être de la science-fiction pendant quelques décennies et voilà c'est fait : après quelques [premiers pas hésitants](w:Calculateur_quantique#La_controverse_D-Wave) et un partenariat avec Google, l'entreprise canadienne [D-Wave Systems](http://www.dwavesys.com/) [lance sur le marché](http://www.engadget.com/2011/05/18/d-wave-one-claims-mantle-of-first-commercial-quantum-computer/) le premier ordinateur quantique !

Le D-Wave One est doté d'un processeur à 128 [qubits](w:qubit) "[flux](w:en:flux_qubit)" baptisé "Rainier", spécialisé dans la résolution de problèmes d' [optimisation combinatoire](w:) discrète, une classe de problèmes "NP" (Non Polynomial), dont la résolution est très lente voire impossible sur un ordinateur classique.

"Rainier" n'a pas grand chose à voir avec la puce de nos PC : il utilise des [jonctions Josephson](w:jonction_Josephson) supraconductrices pour générer les qubits et exploite le [théorème adiabatique](w:) pour accéder à leur état. Les qubits effectuent ensuite l'optimisation par une méthode de "[recuit simulé quantique](w:)". Toutes ces notions sont bien éloignées du pain quotidien des informaticiens d'aujourd'hui.... D'ailleurs un ordinateur quantique ne se "programme" pas réellement, il doit plutôt être configuré pour résoudre un problème donné, un peu à la manière des bons vieux [calculateurs analogiques](w:calculateur_analogique).

{{< figure src="images/ordinateur-quantique-L-UAkw55.jpeg" alt="Vue de Rainier, le processeur du D-Wave One" caption="Vue de &quot;Rainier&quot;, le processeur du D-Wave One" align="aligncenter" width="393" >}}

Avec un prix catalogue de 10 millions de dollars, le D-Wave One s'adresse aux entreprises ayant un problème très particulier à résoudre. Tellement particulier qu'un ordinateur à 10 millions de dollars n'y parvient pas. J'aurais tendance à dire que le marché me semble limité, mais je m'en voudrais de répéter une erreur célèbre:

> "Je pense qu'il y a un marché mondial pour quelque chose comme 5 ordinateurs." (Thomas Watson, président d'IBM, 1943)

_(Edit du 28.9.2012 suite au commentaire de Manu : cette phrase n'est [probablement pas de Watson, ni de 1943](w:en:Thomas_J._Watson#Famous_misquote))_

### Références:

1. <span id="ref-1"></span>M. W. Johnson et al "[Quantum annealing with manufactured spins](http://www.nature.com/nature/journal/v473/n7346/full/nature10012.html)", 2011, Nature R. 473, pp 194–198
2. <span id="ref-2"></span>Newns & Tsuei, "[Quantum computing with d-wave superconductors](http://www.freepatentsonline.com/6495854.html)", 2002, United States Patent 6495854
3. <span id="ref-3"></span>"[Learning to program the D-Wave One](http://dwave.wordpress.com/2011/05/11/learning-to-program-the-d-wave-one/)" sur "[Hack the Multiverse](http://dwave.wordpress.com/)", le blog de D-Wave
4. <span id="ref-4"></span>"Catching quantum mechanics in the act…" sur "[Hack the Multiverse](http://dwave.wordpress.com/)", le blog de D-Wave
5. <span id="ref-5"></span>Hartmut Neven, "[Machine Learning with Quantum Algorithms](http://googleresearch.blogspot.com/2009/12/machine-learning-with-quantum.html)", 2009, Google Research Blog
6. <span id="ref-6"></span>page "[D-Wave Systems](w:)" sur Wikipedia
7. <span id="ref-7"></span>"[Discrete Optimization Methods](http://www.cs.sunysb.edu/~algorith/implement/syslo/implement.shtml)" sur The Stony Brook Algorithm Repository
