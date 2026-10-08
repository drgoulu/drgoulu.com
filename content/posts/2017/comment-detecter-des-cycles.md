---
title: Comment détecter des cycles
slug: comment-detecter-des-cycles
date: '2017-11-08'
categories:
  - "Comment"
tags:
- algorithmes
- oeis
draft: true
---
A la fin de mon article sur [le 1019 ième terme de la suite de Fibonacci](/2017/04/25/comment-calculer-le-1e19-eme-terme-de-la-suite-de-fibonacci/) je suis tombé sur la notion de [période de Pisano](w:)\* et de là au problème de la détection de cycle dans une suite, plus touffu qu'il n'y parait.

D'autant que l'article [détection de cycle](w:) de la Wikipedia n'existe pas à ce jour, la [version anglophone](w:en:cycle_detection)  est limitée à un seul cas particulier, dont seule la solution la plus simple est disponible en français dans l'article  "[Algorithme du lièvre et de la tortue](w:)".  Le sujet n'est donc pas assez bien couvert, ce qui peut conduire le lecteur trop pressé à utiliser un algorithme qui donnera des résultats faux dans certains cas de figure. Exemple : moi.

Une fois n'est pas coutume, je vais adopter un style un peu plus encyclopédique que d'habitude dans la suite de cet article, afin de pouvoir le publier comme base d'un nouvel article Wikipédia "[détection de cycle](w:)".

## Introduction

En [informatique](w:), la [détection de cycle](w:) est le problème [algorithmique](w:) de trouver un cycle dans une [suite](w:suite_(mathématiques)) de valeurs obtenues de manière [itérative](w:itération).

Ce problème doit être distingué de celui de la détection de [cycle dans un graphe](w:Cycle_(théorie_des_graphes)).

## Algorithmes

Plusieurs familles d'algorithmes ont été développés pour couvrir diverses combinaisons de cas possibles:

1. la suite peut être finie ou infinie.
2. les valeurs de la suite peuvent appartenir à un ensemble fini ou infini.
3. les valeurs peuvent apparaître une seule fois au maximum dans le cycle, ou plus d'une fois.
4. le cycle peut être précédé d'une partie non cyclique, ou pas.

#### Suite infinie avec valeurs figurant une seule fois au maximum dans le cycle

Ce cas apparaît en particulier lors de l'application répétée d'une fonction sur elle-même.

Soit une [fonction](w:Fonction_(mathématiques)) {{mvar|f}} d'un [ensemble fini](w:) {{mvar|S}} sur lui\-même, et une valeur initiale {{math|''x''<sub>0</sub>}} de {{mvar|S}}, la suite infinie des valeurs itérées

:<math> x\_0,\\ x\_1=f(x\_0),\\ x\_2=f(x\_1),\\ \\dots,\\ x\_i=f(x\_{i\-1}),\\ \\dots</math>

doit forcément comporter: there must be some pair of distinct indices {{mvar|i}} and {{mvar|j}} such that {{math|1=''x<sub>i</sub>'' = ''x<sub>j</sub>''}}. Once this happens, the sequence must continue [periodically](w:periodic_sequence), by repeating the same sequence of values from {{math|''x<sub>i</sub>''}} to {{math|''x''<sub>''j'' &minus; 1</sub>}}. Cycle detection is the problem of finding {{mvar|i}} and {{mvar|j}}, given {{mvar|f}} and {{math|''x''<sub>0</sub>}}.

L'[algorithme du lièvre et de la tortue](w:) attribué à [Robert Floyd](w:)

 

 

## Applications:

