---
title: Un Python écrit en C++ moderne serait-il plus performant et sécurisé que l'actuel Python écrit en C ?
slug: un-python-ecrit-en-c-moderne-serait-il-plus-performant-et-securise-que-l-actuel-python-ecrit-en-c
date: '2020-09-25'
draft: false
categories:
- Quora
tags:
- theorie
- informatique
- programmation
- securite
- langage
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Un-Python-%C3%A9crit-en-C-moderne-serait-il-plus-performant-et-s%C3%A9curis%C3%A9-que-lactuel-Python-%C3%A9crit-en-C/answer/Dr-Goulu)*

Non. Regardez le code de [cpython](https://github.com/python/cpython) et trouvez une seule fonction qui serait plus performante en C++. Et si vous la trouvez, alors on peut aussi la rendre encore plus performante en C …

Et pour "sécurisé", qu'entendez-vous par là ? Ce code a été "sécurisé" par des dizaines d'années de développement d'une grande communauté de développeurs, il est testé en continu sur une douzaine de plateformes …

Franchement j'aime beaucoup plus C++ que C, il offre un niveau d'abstraction bien supérieur, et on arrive plus vite à du code qui marche, je suis d'accord.

Mais une fois qu'on a du code qui marche, débogué et optimisé depuis 30 ans , on a rien à gagner à le réécrire dans un autre langage.
