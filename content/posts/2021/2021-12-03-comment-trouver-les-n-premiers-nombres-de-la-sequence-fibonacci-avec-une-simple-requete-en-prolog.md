---
title: Comment trouver les n premiers nombres de la séquence Fibonacci avec une simple requête en Prolog ?
slug: comment-trouver-les-n-premiers-nombres-de-la-sequence-fibonacci-avec-une-simple-requete-en-prolog
date: '2021-12-03'
draft: true
categories:
- Comment
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Comment-trouver-les-n-premiers-nombres-de-la-s%C3%A9quence-Fibonacci-avec-une-simple-requ%C3%AAte-en-Prolog/answer/Dr-Goulu)*

```
fib(1, 1) :- !.
fib(0, 0) :- !.
fib(N, Value) :-
  A is N - 1, fib(A, A1),
  B is N - 2, fib(B, B1),
  Value is A1 + B1.

```

Source : [Rosetta Code](https://rosettacode.org/wiki/Category:Prolog), le site à connaître pour ce genre de questions
