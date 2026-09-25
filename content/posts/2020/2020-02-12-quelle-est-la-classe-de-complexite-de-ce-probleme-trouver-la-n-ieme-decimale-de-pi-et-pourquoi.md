---
title: 'Quelle est la classe de complexité de ce problème : trouver la $n$-ième décimale de $\pi$, et pourquoi ?'
slug: quelle-est-la-classe-de-complexite-de-ce-probleme-trouver-la-n-ieme-decimale-de-pi-et-pourquoi
date: '2020-02-12'
draft: false
categories:
- Pourquoi
tags:
- sciences
- mathematiques
- theorie
- informatique
- temps
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Quelle-est-la-classe-de-complexit%C3%A9-de-ce-probl%C3%A8me-trouver-la-n-i%C3%A8me-d%C3%A9cimale-de-pi-et-pourquoi/answer/Dr-Goulu)*

En base 2 ou base 16, c'est $O(n.log(n)^3)$ en utilisant la fabuleuse [Formule BBP](w:)

En base 10:

> aucune formule réellement efficace n'a été découverte pour calculer le *n*-ième chiffre de π en base 10. [Simon Plouffe](w:) a mis au point en décembre [1996](w:), à partir d'une très ancienne série de calcul de π basée sur les coefficients du [binôme de Newton](w:), une méthode pour calculer les chiffres en base 10, mais sa complexité en $O(n^3.log(n))$ la rendait en pratique inutilisable. [Fabrice Bellard](w:) a bien amélioré l'algorithme pour atteindre une complexité en$O(n^2)$, mais cela n'est pas suffisant pour concurrencer les méthodes classiques de calcul de toutes les décimales.
