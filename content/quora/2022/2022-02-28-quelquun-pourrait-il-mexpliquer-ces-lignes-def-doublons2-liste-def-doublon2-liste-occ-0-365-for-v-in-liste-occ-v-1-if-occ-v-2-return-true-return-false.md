---
title: 'Quelqu’un pourrait il m’expliquer ces lignes def doublons2 (liste): def doublon2 (liste): occ = [0] *365 for v in liste : occ [v] += 1 if occ [v] == 2: return True return False ?'
slug: quelquun-pourrait-il-mexpliquer-ces-lignes-def-doublons2-liste-def-doublon2-liste-occ-0-365-for-v-in-liste-occ-v-1-if-occ-v-2-return-true-return-false
date: '2022-02-28'
draft: false
categories:
- Quora
tags:
- algorithmes
- python-langage-de-programmation
- fonctions
- detection-d-anomalies
- developpeurs-python
- fonction-booleenne
- programmation-en-python
- versions-de-python
- algorithmes-numeriques
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Quelqu-un-pourrait-il-m-expliquer-ces-lignes-def-doublons2-liste-def-doublon2-liste-occ-0-365-for-v-in-liste-occ-v-1-if-occ-v-2-return-True-return-False/answer/Dr-Goulu)*

en Python l'indentation est significative donc je mets celle qui me semble correcte:

```
def doublon2 (liste):
  occ = [0] *365
  for v in liste :
    occ[v] += 1
    if occ[v] == 2:
      return True
  return False

```

ligne:

1. définit la fonction doublon2 qui renvoie True (ligne 6) si deux éléments de la liste sont identiques, False (kigne 7) sinon
2. créée une liste temporaire occ(urences) de 365 zéros ( [0,0,0…0] avec 365 zéros)
3. prend chaque élément v de la liste successivement
4. incrémente le v-ième élément de occ. En passant ceci force les éléments de la liste passée en paramètre à être des entiers entre 0 et 364, ce qui est un peu dommage. voir plus bas pour une alternative plus élégante
5. si occ[v] vaut 2, c'est qu'on a un doublon
6. alors on renvoie True. Là aussi c'est un peu dommage : return v serait plus instructif sur le doublon
7. sinon, après avoir parcouru toute la liste, on renvoie False

Ma version qui marche avec n'importe des listes contenant n'importe quoi, de n'importe quelle longueur, en remplaçant la liste occ par un ensemble:

```
def doublon2 (liste):
  occ = set()
  for v in liste :
    if v in occ:
      return v
    occ.add(v)
  return None

```
