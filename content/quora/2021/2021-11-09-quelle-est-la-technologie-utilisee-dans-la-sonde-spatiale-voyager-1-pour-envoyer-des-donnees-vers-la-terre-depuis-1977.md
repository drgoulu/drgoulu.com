---
title: Quelle est la technologie utilisée dans la sonde spatiale Voyager 1 pour envoyer des données vers la Terre depuis 1977 ?
slug: quelle-est-la-technologie-utilisee-dans-la-sonde-spatiale-voyager-1-pour-envoyer-des-donnees-vers-la-terre-depuis-1977
date: '2021-11-09'
draft: false
categories:
- Quora
tags:
- exploration-spatiale
- telecommunications
- voyager-1-sonde-spatiale
- histoire-de-l-astronautique
- transmission-de-donnees
- technologie-spatiale
- voyage-spatial
- sonde-spatiale
- communications-spatiales
- transmission-des-donnees
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Quelle-est-la-technologie-utilis%C3%A9e-dans-la-sonde-spatiale-Voyager-1-pour-envoyer-des-donn%C3%A9es-vers-la-Terre-depuis-1977/answer/Dr-Goulu)*

[Programme Voyager — Wikipédia](w:Programme_Voyager) indique:

> Les communications avec la Terre sont assurées par un émetteur-récepteur radio fonctionnant à la fois en bande S (13 cm) et en bande X (3,6 cm), relié à une [antenne](w:Antenne_radioélectrique) [parabolique](w:Antenne_parabolique) grand gain de 3,66 m de diamètre qui émet avec un angle d'ouverture de 2,3° en bande S et de 0,6° en bande X. Une antenne à faible gain est montée sur la structure portant la parabole et émet dans l'hémisphère centrée sur l'axe de la grande parabole. Le système de télécommunications est doublé pour faire face à une défaillance, Il permet de transmettre les données scientifiques recueillies avec un débit compris entre 4,8 et 115,2 kilobits par seconde en [bande X](w:) et les mesures télémétriques avec un débit de 40 bits par seconde en [bande S](w:). Les instructions du contrôle de mission sur la Terre sont reçues avec un débit de 16 bits par seconde

L'émetteur a une puissance de 23 Watts, sur Terre il faut une des 3 antennes de 70m de diamètre du [Deep Space Network](w:)pour recevoir environ$9 \times 10^{-20} W$, 1000 fois moins que les plus sensibles récepteurs de radio FM[[1]](#PNaLT) .

Les données sont transmises en [Codage Manchester](w:)avec un [Code de Golay](w:)ou [de Reed-Solomon](w:Code_de_Reed-Solomon)combiné avec un [Convolutional code](w:en:Convolutional_code) pour la correction d'erreur[[2]](#VOqiU) [[3]](#ANUBy)

Vous trouverez tous les détails et les schémas dans [[4]](#sTIMi) si vous voulez construire votre propre sonde interplanétaire…

Notes de bas de page

[[1]](#cite-PNaLT)[https://www.allaboutcircuits.com...](https://www.allaboutcircuits.com/news/voyager-mission-anniversary-celebration-long-distance-communications/)

[[2]](#cite-VOqiU)[Did the Voyager spacecraft use a Golay, a Reed-Solomon and/or a Hamming code for data transmission encoding for error correction? (Need clarification)](https://space.stackexchange.com/questions/54055/did-the-voyager-spacecraft-use-a-golay-a-reed-solomon-and-or-a-hamming-code-for)

[[3]](#cite-ANUBy)[https://descanso.jpl.nasa.gov/DP...](https://descanso.jpl.nasa.gov/DPSummary/Descanso4--Voyager_new.pdf)

[[4]](#cite-sTIMi)[https://descanso.jpl.nasa.gov/mo...](https://descanso.jpl.nasa.gov/monograph/series13/DeepCommo_Chapter3--141029.pdf)
