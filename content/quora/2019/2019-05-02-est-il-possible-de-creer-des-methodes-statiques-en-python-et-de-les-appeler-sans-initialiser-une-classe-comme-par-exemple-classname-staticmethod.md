---
title: 'Est-il possible de créer des méthodes statiques en Python et de les appeler sans initialiser une classe, comme par exemple : ClassName.StaticMethod ()?'
slug: est-il-possible-de-creer-des-methodes-statiques-en-python-et-de-les-appeler-sans-initialiser-une-classe-comme-par-exemple-classname-staticmethod
date: '2019-05-02'
draft: false
categories:
- Quora
tags:
- langages-de-programmation
- developpement-logiciel
- methodes
- classes-en-ligne
- constructeur-programmation-orientee-objet
- developpeurs-python
- python-langage-de-programmation
- programmation-orientee-objet
- programmation-en-python
coverImage: ./images/quora.png
---

*Article initialement publié sur [Quora](https://fr.quora.com/Est-il-possible-de-cr%C3%A9er-des-m%C3%A9thodes-statiques-en-Python-et-de-les-appeler-sans-initialiser-une-classe-comme-par-exemple-ClassName-StaticMethod/answer/Dr-Goulu)*

oui, ça se fait à l’aide du décorateur @staticmethod qui sert exactement à ça:

```
class MyClass:
    @staticmethod
    def staticmethod():
        return 'static method called'

```

on peut ensuite appeler soit

```
MyClass().staticmethod(); # crée un objet, puis appelle sa méthode qui est  statique

```

soit

```
MyClass.staticmethod(); # appelle directement la méthode statique

```

les décorateurs, c’est absolument génialement fabuleusement puissant et simple

[les décorateurs, ou pourquoi j'aime toujours la programmation - Pourquoi Comment Combien](https://www.drgoulu.com/2010/12/03/les-decorateurs-python/)
