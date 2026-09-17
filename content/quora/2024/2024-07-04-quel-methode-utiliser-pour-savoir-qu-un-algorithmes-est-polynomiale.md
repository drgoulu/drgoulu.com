---
title: Quel méthode utiliser pour savoir qu'un algorithmes est polynomiale ?
slug: quel-methode-utiliser-pour-savoir-qu-un-algorithmes-est-polynomiale
date: '2024-07-04'
draft: true
categories:
- Quora
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Quel-m%C3%A9thode-utiliser-pour-savoir-qu-un-algorithmes-est-polynomiale/answer/Dr-Goulu)*

Compter et vérifier les boucles imbriquées.

```
for i=1 to n // linéaire O(n)
  // pas de boucle

```

.

```
for i=1 to n // quadratique O(n^2)
  for j=1 to n
    // pas de boucle

```

.

```
while true
  i=i+1
  if (conditioncompliquee(i))
    break
// ça pue le non polynomial

```

Et si vous avez un algorithme récursif, il faut le "dérécursifier" mentalement ou par écrit pour voir si le nombre de récursions est borné par n, n^2, n.log(n) ou pas.
