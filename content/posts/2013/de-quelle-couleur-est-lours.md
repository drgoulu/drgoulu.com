---
title: "De quelle couleur est l'ours ?"
slug: "de-quelle-couleur-est-lours"
date: 2013-10-08
categories:
  - "Comment"
tags:
  - "geometrie"
  - "humour"
  - "maths"
coverImage: "./images/teddy_bear_rainbow.png"
---

Parfois, un membre du [C@fé des Sciences](http://www.cafe-sciences.org/) lance une "chaîne" de billets sur un thème donné. Là c'est Rock 'n' Science qui a lancé la chaîne des [blagues à caractère scientifique](https://web.archive.org/web/20131005082139/http://sproutchlagrenouille.wordpress.com/2013/10/02/blagues-a-caractere-scientifique-une-chaine/), déjà complétée par plusieurs de mes estimés confrères. Ayant déjà [blogué sur ce thème](/tags/humour/) par le passé et n'osant pas répéter les horreurs circulant sur notre forum interne, ma modeste contribution cette fois-ci se résume à ce petit problème plus mignon que drôle: [![teddy_bear_rainbow](./images/teddy_bear_rainbow.png)](./images/teddy_bear_rainbow.png)

> Un explorateur quitte son campement et marche 20 km plein sud, puis il tourne à angle droit et marche 20 km tout droit en direction de l'est. Puis il tourne à nouveau à angle droit et marche 20 km parfaitement vers le nord. Il arrive en plein sur son campement, où il découvre un ours en train de dévorer ses provisions. De quelle couleur est l'ours ?

Le gag, pour autant qu'il y en ait un, est qu'il existe une réponse logique : blanc.

Apparemment, le trajet de l'explorateur est impossible : comme il est revenu à son point de départ, il a parcouru un triangle équilatéral, mais qui possède deux angles droits ! Or les triangles équilatéraux normaux ont 3 angles de 60°, et un triangle rectangle ne peut comporter qu'un seul angle de 90° puisqu'il est bien connu que la somme des angles d'un triangle vaut 180°.

{{< figure src="./images/4d5f9787f67889f02c5bb6fe390d07cf.png" alt="un triangle équilatéral 3x rectangle (illustration GeoTortue)" caption="un triangle équilatéral 3x rectangle (illustration GeoTortue)" link="http://geotortue.free.fr/index.php?page=geo_intro" align="alignleft" width="192" >}}

Sauf que ceci est valable sur le plan de la [géométrie euclidienne](w:), alors que nous vivons sur une Terre approximativement sphérique où nous devrions plutôt utiliser la [géométrie sphérique](w:) dans laquelle la somme des angles d'un triangle vaut toujours plus de 180°.

De plus, les [coordonnées géographiques](w:) sont bien pratiques dans nos régions, où les directions nord-sud et est-ouest sont bien définies. Mais il existe deux régions au monde où les choses se compliquent : les pôles.

Ce n'est qu'à partir d'un campement situé au pôle nord que notre explorateur peut réaliser le trajet décrit, donc le seul ours qui peut s'y trouver est [Ursus maritimus](w:), dit blanc.

(_paragraphe corrigé le 3.1.14 suite au commentaire de Sophie_) Comme on s'en convainc en observant le dessin ci-contre, l'explorateur revient à sa base selon une direction perpendiculaire à bien différente de sa direction de départ. Tant qu'il reste près du pôle, l'angle au sommet vaut [1 radian, soit 57°](/2010/01/16/histoire-dangles/) environ, mais si son périple descendait jusqu'à l'équateur, il décrirait un triangle équilatéral dont les 3 angles sont droits !

Reste un détail à régler : y'a-t-il vraiment des ours polaires au pôle nord ? Apparemment oui : on en a [vu au dessus de 88°](w:Coordonnées_géographiques) de latitude nord, donc à environ 200 km de l'axe de la Terre.

Bon, il n'est pas vraiment drôle cet article, alors j'en rajoute une courte:

Une logicienne rentre de congé maternité. Un collègue lui demande "ton bébé, c'est un garçon ou une fille ?" Elle : "Vrai."

{{< figure src="./images/bear3.jpg" alt="Le \"triangle\" qu'aurait pu parcourir l'explorateur autour du pôle Sud" caption="Le \"triangle\" qu'aurait pu parcourir l'explorateur autour du pôle Sud" link="https://web.archive.org/web/20120111041956/http://www.qedcat.com/archive/theres_a_bear.html" width="200" >}}

_Ajout du 9.10.13 :_ le commentaire d'Ysmi me plonge dans un émerveillement teinté de regrets, voire de honte. J'aurais du être plus prudent en écrivant qu'il n'y a que la solution du pôle Nord. En fait j'en ai cherché une preuve mathématique que je n'ai pas trouvée, car elle n'existe pas : il existe une solution au pôle Sud, trouvée il y a bien longtemps par Martin Gardner, [décrite en anglais là](https://web.archive.org/web/20120111041956/http://www.qedcat.com/archive/theres_a_bear.html) et illustrée ci-contre.

En effet, si l'explorateur a établi son campement à environ 23,183 km du pôle sud, en descendant 20 km au sud il arrivera à 3.183 km du pôle, puis en allant tout droit vers l'est il décrira un cercle parfait de 20 km de périmètre avant de rejoindre son campement en marchant plein nord sur le chemin par lequel il est arrivé !

Il y a même une infinité de latitudes autour du pôle Sud ou ceci se produit, car si le camp de l'explorateur se trouve à 20 + 10/n.π km où n est un entier positif, il effectuera exactement n tours du pôle sud en parcourant 20 km vers l'est avant de remonter au nord à son campement.

L'ours a donc une forte probabilité d'être en réalité un manchot déguisé, bien que je doute que ces animaux s'éloignent beaucoup de la côte du continent Antarctique
