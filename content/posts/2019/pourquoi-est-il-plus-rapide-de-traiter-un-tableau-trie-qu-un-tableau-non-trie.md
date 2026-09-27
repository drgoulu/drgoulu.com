---
title: Pourquoi est-il plus rapide de traiter un tableau trié qu'un tableau non trié ?
slug: pourquoi-est-il-plus-rapide-de-traiter-un-tableau-trie-qu-un-tableau-non-trie
date: '2019-04-25'
draft: true
categories:
- Pourquoi
tags: []
coverImage: ./images/quora.png
---

*Article initialement publié sur [Quora](https://fr.quora.com/Pourquoi-est-il-plus-rapide-de-traiter-un-tableau-tri%C3%A9-qu-un-tableau-non-tri%C3%A9/answer/Dr-Goulu)*

ça dépend du traitement. Si vous devez faire une opération pour chaque élément du tableau (l’afficher, le stocker, ajouter 5% d’intérêts aux dettes …) ça ne change rien.

A moins que vous ayez des éléments égaux, et dans ce cas s’ils sont triés vous pouvez éventuellement ne faire l’opération qu’une fois par élément distinct.

Ce qui est vraiment plus rapide avec un tableau trié, c’est la recherche, parce qu’on peut faire une [Recherche dichotomique](w:).
