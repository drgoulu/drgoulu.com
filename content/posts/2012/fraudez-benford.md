---
title: Fraudez fort, fraudez Benford
date: 2012-12-07
draft: false
tags:
  - politique
  - statistiques
  - suisse
  - vote
  - fraude
categories:
  - Comment
slug: fraudez-benford
coverImage: ./images/7f8bedc6e4d093147c595c638acb6093.jpg
---

{{< figure src="./images/7f8bedc6e4d093147c595c638acb6093.jpg" >}}

Fabriquer des données comme des montants de fausses factures demande un certain doigté car il existe des tests statistiques permettant de mesurer leur vraisemblance. Le plus usité de ces tests consiste à vérifier que les données suivent la surprenante [loi de Benford](w:), qui dit que le chiffre le plus à gauche de données statistiques est plus souvent un 1 qu'un 2, plus souvent un 2 qu'un 3 et ainsi de suite jusqu'à 9.

Par exemple, en examinant les données de la [population de 196 pays](w:liste_des_pays_par_population), on constate que 55 pays soit 28.1% ont une population qui commence par le chiffre 1 alors qu'il n'y en a que 11 (5.6%) dont la population commence par un 9. Étonnant, non ?

Et ce phénomène se produit pour une multitude de données aussi différentes que la longueur des rivières, [les cornes et les oeufs](https://web.archive.org/web/20121215095925/http://calque.pagesperso-orange.fr/langages/python/pybenford.html) les cours de la bourse, la quantité de minerai extrait, l'âge des capitaines, etc. La loi de Benford reste valable quelles que soient les unités de mesure utilisées, ou  la [base](w:base_\(arithmétique\)) considérée. Elle s'applique même au second chiffre, qui est plus fréquemment un 0 qu'un 9 (12% contre 8% environ). A partir du 3ème chiffre, les probabilités prévues la [loi de Benford généralisée au n-ième digit](w:en:Benford's_law) deviennent très proches des 10% auxquels on s'attend d'après la [loi de probabilité uniforme](w:loi_uniforme_discrète):

{{< figure align="aligncenter" alt="benford" caption="Graphique produit par ma feuille de calcul Google Docs grâce à des fonctions personnalisées en JavaScript (cliquer pour y accéder)" link="https://docs.google.com/spreadsheet/ccc?key=0Al_D4zS2T4QodHhjM0JxejRKZWpWTWVKUUxISVlfTnc#gid=0" src="./images/8f4951b3ff636eb87e630b7b0c8aaf80.png" width="410" >}}

Donc la prochaine fois qu'on vous présentera une liste de nombres, vérifiez rapidement que près d'un tiers commencent par le chiffre 1. Si ce n'est pas le cas, passez en mode méfiance.

Pour une analyse plus rigoureuse, on utilise des  tests statistiques comme le [test du χ²](w:) pour déterminer si des données suivent bien la loi "naturelle" de Benford. Par exemple sur les populations des 196 pays, on obtient χ²= 1.69 pour le premier digit. D'après [cette table](w:en:Chi-squared_distribution#Table_of_.CF.872_value_vs_p-value) (ligne 8 car il y a 9 chiffres possibles pour le 1er digit) , on peut être confiant à 95% que ces données de population mondiale suivent la loi de Benford, alors que si on génère 196 valeurs avec la fonction RAND d'Excel on obtient un χ²= 112 environ indiquant qu'il n'y a pas une chance sur mille qu'elles aient été produites par un processus "naturel"  (\*).

Ce test est aujourd'hui appliqué dans plusieurs domaines : fraude fiscale ou électorale, comptabilité [[1]](#ref-1) et a montré par exemple que _"les données financières rapportées par le Grèce montrent la plus grande déviation par rapport à la loi de Benford de tous les pays de la zone Euro._" [[2]](#ref-2) Ce qui ne signifie pas que la Grèce ait plus fraudé que les autres, mais seulement qu'elle a (probablement) fraudé moins bien.

Car il est facile de fabriquer des données satisfaisant la loi de Benford, et donc de passer le test du χ². Voici 3 méthodes:

1. Recycler des données déjà existantes dans un autre contexte, comme celles de la population des pays. On peut supprimer ou changer les chiffres les plus à droite, tant qu'on ne touche pas aux 2 digits de gauche, ça passe.
2. Utiliser un générateur de nombres aléatoires fabriquant le nombre digit par digit en respectant les probabilités de la loi de Benford. Il existe de tels générateurs en ligne [[3]](#ref-3)
3. Appliquer la formule magique Excel = POWER(10;6\*RAND()) pour obtenir des nombres "Benford compatibles" entre 0 et un million (10^6)

{{< figure align="aligncenter" alt="Une échelle logarithmique. En choisissant un point au hasard selon une loi uniforme sur cette échelle, vous avez environ une chance sur 3 qu'il corresponde à un nombre qui commence par 1. C'est exactement ce que prévoit la loi de Benford." caption="Une échelle logarithmique. En choisissant un point au hasard selon une loi uniforme sur cette échelle, vous avez environ une chance sur 3 qu'il corresponde à un nombre qui commence par 1. C'est exactement ce que prévoit la loi de Benford." src="./images/4925a2c025ba625201061a1814c92483.png" width="635" >}}

La formule "magique" est aussi simple que ça parce que la loi de Benford n'est pas mystérieuse [[4]](#ref-4) : elle traduit simplement le fait que  dans la nature, la taille d'un nombre a plus de "sens" que sa valeur exacte. Pour choisir un grand nombre au hasard, il faut donc surtout choisir au hasard sa taille, donnée par son [logarithme](w:). Jean-Paul Delahaye clarifie ceci dans le "Pour la Science" de novembre [[5]](#ref-5). En utilisant la [complexité de Kolmogorov](w:), il relie la loi de Benford à la [loi de Zipf](w:) ([dont Xochipili a causé ici](https://web.archive.org/web/20121220012644/http://webinet.cafe-sciences.org/articles/zipf-law/)) , mentionne au passage mon désormais célèbre "[nuage de Sloane](/tags/sloane/)" et arrive à cette conclusion:

> Le monde mathématique est déconcertant : l'infini dénombrable, le plus simple de tous, semble interdire qu'on en pioche les éléments au hasard équitablement, alors que le continu de l'intervalle [0,1], plus gros et plus compliqué que l'infini dénombrable, l'autorise. Heureusement, la loi de Zipf( ou de Benford, nDrG), à sa façon, joue ce rôle de probabilité uniforme sur les entiers.

La loi de Benford s'applique donc lorsque les données couvrent plusieurs ordres de grandeur [[6]](#ref-6)

Pour terminer, voici pourquoi je m'intéresse (aussi...) à la loi de Benford. J'ai été nommé à la Commission Électorale Centrale, qui surveille le bon déroulement des votations et élections du Canton de Genève. Parmi divers tests anti-fraude effectués, il y a un test de χ² sur la loi de Benford du 2ème digit (2BL) publié après chaque vote (par exemple [[6]](#ref-6)), mais auquel je ne comprenais pas grand chose.

Maintenant ça va mieux:

- J'ai compris que ce test ne permet pas de détecter des fraudes commises par des électeurs mais "seulement" une éventuelle falsification des résultats par l'administration chargée du dépouillement.
- Or comme le dit très bien un article récent sur la fraude électorale "ce n'est pas le vote qui fait la démocratie, c'est le dépouillement" [[7]](#ref-7)
- Si le test de Benford a permis de soupçonner des irrégularités dans certaines élections [[8]](#ref-8), il est fortement contesté [[9]](#ref-9), [[10]](#ref-10), [[11]](#ref-11), en particulier pour les élections avec peu de bureaux de vote où le nombre de votants ne varie pas sur plusieurs ordres de grandeur. Or ce dernier point est crucial pour l'applicabilité du test [[12]](#ref-12).
- J'ai une [feuille de calcul](https://docs.google.com/spreadsheet/ccc?key=0Al_D4zS2T4QodHhjM0JxejRKZWpWTWVKUUxISVlfTnc) Google munie de [fonctions Javascript](https://gist.github.com/goulu/ecbea29f3b7959206ab8) permettant d'effectuer ce test. Et aussi un module Python. Je publierai ce code bientôt, mais en jouant avec sur des votes falsifiés par mes soins, il me semble de plus en plus que le test de Benford est compliqué et peu fiable...
- Il existe des tests plus simples, facilement compréhensibles et rapides comme celui [dont a causé Guillaume](https://web.archive.org/web/20121130161454/http://blog.science-infuse.fr/post/L-empreinte-statistique-de-la-fraude-electorale) [[7]](#ref-7)  : un simple graphique X/Y affichant un point par bureau de vote aux coordonnées participation/résultat. En voici un que j'ai fait avec les résultats d'un vote récent [[6]](#ref-6) . C'est pas plus clair  que de savoir que χ² =5.096106 ?

[![](./images/a0f2cd2f1122581853f48daf6d87a414.png "graphique_1 (3)")](./images/a0f2cd2f1122581853f48daf6d87a414.png)

Note\*: en fait l'interprétation de la table est plus délicate que ça, et ma "sur-vulgarisation" de ce passage traduit mon inconfort avec le langage des stats... Si quelqu'un pouvait m'aider via un commentaire éclairé svp...

### Références:

1. <span id="ref-1"></span>Xavier Labouze et Robert Labouze "[La détection des fraudes comptables](https://web.archive.org/web/20130725095002/http://www.webridge.fr/98/Qui_sommes_nous/CV__RL/centres_interet/loi_de_benford.htm)", 2000, Revue Française de Comptabilité n°321
2.  Bernhard Rauch, Max Göttsche, Gernot Brähler, & Stefan Engel (2011). Fact and Fiction in EU-Governmental Economic Data German Economic Review, 12 (3), 243-255 {{< altmetric doi="10.1111/j.1468-0475.2011.00542.x" >}}
3. <span id="ref-3"></span>Robert Harder "[How To Generate Your Own Benford’s Law Numbers](http://blog.iharder.net/2010/11/10/benford-how-to-generate-your-own-benfords-law-numbers/ "Permalink for : How To Generate Your Own Benford’s Law Numbers")" 2010 (avec générateur PHP en ligne)
4.  Nicolas Gauvrit, & Jean-Paul Delahaye (2008). Pourquoi la loi de Benford n'est pas mystérieuse Mathématiques & Sciences humaines (182) {{< altmetric doi="10.4000/msh.10363" >}} [(pdf)](http://msh.revues.org/10363?file=1)
5. <span id="ref-5"></span>Jean-Paul Delahaye, "Les entiers ne naissent pas égaux", Pour la Science N°421 - novembre 2012
6. <span id="ref-6"></span>"[Tests de détection de fraudes pour la votation du 23 septembre 2012](https://web.archive.org/web/20150513224106/http://www.ge.ch/votations/20120923/doc/Evaluation-Statistique.pdf)", Chancellerie d'Etat, Canton de Genève, Suisse
7.  Peter Klimek, Yuri Yegorov, Rudolf Hanel, & Stefan Thurner (2012). It's not the voting that's democracy, it's the counting: Statistical detection of systematic election irregularities PNAS {{< altmetric doi="10.1073/pnas.1210722109" >}} [(pdf)](http://arxiv.org/pdf/1201.3087.pdf)
8.   Luis Pericchi, & David Torres (2011). Quick Anomaly Detection by the Newcomb–Benford Law, with Applications to Electoral Processes Data from the USA, Puerto Rico and Venezuela Statistical Science, 26 (4), 502-516 {{< altmetric doi="10.1214/09-STS296" >}} ([pdf](http://arxiv.org/pdf/1205.3290.pdf))
9. <span id="ref-9"></span>Walter R. Mebane, "[Election Fraud or Strategic Voting? Can Second-digit Tests Tell the Difference?](https://web.archive.org/web/20220314112108/http://polmeth.wustl.edu/media/Paper/pm10mebane.pdf)", Summer Meeting of the Political Methodology Society, University of Iowa, July 22–24, 2010
10. <span id="ref-10"></span>Joseph Deckert, Mikhail Myagkov and Peter C. Ordeshook "[The Irrelevance of Benford’s Law for Detecting Fraud in Elections](https://web.archive.org/web/20140517120934/http://www.vote.caltech.edu/sites/default/files/benford_pdf_4b97cc5b5b.pdf)"
11. <span id="ref-11"></span>Susumu Shikano and Verena Mack, "When Does the Second-Digit Benford’s Law-Test Signal an Election Fraud? Facts or Misleading Test Results", _Journal of Economics and Statistics (Jahrbuecher fuer Nationaloekonomie und Statistik_, 2011, vol. 231, issue 5-6, pages 719-732
12. <span id="ref-12"></span>Antoine Nectoux "[La loi de Benford: Apprendre à frauder ou à détecter les fraudes?](http://blog.kleinproject.org/?p=1175&lang=fr)" sur Blog Projet Klein, 2012
