---
title: "Gyroscopes d'hier et de demain"
slug: "gyroscopes-dhier-et-de-demain"
date: 2010-04-09
categories: 
  - "cat2"
tags: 
  - "aerospace"
  - "mecanique"
  - "optique"
  - "physique"
coverImage: "9a440aa4e1cd0fe13d8938d79cc00f26.jpg"
---

{{< figure src="images/272f90341f7ae9ed80c66342c04f50ee.gif" alt="illustration Wikipedia" caption="illustration Wikipedia" link="http://fr.wikipedia.org/wiki/Gyroscope" width="300" >}}

Mon premier [gyroscope](https://fr.wikipedia.org/wiki/gyroscope) était une simple toupie montée dans une cage articulée : une fois lancée à l'aide d'un bout de ficelle, l'axe de la toupie reste insensible aux mouvements du support de la cage, magique.

L'[horizon artificiel](https://fr.wikipedia.org/wiki/horizon_artificiel)  indispensable aux pilotes n'était initialement qu'une version motorisée de mon jouet d'enfant, mais Foucault ayant démontré qu'un gyroscope mesurait la rotation de la terre encore mieux que son célèbre pendule , les longs vols d'avions et de fusées ont nécessité la mise au point de [centrales à inertie](https://fr.wikipedia.org/wiki/centrale_à_inertie) sophistiquées, groupant 3 gyroscopes perpendiculaires et tous les capteurs nécessaires pour déterminer les angles de roulis, tangage et lacet de l'engin porteur.

{{< figure src="images/236b9a97cce47eaa1b02e7604b569a19.jpg" alt="Plateforme inertielle Litton LN3-2A équipant les chasseurs F-104 à la fin du XXème siècle" caption="Plateforme inertielle Litton LN3-2A équipant les chasseurs F-104 à la fin du XXème siècle" align="aligncenter" width="390" >}}

Le summum de la technologie en la matière a probablement été atteint avec le satellite [Gravity Probe B](https://fr.wikipedia.org/wiki/Gravity_Probe_B) destiné à vérifier un aspect méconnu de la théorie de la Relativité d'Albert, selon lequel un corps massif en rotation "enroule" l'espace autour de lui. Sa plateforme à inertie\[1\] est équipée de 4 sphères de quartz incroyablement précises tournant en lévitation magnétique dans le vide quasi absolu et d'un système de mesure capable de mesurer des rotations de l'ordre du cent-milliardième de degré par heure...  Après plusieurs années de mesure et la prise en compte de nombreux effets qui avaient été négligés initialement, on [commence apparemment](http://einstein.stanford.edu/highlights/status1.html) à vérifier une fois de plus que le grand Einstein a désespérément raison.

Comme souvent en technologie, la révolution est venue d'une approche totalement différente, en l'occurrence l'optique. Prenez une bobine de quelques kilomètres de fibre optique. Injectez-y un faisceau laser aux deux extrémités. Si vous faites tourner la bobine sur son axe, l'un des faisceaux devra parcourir un chemin légèrement supérieur à l'autre, et un interféromètre judicieusement placé entre les deux faisceaux pourra mesurer cet écart proportionnel à la vitesse de rotation. Un tel [gyromètre à fibre optique](https://fr.wikipedia.org/wiki/gyromètre_à_fibre_optique) (gyrolaser pour les intimes) ne contient aucune pièce mobile, est plus robuste et moins coûteux qu'un gyroscope mécanique de haute précision, voire plus précis. Après le F-15, ce sont désormais les Airbus 320 et Boeing 777 qui en sont équipés, mais ces appareils sont encore beaucoup trop volumineux et trop chers pour une application aussi indispensable que la manette de jeu de votre console préférée.

La seconde révolution vient de la technologie MEMS ("Micro Electro-Mechanical System", [microsytème électromécanique](https://fr.wikipedia.org/wiki/microsytème_électromécanique)) comprenez les puces de silicium intégrant des éléments mécaniques. Depuis quelques années on sait réaliser ainsi des accéléromètres, et depuis peu des gyroscopes (ou gyromètres si vous préférez) à [structure vibrante](https://en.wikipedia.org/wiki/vibrating_structure_microscope), basés sur la [force de Coriolis](https://fr.wikipedia.org/wiki/force_de_Coriolis). Il s'agit en fait de ce bon vieux [pendule de Foucault](https://fr.wikipedia.org/wiki/pendule_de_Foucault) miniaturisé et amélioré : on réalise une sorte de diapason en silicium, composé de deux masses oscillant l'une par rapport à l'autre à haute vitesse. En faisant tourner la puce, les deux branches du diapason se tordent sous l'effet de la force de Coriolis et les deux masses n'oscillent plus dans le même plan. On mesure cette déformation par la variation de capacité électrique entre les masses et le support de silicium, et le tour est joué : un gyroscope de quelques millimètres cubes seulement, vendu autour d'un Euro, assez précis pour éviter que les modèles réduits Made in China du futur ne s'écrasent lamentablement par l'inexpérience de votre petit neveu.

{{< figure src="images/0cae1abc834a39e14ec0ab2684f8d57d.jpg" alt="a783e_rcjSTgyros2" caption="Puce du gyroscope 2D de ST Microélectronics, qui vient d'en commercialiser un 3D" link="http://www.st.com/internet/com/support/404.jsp" align="aligncenter" width="400" >}}

### Sources:

1. [The Extraordinary Technologies of GP-B](http://einstein.stanford.edu/TECH/technology1.html)
2. [Gyromètre piezoélectrique VIG de l'ONERA](http://www.onera.fr/dmph/capteurs-inertiels/gyro-vig.php)
3. [MEMS Gyroscopes](http://www.st.com/internet/com/support/404.jsp), excellente présentation complète de STM, en anglais
