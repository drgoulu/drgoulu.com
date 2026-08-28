---
title: "Unités et classements"
slug: "unites-et-classements"
date: 2009-05-21
categories: 
  - "cat3"
  - "cat2"
tags: 
  - "economie"
  - "maths"
  - "monde"
  - "societe"
coverImage: "1eb17d17e585d41b1611c3e925e355de.jpg"
---

{{< figure src="images/1eb17d17e585d41b1611c3e925e355de.jpg" alt="Etranger, si tu ne sais pas additionner des pommes et des choux, passe ton chemin..." caption="Etranger, si tu ne sais pas additionner des pommes et des choux, passe ton chemin..." link="http://en.wikipedia.org/wiki/New_Cuyama,_California" align="alignright" width="255" >}}

En maths "pures", un nombre est "pur" aussi. Ce sont les marchands et les physiciens qui ont inventé les unités pour des besoins d'application : 3 pommes ne sont pas égales à 3 vaches, et 3 kilos pas égaux à 3 mètres

La somme 562+2150+1951=4663 figurant sur la panneau de [New Cuyama](https://en.wikipedia.org/wiki/New_Cuyama,_California) ci-contre est donc parfaitement exacte mathématiquement, mais _semble_ n'avoir aucun sens car on y additionne des \[âme\]s, des \[pied\]s et des \[année\]s.

"Semble" car en fait le panneau peut simplement avoir été trop petit pour y ajouter quelques "facteurs de conversion" bien pensés comme:

- Population 562 \[âme\]  (x 1 \[point/âme\] )
- Altitude 2150 \[pied\]  (x 1 \[point/pied\] )
- Fondé en 1951 \[année\]  (x 1 \[point/année\])
- Total = 4663 \[point\]s

Tiré par les cheveux ? Pourtant ceci se fait couramment, entre autres chaque fois que l'on établit un classement de pays en fonction de critères multiples.

### L'indice de développement humain

Un exemple simple est l'[indice de développement humain](https://fr.wikipedia.org/wiki/indice_de_développement_humain), qui fait la moyenne de 3 ou 4 données (espérance de vie, taux d'alphabétisation et de scolarisation, PIB/habitant). Mais contrairement à New Cuyama, les valeurs des quelques facteurs de conversion utilisés dans la formule de l'IDH ne valent pas 1, mais des valeurs précises comme 2.60206 \[log $\]. Il faut dire qu'en plus des facteurs, l'IDH introduit des "non-linéarités" : ce n'est en réalité pas le PIB/habitant qui est considéré, mais son logarithme, donc le nombre de zéros du revenu plutôt que le revenu lui-même...

En fin de compte, l'IDH est un nombre compris entre 0 et 1,  avec la Norvège (0.969) à un extrême et la Sierra Leone (0.329) à l'autre. En modifiant un peu la valeur d'un facteur, il est peu probable que le classement soit bouleversé.

### La compétitivité selon l'IMD

Examinons maintenant le tout récent [classement de la compétitivité](http://www.imd.org/research/publications/wcy/upload/scoreboard.pdf) de 57 pays [réalisé par l'IMD](http://www.imd.org/research/publications/wcy/index.cfm). Pour l'établir, l'IMD combine [329 critères](http://www.imd.org/research/publications/wcy/Factors_and_criteria.cfm) grâce à autant de facteurs de conversion. Je n'ai pas trouvé leur valeurs, probablement jalousement gardées par les spécialistes de l'IMD qui les ont finement ajustés pour traduire en chiffres ce qu'ils appellent la  "compétitivité".

J'ai cependant quelques soupçons sur la manière dont ce classement" est établi, par le fait que les USA sont perpétuellement classés No 1 de la compétitivité avec 100 points selon l'IMD. (Pourtant ils se cantonnent autour de la 15ème place de l'IDH, donc à quoi bon être compétitif  ?)

D'une part certains [critères](http://www.imd.org/research/publications/wcy/upload/All_criteria_list.pdf) choisis sont des valeurs absolues (1.1.01 Gross domestic product (GDP), 4.1.01 Land area, 4.1.23 Total final energy consumption et d'autres )  qui favorisent directement les grands pays ( à moins que le facteur associé ne soit négatif ...)

Beaucoup de ces critères absolus figurent aussi sous forme relative, par habitant, ce qui est une manière masquée de tenir compte de la population. Si un critère absolu vaut X est multiplié par le facteur A et que le critère relatif X/H où H est la population du pays est multiplié par le facteur B, alors on a

A.X + B.X/H = (A.H + B).X/H

autrement dit, on obtient un facteur de X/H qui n'est plus constant mais varie linéairement avec la population et on dispose de deux paramètres A et B au lieu d'un seul. Si A est plus grand que 0, les grands pays sont favorisés.

D'autres critères sont directement associés à la culture anglo-saxonne  comme le 4.5.10 English proficiency : pourquoi pas "chinese proficiency" ?

Mais ce qui est le plus suspect voire fondamentalement faux est le fait que l'IMD utilise beaucoup plus de critères (329) qu'il n' y a de pays à classer (57).

### Comment sculpter votre classement vous-même

En effet, s'il y a plus de critères utilisés que de pays à classer, il est possible de choisir les facteurs de manière à obtenir n'importe quel classement ! Voici comment :

1. collectez N données numériques sur M pays dans un tableau de N colonnes et M lignes, avec N>M. Vous obtenez une "matrice m x n" que nous appellerons A
2. notre but est de déterminer les valeurs des M facteurs de conversion qui vont générer le classement souhaité à partir des données A. Mathématiquement c'est un vecteur colonne que nous appellerons X, car c'est l'inconnue
3. Maintenant, remplissons une colonne de plus contenant à chaque ligne la valeur souhaitée du classement du pays correspondant dans la matrice A . Si vous voulez modifier le classement de l'IMD pour que la France soit No 1 de la compétitivité mondiale, donnez lui la valeur 100, puis 98.146 pour Hong-Kong et ainsi de suite jusqu' à 39.060 pour le Venezuéla, en n'oubliant pas de mettre 68.071 aux USA pour les mettre à la 25 ème place. Appelons ce "vecteur colonne" B
4. On se retrouve avec un [système d'équations linéaires](https://fr.wikipedia.org/wiki/système_d'équations_linéaires) de M équations à N inconnues que l'on écrit sous forme matricielle A.X=B, et comme il y a plus d'inconnues que d'équations et qu'il n'y a pas trop de zéros dans les données de la matrice A ni de lignes identiques car les pays sont tous différents, il est toujours possible de le résoudre\*, donc de trouver les facteurs X qui fabriquent le classement voulu !

Note\* : la résolution est un peu plus compliquée si les facteurs ne doivent pas être négatifs, mais je pense qu'avec 5x plus de critères que de pays on doit pouvoir s'en sortir quand même.
