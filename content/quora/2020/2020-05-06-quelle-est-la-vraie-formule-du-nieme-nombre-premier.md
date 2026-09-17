---
title: Quelle est la vraie formule du «nième nombre premier» ?
slug: quelle-est-la-vraie-formule-du-nieme-nombre-premier
date: '2020-05-06'
draft: false
categories:
- Quora
tags:
- mathematiques
- nombres-naturels
- theorie-des-nombres-premiers
- sequences-de-nombres
- formules-mathematiques
- equations-mathematiques
- theorie-analytique-des-nombres
- theorie-des-nombres
- theoreme-des-nombres-premiers
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Quelle-est-la-vraie-formule-du-ni%C3%A8me-nombre-premier/answer/Dr-Goulu)*

il existe des [Formules pour les nombres premiers](w:) qui disent si un nombre est premier ou pas , par exemple *f*(*n*) = 2 + (2(*n*!) mod(*n* + 1)) donne n+1 si n+1 est premier et 2 sinon.

Ensuite il y en a une qui donne le nombre de nombres premiers inférieurs à k :

$$\pi(k) = k - 1 + \sum_{j=2}^k \left[ {2 \over j} \left(1 +  \sum_{s=1}^{\left\lfloor\sqrt{j}\right\rfloor} \left(\left\lfloor{ j-1 \over s}\right\rfloor - \left\lfloor{j \over s}\right\rfloor\right) \right)\right]$$

Et ensuite il y en a une qui donne le n-ième nombre premier (introduire l'équation ci-dessus dans celle ci-dessous, si vous ne voulez qu'une équation…)

$$p_n = 1 + \sum_{k=1}^{2(\lfloor n \ln(n)\rfloor+1)} \left(1 - \left\lfloor{\pi(k) \over n} \right\rfloor\right)$$

En réalité ce sont des transcriptions sous forme de formules des algorithmes comme le crible d'Erathosthène, en beaucoup moins efficace car on recalcule tout depuis le début pour chaque n.

C'est beau car totalement inutile, mais voilà la "vraie formule du n-ième nombre premier"
