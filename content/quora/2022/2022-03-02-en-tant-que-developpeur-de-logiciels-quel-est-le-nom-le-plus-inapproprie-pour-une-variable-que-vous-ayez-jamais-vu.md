---
title: En tant que développeur de logiciels, quel est le nom le plus inapproprié pour une variable que vous ayez jamais vu?
slug: en-tant-que-developpeur-de-logiciels-quel-est-le-nom-le-plus-inapproprie-pour-une-variable-que-vous-ayez-jamais-vu
date: '2022-03-02'
draft: false
categories:
- Quora
tags:
- informatique
- variables
- developpement-web
- langages-de-programmation
- noms-de-variables
- developpement-logiciel
- sciences-informatiques
- developpement-de-logiciels
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/En-tant-que-d%C3%A9veloppeur-de-logiciels-quel-est-le-nom-le-plus-inappropri%C3%A9-pour-une-variable-que-vous-ayez-jamais-vu/answer/Dr-Goulu)*

pas directement une variable mais

```
for m in `14**7*9`

```

dans du code Python 2.

D'abord on se dit que m va itérer dans les caractères de la chaîne '14**7*9' mais ça n'a aucun sens dans le contexte.

Ensuite on remarque les "backquotes" `…` au lieu des apostrophes et on découvre que c'est un alias de la fonction [repr](https://docs.python.org/3.4/library/functions.html?highlight=repr#repr) qui renvoie une chaîne représentant le paramètre,

et comme ** est l'opérateur d’exponentiation et que 14**7*9=948721536

ben m va itérer dans la chaîne "948721536" qui contient une seule fois chaque chiffre de 1 à 9, ce qui est utile au [Sudoku](/2008/10/12/python/) !

D'accord, c'est presque de l'obfuscation, mais là le but est plutôt d'utiliser le moins de caractères possibles …
