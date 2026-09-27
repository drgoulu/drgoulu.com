---
title: Quel est l’algorithme de compression de texte avec le meilleur ratio facilement implementable en C ?
slug: quel-est-lalgorithme-de-compression-de-texte-avec-le-meilleur-ratio-facilement-implementable-en-c
date: '2021-12-21'
draft: false
categories:
- Quora
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Quel-est-l-algorithme-de-compression-de-texte-avec-le-meilleur-ratio-facilement-implementable-en-C/answer/Dr-Goulu)*

pour du texte la compression [LZW (.zip et similaire)](w:Lempel-Ziv-Welch)donne le meilleur taux de compression parce qu'elle construit un dictionnaire des mots fréquemment utilisés.

Le code prend environ 4 pages de C , voir par exemple

[https://rosettacode.org/wiki/LZW...](https://rosettacode.org/wiki/LZW_compression#C)

mais par pitié ne la réécrivez pas une fois de plus. Il y a 70 repos de compression LZW en C [sur GitHub](https://github.com/search?l=C&q=lzw+compression+c&type=Repositories) …
