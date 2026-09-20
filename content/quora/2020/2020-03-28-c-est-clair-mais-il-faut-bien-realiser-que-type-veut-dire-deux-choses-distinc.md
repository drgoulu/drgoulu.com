---
title: C'est clair. Mais il faut bien réaliser que "typé" veut dire deux choses distinc...
slug: c-est-clair-mais-il-faut-bien-realiser-que-type-veut-dire-deux-choses-distinc
date: '2020-03-28'
draft: false
categories:
- Quora
tags:
- informatique
- python-langage-de-programmation
- developpement-logiciel
- statique
- langages-de-programmation
- science-de-l-informatique
- programmation-en-python
- informatique-general
- langage-de-programmation
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Pensez-vous-que-Python-va-devenir-un-langage-statiquement-typé/answer/Dr-Goulu)*

C'est clair. Mais il faut bien réaliser que "typé" veut dire deux choses distinctes:

1. Que le compilateur / interpréteur /analyseur syntaxique de l'ide vérifie que les types des paramètres effectifs passés aux fonctions et opérateurs correspond aux declarations
2. Que l'implémentation des différents types est différente, voire optimisée. En C, Java ou autre, un int ne prend que 4 bytes, peut être passé en registre etc. alors qu'une string est un pointeur vers un buffer contenant des bytes avec un 0 à la fin.

Python n'est définitivement pas 2, puisque tout est objet avec un dictionnaire de méthodes, et les variables sont en fait des références comptées. La performance est plus faible, mais on a pas à se faire ch… avec malloc…

Ma réponse dit que python peut être 1 si on veut, et c:est souvent ce qu'on veut…
