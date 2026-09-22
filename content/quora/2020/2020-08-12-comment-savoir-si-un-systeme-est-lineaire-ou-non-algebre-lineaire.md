---
title: Comment savoir si un système est linéaire ou non (algèbre linéaire)?
slug: comment-savoir-si-un-systeme-est-lineaire-ou-non-algebre-lineaire
date: '2020-08-12'
draft: false
categories:
- Comment
tags:
- mathematiques
- algebre-lineaire
- systeme
- equations
- sciences
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Comment-savoir-si-un-syst%C3%A8me-est-lin%C3%A9aire-ou-non-alg%C3%A8bre-lin%C3%A9aire/answer/Dr-Goulu)*

Vous parlez d'un [Système d'équations linéaires](w:) ? Alors si vous arrivez à mettre votre système sous la forme matricielle A.x=b ou A est une matrice de coefficients constants (indépendants de x) et b un vecteur constant aussi, votre système est linéaire.

Si vous parlez d'un [Système dynamique](w:Système_linéaire) , c'est la même chose : si sa [Représentation d'état](w:) peut être mise sous forme d'un système d'équations linéaires, il est linéaire.

C'est l'occasion de ressortir une grande vérité que j'avais sortie lors d'un séminaire d'automatique et dont je ne suis pas peu fier:

> un système linéaire est un cas très particulier de système non linéaire.

En effet, un système linéaire s'obtient en général en linéarisant, ou en négligeant totalement des effets non linéaires. Ces non linéarités peuvent être gentilles, lisses comme des polynômes par exemple. De ce point de vue, un système linéaire est un système bilinéaire particulier, qui est un système polynomial particulier, qui peut être une approximation polynomiale aussi précise qu'on veut de fonctions non linéaires moins lisses etc.
