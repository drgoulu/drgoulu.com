---
title: Dynamique des (méta) machines
slug: dynamique-des-meta-machines
date: '2012-11-25'
tags:
- production
draft: true
coverImage: "image00-199x300.jpg"
---
Pour une fois, je vais vous parler un peu de mon boulot. Et vous expliquer pourquoi, après une  [thèse en robotique](http://library.epfl.ch/theses/?nr=1228) et quelques années passées à développer des commandes de machines industrielles de plus en plus productives, j'en suis arrivé à m'intéresser à la production de ces machines, domaine souvent ignoré voire méprisé par mes collègues du "R&D"\*.  Pourtant une usine de production de machines peut être vue comme une "métamachine" dont la productivité peut être améliorée en lui appliquant des principes et méthodes connus pour la "[régulation](w:)" des machines et autres [systèmes dynamiques](w:Système_dynamique).

{{< figure src="images/image00-199x300.jpg" alt="image00" caption="système non holonome très dynamique" link="/wp-content/uploads/2012/11/image00.jpg" width="199" >}}

Je me suis tout à coup aperçu que ma première activité chez Bobst, à savoir le développement du “Power Aligner” (PA) d’Asitrade, permettait d’expliquer ou de rafraîchir un certain nombre de notions sur les systèmes dynamiques seront utiles pour comprendre la nécessité d’un APS.

Le PA est un dispositif assez proche du “Power Register” (PR) tant par la fonction que par la technologie : il corrige la position de feuilles arrivant en nappe, mais contrairement au PR, les feuilles ne s’arrêtent jamais. Le PA les accélère pour amener leur bord frontal à un point précis et à une vitesse précise où elles sont contre-collées bord à bord sur les cannelures d’une feuille d’ondulé simple face. Le mécanisme utilisé est ingénieux : il est composé de deux rouleaux qui peuvent entraîner la feuille à des vitesses différentes à gauche et à droite, ce qui permet ainsi de faire tourner la feuille pour l’aligner un peu à la façon d’un “Gyrobox” asservi.

Au moment où j’ai rejoint l’équipe projet, elle butait sur plusieurs problèmes dont celui-ci:

- comment coordonner l’action simultanée de plusieurs moteurs ? Ce problème posé le PA va plus loin que l’habituelle synchronisation de mouvements séquentiels car sa conception introduit des couplages entre mouvements. Par exemple lorsqu’une feuille n’est pas alignée, son bord latéral va se décaler pendant le roulement.

Un tel système dans lequel plusieurs entrées ont des effets combinés sur plusieurs sorties est dit multivariable. La [représentation d’état](w:Représentation_d'état) qui permet de les décrire présente plusieurs similarités avec la [représentation matricielle des graphes](w:Théorie_des_graphes#Graphes_et_alg.C3.A8bre_lin.C3.A9aire) utilisée en  [recherche opérationnelle](w:).

Un autre problème plus délicat encore était lié au premier :

- comment combiner les mouvements de correction avec l’accélération? L’idée initiale était de réaliser ces mouvements en séquence, mais on ne voyait pas comment le faire sans arrêter la feuille entre chaque mouvement.

J’ai alors réalisé que les ingénieurs de l’équipe n’étaient pas des handicapés, sinon ils auraient vu que leur système est semblable à une chaise roulante ! En effet, en manoeuvrant les deux roues indépendemment, un handicapé peut se déplacer par exemple sur un terrain de tennis pour se retrouver au bon endroit au bon moment pour frapper la balle:

Un tel système est dit “[non-holonome](w:en:Nonholonomic_system)” : il y a moins d’entrées (2 moteurs) que de sorties, ici les 3 “degrés de liberté” de la feuille (X, Y et rotation θ).

La différence provient d’une contrainte : la roue ne permet pas de se déplacer perpendiculairement au véhicule. Et pour tenir compte de cette contrainte, tout conducteur de véhicule à roues sait qu’il doit planifier une trajectoire compatible avec les contraintes car l’ordre des commandes au véhicule est important : si on avance de 10m puis qu’on tourne à droite de 30°, on n’arrive pas au même endroit que si on commence par tourner de 30°, puis qu’on avance de 10m. Ensuite, “il suffit de” suivre la trajectoire en la corrigeant en fonction des écarts que l’on observe.

Cependant, les roues de l’AP sont pilotées par un paraplégique aveugle. En effet, les capteurs ne mesurent la position de la feuille à corriger qu’une seule fois, à un instant précis du début cycle. C’était un autre problème :

- Comment piloter la trajectoire de correction de la feuille en  (X, Y, θ) en utilisant seulement les informations fournies par les 2 encodeurs des moteurs ?

La solution a été d’utiliser un “[observateur d’état”](w:Observateur_d'état). Le principe est simple : on simule le système en temps réel en intégrant les données à notre disposition (les mesures de départ des capteurs, puis celles fournies en continu par les encodeurs) de façon à reconstruire celles qui nous manquent (X, Y, θ) pour la régulation.

Références:

1. {{< openbook booknumber="ISBN:9780072824032" templatenumber="5" >}}
2. Philippe Guglielmetti, Michel Siegenthaler, Thomas Mayer, Alex Mann "[Method for manufacturing a multi-layer composite, arrangement for positioning a sheet-like element onto a backing in a laminating unit and laminating unit](https://data.epo.org/publication-server/getpdf.jsp?pn=2305463&ki=A1&cc=EP)" 2011, Patent EP 2 305 463 A1
3. - Publié le 4 avril 2011
    
    Inventeurs :
