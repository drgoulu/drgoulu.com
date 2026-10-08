---
title: "Icosien, le nouveau jeu de Neamar"
slug: "icosien-le-nouveau-jeu-de-neamar"
date: 2010-06-24
categories:
  - "Comment"
tags: 
  - "casse-tetes"
  - "graphes"
  - "internet"
  - "jeux"
coverImage: "./images/f860cf98facccf60ba0d8705f857b25d.png"
---

Il l'avait annoncé, il l'a fait : Neamar a ajouté un nouveau jeu à sa [saga des graphes](/2010/03/06/la-saga-des-graphes/) : [Icosien](http://neamar.fr/Res/Icosien/). Et c'est un excellent jeu. En réalité il y a même deux jeux pour le prix d'un seul:

- Dans les 10 premiers tableaux, il s'agit de reproduire le motif gris d'un seul mouvement de souris, sans repasser deux fois sur le même trait (mais les croisements de fil sont autorisés). En termes techniques, il s'agit de vérifier que ces tableaux sont des [graphes eulériens](w:Graphe_eulérien). Pas trop difficile une fois qu'on a trouvé le truc.
- Dans les 10 tableaux suivants, il faut passer une et une seule fois par chaque noeud, en utilisant uniquement les traits disponibles  (mais on n'est pas obligé de passer sur tous les traits). Pour les matheux, il s'agit de trouver des [circuits hamiltoniens](w:Graphe_hamiltonien). Là, la difficulté passe de "petit casse-tête sympa" à "horrible arrache neurones énervant"...

{{< figure src="./images/f860cf98facccf60ba0d8705f857b25d.png" alt="tableau19" caption="J'en suis là. C'est dur. Regarder la soluce de Neamar serait déshonorant. A l'aide Python !" link="http://neamar.fr/Res/Icosien/" align="aligncenter" width="512" >}}

De plus, je décerne à Icosien le titre envié de "plus beau jeu de graphes du web" pour deux raisons:

- Le design de Licoti ([un de plus](/2010/06/06/le-systeme-solaire-selon-licoti/)) est vraiment réussi. Bravo !

- L'interface utilisateur est tout simplement géniale. Quand Neamar avait pondu un [petit article sur le sujet](https://web.archive.org/web/20101130153810/http://blog.neamar.fr/component/content/article/18-algorithmie-et-optimisation/119-mouvement-intuitif-graphe-souris), je n'avais pas compris à quel point son système est simple et efficace.  Je réalise maintenant que sans ça, ce beau jeu aurait été injouable.

Enfin, mentionnons qu'Icosien peut être instructif. "Peut" car on n'est pas obligé de connaitre la théorie des graphes pour y jouer, mais qu'y jouer peut inciter à la lecture des nombreuses informations figurant sur la page du jeu, et  suivre les liens conduit vers pleins d'infos intéressantes.

### A voir aussi:

- le "[making of](http://blog.neamar.fr/component/content/article/15-as3/137-images-icosien)" (spoiler alert ! cetta page contient la solution de certains tableaux, dont le 19, argh! )
- le [code source](http://neamar.fr/Res/Icosien/Code.php) en Action Script 3
- la version 1857 de l' "[Icosian Game](https://web.archive.org/web/20100128044455/http://puzzlemuseum.com/month/picm02/200207icosian.htm)" par Hamilton himself, en vrai bois d'arbre
- "[Icosian Game](http://mathworld.wolfram.com/IcosianGame.html)" sur MathWorld
