---
title: Une orbite géosynchrone peut-elle se produire sur chaque planète ? Ou faut-il des circonstances spécifiques comme une certaine vitesse de rotation / révolution ? Et pouvez-vous le faire avec n'importe quel objet ?
slug: une-orbite-geosynchrone-peut-elle-se-produire-sur-chaque-planete
date: '2020-03-26'
draft: true
categories:
- Quora
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Une-orbite-g%C3%A9osynchrone-peut-elle-se-produire-sur-chaque-plan%C3%A8te-Ou-faut-il-des-circonstances-sp%C3%A9cifiques-comme-une-certaine-vitesse-de-rotation-r%C3%A9volution-Et-pouvez-vous-le-faire-avec-n/answer/Dr-Goulu)*

Parlons plutôt de l'[Orbite géostationnaire](w:), cas particulier d'[Orbite géosynchrone.](w:Orbite_géosynchrone)

L'altitude de l'orbite est$h= \left (\frac{G \times M \times T^2}{4\pi^2} \right )^\frac{1}{3} - R$

où M est la masse de la planète, T sa [Période de révolution](w:) et R son rayon.

- d'abord vous voyez que la masse du satellite n'apparaît pas, donc oui, on peut le faire avec n'importe quel objet
- Ensuite, vous voyez que l'altitude devient nulle pour $T_0=\frac{2\pi R^{3/2}}{\sqrt{G.M}},$il faut donc que la période soit supérieure à ceci

J’ai fait [cette feuille de calcul](https://docs.google.com/spreadsheets/d/1IL1NvLadi8HYBa-RnhihT5C5BUbqR5NCD-IN7oeSY7g/edit?usp=sharing) pour toutes les planètes, le Soleil et la Lune.

On y voit que l'orbite géostationnaire est "assez haute" pour toute les planètes. Elle est la plus basse pour Mars (16685 km)

Pour la Lune, qui ne fait un tour qu'en 29 jours l’orbite est à 90300 km, mais je crains qu’il ne faille tenir compte de la Terre et que ça complique beaucoup la situation.*

Pour le Soleil**, l'orbite est à 23'664'355 km, soit à peu près la moitié de l'orbite de Mercure. Ca passe…

Les orbites géosynchrones sont à la même altitude que la géostationnaire, mais oscillent autour de l’équateur. Donc oui, il y en a pour toutes les planètes du Système solaire.

Note* : paragraphe modifié après erreur détectée par Pierre Von Berg

Note**: le Soleil ne tourne pas de façon uniforme, j'ai pris la période à l'équateur, 24 jours.
