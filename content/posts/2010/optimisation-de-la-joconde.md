---
title: "Optimisation de la Joconde"
slug: "optimisation-de-la-joconde"
date: 2010-06-14
categories:
  - "Comment"
tags: 
  - "art"
  - "graphes"
  - "graphisme"
  - "informatique"
  - "maths"
  - "proce55ing"
  - "tsp"
coverImage: "./images/10c3a606506bb2299f7b51b61b0ea16f.jpg"

aliases:
  - "/2010/06/13/optimisation-de-la-joconde/"
---

{{< figure src="./images/10c3a606506bb2299f7b51b61b0ea16f.jpg" >}}

Voici enfin l'occasion de consacrer un article marrant au célèbre mais barbant "[problème du voyageur de commerce](w:)". J'ai réalisé une applet en processing qui dessine Mona Lisa avec une seule ligne brisée zig-zaguant entre 100'000 points sans jamais s'entrecouper. De plus la ligne n'a ni début ni fin, elle forme un cycle. Autrement dit, on peut dessiner la Joconde comme un cercle déformé, sans lever le crayon... Voici ce que ça donne : c'est publié aussi :

<iframe src="https://openprocessing.org/sketch/10400/embed/?plusEmbedHash=59c47346&userID=573&plusEmbedTitle=true&show=sketch" width="640" height="640"></iframe>

*(Applet p5.js disponible sur [OpenProcessing)](https://web.archive.org/web/20100614/https://openprocessing.org/@Goulu/10400) ou [GitHub Pages](https://goulu.github.io/processing/src/TSPart/) • Code source sur [GitHub](https://github.com/goulu/processing/tree/main/src/TSPart))*

Le dessin a initialement été produit par [Robert Bosch](https://web.archive.org/web/20100620094923/http://www.oberlin.edu/math/faculty/bosch.html), un prof de maths allemand qui étudie l' "Opt Art", l'utilisation de techniques d'optimisation dans l'art. La [méthode](https://web.archive.org/web/20100529102805/http://www.oberlin.edu/math/faculty/bosch/making-tspart-page.html) est assez simple:

1. on prend une image en "niveaux de gris"
2. on dispose un grand nombre N de points sur l'image, resserrés dans les zones sombres, plus espacés dans les zones claires. [Craig S. Kaplan](http://www.cgl.uwaterloo.ca/~csk/) a eu l'idée d'utiliser l'algorithme "[Voronoï Stippler](https://web.archive.org/web/20100615071546/http://mrl.nyu.edu/~ajsecord/stipples.html)" [[2]](#ref-2) qui fait ça de manière remarquable.
3. Ensuite, il suffit de résoudre le problème du voyageur de commerce à N villes pour obtenir le circuit le plus court entre les N points, donc sans intersection.

Quand vous lisez "il suffit de.."  , il faut vous méfier. C'est souvent sous cette formule lapidaire qu'on cache l'os. En réalité, le problème du voyageur de commerce ("Travelling Salesman Problem" en anglais, TSP dans la suite) est un problème "NP-complet", un de ceux qui nécessite un nombre "non polynomial" d'opérations pour sa résolution, "non polynomial" étant un euphémisme. En l'occurence, il faut en principe mesurer la longueur des N! (N [factorielle](w:)...) [cycles hamiltoniens](w:graphe_hamiltonien) possibles passant par les N points pour déterminer lequel est le plus court. Au delà de N=20, on oublie.

Mais le TSP a un intérêt certain pour beaucoup d'applications pratiques dans lesquelles N est bien plus grand, ce qui justifie la recherche d'algorithmes efficaces mêmes s'ils ne fournissent pas la solution absolument optimale. Le site [TSP de Georgia Tech](https://web.archive.org/web/20100605135713/http://www.tsp.gatech.edu/) est une mine d'exemples et d'infos sur les progrès de la résolution du TSP. On y trouve également [Concorde](https://web.archive.org/web/20100613012038/http://www.tsp.gatech.edu/concorde/index.html), un solveur de TSP open source très performant basé sur la [programmation linéaire](w:). Il détient le record du plus gros TSP résolu, pour N=85'500 calculé en  135 années de CPU, mais résout des problèmes raisonnables en un temps qui l'est aussi. J'ai eu l'occasion de m'en servir pour optimiser le parcours d'une perceuse de circuits imprimés où N valait autour de 1000: quelques minutes de calcul permettent d'économiser des secondes de travail par circuit. Il existe d'ailleurs un [Concorde en ligne](https://neos-server.org/neos/solvers/co:concorde/TSP.html) pour résoudre vos (pas trop gros) problèmes de TSP.

Pour revenir à la Joconde, elle fait l'objet d'un petit [concours](https://web.archive.org/web/20100626050431/http://www.tsp.gatech.edu/data/ml/monalisa.html) car il n'est pas sur que le chemin affiché dans l'image soit le plus court possible entre les 100'000 points définis par R. Bosch. Ce chemin, calculé par Yuichi Nagata avec Concorde a une longueur de 5'757'191 unités, alors qu'on a pu déterminer que le chemin ne peut pas être plus court que 5'757'044 unités. Il est donc possible qu'il existe un chemin encore plus court de 0.0026% ! Tout ce qu'il vous faut pour le trouver, c'est le fichier [mona-lisa100K.tsp](https://web.archive.org/web/20100627205442/http://www.tsp.gatech.edu/data/ml/mona-lisa100K.tsp), et touiller un peu le code de Concorde ou de son concurrent [TSPLib](https://www.iwr.uni-heidelberg.de/groups/comopt/software/TSPLIB95/). Ah, et un superordinateur peut être utile aussi.  Si vous trouvez le chemin le plus court, vous gagnerez la somme mirobolante de $100 !

_edit du 20/9/13_ : l'applet utilise maintenant Processing.js, mais le chargement des données est très lent...

### Références:

1. <span id="ref-1"></span>Robert Bosch, "[Opt Art](https://docs.google.com/viewer?url=http%3A%2F%2Fwww.maa.org%2Fmathhorizons%2Fpdfs%2FFeb_2006_p.06-09.pdf)", Math Horizons, February 2006, pages 6--9.
2. <span id="ref-2"></span>Adrian Secord, "[Weighted Voronoi Stippling](https://web.archive.org/web/20100615232655/http://mrl.nyu.edu/~ajsecord/npar2002/npar2002_ajsecord_preprint.pdf)", 2002, Proceedings of 2nd [NPAR](http://www.npar.org/), Annecy, p 37-43
