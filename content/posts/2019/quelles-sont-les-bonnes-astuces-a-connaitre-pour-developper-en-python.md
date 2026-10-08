---
title: Quelles sont les bonnes astuces à connaître pour développer en Python ?
slug: quelles-sont-les-bonnes-astuces-a-connaitre-pour-developper-en-python
date: '2019-10-01'
draft: false
categories:
- Quora
tags:
- informatique
- programmation
- langage
- python
- developpement-logiciel
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Quelles-sont-les-bonnes-astuces-%C3%A0-conna%C3%AEtre-pour-d%C3%A9velopper-en-Python/answer/Dr-Goulu)*

1. Pour du dev sérieux, utiliser la distribution [Anaconda](https://www.anaconda.com/distribution/) et un IDE comme PyCharm, VSCode, ou un Eclipse avec PyDev comme [LiClipse](https://www.liclipse.com/) par exemple.
2. Définir un e[nvironnement virtuel](https://docs.python.org/fr/3/tutorial/venv.html) par projet et y installer uniquement les packages nécessaires. [Conda est mieux que Pip](https://web.archive.org/web/20190920165049/https://www.anaconda.com/understanding-conda-and-pip/) pour les gros projets.
3. Vraiment bien comprendre que tout est objet, et que les "variables" sont en fait des références à des objets. Si vous ne comprenez pas pourquoi :

```
>>> a=[1,2,3]
>>> b=a
>>> a.append(4)
>>> b
[1, 2, 3, 4]
```

alors révisez [le modèle de données](https://docs.python.org/fr/3/reference/datamodel.html) avant de coder.
4. Vraiment bien comprendre que les objets sont définis par leur [__dict__](https://docs.python.org/fr/3/library/stdtypes.html#object.__dict__) , qui gère l'héritage et tout et tout.
5. Comprendre les [générateurs](https://docs.python.org/fr/3/glossary.html#term-generator) ( instruction [yield](https://docs.python.org/fr/3/reference/simple_stmts.html#yield)), et la notion sous jacente d'itérateur.
6. Connaître l'existence de toutes les librairies de [La bibliothèque standard](https://docs.python.org/fr/3/library/) Python. Il y a très probablement déjà là des briques importantes de votre futur programme.
7. Cherchez les autres briques sur [PyPI](https://pypi.org/) avant de réinventer la roue.
8. Have fun ! N'oubliez pas de faire un petit
`>>> import antigravity`
de temps en temps :-)
