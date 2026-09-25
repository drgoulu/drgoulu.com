---
title: Combien d’entiers $n$ sont tels que $|2\pi-\sum_{k=2}^n \frac{1}{k\ln{k}}|\leq 10^{-100}$ ?
slug: combien-dentiers-n-sont-tels-que-2-pi-sum-k-2-n-frac-1-k-ln-k-leq-10-100
date: '2022-04-14'
draft: true
categories:
- Combien
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Combien-d-entiers-n-sont-tels-que-2pi-sum-k2-n-frac-1-kln-k-leq-10-100/answer/Dr-Goulu)*

petit plaisantin ;-)

la somme diverge, mais très lentement ….

le terme de la somme devient plus petit que $10^{-100}$ pour $k=e^{W(10^100)}$ où W est la [Fonction W de Lambert](w:). [WolframAlpha](https://www.wolframalpha.com/input?i=+solve+1/(k*ln(k))+=+1E-100+for+k) dit que c'est autour de $k\approx 4.44755\times 10^{97}$

reste plus qu'à savoir si la somme vaut plus que $2\pi$ pour $k=.44755\times 10^{97}$ et dans ce cas la réponse à votre question est "aucun, ou peut être 1 seul par chance", mais si la somme vaut moins que $2\pi$, alors la réponse est "beaucoup"…

C'est un problème de ProjectEuler ou similaire, pour que je sache si ça vaut la peine de se casser plus la tête ?
