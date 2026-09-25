---
title: Comment la cryptographie symétrique fonctionne-t-elle ? Si un disque dur est encodé en utilisant l'encodage symétrique et 10 personnes doivent y avoir accès, est-ce que chacun utilisera le même mot de passe pour l'encodage et le décodage ?
slug: comment-la-cryptographie-symetrique-fonctionne-t-elle
date: '2020-03-26'
draft: true
categories:
- Comment
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Comment-la-cryptographie-sym%C3%A9trique-fonctionne-t-elle-Si-un-disque-dur-est-encod%C3%A9-en-utilisant-l-encodage-sym%C3%A9trique-et-10-personnes-doivent-y-avoir-acc%C3%A8s-est-ce-que-chacun-utilisera-le/answer/Dr-Goulu)*

Oui. La [Cryptographie symétrique](w:) utilise la même clé pour le chiffrement et le déchiffrement, donc toutes les personnes qui accèdent aux informations doivent avoir cette clé.

C'est pour ça qu'on utiliserait en aucun cas cette méthode dans le cas que vous décrivez.

Aujourd'hui toutes les solutions informatiques utilisent la Cryptographie asymétrique, qui permet en plus d'identifier les utilisateurs et de leur donner des droits distincts d'accès en lecture, écriture, modification, effacement.

C'est plus facile que ça en a l'air

[Alice et Bob et les clés asymétriques - Pourquoi Comment Combien](/2017/02/15/alice-et-bob-et-les-cles-asymetriques/)

Dans votre cas, le disque dur pourrait être encrypté symétriquement, mais seul l'ordinateur dans lequel il est aurait la clé et decoderait+reencoderait les informations avec chaque clé publique de chaque utilisateur authentifié.
