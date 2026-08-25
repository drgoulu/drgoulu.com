---
title: "Pourquoi une loupe ne viole pas la thermodynamique"
slug: "pourquoi-une-loupe-ne-viole-pas-la-thermodynamique"
date: 2013-02-03
categories: 
  - "cat1"
tags: 
  - "energie"
  - "physique"
  - "soleil"
coverImage: "5e444ce2c6a868f184599d09d78b91c7.jpg"
---

_Petit article vite fait : je me contente de traduire un [article paru sur Ask a Physicist](http://www.askamathematician.com/2013/01/qhow-do-lenses-that-concentrate-light-not-violate-the-second-law-of-thermodynamics-if-you-use-a-magnifying-glass-to-burn-ants-arent-you-making-a-point-hotter-than-the-ambient-temperature-without/) qui répond à une question simple, pertinente et plus intéressante qu'il n'y parait :_

#### Pourquoi les lentilles qui concentrent la lumière ne violent pas le second principe de la thermodynamique ? En utilisant une loupe pour brûler des fourmis, ne rendez-vous pas un point plus chaud que la température ambiante sans dépenser d'énergie ?

Il est absolument impossible de créer de l'énergie, mais rien n'empêche de transférer de l'énergie d'un endroit à un autre, par exemple avec un tuyau allant de votre chauffe-eau à votre douche.  Dans le cas de la lumière solaire et de la lentille, il faut juste traiter ce transfert d'énergie d'une manière un peu plus abstraite.

Focaliser la lumière du Soleil ne fait pas diminuer l'[entropie](https://fr.wikipedia.org/wiki/Entropie_(thermodynamique)) car ce que fait la lentille, très grossièrement, est d'échanger de l' "information de direction" contre de l "information de position" : la lumière provenant d'une direction (celle du Soleil) est amenée à une position (le foyer de la lentille).

{{< figure src="images/921ad8de5752087fdb541982cfe602bb.jpg" alt="Parallel light" caption="La lumière parfaitement parallèle peut être focalisée en un point, mais la lumière d'une direction différente est focalisée en un autre point. La lumière provenant de différentes directions ne peut pas être focalisée en un seul point." link="http://www.askamathematician.com/2013/01/qhow-do-lenses-that-concentrate-light-not-violate-the-second-law-of-thermodynamics-if-you-use-a-magnifying-glass-to-burn-ants-arent-you-making-a-point-hotter-than-the-ambient-temperature-without/foci/" align="aligncenter" width="324" >}}

Donc, si la lumière provenant du Soleil n'était pas si parallèle, on ne pourrait pas utiliser une loupe pour la concentrer si bien. C'est pourquoi, un jour nuageux, vous ne pouvez pas brûler des fourmis même si le temps est assez clair. L'énergie est là, mais dispersée.

C'est un peu surprenant mais focaliser des rayons parallèles en un point ne change pas l'entropie de la lumière, et il y a un joli moyen de montrer ceci. Une bonne règle empirique au sujet de l'entropie est "si vous pouvez inverser le processus, l'entropie est constante". Or ici, vous pouvez si vous le souhaitez ajouter une seconde lentille pour "reparalléliser" la lumière:

{{< figure src="images/c8bfdb37df22df1606a767889a33d980.jpg" alt="The act of focusing light is reversible, so it doesn't increase entropy." caption="Focaliser la lumière peut être inversé, comme ici, donc ça n'augmente pas l'entropie." link="http://www.askamathematician.com/2013/01/qhow-do-lenses-that-concentrate-light-not-violate-the-second-law-of-thermodynamics-if-you-use-a-magnifying-glass-to-burn-ants-arent-you-making-a-point-hotter-than-the-ambient-temperature-without/reversible/" align="aligncenter" width="460" >}}

On pourait penser qu'avec des miroirs, des lentilles et des fibres optiques il devrait y avoir moyen d'amener plein de rayons de lumière en un seul point  pour le rendre aussi chaud qu'on veut. Mais non. C'est encore un exemple d'odieux [théorème no-go](https://fr.wikipedia.org/wiki/théorème_no-go) de l'univers.

Il y a une loi générale de la thermodynamique qui dit qu'on ne peut jamais focaliser de l'énergie de manière à ce que la cible devienne plus chaude que la source.  Donc vous pouvez utiliser tous les miroirs et lentilles que vous voulez, vous n'arriverez jamais à focaliser la lumière solaire pour qu'elle dépasse 5800K, la température à la surface du Soleil, mais vous pouvez vous en approcher pas mal. [En pratique](https://fr.wikipedia.org/wiki/Centrale_solaire_PS10) ce n'est cependant pas très utile car les machines ont tendance à fondre à de telles températures.

{{< figure src="images/5e444ce2c6a868f184599d09d78b91c7.jpg" alt="Si vous étiez au point lumineux, vous verriez une image agrandie du Soleil à travers la loupe. (Photo CC-BY Walter J. Pilsak )" caption="Si vous étiez au point lumineux, vous verriez une image agrandie du Soleil à travers la loupe. (Photo CC-BY Walter J. Pilsak )" link="http://commons.wikimedia.org/wiki/File:Brennglas.jpg" align="aligncenter" width="400" >}}

Une bonne façon de se représenter ceci est de vous imaginer vous promener à la surface du Soleil, puis de vous imaginer au foyer de la lentille. En étant dans les couches externes du Soleil, vous auriez tout autour de vous dans toutes les directions de la matière rayonnant a environ 5800 Kelvin. En conséquence vous vous retrouveriez à équilibrer cette température, en vous brûlant pour de bon. Si vous étiez au foyer d'un ensemble élaboré de miroirs et de bidules, vous seriez dans la même situation, voyant le Soleil dans toutes les directions. Et le résultat serait le même.

On _sent_ qu'il pourrait y avoir un moyen de tricher, mais il n'y en a juste pas. Si vous pouviez trouver un moyen de produire une cible plus chaude que la source, vous auriez produit un [mouvement perpétuel](https://fr.wikipedia.org/wiki/mouvement_perpétuel). _(Note Dr. G : avec les mêmes chances de succès que les roues gravitationnelles et les bidules à aimants : [nulles](/2012/05/27/dites-non-au-mouvement-perpetuel/))_
