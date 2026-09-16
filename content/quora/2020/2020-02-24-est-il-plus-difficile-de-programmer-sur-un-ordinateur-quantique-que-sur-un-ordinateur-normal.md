---
title: Est-il plus difficile de programmer sur un ordinateur quantique que sur un ordinateur normal ?
slug: est-il-plus-difficile-de-programmer-sur-un-ordinateur-quantique-que-sur-un-ordinateur-normal
date: '2020-02-24'
draft: false
categories:
- Quora
tags:
- informatique
- difficulte
- ordinateurs-quantiques
- science-de-l-information-quantique
- science-de-l-informatique
- programmation-quantique
- l-informatique-quantique
- informatique-quantique
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Est-il-plus-difficile-de-programmer-sur-un-ordinateur-quantique-que-sur-un-ordinateur-normal/answer/Dr-Goulu)*

En fait la "programmation" d'un [Calculateur quantique](w:) revient plutôt à câbler un "circuit quantique" qui résout un problème particulier "d'un coup". Pour ce que j'en comprends actuellement, c'est similaire à la "programmation" des anciens [Calculateurs analogiques](w:Calculateur_analogique) où on connectait entre eux des ampli-ops pour réaliser des fonctions de transfert pour réaliser des simulations dynamiques extrêmement rapides.

Mon impression est que la programmation quantique repose sur des concepts tellement différents du séquentiel, ou même du parallélisme "ordinaire" que c'est difficilement comparable. Les algos et leurs complexités sont totalement différents (voir [Algorithme de Grover](w:) par exemple), donc la "manière de penser" doit être très différente.

Ce qui est sur, c'est que les ordinateurs quantiques actuels sont encore très "simples" et visent à résoudre une classe réduite et bien spécifiques de problèmes. Ce qui fait la complexité de la programmation "normale" c'est la généralité de ce qu'on peut traiter avec les machines classiques, qu'on développe à une cadence ahurissante depuis une cinquantaine d'années maintenant.

Donc je me risque à dire que la programmation quantique est actuellement plus simple que la programmation séquentielle.

Merci pour la question qui m'a permis de découvrir [Qiskit](https://qiskit.org/) qui me permettra de vérifier mon impression.
