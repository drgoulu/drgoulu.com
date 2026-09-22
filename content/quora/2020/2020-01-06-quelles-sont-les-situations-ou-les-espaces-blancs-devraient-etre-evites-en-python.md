---
title: Quelles sont les situations où les espaces blancs devraient être évités en Python ?
slug: quelles-sont-les-situations-ou-les-espaces-blancs-devraient-etre-evites-en-python
date: '2020-01-06'
draft: false
categories:
- Quora
tags:
- programmation
- langage
- conseils
- python
- developpement-logiciel
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Quelles-sont-les-situations-o%C3%B9-les-espaces-blancs-devraient-%C3%AAtre-%C3%A9vit%C3%A9s-en-Python/answer/Dr-Goulu)*

Les recommandations sont dans le [PEP 8](https://www.python.org/dev/peps/pep-0008/#whitespace-in-expressions-and-statements). Utilisez un IDE qui formate le code de cette manière.

A ma connaissance il n'existe aucun cas ou un espace peut provoquer un équivoque, à part la fameuse indentation bien sur…

Comme j'ai déjà eu l'occasion de le dire, l'indentation Python encourage vraiment à écrire de petites fonction et de petits blocs. Ma règle personnelle est de ne jamais imbriquer plus de 3 niveaux dans une fonction, et de ne jamais faire de fonction plus longue qu'un écran. Et de ne pas utiliser d'écran en mode portrait…
