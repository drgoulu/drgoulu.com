---
title: "Le &quot;Sleep sort&quot;"
date: 2011-06-19
categories: 
  - "cat2"
tags: 
  - "informatique"
  - "programmation"
  - "tri"
coverImage: "3016524792_cdb7edf4c8_m-1.jpg"
---

Tout a commencé\* par un [message "Genius sorting algorithm: Sleep sort" sur 4chan](http://dis.4chan.org/read/prog/1295544154) : un anonyme propose un algorithme de tri en 2 lignes de code [bash](http://fr.wikipedia.org/wiki/Bourne-Again_shell) :

`function f() {sleep "$1" echo "$1"} while [ -n "$1" ] do f "$1" & shift done wait`

Lorsqu'il est appelé avec une liste de N nombres comme dans `./sleepsort.bash 5 3 6 3 6 3 1 4 7 ,` ce code lance un processus pour chacun des nombres n. Chaque processus effectue la fonction f, qui utilise la fonction [sleep](http://fr.wikipedia.org/wiki/Sleep_\(Unix\)) pour attendre n secondes avant d'afficher le nombre n. Dans l'exemple, le 7ème processus n'attendra qu'une seconde avant d'afficher "1", le 4ème et le 6ème attendront 3 secondes avant d'afficher "3" dans un ordre qui n'a aucune importance et ainsi de suite jusqu'au dernier processus qui affichera "7" après 7 secondes. L'utilisateur verra ainsi s'afficher progressivement les N nombres triés dans l'ordre croissant.

Depuis ce message on voit des implémentations de "Sleep sort" fleurir dans [tous](http://pastebin.com/8NEH9kSh) [les](http://www.codesphp.com/php-category/algorithms/php-genius-sorting-algorithm-sleep-sort.html) [langages](http://code.msdn.microsoft.com/Sleep-Sort-in-C-8e7831b3/sourcecode?fileId=22380&pathId=934743301) [de](https://gist.github.com/1028467) programmation en utilisant [diverses](http://code.activestate.com/recipes/577756-sleepsort/?in=lang-python) [astuces](http://code.activestate.com/recipes/577762-sleepsort-timer-version/), et des [discussions sans fin sur les forums](http://www.reddit.com/r/programming/comments/i0dcx/4chan_sleep_sort/), anglophones surtout pour l'instant.

Prétextant que ce programme mettrait plus de 11 jours à trier les deux nombres 1000000 et 673, certains considèrent le "sleep sort" comme un bon gag, ce qu'il est certainement à l'origine. Pour ma part j'ai [voté contre l'effacement](http://en.wikipedia.org/wiki/Wikipedia:Articles_for_deletion/Sleep_sort#Sleep_sort) de la [page "Sleep sort" de la Wikipedia](http://en.wikipedia.org/wiki/Sleep_sort). Voici pourquoi.

D'abord, ce code est simple et fait l'éloge d'une grande qualité du programmeur : la paresse. Faire quelque chose d'utile simplement en attendant, quoi de plus beau ? A ce titre il mérite amplement sa place à côté du [Spaghetti sort](http://en.wikipedia.org/wiki/Spaghetti_sort) dont [j'ai déjà causé ici](http://drgoulu.local/2008/11/22/tri/) en français, du ["tri stupide" (Bogosort)](http://fr.wikipedia.org/wiki/Tri_stupide) ou des [Stooge sort](http://en.wikipedia.org/wiki/Stooge_sort) et [Lucky sort](http://en.wikipedia.org/wiki/Luckysort) sans intérêt, mais qui ont leur page Wikipédia.

{{< figure src="images/3016524792_cdb7edf4c8_m-1.jpg" alt="Photo par Eben Regis sur flickr" caption="Photo par Eben Regis sur flickr" link="http://www.flickr.com/photos/30271386@N04/3016524792/in/photostream/" align="alignright" width="240" >}}

 

Plus sérieusement, "Sleep sort" exploite de manière active l'écoulement du temps au lieu de le subir, ce qui est déjà intéressant en soi, mais pose également des questions intéressantes sur la ["complexité" de tels algorithmes](http://fr.wikipedia.org/wiki/Th%C3%A9orie_de_la_complexit%C3%A9_des_algorithmes).

Car le "génie" de cet algorithme, s'il vous avait échappé, est qu'il prend en apparence un temps proportionnel à max(n), le plus grand des nombres à trier, pour s'exécuter, plus un temps proportionnel à N pour créer les processus. Or les [algorithmes de tri généraux](http://fr.wikipedia.org/wiki/Algorithme_de_tri) existants prennent un temps proportionnel à N.log(N). Il pourrait donc exister des cas où le "sleep sort" serait plus rapide. Mais est-ce vraiment le cas ?

Traitons d'abord de la partie la plus perceptible du temps d'exécution, l'attente de max(n) secondes. Sur les machines actuelles, [l'attente se spécifie en millisecondes](http://en.wikipedia.org/wiki/Sleep_\(operating_system\)), et on pourrait probablement passer aux microsecondes. En fait il faut simplement garantir que deux processus associés à deux nombres x et x+1 se réveillent dans le bon ordre et aient le temps de produire leur sortie sans perturber le réveil des processus suivants. Déjà ceci soulève plein de problèmes intéressants au niveau des systèmes d'exploitation, de l'accès aux ressources critiques etc. Mais quelles que soient les solutions techniques, il reste qu'on ne sait pas bien exprimer théoriquement la complexité d'un tel algorithme : en principe, une durée d'exécution proportionnelle à l'une des données conduit à une complexité O(1) supposée largement inférieure à O(N), ce qui n'est pas le cas en pratique ici.

Ensuite la partie "proportionnelle à N" dans laquelle on crée les N processus est elle vraiment O(N) ? En principe oui, mais il existe une partie invisible : la gestion interne de la fonction système "sleep". Dans tous les systèmes d'exploitation que je connais (au moins deux...), "sleep" provoque l'insertion du processus dans une liste de tous les processus suspendus en attente de l'échéance d'un certain temps. Et pour éviter de parcourir toute la liste à chaque interruption du timer pour trouver quels processus doivent être réveillés, on la maintient triée dans l'ordre des réveils programmés. "Triée" ? Et oui... : à chaque instruction "sleep", rencontrée le processus est inséré au bon endroit. "Inséré" ? Et re-oui... : l'exécution des N "sleep" revient à un "[tri par insertion](http://fr.wikipedia.org/wiki/Tri_par_insertion)", d'une complexité O(N²) rédhibitoire.

"Sleep sort" n'est donc pas un tri linéaire, du moins sur un ordinateur ayant beaucoup moins de N processeurs. Mais il soulève plein de questions intéressantes sur les algorithmes, les systèmes d'exploitation, l'architecture des ordinateurs et la psychologie des programmeurs. [Il faut le garder](http://en.wikipedia.org/wiki/Wikipedia:Articles_for_deletion/Sleep_sort#Sleep_sort) !

Note\* : en fait l'idée est plus ancienne comme le montre ce post "[Linear Time Sort Puzzler](http://gafter.blogspot.com/2006/11/linear-time-sort-puzzler.html)" datant de 2006
