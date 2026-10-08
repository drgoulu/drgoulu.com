---
title: "Palindrome de 196"
slug: "palindrome-de-196"
date: 2008-09-14
categories:
  - "Pourquoi"
tags: 
  - "informatique"
  - "maths"
  - "python"
coverImage: "./images/ba5485f7dc2d3ad49c29a5e809e739641.jpg"
---

{{< figure src="./images/ba5485f7dc2d3ad49c29a5e809e73964.jpg" alt="palindrome par puja (flickr)" caption="palindrome par puja (flickr)" link="http://www.flickr.com/photos/puja/251008157/" width="240" >}}

Prenons un nombre au hasard : 1729. Ecrivons-le à l'envers : 9271 et additionnons les deux nombres : 1729+9271=11000. Recommençons avec ce nombre : 11000+00011 = 11011.

Ce nombre est égal à lui même écrit à l'envers, c'est un nombre [palindrome](w:), comme le mot "radar" ou la phrase "élu par cette crapule" si on ne tient pas compte des espaces, ou encore "[le grand palindrome](https://web.archive.org/web/20080919221059/http://homepage.urbanet.ch/cruci.com/lexique/palindrome.htm)", un texte de 5566 lettres écrit par Georges Perec en 1969.

Tiens, refaisons le calcul avec 1969 pour voir : 1969+9691 = 11660 11660+06611 = 18271 18271+17281 = 35552 35552+25553 = 61105 61105+50116 = 111221 111221+122111 = 23332 : palindrome !

Bizarre n'est-ce pas ? En fait on peut prendre n'importe quel nombre de départ, et la séquence d'opérations arrive inévitablement à un nombre palindrome en un nombre fini d'itérations. C'est du moins ce que l'on [conjecture](w:), car il y a deux problèmes :

1. nos amis mathématiciens n'ont aucune idée de la raison qui fait que ça marche, entre autre parce que "écrire un nombre en base 10 à l'envers" n'a pas de signification mathématique simple.
2. il y a un gros hic. Si on commence avec 196, on n'arrive pas à un palindrome même après 300 millions d'itérations...

196 est le plus petit des "[nombres de Lychrel](w:)" (en l'honneur de Cheryl, la petite amie du matheux qui a proposé cette propriété) : les nombres qui n'aboutissent apparemment pas à un palindrome ... [Dans ces nombres](http://oeis.org/A023108) se trouvent évidemment [ceux produits à chaque itération à partir de 196](http://oeis.org/A006960), mais aussi quelques autres.

Ce qui est intéressant aussi, c'est la distribution du nombre d'itérations : très souvent, on atteint le palindrome en quelques étapes, même pour de très grands nombres, mais quelques rares nombres demandent quelques étapes de plus

Par exemple pour les nombres de 1 à 99, on arrive à un palindrome en 4 itérations ou moins  pour 98 nombres, 79 et 97 ont besoin de 6 itérations, mais 89 et 98 nécessitent 24 itérations.

Pour les nombres de 1 à 999, 929 atteignent le palindrome en 6 itérations ou moins, 13 sont des nombres de Lychrel et les 57 restant ont besoin de moins de 24 étapes : 89 et 98 sont toujours les plus gourmands en itérations

Poussons jusqu'à 10'000 : à part les 249 (_edit du 6.1.14 : et non 246_) nombres de Lychrel, il n'y a toujours pas d'autre nombre que 89 et 98 qui nécessite plus de 24 itérations.

La quête du "[palindrome le plus retardé](http://www.jasondoucette.com/worldrecords.html)" a commencé par ces résultats :

| Nombre | Iterations | Palindrome |
| --- | --- | --- |
| 10911 147996 150296 1000689 1005744 1017501 7008899 9008299 | 55 58 64 78 79 80 82 96 | 4668731596684224866951378664 8834453324841674761484233544388 682049569465550121055564965940286 796589884324966945646549669423488985697 796589884324966945646549669423488985697 14674443960143265333356234106934447641 68586378655656964999946965655687368586 555458774083726674580862268085476627380477854555 |

le record du monde actuel (2008) date de 2005 et concerne le nombre 1'186'060'307'891'929'990, qui produit un palindrome de 119 chiffres après 162 itérations.

On voit que le nombre maximal d'itérations requises n'augmente que très lentement, ce qui rend les nombres de Lychrel encore plus intriguants et exceptionnels.

A propos : j'ai commencé cet article par [mon nombre fétiche 1729 parce que celui de Zinzin, 1548](/2008/08/24/nombres-acratopeges/) est peu intéressant : 1548+8451 = 9999. Ou alors, 30 ans plus tard, je viens de découvrir une nouvelle propriété de ce nombre ...

### Références:

- [forum avec un bout de code Python](w:en:Wikipedia:Reference_desk/Archives/Computing/2008_August_25) pour le calcul de palindromes
- [196-Algorithm](http://mathworld.wolfram.com/196-Algorithm.html) sur MathWorld
