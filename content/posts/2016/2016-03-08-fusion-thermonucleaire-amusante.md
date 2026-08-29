---
title: "Fusion thermonucléaire amusante"
slug: "fusion-thermonucleaire-amusante"
date: 2016-03-08
categories: 
  - "cat2"
tags: 
  - "fusion"
  - "jeux"
  - "physique"
coverImage: "2016-03-08_203842.png"
---

{{< figure src="images/2016-03-08_203842.png" alt="2016-03-08_203842" caption="cliquez pour jouer en ligne !" link="http://dimit.me/Fe26/" align="alignleft" width="360" >}}

Grâce à [cet article sur la fusion](http://www.internetactu.net/2016/03/08/contre-leffondrement-67-quel-avenir-pour-la-fusion-nucleaire/), je viens de découvrir une variante addictive et nucléaire du fameux [jeu 2048](/2014/04/09/bits-en-vrac/) à la mode il y a deux ans : [Fe\[26\]](http://dimit.me/Fe26/).

Ce jeu permet de se familiariser avec la [nucléosynthèse stellaire](w:) : il s'agit de provoquer la [fusion nucléaire](w:) d'atomes de plus en plus lourds à partir de l'Hydrogène, jusqu'à fabriquer un atome de [Fer](w:)

![digraph G { size="4,10"; ratio = fill; node \[shape=box, style=filled, color="#f2b280"\]; H->D; H->D; H->He3; D->He3; He3->He4; He3->He4; He4->Be7; He3->Be7; He4->Be8; He4->Be8; Be8->C12; He4->C12; C12->O16; He4->O16; O16->Ne20; He4->Ne20; C12->Ne20; C12->Ne20; Ne20->Ma24; He4->Ma24; O16->Si28; O16->Si28; Si28->S32; He4->S32; S32->Ar36; He4->Ar36; Ar36->Ca40; He4->Ca40; Ca40->Ti44; He4->Ti44; Ti44->Cr48; He4->Cr48; Cr48->Fe52; He4->Fe52; Fe52->Ni56; He4->Ni56; Be7->He4; Be8->He4; Ne20->O16; Fe52->Cr48; Ni56->Fe56; }](images/2016-03-08_193933.png)

Malgré les apparences, le jeu est très différent du "2048". Pour commencer, on n'additionne pas les atomes comme des puissances de deux.

Les règles de fusion des atomes sont représentées dans le graphe ci-contre (fait avec [webgraphviz](http://www.webgraphviz.com) ) . Comme on le voit, le 4Helium (He4) est un ingrédient indispensable: il faut en produire autant que possible. A l'inverse, le 24Magnesium est un piège à éviter car une fois synthétisé, on ne peut rien en faire.

Ensuite, certains atomes sont instables et se transmutent en d'autres au bout d'un nombre de coups indiqué dans une pastille verte. Il faut donc se dépêcher de combiner du Be8 avec un He4 pour produire du C12 avant que le Be8 ne se désintègre en He4. Et si on produit du Be7 par erreur, il n'y a plus qu'à attendre qu'il fasse de même. Idem pour le Ne20 qui finira par produire du très utile O16, mais il faut veiller à ce qu'il ne rencontre pas un He4 pendant sa "demi-vie" sous peine de tomber dans le piège du magnésium. Enfin, une fois le Fe52 produit il faut très vite lui ajouter un He4 pour produire du Ni56 sans quoi on retombe au Cr48. Et une fois le Ni56 synthétisé, il faut encore être capable de jouer quelques coups en attendant qu'il transmute en Fe56 victorieux.

Comme le disent les auteurs [Dimitar Dimitrov](http://dimit.me/) et [Kevin O'Connor](http://kevo.io/) cette nucléosynthèse est simplifiée pour rendre le jeu jouable (mais difficile), mais correspond le mieux possible aux processus de fusion actifs dans les vieilles étoiles.

Je trouve très intéressante cette combinaison d'une interface utilisateur ultra-simple avec un processus physique pas intuitif du tout. Le résultat est vraiment prenant (je n'ai pas encore gagné ...) Je ne sais pas si les joueurs apprennent véritablement quelque chose sur la nucléosynthèse, mais peut-être que ce jeu peut générer de l'intérêt pour ce mécanisme fondamental de l'Univers.

Accessoirement je vais regarder [le code](https://github.com/Newbrict/Fe26) de plus près, car j'ai toujours en réserve l'idée d'un jeu sur la [transmutation du plomb en or](/2013/03/15/comment-transformer-le-plomb-en-or/) qui pourrait s'inspirer de Fe\[26\]. S'il y a un programmeur JavaScript intéressé à collaborer dans la salle...
