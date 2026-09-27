---
title: Pourquoi le bloc finally est exécuté avant except en python ?J'ai 13 ans et j'apprends python. j'ai mis une instruction raise sur un except et un print sur finally mais je vois que le finally s'éxecute avant.
slug: pourquoi-le-bloc-finally-est-execute-avant-except-en-python
date: '2023-02-25'
draft: false
categories:
- Pourquoi
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Pourquoi-le-bloc-finally-est-ex%C3%A9cut%C3%A9-avant-except-en-python-Jai-13-ans-et-japprends-python-jai-mis-une-instruction-raise-sur-un-except-et-un-print-sur-finally-mais-je-vois-que-le-finally-s/answer/Dr-Goulu)*

D'abord bravo, une question de ce niveau à 13 ans, ça montre que tu n'es pas un débutant…

il faut distinguer la "levée de l'exception" dans le bloc except et la "reprise de l'exception" dans le code appelant.

Voici un petit exemple :

```
def test(a):
    try:
        print("j'essaie de diviser par", a)
        x = 1 / a
    except ZeroDivisionError:
        print("ya un problème...")
        raise Exception("division par zéro")
    else:
        print("pas d'erreur")
    finally:
        print("fini")
try:
    test(0)
except Exception as e:
    print(e)

```

il produit :

```
j'essaie de diviser par 0
ya un problème...
fini
division par zéro

```

ou tu vois :

- que le print du except est bien executé avant le finally dans la fonction
- et le print du except du programme principal imprime l'exception du raise

Python a une excellente documentation en français, parfois un peu technique, mais il y a tout là :

[https://docs.python.org/fr/3/tut...](https://docs.python.org/fr/3/tutorial/errors.html#handling-exceptions)

il y a un paragraphe qui dit :

> - Une exception peut se produire durant l'exécution d'une clause `except` ou `else`. Encore une fois, l'exception est reprise **après que la clause**`finally`**a été exécutée**.

en fait en utilisant raise dans le bloc except , tu produis en réalité une 2eme exception dans le except, et cette exception sera reprise (= traitée dans le code appelant) après le bloc finally.
