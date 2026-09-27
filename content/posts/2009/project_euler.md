---
title: "Programmer pour le fun"
slug: "project_euler"
date: 2009-02-23
categories:
  - "Comment"
tags: 
  - "casse-tetes"
  - "maths"
  - "programmation"
coverImage: "./images/a9192f1b2a56a4bbaee679259c557e57.jpg"

aliases:
  - "/2009/02/24/project_euler/"
---

{{< figure src="./images/a9192f1b2a56a4bbaee679259c557e57.jpg" >}}

Amis des casse-tête mathématiques ardus et de la programmation d'algorithmes optimisés, bonjour!

Je viens de découvrir [Project Euler.net](http://projecteuler.net/), et j'ai honte de ne pas l'avoir trouvé avant. Ce site propose 233 problèmes (et environ un de plus chaque semaine environ) pouvant parfois être résolus avec un papier et un crayon propulsé par un cerveau en ébullition, mais pour la plupart requièrent  quelques lignes de code bien pensées et un stupide esclave électronique pour les exécuter.

Une fois inscrit sur le site, vous pouvez soumettre vos solutions aux problèmes dans l'ordre qui vous plait et chaque bonne réponse vous apporte instantanément:

- la possibilité d'accéder à un forum où les solutions sont comparées et discutées. C'est en général là qu'on commence à avoir mal au front, quand on découvre des algorithmes 1000x plus rapides que ceux qu'on s'est escrimé à mettre au point, ou pire, la petite formule qui tue...
- un bon point. Après 25 bonnes réponses vous entrez dans le tableau des [scores](http://projecteuler.net/index.php?section=scores) et pouvez espérer rejoindre un jour la [vingtaine de mutants](http://projecteuler.net/index.php?section=scores&level=5) qui ont résolu tous les problèmes jusqu'ici.

Il faut dire que les premiers problèmes sont relativement simples, par exemple les 17 que j'ai déjà résolus sont :

- additionner tous les entiers intérieurs à 1000 qui sont multiples de 3 ou 5
- trouver la somme de tous les nombres pairs de la [suite de Fibonacci](w:Nombre_de_Fibonacci) inférieurs à 4'000'000
- trouver le plus grand facteur premier de 600'851'475'143
- trouver le plus grand palindrome formé par le produit de 2 nombres de 3 chiffres
- quel est le plus petit nombre divisible par tous les entiers de 1 à 20 ? (facile. celui là je l'ai fait à la main)
- quelle est la différence entre le carré de la somme des 100 premiers entiers et la somme du carré de ces même nombres ?
- trouver le 10001ème nombre premier
- trouver le plus grand produit de 5 chiffres consécutifs dans un nombre à 1000 chiffres
- trouver le seul [triplet pythagoricien](w:Nombres_pythagoriciens) dont la somme a+b+c=1000
- calculer la somme des nombres premiers inférieurs à 2'000'000
- quel est le premier [nombre triangulaire](w:) ayant plus de 500 diviseurs ?
- quels sont les 10 premiers chiffres de la somme de 100 nombre de 50 chiffres donnés?
- trouver le nombre inférieur à 1'000'000 générant la plus longue [suite de Syracuse](w:Conjecture_de_Syracuse)
- en partant d'un coin d'une grille de 20x20, combien y'a-t-il de chemins au coin opposé ? ([j'ai déjà vu ça quelque part](/2008/05/17/recrutement-et-casse-tete/)...)
- quelle est la somme des chiffres de  21000?
- quel est le premier terme supérieur à 101000 de la suite de Fibonacci ? (et si je vous disais qu'on peut le trouver sans calculer les termes précédents ?)
- trouver la somme des chiffres de 100! (factorielle...)

Certains de ces problèmes exigent de pouvoir manipuler de grands nombres, ce qui est une force du langage [Python](/2008/10/17/pythonxy/), que j'aime de plus en plus. On peut par exemple obtenir la somme des chiffres de la factorielle de 100 en une seule ligne\* combinant la [programmation fonctionnelle](w:Python_(langage)#Programmation_fonctionnelle) et la fonction [reduce (un des piliers de la puissance de Google):](/2008/11/22/tri/)

```
reduce(lambda x, y: x + y, [int(i) for i in str(reduce(lambda x, y: x * y, range(1, 100)))])
```

Bon, jusqu'ici j'ai fait le facile : même avec une approche un peu brutale, on s'en sort. Mais rapidement la complexité fait son apparition au carré : au niveau mathématique et au niveau algorithmique, condamnant le programmeur peu subtil à patienter des minutes, des heures ou des siècles devant un sablier virtuel ...

Je vois encore quelques problèmes liés à des sujets déjà abordés sur Dr.Goulu comme:

- trouver le polynôme _n_² + _an_ + _b_, où|_a_| < 1000 et|_b_| < 1000 qui produit le plus de [nombres premiers consécutifs](/2007/01/20/les-nombres-premiers/)
- quel nombre premier inférieur à 1'000'000 est la [somme du plus de nombres premiers consécutifs](/2008/06/03/sommes-egales-de-nombres-premiers-consecutifs/) ?
- combien existe-t-il de [nombres de Lychrel](/2008/09/14/palindrome-de-196/) inférieurs à 10'000 ?

Il y a encore environ entre 20 et 50 problèmes que j'espère pouvoir résoudre à raison d'un  par soirée.

Après, ce sera **l'enfer** mais j'espère vous y retrouver, ami lecteur ... (insérer un rire [sardonique](http://fr.wiktionary.org/wiki/sardonique) ici)

_Note\* dans le forum on découvre une solution en 13 caractères seulement, en [APL](w:APL_(langage)) évidemment: +/"."0":!100x_

![](./images/Dr_Goulu.png)
