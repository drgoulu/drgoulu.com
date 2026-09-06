---
title: "La vie à bas Reynolds"
slug: "la-vie-a-bas-reynold"
date: 2011-03-13
categories:
  - "Comment"
  - "Pourquoi"
tags: 
  - "fluides"
  - "mecanique"
  - "nano"
coverImage: "6b6e8564e18a75bb838389e2aee49068.jpg"
---

{{< figure src="images/6b6e8564e18a75bb838389e2aee49068.jpg" alt="© Anthony Carré - CNRS 2006" caption="© Anthony Carré - CNRS 2006" width="215" >}}

Cet article est parti d'une question de Michel : "pourquoi l'araignée ne tourne pas au bout de son fil ?" .

Les réponses que l'on trouve sur le web se réfèrent principalement aux étonnantes propriétés mécaniques du fil d'araignée  [[1]](#ref-1). D'un diamètre de 2 à 15 microns selon les espèces, il peut soutenir une traction de plusieurs grammes grâce à sa résistance de 450 kg/mm2, nettement supérieure à celle d'un bon acier trempé (~100 kg/mm2). Le fil d'araignée est également très élastique, il peut s'allonger de 40% avant de céder. En torsion, le fil d'araignée est plus rigide que le kevlar [[1]](#ref-1), mais surtout il amortit les oscillations de manière spectaculaire, un peu comme les matériaux à "mémoire de forme", ce qui conduit à penser que le fil joue un rôle important dans la stabilité de l'animal. [[2]](#ref-2), [[3]](#ref-3)

Toutefois cette explication ne me satisfait pas pleinement, car la constante de torsion d'un fil de 20 microns de diamètre et de 1m de long n'est que de 37.10\-12 Nm/rad, donc si un léger courant d'air appliquait une force d'un milligramme (10 millinewtons) de plus d'un côté d'une araignée de 2cm que de l'autre, la pauvre bête effectuerait plus de 425 tours sur elle-même avant que le moment de rappel du fil ne stoppe son supplice.

Un autre phénomène empêche donc les araignées de se transformer en toupies : l'aérodynamique. Pour un animal d'un centimètre dans l'air calme des sous-bois, disons limité à 1 m/s (3.6 km/h), le [nombre de Reynolds](w:) ne vaut que re=640, inférieur à 2000 ce qui signifie que l'écoulement de l'air autour de l'araignée est laminaire : aucune turbulence n'existe pour créer de petite force qui ferait tourner l'araignée.

En réalité, l'araignée se sent dans la brise comme un petit alevin dans l'eau calme d'un étang. Ca surprend, mais la [viscosité cinématique](w:) de l'air est 15 fois plus élevée que celle de l'eau, ce qui signifie qu'un écoulement d'air autour d'un objet donné est similaire à un écoulement d'eau 15 fois plus lent, plus facile à se représenter. A son échelle, l’araignée nage littéralement dans un fluide visqueux. Peu dense certes, mais la viscosité élevée de l'air à cette échelle amortit tout mouvement de l'araignée, freinée tout comme un alevin s'arrête net dès qu'il cesse de frétiller de la nageoire.

D'ailleurs les très petits animaux aquatiques ne nagent pas du tout de la même manière que les baleines, comme l'a remarqué Purcell dans un article culte de 1977 [[4]](#ref-4)\*. La micro-algue Eutreptiella ci-dessous mesure environ 0.1 mm de long et met environ 10 secondes à avancer de sa propre longueur:

{{< youtube id="_k78AWnDaqA" width="640" >}}

Elle nage donc à 0.01 mm/s et l'écoulement est caractérisé par un nombre de Reynolds re=0.001, extrêmement faible. C'est donc un [écoulement de Stokes](w:) si lent que l'inertie du liquide ne joue plus aucun rôle. Qui plus est, un tel écoulement est parfaitement réversible, ce qui a un effet intéressant sur la natation : un organisme qui effectuerait un certain mouvement pour se propulser reculerait d'autant en effectuant le mouvement inverse. Par exemple, les mouvements alternés de la queue d'un poisson ne lui permettraient pas d'avancer dans un liquide beaucoup plus visqueux que l'eau, comme on le voit dans [cette video](http://www.youtube.com/watch?v=2kkfHj3LHeE).

Depuis quelques années on étudie les techniques de natation à bas Reynolds, soit pour les imiter avec de futurs [nano-robots](/2007/04/15/mini-micro-nano/), soit pour perturber les déplacements de microbes pathogènes. Un des premiers modèles proposés est le "nageur de Golestanian", qui avance en utilisant les mouvements relatifs de 3 sphères alignées [[5]](#ref-5). Un peu plus tard, A. De Simone a imaginé un "stick and donut" plus rapide pour la même puissance, mais nécessitant une déformation importante du nageur, une faculté partagée par Eutreptiella et de nombreux unicellulaires.

{{< youtube id="aN6I9mJVuas" width="640" >}}

On pourrait croire que les spermatozoïdes et autres cellules [flagellées](w:flagelle) sont des contre-exemples, mais il n'en est rien car les flagelles ne font pas des mouvements d'aller/retour, mais des cycles toujours dans le même sens grâce aux seuls "roues" et moteurs rotatifs que la nature ait produit. Les flagelles sont plus des hélices que des nageoires, et les hélices, ça marche assez bien à bas Reynolds, comme on le voit dans [cette video](http://www.youtube.com/watch?v=s_5ygWhcxKk).

Comme l'avait [si bien expliqué Feynman](/2009/06/11/il-y-a-plein-de-place-en-bas-2/), beaucoup de phénomènes physiques sont plus simples et plus maîtrisables à petite échelle, et c'est le cas pour les fluides. Michel, ne t'en fais pas : la vie est bien plus simple pour une araignée au bout de son fil que pour un alpiniste pendu au bout de sa corde.

**Note\* :** j'ai commencé la traduction en français de cet article. La traduction en français est terminée, elle est [ici](/2011/04/30/la-vie-a-faible-nombre-de-reynolds/)

### Références

1. <span id="ref-1"></span>Ko, Kawabata et al "[Engineering properties of spider silk](http://web.mit.edu/course/3/3.064/www/slides/Ko_spider_silk.pdf)"
2. <span id="ref-2"></span>"[Pourquoi l'araignée suspendue à un fil ne tourne pas sur elle-même](http://www2.cnrs.fr/presse/communique/840.htm)", Communiqué de presse du CNRS, 30 mars 2006
3. <span id="ref-3"></span>Olivier Emile, Albert Le Floch, Fritz Vollrath, "[Biopolymers: Shape memory in spider draglines](http://www.nature.com/nature/journal/v440/n7084/full/440621a.html)", Nature 440, 621, 30 March 2006,([graphique](http://www.nature.com/nature/journal/v440/n7084/fig_tab/440621a_F1.html))
4. <span id="ref-4"></span>E.M. Purcell. "[Life at Low Reynolds Number](http://jila.colorado.edu/perkinsgroup/Purcell_life_at_low_reynolds_number.pdf)", 1977, American Journal of Physics vol 45, pages 3-11 ([traduction française](/2011/04/30/la-vie-a-faible-nombre-de-reynolds/))
5. <span id="ref-5"></span>Ali Najafi, Ramin Golestanian, "[Propulsion at low Reynolds number](http://iopscience.iop.org/0953-8984/17/14/009)", 2005 J. Phys.: Condens. Matter17 S1203
6. <span id="ref-6"></span>[Natation a faible nombre de Reynolds](http://www.cmap.polytechnique.fr/~alouges/nage.php), Centre de Mathématiques Appliquées, Polytechnique
