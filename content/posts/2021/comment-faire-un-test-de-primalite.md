---
title: Comment faire un test de primalité ?
slug: comment-faire-un-test-de-primalite
date: '2021-04-29'
draft: false
categories:
- Comment
tags:
- mathematiques
- theorie
- informatique
- nombres
- securite
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Comment-faire-un-test-de-primalit%C3%A9/answer/Dr-Goulu)*

Ca dépend ce que vous appelez "faire un test de primalité".

Si vous avez un seul nombre à tester, vous allez sur [Wolfram|Alpha](https://www.wolframalpha.com/input/?i=is+23467230726309672075423546260650245923452348549027543723+prime) et vous tapez "is (le nombre) prime"

Si vous en avez plusieurs, vous pouvez installer Python et utiliser par exemple ma fonction [Goulib.math2.is_prime](https://goulib.readthedocs.io/en/latest/modules/Goulib.math2.html#Goulib.math2.is_prime) qui est très efficace (elle utilise le [Test de primalité de Miller-Rabin](w:)pour les "petits" nombres, et le [Baillie–PSW primality test](w:en:Baillie–PSW_primality_test) pour les grands)

Si vous en avez besoin dans un autre langage, par exemple en C pour un bidule cryptographique, vous pouvez aller sur [Rosetta code](https://rosettacode.org/wiki/Miller–Rabin_primality_test) par exemple

Et si vous voulez vraiment faire votre propre algorithme de test, alors vous allez devoir sérieusement étudier la théorie des nombres, avec les [Courbes elliptiques](w:Courbe_elliptique) et tout le toutim, et je vous souhaite bonne chance pour votre [Médaille Fields](w:) …

[https://www.drgoulu.com/2012/04/...](/2012/04/15/comment-produire-des-nombres-premiers/)
