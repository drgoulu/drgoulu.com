---
title: Est-il possible de calculer un gogolplex (10^10^100) un ordinateur en est-il capable ?
slug: est-il-possible-de-calculer-un-gogolplex-10-10-100-un-ordinateur-en-est-il-capable
date: '2021-05-27'
draft: false
categories:
- Quora
tags:
- informatique
- mathematiques
- capacite-mentale
- puissance-de-calcul
- capacites
- sciences-informatiques
- calcul-mathematique
- mathematiciens
- capacite-du-cerveau
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Est-il-possible-de-calculer-un-gogolplex-10-10-100-un-ordinateur-en-est-il-capable/answer/Dr-Goulu)*

Oui bien sur. Mon petit programme python le fait :

[https://gist.github.com/goulu/13...](https://gist.github.com/goulu/13ee3a2d8145398b75d008d55d66196a)

Toute l'astuce est dans la représentation des nombres. Le binaire auquel tout le monde pense en premier est bien pratique jusque vers 2^64 ou 2^2048 en cryptographie par exemple, mais pour les nombres plus grands, il faut choisir une autre représentation.

La représentation symbolique sous forme "10^10^100" est déjà une façon claire et précise de mémoriser le nombre. On peut aussi le faire dans une structure en arbre comme pow(10,pow(10,100)) par exemple

Ensuite "calculer" un tel nombre n'a pas tellement de sens. On devrait plutôt dire calculer "avec" ce nombre. Et là encore, il y a rarement une bonne raison de manipuler le [Développement décimal](w:) complet d'un nombre, on peut très bien calculer "avec" un nombre sans manipuler chacun de ses chiffres. Par exemple, si je veux calculer gogolplex/gogolplex, je n'ai pas vraiment besoin de faire une division…

Mais j'ai bien compris que vous aimeriez un programme qui "calcule" un gogolplex en imprimant son développement décimal.

Donc le petit programme ci-dessus représente les puissances de dix en utilisant [itertools.product](https://docs.python.org/fr/3/library/itertools.html#itertools.product), une autre géniale fonction qui renvoie un [itérateur](w:)correspondant à des boucles imbriquées.

par exemple

```
for x in product(range(10),repeat=2):
	print(x)

```

fait la même chose que

```
for x in range(10):
	for y in range(10):
		print(x,y)

```

sauf que

```
product(range(10), repeat=100)

```

est plus facile à écrire que 100 boucles imbriquées…

Ensuite, la fonction tenprint imprime le nombre sous forme d'un '1' suivi d'un zéro par boucle de l'itérateur, et voilà.

En passant, les itérateurs permettent même de représenter et de manipuler des objets infinis :

[https://www.drgoulu.com/2017/06/...](/2017/06/26/series-infinies-et-oeis-en-python/)

Donc ce n'est pas un tout petit nombre de rien du tout comme un gogolplex qui va leur faire peur.

[https://www.drgoulu.com/2008/11/...](/2008/11/04/tres-tres-tres-grands-nombres/)
