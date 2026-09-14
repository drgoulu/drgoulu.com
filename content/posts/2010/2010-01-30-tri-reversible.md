---
title: "Tri réversible ?"
slug: "tri-reversible"
date: 2010-01-30
categories:
  - "Combien"
  - "Comment"
tags: 
  - "algorithmes"
  - "informatique"
  - "theorique"
  - "tri"
coverImage: "./images/fdd88ca55a8f211b9fc8f978d988744c.jpg"
---

{{< figure src="./images/d4e5d0a778dba725091d8317e6bac939.gif" alt="animation de l'algorithme Quick Sort" caption="animation de l'algorithme Quick Sort" link="http://commons.wikimedia.org/wiki/File:Sorting_quicksort_anim.gif" width="280" >}}

En informatique, le tri est une opération incontournable car il est beaucoup plus rapide de rechercher une information dans une liste triée que dans un fouillis. C'est pourquoi j'ai longtemps cru qu'une liste triée contenait plus d'information qu'une liste non triée, car je voyais le tri comme un pré-traitement permettant d'accélérer les opérations suivantes, donc un "plus" par rapport à une situation "moins" performante.

Pris d'un doute il y a quelques années, j'avais posé la question sur un forum consacré à l'informatique théorique :

> "est-ce qu’une liste triée contient vraiment plus d’information qu’une liste non triée ?”

Un érudit professeur m’avait répondu simplement ceci :

> "ce contient d’ est- information liste liste? non plus qu' qu' triée triée une une vraiment".

J’ai mis un moment à comprendre la profondeur de cette réponse : ma question, une fois les mots triés par ordre alphabétique, était devenue incompréhensible, et contenait donc moins d’information que la phrase originale ! Depuis je sais que [l'informatique détruit toujours l'information](/2007/02/25/linformatique-detruit-linformation/).

[Ce petit concours](http://www.delphigeist.com/2010/01/reversable-sorting-algorithm-contest.html) a reposé la question sous un angle intéressant : est-il possible de programmer un algorithme de tri "réversible", permettant de remettre une liste triée dans son état initial ? Évidemment oui : il suffit de stocker en plus l'information perdue lors du tri, le plus simple étant de mémoriser l'état initial de la liste par exemple en ajoutant à chaque élément trié son numéro d'ordre :

> "ce2 contient7 d’10 est-1 information11 liste5 liste14 non15 plus9 qu'3 qu'12 triée6 triée?16 une4 une13 vraiment8 ”.

Pour une liste contenant n éléments, on a besoin de log(n) bits\* pour stocker chaque numéro, donc de n.log(n) bits au total.

Peut-on faire mieux? On pourrait se dire que beaucoup d'[algorithmes de tri](w:Algorithme_de_tri) comme [QuickSort](w:Tri_rapide) permutent des éléments après les avoir comparés, et qu'il suffirait donc de stocker le résultat des comparaisons effectuées, soit un bit par test, pour pouvoir ensuite "défaire le tri" en parcourant la liste des bits à l'envers. Combien faut-ils de bits ? ben ... au moins n.log(n) aussi puisque c'est justement le nombre de comparaisons qui détermine la "complexité" des algorithmes de tri, et que les bons algorithmes ont une complexité de n.log(n).

Rien ne sert de se casser la tête sur "algorithme de tri réversible", il ne peut pas être plus efficace que de simplement stocker l'ordre initial des données. Etonnant non ?

Le problème, c'est que la donnée du concours spécifie qu'on n'a le droit de stocker que 50% d'information supplémentaire par rapport à la taille des données : si on trie 4K octets, on n'a droit qu'à 2K de données supplémentaires. Or en fonction de ce qui précède on a besoin de 4096\*log(4096) bits, soit 6K, plus que les données! En passant, ça signifie qu'en [triant beaucoup](/2008/11/22/tri/) de petites données, on peut perdre plus de la moitié de l'information contenu dans la liste initiale !

Bref, personne n'a gagné le petit concours parce que ce n'était tout simplement pas possible.,

Note\* : en informatique, log(n) dénote évidemment le [logarithme](w:) binaire ou base 2
