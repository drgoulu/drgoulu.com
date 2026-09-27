---
title: Qui peut m'expliquer comment les plateformes comme Netflix et autres peuvent délivrer simultanément autant de vidéo à autant d'utilisateurs ? Quel shardwares et logiciels utilisent t ils ?
date: 2025-11-21
draft: false
tags:
  - informatique
  - technologies
  - contenu
  - infrastructures
  - plateforme
categories:
  - Comment
slug: qui-peut-m-expliquer-comment-les-plateformes-comme-netflix-et-autres-peuvent-delivrer-simultanement-autant-de-video-a-autant-d-utilisateurs-quel-shardwares-et-logiciels-utilisent-t-ils
coverImage: ./images/quora.png
---

_Réponse publiée_ [_sur Quora_](https://fr.quora.com/Qui-peut-mexpliquer-comment-les-plateformes-comme-Netflix-et-autres-peuvent-d%C3%A9livrer-simultan%C3%A9ment-autant-de-vid%C3%A9o-%C3%A0-autant-dutilisateurs-Quel-shardwares-et-logiciels-utilisent-t-ils/answer/Dr-Goulu)

Le blog technique de Netflix est passionnant si vous vous intéressez à ces questions

[https://netflixtechblog.com/](https://netflixtechblog.com/)

Une partie de leur code source est public, régalez-vous

[GitHub - Netflix, Inc.](https://github.com/Netflix)

Mais l'essentiel est dans leurs brevets :

[https://patents.justia.com/assig...](https://patents.justia.com/assignee/netflix-inc)

En gros, ils ont leur propre [CDN](w:Réseau_de_diffusion_de_contenu) appelé [Open Connect](w:en:Open_Connect)et installé chez les principaux FAI. Ils uploadent le contenu à l'avance en fonction des prédictions faites sur l'utilisation des clients locaux.

A part ça leurs films sont remarquablement comprimés comme vous pouvez vous en apercevoir en téléchargeant des films pour visionnage offline…

En passant, je vous recommande la série "the playlist" qui montre, entre autres, comment Spotify a résolu un problème similaire, très différemment. La série est sur Netflix ;-)
