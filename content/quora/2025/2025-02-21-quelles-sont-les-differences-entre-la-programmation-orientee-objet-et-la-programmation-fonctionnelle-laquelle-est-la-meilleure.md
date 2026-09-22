---
title: Quelles sont les différences entre la programmation orientée objet et la programmation fonctionnelle ? Laquelle est la meilleure ?
slug: quelles-sont-les-differences-entre-la-programmation-orientee-objet-et-la-programmation-fonctionnelle-laquelle-est-la-meilleure
date: '2025-02-21'
draft: false
categories:
- Quora
tags:
- informatique
- programmation
- langage
- comparaisons
- sciences-informatiques
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Quelles-sont-les-diff%C3%A9rences-entre-la-programmation-orient%C3%A9e-objet-et-la-programmation-fonctionnelle-Laquelle-est-la-meilleure/answer/Dr-Goulu)*

Ce sont des "paradigmes" différents, mais pas opposés ni incompatibles.

Après une carrière dans ce domaine, je dirais que la [Programmation orientée objet](w:)est adaptée à des gros projets bien formalisés où on utilise des outils, de modélisation (UML), où on définit bien les interfaces des objets et classes dont on peut répartir la réalisation sur plusieurs programmeurs.

La [Programmation fonctionnelle](w:)"pure" est très limitative, à part quelques logiciels embarqués critiques en Erlang ou des trucs d'ingénieurs en Lisp, je ne connais aucun gros logiciel écrit en fonctionnel.

Par contre c'est assez cool de passer des fonctions en paramètres à des procédures ou méthodes.

Une des plus jolies introduction à ceci est la [documentation python](https://docs.python.org/3/howto/functional.html)sur les itérateurs, décorateurs etc.

Et le plus bel exemple que je connaisse est ma classe Sequence (donc objet) qui implante des suites d'entiers infinies (en programmation fonctionnelle) :

[https://drgoulu.com/2017/06/26/s...](/2017/06/26/series-infinies-et-oeis-en-python/)
