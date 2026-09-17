---
title: Pourquoi Python est-il si lent à traiter les boucles "for" ?
slug: pourquoi-python-est-il-si-lent-a-traiter-les-boucles-for
date: '2020-05-16'
draft: true
categories:
- Pourquoi
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Pourquoi-Python-est-il-si-lent-%C3%A0-traiter-les-boucles-for/answer/Dr-Goulu)*

Si votre code doit être rapide, n'utilisez pas python.

Si vous voulez accélérer une boucle python:

1. vérifiez que vous devez vraiment utiliser une boucle for. Les librairies python contiennent beaucoup de fonctions comme map, sum ou index qui effectuent des boucles bien plus vite qu'en code
2. Utilisez des librairies compilées comme numpy pour le calcul matriciel, images etc
3. Au besoin, reecrivez juste la partie du code qui doit être rapide en un autre langage et appelez la depuis python.
