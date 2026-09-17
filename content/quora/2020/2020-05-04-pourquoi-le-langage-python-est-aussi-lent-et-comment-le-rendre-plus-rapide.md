---
title: Pourquoi le langage Python est aussi lent, et comment le rendre plus rapide ?
slug: pourquoi-le-langage-python-est-aussi-lent-et-comment-le-rendre-plus-rapide
date: '2020-05-04'
draft: true
categories:
- Pourquoi
- Comment
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Pourquoi-le-langage-Python-est-aussi-lent-et-comment-le-rendre-plus-rapide/answer/Dr-Goulu)*

Si vous le trouvez lent, c'est probablement que vous ne l'utilisez pas correctement.

Les fonctions nécessitant de la puissance de calcul sont disponibles dans des librairies compilées, comme numpy par exemple.

Identifiez les 20% de votre code qui prennent 80% du temps et cherchez une librairie qui le fait plus vite. Ou écrivez cette partie en C.
