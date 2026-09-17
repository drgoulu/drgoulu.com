---
title: Est-il possible de rendre un site web impiratable aux attaques des pirates informatique ?
slug: est-il-possible-de-rendre-un-site-web-impiratable-aux-attaques-des-pirates-informatique
date: '2022-10-20'
draft: false
categories:
- Quora
tags:
- securite-informatique
- cybercriminalite
- securite-sur-internet
- vulnerabilite
- cyberattaques
- piratage-informatique
- cybersecurite
- securite-des-systemes-informatiques
- piratage-informatique-securite
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Est-il-possible-de-rendre-un-site-web-impiratable-aux-attaques-des-pirates-informatique/answer/Dr-Goulu)*

L'héberger sur un serveur auquel on a un accès physique pour les mises à jour et ne laisser aucun accès réseau en fermant tous les ports sauf le 80.

Ne pas faire de console d'administration du site par le web, ne pas faire de compte ayant des droits particuliers, faire une page 404 sans aucune info techniques pour toute requête non autorisée.

Idéalement, faire un site statique.

Faire un site inintéressant pour les pirates. (sous-traiter le e-commerce, pas de données personnelles stockées etc)

Les pirates pourront toujours faire des attaques DoS, mais elles coûtent cher donc elles ne se font pas contre des sites mineurs.
