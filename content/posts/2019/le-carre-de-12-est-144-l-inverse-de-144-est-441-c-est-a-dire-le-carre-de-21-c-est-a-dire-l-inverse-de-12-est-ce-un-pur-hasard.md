---
title: Le carré de 12 est 144. L'inverse de 144 est 441, c'est à dire le carré de 21, c'est à dire l'inverse de 12. Est-ce un pur hasard ?
slug: le-carre-de-12-est-144-l-inverse-de-144-est-441-c-est-a-dire-le-carre-de-21-c-est-a-dire-l-inverse-de-12-est-ce-un-pur-hasard
date: '2019-12-09'
draft: false
categories:
- Quora
tags:
- mathematiques
- curiosite
- nombres
- questions
- post
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Le-carr%C3%A9-de-12-est-144-Linverse-de-144-est-441-cest-%C3%A0-dire-le-carr%C3%A9-de-21-cest-%C3%A0-dire-linverse-de-12-Est-ce-un-pur-hasard/answer/Dr-Goulu)*

A ma grande surprise, la suite définie par [Miranda Umino](https://fr.quora.com/profile/Miranda-Umino) dans sa réponse ne figure pas encore dans [L'Encyclopédie en ligne des suites de nombres entiers](https://oeis.org/?language=french).

Il y a déjà :

- [A061457](https://oeis.org/A061457) qui contient les carrés qui sont toujours carrés lus à l'envers
- [A102859](https://oeis.org/A102859) qui contient les nombres dont les carrés sont dans A061457.

donc j'ai soumis à l'OEIS la nouvelle série qui devrait s’appeler A330287 après validation. *Edit : en fait la suite existait déjà, c'est*[*A061909*](https://oeis.org/A061909)*qui a une définition très différente mais produit les même nombres pour une raison mystérieuse*

et j'ai implanté tout ça dans mes [Suites infinies en Python](/2017/06/26/series-infinies-et-oeis-en-python/) :

```
A000290 = Sequence(None, lambda n: n * n, lambda n: is_square(n), 'squares') #existait déjà

A061457 = A000290.filter(lambda x:is_square(reverse(x)))
A061457.desc = "Numbers n such that n and its reversal are both squares."

A102859 = A061457.apply(isqrt,containf=lambda x:is_square(reverse(x * x)))
A102859.desc = "Numbers that when squared and written backwards give a square again"

A061457=A102859.filter(lambda x:reverse(x) in A102859)

```
