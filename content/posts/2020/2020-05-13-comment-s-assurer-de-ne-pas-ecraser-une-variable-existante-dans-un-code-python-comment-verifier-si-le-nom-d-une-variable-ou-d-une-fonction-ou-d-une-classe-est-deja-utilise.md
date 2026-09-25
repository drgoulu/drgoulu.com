---
title: Comment s'assurer de ne pas écraser une variable existante dans un code Python ? Comment vérifier si le nom d'une variable ou d'une fonction ou d'une classe est déjà utilisé ?
slug: comment-s-assurer-de-ne-pas-ecraser-une-variable-existante-dans-un-code-python-comment-verifier-si-le-nom-d-une-variable-ou-d-une-fonction-ou-d-une-classe-est-deja-utilise
date: '2020-05-13'
draft: false
categories:
- Comment
tags:
- informatique
- programmation
- developpement
- python
- developpement-logiciel
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Comment-sassurer-de-ne-pas-%C3%A9craser-une-variable-existante-dans-un-code-Python-Comment-v%C3%A9rifier-si-le-nom-dune-variable-ou-dune-fonction-ou-dune-classe-est-d%C3%A9j%C3%A0-utilis%C3%A9/answer/Dr-Goulu)*

Il n'y a pas de variables en python. Il n'y a que des références (des sortes de pointeurs) à des objets :

```
a=2 # a pointe sur l'objet int 2
a="hello" # maintenant a pointe sur la str

```

Aucun langage n'empêche d'assigner un objet à une référence à un autre objet, Python ne fait pas exception ;-)

La bonne pratique est de faire des fonctions et méthodes très courtes (max un écran) ce qui force à avoir des références valides sur un scope très court, ce qui évite le problème que vous mentionnez.

Accessoirement, Python force à préfixer les références à des champs (par self.), ce qui permet par exemple

```
class C:
  def __init__(self, a) :
    self.a=a # crée un champ a

```

Dans le même genre d'idée évitez à tout prix

```
from math import *
from vache import *
périmètre = pi * rayon

```

Parce que si vache à défini pi=4, vous serez mal…

```
from math import pi
from vache import pis
périmètre = pi * rayon

```

Maintenant si vous voulez vraiment savoir si une référence existe, et commencer à comprendre pourquoi python est un langage pour adultes consentants, lisez la suite

La fonction dir permet d'obtenir la liste des références définies

```
a=2
class C:
  pass

dir() # sans paramètres, renvoie les références globales

```

['C', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a']

Vous pouvez donc tester l'existence d'une référence globale avec:

```
'a' in dir() # renvoie True
'b' in dir() # renvoie False

```

Mais ce n'est pas pratique car vous devez avoir le nom de la référence en str. Et non, l'objet n'a pas cette str en mémoire par plusieurs références peuvent pointer sur le même objet…

Donc il vaut mieux faire comme ça :

```
try:
  b
except NameError: # n'existe pas
  b=a # seconde référence sur l'objet 2

```

Sinon :

```
dir(C) # références définies dans l'objet C (qui est une classe)

```

['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']

la fonction [hasattr](https://docs.python.org/fr/3/library/functions.html#hasattr) permet de savoir si un champ existe dans un objet.

Pour finir, voici une drôle de manière de créer une variable globale:

```
globals()['b']=3
b # existe ! Et vaut 3

```

Juste pour illustrer le fait que toutes les références sont gérées par des dictionnaires, donc dynamiquement modifiables et extensibles.

Et ça, ya pas beaucoup de langages qui le font…
