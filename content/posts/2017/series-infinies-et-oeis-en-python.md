---
title: "Suites infinies en Python"
slug: "series-infinies-et-oeis-en-python"
date: 2017-06-26
categories:
  - "Comment"
tags: 
  - "algorithmes"
  - "fibonacci"
  - "nombres"
  - "nombres-premiers"
  - "oeis"
  - "python"
coverImage: "./images/E6fJJ.png"
---

{{< figure src="./images/E6fJJ.png" >}}

Depuis que je programme en Python, j'entasse les petits bouts de code utiles ou potentiellement réutilisables dans "Goulib", ma librairie perso et néanmoins disponible en open-source (licence LGPL)  sur [Pypi](https://pypi.python.org/pypi/Goulib/), [GitHub](https://github.com/goulu/Goulib), ReadTheDocs pour [la doc](http://goulib.readthedocs.io/en/latest/), avec des [notebooks Jupyter de démo.](http://nbviewer.jupyter.org/github/Goulu/Goulib/blob/master/notebook.ipynb)

Comme la valeur d'un code se mesure surtout par les tests qui vérifient son bon fonctionnement, je me suis lancé dans un ambitieux projet (de plus...) : tester un maximum de fonctions de mes modules [math2](http://goulib.readthedocs.io/en/latest/modules/Goulib.math2.html) et [itertools2](http://goulib.readthedocs.io/en/latest/modules/Goulib.itertools2.html) en calculant des suites de l' [Encyclopédie en ligne des suites de nombres entiers](https://oeis.org/), plus connue sous son acronyme anglais OEIS.

Pour cela j'ai fait un truc dont je suis vachement fier\* :

## La classe Sequence

Ce [container](w:conteneur_(informatique)) ([embryon de doc](https://goulib.readthedocs.io/en/latest/modules/Goulib.container.html#Goulib.container.Sequence)) permet de représenter une [suite](w:suite_(mathématiques)) (sequence en anglais) finie ou infinie de nombres\*\* à partir d''une ou plusieurs fonctions passées à [son constructeur](https://goulib.readthedocs.io/en/latest/modules/Goulib.container.html#Goulib.container.Sequence.__init__):

- iterf : un [itérateur](w:) ou générateur produisant les termes de la suite l'un après l'autre
- itemf : une fonction  retournant le i-ème paramètre de la suite
- containf : une fonction renvoyant vrai (True) si son paramètre appartient à la suite.

On peut créer par exemple la série (infinie) des nombres premiers ainsi :

[A000040](https://oeis.org/A000040)\=Sequence(containf=[is\_prime](http://goulib.readthedocs.io/en/latest/modules/Goulib.math2.html#Goulib.math2.is_prime))

Ensuite, l'objet ainsi créé avec n'importe quelle combinaison de ces 3 paramètres peut être utilisé indifféremment:

- comme un générateur : for p in A000040() : print(p) # affiche les nombres premiers (jusqu'à l'infini)
- comme une liste: A000040\[999\] # renvoie le 1000ème nombre premier (parce que Python indice à partir de 0...)
- comme un ensemble: 201420142013 in A000040 # renvoie True car ce nombre est premier.

Evidemment, si on dispose de fonctions plus efficaces pour chacun de ces paramètres, on peut les utiliser pour rendre les calculs bien plus rapides. Par exemple pour la suite de Fibonacci, on peut exploiter trois algorithmes différents :

[A000045](https://oeis.org/A0000405)\=Sequence(iterf=[fibonacci\_gen](http://goulib.readthedocs.io/en/latest/modules/Goulib.math2.html#Goulib.math2.fibonacci_gen), itemf=[fibonacci](http://goulib.readthedocs.io/en/latest/modules/Goulib.math2.html#Goulib.math2.fibonacci), containf=[is\_fibonacci](http://goulib.readthedocs.io/en/latest/modules/Goulib.math2.html#Goulib.math2.is_fibonacci))

En passant, voici comment est définie la séquence "auto descriptrice"qui orne la bannière de l'OEIS ci-dessus:

[A005150](https://oeis.org/A0005150)\=Sequence( [recurrence](http://goulib.readthedocs.io/en/latest/modules/Goulib.itertools2.html#Goulib.itertools2.recurrence)( lambda x: [num\_from\_digits](http://goulib.readthedocs.io/en/latest/modules/Goulib.math2.html#Goulib.math2.num_from_digits)( [flatten](http://goulib.readthedocs.io/en/latest/modules/Goulib.itertools2.html#Goulib.itertools2.flatten)( [swap](http://goulib.readthedocs.io/en/latest/modules/Goulib.itertools2.html#Goulib.itertools2.swap)( [compress](http://goulib.readthedocs.io/en/latest/modules/Goulib.itertools2.html#Goulib.itertools2.compress)( [digits](http://goulib.readthedocs.io/en/latest/modules/Goulib.math2.html#Goulib.math2.digits)(x))))) ,1))

Compact et presque clair, non ?

## Dérivation

Une Sequence peut être dérivée d'une autre grâce à plusieurs méthodes:

- [filter](http://goulib.readthedocs.io/en/latest/modules/Goulib.container.html#Goulib.container.Sequence.filter) renvoie une Sequence correspondant à la Sequence source filtrée par une fonction. Par exemple: [A000043](https://oeis.org/A000043)\=A000040.filter([math2.lucas\_lehmer](http://goulib.readthedocs.io/en/latest/modules/Goulib.math2.html#Goulib.math2.lucas_lehmer)) renvoie les "exposants de Mersenne", les nombres premiers p tels que $2^p - 1$ est premier.
- [apply](http://goulib.readthedocs.io/en/latest/modules/Goulib.container.html#Goulib.container.Sequence.apply) applique une fonction à chaque terme de la Sequence source. Par exemple la série des carrés des nombres premiers peut se définir ainsi: [A001248](https://oeis.org/A001248)\=A000040.apply(lambda n:n\*n)
- Pour éviter l'utilisation d'apply dans des cas trivialement simples, l'addition (et la soustraction) d'une Sequence et d'un entier sont définies. Par exemple: [A000215](https://oeis.org/A000215)\=[A001146](https://oeis.org/A001146)+1 définit les [nombres de Fermat](w:nombre_de_Fermat) à partir des nombres de la forme $2^{2^n}$
- [accumulate](http://goulib.readthedocs.io/en/latest/modules/Goulib.container.html#Goulib.container.Sequence.accumulate) renvoie une Sequence dont le n-ième terme est obtenu en sommant les n premiers termes de la Sequence source: [A007504](https://oeis.org/A007504)\=A000040.accumulate()
- [pairwise](http://goulib.readthedocs.io/en/latest/modules/Goulib.container.html#Goulib.container.Sequence.pairwise) renvoie une Sequence produite en appliquant applique une fonction à chaque paire de termes consécutifs. Ainsi la suite des différences entre nombres premiers consécutifs s'écrit: [A001223](https://oeis.org/A001223)\=A000040.pairwise(operator.sub)

On peut aussi combiner deux Sequences pour en créer une nouvelle:

- L'opérateur % (modulo, pourquoi pas...) renvoie les termes de la Sequence opérande de gauche qui ne sont PAS dans l'opérande de droite. Ainsi: [A007510](https://oeis.org/A007510)\=A000040 % [A001097](https://oeis.org/A001097) définit la Sequence des nombres premiers qui ne sont pas [jumeaux](w:Nombres_premiers_jumeaux)
- L'opérateur & (and) renvoie les termes de la Sequence opérande de gauche qui sont aussi dans l'opérande de droite. Ainsi: [A020449](https://oeis.org/search?q=A020449)\=[A007088](https://oeis.org/search?q=A007088) & A000040 définit la suite des nombres premiers dont qui ne s'écrivent qu'avec des 0 et des 1.
- L'opérateur | (or) renvoie la fusion de deux séquences à l'aide du génial [heapq.merge](http://sametmax.com/heapq-le-module-python-incompris/) . Ainsi: [A030513](https://oeis.org/A030513)\=[A030078](https://oeis.org/A030078) | [A006881](https://oeis.org/A006881) définit les nombres ayant 4 diviseurs (dont 1 et eux-mêmes) comme l'union de ceux qui sont le produit de deux nombres premiers avec ceux qui sont le cube d'un nombre premier.

Il y a encore deux méthodes un peu "tirées par les cheveux" du point de vue mathématique, mais qui fonctionnent très bien informatiquement:

- [sort](http://goulib.readthedocs.io/en/latest/modules/Goulib.container.html#Goulib.container.Sequence.sort) renvoie une Sequence [monotone croissante](w:Suite_(mathématiques)#Suites_monotones) (par défaut) en triant les termes de la Sequence d'origine. Par exemple, voici la suites des surfaces des [triplets pythagoriciens](/2017/01/02/2017-et-les-triplets-pythagoriciens/) dans l'ordre croissant: [A024406](https://oeis.org/A024406)\=Sequence(math2.primitive\_triples).apply(lambda x:x\[0\]\*x\[1\]//2) .sort()
- [unique](http://goulib.readthedocs.io/en/latest/modules/Goulib.container.html#Goulib.container.Sequence.unique) renvoie une Sequence où les termes redondants de la suite d'origine sont absents, par exemple: [A001097](https://oeis.org/A001097) = [A077800](https://oeis.org/A077800) .unique() // oui, parce que le 5 appartient à deux paires de nombres premiers jumeaux ...

Ces méthodes utilisent respectivement [itertools2.sorted\_iterable](http://goulib.readthedocs.io/en/latest/modules/Goulib.itertools2.html#Goulib.itertools2.sorted_iterable) et  [itertools2.unique,](http://goulib.readthedocs.io/en/latest/modules/Goulib.itertools2.html#Goulib.itertools2.unique) qui fonctionnent tant que la suite initiale est "presque" triée, à savoir tant que l'écart n entre un terme $a_i+n \leq a_i$ n'excède pas le paramètre "buffer" de la fonction. On peut évidemment trouver des suites qui ne pourront "mathématiquement" pas être traitées ainsi, mais informatiquement j'arrive à reproduire les suites de l'OEIS rencontrées jusqu'ici avec buffer=100 seulement

## Le dictionnaire OEIS

J'ai ainsi constitué peu à peu le fichier [oeis.py](https://github.com/goulu/Goulib/blob/master/examples/oeis.py) qui définit actuellement environ 150 séries de l'OEIS, et que j'étoffe lorsque l'occasion se présente. A la fin de ce module, j'utilise la géniale possibilité d'introspection de Python pour regrouper toutes les Sequence définies dans un dictionnaire fort utile pour les tests:

\[python\]# Construit le dictionnaire OEIS par introspection : Simple et WOW ! oeis={} # on crée le dictionnaire vide seqs=globals().copy() # on copie tous les objets déclarés dans ce module for id in seqs: # on parcourt tous les identificateurs des objets if id\[0\]=='A' and len(id)==7: # et s'ils ont un nom de séquence OEIS ... oeis\[id\]=seqs\[id\] # on les ajoute au dictionnaire ... seqs\[id\].name=id # et on définit leur champ name \[/python\]

## Performance

Un point important est qu'aucun calcul n'est effectué lors des opérations ci-dessus. Ce n'est qu'au moment d'utiliser les Sequence ainsi définies que les fonctions iterf, itemf, containf et leurs éventuelles compositions sont évaluées.

C'est un peu "automagique", mais il faut tout de même veiller à utiliser les algorithmes les plus efficaces, et c'est même un des buts que je poursuis avec ce projet. Par exemple la suite des nombres premiers dont qui ne s'écrivent qu'avec des 0 et des 1 [A020449](https://oeis.org/A020449)\=[A007088](https://oeis.org/A007088) & A000040 aurait pu s’écrire également: A020449=A000040 & A007088 mais la première formulation est beaucoup plus rapide car la série A007088 des nombres ne s'écrivant qu'avec des 0 et des 1 croît beaucoup plus vite que celle des nombres premiers A000040. Il est par conséquent beaucoup plus rapide de tester si les nombres du genre 1101010101011101 sont premiers que d'énumérer tous les nombres premiers de 16 chiffres et de jeter ceux qui contiennent d'autres chiffres que des 0 ou 1.

Malgré toutes ces précautions, parcourir une suite infinie prendra forcément un temps infini, et ces idiots d'ordinateurs ne sont toujours pas foutus de gérer le [problème de l'arrêt](w:). J'ai donc écrit un [décorateur (j'adore!)](/2010/12/04/les-decorateurs-python/) qui limite le temps de calcul d'une boucle ainsi :

for x in [decorators.itimeout](https://goulib.readthedocs.io/en/latest/modules/Goulib.decorators.html#Goulib.decorators.itimeout)(suite,1): print(x) # affiche tous les termes calculables en 1 seconde (au total)

Ce décorateur est utilisé en particulier dans [pprint,](https://goulib.readthedocs.io/en/latest/modules/Goulib.tests.html#Goulib.tests.pprint) la fonction appelée par [Sequence.\_\_repr\_\_](https://goulib.readthedocs.io/en/latest/modules/Goulib.container.html#Goulib.container.Sequence.__repr__) pour afficher les dix premiers termes d'une Sequence, ou du moins ceux qu'on peut calculer en moins d'une seconde.

Les suites particulièrement lentes sont par exemple [A007508](https://oeis.org/A007508) ou [A035533](https://oeis.org/A035533) dont le n-ième terme donne le nombre de nombres inférieurs à 10^n  satisfaisant une certaine condition. Faute de meilleur algorithme, chaque terme prend 10x plus de temps que le précédent ...

## Tests

Voià, tous les ingrédients sont prêts pour tester si mes beaux algorithmes fonctionnent correctement, ce qui était le but initial je le rappelle.

Pour ceci, il suffit de vérifier que chaque Sequence fournit bien les mêmes termes que ceux disponibles dans l'OEIS. Ceci est facilité par le fait que l'OEIS fournit pour chaque suite les n premières valeurs dans un fichier texte en [format maison "B-file"](https://oeis.org/wiki/B-files) accessible par le web. Par exemple [https://oeis.org/A000040/b000040.txt](https://oeis.org/A000040/b000040.txt) fournit les 10'000 premiers nombres premiers.

Donc mon fichier [test\_oeis.py](https://github.com/goulu/Goulib/blob/master/examples/test_oeis.py) est lui aussi génialement simple\* : il traverse le dictionnaire oeis et pour chaque Sequence il télécharge les N termes de référence du site OEIS, vérifie que les n premiers termes de la Sequence sont bien ceux attendus, et produit une erreur sinon. Ou un avertissement si itimeout a limité n à moins de 10.

Ces tests sont automatiquement exécutés (avec beaucoup d'autres) [sur Travis-CI](https://travis-ci.org/goulu/Goulib) chaque fois que je pousse une nouvelle version de [Goulib sur GitHub](https://github.com/goulu/Goulib), ce qui fait que je suis averti si modification crée un problème avec une ancienne version de Python ou si un Pingouin détecte un problème invisible de mes Fenêtres.

## Débogage... de l'OEIS !

J'ai ainsi beaucoup débogué, amélioré et optimisé la plupart des fonctions de  [Goulib.math2](http://goulib.readthedocs.io/en/latest/modules/Goulib.math2.html) et beaucoup d'[itertools2](http://goulib.readthedocs.io/en/latest/modules/Goulib.itertools2.html), et je compte poursuivre dans cette voie qui permet d'utiliser les données de l'OEIS comme une référence, validées par de nombreux utilisateurs.

Sauf que des fois, le bug était chez eux. Et je ne suis pas peu fier d'[avoir pu corriger](https://oeis.org/history?user=Philippe%20Guglielmetti) sur l'OEIS :

- [A121727](https://oeis.org/A121727) , comme déjà mentionné dans [cet article](/2017/01/02/2017-et-les-triplets-pythagoriciens/), le 20ème terme de la série est 145, pas 142.
- [A036275](https://oeis.org/A036275), dont certains termes avaient besoins de 0 supplémentaires. Tant qu'à faire j'ai fourni un B-file contenant les 1000 premiers termes exacts pour remplacer l'ancien qui n'en avait que 500.

A cette occasion j'ai remarqué que l'édition de l'OEIS est un peu rébarbative, ce qui peut décourager les contributeurs débutants. Peut-être que mon modeste projet pourrait servir de base à un site plus interactif, utilisant du code (Python of course) pour calculer dynamiquement les suites requises ...

Ce long article mijoté pendant plus de six mois se termine par un appel aux allumés du code bonnes volontés : si cet article vous a motivé , n'hésitez pas à contribuer à la Goulib sur GitHub.

Pour ma part je m'attaque aux [nombre narcissique](w:nombres_narcissiques) et [nombres de Friedman](w:nombre_de_Friedman) qui seront l'occasion de nettoyer le code du [jeu de l'année](/2012/01/18/jeu-de-lannee-2012-et-autres-cest-fini/)  en utilisant et testant le module [Goulib.expr](http://goulib.readthedocs.io/en/latest/modules/Goulib.expr.html)

### Notes

\*sinon je n'en parlerais pas ici... \*\*ou d'autres objets mais je n'ai pas encore trouvé quoi...
