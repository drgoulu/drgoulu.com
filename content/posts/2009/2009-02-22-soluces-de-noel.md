---
title: "Soluces de Noël"
date: 2009-02-22
categories: 
  - "cat2"
tags: 
  - "casse-tetes"
  - "graphes"
  - "maths"
coverImage: "a4a08144f1c5337e35f952ea5b03384f.png"
---

Voici enfin quelques solutions aux [problèmes posés à Noël](http://drgoulu.local/2008/12/23/maths-de-noel/)

### le jeu des nénuphars

Pour gagner à [ce petit jeu énervant](http://www.echecsetmaths.com/enigme/pap/1.htm#), j'ai commencé par "tricher" en examinant le petit programme JavaScript qui s'occupe de tout. On y trouve ceci :

```
//positions gagnantes
var gagnant = new Array(777,667,557,447,337,227,456,236,135);
```

En codantla position de chaque grenouille par un chiffre de 0 à 7, la position de départ est notée 024 et la position gagnante finale 777. (On remarque au passage que les positions obtenues en permutant les lignes de nénuphars sont stratégiquement équivalentes, donc on peut représenter toutes ces permutations par un seul code dont les 3 chiffres sont triés dans l'ordre croassant )

Pour y arriver, si on a une grenouille sur 7, il faut s'assurer que les deux autres restent au même niveau : les positions 227,337,447,557 et 667 sont gagnantes parce que l'adversaire n'arrive jamais à faire 777 en un coup alors qu'on peut dans tous les cas se remettre en position gagnante.

Le début de la partie est plus compliqué, et c'est là que tout se joue. Pour comprendre pourquoi 135, 236 et 456 sont des positions gagnantes, j'ai fait ce graphe.

{{< figure src="images/a4a08144f1c5337e35f952ea5b03384f.png" alt="nenuphars2" caption="(cliquer pour agrandir)" link="http://drgoulu.local/wp-content/uploads/HLIC/a4a08144f1c5337e35f952ea5b03384f.png" align="aligncenter" width="471" >}}

On y voit:

1. que comme les positions xx7 , les positions 135, 236 ou 456 sont bien gagnantes car  tout mouvement depuis ces positions permet ensuite à un adversaire jouant bien de  revenir à une position gagnante.
2. il y a encore 3 autres positions gagnantes : 025, 034 et 124, et celles-ci sont accessibles à partir de la position de départ 024. Ca signifie qu'en suivant le graphe**, celui qui commence le jeu est sur de gagner !**

Merci et Bravo à [Xochipili](http://www.webinet.blogspot.com/), qui m'a soumis par mail son analyse de ce problème sans "tricher" en lorgnant le code. Cet article est le résultat de la combinaison de nos idées.

### Les boulets de canon

les [solutions](http://www.ffjm.org/upload/fichiers/reponsesQuartsFinIndividuel.pdf) aux problèmes des quarts de finales de la FFJM sont disponibles. J'ai surtout ramé au problème No 16 pour lequel je n'ai pas trouvé de méthode, et au dernier, celui des boulets de canon, qui est très beau.

Une pile de boulets formée sur une base rectangulaire se termine par une couche ne contenant qu'une ligne de m boulets. La couche juste inférieure contient 2 lignes de m+1 boulets, la suivante 3 lignes de m+2 boulets et ainsi de suite. La i-ème couche contient donc i.(m+i-1) boulets et le nombre de boulets d'une pile contenant c couches est de

$latex n= sum\_{i=1}^{c} i.(m+i-1) = m.sum\_{i=1}^{c} i + m.sum\_{i=1}^{c} i^2 -c$

En utilisant la formule de la somme des premiers entiers et celle de la [somme des premiers carrés](http://www.les-suites.fr/somme-des-n-premiers-carres.htm), on obtient n=c.(c+1).(3m+2c-2)/6, résultat que l'on retrouve déjà dans un "[Cours de mathématiques: à l'usage des écoles impériales militaires](http://books.google.ch/books?id=2NI2AAAAMAAJ&pg=RA1-PA211&lpg=RA1-PA211&dq=pile+de+boulets+de+canon&source=web&ots=MpGduIk45L&sig=8T6edoA5xMKAYbnbJSmOvlHHNrA&hl=fr&sa=X&oi=book_result&resnum=4&ct=result)" de 1813!

Dans le problème posé, la largeur de la pile de base étant égale à m, on a c=m et donc n=m.(m+1).(5m-2)/6 . Reste à trouver la valeur de m donnant un n qui soit un carré parfait. C'est vite fait à la main : m=6 donne 14^2=196 boulets. Mais il existe une autre solution: m=49 donne 99'225 boulets, le carré de 49. Sans Python, j'ai raté celle là ...
