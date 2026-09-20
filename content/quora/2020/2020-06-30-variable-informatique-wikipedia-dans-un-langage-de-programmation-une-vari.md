---
title: Variable (informatique) — Wikipédia :"Dans un langage de programmation, une vari...
slug: variable-informatique-wikipedia-dans-un-langage-de-programmation-une-vari
date: '2020-06-30'
draft: false
categories:
- Quora
tags:
- langages-de-programmation
- developpement-logiciel
- variables
- python-langage-de-programmation
- ingenierie-logicielle
- programmation-en-python
- creation-logicielle
- developpement-informatique
- developpement-de-logiciels
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Est-il-possible-de-créer-un-logiciel-en-Python-sans-variables-Si-possible-comment/answer/Dr-Goulu)*

[Variable (informatique) — Wikipédia](w:Variable_(informatique)) :

"Dans un langage de programmation, une variable est un espace de stockage pour un résultat.".

Ben pas en Python, justement, puisque deux références peuvent référencer le même "stockage pour un résultat".

de même la notion de type s'applique à l'objet, pas à la référence.

donc non, Python n'a pas de variables. Il a des références à des variables internes si vous voulez, que vous pouvez utiliser comme des variables si vous voulez, mais les considérer d'emblée comme des références vous évitera bien des hésitations, voire des bugs…
