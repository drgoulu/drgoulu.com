---
title: "La ChemCam de Curiosity"
slug: "la-chemcam-de-curiosity"
date: 2014-05-26
categories: 
  - "cat2"
tags: 
  - "aerospace"
  - "geologie"
  - "laser"
  - "mars"
coverImage: "chemcamdetail1.png"
---

Vu la photo ci-dessous dans un [article](http://www.universetoday.com/111930/curiosity-says-goodbye-kimberley-after-parting-laser-blasts-and-seeking-new-adventures-ahead/) consacré au [robot "Curiosity" sur Mars](w:Mars_Science_Laboratory). C'est juste un forage sur Mars... Mais qu'est-ce donc que cette ligne de points noirs ? D'après la légende, ils ont été faits par un "rock-zapping laser"... Le mystère s'épaississait, il fallait que je cherche, que je sache.

{{< figure src="images/chemcamdetail1.png" alt="fsdad" caption="trou foré sur Mars par le robot Curiosity et, dans le trou, une ligne de cicatrices produit par son &quot;rock-zapping laser&quot;. ∅ trou 16 mm environ (détail d'une image NASA, cliquer pour l'image complète)" link="http://mars.jpl.nasa.gov/msl-raw-images/msss/00629/mhli/0629MH0004130000203715R00_DXXX.jpg" align="aligncenter" width="600" >}}

En fait il s'agit de traces de mesures faites par la [ChemCam](http://www.msl-chemcam.com/), un dispositif digne d'un Maître Jedi : un laser vaporise la matière, et un spectromètre analyse la lumière émise par le plasma pour en déterminer les constituants. Ca s'appelle [Spectroscopie sur plasma induit par laser](w:) ou "LIBS" en anglais.

{{< figure src="images/1abe58b8b2e2ccecfd1857cf25c310fe.png" alt="Vois-tu, jeune padawan, d'après la couleur, cette porte est en titane-béryllium..." caption="Vois-tu, jeune padawan, d'après la couleur, cette porte est en titane-béryllium..." align="aligncenter" width="599" >}}

C'est même plus fort qu'un Maître Jedi, car la ChemCam fonctionne jusqu'à 9 mètres de distance ! Et en utilisant une série de courtes impulsions, elle peut commencer par "nettoyer" la surface à analyser de la poussière ou de l'oxydation de surface pour atteindre la roche proprement dite.

{{< youtube id="fEZ5dEi4oPo" >}}

Concrètement, la partie optique de la ChemCam se trouve dans le mât qui domine le robot, juste à côté de la caméra "[Mastcam](http://www.msss.com/all_projects/msl-mastcam.php)" qui lui sert de viseur, alors que les spectromètres sont dans le corps du robot :

{{< figure src="images/9c909a3b0b88957c07817f3e87c0e9e3.jpg" alt="Diagramme bloc de l'instrument ChemCam. Credit: ChemCam/LANL/IRAP/CNES" caption="Diagramme bloc de l'instrument ChemCam. Credit: ChemCam/LANL/IRAP/CNES" link="http://www.msl-chemcam.com/index.php?menu=inc&page_consult=textes&rubrique=64&sousrubrique=224&soussousrubrique=0&art=259&titre_url=ChemCam%20-%20How%20does%20ChemCam%20work?&step=2#.U4G0h_n90wA" align="aligncenter" width="575" >}}

La ChemCam a été en partie conçue et réalisée par des équipes françaises (bravo les voisins, cocorico! [[1]](#ref-1)) notamment le laser qui a été développé par Thalès. Ce laser produit des impulsions très courtes de 8 nanosecondes environ, et d'une énergie de 30 milliJoule seulement [[2]](#ref-2). C'est très très faible. Mais 30 \[mJ\] / 8 \[ns\] ça fait dans les 3.75 MW de puissance ! ( J'ai [vérifié le calcul](http://www.wolframalpha.com/input/?i=30+mJ%2F8+ns+in+watt) pour être sur ...) Comme il faut environ 1GW/cm² pour créer le plasma de roche, le "rock-zapping" laser ne zappe qu'un tiers de mm² environ, mais ça suffit pour le spectromètre.

_(ajout du 27.5.14)_ En 8 nanosecondes, la lumière ne parcourt que 2.4 mètres ! Le laser est déjà "éteint" lorsque la lumière atteint un rocher à 8m de Curiosity. L'impulsion ressemble donc plus à un tir de pistolet laser qu'à un coup de sabre.

La ChemCam fonctionne très bien, elle a vaporisé son 100'000ème morceau de roche lunaire martienne (!) en novembre 2013 [[3]](#ref-3) dont je ne sais pas combien dans des trous perçés par la [foreuse PADS.](http://msl-scicorner.jpl.nasa.gov/samplingsystem/) Comme l'indique Sylvestre Maurice du CNES de l'[IRAP](http://www.irap.omp.eu/), un des concepteurs de la ChemCam [[4]](#ref-4), ça permet de faire des statistiques plutôt que de se satisfaire de quelques mesures ponctuelles.

Voilà, ma curiosité est satisfaite pour quelques heures...

### Références:

1. <span id="ref-1"></span>"[Le robot Curiosity embarque deux instruments français](http://www.lefigaro.fr/sciences/2011/11/24/01008-20111124ARTFIG00761-la-sonde-curiosity-embarque-deux-instruments-francais.php)", 2011, le Figaro
2. <span id="ref-2"></span>S. Maurice et al. "The ChemCam Instrument Suite on the Mars Science Laboratory (MSL) Rover: Science Objectives and Mast Unit Description" , 2012, Space Science Reviews, Volume 170, Issue 1-4, pp 95-166 [pdf](https://www.researchgate.net/profile/David_Baratoux/publication/257664696_The_ChemCam_Instrument_Suite_on_the_Mars_Science_Laboratory_%28MSL%29_Rover_Science_Objectives_and_Mast_Unit_Description/file/50463526ee47fa6a2b.pdf) 61 pages avec la description très complète!
3. <span id="ref-3"></span>"[100'000ème tir du laser ChemCam sur Mars](https://www.thalesgroup.com/fr/worldwide/securite/event/100000th-firing-chemcam-laser-mars)", novembre 2013, Thalès
4. <span id="ref-4"></span>interview [vidéo](https://www.youtube.com/watch?v=ZxFXCpaA7Lo) de Sylvestre Maurice de l'IRAP
