---
title: "Solutions admissibles"
slug: "solutions-admissibles"
date: 2016-09-11
categories:
  - "Pourquoi"
tags: 
  - "maths"
  - "physique"
coverImage: "./images/Une-voiture-dans-le-decor-pas-de-blesse_reference.jpg"
---

Chaque fois que je tombe sur des théories physiques un peu exotiques comme la [Métrique d'Alcubierre](w:Métrique_d_Alcubierre), le [Big Bounce](w:) ou les [trous de ver](w:trou_de_ver), je repense à une anecdote survenue lors d'un examen de physique au [Collège Lycée de l'Abbaye de St-Maurice.](w:Lycée-collège_de_l_Abbaye_de_Saint-Maurice).

{{< figure src="./images/Une-voiture-dans-le-decor-pas-de-blesse_reference.jpg" alt="Mathématiquement, il suffit d'attendre un moment ..." caption="Mathématiquement, il suffit d'attendre un moment ..." width="480" >}}

Contrairement à [Zinzin](/2008/08/24/nombres-acratopeges/), le très divertissant prof de maths, notre prof de physique était, en première approximation, un affreux cynique antipathique assénant des notes impitoyables à des élèves terrifiés. Le problème qu'il nous avait énoncé de sa voix nasillarde\* ce jour là était de ce genre:

> Un conducteur roule à 72 km/h lorsqu'il aperçoit un gros rocher sur la route devant lui. Après un temps de réaction, il écrase le frein quand sa voiture de 1000 kg n'est plus qu'à 10 m de l'obstacle. La force de freinage est de 10000 [Newton](w:Newton_(unité)). Déterminez si sa voiture heurte le rocher, et si oui après combien de temps et à quelle vitesse.

Fââcile : [F=m.a](/2013/12/15/comment-expliquer-la-relativite-aux-enfants/#.V8CO1CiLSpc), donc a=F/m, la voiture ralentit pile à a=10 m/s². La vitesse initiale de 72 km/h correspond à v0\=20 m/s. La position de la voiture en fonction du temps s'écrit p(t)=v0.t-a.t²/2 qu'on résout pour  p(t)=10 m  , ce qui donne l'équation du second degré: -5t²+20t-10 = 0

Comme le discriminant b²-4ac vaut 400-4.5.10 = 200 est positif, il existe des solutions donc la bagnole tape bien dans le caillou après t=2±√2 secondes, Et pour la vitesse on a v(t)=v0\-a.t ce qui donne la vitesse au moment où la voiture heurte l'obstacle : v=±10√2 m/s, soit ±51 km/h environ.

Tous ceux qui ont donné ce résultat ont eu zéro. Et une bordée du prof en prime, dont je me rappelle quasiment chaque mot 35 ans plus tard:

> Alors comme ça bande de [peigne-cul](https://fr.wiktionary.org/wiki/peigne-cul)\*\*, vous croyez aveuglément une équation qui donne des solutions débiles ? Vous croyez que la bagnole va traverser le rocher, s'arrêter après [deux secondes](https://web.archive.org/web/20211206134607/https://www.wolframalpha.com/input/?i=solve+-5t%5E2%2B20t-10%3D0) et reculer sous l'effet des freins pour se fracasser une deuxième fois en marche arrière ? On est pas au cours de maths ici ! En physique un problème a des **solutions admissibles\*\*\***, mais aussi des solutions inadmissibles. C'est la Nature qui dit si une solution de maths est admissible ou pas. Si vous pigez pas ça, vous êtes nuls : zéro !

Dur. Mais juste. Avec le recul, la leçon était très importante.

L'[équation d Einstein](w:) (pas E=mc², l'autre, celle de la [relativité générale](w:)) est un chef d'oeuvre. Albert a généralisé la [loi universelle de la gravitation](w:) de Newton en décrivant comment l'énergie et la matière déforment l'espace et le temps. Le problème est que l'équation d'Einstein admet de nombreuses solutions qu'on peut classer ainsi:

1. celles qui correspondent aux observations : le [Big Bang](w:), l'[expansion de l'Univers](w:), la précession du périhélie de Mercure, les [trous noirs](/tags/trou-noir/), le décalage des horloges atomiques situées à des altitudes différentes ou en mouvement l'une par rapport à l'autre, et encore tout récemment les [ondes gravitationnelles](w:).
2. celles qui ne sont carrément pas compatibles avec notre Univers. La plus fameuse "solution inadmissible" est due à Einstein lui-même : lorsqu'[Alexandre Friedman](w:) s'est aperçu que l'équation d'Einstein décrivait un univers en expansion (ou en contraction), Albert a ajusté la [constante cosmologique](w:) de son équation pour forcer l'Univers à être statique. Lorsque [Edwin Hubble](w:) montra que l'Univers était bel et bien en expansion, Einstein dit qu'il avait fait la  plus grosse gaffe ("blunder" en anglais) de sa vie. D'autres solutions mathématiquement correctes de l'équation d'Einstein sont très surprenantes, comme l'[Univers de Gödel](w:) dans lequel le voyage temporel est non seulement possible, mais inévitable [[1]](#ref-1).
3. Les fameuses théories "exotiques" ([Métrique d'Alcubierre](w:Métrique_d_Alcubierre), [trous de ver](w:trou_de_ver) etc.) dont on ne sait pas encore si elles sont "admissibles" ou non. Mais ces solutions mathématiques font apparaître des choses étranges comme de l'[énergie négative](w:) et/ou de la [masse négative](w:) dont on  pas vu le début du commencement d'une apparence d'existence. Bon, il y a bien l'[effet Casimir](w:) mais il revient un peu à jouer un peu sur les notions de [vide](w:vide_quantique) et de [zéro absolu](w:).

C'est pourquoi je reste très sceptique face à ces admirables et très respectables solutions mathématiques de physique théorique. Mon indécrottable [empirisme](w:) exige de voir dans cet univers un petit quelque chose de concret qui supporte l'idée qu'une voiture puisse éviter un rocher en passant par un trou de ver, ou qu'une voiture de masse négative puisse accélérer en marche arrière si on appuie sur le frein...

### Notes:

\*j'avais écris "nazillarde"... Toujours est-il qu'il nous avait donné un jour un problème consistant à calculer la force avec laquelle le nez d'un alpiniste se fracassait contre le rocher après une chute d'un surplomb avec une corde d'une élasticité donnée. Lorsque le résultat (quelques [tonnes-force](w:)) avait été trouvé, il avait conclu "Ouais. Je suis solide hein ?" Il nous avait donné [son accident de montagne](/wp-content/uploads/2016/08/ESM095040.pdf) comme exercice...

\*\* son insulte favorite, suffisamment pédante pour être tolérée dans un collège catholique de l'époque...

\*\*\* l'expression n'est pas courante en physique, mais très habituelle en [optimisation](w:Optimisation_(mathématiques)), ou une "solution admissible" n'est pas optimale, mais satisfait les contraintes du problème. En physique, on pourrait appeler "solution admissible" une solution qui satisfait les contraintes de l'observation expérimentale (la voiture ne peut pas traverser le rocher), même si on y [approxime ou néglige](/2008/05/28/lingenieur-est-un-type-qui-sait-ce-quil-peut-negliger/) beaucoup de phénomènes (frottement de l'air, variation de la force de freinage). On peut ensuite "optimiser" la solution en y incorporant ces phénomènes au besoin.

\*\*\*\* Finalement, la gaffe n'est peut-être pas si monumentale que ça vu que l'[accélération de l'expansion de l'Univers](w:) due à la mystérieuse [énergie sombre](w:) pourrait correspondre à une valeur précise de la [constante cosmologique](w:).

### Références

1. <span id="ref-1"></span>M Buser, E Kajari and W P Schleich "Visualization of the Gödel universe'", 2013 New J. Phys. 15 013063){{< altmetric doi="10.1088/1367-2630/15/1/013063" >}} ([video abstract](https://www.youtube.com/watch?v=078jOiaevAQ))
