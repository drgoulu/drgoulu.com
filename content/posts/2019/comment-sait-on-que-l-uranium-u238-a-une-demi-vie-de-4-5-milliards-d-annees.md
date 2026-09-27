---
title: Comment sait-on que l'uranium (U238) a une demi-vie de 4,5 milliards d'années ?
slug: comment-sait-on-que-l-uranium-u238-a-une-demi-vie-de-4-5-milliards-d-annees
date: '2019-11-28'
draft: true
categories:
- Comment
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Comment-sait-on-que-l-uranium-U238-a-une-demi-vie-de-45-milliards-d-ann%C3%A9es/answer/Dr-Goulu)*

Avec un compteur "Geiger", on mesure 12.4 désintégrations par seconde ([Becquerel](w:)) dans un milligramme d' [U238](w:Uranium_238).

Or une [Mole](w:Mole_(unité)) d'Uranium 238 (238 grammes) contient le nombre d'Avogadro d'atomes : 6.02214076e+23

Donc dans un milligramme on a 6.02214076E23/238000 = 2.5303112e+18 atomes, donc si 12.4 se désintègrent par seconde, il faut 2.5303112e+18/(2*12.4*60*60*24*365) = 3.235e9 années pour que la moitié se désintègre

MAIS c'est tôt le matin, je suis encore un peu endormi, et j'ai négligé que la désintégration est exponentiellement décroissante puisqu'il y a de moins en moins d'uranium au cours du temps , alors en utilisant la formule

$T_{1/2}=\ln{2}\,\frac{N_\mathrm A}{A}\cdot\frac{m}{M}$

qu'on trouve sous [Activité massique — Wikipédia](w:Activité_massique) on obtient

$$T_{1/2}=\ln{2}\,\frac{6.02214076e+23}{12.4}\cdot\frac{0.001}{238} = 1.4144178262161582e+17$$

secondes

soit 1.4144178262161582e+17/(60*60*24*365.25)= **4.48e9 années**
