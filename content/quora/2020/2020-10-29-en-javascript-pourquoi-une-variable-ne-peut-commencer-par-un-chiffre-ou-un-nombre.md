---
title: En Javascript, pourquoi une variable ne peut commencer par un chiffre ou un nombre ?
slug: en-javascript-pourquoi-une-variable-ne-peut-commencer-par-un-chiffre-ou-un-nombre
date: '2020-10-29'
draft: false
categories:
- Pourquoi
tags:
- developpement-web
- langages-de-programmation
- variables
- developpement-logiciel
- javascript
- nom-de-variable
- programmation-web
- syntaxe-langages-de-programmation
- developpement-web-et-mobile
- langages-de-programmation-web
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/En-Javascript-pourquoi-une-variable-ne-peut-commencer-par-un-chiffre-ou-un-nombre/answer/Dr-Goulu)*

aucun langage de programmation à ma connaissance ne le permet.

l'[Analyse lexicale](w:)est beaucoup plus simple lorsqu'on peut simplement balayer le code de gauche à droite, chaque nouveau caractère permettant de construire le graphe. Si on permet aux variables de commencer par un chiffre, l'analyseur ne sait pas si il analyse une constante numérique ou un identificateur jusqu'aux caractères les plus à droite.

Et j'y pense après coup : permettre la variable 2x3 est déjà vachement dangereux tant ça ressemble à 2*3, mais alors 2E3, c'est quoi ? une variable, ou la constante 2000 ?
