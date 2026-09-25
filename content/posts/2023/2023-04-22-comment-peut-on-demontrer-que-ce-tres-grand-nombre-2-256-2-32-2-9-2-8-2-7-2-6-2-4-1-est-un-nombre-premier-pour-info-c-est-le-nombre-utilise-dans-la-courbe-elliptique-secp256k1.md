---
title: Comment peut-on démontrer que ce très grand nombre 2^256 - 2^32 - 2^9 - 2^8 - 2^7 - 2^6 - 2^4 - 1 est un nombre premier ? (Pour info c'est le nombre utilisé dans la courbe elliptique secp256k1)
slug: comment-peut-on-demontrer-que-ce-tres-grand-nombre-2-256-2-32-2-9-2-8-2-7-2-6-2-4-1-est-un-nombre-premier-pour-info-c-est-le-nombre-utilise-dans-la-courbe-elliptique-secp256k1
date: '2023-04-22'
draft: false
categories:
- Comment
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Comment-peut-on-d%C3%A9montrer-que-ce-tr%C3%A8s-grand-nombre-2-256-2-32-2-9-2-8-2-7-2-6-2-4-1-est-un-nombre-premier-Pour-info-cest-le-nombre-utilis%C3%A9-dans-la-courbe-elliptique-secp256k1/answer/Dr-Goulu)*

On demande à [Wolfram|Alpha : is 2^](https://www.wolframalpha.com/input?i=is++2^256+-+2^32+-+2^9+-+2^8+-+2^7+-+2^6+-+2^4+-+1+prime)256[- 2^32 - 2^9 - 2^8 - 2^7 - 2^6 - 2^4 - 1 prime](https://www.wolframalpha.com/input?i=is++2^256+-+2^32+-+2^9+-+2^8+-+2^7+-+2^6+-+2^4+-+1+prime)?

et il répond que oui, donc c'est un nombre premier.

ça utilise le [Test de primalité de Miller-Rabin](w:)qui est probabiliste, mais la probabilité que le test donne un faux positif est inférieure à la probabilité que vous ou un ordinateur se trompe pendant les longs calculs d'un test déterministe.

Oui, un ordinateur peut se tromper si un rayon cosmique passe au mauvais moment par le mauvais bit. La probabilité est faible, mais multipliée par des centaines d'heures de calcul (estimation pour un nombre de 256 bits) n'est pas nulle.
