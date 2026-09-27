---

title: Est ce possible de vérifier que chaque nombre premier entre 6 et 200 par exemple, est obligatoirement un nombre qui se termine par 1 ou 3 ou 7 ou 9, sous condition de ne pas être divisible par 3, pas être multiple de 3 ? Ils ne sont pas si aléatoires
slug: est-ce-possible-de-verifier-que-chaque-nombre-premier-entre-6-et-200-par-exemple-est-obligatoirement-un-nombre-qui-se-termine-par-1-ou-3-ou-7-ou-9-sous-condition-de-ne-pas-etre-divisible-par-3-pas-etre-multiple-de-3-ils-ne-sont-pas-si
date: '2020-04-08'
draft: true
categories:
- Quora
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Est-ce-possible-de-v%C3%A9rifier-que-chaque-nombre-premier-entre-6-et-200-par-exemple-est-obligatoirement-un-nombre-qui-se-termine-par-1-ou-3-ou-7-ou-9-sous-condition-de-ne-pas-%C3%AAtre-divisible/answer/Dr-Goulu)*

Oui c'est un critère assez basique de non divisibilité par 2,3,5 et ça marche assez bien pour les petits nombres.

C'est ce qu'on appelle un critère nécessaire, mais pas suffisant. Par exemple 97 est premier, mais pas 91 (= 7*13)

Le problème avec ce genre de tests, c'est qu'ils ont tous des "faux positifs" qu'on appelle plutôt des [Nombres pseudo-premiers](w:Nombre_pseudo-premier).

Les tests de primalité modernes comme le [Baillie–PSW](w:en:Baillie–PSW_primality_test) que j'ai implanté dans en Python dans [Goulib.math2.is_prime2](https://goulib.readthedocs.io/en/latest/modules/Goulib.math2.html#Goulib.math2.is_prime) sont capables de dire en une fraction de seconde lequel de ces deux nombres est premier. Et vous ?

- 4547337172376300111955330758342147474062293202868155909393
- 4547337172376300111955330758342147474062293202868155909489

Les nombres premiers ne sont pas du tout aléatoires. Ils sont parfaitement déterministes et générés par des méthodes déterministes très rapides.

Bon en fait les méthodes qu'on utilise en pratique sont plutôt probabilistes, mais elles sont en même temps plus fiables que les méthodes déterministes !

En effet la probabilité qu’un nombre de cette taille soit [pseudopremier](http://www.wikipedia.org/search-redirect.php?language=fr&go=Go&search=Nombre_pseudopremier) est de l’ordre d’une sur 10^30 donc le risque qu’un rayon cosmique change un bit du nombre pendant un test de primalité déterministe est un million de fois plus élevé ! J’aime bien cette idée qu’un algorithme probabiliste soit plus fiable qu’une machine considérée comme déterministe, pas vous ?

[Comment trouver des nombres premiers - Pourquoi Comment Combien](/2012/04/15/comment-produire-des-nombres-premiers/#.Xo7AeMiiGCo)
