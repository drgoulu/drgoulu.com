---
title: Si je devais apprendre UN seul language de programmation pour avoir le plus de chance de rentrer dans une grande entreprise tel les GAFAM. Qu’elle language dois-je apprendre ?
slug: si-je-devais-apprendre-un-seul-language-de-programmation-pour-avoir-le-plus-de-chance-de-rentrer-dans-une-grande-entreprise-tel-les-gafam-quelle-language-dois-je-apprendre
date: '2020-06-25'
draft: false
categories:
- Quora
tags:
- entreprises
- langages-de-programmation
- carriere
- gafam
- emplois
- developpement-web
- carriere-professionnelle
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Si-je-devais-apprendre-UN-seul-language-de-programmation-pour-avoir-le-plus-de-chance-de-rentrer-dans-une-grande-entreprise-tel-les-GAFAM-Qu-elle-language-dois-je-apprendre/answer/Dr-Goulu)*

Vous ne devez pas apprendre un langage de programmation, vous devez apprendre à programmer.

C'est très différent.

Programmer c'est "penser machine" : arriver à décomposer un cahier des charges en fonctions, données, flux, algorithmes, [patrons de conception](w:Patron_de_conception) etc. et plus ou moins comprendre comment ça va être exécuté pour pouvoir déboguer.

Ensuite le langage sert à exprimer tout ceci, mais

```
//TypeScript
function ca_sert(a:rien) {if(votre){code(); fait(nimporte)}; quoi();}

```

reste assez équivalent à

```
#python
def ca_sert(a:rien):
  if votre:
	code():
	fait(nimporte)
  quoi();

```

Les langages ça va ça vient avec les modes. La programmation reste.

Ok, il y a tout de même des différences entre les langages adaptés au front-end (interface web) et au back-end (ce qui tourne sur le serveur). Aujourd'hui je dirais:

- Python pour le back-end ( voir [les décorateurs, ou pourquoi j'aime toujours la programmation - Pourquoi Comment Combien](/2010/12/03/les-decorateurs-python/#.XvS9iyiiGCo) )
- TypeScript pour le front-end. Ces temps-ci je me mets aux [Composants web](w:) avec [Stencil](https://stenciljs.com/docs/introduction), et c'est cool ( il y a même des décorateurs …)
