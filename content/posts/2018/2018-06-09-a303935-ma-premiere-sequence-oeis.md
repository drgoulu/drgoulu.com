---
title: "A303935 , ma première suite OEIS"
slug: "a303935-ma-premiere-sequence-oeis"
date: 2018-06-09
categories:
  - "Comment"
tags: 
  - "nombres"
  - "oeis"
  - "python"
coverImage: "euler-level2-2.png"
---

{{< figure src="images/euler-level2-2.png" >}}

Depuis le temps que je joue avec l'['Encyclopédie en ligne des Suites de Nombres Entiers](https://oeis.org/Seis.html) ([OEIS](w:)), ça a fini par arriver : j'ai réussi à y ajouter une nouvelle suite,  [A303935](https://oeis.org/A303935) !

Tout a commencé avec le [Problème 74 du Project Euler](https://projecteuler.net/problem=74), qui traite de la somme des factorielles des chiffres (dfs) des nombres  ([A061602](https://oeis.org/A061602)). Seuls quatre d'entre eux appelés [factorion](w:) sont égaux à la somme des factorielles de leurs chiffres : 1, 2, 145 et 40585  ([A014080](https://oeis.org/A014080)).

Quelqu'un a prouvé en 2004 \[1\] que l'application répétée de la fonction dfs atteint immanquablement un des 4 factorions ou l'une des trois seules et uniques "boucles" suivantes:

169 → 363601 → 1454 → 169 871 → 45361 → 871 872 → 45362 → 872

Ne restait plus qu'à compter la longueur de l' [orbite](w:Action_de_groupe_(mathématiques)#Orbite) de dfs(n), et c'est précisément ce que liste [A303935](https://oeis.org/A303935), qui n'était pas encore répertoriée dans l'OEIS.

## Publier dans l'OEIS, c'est du sérieux.

Le processus de publication dans l'OEIS est très strict, sur le modèle de certaines publications scientifiques. "The standards are those of a mathematics reference work." comme ils le mentionnent.

Après s'[être enregistré](https://oeis.org/wiki/Special:RequestAccount) il faut préparer tout le contenu comme pour un "papier", en citant d'autres séries liées et des publications scientifiques.  Ensuite des "reviewers" ne se privent pas de demander des précisions et clarifications, voire de corriger la ponctuation... C'est vraiment strict, et ça peut prendre un mois, [comme dans le cas présent](https://oeis.org/history?seq=A303935&start=30) qui a nécessité 40 itérations avant publication.

J'ai failli abandonner car l'édition de [mon profil wiki dans l'OEIS](https://oeis.org/wiki/User:Philippe_Guglielmetti)  m'avait plutôt fait imaginer un processus collaboratif à la Wikipédia. Puis je me suis dit que puisque "ma" suite était connue depuis quelques années mais pas publiée dans l'OEIS, mes prédécesseurs avaient du se décourager, mais qu'il fallait que quelqu'un se sacrifie, alors voilà :

2, 1, 1, 16, 8, 10, 15, 32, 36, 35, 2, 2, 17, 33, 13, 10, 15, 32, 36, 35, 17, 17, 9, 37, 7, 12, 6, ... telle est désormais ma suite d'entiers préférée.

Et une référence "peer reviewed" de plus \[2\] !

## Et en Python ?

Le code suivant, tiré de [Goulib/examples/oeis.py](https://github.com/goulu/Goulib/blob/master/examples/oeis.py) , implante les trois suites mentionnées en Python, à l'aide de la [classe Sequence déjà décrite ici](/2017/06/26/series-infinies-et-oeis-en-python/).

\[python\] def dfs(n): return sum(map(factorial,digits(n)))

A061602=Sequence(0, dfs, desc="Sum of factorials of the digits of n")

A014080=Sequence(0,None,lambda n:dfs(n)==n)

def dfcl(n): l=set() i=n while i not in l: l.add(i) i=dfs(i) return len(l)

A303935=Sequence(0,dfcl) )\[/python\]

Ce code est suffisant pour calculer quelques milliers de termes de A303935, mais pour résoudre le problème 74 rapidement, il faut être légèrement plus subtil... Comme je ne donne pas de solutions aux Problèmes Euler, je vous laisse chercher...

En passant, ce problème était mon 100ème résolu, ce qui fait que je suis passé "Level 4 " ! ![](images/Dr_Goulu.png)

## Référence

1. Gupta, S. S. (2004). 88.31 Sum of the factorials of the digits of integers. The Mathematical Gazette, 88(512), 258–261. {{< altmetric doi="10.1017/S0025557200174996" >}}
2. Ph. Guglielmetti, Sequence [A303935](https://oeis.org/A303935) in _The On-Line Encyclopedia of Integer Sequences_ (2018), published electronically at [https://oeis.org](https://oeis.org/).
