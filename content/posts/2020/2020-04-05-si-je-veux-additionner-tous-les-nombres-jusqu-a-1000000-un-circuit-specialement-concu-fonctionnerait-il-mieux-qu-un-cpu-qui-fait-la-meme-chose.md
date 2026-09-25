---
title: Si je veux additionner tous les nombres jusqu'à 1000000, un circuit spécialement conçu fonctionnerait-il mieux qu'un CPU qui fait la même chose ?
slug: si-je-veux-additionner-tous-les-nombres-jusqu-a-1000000-un-circuit-specialement-concu-fonctionnerait-il-mieux-qu-un-cpu-qui-fait-la-meme-chose
date: '2020-04-05'
draft: true
categories:
- Quora
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Si-je-veux-additionner-tous-les-nombres-jusqu-%C3%A0-1000000-un-circuit-sp%C3%A9cialement-con%C3%A7u-fonctionnerait-il-mieux-qu-un-CPU-qui-fait-la-m%C3%AAme-chose/answer/Dr-Goulu)*

Oui. quand on besoin d'aller vraiment vite, actuellement on programme des [FPGA](w:Circuit_logique_programmable) en [VHDL](w:), ce qui revient à faire un circuit "spécialement conçu".

Mais en général, utiliser un bon algorithme sur un petit PC est plus efficace que d'en utiliser un mauvais sur un superordinateur.

Par exemple la somme des nombres de 1 à n vaut n*(n+1)/2 donc la somme des entiers de 1 à 1000000 vaut 500000500000
