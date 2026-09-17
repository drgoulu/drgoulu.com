---
title: Que feriez-vous si vous inventiez un algorithme capable de factoriser n'importe quel nombre semi-premier quasi-instantanément ?
slug: que-feriez-vous-si-vous-inventiez-un-algorithme-capable-de-factoriser-n-importe-quel-nombre-semi-premier-quasi-instantanement
date: '2022-02-08'
draft: false
categories:
- Quora
tags:
- informatique
- mathematiques
- cryptanalyse
- securite-informatique
- algorithmes
- factorisation-mathematiques
- science-de-l-informatique
- cryptographie
- securite-des-donnees
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Que-feriez-vous-si-vous-inventiez-un-algorithme-capable-de-factoriser-nimporte-quel-nombre-semi-premier-quasi-instantan%C3%A9ment/answer/Dr-Goulu)*

Je le publierais car ce serait la célébrité immédiate et une avancée majeure dans le [Problème P ≟ NP](w:)(même si la factorisation n'a pas formellement été établie comme étant un problème NP)

Comme indiqué par [Olivier Galand dans sa réponse](https://fr.quora.com/Que-feriez-vous-si-vous-inventiez-un-algorithme-capable-de-factoriser-nimporte-quel-nombre-semi-premier-quasi-instantan%C3%A9ment/answer/Olivier-Galand), ça aurait des conséquences quasi immédiates en cryptographie, mais pas autant qu'on l'imagine car :

1. le [Chiffrement RSA](w:)n'est pas si généralisé que ça. En fait on l'utilise surtout pour l'échange de clés symétriques, que l'on peut désormais faire autrement (voir plus bas)
2. L'industrie s'attend à ce que ce soit possible dans quelques années grâce aux ordinateurs quantiques. Il y a donc une recherche importante en [Cryptographie post-quantique](w:) et des alternatives à RSA comme [NTRUEncrypt](w:)sont déjà disponibles (et peut-être utilisées, je ne sais pas)

Pour la petite histoire, J'ai assisté à une présentation d'IBM sur l'informatique quantique aux alumni informaticiens EPFL, et quand le type a dit "la factorisation quantique ce sera dans 5 à 10 ans selon nos estimations, donc dans la prescription légale…" il y a eu un silence de mort chez mes collègues banquiers qui se tortillaient sur leurs chaises : toute entité (NSA, IRS ou autre) qui aurait eu l'idée saugrenue de stocker des messages cryptés pourra les décrypter et intenter des actions en justice avant qu'il y ait prescription… Je ne serais donc pas étonné que nos amis banquiers passent au post-quantique encore plus vite que les militaires.
