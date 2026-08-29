---
title: "Succès hollywoodiens et transformée de Fourier"
slug: "succes-hollywoodiens-et-transformee-de-fourier"
date: 2010-03-06
categories: 
  - "cat2"
tags: 
  - "art"
  - "maths"
  - "media"
  - "researchblogging"
coverImage: "74e0df9764ab035d5a99e89c42fdb0471.png"
---

{{< figure src="images/74e0df9764ab035d5a99e89c42fdb047.png" alt="MathsAlien" link="http://goulu.net/wp-content/uploads/2010/03/mathsalien.png" >}}

Incroyable : une deuxième tentative d'article scientifique en une semaine dans le [torchon du coin café](http://www.20min.ch/ro/)! Ils ont du engager un stagiaire qui vise Science&Vie ... Cette fois c'est "Le succès des films tient à une formule de maths." Attachez vos ceintures :

> ... les films à succès suivent une formule mathématique. Il s'agit de la "transformée de Fourier". Derrière ce nom barbare se cache la fluctuation 1/f ...

Ouch! Ca fait mal à ceux qui ont étudié le barbare sous toutes ses coutures...

Décryptons. Parce qu'à la base il y a une info, une vraie, qui aurait pu être intéressante si elle n'avait pas été massacrée. [James E. Cutting](http://people.psych.cornell.edu/~jec7/), professeur de psychologie à Cornell a mesuré la durée des plans de 150 films tournés entre 1935 et 2005 [[1]](#ref-1). Première chose étonnante : ces films d'une durée moyenne de 126 minutes contiennent de 231 plans pour "Seven Year Itch" (1950) à 3099 pour "King Kong" (2005) , et en moyenne 1132 plans d'une durée toujours aussi moyenne de 6.68 secondes seulement !

L'étude analyse ensuite l'[autocorrélation](w:) de la durée des plans de chaque film, qui a permis de montrer que "les films hollywoodiens sont devenus progressivement découpés en paquets de plans de durée similaire. Par exemple, les scènes d'action sont typiquement formées de plans relativement courts, alors que les scènes de dialogue  sont formées de plans plus longs alternant d'un acteur à l'autre. De ce point de vue, les éditeurs de films ont progressivement augmenté pendant 70 ans  leur contrôle sur le mouvement visuel de leurs narrateurs, rendant les relations entre la durée des plans plus cohérente" (traduction personnelle d'un passage de l'article)

{{< figure src="images/20d090415fee3c51012a23c9fe260b0c.png" alt="movies autocorrelation" caption="autocorrélation de la durée des plans des films en fonction de leur distance, fonction de régression 1/(lag + 1)β et son intervalle de confiance de 95%" link="images/20d090415fee3c51012a23c9fe260b0c.png" align="aligncenter" width="473" >}}

Et le barbare là dedans ? La [transformée de Fourier](w:) permet de décomposer un signal quelconque en une somme de signaux tout simples : des sinusoïdales de fréquences distinctes. Elle permet donc de discerner des périodicités dans des signaux compliqués et bruités. Et de les filtrer. Et de les transmettre. Et de les stocker. Et de les visualiser. Et...  Je m'avance peut-être un peu, mais je dirais que Joseph Fourier est l'Archimède des ingénieurs : sans son coup de génie, tous les bidules électroniques fonctionneraient aussi bien que des bateaux en silex massif. Voilà pour le barbare.

Mais pour terminer cet article, il nous faut encore un ostrogoth et un  hussard : le [théorème de Wiener–Khintchine](w:) a dit à Cutting et son équipe qu'en appliquant la transformée de Fourier à l'autocorrélation de la durée des plans déterminée plus haut, il obtiendront la [densité spectrale de puissance](w:) de chaque film. Ca donne en quelque sorte une mesure de la fréquence de la variation de la durée des scènes (_c'est un peu difficile à exprimer avec des mots, en fait... des propositions ?_)

Toujours est-il que Cutting montre dans son article que cette densité spectrale de puissance change avec le temps. Il l'approxime par une distribution en 1/fα Au débuts du cinéma, la durée des scènes était proche d'un "[bruit blanc](w:)" (α=0) comme si la durée d'un plan n'avait absolument aucune relation avec le reste du film. Aujourd'hui, elle s'approche d'une distribution en 1/f (α=1) typique du "[bruit rose](w:)".

{{< figure src="images/587d18f26adb685f14ab5604f982ca3d.png" alt="Movies alpha" caption="spectre de puissance, intervalle de confiance 95% et valeur de alpha pour des films typiques de leur époque" link="images/587d18f26adb685f14ab5604f982ca3d.png" align="aligncenter" width="485" >}}

Là où ça devient vraiment intéressant, c'est que les processus aléatoires qui ont une distribution en 1/f captent apparemment mieux notre attention [[4]](#ref-4). Cette distribution est typique des processus complexes, biologiques entre autres : ils sont aléatoires, mais leurs composantes "lentes" sont plus importantes que les "rapides" : ça nous intrigue beaucoup plus qu'un phénomène totalement imprévisible, ou totalement prévisible.

Dans l'article, Cutting doute que les réalisateurs hollywoodiens soient réellement conscients de ceci et que leurs monteurs découpent volontairement leurs plans selon une loi en 1/f. Et si c'était plutôt un processus évolutionniste ?

Bon, ok, à la décharge du journaliste stagiaire, il faut du temps bon marché de blogueur initié et plus de place que quelques lignes pour expliquer tout ça. Et s'il n'avait pas raconté n'importe quoi sur Fourier, je ne me serais jamais intéressé à l'article scientifique sous-jascent, que je trouve excellent. Donc finalement il a fait son boulot...

### Références

1. <span id="ref-1"></span>{{< altmetric pmid="20424081" float="right" >}}Cutting JE, DeLong JE, & Nothelfer CE (2010). Attention and the evolution of Hollywood film. Psychological science, 21 (3), 432-9 PMID: [20424081](http://www.ncbi.nlm.nih.gov/pubmed/20424081) [\[pdf\]](http://people.psych.cornell.edu/%7Ejec7/pubs/cuttingetalpsychsci10.pdf)
2. <span id="ref-2"></span>Christine Nothelfer, ["Research Bulletin: Making the Cut"](http://www.onfiction.ca/2009/04/research-bulletin-making-cut.html) 2009, OnFiction
3. <span id="ref-3"></span>"[Solved: The mathematics of the Hollywood blockbuster](http://www.newscientist.com/article/mg20527483.900-cinemaths-grabs-our-fickle-attention.html)", New Scientist, 28 février 2010
4. <span id="ref-4"></span>{{< altmetric pmid="11212631" float="right" >}} Gilden, D.L. (2001). "Cognitive emission of 1/f noise". Psychological Review, 108, 33–56. [(pdf)](http://linkage.rockefeller.edu/wli/moved.8.04/1fnoise/gilden01.pdf)
