---
title: Pourquoi les lasers coupent-ils l'acier comme du beurre mais rebondissent simplement sur un miroir en verre ?
slug: pourquoi-les-lasers-coupent-ils-l-acier-comme-du-beurre-mais-rebondissent-simplement-sur-un-miroir-en-verre
date: '2019-04-02'
draft: false
categories:
- Pourquoi
tags:
- physique
- materiaux
- optique
- reflexion
- proprietes-physiques
coverImage: ./images/qimg-bc5ba97d9257082d3b6c250b9857a621.jpg
---

*Article initialement publié sur [Quora](https://fr.quora.com/Pourquoi-les-lasers-coupent-ils-lacier-comme-du-beurre-mais-rebondissent-simplement-sur-un-miroir-en-verre/answer/Dr-Goulu)*

Principalement parce que le laser n’est pas focalisé entre la source et la tête.

On croit toujours qu’un laser est forcément très fin comme dans James Bond, mais ce n’est pas le cas.

Si vous regardez l’illustration ci-dessous tirée de [Laser cutting - Wikipedia](w:en:Laser_cutting), vous voyez que le “laser beam” arrivant en haut à gauche a un diamètre de 32 mm dans la machine 4000W que je connais. Il y a donc une densité de puissance de 5 W / mm2 sur le miroir (en fait moins, car le miroir étant incliné, la surface de l’ellipse est plus grande que celle d’une section du faisceau).

Après la lentille par contre, les 4000W sont concentrés sur un spot d’environ 0.1 mm de diamètre : vous vous retrouvez avec 500 kW / mm2, 100′000 fois plus ! Là, rien ne résiste :

![](./images/qimg-bc5ba97d9257082d3b6c250b9857a621.jpg)

Pour des raisons technologiques, on utilise des laser infrarouges, et là on a le problème que le verre n’est pas assez transparent dans l’infrarouge.

Donc le miroir n’est pas recouvert de verre, c’est juste une surface bien polie, mais il faut quand même refroidir quelques dizaines de watts de pertes.

Par contre la lentille qui focalise le laser est un vrai problème, car il faut la faire en [Séléniure de zinc](w:) pour qu’elle soit assez transparente. Et si cette lentille se salit, elle peut chauffer et dégager un gaz très toxique… C’est une des raisons pour laquelle on injecte un gaz inerte (azote) dans la tête pour éviter que des particules de métal en fusion ne remontent et touchent la lentille. Ca les fait gicler de côté, c’est très joli.
