---
title: "La fonction dont la réciproque est sa dérivée"
slug: "fonction-dont-reciproque-derivee"
date: 2018-03-11
categories: 
  - "cat1"
tags: 
  - "internet"
  - "maths"
  - "quora"
coverImage: "maitre.jpg"
---

Quora, c'est vraiment bien. Je ne regrette pas d'y être [plus actif](https://fr.quora.com/profile/Philippe-Guglielmetti) que sur ce blog ces temps-ci. Il y a beaucoup de questions de niveaux très variés, mais les plus intéressantes sont évidemment celles dont on ne trouve pas la réponse facilement sur le web ou Wikipédia. Et parfois, par la magie d'internet, une collaboration efficace et désintéressée débouche sur une réponse vraiment originale.

Par exemple:

### [Est-ce que la dérivée d'une fonction peut être sa réciproque ? Y a-t-il un exemple simple ?](https://fr.quora.com/Est-ce-que-la-d%C3%A9riv%C3%A9e-dune-fonction-peut-%C3%AAtre-sa-r%C3%A9ciproque-Y-a-t-il-un-exemple-simple)

[![maître des dérivées](images/maitre.jpg)](http://www.jybaudot.fr/Analyse/opderiv.html)[André Harnist](https://fr.quora.com/profile/Andr%C3%A9-Harnist), mathématicien a très bien résumé mon propre sentiment "Cette question est géniale ! J’ai aucune idée si c’est possible ou pas…"

Puis il a posé le problème en langage mathématique :

> Soit \[latex\]f\[/latex\] une fonction dérivable définie sur un [ouvert](https://fr.wikipedia.org/wiki/Ouvert_(topologie)) $latex U$ de $latex \\mathbb R$ de [réciproque](https://fr.wikipedia.org/wiki/bijection_réciproque) $latex g$. Supposons que $latex g = f’$, on a $latex f’(f(x)) = x$ pour tout $latex x\\in U$.

En développant [sa réponse](https://fr.quora.com/Est-ce-que-la-d%C3%A9riv%C3%A9e-dune-fonction-peut-%C3%AAtre-sa-r%C3%A9ciproque-Y-a-t-il-un-exemple-simple/answer/Andr%C3%A9-Harnist?share=3a8117ff&srid=3iJbP) il arrive à l'équation que doit satisfaire la fonction $latex f : x^3 = x^2+f'(f'(x))(f(x)-f'(x))$, mais "ne voit pas trop quelle fonction vérifie ça".

Là dessus [Quentin Canu](https://fr.quora.com/profile/Quentin-Canu) passe la nuit sur ce problème avec la collaboration d'une mystérieuse "drama\[list\]" et [trouve](https://fr.quora.com/Est-ce-que-la-d%C3%A9riv%C3%A9e-dune-fonction-peut-%C3%AAtre-sa-r%C3%A9ciproque-Y-a-t-il-un-exemple-simple/answer/Quentin-Canu?share=9b9d2410&srid=3iJbP) :

$latex \\Large f (x) = \\left(\\frac{1}{\\varphi}\\right)^\\frac{1}{\\varphi} x^\\varphi$

définie de $latex \\mathbb R^+$ dans $latex \\mathbb R^+$, où $latex \\varphi = \\frac{1+\\sqrt 5}{2}$ est le [fameux](/2016/07/03/nombre-dor-et-abeilles/#.WqUeWOghKCo) [nombre d’or](https://fr.wikipedia.org/wiki/nombre_d’or) !

On a bien $latex g(x) = \\varphi^{\\frac{1}{\\varphi}^2}y^\\frac{1}{\\varphi}$, et  $latex f'(x) = (\\frac{1}{\\varphi})^\\frac{1}{\\varphi}\\varphi x^{\\varphi-1} = \\varphi^\\frac{\\varphi-1}{\\varphi} x^{\\varphi-1}$

C’est là que le nombre d’or aide grâce à la célèbre relation : $latex \\varphi -1 = \\frac{1}{\\varphi}$ En l'introduisant, on obtient $latex f'(x) = (\\varphi)^\\frac{1}{\\varphi^2} x^{\\frac{1}{\\varphi}} = g(x)$

Un autre Quoriste, [Simon Labrunie](https://fr.quora.com/profile/Simon-Labrunie) , est parvenu au même résultat quasi simultanément, [de cette manière](https://fr.quora.com/Est-ce-que-la-d%C3%A9riv%C3%A9e-dune-fonction-peut-%C3%AAtre-sa-r%C3%A9ciproque-Y-a-t-il-un-exemple-simple/answer/Quentin-Canu/comment/54563451):

> Je me suis dit : sachant que la réciproque d’une fonction puissance est une autre puissance, et que sa dérivée est encore proportionnelle à une autre puissance, un truc genre $latex f(x) = a.x^n$ a des chances de marcher. Après il n’y a plus qu’à faire les calculs : la réciproque est $latex (x/a)^{1/n}$ et la dérivée est $latex n.a x^{n-1}$. D’où $latex 1/n = n-1$, donc n est le nombre d’or  $latex n= \\varphi = (1+\\sqrt{5})/2$ ou son conjugué algébrique $latex (1-\\sqrt{5})/2$, et $latex n.a=a^{-1/n}$ soit $latex n = a^{-n}$ et $latex a = n^{-1/n}$.
> 
> En revanche, je ne vois pas d’autre genre de fonctions dont la dérivée et la réciproque appartiennent à la même classe générale.

### Alors, y'a-t-il d'autres solutions ?

[Patrick-Sole](https://fr.quora.com/profile/Patrick-Sole), chercheur au CNRS, estime que la question est trop pointue pour Quora (peut-être, mais ce n'est pas évident à première vue) et indique une conversation sur MathOverflow intitulée [function satisfying $latex f^{-1} = f'$](https://mathoverflow.net/questions/34052/function-satisfying-f-1-f)

On y trouve [une réponse](https://mathoverflow.net/a/256811/88768) de José Hernandez Santiago qui:

1. fournit la référence du problème original : [H. L. Nelson](http://www.ucalgary.ca/lib-old/SpecColl/nelson.htm) "[Problem 2105](https://www.tandfonline.com/doi/abs/10.1080/00029890.1968.11971062) in Elementary Problems", 1968, The American Mathematical Monthly vol: 75(7) page 779 DOI>[10.1080/00029890.1968.11971062](https://doi.org/10.1080/00029890.1968.11971062) . Il semblerait que [The American Mathematical Monthly](https://fr.wikipedia.org/wiki/The_American_Mathematical_Monthly) soit une mine de jolis problèmes de maths depuis quelques décennies...
2. démontre qu'il n'y a pas d'autres solutions, mais la démonstration dépasse mon modeste niveau...

Ce n'est pas grâce à cette question que j'ai reçu le badge  "meilleur auteur 2018" sur Quora puisque je n'y ai pas contribué, mais cette petite histoire m'a convaincu que Quora est un site "sain" et constructif. J'y retourne ...
