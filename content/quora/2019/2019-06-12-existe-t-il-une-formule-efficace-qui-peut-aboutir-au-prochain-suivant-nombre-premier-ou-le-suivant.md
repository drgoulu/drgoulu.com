---
title: Existe-t-il une formule efficace qui peut aboutir au prochain (suivant) nombre premier ou le suivant ?
slug: existe-t-il-une-formule-efficace-qui-peut-aboutir-au-prochain-suivant-nombre-premier-ou-le-suivant
date: '2019-06-12'
draft: false
categories:
- Quora
tags:
- mathematiques
- ecart-entre-nombres-premiers
- theorie-analytique-des-nombres
- formule-empirique
- algorithmes
- formules-mathematiques
- algorithmes-numeriques
- theorie-des-nombres-premiers
- theorie-des-nombres
coverImage: ./images/quora.png
---

*Article initialement publié sur [Quora](https://fr.quora.com/Existe-t-il-une-formule-efficace-qui-peut-aboutir-au-prochain-suivant-nombre-premier-ou-le-suivant/answer/Dr-Goulu)*

Non, mais il existe:

1. des formules qui donnent des nombres premiers plus souvent qu'en tirant au hasard (ou en suivant) par exemple les nombres de la forme p=3×2^n-1 ( [Nombre de Thebit](w:)) ou p = 2^n-1 où n est premier ( [Nombre de Mersenne](w:Nombre_de_Mersenne_premier))
2. des méthodes très rapides pour savoir si ces "candidats" sont premiers ou non. Le [Test de primalité de Miller-Rabin](w:) est le plus utilisé en pratique (= en cryptographie pour générer des clés)
3. avec ce qui précède, du code assz efficace comme [Goulib.math2.nextprime](https://goulib.readthedocs.io/en/latest/_modules/Goulib/math2.html#nextprime) ou [Goulib.math2.random_prime](https://goulib.readthedocs.io/en/latest/_modules/Goulib/math2.html#random_prime)

(voir [Comment trouver des nombres premiers - Pourquoi Comment Combien](https://www.drgoulu.com/2012/04/15/comment-produire-des-nombres-premiers/))

En passant, il semblerait que les propriétés étonnantes des nombres premiers soient plus liées au principe de base du crible qu'à leur absence de diviseurs. Voir [2019 passée au crible - Pourquoi Comment Combien](https://www.drgoulu.com/2019/01/06/2019-passee-au-crible/)
