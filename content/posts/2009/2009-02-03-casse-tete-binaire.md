---
title: "Casse-tête binaire"
slug: "casse-tete-binaire"
date: 2009-02-03
categories: 
  - "cat3"
tags: 
  - "casse-tetes"
  - "informatique"
coverImage: "799b28c713fe0b24c23115571899f28f-1.jpg"
---

Je viens d'inventer le problème suivant, qui est en fait une variation informatique d'un [casse-tête récemment proposé sur un autre blog](http://webinet.blogspot.com/2009/01/petite-enigme.html) membre du C@fé des Sciences.

Un registre de microprocesseur contient un mot de 32 bits quelconque, mais dont exactement 8 bits sont à 1, les autres à 0 (par exemple 01001000000000111000010000101000)

Comment faire pour modifier les premiers 8 bits du mots de façon à ce qu'ils comportent autant de bits à '1' qu'il n'y en a au total dans les 24 bits suivant (soit 6 dans l'exemple ci-dessus), et ceci en une seule instruction du processeur ?

{{< figure src="images/799b28c713fe0b24c23115571899f28f.jpg" alt="Binary Kite par Syntopia" link="http://www.flickr.com/photos/syntopia/2058406738/" width="500" >}}

Si vous n'êtes pas familier avec l'[assembleur](http://fr.wikipedia.org/wiki/Assembleur), disons que vous disposez des mêmes opérations qu'une calculatrice, mais en binaire : addition, soustraction, ansi que des [fonctions logiques (et, ou, ...)](http://fr.wikipedia.org/wiki/Op%C3%A9rateur_bool%C3%A9en#Fonctions_logiques). Une instruction, c'est une de ces opérations suivie d'une [opérande](http://fr.wikipedia.org/wiki/Op%C3%A9rande).
