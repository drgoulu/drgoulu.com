---
title: Qu'est-ce qu'un nombre premier ?
slug: qu-est-ce-qu-un-nombre-premier
date: '2021-02-02'
draft: false
categories:
- Quora
tags:
- sciences
- mathematiques
- theorie
- nombres
- nombres-premiers
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Quest-ce-quun-nombre-premier/answer/Dr-Goulu)*

C'est un nombre qui n'est pas un [Nombre composé.](w:Nombre_composé)

Je dis ça parce que les nombres premiers sont effectivement obtenus comme ça : par élimination des nombres composés. C'est le principe du [Crible d'Ératosthène](w:), mais aussi des [Tests de primalité](w:Test_de_primalité) déterministes, qui fonctionnent par élimination:

est-ce que 7133 est premier ?

- il est impair, donc ce n'est PAS un multiple de 2
- la somme de ses chiffres n'est pas un multiple de 3 donc ce n'est PAS un multiple de 3
- il ne se termine pas par 0 ou 5 donc ce n'est PAS un multiple de 5
- ah, il se divise par 7, donc c'est un multiple de 7…

Bref, le fait d'être un nombre premier n'est pas une propriété particulière, c'est plutôt une absence de propriété particulière. Et la question qu'on se pose depuis des siècles, c'est : est-il possible de trouver ces nombres sans procéder par élimination …

On dit souvent que les nombres premiers sont très utiles en cryptographie, mais en réalité ce sont plutôt les nombres composés de grands nombres premiers qui sont utiles, parce que faciles à produire, mais très difficiles à factoriser.

Il existe d'autre suites de nombres produites par d'autres cribles, par exemple les [Nombre chanceux](w:), qui ont des propriétés étonnamment proches de celles des nombres premiers, ce qui est étudié par la [Théorie des cribles](w:).

Sur ce thème :

[Comment trouver des nombres premiers - Pourquoi Comment Combien](/2012/04/15/comment-produire-des-nombres-premiers/#.YBpPJOhsOCo)

[Alice et Bob et les clés asymétriques - Pourquoi Comment Combien](/2017/02/15/alice-et-bob-et-les-cles-asymetriques/#.YBpPPOhsOCo)

[2019 passée au crible - Pourquoi Comment Combien](/2019/01/06/2019-passee-au-crible/#.YBpNBehsOCo)
