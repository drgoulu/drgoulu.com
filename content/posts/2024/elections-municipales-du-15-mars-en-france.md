---
title: 'Elections municipales du 15 mars en France : au 21ème siècle, n''y a-t-il pas un autre moyen d''organiser des élections municipales, je pense notamment à un vote par internet validé par des empreintes ou une reconnaissance faciale ?'
slug: elections-municipales-du-15-mars-en-france
date: '2024-08-13'
draft: false
categories:
- Quora
tags:
- france
- systeme
- innovation-technologique
- vote
- democratie-participative
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Elections-municipales-du-15-mars-en-France-au-21%C3%A8me-si%C3%A8cle-ny-a-t-il-pas-un-autre-moyen-dorganiser-des-%C3%A9lections-municipales-je-pense-notamment-%C3%A0-un-vote-par-internet-valid%C3%A9-par-des/answer/Dr-Goulu)*

Pas d'accord avec [Moussa Chikhi](https://fr.quora.com/profile/Moussa-Chikhi).

J'ai œuvré quelques années en tant qu'expert en informatique pour la commission électorale du canton de Genève qui a utilisé un système de vote par internet pendant plusieurs années.

Il a hélas été abandonné pour des raisons de coût, parce que la loi obligeait à envoyer à chaque citoyen une carte de vote lui permettant de voter soit :

- À l'urne
- Par correspondance
- Par internet, avec des identifiants uniques (zone à gratter, carnet de codes permettant la vérifiabilité)

Le principe était calqué sur celui du vote par correspondance, la mise en enveloppe correspondant à un chiffrement.

- La clé privée permettant le déchiffrement des votes était détenue pour moitié par deux membres de la commission.
- Les votes étaient chiffrés avec la clé publique correspondante.
- Et surchiffrés avec l'identité de l'électeur
- Ceci lui permettait de vérifier que son vote avait bien été reçu et non modifié. Cette possibilité qui n'existe pas avec les votes papier avait été imposée politiquement, ce qui avait causé le surcout fatal
- A la réception, on avait donc l'identité de l'électeur en clair pour pouvoir vérifier qu'il ne votait pas une seconde fois par correspondance ou à l'urne, mais son vote était encrypté pour le secret du vote.
- Au moment du dépouillement, les votes chiffrés étaient brassés avec un générateur [ID Quantique](w:en:ID_Quantique)(un peu de pub…) puis déchiffrés et comptés.

A mon humble avis, ce système était au moins aussi sur que le vote par correspondance (dépouillé par des machines à lecture optique) et beaucoup plus que les votes à l'urne.

D'ailleurs nous avons du une fois procéder à un second dépouillement ce qui a permis de vérifier le taux d'erreur de chaque canal :

- 0% pour le vote par internet, heureusement …
- Environ 1/10000 pour les lecteurs optiques du vote par correspondance. Pour la petite histoire, même les membres de la commission jvont eu du mal à déterminer l'intention des votants sur les cartes lues de manière différente aux deux passages…
- Près de 1% aux votes à l'urne. Une commune avait notamment inversé le nombre de oui et de non…

J'ajouterais que le vote par internet permet plein de vérifications et de systèmes de détection de fraude sans équivalent papier.

J'avais pondu ça à l'époque :

[https://fr.slideshare.net/Goulu/...](https://fr.slideshare.net/Goulu/indicateurs-statistiques-de-fraude-lectorale)

A mon avis, le risque de fraude individuelle était anecdotique (on sait que certains votants votent par correspondance avec le matériel de leurs proches qui s'abstiennent), mais le risque d'un sabotage par intrusion était un peu sous estimé.

A la commission électorale siégeait aussi un temps Alexis Roussel, qui était président du parti pirate Suisse et avait notamment demandé et obtenu que le code soit mis en open source[[1]](#AfrQO) . Il est aussi grand connaisseur des blockchains et avait fait un peti proto de système de vote basé sur la plate-forme Ethereum très convaincant. [[2]](#PkrZj) [[3]](#FUJot)

Mais je le mentionne ici pour une autre raison : il est binational français et suisse, et nous avait éclairé sur des différences culturelles.

En Suisse on vote 4 fois par année sur une douzaine de référendums, donc on souhaite un processus simple, et on fait confiance aux organes chargés du dépouillement. Et comme la politique se discute sur la place publique de la démocratie directe, le secret du vote n'est pas perçu comme aussi important qu'en France.

La réponse de Moussa Chikhi le montre bien : le vote en France est basé sur la méfiance, pas sur la confiance.

Donc oui, le vote par internet est tout à fait techniquement possible, d'ailleurs la Suisse continue dans cette voie avec un autre système[[4]](#JVdaq)[[5]](#piZGb) (pas open source, ni blockchain hélas…), mais ça ne pourra marcher en France ou ailleurs qu'en ayant confiance dans le processus de dépouillement.

Notes de bas de page

[[1]](#cite-AfrQO)[GitHub - republique-et-canton-de-geneve/chvote-1-0: The Geneva electronic vote system, version 1.](https://github.com/republique-et-canton-de-geneve/chvote-1-0)

[[2]](#cite-PkrZj)[Secure Voting Website Using Ethereum and Smart Contracts](https://web.archive.org/web/20240916084150/https://www.mdpi.com/2571-5577/6/4/70)

[[3]](#cite-FUJot)[GitHub - Krish-Depani/Decentralized-Voting-System: A decentralized voting system using Ethereum blockchain for secure and transparent elections, with features like user authentication and real-time result tracking.](https://github.com/Krish-Depani/Decentralized-Voting-System)

[[4]](#cite-JVdaq)[Vote électronique](https://www.ch.ch/fr/votations-et-elections/vote-electronique/#informations-complementaires)

[[5]](#cite-piZGb)[Vote électronique | La Poste](https://digital-solutions.post.ch/fr/e-government/solutions-numerisation/vote-electronique)
