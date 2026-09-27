---

title: Le test de primalité de Miller-Rabin permet de prédire avec une forte probabilité qu'un grand nombre est premier, existe-t-il des tests du même genre pour savoir si un nombre est produit de deux nombres premiers (grands) et lesquels ?
slug: le-test-de-primalite-de-miller-rabin-permet-de-predire-avec-une-forte-probabilite-qu-un-grand-nombre-est-premier-existe-t-il-des-tests-du-meme-genre-pour-savoir-si-un-nombre-est-produit-de-deux-nombres-premiers-grands-et-lesquels
date: '2022-04-17'
draft: true
categories:
- Quora
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Le-test-de-primalit%C3%A9-de-Miller-Rabin-permet-de-pr%C3%A9dire-avec-une-forte-probabilit%C3%A9-qu-un-grand-nombre-est-premier-existe-t-il-des-tests-du-m%C3%AAme-genre-pour-savoir-si-un-nombre-est-produit/answer/Dr-Goulu)*

Un test répond oui ou non.

Si un test de primalité (Miller Rabin, AKS ou autre) répond non, alors votre nombre est le produit d'au moins 2 nombres premiers, grands ou petits.

Mais savoir lesquels demande plus un simple test, il vous faut un algorithme de factorisation, ou [Décomposition en produit de facteurs premiers](w:).

Le plus simple consiste à essayer les divisions par les nombres premiers successifs, de ce point de vue on peut dire que la factorisation demande de très nombreux tests.

C'est le principe de l'utilisation des nombres premiers en cryptographie : il est facile de créer une clé en multipliant deux grands nombres premiers , mais extrêmement difficile de retrouver ces deux nombres à partir de la clé.
