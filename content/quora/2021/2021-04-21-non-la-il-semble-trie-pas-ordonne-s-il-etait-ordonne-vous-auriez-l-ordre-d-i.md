---
title: non. Là il semble trié, pas ordonné. S'il était ordonné, vous auriez l'ordre d'i...
slug: non-la-il-semble-trie-pas-ordonne-s-il-etait-ordonne-vous-auriez-l-ordre-d-i
date: '2021-04-21'
draft: false
categories:
- Quora
tags:
- informatique
- differences-et-similitudes
- ensembles-mathematiques
- python-langage-de-programmation
- langages-de-programmation
- structures-de-donnees
- programmation-python-javascript
- theorie-des-ensembles
- programmation-en-python
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Quelle-différence-y-a-t-il-entre-les-listes-et-les-ensembles-dans-Python/answer/Dr-Goulu)*

non. Là il semble trié, pas ordonné. S'il était ordonné, vous auriez l'ordre d'insertion {2, 3, 1, 5 ,4}, comme pour les listes, les tuples, ou les dict depuis la version 3.7.

La doc est très claire : [5. Structures de données](https://docs.python.org/fr/3/tutorial/datastructures.html#sets) : "Un ensemble est une collection non ordonnée sans élément dupliqué. "

dans votre exemple, comme vous n'utilisez que des nombres entiers consécutifs, la table de hachage correspondante est "par hasard" triée, mais regardez l'exemple de la doc:

>>> a = set('abracadabra')
>>> a
{'c', 'a', 'b', 'r', 'd'}

ce n'est ni l'ordre d'insertion ni trié …
