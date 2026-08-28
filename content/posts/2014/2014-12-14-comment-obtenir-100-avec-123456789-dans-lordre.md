---
title: "Comment obtenir 100 avec 1,2,3,4,5,6,7,8,9 dans l'ordre ?"
slug: "comment-obtenir-100-avec-123456789-dans-lordre"
date: 2014-12-14
categories: 
  - "cat2"
tags: 
  - "jeux"
  - "maths"
coverImage: "5a68bb5e66369fdad9b2faaddf73c871.jpg"
---

[![Srinivasa Ramanujan est célèbre pour des formules très surprenantes du genre de celle exposée dans cet article](images/5a68bb5e66369fdad9b2faaddf73c871.jpg "Srinivasa Ramanujan est célèbre pour des formules très surprenantes du genre de celle exposée dans cet article")](https://fr.wikipedia.org/wiki/Srinivasa_Ramanujan)

A la recherche d'un petit article vite fait, j'ai vu [ce problème sur Quora](https://www.quora.com/Mathematical-Puzzles/Can-you-make-100-out-of-the-digits-1-2-3-4-5-6-7-8-9-in-order) et je me suis dit : soit c'est encore un "[jeu de l'année](/2012/01/18/jeu-de-lannee-2012-et-autres-cest-fini/)" , soit il y a un piège [genre 33](/2012/06/20/comment-dire-33-avec-3-cubes/). Alors je l'ai lu, et ça n'avait pas l'air trop difficile, vu le nombre de solutions proposées:\[mathjax\]

- \\(1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 \* 9\\)
- \\(123 - 45 - 67 + 89\\)
- \\(1^{2345} + 6 \* (7 + 8) + 9\\)
- \\(- 1 + 2^{3 + 4} - 5 + 67 - 89\\)
- \\(1\* (2 + 3) \* 4 \* 5 \* (6 - 7) \* (8 - 9)\\)
- et des dizaines d'autres variantes

Evidemment, le même problème a été posé pour [200](https://www.quora.com/Can-you-make-200-using-the-digits-1-2-3-4-5-6-7-8-9-in-order), [300](https://www.quora.com/Can-you-make-300-using-the-digits-1-2-3-4-5-6-7-8-9-in-order),[1000](https://www.quora.com/Can-you-make-1000-using-the-digits-1-2-3-4-5-6-7-8-9-in-order), [10000](https://www.quora.com/How-can-one-make-10-000-out-of-the-digits-1-2-3-4-5-6-7-8-and-9-in-order) et pourrait l'être pour [1548, 1729](/2008/08/24/nombres-acratopeges/) ou n'importe quel autre entier, mais [Michal Forišek](http://people.ksp.sk/~misof/cv.php?newlanguage=ENG) a fait très fort en proposant une solution générale, valable pour tout N :

\\(N= - \\log\_{1\\cdot 2} \\left( \\log\_{3+4-5} \\sqrt{ \\sqrt{ \\cdots \\sqrt{-6+7-8+9}}}\\right)\\) où l'expression comporte N racines imbriquées.

L'astuce, c'est que \\(\\sqrt{ \\sqrt{ \\cdots \\sqrt{2}}} = 2^{(1/2)^N} = 2^{2^{-N}}\\), donc il suffit d'en prendre deux fois le logarithme base 2 pour obtenir -N .

Bon ça ne va pas simplifier mon programme python qui résout ce genre de problèmes, mais c'est génial, non ?
