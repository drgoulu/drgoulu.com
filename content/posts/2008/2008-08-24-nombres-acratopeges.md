---
title: "Chasse aux nombres acratopèges"
slug: "nombres-acratopeges"
date: 2008-08-24
categories: 
  - "cat2"
tags: 
  - "maths"
  - "nombres"
  - "oeis"
  - "sloane"
coverImage: "b7890bc9a5c14c872c33caa54797a9cb1.jpg"
---

{{< figure src="images/b7890bc9a5c14c872c33caa54797a9cb.jpg" >}}

En utilisant l' [Encyclopédie en ligne des suites de nombres entiers](http://oeis.org/Seis.html) pour un article précédent, j'ai découvert qu'elle pouvait m'aider pour une vieille idée : la recherche de nombres acratopèges.

Le mot "[Acratopège](http://fr.wiktionary.org/wiki/acratop%C3%A8ge)" signifie "sans propriété particulière" et on ne le trouve plus que sur l'étiquette de quelques bouteilles d'eau faiblement minéralisée.

Les nombres entiers sont soit pairs, soit impairs. Certains sont premiers, d'autres des carrés ou des cubes d'autres nombres. Au fil des siècles, les mathématiciens ont ainsi défini des centaines de propriétés particulières dont jouissent certains nombres et ont rangés les nombres en suites définissant ces propriétés:

- 2,3,5,7,11,13,17, 19, 23 ... : les nombres premiers
- 1,2,4,8,16,32,64,128 ... : les puissances de deux
- et des centaines d'autres

Les petits nombres ont énormément de propriétés. En cherchant “1” dans l'encyclopédie, on trouve 141'541 resultats, pour “2” :  117'375,  pour “3” : 92'953, et pour “1963”, mon année de naissance :  401 …

Je me suis demandé quels sont les nombres qui apparaissent le moins dans ces suites, et puisqu'ils n'ont aucune propriété particulière, méritent d'être qualifiés d'acratopèges.

### 1548 : le nombre de Zinzin

Zinzin était un prof de maths célèbre du Collège de St-Maurice. Au début des années 80, ses cours étaient de véritables shows et je repense à lui chaque fois que je "fais Barbe Bleue"\* avec une équation et chaque fois que je croise son nombre fétiche : 1548.

Tous les problèmes posées par Zinzin avaient la même solution : 1548 ou une de ses variations comme 1.548, 720 (= 15x48 ) ou encore 31.6348490636206336. Etonné par ce dernier résultat, j'avais dit à Zinzin que je m'étais probablement trompé quelque part et il m'avait suggéré d'en prendre la racine 8-ième : oui c'est bien 1.54^8 ...

Zinzin comptait ainsi : "0,1,e,pi,1548, beaucoup". Selon lui, 0,1,e et pi suffisent à construire les mathématiques avec "Beaucoup" , qui est une notion moins perturbante que l'infini. Et 1548, était un nombre quelconque, sans propriété particulière.

Une génération d'étudiants a cherché pourquoi Zinzin chérissait 1548 plus que tout autre nombre, mais il ne semblait justement pas y avoir de raison. 1548 est-il un nombre acratopège ?

l'Encyclopédie des suites nous apprend que [1548 appartient à pas moins de 115 suites](http://oeis.org/search?q=1548) comme :