- Determining the cycle length of a [pseudorandom number generator](w:en) is one measure of its strength. This is the application cited by Knuth in describing Floyd's method.[\[3\]](https://en.wikipedia.org/wiki/Cycle_detection#cite_note-knuth-3) Brent[\[8\]](https://en.wikipedia.org/wiki/Cycle_detection#cite_note-brent-8) describes the results of testing a [linear congruential generator](w:en "Linear congruential generator") in this fashion; its period turned out to be significantly smaller than advertised. For more complex generators, the sequence of values in which the cycle is to be found may not represent the output of the generator, but rather its internal state.
- Several [number-theoretic](w:en:Number_theory) algorithms are based on cycle detection, including [Pollard's rho algorithm](w:en:Pollard%27s_rho_algorithm "Pollard's rho algorithm") for integer factorization[\[20\]](https://en.wikipedia.org/wiki/Cycle_detection#cite_note-20) and his related [kangaroo algorithm](w:en:Pollard's_kangaroo_algorithm) for the [discrete logarithm](w:en) problem.[\[21\]](https://en.wikipedia.org/wiki/Cycle_detection#cite_note-21)
- In [cryptographic](w:en:Cryptography) applications, the ability to find two distinct values _x_μ−-1 and _x_λ+μ−-1 mapped by some cryptographic function ƒ to the same value _x_μ may indicate a weakness in ƒ. For instance, Quisquater and Delescaille[\[17\]](https://en.wikipedia.org/wiki/Cycle_detection#cite_note-qd-17) apply cycle detection algorithms in the search for a message and a pair of [Data Encryption Standard](w:en) keys that map that message to the same encrypted value; [Kaliski](w:en:Burt_Kaliski "Burt Kaliski"), [Rivest](w:en:Ron_Rivest "Ron Rivest"), and [Sherman](w:en:Alan_Sherman "Alan Sherman")[\[22\]](https://en.wikipedia.org/wiki/Cycle_detection#cite_note-krs-22) also use cycle detection algorithms to attack DES. The technique may also be used to find a [collision](w:en:Hash_collision "Hash collision") in a [cryptographic hash function](w:en "Cryptographic hash function").[\[23\]](https://en.wikipedia.org/wiki/Cycle_detection#cite_note-23)
- Cycle detection may be helpful as a way of discovering [infinite loops](w:en:Infinite_loop) in certain types of [computer programs](w:en:Computer_program "Computer program").[\[24\]](https://en.wikipedia.org/wiki/Cycle_detection#cite_note-24)
- [Periodic configurations](w:en:Oscillator_(cellular_automaton)) in [cellular automaton](w:en) simulations may be found by applying cycle detection algorithms to the sequence of automaton states.[\[12\]](https://en.wikipedia.org/wiki/Cycle_detection#cite_note-nivasch-12)
- [Shape analysis](w:en:Shape_analysis_(software) "Shape analysis (software)") of [linked list](w:en) data structures is a technique for verifying the correctness of an algorithm using those structures. If a node in the list incorrectly points to an earlier node in the same list, the structure will form a cycle that can be detected by these algorithms.[\[25\]](https://en.wikipedia.org/wiki/Cycle_detection#cite_note-25) In [Common Lisp](w:en "Common Lisp"), the [S-expression](w:en) printer, under control of the `*print-circle*` variable, detects circular list structure and prints it compactly.
- Teske[\[14\]](https://en.wikipedia.org/wiki/Cycle_detection#cite_note-teske-14) describes applications in [computational group theory](w:en): determining the structure of an [Abelian group](w:en "Abelian group") from a set of its generators. The cryptographic algorithms of Kaliski et al.[\[22\]](https://en.wikipedia.org/wiki/Cycle_detection#cite_note-krs-22) may also be viewed as attempting to infer the structure of an unknown group.
- [Fich (1981)](w:en:Cycle_detection#CITEREFFich1981) briefly mentions an application to [computer simulation](w:en "Computer simulation") of [celestial mechanics](w:en "Celestial mechanics"), which she attributes to [William Kahan](w:en "William Kahan"). In this application, cycle detection in the [phase space](w:en) of an orbital system may be used to determine whether the system is periodic to within the accuracy of the simulation.[\[18\]](https://en.wikipedia.org/wiki/Cycle_detection#cite_note-fich-18)

## La détection de cycle

Partant du principe "qui peut le plus peut le moins"

## Back to Pisano

Pour résoudre le "problème idiot", il suffit donc de déterminer la période de Pisano correspondant à m=1000000007, ce qui m'a mené au problème de déterminer l'apparition d'un cycle dans une suite, plus touffu qu'il n'y parait

qui ouvre une autre voie pour résoudre le "problème idiot" posé.

En effet, [Lagrange](w:Joseph_Louis_Lagrange) ayant montré en 1774 que les suites de Fibonacci modulo m sont cycliques, il suffit de connaitre un cycle, ou même seulement la période p du cycle pour calculer le n-ième terme hyper rapidement quel que soit n.

Par exemple si je cherche le fameux 1019 ième terme mais modulo 10 pour commencer, je consulte [A001175](https://oeis.org/A001175) qui me dit que pour m=10, la période p=60. Je calcule alors  n mod p = 1019 mod 60 = 40 et je sais alors que le 1019 ième terme est égal au 41 ième\*\*, que je peux calculer très vite ou trouver directement dans [A003893](https://oeis.org/A003893) : c'est 5 .

La question devient : comment trouver la période de Pisano correspondant à un m quelconque, par exemple 10 ou 1000000007 ?

## Algorithme du Lièvre et de la Tortue

 

https://en.wikipedia.org/wiki/Cycle\_detection

https://rosettacode.org/wiki/Cycle\_detection#Python

http://stackoverflow.com/questions/10441715/finding-a-repeating-sequence-at-the-end-of-a-sequence-of-numbers

https://discuss.leetcode.com/topic/10398/rolling-hash-ac-python-solution

http://stackoverflow.com/questions/22216948/python-rabin-karp-algorithm-hashing

http://stackoverflow.com/questions/711770/fast-implementation-of-rolling-hash

https://rosettacode.org/wiki/Cycle\_detection

http://www.gabrielnivasch.org/fun/cycle-detection

http://www.markandclick.com/advance.html#SubString

 

 

1. Floyd's algorithm (_The Art of Computer Programming_, vol. 2, exercise 3.1-6).
2. Gosper's algorithm ([_HAKMEM_, item 132](http://www.inwap.com/pdp10/hbaker/hakmem/flows.html#item132)).
3. Brent's algorithm ("An improved Monte Carlo factorization algorithm", _BIT_ 20, pp. 176-184, 1980).
4. Sedgewick, Szymanski, and Yao's algorithm ("The complexity of finding cycles in periodic functions", _SIAM J. Comput._ 11 (2), pp. 376-390, 1982).
5. The "distinguished point" method (Quisquater and Delescaille, "How easy is collision search? Application to DES", _Eurocrypt '89_, [LNCS 434, pp. 429-434](https://web.archive.org/web/20191212040827/http://www.springerlink.de/openurl.asp?genre=article&issn=0302-9743&volume=434&spage=429)).

 

Si elle est courte, la méthode ci-dessus pourrait même être plus rapide que l'exponentiation modulaire de matrices décrite dans [l'article](/2017/04/25/comment-calculer-le-1e19-eme-terme-de-la-suite-de-fibonacci/). Mais elle pourrait aussi être

 

 

obtenir le n-ième terme modulo m

Il m'a semblé très logique de rechercher la période correspondant

 

Note\* : "Pisano" signifie "de Pise" et était un des noms de [Leonardo Fibonacci](w:)

\*\* parce que l'opération modulo peut donner 0, mais les humains indicent les listes à partir de 1...
