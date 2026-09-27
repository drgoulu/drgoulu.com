---
title: La recherche exacte (non approximative) des n plus proches voisins dans des espaces à grandes dimensions (>100) restera-t-elle toujours résolue pas mieux qu'en temps linéaire (par énumération exhaustive)?
slug: la-recherche-exacte-non-approximative-des-n-plus-proches-voisins-dans-des-espaces-a-grandes-dimensions-100-restera-t-elle-toujours-resolue-pas-mieux-qu-en-temps-lineaire-par
date: '2021-02-16'
draft: true
categories:
- Quora
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/La-recherche-exacte-non-approximative-des-n-plus-proches-voisins-dans-des-espaces-%C3%A0-grandes-dimensions-100-restera-t-elle-toujours-r%C3%A9solue-pas-mieux-qu-en-temps-lin%C3%A9aire-par-%C3%A9num%C3%A9ration/answer/Dr-Goulu)*

le nombre de dimensions ou même la topologie ne change rien à la complexité, vous devez de toutes façons évaluer des normes.

Si vous n'avez pas stocké vos N points dans une structure futée comme un [R-arbre](w:), vous allez devoir traverser tous vos points, oui.

Avec un R-arbre, il suffira de tester les n-1 autres points du sous-espace auquel appartient un point donné.