- [A135189](http://oeis.org/A135189 "Numbers n that raised to the powers from 1 to k (with k>=1) are multiple of the sum of their digits (n raised to k+1 must not be"): Nombres n qui, élevés aux puissances de 1 à 4, sont multiples de la somme de leurs digits :
    - 1548 = 86 x (1+5+4+8 )
    - 1548^2 = 2396304 = 88752 x (2+3+9+6+3+0+4)
    - 1548^3= 3709478592 = 68694048 x (3+7+0+9+4+7+8+5+9+2)
    - 1548^4=5742272860416 = 106338386304 x (5+7+4+2+2+7+2+8+6+0+4+1+6)
    - (ça ne joue plus avec 1548^5...)
- [A112557](http://oeis.org/A112557 "Smallest number of stones in Tchoukaillon (or Mancala, or Kalahari) solitaire which make use of (2*n-1)-th hole for n>=1; a bise") : Plus petit nombre de pierres au [Tchoukaillon](http://mancala.wikia.com/wiki/Tchoukaillon) qui utilise le (2\*n-1)-ème trou
- et autres folies de mathématiciens

Mais il est vrai qu'avec 115 résultats, 1548 a peu de propriétés, nettement moins que  ses voisins 1547 (151) et que 1549 (304) par exemple. C'est un nombre que je qualifierais de "faiblement minéralisé" plutôt que d'acratopège.

### 1729 : Le nombre de Hardy-Ramanujan (et Goulu)

Sur les traces de Zinzin, je m'étais mis en tête de trouver mon propre nombre fétiche et ai choisi 1729, en raison d'une histoire légèrement brodée par le fameux Zinzin. Le mathématicien Hardy avait pris le taxi numéro 1729 pour rendre visite à [Ramanujan](https://fr.wikipedia.org/wiki/Ramanujan) et en chemin il avait trouvé ce nombre acratopège : il lui semblait qu'il n'avait aucune particularité. Mais en arrivant, Ramanujan dit immédiatement "Non ,c'est un nombre fort intéressant ; c'est le plus petit que l'on puisse exprimer comme somme de deux cubes de deux manières différentes." En effet, 1729 = 123 + 13 = 103 + 93

Depuis, un tel nombre est appelé "[nombres taxicab](https://fr.wikipedia.org/wiki/nombres_taxicab)" et 1729 est le plus petit taxicab-2. Faisant confiance à l'instinct de Hardy, j'espérais donc que ce soit la seule propriété remarquable de 1729, mais hélas, il y a [369 suites répertoriées contenant 1729](http://oeis.org/search?q=1729) qui est donc un nombre bien moins acratopège que celui de Zinzin.

Seule consolation, il n'y a que [deux suites connues contenant 1548 et 1729,](http://oeis.org/search?q=1548+1729) dont [une dans laquelle les deux nombres se suivent](http://oeis.org/A051624), celle des nombres dodécagonaux donnés par la formule An\=n.(5n-4)

(à part que A2\=12, je ne vois pas le rapport avec les dodécagones, si quelqu'un peut m'éclairer...)

### La chasse est ouverte !

Quel est le plus petit nombre entier qui n’apparaît dans aucune suite de l'Encyclopédie ? et ceux qui n'y apparaissent qu'une fois ?

On peut répondre à ces questions facilement car le contenu de la base de données est [disponible en format texte](http://oeis.org/Seis.html) et qu'un petit programme vite fait en Python peut y compter le nombre d'occurrences des nombres dans les suites en quelques secondes minutes et produire une fichier lisible sous Excel.... et voilà !

- 8795, 9935, 11147, 11446, 11612, 11630, ... sont les premiers nombres parfaitement acratopèges : ils ne figurent dans aucune des suites de la base ! On pourrait définir une suite "Acra0" avec ces nombres définis comme n'apparaissant que dans Acra0 ...
- 8267, 9734 sont les premiers nombres de la suite Acra1. Ce sont les seuls nombres inférieurs à 10'000 qui n'ont qu'une seule propriété répertoriée :
    - [8267](http://oeis.org/search?q=8267) est un nombre tel que la juxtaposition de tous les précédents dans la suite est un nombre premier. Autrement dit le nombre (oubliez les virgules et les espaces, considérez ce qui suit comme un seul nombre entier) : 1, 3, 7, 11, 13, 29, 37, 113, 121, 149, 151, 201, 219, 251, 451, 453, 573, 669, 689, 697, 749, 913, 969, 1157, 1269, 1503, 1531, 1809, 2087, 2163, 2179, 2511, 2537, 2599, 2709, 2789, 2929, 3243, 3989, 4033, 4151, 5019, 5389, 5423, 5599, 6179, 6433, 8267 est premier ...
    - [9734](http://oeis.org/search?q=8727) me plait particulièrement : 11 ème terme de sa suite, c'est le nombre de polyminos différents de 11 carrés dont le périmètre vaut 24, qui est le périmètre maximal de ces polyminos. C'est plus clair si on parle du[pentomino](https://fr.wikipedia.org/wiki/pentomino) classique : le 5ème terme de la suite dit qu'il en existe 11 dont le périmètre vaut 12. Effectivement, seul le "P" a un périmètre de 10. Wow !
- [7495](http://oeis.org/search?q=7495), [8758](http://oeis.org/search?q=8758), [9820](http://oeis.org/search?q=9820), ... ont deux propriétés seulement. Ils définissent la suite Acra2
- [5974](http://oeis.org/search?q=5974) est le plus petit nombre avec 3 propriétés
- Acra5 commence par [5217](http://oeis.org/search?q=5217)
- Acra10 commence par [3962](http://oeis.org/search?q=3962)
- [1238](http://oeis.org/search?q=1238) est le plus petit nombre avec moins de 100 propriétés (88 )

Voilà, vous connaissez désormais les nombres les moins utiles des mathématiques !
