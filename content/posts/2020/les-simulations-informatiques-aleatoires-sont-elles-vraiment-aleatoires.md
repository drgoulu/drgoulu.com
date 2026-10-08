---
title: Les simulations informatiques aléatoires sont-elles vraiment aléatoires ?
slug: les-simulations-informatiques-aleatoires-sont-elles-vraiment-aleatoires
date: '2020-04-22'
draft: false
categories:
- Quora
tags:
- sciences
- informatique
- statistiques
- sciences-informatiques
- probabilite-statistiques
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Les-simulations-informatiques-al%C3%A9atoires-sont-elles-vraiment-al%C3%A9atoires/answer/Dr-Goulu)*

Comment savez vous ce qui est “vraiment du hasard” ?

Par exemple cette séquence :

> 211,190,16,57,178,95,209,29,26,38,101,243,20,139,33,40,112

est-elle générée par [RANDOM.ORG - Sequence Generator](https://www.random.org/sequences/) ou est-ce une suite d’octets extraite de [SainteBible.zip](https://web.archive.org/web/20200422/http://SainteBible.zip) ? (par définition, une excellente compression produit un excellent hasard, méditez là dessus…)

Si vous ne savez pas comment elle a été produite, tout ce que vous pouvez faire est d’utiliser des [tests statistiques](w:Générateur_de_nombres_aléatoires) pour voir si la séquence est “de bonne qualité”, mais il vous faudra beaucoup plus de nombres que ci-dessus pour obtenir un résultat fiable, mais jamais certain à 100%.

Mais si vous savez que la séquence a été produite par ordinateur, alors en connaissant l’algorithme utilisé et ses paramètres d’entrée, vous serez capables de re-générer la séquence ci-dessus, et sa suite, donc de dire immédiatement “non, ce n’est pas du hasard du tout”.

Moralité : méfiez vous des générateurs de nombres (pseudo) aléatoires que vous ne connaissez pas : ils ne sont peut être pas du tout aléatoires, mais vous êtes le seul à l’ignorer. Un exemple magnifique est dans cet article où un générateur “aléatoire” produit au beau milieu de la séquence le nom de son auteur :

[Manipulating a random number generator](https://www.johndcook.com/blog/2017/08/16/manipulating-a-random-number-generator/)
