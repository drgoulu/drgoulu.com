---
title: "Le cadran des trois neufs"
slug: "le-cadran-des-trois-neufs"
date: 2014-06-03
categories: 
  - "cat2"
tags: 
  - "casse-tetes"
  - "maths"
  - "nombres"
coverImage: "horloge3x9.jpg"
---

{{< figure src="images/horloge3x9-294x300.jpg" alt="horloge3x9" >}}

_(Mises à jour du 4+5 juin: Bravo à ced, Danakh et Groug dont les commentaires m'ont convaincu que j'aurais du [réutiliser mon code](/2012/01/18/jeu-de-lannee-2012-et-autres-cest-fini/#.U48_Evn90wA)... Je me vois contraint de mettre à jour l'article avec leurs découvertes. Et j'en profite pour tester [MathJax](http://www.mathjax.org/) pour le rendu des formules. C'est nettement plus joli qu'avant, non ?)_

Emmanuel m'a envoyé la photo ci-contre en me demandant si on peut graduer ainsi un cadran d'horloge avec d'autres chiffres que le 9.

Ce qu'il y a d'assez fort, c'est que chaque heure du cadran est obtenue avec trois 9, sauf le 1 qui en n'en utilise que deux. Pourtant il existe une solution avec trois 9 ( \[mathjax\]\\(1=9^{9-9}\\) ), donc on va considérer considérer que le jeu consiste à obtenir les 12 heures du cadran en utilisant trois fois les mêmes chiffres, et les opérations suivantes:

- les 4 opérations de base
- la racine carré et la racine x-ième
- la [factorielle](https://fr.wikipedia.org/wiki/factorielle) (il y a d'ailleurs une erreur : \\(5= \\sqrt{9}!-9/9\\) et pas \\(\\sqrt{9!}-9/9\\) comme sur la photo)
- le [développement décimal périodique](https://fr.wikipedia.org/wiki/développement_décimal_périodique) noté \\(\\overline{.x}\\) et valant x/9. Et oui,  \\(\\overline{.9} = 1\\) (voir [Développement décimal de l'unité](https://fr.wikipedia.org/wiki/Développement_décimal_de_l'unité))
- la concaténation. C'est un peu tiré par les cheveux mais on accepte xx = 11\*x

Avec ceci on peut mettre au point quelques recettes pour obtenir certaines "heures" facilement:

1. \\(1 = x^{x-x}\\)
2. \\(2 = (x+x)/x\\)
3. \\(x-1 = x-x/x\\)
4. \\(x = \\sqrt\[x\]{x^x}\\), parmi plusieurs autres possibilités
5. \\(x+1 = x+x/x\\)
6. \\(11 = xx/x\\), où xx désigne la concaténation de deux x
7. \\(3x = x+x+x\\)
8. \\(9-x = x/\\overline{.x} -x\\)
9. \\(x+3 = x+\\sqrt{x/\\overline{.x}}\\)
10. \\(x-3 = x-\\sqrt{x/\\overline{.x}}\\) (trouvé par ced...)
11. \\(9 = \\sqrt{x\*x}/\\overline{.x}\\) (bravo ced !)
12. \\(2x = x+\\sqrt{x\*x}\\) (encore ced !)
13. \\(3 =  \\sqrt{\\sqrt{x\*x}/\\overline{.x}}\\) (bien vu Danakh)

Voici le tableau indiquant les heures que je suis parvenu les commentateurs et moi-même avons pu définir avec trois et uniquement trois utilisations de chaque chiffre. Les lettres entre parenthèses rapportent aux recettes ci-dessus et les formules sont les solutions "hors-recettes" que j'ai trouvées :

| x/heure | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | (a) | (a) | (a) | (a) | (a) | (a) | (a) | (a) | (a) |
| 2 | (b) | (b) | (b) | (b) | (b) | (b) | (b) | (b) | (b) |
| 3 | (g) | (e) | (d) | (c) | (m) | (h) | (m) | (m) | \\(\\sqrt{9}+9-9\\) |
| 4 | (i) | (l) | (e) | (d) | (c) | \\(\\sqrt{6\*6}\*\\overline{.6}\\) | (j) | \\(8-\\sqrt{8+8}\\) | \\(\\sqrt{9}+9/9\\) |
| 5 | \\(\\sqrt{1/\\overline{.1}}! -1\\) |  (i) | \\(3!-3/3\\) | (e) | (d) | (c) |  | (j) | \\(\\sqrt{9}!-9/9\\) |
| 6 | \\((1+1+1)!\\) | (g) | \\(3!+3-3\\) | \\((4-4/4)!\\) | (e) | (d) | (c) | \\(8-\\sqrt{\\sqrt{8+8}}\\) | (j) |
| 7 |  (h) | \\(3!+3/3\\) | \\((4!+4)/4\\) |  | (e) | (d) | (c) | \\(9-\\sqrt{9}+\\overline{.9}\\) |
| 8 | (h) | \\(2\*2\*2\\) | \\((3!/3)^3\\) | \\(4!-4\*4\\) | (i) | \\((6+6)\*\\overline{.6}\\) | (e) | (d) | (c) |
| 9 | (k) | (k) | (g) | (k) | (k) | (k) | (k) | (e) | (d) |
| 10 | \\(11-1\\) |  |  | \\(4+4+\\sqrt{4}\\) | (l) | \\(6+6\*\\overline{.6}\\) | (i) | \\(8+\\sqrt{\\sqrt{8+8}}\\) | (e) |
| 11 | (f) | (f) | (f) | (f) | (f) | (f) | (f) | (f) | (f) |
| 12 | \\(11+1\\) | \\((2+2)!/2\\) | \\(3\*3+3\\) | (g) | \\(5!/(5+5)\\) | (l) |  | \\(8+\\sqrt{8+8}\\) | \\(9+9/\\sqrt{9}\\) |

Grâce aux contributions de géniaux et persévérants commentateurs, de nombreuses cellules ont pu être remplies:

En remplaçant un seul chiffre par deux grâce à \\(x = \\sqrt{x\*x}\\) comme remarqué par ced, on peut remplir la ligne 9 et plusieurs autres cases en utilisant trois répétitions de x au lieu de deux. Et Danakh a complété la ligne du 3 en ajoutant une racine...

Donc à part le cadran du 9 les seuls autres cadrans possibles avec 3 répétitions sont:

- le cadran du 4. El Jj avait d'ailleurs [remarqué la "fertilité" du quatre](http://eljjdx.canalblog.com/archives/2007/12/09/7174320.html) il y a longtemps.
- ceux du 1 et du 6, obtenus grâce à la sagacité de Danakh. Bravo² !
- celui du 8, brillamment terminé par Groug grâce à un [Œuf de Colomb](https://fr.wikipedia.org/wiki/Œuf_de_Colomb) de plus. Bravo !

En autorisant quatre répétitions, on peut:

- remplir les lignes 8 et 10 grâce aux recettes \\(8 = x/\\overline{.x} - x/x\\)  et \\(10 = x/\\overline{.x} + x/x\\), ce qui complète le cadran du 2 et celui du 3
- et celui du 5 avec 7 = 5+(5+5)/5

Il faut quand même qu'on vous laisse un os à ronger... Combien de répétitions faut-il pour le cadran du 7 ?
