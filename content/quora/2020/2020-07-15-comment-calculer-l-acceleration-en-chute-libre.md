---
title: Comment calculer l'accélération en chute libre ?
slug: comment-calculer-l-acceleration-en-chute-libre
date: '2020-07-15'
draft: false
categories:
- Comment
tags: []
coverImage: ./images/qimg-6ce98c5988dbcbb1eb8eeaf14e74786c.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Comment-calculer-l-acc%C3%A9l%C3%A9ration-en-chute-libre/answer/Dr-Goulu)*

En chute libre (sans frottement de l'air) vous ne ressentez aucune accélération. Les astronautes dans l'ISS, la Lune autour de la Terre, la Terre autour du Soleil etc, tous les corps sont en chute libre : pas de force sur eux = pas d'accélération.

Quand vous regardez un caillou tomber à vos pieds, c'est vous qui accélérez vers le haut. Le [Principe d'équivalence](w:) dit que ces deux situations sont indistinguables :

![](./images/qimg-6ce98c5988dbcbb1eb8eeaf14e74786c.png)

Cela dit, pour mesurer l'accélération de la fusée ou du sol, que vous pouvez interpréter comme l'accélération de la balle vers le sol si vous voulez mais c'est faux, il vous suffit de mesurer la position de la balle pendant qu'elle est en chute libre.

Sur Terre, avec une caméra qui prend 25 images par seconde et en regardant ensuite votre film image par image pour relever la position de la balle arrondie au centimètre près vous pouvez faire un tableau de mesure comme ça :

![](./images/qimg-8cceae75fefdb18e49c1267ea39d3ae6.png)

après, vous ajoutez un colonne pour calculer la vitesse en faisant la différence entre chaque paire de lignes :

![](./images/qimg-b95b4c1cfee0a6793e82958020509ef5.png)

et vous refaites la même chose pour l'accélération :

![](./images/qimg-723a72134aab450d8ef1314b50431c0a.png)

avec une petite moyenne à la fin pour tenir compte des arrondis que vous avez faits, vous tombez sur quelque chose pas de pas trop faux (5% d'erreur avec 12 mesures grossières seulement et de la dérivation numérique brutale d'ordre 1, c'est pas si mal …)

Si vous n'avez pas de caméra, vous pouvez [faire comme Galilée](w:Pesanteur) : un plan incliné avec un bille qui heurte des clochettes régulièrement espacées…
