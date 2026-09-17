---
title: Qu'est-ce que le web scraping avec Python ?
slug: qu-est-ce-que-le-web-scraping-avec-python
date: '2021-01-25'
draft: false
categories:
- Quora
tags:
- informatique
- web-scraping
- developpement-web
- python-langage-de-programmation
- collecte-de-donnees
- langages-de-programmation
- programmation-web
- acquisition-de-donnees
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Quest-ce-que-le-web-scraping-avec-Python/answer/Dr-Goulu)*

Le [Web scraping](w:)consiste à extraire automatiquement des informations de sites Web.

La librairie python [Beautiful Soup](w:)permet de faire ça facilement.

Attention si vous vous amusez à ça : le scraping peut être détecté par le site cible et même considéré comme une attaque. Ajoutez plein de pauses dont chaque durée est aléatoire pour que votre script ressemble le plus possible à un humain et modifiez l'agent HTTP utilisé dans les requêtes en adaptant la recette proposée dans [How to scrape a webpage using Beautiful Soup as if using Chrome?](https://stackoverflow.com/questions/47522957/how-to-scrape-a-webpage-using-beautiful-soup-as-if-using-chrome?rq=1) …
