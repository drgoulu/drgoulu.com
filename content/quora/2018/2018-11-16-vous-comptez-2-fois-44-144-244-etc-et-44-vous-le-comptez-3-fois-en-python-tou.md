---
title: vous comptez 2 fois 44, 144, 244 etc et 44 vous le comptez 3 fois …En python tou...
slug: vous-comptez-2-fois-44-144-244-etc-et-44-vous-le-comptez-3-fois-en-python-tou
date: '2018-11-16'
draft: true
categories:
- Quora
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Combien-de-fois-le-chiffre-4-apparaîtrait-il-de-1-à-1234/answer/Nabil-Doghri)*

vous comptez 2 fois 44, 144, 244 etc et 44 vous le comptez 3 fois …

En python toujours

print(sum([1 if '4' in str(x) else 0 for x in range(1234)]))

donne 312
