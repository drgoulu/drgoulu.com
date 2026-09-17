---
title: Théoriquement, serait-il possible de localiser un véhicule spatial en utilisant les satellites du système GPS ?
slug: theoriquement-serait-il-possible-de-localiser-un-vehicule-spatial-en-utilisant-les-satellites-du-systeme-gps
date: '2020-03-27'
draft: false
categories:
- Quora
tags:
- exploration-spatiale
- communications-satellite
- systeme-de-coordonnees-geographiques
- navigation-gps
- geolocalisation
- satellites
- technologie-spatiale
- vehicule-spatial
- systeme-de-positionnement-par-satellites
- navigation-satellite
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Th%C3%A9oriquement-serait-il-possible-de-localiser-un-v%C3%A9hicule-spatial-en-utilisant-les-satellites-du-syst%C3%A8me-GPS/answer/Dr-Goulu)*

Les satellites GPS orbitent à 20200 km d'altitude, donc tant qu'on est en dessous, ça marche. C'est même utilisé sur l'ISS pour déterminer l'orientation de la station et pour les rendez-vous spatiaux (voir [Robert Frost's answer to Does GPS work on the ISS?](https://www.quora.com/Does-GPS-work-on-the-ISS/answer/Robert-Frost-1?ch=10&share=648a3146&srid=pzDv) ) , mais il faut des récepteurs spéciaux qui ne soient pas "bridés" pour fonctionner à faible altitude comme les récepteurs grand public.

(Pour comprendre pourquoi, lire [Le GPS pour les nuls : Satellites et Signaux - Pourquoi Comment Combien](https://www.drgoulu.com/2008/09/27/le-gps-pour-les-nuls-satellites-et-signaux/#.Xn4e2ohsOCo) )

Avec des récepteurs spéciaux fonctionnant avec plus de 4 satellites pour éliminer cette contrainte, on peut utiliser le GPS un peu au dessus des orbites. Selon [GPS in Space](https://www.technologyreview.com/s/401315/gps-in-space/) on y arrive au moins jusqu'à l'orbite géostationnaire (36000 km) voire un peu au dessus.

Pour des sondes lointaines, on envisage de plus en plus utiliser un GPS naturel : la [Navigation basée sur des pulsars X](w:).

Selon la page anglophone [X-ray pulsar-based navigation - Wikipedia](w:en:X-ray_pulsar-based_navigation), ça a été testé en 2018 sur l'ISS et donné une précision de 7km. Ca parait beaucoup comme ça mais dites vous que cette précision serait la même dans tout l'espace compris entre une vingtaine de [Pulsars milliseconde](w:Pulsar_milliseconde), des années-lumière cube ! WOW !

(dont on connait donc désormais la position et la vitesse relative de ces pulsars à 7km près ??? faut que je checke ça !)
