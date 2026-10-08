---
title: "la Résurrection du Jeu de la Vie"
slug: "la-resurrection-du-jeu-de-la-vie"
date: 2009-03-29
categories:
  - "Comment"
tags:
  - "informatique"
  - "logiciels"
  - "programmation"
  - "theorique"
coverImage: "./images/a470c29cf6c88b820cc608831b61f545.gif"
---

Le [Jeu de  vie](w:Jeu_de__vie) imaginé par [John Conway](w:) en 1970 est un automate cellulaire célébrissime pour au moins deux raisons:

1. {{< figure src="./images/a470c29cf6c88b820cc608831b61f545.gif" alt="Un canon à planeurs" caption="Un \"canon à planeurs\"" width="250" >}}

   A partir de règles toutes simples, le jeu de la vie génère une "vie" artificielle étrangement complexe et imprévisible, posant toutes sortes de questions intéressantes

2. Le Jeu de la Vie étant très facile à programmer, des générations d'étudiants ont codé des programmes "Life" dans tous les langages imaginables.

Après une flambée d'intérêt dans les années 1980 où on a même vu apparaitre des processeurs spécialisés dans l'exécution d'automates cellulaires, le soufflé est retombé dans la décennie suivante car la simulation de grands automates demandait beaucoup de puissance de calcul et de mémoire.

Mais comme nous l'apprend Jean-Paul Delahaye dans le dernier "Pour la Science" [[1]](#ref-1), il y a du nouveau. En 2005 est apparu "[Golly](https://web.archive.org/web/20090423220053/http://golly.sourceforge.net/)", un logiciel Open Source utilisant "[Hashlife](w:)", un algorithme accélérant le calcul des automates cellulaires d'une manière phénoménale. Hashlife a été imaginé en 1984 déjà par [Bill Gosper](w:) [[3]](#ref-3), un des premiers "hacker" du Xerox Park de Palo Alto. Mais pour une étrange raison, ce n'est qu'en 2004 Tomas Rokicki l'a implanté en C et décrit dans un article intitulé "un algorithme pour compresser le temps et l'espace" [[2]](#ref-2).

Hashlife combine en effet deux techniques de programmation :

1. une partition de l'espace qui permet d'une part d'ignorer les grandes zones de cellules vides et d'autre part de reconnaitre les copies identiques de groupes de cellules
2. la "[Mémoization](w:)", qui consiste à mémoriser des résultats précédemment calculés afin de les restituer immédiatement lorsque la même situation se représente.

Ainsi, hashlife ne calcule qu'une seule fois l'évolution d'un groupe de cellules qui serait présent à des milliers d'exemplaires dispersés sur un immense jeu de la vie, et n'a besoin de mémoire que pour stocker chacune des étapes d'un cycle au lieu de millions de cellules.

Hashlife parvient ainsi à calculer des milliers de générations par seconde de "Jeux de la Vie" comportant 10^50 cellules sur un PC ordinaire doté de 10^9 octets de mémoire !

Voici par exemple "[Golly](https://web.archive.org/web/20090423220053/http://golly.sourceforge.net/)" en action sur le "breeder", la première structure générant un nombre de cellules augmentant comme le carré du nombre de générations :

{{< youtube id="FVP58qsG0MY" width="640" >}}

On voit comment un groupe de "fusées" se déplace vers la droite en générant des "canons à planeurs". En quelques secondes, 400'000 générations ont été calculées (même pas à vitesse maximale) , générant 160 millions de cellules actives.

Cette vitesse permet de visualiser confortablement d'autres structures extraordinaires découvertes récemment, comme les "métacellules":

{{< youtube id="wkOEeQsKEvU" width="640" >}}

On voit ici un tableau de 15x15 métacellules, dont chacune se comporte comme une cellule du Jeu de la Vie ! En 30'000 générations environ, chaque métacellule compte le nombre de ses voisins "vivants" et devient elle-même vivante en se remplissant de planeurs en suivant la règle de Conway !

Le "Jeu de la Vie" est donc capable d'exécuter un programme jouant au "Jeu de la Vie". Mais quels autres programmes peut-il exécuter ? On connait depuis 1984 des structures calculant les nombres premiers, et d'autres "écrivant" en clair comme celle-ci :

{{< youtube id="Rj3va_5qcM4" width="640" >}}

Mais en 2000, Paul Rendell a réussi a créer une  "[Machine de Turing](w:)" en Jeu de la Vie [[3]](#ref-3), ce qui signifie que ce petit jeu aux  règles extraordinairement simple est capable, avec une astucieuse programmation, de réaliser toutes les opérations d'un ordinateur usuel.

Outre le jeu de la Vie, Golly peut exécuter d'autres automates cellulaires en utilisant le fantastique algorithme Hashlife, notamment [Wireworld](w:), un système simulant les circuits électroniques digitaux.

"Hashlife" est bien un algorithme qui compresse l'espace et le temps, comme le dit Rokicki, et il  est même d'un usage assez général. Je ne serais pas étonné s'il trouvait prochainement des applications "sérieuses", en simulation notamment.

J'adore les rubriques de Jean-Paul Delahaye dans "Pour la Science". Surtout celle du mois prochain...

## Références:

1. <span id="ref-1"></span>Jean-Paul Delahaye "[Le royaume du Jeu de la vie](https://web.archive.org/web/20130612202722/http://www.pourlascience.fr/ewb_pages/f/fiche-article-le-royaume-du-jeu-de-la-vie-20905.php)", Pour la Science, avril 2009, p. 86-91
2. <span id="ref-2"></span>Tomas G. Rokicki "[An Algorithm for Compressing Space and Time](https://web.archive.org/web/20100324150738/http://drdobbs.com/high-performance-computing/184406478)", Dr. Dobbs Journal, avril 2006
3. <span id="ref-3"></span>William Gosper "Exploiting Regularities in Large Cellular Spaces", 1984, Physica D. Nonlinear Phenomena, Vol 10, pp. 75-80 {{< altmetric doi="10.1016/0167-2789(84)90251-3" >}}
4. <span id="ref-4"></span>Paul Rendell " [a Turing Machine implemented in Conway's Game of Life](http://rendell-attic.org/gol/tm.htm)", 2000
5. <span id="ref-5"></span>Paul Callahan "Wonders of Math : [What is the Game of Life?](http://www.math.com/students/wonders/life/life.html)" sur Math.com
6. <span id="ref-6"></span>[Game of Life News](https://web.archive.org/web/20090417030104/http://pentadecathlon.com/lifeNews/index.php), un blog dédié aux nouvelles découvertes sur le Jeu de la Vie
7. <span id="ref-7"></span>Un "[Jeu de la Vie](http://www.ibiblio.org/lifepatterns/)" en Java, utilisant l'algorithme Hashlife implanté dans ce langage, en open source.
8. <span id="ref-8"></span>David Bau "[Python Curses Life](http://davidbau.com/archives/2006/07/26/python_curses_life.html)", une implantation (simplifiée) de Hashlife en Python
