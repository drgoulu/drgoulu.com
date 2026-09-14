---
title: "Couleurs, Gamuts, Python et Open Source"
slug: "couleur-gamut-python-open-source"
date: 2016-09-30
categories:
  - "Comment"
tags: 
  - "couleur"
  - "geometrie"
  - "open-source"
  - "programmation"
  - "python"
coverImage: "./images/crt_print_gamut_big.JPG"
---

Ce fut une excellente journée de travail, stimulante et productive. Tôt le matin, Cédric m'a montré les slides d'un article sur la mesure géométrique de la différence entre deux [gamuts](w:gamut), en me demandant s'il était facile de programmer la méthode présentée [[1]](#ref-1)

Avant d'attaquer la question et la réponse,  une petite introduction sur le merveilleux monde des couleurs s'impose.

### Couleurs et gamuts

En imprimerie, on mesure à l'aide d'un [spectrophotomètre](w:) l'ensemble des couleurs produites par une imprimante, ne serait-ce que pour la calibrer [[2]](#ref-2). Mais lorsqu'on développe une imprimante industrielle, il faut en plus mesurer l'effet sur les couleurs de nombreux paramètres (qualité des substrats, composition des encres, puissance des séchoirs etc. ) afin de maximiser le "volume" des couleurs que l'imprimante est capable de reproduire.

{{< figure src="./images/color7.gif" alt="cube des couleurs RGB (Red Green Blue)" caption="cube des couleurs RGB (Red Green Blue)" width="320" >}}

L'ensemble des couleurs définit un volume car il faut trois paramètres pour déterminer une couleur. La représentation la plus connue est celle basée sur les [couleurs primitives](w:) rouge, vert et bleu, le "RGB". Sur votre écran, des pixels rouges, verts et bleus peuvent être allumés avec des intensités variables, habituellement codée par un entier entre 0 et 255. La [synthèse additive](w:) permet ainsi de vous faire percevoir 16'777'216 couleurs différentes définies par autant de points dans le cube ci-contre.

De même, on peut faire un cube "CMY" avec les couleurs produites par [synthèse soustractive](w:) en déposant des encres cyan, magenta et jaune sur du papier supposé blanc.

Oui mais voilà, comme vous vous en apercevez chaque fois que vous imprimez des photos à la maison, on n'obtient pas les mêmes couleurs en RGB et en CMY. Les deux cubes ne se superposent pas bien. Intuitivement, on comprend qu'un écran ne peut pas être plus noir que quand il est éteint, et qu'on ne peut pas rendre le papier plus blanc qu'il ne l'est originellement. Le même raisonnement s'applique aux autres directions de l'espace des couleurs : certaines couleurs possibles en RGB ne peuvent pas être obtenues en impression CMY, et vice-versa. C'est d'ailleurs pour ça que les imprimantes photo ont des couleurs supplémentaires, souvent du "magenta clair" et du "cyan clair" pour mieux imprimer vos couchers de soleils. Et aussi du noir, mais c'est plutôt pour imprimer du plus joli texte et économiser de l'encre des 3 autres couleurs.

Les couleurs que l'on peut reproduire fidèlement se trouvent dans l'intersection des deux cubes, mais les axes des deux cubes ne sont pas les mêmes, alors comment faire ?

En les représentant dans un autre espace de couleurs, plus vaste, le [CIE_L\*a\*b\*](w:CIE_L*a*b*). Dans cet espace, la coordonnée L\* correspond à la [luminance](w:) et les coordonnées a\* et b\* à des échelles entre couleurs tenant compte de la sensibilité de l'oeil humain. En LAB, le cube CMY d'une imprimante donnée devient un patatoïde comme celui représenté ci-dessous, et le cube RGB d'un écran précis devient le volume enfermé dans le treillis. Comme on le voit, l'intersection des deux est un volume compliqué, nettement plus petit que chacun des patatoïdes.

{{< figure src="./images/crt_print_gamut_big.JPG" alt="Gamut d" caption="Gamut d'une imprimante (solide) et d'un moniteur (treillis). Image : Michael J. Vrhel" link="http://www.viegroup.com/mvrhelweb/gamut.html" align="aligncenter" width="512" >}}

