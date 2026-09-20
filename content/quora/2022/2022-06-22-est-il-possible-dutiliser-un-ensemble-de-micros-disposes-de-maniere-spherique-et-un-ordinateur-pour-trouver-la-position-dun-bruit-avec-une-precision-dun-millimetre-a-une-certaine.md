---
title: Est-il possible d’utiliser un ensemble de micros disposés de manière sphérique et un ordinateur pour trouver la position d’un bruit avec une précision d’un millimètre à une certaine distance, le rayon de la sphère n’est pas fixe pour la position ?
slug: est-il-possible-dutiliser-un-ensemble-de-micros-disposes-de-maniere-spherique-et-un-ordinateur-pour-trouver-la-position-dun-bruit-avec-une-precision-dun-millimetre-a-une-certaine
date: '2022-06-22'
draft: false
categories:
- Quora
tags:
- informatique
- microphones
- recherche-scientifique
- precision
- traitement-du-signal
- acoustique
- ingenierie
- localisation
- traitement-du-signal-numerique
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Est-il-possible-d-utiliser-un-ensemble-de-micros-dispos%C3%A9s-de-mani%C3%A8re-sph%C3%A9rique-et-un-ordinateur-pour-trouver-la-position-d-un-bruit-avec-une-pr%C3%A9cision-d-un-millim%C3%A8tre-%C3%A0-une-certaine/answer/Dr-Goulu)*

Je ne comprends pas la fin "le rayon de la sphère n’est pas fixe pour la position" mais pour le reste, ça dépend du "bruit", et 4 micros suffisent, mais pour le mm c'est vraiment très limite techniquement.

Ca s'appelle de la "goniométrie acoustique" (acoustic goniometry en anglais), et une petite recherche ne m'a pas donné de publication similaire à ce que vous essayez de faire … (j'ai travaillé dans ce domaine, mais avec une précision en kilomètres…[[1]](#MEkaJ))

L'idée est simplement de mesurer le décalage temporel, le "déphasage" entre les 4 signaux mesurés et de faire un peu de trigo comme dans un GPS[[2]](#vlNxI) pour retrouver la position de la source

Le son se propageant à 300 m/s environ, il parcourt 1mm en 1/300'000ème de seconde, donc pour obtenir une résolution du mm il faut échantillonner votre son à 300 kHz, ce qui est supérieur aux fréquences habituelles dans l'audio ( 44 kHz, 48 kHz, 96 kHz, 192 kHz au max) donc avec des cartes son haut de gamme (comptez 1000 Euro) vous pouvez espérer 2mm de précision.

Après il faut faire un peu de soft ([pas grand chose sur GitHub)](https://github.com/search?q=goniometry) …

Si il fallait vraiment le mm pour un projet professionnel, j'utiliserais LabView[[3]](#uhfgo) avec la seule carte NI [capable d'échantillonner 4 canaux à 300 kHz](https://www.ni.com/en-us/shop/hardware/products/pxi-sound-and-vibration-module.html) , mais il faudrait convaincre le client de sortir 12'000 Euro pour ça …

Notes de bas de page

[[1]](#cite-MEkaJ)[Avalanches et goniomètre à infrasons - Pourquoi Comment Combien](/2016/01/14/avalanches-et-gonimetre-a-infrasons/)

[[2]](#cite-vlNxI)[Le GPS pour les nuls : Satellites et Signaux - Pourquoi Comment Combien](/2008/09/27/le-gps-pour-les-nuls-satellites-et-signaux/)

[[3]](#cite-uhfgo)[les décorateurs, ou pourquoi j'aime toujours la programmation - Pourquoi Comment Combien](/2010/12/03/les-decorateurs-python/)
