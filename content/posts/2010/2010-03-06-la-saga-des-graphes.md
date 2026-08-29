---
title: "La  saga des graphes"
slug: "la-saga-des-graphes"
date: 2010-03-06
categories: 
  - "cat2"
tags: 
  - "casse-tetes"
  - "graphes"
  - "internet"
  - "jeux"
coverImage: "19aab911f31dc5631223df29f0afbdab.png"
---

Découvert grâce à Patric quelques [petits jeux intelligents](/2009/12/19/petits-jeux-intelligents/) de plus : la [saga des graphes de Neamar](http://neamar.fr/Res/Graphe/). 3 jeux en Flash attendent impatiemment vos neurones :

{{< figure src="images/19aab911f31dc5631223df29f0afbdab.png" alt="AGraphe" caption="AGraphe" link="http://neamar.fr/Res/AGraphe/" align="aligncenter" width="300" >}}

[AGraphe](http://neamar.fr/Res/AGraphe/) est le plus facile en apparence : il s'agit d'allumer le noeud supérieur du graphe, qui ne peut l'être que si tous ses noeuds enfants sont allumés. L'astuce est qu'on ne peut avoir plus de N noeuds allumés simultanément, donc qu'il faut aussi éteindre judicieusement les noeuds. Mais il reste facile.

{{< figure src="images/e046b6ff88906a9d4cf6e5fc404da844.png" alt="BGraphe" caption="BGraphe" link="http://neamar.fr/Res/BGraphe/" align="aligncenter" width="300" >}}

Dans [BGraphe](http://neamar.fr/Res/BGraphe/), il faut déplacer les noeuds de façon à ce que les arêtes ne se coupent pas. Une fois qu'on a compris le truc on passe quelques tableaux assez facilement, puis ça devient vraiment trop difficile.

{{< figure src="images/8ac3dd74a4432546fc1330bcb2b94b97.png" alt="CGraphe" caption="CGraphe" link="http://neamar.fr/Res/CGraphe/" align="aligncenter" width="300" >}}

[CGraphe](http://neamar.fr/Res/CGraphe/) est une implantation du "[Shannon Switching Game](w:en)" qui se joue à 2:

- le "Paintre" doit relier les deux noeuds marqués en rouge en allumant une arête à chaque tour
- le "Couhpeur" doit l'en empêcher en supprimant carrément une arête à chaque tour.

On joue alternativement chaque rôle, et l'ordinateur l'autre. Les premiers tableaux permettent de mettre au point la stratégie de chaque rôle, et les tableaux suivants sont là pour l'éprouver...

Sur chaque page, n'omettez pas de lire le texte en dessous de chaque jeu. On y apprend des choses intéressantes sur les graphes et sur le processus de développement de ces jeux très bien réalisés. On en trouve même le code source. Et Neamar y explique aussi comment fabriquer nos propres tableaux pour ses jeux en attendant le  DGraphe qu'il nous nous prépare.

En fouillant un peu, on trouve que ce Neamar fait plein d'[autres choses passionnantes et marrantes](http://neamar.fr/), dont un [blog](http://blog.neamar.fr/). Hop, un flux RSS de plus.
