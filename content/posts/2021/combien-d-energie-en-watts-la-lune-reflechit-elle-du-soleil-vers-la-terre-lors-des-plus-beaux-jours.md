---
title: Combien d'énergie (en watts) la lune réfléchit-elle du soleil vers la Terre lors des plus beaux jours ?
slug: combien-d-energie-en-watts-la-lune-reflechit-elle-du-soleil-vers-la-terre-lors-des-plus-beaux-jours
date: '2021-06-01'
draft: false
categories:
- Combien
tags:
- physique
- sciences
- astronomie
- astrophysique
- terre
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Combien-d%C3%A9nergie-en-watts-la-lune-r%C3%A9fl%C3%A9chit-elle-du-soleil-vers-la-Terre-lors-des-plus-beaux-jours/answer/Dr-Goulu)*

L'énergie se mesure en Joule, qui sont des watt-heure, ou plutôt en kilowatt-heures.

Le watt mesure une puissance.

Celà dit, en reprenant les équations de

[https://www.kartable.fr/ressourc...](https://www.kartable.fr/ressources/enseignement-scientifique/methode/calculer-la-puissance-du-rayonnement-solaire-recu-par-la-terre/51534)

On peut calculer la puissance du Soleil reçue par la lune avec

$P_{lune}=\frac{R_{lune}^2}{4 D_{soleil-lune}^2}\times P_{soleil}$

soit

$P_{lune}=\frac{1737100^2}{4(150\times 10^{9})^2}\times 3.86\times 10^{26}$

ce qui donne $P_{lune}=12.94\times 10^{15}$Watt

Ensuite on réutilise cette formule de la Lune à la Terre, en considérant que

1. la Lune diffuse la lumière dans toutes les directions. C'est à peu près vrai quand on regarde la pleine lune, elle n'est pas beaucoup plus lumineuse au centre que vers les bords
2. l'[Albédo](w:Albédo_géométrique) de la Lune est de 0.11 : elle ne renvoie que 11% de la lumière (sa couleur est donc un gris très sombre)

On obtient donc

$$P_{terre}=\frac{R_{terre}^2}{4 D_{terre-lune}^2}\times Albedo_{lune}\times P_{lune}$$

soit

$P_{terre}=\frac{6371000^2}{4\times 400000000^2}\times 0.11 \times P_{lune}$

ce qui donne $P_{terre}=6.97\times\10^{-6} \times P_{lune}$

autrement dit, la Terre reçoit de la pleine Lune environ 7 millionièmes de ce que la Lune reçoit du Soleil, et en introduisant $P_{lune}=12.94\times 10^{15}$on obtient

$P_{terre}= 90.2 \times 10^{9}$

90 Gigawatt, un peu moins à la surface après diffusion et albedo terrestre.

Ca a l'air beaucoup, mais c'est presque rien par m2
