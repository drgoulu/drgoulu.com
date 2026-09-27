---
title: "Superordinateurs de table"
slug: "superordinateurs-de-table"
date: 2009-03-13
categories:
  - "Comment"
tags: 
  - "3d"
  - "informatique"
  - "loi-de-moore"
  - "simulation"
coverImage: "./images/a470c29cf6c88b820cc608831b61f545.gif"
---

Depuis de nombreuses années, les [ordinateurs les plus puissants](http://top500.org/) sont formés de très nombreux processeurs calculant en parallèle. Le record actuel est tenu par le [“Roadrunner” d’IBM](w:Roadrunner_(supercalculateur)) qui comprend 6'948 Opteron bicœurs et 12'960 processeurs [PowerXCell 8i](http://www.onversity.net/cgi-bin/progactu/actu_aff.cgi?Eudo=bgteob&P=00001079) d'IBM, contenant chacun [8 unités de calcul en flux](w:Cell_(processeur)#Un_c.C5.93ur_principal_et_huit_c.C5.93urs_sp.C3.A9cifiques) ("[Stream Processing](w:en) Unit", SPU).

### Combien ?

"Roadrunner" peut effectuer 1 [petaflops](w:Floating-point_operations_per_second), soit un million de milliards d'opérations arithmétiques par seconde et vaut des millions d'euros. Vous pouvez aujourd'hui assez facilement disposer dans votre PC du millième de cette puissance pour quelques centaines d'euros seulement.

En effet, les [processeurs graphiques](w:Processeur_graphique) "GPU" récents sont formés de centaines d'[unités de calcul en flux](w:en:Graphics_processing_unit#Stream_Processing_and_General_Purpose_GPUs_.28GPGPU.29) assez semblables aux 8 SPU du Cell. Initialement dédiés à la génération d'images réalistes en 3D temps réel et limités au calcul en virgule fixe, les GPU sont devenus capables d'exécuter certains programmes en virgule flottante beaucoup plus rapidement que sur les processeurs classiques : c'est le calcul générique sur GPU  ([GPGPU](w:en)).

La [série 5000 d'ATI (racheté par AMD) et les nouvelles GTX 200 de nVidia](http://www.pcauthority.com.au/Review/119738,ati-radeon-hd-4000-vs-nvidia-geforce-gtx-200.aspx) offrent désormais une puissance de l'ordre du teraflops, soit 200x plus que [les plus puissants processeurs intel](http://www.intel.com/support/processors/sb/CS-023143.htm#1). D'ailleurs nVidia commercialise désormais ses derniers processeurs sur des [cartes "Tesla"](http://www.nvidia.com/object/tesla_computing_solutions.html) dédiées au calcul, et dépourvues de sortie video, un comble pour des processeurs graphiques !

{{< figure src="./images/94026009fee5d5ba9d3a9574be8e5250.jpg" alt="ça ressemple à de la pub, mais ça n'en est pas (hélas)" caption="ça ressemple à de la pub, mais ça n'en est pas (hélas)" align="aligncenter" width="550" >}}

Ainsi, la science peut bénéficier de processeurs puissants à des prix très bas grâce aux [millions de consoles](http://www.vgchartz.com/) et de PC familiaux.

{{< youtube id="jUecNi222Fw" >}}

_Simulation d'écoulement d'un fluide par la méthode "Lattice Bolzmann" exécutée simultanément sur le CPU et sur le GPU..._

### Comment ?

La [loi d'Amdahl](w:) limite beaucoup le gain de performances obtenu en répartissant un programme existant sur plusieurs processeurs ([MIMD](w:Multiple_Instructions_on_Multiple_Data)). Dans un GPU, les centaines de processeurs travaillant en parallèle ne sont réellement efficaces que s'lorsqu'ils effectuent tous les mêmes opérations sur des données différentes ([SIMD](w:Single_Instruction_Multiple_Data)).

Pour exploiter la puissance des GPU il faut donc re-coder bon nombre d'algorithmes et de méthodes numériques en se basant sur une bonne connaissance de l'architecture des GPU, et en utilisant des langages de programmation spécifiques. nVidia a pris une longueur d'avance dès 2007 en proposant [CUDA](w:), une extension du langage C et son compilateur pour les GPU de marque nVidia exclusivement. ATI/AMD a suivi fin 2008 en lançant [Stream](http://www.amd.com/us/products/technologies/Pages/technologies.aspx), une variante du langage [BrookGPU](http://graphics.stanford.edu/projects/brookgpu/), lui même dérivé du C par l'Université de Stanford. Mais Stream ne fonctionne que sur les GPU d'AMD/ATI, évidemment.

Là dessus, des entreprises comme [RapidMind](http://software.intel.com/en-us/articles/intel-array-building-blocks/) ont développé des plate-formes de développement permettant de compiler le même programme C++ pour CPU classiques, GPU nVidia ou ATI/AMD et aussi pour les [processeurs Cell](w:Cell_(processeur)) de "Roadrunner" et des consoles PlayStation 3 de Sony.

Apple a annoncé une nouvelle étape avec [OpenCL](w:), une autre variante de C qui devrait être supportée par son prochain système d'exploitation OS X 10.6 "Snow Leopard" cette année. Microsoft suivra probablement avec quelque chose d'équivalent intégré au Direct X 11 qui accompagnera Windows Seven (si tout va bien...)

Resté bien silencieux sur le sujet des GPU, intel prépare sa revanche en 2010 avec son processeur [Larrabee](w:en:Larrabee_(GPU)), qui contiendra quelques dizaines de coeurs de ses processeurs classiques x86, et donc sera en principe capable d'exécuter simultanément un grand nombre de programmes habituels, tout en offrant une puissance suffisante pour générer des images en 3D également.

### Pour quoi ?

" _le PowerXcell 8i s'adresse avant tout aux scientifiques et au marché des consoles_". Cette merveilleuse [phrase](http://www.pcauthority.com.au/Review/119738,ati-radeon-hd-4000-vs-nvidia-geforce-gtx-200.aspx) s'applique également aux GPU : le marché porteur est celui des jeux video, toujours plus gourmands en qualité d'image et d'animation de scènes 3D complexes, mais aussi en capacité de simulation de phénomènes physiques. On veut de plus en plus de réalisme des chutes, collisions, explosions.

{{< figure src="./images/40dd712b15cbbfe9fbf94f84b24f89a7.jpg" alt="un dinosaure s'effondre... : illustration du chapitre de GPU Gems 3 consacré à la simulation physique. Cliquez sur l'image pour accéder au texte" caption="un dinosaure s'effondre... : illustration du chapitre de GPU Gems 3 consacré à la simulation physique. Cliquez sur l'image pour accéder au texte" link="http://http.developer.nvidia.com/GPUGems3/gpugems3_part05.html" align="aligncenter" width="500" >}}

Jusqu'ici les jeux intégraient la mécanique des corps rigides, mais désormais les cheveux et les habits de nos héros virtuels suivent leurs mouvements, car il est possible de simuler la déformation élastique et la rupture. La prochaine étape est de [simuler l'écoulement de fluides en temps réel](http://3dmon.wordpress.com/2008/08/21/fluides-en-temps-reel-aussi/), on y est presque.

Or les méthodes nécessaires à ces applications ludiques sont très semblables à celles permettant de prévoir la météo, de simuler des galaxies ou de déterminer les propriétés de molécules chimiques, entre autres.

Parmi les 200 applications listées sur la [Cuda Zone de NVidia](http://www.nvidia.com/object/cuda_home_new.html), bon nombre sont des [librairies numériques](http://www.nvidia.com/object/cuda_home_new.html) et d'algèbre linéaire pouvant être appliquées dans de nombreux domaines, comme par exemple [le contrôle des miroirs actifs des télescopes ESO](http://sine.ni.com/cs/app/doc/p/id/cs-11465) qui nécessite d'effectuer chaque milliseconde un produit scalaire d'une matrice 3000 x 6000 par le vecteur des 6000 mesures pour obtenir les 3000 commandes ([video à ce sujet](http://www.youtube.com/watch?v=aHMUQWgWsss))

Les logiciels scientifiques usuels commencent à tirer parti de ces librairies de façon quasiment transparente:

- pour Matlab, il existe déjà un [plugin FFT](http://developer.nvidia.com/cuda-tools-ecosystem) et le l'environnement [Jacket](http://www.accelereyes.com/)
- LabView dispose d'un suport "multicore" intégrant Cuda, utilisé dans le projet [mentionné plus haut](http://sine.ni.com/cs/app/doc/p/id/cs-11465)
- [Mathematica utilise Cuda](http://www.nvidia.fr/object/cuda-programming-mathematica-fr.html) _(lien mis à jour le 13.3.12)_
- Python, mon langage préféré du moment, peut aussi accéder à la puissance de Cuda grâce à [PyCuda](http://pypi.python.org/pypi/pycuda) (_faut que j'essaie ça asap!_)

Et bien d'autres applications spécifiques comme:

- [OpenMM](https://simtk.org/home/openmm), une librairie de [simulation moléculaire](/2008/05/21/si-on-jouait-a-plier-des-proteines/) utilisée dans les [clients haute performance](http://folding.stanford.edu/English/DownloadWinOther) de [Folding@home](http://folding.stanford.edu/French/Main) qui accélère les calculs jusqu'à 700x par rapport à un processeur normal.
- Différents solveurs en [mécanique des fluides](http://www.nvidia.com/object/cuda_home_new.html).
- Des logiciels de [traitement du signal ou d'image](http://www.nvidia.com/object/cuda_home_new.html), appliqués à l'imagerie médicale ou au marché de la sécurité. Même l'encodage de films peut désormais profiter de la puissance des GPU : [Badaboom](http://www.nvidia.fr/object/badaboom_fr.html), écrit spécialement pour GPU va extrêmement vite mais le résultat est d'une qualité inférieure à celui de  [TMPGEnc,](http://tmpgenc.pegasys-inc.com/en/product/te4xp.html#tabs) qui va de 2 à 5 fois plus vite lorsque Cuda est activé.

Quel que soit votre utilisation de l'ordinateur, souvenez-vous de faire bien attention au GPU qui équipera votre prochaine machine : ce sera lui qui fera de votre machine un superordinateur de table.

### Liens:

1. [Geeks3d.com](http://www.geeks3d.com/) le site de référence de mon gourou sur ce sujet, JegX
2. [La montée en puissance des GPUs](/2007/11/02/la-montee-en-puissance-des-gpus/)
3. [Loi de Moore toujours](/2008/06/19/moore-toujours/)
4. Damien Triolet, "[Nvidia CUDA : aperçu](http://www.hardware.fr/articles/659-1/nvidia-cuda-apercu.html)", sur hardware.fr 2 Mars 2007
