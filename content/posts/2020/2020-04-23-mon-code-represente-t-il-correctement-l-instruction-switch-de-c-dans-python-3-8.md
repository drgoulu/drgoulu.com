---
title: Mon code représente-t-il correctement l'instruction switch de C dans Python 3.8?
slug: mon-code-represente-t-il-correctement-l-instruction-switch-de-c-dans-python-3-8
date: '2020-04-23'
draft: true
categories:
- Quora
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Mon-code-repr%C3%A9sente-t-il-correctement-l-instruction-switch-de-C-dans-Python-3-8/answer/Dr-Goulu)*

Ouch ! Désolé ça fait mal aux yeux… Oubliez C, Python est un langage de BEAUCOUP plus haut niveau !

- les [dictionnaires](https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/232273-utilisez-des-dictionnaires) sont des structures très souples et hyper efficaces. Utilisez-les ! 9 fois sur 10 vous pouvez remplacer une boucle par une fonction prédéfinie de dict ou de list (dans votre code vous auriez pu utiliser [index](https://docs.python.org/fr/3/tutorial/datastructures.html) à la place de la boucle :

```
i=liste_valeurs.index(variable)

```

- [eval](https://docs.python.org/fr/3/library/functions.html#eval)est fait pour des applications très particulières, c'est dangereux, lent pas pratique. Ne l'utilisez pas. En python, il est super facile de passer une fonction en paramètre, ici en les stockant dans le dict
- n'utilisez pas print() dans des fonctions. Utilisez [logging](https://docs.python.org/fr/3/library/logging.html). Un jour vous me remercierez.
- vos fonctions doivent toujours renvoyer un résultat. Même si vous pensez que c'est inutile, faites le quand même et vous verrez que c'est très utile.
- formattez votre doc pour [Sphinx](https://www.sphinx-doc.org/en/master/) dès le départ.

donc voilà ma version, aussi compatible que possible avec la vôtre :

```
def switch(variable, dico, instruction_defaut=None):
    """fonctionne comme l'instruction switch de C ou C#
    :param variable: any, variable à tester, ex : ma_variable
    :param dico: dictionnaire de fonctions à appeler indexées par la correspondante valeur de la variable
    les fonctions peuvent être soit des vraies fonctions python
    soit des str eval-uées pour compatibilité
    :param instruction_defaut: fonction à appeler si pas de correspondance
    :return: fonction executée"""

    # le dictionnaire est LA structure méga puissante en Python
    # et le "duck typing" est très utilisé :
    try:
        f = dico[variable]
    except KeyError:
        f = instruction_defaut

    # on aurait aussi pu faire du duck typing, mais isinstance est utile aussi
    if f is None:
        res = None
    elif isinstance(f, str):
        res = eval(f)
    else:  # si pas None, part de l'idée que c'est une fonction
        res = f()
    return res  # on renvoie ce qu'on a evalué, dans tous les cas

```

- écrivez des tests. Toujours. Une bonne pratique est même d'écrire les tests avant la fonction, comme ça vous êtes forcé d'écrire une fonction qui marche

```
# tests:
def f(): return "une fonction"

# si vous aimez le C, ça peut ressembler à du C :

i = 2
r = switch(i, {
    1:"print(1)",   # sera evalu-uée
    'a':f,          # une fonction normale avec ce que vous voulez
    2:lambda :'a'   # une fonction "lambda" courte
    },
    "print('pas dans le dico')"
)
assert(r=='a') # en principe on teste comme ça

# mais les {} englobent en fait un dictionnaire
d = {1:"print(1)", 'a':f} # qui peut être statique
d[2]=lambda :'a' # ou créé dynamiquement

switch(1, d) # imprime 1 tout seul par le eval
print(switch(2, d))
switch(3, d, "print('pas dans le dico')")  # test de la fonction par défaut
print(switch('a', d, f))
print(switch('b', d))  # pas de fonction par défaut : renvoie None

print(switch(switch(2, d), d))  # ben oui quoi... ça sert à ça des valeurs retournées

```

- utilisez plutôt un[gist](https://gist.github.com/) que drive pour du code… ça permet de l'éditer, de commenter etc.
- pas sur que Quora soit le meilleur endroit pour un cours de python …
- Persévérez! Mais commencer par lire la [Documentation](https://docs.python.org/fr/3/) svp. Elle est extrêmement bien faite. Et commencez par [le tutoriel Python](https://docs.python.org/fr/3/tutorial/index.html), ça vaut vraiment le coup.
- Et n'essayez pas de faire ressembler python à C. Python ressemble à un langage écrit 20 ans plus tard, c'est pas pour rien …
