---
title: Au moment où on a décidé d'utiliser les vibrations de l'atome de césium pour fixer la durée de la seconde, pourquoi ne pas avoir choisi un nombre rond comme 9 milliards de vibrations très exactement par exemple (plutôt que 9 192 631 770) ?
slug: au-moment-ou-on-a-decide-d-utiliser-les-vibrations-de-l-atome-de-cesium-pour-fixer-la-duree-de-la-seconde
date: '2022-08-18'
draft: false
categories:
- Pourquoi
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Au-moment-o%C3%B9-on-a-d%C3%A9cid%C3%A9-d-utiliser-les-vibrations-de-l-atome-de-c%C3%A9sium-pour-fixer-la-dur%C3%A9e-de-la-seconde-pourquoi-ne-pas-avoir-choisi-un-nombre-rond-comme-9-milliards-de-vibrations-tr/answer/Dr-Goulu)*

Excellente question.

Mais un nombre rond en base 10 n'arrange pas grand chose, surtout qu'on a fixé c=299792458 pour la "vitesse de la lumière", donc le mètre est la distance parcourue par la lumière en

> $$9192631770 / 299792458 =30.663318988498369762190615254354779665604529650976076256…$$
>
>
>
>
>
> oscillations de l'atome de césium, ce qui n'est pas très pratique pour fabriquer un mètre étalon.
>
>
>
> Ce n’est pas une jolie fraction car le [pgcd](http://www.wikipedia.org/search-redirect.php?language=fr&go=Go&search=pgcd) de 9192631770 et de 299792458 n’est que 14. S’il est désormais très difficile de changer la durée de la seconde, peut-être aurait-on pu redéfinir légèrement le mètre en utilisant un dénominateur légèrement supérieur à 299792458 (pour se rapprocher des 300’000 km/s) donnant un pgcd plus grand.
>
>
>
> En [cherchant un peu](https://www.pythonanywhere.com/gists/a7332063593056348c6de43239f7f119/metercst.py/python3/?gist-runner-auth-key=7176d4139a344ab18816c7d2b1b232f1), je trouve que 299901462 aurait bien convenu. Le pgcd vaut alors 13039194, ce qui permettrait de mesurer 23 “nouveaux mètres” comme étant la distance parcourue par la lumière en 705 oscillations de césium pile poil. Mais cela aurait raccourci le mètre de 0.4 mm soit 0.04% environ… Où aurait-ce causé des problèmes ?

[https://www.drgoulu.com/2017/05/...](https://www.drgoulu.com/2017/05/26/pourquoi-on-ne-peut-plus-mesurer-la-vitesse-de-la-lumiere/)
