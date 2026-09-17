---
title: Pourquoi est-il nécessaire d'avoir un quatrième satellite pour la synchronisation de l'horloge du boitier GPS ? La synchronisation pourrait-elle être réalisée à partir d'un des trois autres satellites (éliminant donc le besoin du quatrième)?
slug: pourquoi-est-il-necessaire-d-avoir-un-quatrieme-satellite-pour-la-synchronisation-de-l-horloge-du-boitier-gps
date: '2022-11-12'
draft: false
categories:
- Pourquoi
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Pourquoi-est-il-n%C3%A9cessaire-d-avoir-un-quatri%C3%A8me-satellite-pour-la-synchronisation-de-l-horloge-du-boitier-GPS-La-synchronisation-pourrait-elle-%C3%AAtre-r%C3%A9alis%C3%A9e-%C3%A0-partir-d-un-des-trois/answer/Dr-Goulu)*

Comme votre récepteur GPS ne dispose pas d'une horloge atomique, il ne peut que mesurer le décalage temporel relatif entre les signaux qu'il reçoit de N satellites.

Avec N=3, il y a beaucoup de points qui correspondent à 3 déphasages de signaux : les intersections de 3 ensembles de sphères en pelures d'oignon, correspondant à la période des signaux GPS. C'est même plus compliqué que ça car les satellites bougent vite…

Si vous pouvez fixer une coordonnée, par exemple altitude=0 si vous êtes en mer, ça peut encore marcher.

Mais si vous voulez 3 coordonnés spatiales, vous ne pouvez vous en sortir qu'en déterminant aussi la 4ème coordonnée d'un événement dans l'espace-temps : le temps.

4 inconnues impliquent 4 équations (ou plus pour minimiser les erreurs)

[https://www.drgoulu.com/2008/09/...](https://www.drgoulu.com/2008/09/27/le-gps-pour-les-nuls-satellites-et-signaux/#.Y3AQ96Tfs0E)
