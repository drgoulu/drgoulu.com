---
title: Quel est l’interêt d’utiliser une modélisation numérique pour résoudre des équations différencielles en mechanique et quelles en sont les limites ?
slug: quel-est-linteret-dutiliser-une-modelisation-numerique-pour-resoudre-des-equations-differencielles-en-mechanique-et-quelles-en-sont-les-limites
date: '2021-03-02'
draft: false
categories:
- Quora
tags:
- physique
- informatique
- modelisation
- equations-differentielles
- simulation-numerique
- mathematiques-appliquees
- mecanique
- analyse-numerique
- physique-mathematique
- modelisation-mathematique
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Quel-est-l-inter%C3%AAt-d-utiliser-une-mod%C3%A9lisation-num%C3%A9rique-pour-r%C3%A9soudre-des-%C3%A9quations-diff%C3%A9rencielles-en-mechanique-et-quelles-en-sont-les-limites/answer/Dr-Goulu)*

A part pour des cas très simples (poutre encastrée, sur deux appuis etc) il n'y a pas de solutions analytiques de ces équations.

La [méthode des éléments finis](w:) permet de ramener les cas plus complexes au cas simple de cubes (ou tétraèdres) soumis à différentes forces et moments. Pour des formes complexes, on se retrouve avec des millions d'éléments, ce qui exige évidemment des ordinateurs pour résoudre les systèmes d'équations correspondants, et aussi pour "mailler" les pièces en éléments approximant bien la géométrie, suffisamment nombreux dans les zones de contraintes, et "bien conditionnés" numériquement.

Les limites (de la précision du calcul) sont principalement liées à la modélisation des "conditions aux limites", soit la manière dont le système étudié est lié à son environnement. Par exemple on modélise trop facilement deux faces boulonnées comme collées, alors qu'en réalité la précontrainte du serrage est beaucoup plus complexe.

D'autre part, la résolution est simple et rapide pour les systèmes linéaires. Dès que votre système contient des éléments non linéaires (jeu mécanique par exemple) la résolution est beaucoup plus complexe, donc on a parfois tendance à "linéariser" un peu trop …
