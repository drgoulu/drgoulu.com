---
title: idem. mais Quora n'est pas le bon endroit pour parler programmation. StackAdviso...
slug: idem-mais-quora-n-est-pas-le-bon-endroit-pour-parler-programmation-stackadviso
date: '2021-10-04'
draft: false
categories:
- Quora
tags:
- langages-de-programmation
- developpement-logiciel
- python-3
- interfaces-en-ligne-de-commande
- python-langage-de-programmation
- scripting-python
- programmation-systeme
- developpement-de-logiciels
- langage-de-programmation
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Jessaie-de-créer-une-CLI-en-Python-3-mais-je-ne-sais-pas-par-où-commencer/answer/Dr-Goulu)*

idem. mais Quora n'est pas le bon endroit pour parler programmation. StackAdvisor est 1000 fois mieux.

je ne comprends toujours pas… Un "terminal" accepte des commandes, donc il fait un truc comme

```
parser = argparse.ArgumentParser()
# définir la syntaxe avec parser.add_argument(...)
while True:
  commande=input('nom@nom-du-terminal $')
  parser.convert_arg_line_to_args(commande)
  args = parser.parse_args()
  # faire qq chose avec les args ...

```

Si ça peut aider, j'avais fait un interpréteur de formules mathématiques [Goulib.expr module](https://goulib.readthedocs.io/en/latest/modules/Goulib.expr.html#module-Goulib.expr) basé sur [ast - Arbres Syntaxiques Abstraits](https://docs.python.org/fr/3/library/ast.html)…
