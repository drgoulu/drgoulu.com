---
title: "Hyperion 3D"
slug: "hyperion-3d"
date: 2007-03-25
tags: 
  - "3d"
  - "logiciels"
coverImage: "./images/b24023b52e01ce08024a5ef067f2ea0a.gif"
---

[Hypergraphics-3D](https://web.archive.org/web/20070127095756/http://www.hypergraphics3d.com) est une entreprise genevoise en création qui va "faire très fort". ![](./images/b24023b52e01ce08024a5ef067f2ea0a.gif)Son produit "[Hyperion](http://www.ozone3d.net/demoniak3d/)" est une version "professionnelle et facile à utiliser" des moteurs 3D utilisés dans les jeux pour faire du rendu et de l'animation en temps réel.

Par "professionnelle", il faut comprendre qu'[Hyperion](http://www.ozone3d.net/demoniak3d/) vise le réalisme et la qualité d'image pour la visualisation de produits industriels ou de constructions.

![](./images/demo_001.jpg) _Exemple de rendu en **temps réel** obtenu avec Hyperion !_

[Hyperion](http://www.ozone3d.net/demoniak3d/) est "facile à utiliser" car toute la scène à représenter, les informations d'éclairage, de matière (texture) , l'interactivité, les effets visuels spéciaux et bien d'autres choses sont décrites dans un seul fichier XML, éditable avec un éditeur de texte comme [PsPad](/2005/06/16/pspad/) par exemple.

<!--more-->

### Un peu de démo

En pratique, vous pouvez télécharger "Hyperion Demo-System Free" (gratuit pour utilisation privée) [ici](http://www.ozone3d.net/demoniak3d/download.php), l'installer puis aller à la [page des démos](http://www.ozone3d.net/demos_projects/index.php) pour télécharger quelques exemples de réalisations.

Mes préférés sont :

- [La montre](https://web.archive.org/web/20070831122707/http://www.hypergraphics3d.com/demos/watch.php), qui n'est pas encore en ligne, mais que j'ai eu l'occasion de voir chez Hypergraphics-3D. Franchement bluffant : au chargement j'ai vu l'image ci-dessus et cru qu'il s'agissait d'une image fixe produite par rendu, et tout à coup tout s'est mis à tourner, fluide, avec ombres et réflexions. Magnifique!
- [Lost Church](http://www.ozone3d.net/demos_projects/lost_church.php) et [Musée Privé](http://www.ozone3d.net/demos_projects/private_museum.php) pour les application "architecturales", montrant le rendu des éclairages
- [Aberration Chromatique](http://www.ozone3d.net/demos_projects/chromatic_aberration.php) qui visualise un objet transparent et les effets optiques qu'il provoque
- [Fractale de Mandelbrot](http://www.ozone3d.net/demos_projects/mandelbrot_set.php), qui n'est pas de la 3D mais illustre un point important que je développe un peu plus bas.

### Un peu de sous

Hyperion est très bon marché : gratuit pour utilisation individuelle, €149 (~ Frs 240.-) pour l'édition "indie" permettant déjà une utilisation commerciale et €749 (~1200.-) pour l'édition professionnelle, qui offre une résolution illimitée du rendu.

Franchement ça vaut le coup, et Hypergraphics-3D a besoin d'un coup de main pour démarrer. Je ne fais pas souvent de pub mais là je le dis : [achetez Hyperion](http://www.ozone3d.net/demoniak3d/purchase.php) !

### Un peu de technique

Il y a d'autres moyens de visualiser des produits ou projets en 3D "temps réel", mais ils entrent tous dans 2 catégories:

1. les visualisateurs de fichers 3D comme [e-Drawings](https://web.archive.org/web/20081219092141/http://www.solidworks.fr/sw/products/free-cad-software-downloads.htm) ont une interactivité limitée car prédéfinie : on ne peut que cacher certains éléments. D'autre part, visant le travail collaboratif, ils réduisent la taille des fichiers au minimum au détriment de la qualité du rendu.
2. les "moteurs 3D" comme [Irrlicht](https://web.archive.org/web/20070322102404/http://irrlicht.sourceforge.net/), qui sont fait pour être intégrés dans un programme spécifique développé par l'utilisateur. En pratique, cette approche est utilisée dans tous les jeux video

[Hyperion](http://www.ozone3d.net/demoniak3d/) combine un moteur 3D performant avec un interpréteur XML et le langage de script [LUA](http://www.lua.org/) qui permet. Cette approche permet de combiner les avantages respectifs des 2 catégories ci dessus:

1. une scène complète peut être décrite par un fichier XML,
2. en conservant tous la souplesse permise par un langage de programmation.

La puissance unique de cette combinaison apparait lorsqu'on s'intéresse aux "[shaders](w:Shader)". Ces mini-programmes s'exécutent dans le GPU de la carte graphique et permettent de calculer le rendu précis de la matière ou de réaliser des effets spéciaux divers.

Habituellement, il faut les programmer puis les compiler à l'aide d'outils spéciaux, ce qui réserve leur usage aux jeux, démos de cartes graphiques et autres applications pointues comme le ["RealView" de SolidWorks](http://www.solidworks.com/sw/products/details.htm?productid=217). Hyperion permet d'intégrer directement les shaders au niveau du fichier XML de description de scène, ce qui donne accès à toute la puissance des cartes graphiques depuis un programme "de haut niveau".

La démo [Fractale de Mandelbrot](http://www.ozone3d.net/demos_projects/mandelbrot_set.php) d'Hypérion montre ceci de façon spectaculaire : elle utilise le GPU de la carte graphique et non le CPU de votre PC pour réaliser une quantité énorme de calculs : chaque pixel de l'écran est calculé par son propre "shader", dont le code peut être consulté directement dans le fichier XML !

"Stay Tuned". Je vais recauser d'Hyperion très bientôt.
