---
title: "Avalanches et goniomètre à infrasons"
date: 2016-01-14
categories: 
  - "cat3"
  - "cat2"
tags: 
  - "acoustique"
  - "informatique"
---

Dans la liste ["Réalisations" de mon CV](http://www.philippe-guglielmetti.com/cv/jobs/liste_0) se trouve une ligne "Téléopération d’un goniomètre à infrasons" sur laquelle je ne pouvais pas être très bavard car il s'agissait d'un projet militaire top secret m'avait-on dit. Mais maintenant que je trouve des informations publiques [[1]](#ref-1), [[2]](#ref-2) sur le net concernant cette réalisation étonnante (à laquelle je n'ai contribué que 3 semaines ), j'ose en dire un peu plus.

Selon [[1]](#ref-1) l'histoire a commencé par le projet militaire, mais à ce qu'on m'avait dit, ce sont plutôt des recherches sur les avalanches qui  ont lancé le projet militaire. L'idée d'un chercheur au [LEMA de l'EPFL](http://lema.epfl.ch/) était de détecter des avalanches, voire d'avertir de leur imminence en mesurant les infrasons provoqués par le tassement ou la rupture du manteau neigeux. Mais il s'est rapidement aperçu que ses mesures d'infrasons en altitude étaient polluées par beaucoup de bruits parasites : bang supersoniques, explosions, hélicoptères ...

"Hélicoptères ? Votre microphone à infrasons entend des hélicoptères volant dans les vallées alpines, sous les radars ?" Ni une ni deux, l'armée suisse finance le projet et construit un système de mesure baptisé "Peiler", composé de plusieurs micros espacés de quelques dizaines de mètres près des pistes d' [Anzère](https://fr.wikipedia.org/wiki/Anzère). En mesurant le décalage temporel ([déphasage](https://fr.wikipedia.org/wiki/déphasage)) des sons captés, un logiciel de traitement des signaux ( en [LabView](https://fr.wikipedia.org/wiki/LabView), mon [langage de prédilection à l'époque](http://drgoulu.local/2010/12/03/les-decorateurs-python) ) pouvait déterminer la direction de la source.

Par exemple dans le [spectrogramme](https://fr.wikipedia.org/wiki/spectrogramme) ci-dessous un œil entraîné ou un logiciel bien foutu peut distinguer:

1. Un hélicoptère Lama ou Alouette à turbine, dont les pales génèrent du 17.5 Hz, avec un [effet Doppler](https://fr.wikipedia.org/wiki/effet_Doppler) visible quand l'hélicoptère se déplace
2. Un autre hélicoptère, stationnaire.
3. Une série d'explosions à 15h14m35s, azimut 239°, 15h16m28s, azimut 264°, et d'autres explosions à 15h12m10s,15h14m12s, 15h15m09s.
4. Une avalanche tout de même à 15h16m36s, durant environ 1min46s.

{{< figure src="images/histogramme.jpg" alt="source : Arfang (1)" caption="source : Arfang (1)" link="http://www.arfang.com/index.php?nav=home&lang=fr" align="aligncenter" width="762" >}}

Les azimuts ne sont pas très précis car le vent dévie les sons, mais on peut partiellement en tenir compte avec des données météo.

Pour déterminer la distance, et donc la position de la source, c'est plus compliqué car il faudrait tenir compte de l'atténuation du son une fois qu'on en connait l'origine. A l'époque où j'ai effectué mon service militaire on détectait certaines explosions tous les jours aux même heures, et à peu près au même azimut. On s'est aperçus que c'étaient les bang supersoniques du Concorde qui partait d'Orly pour Rio de Janeiro ! Mais comme les sons mettent une demi heure pour faire les 600 km de Paris au Valais, les militaires ne pouvaient pas faire autre chose que juste compter des bangs supersoniques de pratiquement tous les vols militaires en Europe... Ce système captait à l'époque des bruits diffus et mal localisés arrivant de l'Est en quasi permanence. Finalement on a compris qu'ils provenaient du [siège de Sarjevo](https://fr.wikipedia.org/wiki/siège_de_Sarjevo), à plus de 1000 km...

Il faut dire qu'à l'altitude en question (2300m), l'atmosphère se comporte un peu comme un [guide d'onde](https://fr.wikipedia.org/wiki/guide_d'onde) : les sons émis plus haut et plus bas se concentrent et se propagent bien à cette altitude. La même chose se produit dans la mer autour de 900m de profondeur [[3]](#ref-3), où on place des dispositifs d'écoute de sous-marins probablement très similaires au "Peiler".

La technologie d'aujourd'hui a permis le développement de l'application civile de détection des avalanches [[1]](#ref-1), et c'est tant mieux. Pour moi ce projet avait été l'occasion de découvrir un peu l'acoustique, mais j'y repense surtout lorsqu'on parle de recherche militaire, ou de financement de recherches par l'armée.

Souvent une même découverte débouche à la fois  sur des applications civiles et militaires. Vouloir empêcher l'application militaire, c'est parfois retarder, voire condamner l'application civile car c'est un fait : les militaires ont du soutien politique, et beaucoup d'argent qu'ils sont prêts à investir très en amont, en prenant beaucoup de risques. Ils ne veulent pas forcément bloquer l'application civile ni même un retour sur investissement, ils veulent juste être les premiers à utiliser la technologie. Si ça ne concerne pas directement des armes ou ne soulève pas de gros problème éthique, pourquoi se priver d'un financement somme toute tout aussi étatique que les fonds pour la recherche nationale ?

### Références:

1. <span id="ref-1"></span>[Arfang Infrasonic Avalanche Monitoring](http://www.arfang.com/index.php?nav=home&lang=fr) , site web de la solution commerciale
2. <span id="ref-2"></span>Chritin, V., & Rossi, M. (1995). "[Détection acoustique des avalanches Site La Sionne-Anzère Valais](http://www.iav.ch/ref/detection-acoustique-avalanches-IGS95.pdf)". Symposium International Sciences et Montagne, Les Apports Scientifiques à La Sécurité Neige, Glace et Avalanches.  http://infoscience.epfl.ch/record/96418
3. <span id="ref-3"></span>Olivier Le Calvé "[Le son dans la mer](http://lecalve.univ-tln.fr/oceano/fiches/fiche3F.htm)"
4. <span id="ref-4"></span>{{< altmetric doi="10.1117/12.2241095" float="right" >}}Chritin, V., Van Lancker, E., Wellig, P., & Ott, B. (2016). High infrasonic goniometry applied to the detection of a helicopter in a high activity environment. In SPIE International Society for Optics and Photonics SECURITY + DEFENCE Conference (Vol. 10, p. 999703). Edinburgh, United Kingdom: SPIE International Society for Optics and Photonics. DOI>[10.1117/12.2241095](https://doi.org/10.1117/12.2241095)
