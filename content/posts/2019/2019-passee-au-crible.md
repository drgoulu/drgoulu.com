---
title: "2019 passée au crible"
slug: "2019-passee-au-crible"
date: 2019-01-06
tags: 
  - "annee"
  - "oeis"
coverImage: "./images/2019-acheter-en-espagne.jpg"
---

## 2018 sur drgoulu.com

![](./images/2019-acheter-en-espagne.jpg)

Bon, ok, j'ai été [trop actif sur Quora](https://fr.quora.com/profile/Philippe-Guglielmetti) et n'ai publié que 8 articles ici l'année passée, mais il y a tout de même eu 299'047 pages de DrGoulu.com vues en 2018, légèrement plus qu'en 2017.

L'article sur l'[amiante](/2008/02/01/amiante-pas-de-panique/) a été nettement plus lu (27'548) que celui sur le [mouvement perpétuel](/2012/05/27/dites-non-au-mouvement-perpetuel/) (11'457), mais la surprise vient de celui sur [l'énergie de la foudre](/2007/09/09/lenergie-de-la-foudre/#.XC5GPlxsOCo) (14'847) qui se place second (encore une année à puissants orages...), juste avant celui sur la [génération des nombres premiers](/2012/04/15/comment-produire-des-nombres-premiers/) (14'502). Si vous aimez ce sujet, vous allez aimer le paragraphe suivant.

## Bonne Chance pour 2019 !

Je partage [l'avis d'ElJj : 2019 est numériquement assez quelconque](http://eljjdx.canalblog.com/archives/2019/01/01/36975652.html), mais la notion de [nombre chanceux](w:) m'a plus interpellé que lui. Il faut dire que [A118130](https://oeis.org/A118130) est la seule suite de l'[OEIS](https://oeis.org/?language=french) qui contienne 2019 précédé de 1963, un nombre important pour moi. Tous deux sont non seulement des nombres chanceux, mais leurs facteurs premiers le sont aussi : 1963 = 13\*151 et 2019 = 3\*673, et 3,13,151 et 673 sont également chanceux  ([A000959](https://oeis.org/A000959)).

En codant ces [suites infinies en Python](/2017/06/26/series-infinies-et-oeis-en-python/) je suis tombé sur les étonnantes similitudes entre ces nombres et les nombres premiers. Le rapport ne concerne pas les nombres eux-mêmes, car beaucoup de nombres chanceux sont composés ([A031157](https://oeis.org/A031157) liste les nombres à la fois heureux et premiers), mais les suites partagent de nombreuses propriétés:

- elles sont infinies

- leur [densité asymptotique](w:) est la même : 1 / ln(x)

- il existe une infinité de nombres (premiers ou chanceux) jumeaux

- il existe une conjecture analogue à [celle de Goldbach](w:Conjecture_de_Goldbach) : il semblerait que tout entier soit la somme de deux nombres chanceux

Ca commence à faire beaucoup de coïncidences, si bien qu'on commence à se demander si ces propriétés ne sont pas liées plutôt à la notion de [crible](w:Crible_(mathématiques)) qu'à celle de nombre premier [[1]](#ref-1). Car les nombres chanceux n'ont rien de vraiment particulier, si ce n'est qu'ils sont produits par un crible très semblable au fameux [crible d'Ératosthène](w:).

Une bonne résolution à laquelle je me suis attaqué tout de suite consiste donc à coder en Python une classe Sieve qui implante un crible mathématique généralisé. Le [premier jet est là](https://goulib.readthedocs.io/en/develop/_modules/Goulib/math2.html#Sieve), et la suite permettra d'implanter le [crible d'Atkin](w:), voire le [crible algébrique](w:) si tout va bien.

Voilà mes chers lecteurs, il me reste à vous souhaiter à tous une

Bonne et Chanceuse Année 2019 !  

... et profitez en bien, car la prochaine année chanceuse sera 2217 ...

### Références :

1. <span id="ref-1"></span>V. Gardiner, R. Lazarus, N. Metropolis, S. Ulam (1956) : [*Similarities between the properties of the prime numbers and lucky numbers*](https://doi.org/10.1088/0025570X.1956.11976563), Mathematics Magazine, 29 (5), p. 273–280.
