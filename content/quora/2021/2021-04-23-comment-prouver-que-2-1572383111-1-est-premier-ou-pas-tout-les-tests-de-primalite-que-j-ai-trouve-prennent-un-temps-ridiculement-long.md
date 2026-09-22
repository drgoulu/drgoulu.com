---
title: Comment prouver que 2^1572383111-1 est premier (ou pas)? Tout les tests de primalité que j'ai trouvé prennent un temps ridiculement long…
slug: comment-prouver-que-2-1572383111-1-est-premier-ou-pas-tout-les-tests-de-primalite-que-j-ai-trouve-prennent-un-temps-ridiculement-long
date: '2021-04-23'
draft: false
categories:
- Comment
tags:
- mathematiques
- theorie
- informatique
- nombres
- calcul
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Comment-prouver-que-2-1572383111-1-est-premier-ou-pas-Tout-les-tests-de-primalit%C3%A9-que-jai-trouv%C3%A9-prennent-un-temps-ridiculement-long/answer/Dr-Goulu)*

Votre nombre est un nombre de Mersenne. Vous pouvez donc appliquer le [Test de primalité de Lucas-Lehmer pour les nombres de Mersenne](w:).

Il se trouve dans ma [goulib.math2](https://goulib.readthedocs.io/en/latest/_modules/Goulib/math2.html#lucas_lehmer) mais vient en fait [d'ici](http://rosettacode.org/wiki/Lucas-Lehmer_test#Python). En l'utilisant :

```
>>> from Goulib import *
>>> lucas_lehmer(1572383111)
False

```

j'ai un résultat immédiat : non 2^1572383111-1 n'est pas premier.

en fait c'est tellement rapide que j'ai un doute :

```
>>> list(factorize(1572383111))
[(13, 1), (71, 1), (1703557, 1)]

```

comme votre exposant n n'est pas premier 2^n-1 ne peut pas être premier.

Le test de Lucas-Lehmer n'est donc même pas exécuté, c'est le test de primalité de l'exposant qui échoue.

En fait le nombre premier suivant votre exposant est

```
>>> nextprime(1572383111)
1572383149

```

résultat quasi instantané aussi, alors qu'on teste la primalité d'une vingtaine de nombres. C'est parce que ma lib utilise* le [Test de primalité de Miller-Rabin](w:) qui est un test très rapide "mais" probabiliste.

Le "mais" est parce qu'il existe des faux positifs, très rares. Le premier est 3825123056546413051, donc comme 1572383111 est plus petit, aucun risque de se tromper : Miller-Rabin est déterministe..

Et au dessus, la probabilité de trouver un faux positif est plus faible que d'avoir un rayon cosmique qui change un bit lors d'un test déterministe, donc le test probabiliste est plus sur que les test déterministe !

Cela dit c'est vrai, le test de Lucas-Lehmer pour 1572383149 est terriblement lent.

En fait, au dessus de

```
>>> lucas_lehmer(19937)
True

```

ma machine prend plusieurs secondes, et comme 82589933 est le plus grand exposant de Mersenne premier connu actuellement (depuis 2018) et a été obtenu par GIMPS ([Great Internet Mersenne Prime Search](w:)) avec une puissance de calcul colossale, je doute beaucoup que la primalité de 2^1572383149-1 puisse être testée avant longtemps.

Note* : en fait c'est plus compliqué que ça, voir la doc de [Goulib.math2.is_prime](https://goulib.readthedocs.io/en/latest/modules/Goulib.math2.html#Goulib.math2.is_prime)

Plus sur ce sujet :

[https://www.drgoulu.com/2012/04/...](/2012/04/15/comment-produire-des-nombres-premiers/)
