---
title: "Surfaces implicites"
slug: "surfaces-implicites"
date: 2009-02-04
categories:
  - "Comment"
tags:
  - "3d"
  - "art"
  - "geometrie"
  - "logiciels"
coverImage: "./images/Boy.jpg"
---

Les surfaces "explicites" sont faciles à représenter graphiquement : de nombreux logiciels sont capables d'évaluer des fonctions du type {x,y,z}=f(u,v) en balayant les paramètres u et v pour obtenir très rapidement de nombreux points de la surface, et les ordinateurs actuels disposent de cartes graphiques pouvant afficher le résultat sous n'importe quel angle en temps réel ([JegX arrive même à y ajouter des poils...](http://www.ozone3d.net/benchmarks/fur/index.php?lang=1))

{{< figure src="./images/2336066181deafac8b8a8b928a1520d0.jpg" alt="Surface de Boy (explicite) tracée par 3D-XplorMath" caption="Surface de Boy (explicite) tracée par 3D-XplorMath. Les courbes noires correspondent à la paramétrisation {u,v}" link="http://3d-xplormath.org/TopLevel/download.html" width="400" >}}

Mais de nombreuses surfaces mathématiques ne peuvent pas être définies explicitement. La formulation la plus générale des surfaces, f(x,y,z)=0, est "implicite" : il faut chercher quels sont les points de l'espace à 3 dimensions appartiennent à la surface, puis "lisser" la représentation graphique de cet ensemble de points, ce qui est loin d'être simple. En fait c'est toujours un [sujet de recherche actuel](http://www.google.com/search?q=visualization+of+implicit+surfaces)

Jusqu'à récemment, seuls les logiciels de maths comme Maple ou [Mathematica](http://reference.wolfram.com/mathematica/ref/ContourPlot3D.html) permettaient de représenter des surfaces implicites, mais l'esthétique n'était pas au rendez vous. Mais il existe désormais des logiciels gratuits produisant de magnifiques rendus de surfaces implicites obtenus par lancer de rayons (ray tracing).

Le plus avancé est "[Surfer](http://www.imaginary2008.de/surfer.php)", développé l'an passé en Allemagne, pays où 2008 fut décrété "année des mathématiques". L'[exposition itinérante "Imaginary 2008"](http://www.imaginary2008.de/) présentait des [oeuvres produites avec Surfer](http://www.imaginary2008.de/galerie.php) par des artistes ou par les participants à un [concours de la plus belle surface](http://www.imaginary2008.de/galerie_view.php?gal=29).

{{< figure src="./images/cfde4c4738f15eeac11350853a7476ac.png" alt="Tülle, par Herwig Hauser, produit avec le logiciel Surfer" caption="\"Tülle\", par Herwig Hauser, produit avec le logiciel Surfer" link="http://images.math.cnrs.fr/spip.php?page=image&id_document=733" align="aligncenter" width="439" >}}

Surfer est disponible pour Windows et pour Linux (avec code source C++), mais aussi sous forme d'une [applet Java,  JSurfer](http://www.imaginary2008.de/jsurfer.php).

[3D-XplorMath](http://3d-xplormath.org) est un logiciel plus ancien dont j'ai déjà parlé [ici](/2007/09/19/maths-et-art/). Depuis sa récente version 10, il peut également représenter des surfaces implicites et il existe également une [applet Java aux possibilités très étendues](http://3d-xplormath.org/j/applets/fr/index.html)

{{< figure src="./images/00df67d596832fce74a1c9b0d3885549.png" alt="sextique" caption="Sextique de Barth faite avec 3X-XplorMath. Cette surface comporte de nombreuse singularités et est d'autant plus difficile à représenter." link="http://3d-xplormath.org/j/applets/fr/vmm-surface-implicit-BarthSextic.html" align="aligncenter" width="439" >}}
