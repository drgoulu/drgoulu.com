---
title: "Comment calculer le 10'000'000'000'000'000'000 ème terme de la suite de Fibonacci"
slug: "comment-calculer-le-1e19-eme-terme-de-la-suite-de-fibonacci"
date: 2017-04-25
categories: 
  - "cat2"
tags: 
  - "algorithmes"
  - "fibonacci"
  - "nombres"
  - "oeis"
  - "python"
coverImage: "1nv66i.jpg"
---

Tombé l'autre jour sur un problème idiot [[1]](#ref-1) mais intéressant : calculer le 1019 ème terme de la [suite de Fibonacci](https://fr.wikipedia.org/wiki/suite_de_Fibonacci). Idiot parce que ça ne sert à rien. Intéressant parce que ça sous-entend qu'il existe une manière de calculer le n-ième terme de cette suite définie par récurrence sans calculer tous les termes précédents. En effet, calculer les termes les uns après les autres prendrait dans les 300'000 ans à raison d'une microseconde par terme...

## Un nombre d'or, mais flottant

Comme même les ésotéristes le savent, la suite de Fibonacci est liée au [nombre d'or.](/2016/07/03/nombre-dor-et-abeilles/) A partir de ce fait, Moivre, Euler et Binet ont indépendamment obtenu ce qu'on appelle aujourd'hui la [formule de Binet](https://fr.wikipedia.org/wiki/Suite_de_Fibonacci#formule_de_Binet), et qui donne directement le n-ième terme de la suite:

\[latex\]\\mathcal F\_n=\\frac1{\\sqrt5}(\\varphi^n-\\varphi'^n)\[/latex\], avec \[latex\] \\varphi=\\frac{1+\\sqrt5}2\[/latex\], et \[latex\] \\varphi'=-\\frac1\\varphi\[/latex\] .

En pratique, le terme en \[latex\] \\varphi'\[/latex\] devient rapidement négligeable et il suffit de chercher l'entier le plus proche de \[latex\]\\frac{\\varphi^n}{\\sqrt5}\[/latex\]. Par exemple pour n=50, on peut calculer très vite \[latex\]\\mathcal F\_{50}\\approx\\frac{\\varphi^{50}}{\\sqrt5}\[/latex\] = 12586269025

Mais on se heurte rapidement au problème de la précision de calcul en nombres flottants sur nos ordinateurs : \[latex\]\\varphi\[/latex\] étant [irrationnel](https://fr.wikipedia.org/wiki/Nombre_irrationnel) (mais pas aussi [transcendant](https://fr.wikipedia.org/wiki/Nombre_transcendant) que \[latex\]\\pi\[/latex\] ...), il faut calculer \[latex\]\\varphi^n\[/latex\] avec au moins autant de décimales que \[latex\]\\mathcal F\_n\[/latex\] comporte de chiffres. Dès n=71 on dépasse les 53 bits de la mantisse des nombres "extended precision" et les dernières décimales des termes calculés sont faux.

Dit autrement, à partir de n=70 la division \[latex\]\\mathcal F\_n/\\mathcal F\_{n-1}\[/latex\] donne au moins autant de décimales de \[latex\] \\varphi\[/latex\] que son calcul en nombres flottants

## La Matrice salvatrice

Pour une méthode de calcul en nombres entiers atteignant (presque) la rapidité de la formule de Binet, il faut utiliser l'idée d'un certain Brenner : écrire la récurrence de Fibonacci sous forme matricielle [[2]](#ref-2). La matrice toute simple \[latex\]Q=\\begin{pmatrix}1&1\\\\1&0\\end{pmatrix}\[/latex\] permet d'obtenir un nouveau terme de la série de Fibonacci en la multipliant par un vecteur formé des deux termes précédents:

\[latex\]\\begin{pmatrix}1&1\\\\1&0\\end{pmatrix}\\begin{pmatrix}\\mathcal F\_{n-1}\\\\\\mathcal F\_{n-2}\\end{pmatrix}=\\begin{pmatrix}\\mathcal F\_{n}\\\\\\mathcal F\_{n-1}\\end{pmatrix}\[/latex\]

En enchaînant les multiplications matricielles, on obtient le n-ième terme à partir des deux premiers (0,1) ainsi :

\[latex\]\\begin{pmatrix}1&1\\\\1&0\\end{pmatrix}^{n-1}\\begin{pmatrix}1\\\\0\\end{pmatrix}=\\begin{pmatrix}\\mathcal F\_{n}\\\\\\mathcal F\_{n-1}\\end{pmatrix}\[/latex\]

En fait on retrouve les termes de la suite directement dans la matrice  \[latex\]Q^n = \\begin{pmatrix}\\mathcal F\_{n+1}&\\mathcal F\_{n}\\\\\\mathcal F\_{n}&\\mathcal F\_{n-1}\\end{pmatrix}\[/latex\].

L'algorithme de l'[exponentiation rapide](https://fr.wikipedia.org/wiki/exponentiation_rapide) permet d'élever la matrice Q à la puissance n en effectuant log2(n) multiplications de matrices 2x2, soit [environ 63](https://www.wolframalpha.com/input/?i=log\(10%5E19\)%2Flog\(2\)) pour n=1019. Ultra rapide, et facilement généralisable à d'autres formules de récurrence !

Malheureusement, la fonction [matrix\_power de la librairie Python numpy](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.matrix_power.html) souffre d'une [limitation, voire d'un bug](https://github.com/numpy/numpy/issues/5166) qui empêche de l'utiliser dès n=71 car elle utilise les nombres flottants. Il m'a donc fallu la réécrire, en résolvant une petite contrainte technologique au passage.

## Vers les pétaoctets et au delà ...

Il se trouve que le 1019\-ième terme de la suite de Fibonacci est trop grand pour tenir dans le plus super des ordinateurs. En effet, la longueur du n-ième terme de la suite s'obtient facilement en prenant le log (base 10)  de la formule de Binet : \[latex\]\\mathcal L\_n=\\lceil n\\log{\\varphi}\\rceil\[/latex\] , soit grosso-modo n\*0.208987640249978733769272089237555416822459239918210953539...

Vérifions. Pour n=1000, on obtient:

\[latex\]\\mathcal F\_{1000}\[/latex\]=43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875 qui comporte bien pile 209 chiffres.

Donc \[latex\]\\mathcal F\_{10^{19}}\[/latex\] comporte 2089876402499787337 chiffres ... Il faudrait [dans les 867](https://www.wolframalpha.com/input/?i=10%5E19*log\(\(1%2Bsqrt\(5\)\)%2F2\)%2Flog\(2\)%2F8) [péta](https://fr.wikipedia.org/wiki/péta)octets de RAM (de préférence...) pour stocker ce nombre ...

{{< figure src="images/1nv66i.jpg" alt="(mon premier meme ... désolé ...)" caption="(mon premier meme ... désolé ...)" align="alignright" width="500" >}}

## Et modulo 1000000007 ?

Fort heureusement, le problème idiot avait un petit détail en prime : il fallait calculer le résultat [modulo](https://fr.wikipedia.org/wiki/Modulo_(opération)) 1000000007, et ça, ça change tout.

Ce nombre est premier (pour que ça soit plus intéressant), mais surtout il est inférieur à 230, ce qui fait que la multiplication modulo 1000000007 ne nécessite que des opérations sur des [entiers](https://fr.wikipedia.org/wiki/Entier_(informatique)) 32 bits (signés), ultra rapide.

Voici donc quelques fonctions Python tirées du [module math2 de ma librairie Goulib](https://github.com/goulu/Goulib/blob/master/Goulib/math2.py) qui effectuent:

- le produit matriciel, optionnellement modulaire
- l'exponentiation rapide d'une matrice, optionnellement modulaire, et qui corrige le bug de numpy.matrix\_power
- le calcul quasi instantané du n-ième terme de la série de Fibonacci, avec une option modulaire vivement recommandée pour de grands n

\[gist id="f56725fa32fbb4840c855a8309662c9d"\]

Avec ça on obtient fibonacci(int(1E19),1000000007) = 647754067 ce qui nous fait une belle jambe,  mais nous a appris pas mal de choses intéressantes, non ?

Prochaine étape : trouver la [période de Pisano](https://fr.wikipedia.org/wiki/période_de_Pisano) correspondante ...

### Références

1. <span id="ref-1"></span>[Nth Fibonacci number for n as big as 10^19?](http://stackoverflow.com/questions/28548457/nth-fibonacci-number-for-n-as-big-as-1019) sur StackOverflow (et [réponse de will](http://stackoverflow.com/a/28549402/1395973) qui m'a inspiré cet article)
2. <span id="ref-2"></span>Weisstein, Eric W. "[Fibonacci Q-Matrix](http://mathworld.wolfram.com/FibonacciQ-Matrix.html)." From MathWorld--A Wolfram Web Resource.
3. <span id="ref-3"></span>Arthur Charpentier "[Fibonacci, les lapins, le nombre d'or et les calculs actuariels"](https://freakonometrics.hypotheses.org/48554), 2016 sur Freakonometrics (mention spéciale pour l'image de la spirale...)
