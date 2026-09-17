---
title: La plupart des programmes de calcul fonctionnent en « double précision », soit 16 chiffres. Quand avez-vous besoin de 16 chiffres et quand 16 chiffres ne suffisent-ils pas ?
slug: la-plupart-des-programmes-de-calcul-fonctionnent-en-double-precision-soit-16-chiffres-quand-avez-vous-besoin-de-16-chiffres-et-quand-16-chiffres-ne-suffisent-ils-pas
date: '2023-11-14'
draft: false
categories:
- Quora
tags:
- informatique
- erreurs
- precision
- calcul
- chiffres-significatifs
- langage-et-programation
- calcul-mathematique
- sciences-informatiques
- l-informatique
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/La-plupart-des-programmes-de-calcul-fonctionnent-en-double-pr%C3%A9cision-soit-16-chiffres-Quand-avez-vous-besoin-de-16-chiffres-et-quand-16-chiffres-ne-suffisent-ils-pas/answer/Dr-Goulu)*

J'avais posé la question légèrement différente ici

[https://physics.stackexchange.co...](https://physics.stackexchange.com/questions/9621/how-many-digits-of-pi-are-required-in-physics#:~:text=You need to know 9,of physics that is testable).

Et on m'avait répondu que 9 ou 10 décimales (de pi) étaient utiles dans le cadre du [Moment magnétique anomal](w:), mais dans l'article on mentionne des valeurs calculées avec 13 à 15 décimales.

Le problème plus courant est que les erreurs d'arrondi se cumulent avec le nombre d'opérations, surtout lors d'opérations combinant des grands nombres et des petits.