### Retour au Code

Bon mais alors, est-ce qu'on peut faire facilement un programme qui calcule l'intersection de deux gamuts quelconques ? Dans ces cas là la réponse standard est "ça dépend" :

- si le code Matlab décrit dans l'article [[1]](#ref-1) est disponible, c'est tout cuit. Et peut-être même gratuit si  [Octave](https://www.gnu.org/software/octave/) suffit.
- sinon (je n'ai pas trouvé le code...), ça dépend de l'existence de librairies (Python de préférence) effectuant les opérations délicates:
    - Lire les fichiers produits par le  : pas de problème car ce sont des .txt avec les valeurs LAB des quelques dizaines de couleurs mesurées
    - Obtenir l'[enveloppe convexe](w:)\* des points : pas de problème non plus. J'avais déjà utilisé la fonction [scipy.spatial.ConvexHull](http://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.ConvexHull.html) basée sur la librairie [QHull](http://www.qhull.org) [[3]](#ref-3). C'est d'ailleurs la même qu'utilise la fonction Matlab [convhulln](http://mathworks.com/help/matlab/ref/convhulln.html). Et elle fournit même le volume du [polyèdre](w:) en prime!
    - Par contre, je n'ai aucune idée de comment calculer l'intersection des deux polyèdres / gamuts. Ou plutôt si : je sais que si je ne trouve pas du code faisant ça vite et bien, je vais passer longtemps à le faire mal. En gros il faut calculer l'intersection de la surface en fil de fer avec la surface colorée dans l'image ci-contre, et vice-versa. L'algorithme le plus simple qui vient à l'esprit est de vérifier si chaque côté des petits triangles formant une surface intersecte un (ou deux ...) triangles formant l'autre surface, puis de refaire une enveloppe convexe de tous points d'intersection. Comme tout algo simple, il y en a probablement un bien plus efficace quelque part ...

En cherchant un peu, je tombe sur la solution : [trimesh](https://pypi.python.org/pypi/trimesh), un package Python capable de faire des "Boolean operations on meshes (intersection, union, difference)". Je l'installe, je code le gros de l'application, et exactement une heure après avoir attaqué le problème, je vois le volume de mes gamuts s'afficher ! mais l'appel à la fonction calculant l'intersection crashe...

### C'est la saison des châtaignes : débogage

- d'abord il faut installer [RTree](http://toblerity.org/rtree/), un wrapper Python de [libspatialindex](http://libspatialindex.github.io/). J'avais déjà rencontré cette librairie permettant de trouver rapidement les points les plus proches d'un autre en utilisant la structure d'[arbre R\*](w:en:R*_tree) [[5]](#ref-5) mais n'étais pas sur d'en avoir vraiment besoin. Un message d'erreur me dit que si... Sur une machine Windows, cette librairie ne s'installe pas "toute seule", il faut aller la chercher sur la fabuleuse page "[Unofficial Windows Binaries for Python Extension Packages](http://www.lfd.uci.edu/~gohlke/pythonlibs/)"
- ensuite je découvre pourquoi la phrase "Boolean operations on meshes (intersection, union, difference)" avait une suite : "if [OpenSCAD](w:) or [Blender](w:) is installed". En fait, trimesh appelle l'un ou l'autre de ces logiciels pour faire le vrai boulot. Connaissant l'existence des deux, mais ayant joué avec Blender il y a quelques années et me souvenant qu'il utilise Python comme langage de script, j'opte pour Blender et ...
- ... le code tourne ! Mais me renvoie toujours un volume de l'intersection de mes gamuts nul. Ce sont les [fichiers STL](w:fichier_de_stéréolithographie) temporaires que trimesh crée qui sont encore ouverts lorsque Blender y accède. Bizarre, parce que [trimesh uilise travis-ci](https://travis-ci.org/mikedh/trimesh) pour effectuer des tests automatiques et que ceux-ci ne montrent aucun problème ... Mais les tests tournent sur une machine (virtuelle) Linux ! Apparemment, un pingouin a le droit de lire un fichier qu'un autre pingouin a laissé ouvert, mais une fenêtre doit être refermée avant qu'elle puisse être réouverte... Je vais devoir modifier le code de trimesh pour corriger ça, et je décide de le faire bien.

### L'Open Source, c'est bon pour le business

![%image\_alt%](./images/opensourceloveday.png)En effet, je ne sais pas si vous avez tout suivi mais je travaille dans une entreprise qui vend des machines pour gagner du pognon et payer quelques salaires en passant. Or tous les logiciels utilisés pour développer cette application relativement pointue en une seule journée sont "[Open Source](w:)", gratuits. La moindre des choses est, me semble-t-il, de renvoyer parfois l'ascenseur partageant les améliorations que j'apporte à ces logiciels, évidemment dans la mesure où ça ne va pas à l'encontre des intérêts de mon employeur.

J'ai donc [forké le source](https://github.com/goulu/trimesh) de [trimesh disponible sur GitHub](https://github.com/mikedh/trimesh), modifié [le fichier](https://github.com/goulu/trimesh/blob/master/trimesh/interfaces/generic.py) qui gère les fichiers temporaires et hop ! l'application fonctionne après grosso-modo 4 heures de boulot et 4 cafés. Et comme [les tests](https://travis-ci.org/goulu/) de trimesh passent toujours (sur Linux), je soumets une "[pull request](https://github.com/mikedh/trimesh/pull/33)" à l'auteur de trimesh pour lui proposer d'incorporer mes changements à la branche officielle : B.A. accomplie en une heure supplémentaire à tout casser.

Après ça il me restait encore un moment pour implanter une idée qui m'avait traversé l'esprit : compter combien de [couleurs Pantone](w:Pantone_(entreprise)) sont incluses dans chaque gamut (et donc possible d'imprimer avec notre machine), et lister celles qui n'y sont pas. Mais comme les valeurs Lab de ces couleurs sont protégées par copyright, je ne pourrai pas mettre ce code à disposition en Open Source. Des centaines de milliers de lignes de code testé et performant oui, mais une table de couleurs, non...

Note\* : ce qu'il y a de bien en écrivant un article, c'est que ça met les idées en place, ou que ça instille un léger doute. En regardant les polyèdres des gamuts RGB et CMY dans LAB, on voit qu'ils ne sont pas convexes... Pour être plus précis, peut-être bien qu'il me faudrait utiliser un algo plus subtil que ConvexHull ...

### Références:

1. <span id="ref-1"></span>Deshpande, K., Green, P., & Pointer, M. R. "Metrics for comparing and analyzing two colour gamuts", 2015, Color Research & Application, 40(5), 465–471.{{< altmetric doi="10.1002/col.21930" >}} ([slides pdf](http://www.color.org/events/frankfurt/Deshpande_ICCFrankfurt2013_Gamut_analysis.pdf))
2. <span id="ref-2"></span>Arnaud Frich "Guide de la Gestion des Couleurs - [le calibrage de l'imprimante](http://www.guide-gestion-des-couleurs.com/calibrage-imprimante.html)", 2016
3. <span id="ref-3"></span>Barber, C.B., Dobkin, D.P., and Huhdanpaa, H.T., "The Quickhull algorithm for convex hulls," _ACM Trans. on Mathematical Software_, 22(4):469-483, Dec 1996, [http://www.qhull.org](http://www.qhull.org)
4. <span id="ref-4"></span>Vrhel, M. J., & Trussell, H. J. "[Color Device Calibration: A Mathematical Formulation](http://www.viegroup.com/mvrhelweb/pdfs/IP_COLOR_PAPER.pdf)", 1999, IEEE Transactions on Image processing, 8(12).
5. <span id="ref-5"></span>Beckmann, N., & al. "[The R\*-tree: an efficient and robust access method for points and rectangles](https://epub.ub.uni-muenchen.de/4256/1/31.pdf)" 1990, In Proceedings of the 1990 ACM SIGMOD international conference on Management of data  - SIGMOD ’90 (Vol. 19, pp. 322–331). New York, USA: ACM Press.{{< altmetric doi="10.1145/93597.98741" >}}
