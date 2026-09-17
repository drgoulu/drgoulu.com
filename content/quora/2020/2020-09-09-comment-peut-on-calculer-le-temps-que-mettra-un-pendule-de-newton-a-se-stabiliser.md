---
title: Comment peut-on calculer le temps que mettra un pendule de Newton à se stabiliser ?
slug: comment-peut-on-calculer-le-temps-que-mettra-un-pendule-de-newton-a-se-stabiliser
date: '2020-09-09'
draft: false
categories:
- Comment
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Comment-peut-on-calculer-le-temps-que-mettra-un-pendule-de-Newton-%C3%A0-se-stabiliser/answer/Dr-Goulu)*

C'est très difficile à calculer car ça dépend énormément de la construction du pendule. Des minuscules espaces entre les boules au repos ou des défauts d'alignement feront perdre de l'énergie en chocs supplémentaires ou pas parfaitement dans l'axe, ça se voit très bien avec des pendules bon marché.

Avec un pendule très bien fait, c'est surtout le [Coefficient de restitution e](w:Coefficient_de_restitution) des boules utilisées qui est critique. Chaque choc va diminuer la vitesse de la boule suivante d'un facteur e, alors au bout de n chocs la vitesse de la boule est e^n inférieure à la vitesse initiale .

Pour des chocs acier/acier on a e=19/20 environ, donc e=0.95.

après 10 chocs, vous n'avez plus que 60% de la vitesse initiale, et après 100 chocs 0.6%. On voit bien cette décroissance exponentielle quand on joue avec un pendule de Newton. Et théoriquement elle ne s'arrête jamais. D'ailleurs en pratique on relance souvent le système avant qu'il ne soit totalement immobile.

En plus il va y avoir de la dissipation d'énergie par frottement de l'air, plus difficile à calculer car elle augmente comme le carré des vitesses des boules et des fils. Ca serait plus facile à mettre une cloche à vide autour du système que de calculer …

vidéo sympa sur le sujet :

[https://www.youtube.com/watch?v=...](https://www.youtube.com/watch?v=HIoRuruuz3Q)
