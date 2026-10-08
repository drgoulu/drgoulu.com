---
title: "Le Théorème de Noether a un siècle"
slug: "le-theoreme-de-noether-a-un-siecle"
date: 2018-06-23
categories:
  - "Pourquoi"
tags: 
  - "dame"
  - "maths"
  - "physique"
coverImage: "./images/3-82.jpg"
---

{{< figure src="./images/3-82.jpg" alt="Emmy Noether" caption="Emmy Noether" width="400" >}}

Il y a pile un siècle, en 1918, la mathématicienne Emmy Noether publia un résultat si important pour la physique qu'Einstein le qualifia de "monument de la pensée mathématique".

En deux mots, le théorème de Noether relie les lois de conservation à la symétrie des lois de la physique.

## Les lois de conservation

Depuis quelques siècles, les scientifiques se sont aperçus que certaines propriétés d'un système physique restent constantes lors de ses transformations, donnant naissance à autant de [lois de conservation](w:Loi_de_conservation).

La plus connue est certainement le [principe de Lavoisier](w:conservation_de_la_masse) :

> … car rien ne se crée, ni dans les opérations de l'art, ni dans celles de la nature, et l'on peut poser en principe que, dans toute opération, il y a une égale quantité de matière avant et après l'opération ; que la qualité et la quantité des principes est la même, et qu'il n'y a que des changements, des modifications. [[1]](#ref-1)

mais il n'est pas exact. Il semblait très valable jusqu’à la découverte de la radioactivité et de la relativité, qui permettent à la masse de varier. Mais en y incorporant le fameux E=m.c² , c’est devenu le fameux principe de [conservation de l'énergie](w:).

Le principe de conservation de la [quantité de mouvement](w:) est encore plus ancien, déjà mentionné par Galilée au XVIIème siècle. On l'appelle plutôt "[inertie](w:principe_d'inertie) actuellement : en l'absence de forces, les corps tendent à poursuivre leur trajectoire en ligne droite, à vitesse constante.

Le principe de [conservation du moment cinétique](w:) est encore moins intuitif, mais tout aussi réel:

{{< youtube id="yfwb39VCNcQ" width="640" >}}

A ces trois lois de la mécanique classique s'ajoutent la [conservation de la charge électrique](w:) et celle du [flux magnétique](w:) en électromagnétisme, et en physique des particules, la [conservation de la charge de couleur](w:) et celles du [nombre baryonique](w:) et du [nombre leptonique](w:) décrivent les transformations "autorisées" des particules.

Ce paragraphe, mais aussi le jargon courant des physiciens, mélange allègrement les notions de "[loi physique](w:)" et de "[principe physique](w:)". C'est un premier effet du théorème de Noether : historiquement un principe est une "loi apparente qu'aucune expérience n'a invalidée jusque-là bien qu'elle n'ait pas été démontrée." Mais justement, Emmy Noether a démontré que ces principes découlent de la symétrie, et peuvent donc être considérés comme des lois.

## La symétrie en physique

En mathématiques, la [symétrie](w:) est une notion [plus générale que la réflexion dans un miroir](/2009/04/04/miroir/): elle inclut toutes les transformations qui préservent la "structure" d'un objet. En géométrie, les translations et rotations sont aussi des symétries, et comme l'avait pressenti [Pierre Curie](w:) en 1894, cette notion peut être étendue à la physique :

> Je pense qu’il y aurait intérêt à introduire dans l’étude des phénomènes physiques les considérations sur la symétrie familières aux cristallographes. \[…\] Les physiciens utilisent souvent les conditions données par la symétrie, mais négligent généralement de définir la symétrie dans un phénomène. \[…\] Deux milieux de même dissymétrie ont entre eux un lien particulier, dont on peut tirer des conséquences physiques.  [[2]](#ref-2)

En effet, une symétrie correspond mathématiquement à un [automorphisme](w:), qui est une généralisation d'une [bijection](w:) d'un ensemble dans lui-même.  Quand cet ensemble est l'[espace euclidien](w:), on retrouve les symétries géométriques, mais on peut aussi considérer comme ensemble le champ électrique ou l'[espace de Minkowski](w:) dans lequel les [transformations de Lorentz](w:) définissent des symétries.

Ainsi par exemple la "symétrie par translation dans le temps" est la façon scientifique de dire que si on ne lui fait rien subir pendant une seconde, une patate reste une patate.

## Emmy et son théorème

Née en 1882, [Amalie "Emmy" Noether](w:Emmy_Noether) est la fille du mathématicien [Max Noether](w:), très connu alors. Très douée, elle renonce à devenir enseignante de français ou d'anglais pour étudier les maths. Après une thèse en 1907, elle travaille bénévolement à l'Université d'Erlangen car les femmes ne peuvent y obtenir un poste. Repérée par LE [David Hilbert](w:) (né à [Königsberg](/2013/11/22/le-postier-chinois-de-konigsberg/)...), elle le rejoint à l'Université de Göttingen (où là non plus, elle n'est pas acceptée comme professeur(e)...) en 1915.

En fait Hilbert l'a invitée pour profiter de son expertise en [théorie des invariants](w:invariant) pour l'aider à éclaircir certains aspects mathématiques de la [relativité générale](w:) d'Einstein, publiée également en 1915. Hilbert avait remarqué la relativité semblait violer le principe de la conservation de l'énergie, l'énergie gravitationnelle pouvant elle-même créer une force d'attraction\*. Noether fournit une explication de ce paradoxe, et développa à cette occasion son fameux [premier théorème](w:théorème_de_Noether_(physique)) qu'elle [démontra](w:Théorème_de_Noether_(physique)#Démonstrations) en 1915, mais ne publia qu'en 1918 [[3]](#ref-3).

À la réception de son travail, Einstein écrivit à Hilbert :

> J'ai reçu hier de Mademoiselle Noether un article fort intéressant sur les invariants. J'ai été impressionné par le degré de généralité apporté par cette analyse. La vieille garde à Göttingen devrait prendre des leçons de Mademoiselle Noether ; elle semble maîtriser le sujet !

Après ça, elle a finalement été nommée [Privat-docent](w:), mais toujours pas professeur(e) ...

Alors que dit-il finalement, ce fameux théorème ? Il dit :

> À toute transformation infinitésimale qui laisse le [Lagrangien](w:) d'un système invariant à une dérivée temporelle totale près correspond une grandeur physique conservée.

Autrement dit : si une transformation ne change pas les lois de la physique (qui peuvent s'écrire sous la forme d'un [Lagrangien](w:)\*\*), alors il existe une valeur mesurable qui reste constante quelle que soit cette transformation.

Le théorème de Noether démontre donc mathématiquement l'équivalence entre le fait que les lois de la physique restent constantes selon certaines transformations et l'existence de lois de conservation correspondantes !

Par exemple, puisque nous pouvons faire des expériences qui donnent le même résultat quelle que soit notre orientation dans l'espace (c'est le cas car l'espace est [isotrope](w:isotropie), alors il existe une grandeur qui se conserve lorsqu'un système est en rotation. Cette grandeur bien connue des patineuses est le [Moment cinétique](w:)

Voici toutes les lois de conservation et leurs symétries correspondantes:

| Propriété du [système physique](w:) | Symétrie | Invariant |
| --- | --- | --- |
| Espace homogène | Invariance par [translation](w:) dans l'espace | Conservation de l'[impulsion](w:), [Principe d'inertie](w:) |
| Espace isotrope | Invariance par rotation dans l'espace |  [Conservation du moment cinétique](w:) |
| Système indépendant du temps | Invariance par translation dans le temps (les lois sont les mêmes tout le temps) | [Conservation de l'énergie](w:) |
| Pas d'identité propre des particules | Permutation de particules identiques | [Statistique de Fermi-Dirac](w:), [Statistique de Bose-Einstein](w:) |
| Pas de référence absolue pour la phase des particules chargées | Invariance par changement de phase | Conservation de la [charge électrique](w:) |

## L'héritage

Chassée par les nazis, Emmy Noether a poursuivi sa carrière aux Etats-Unis où elle décède en 1935 déjà, à 53 ans, des suites d'une opération. Elle n'a donc pas vu la notoriété de son résultat augmenter spectaculairement dès les années 1970. Comme souvent, il faut quelques temps aux travaux géniaux pour être reconnus :

{{< figure src="./images/Emmy_Noether_NGrams-1.png" alt="Nombre de mentions d'Emmy Noether dans la littérature (Google NGrams)" caption="Nombre de mentions d'Emmy Noether dans la littérature (Google NGrams)" link="https://books.google.com/ngrams/graph?content=Emmy+Noether&year_start=1918&year_end=2008&corpus=15&smoothing=10&share=&direct_url=t1%3B%2CEmmy%20Noether%3B%2Cc0" align="aligncenter" width="640" >}}

C'est que le théorème de Noether est devenu un outil fondamental de la physique théorique, non seulement à cause de l'éclairage qu'il apporte aux lois de conservation, mais aussi comme une méthode de calcul effective. De plus, il facilite l'étude de nouvelles théories : si une telle théorie possède une symétrie, le théorème garantit l'existence d'un invariant, lequel doit être expérimentalement observable.

Pour "la vie de tous les jours" la leçon à retenir est qu'Emmy Noether a démontré que [L’énergie n’est pas une chose](https://fr.quora.com/blog/drgoulu/L%E2%80%99%C3%A9nergie-n%E2%80%99est-pas-une-chose) ! "L'énergie pure", ça n'existe pas. L'[énergie](w:) est juste un nombre qui reste constant lors de toutes les transformations possibles d’un système, et ce nombre existe parce que les lois de la physique ne varient pas dans le temps (= “invariance par translation dans le temps”).

Voilà donc une 4ème et excellente raison de [dire "Non au mouvement perpétuel"](/2012/05/27/dites-non-au-mouvement-perpetuel/) et à tous les doux rêveurs de systèmes "surunitaires" qui produiraient (conditionnel) plus d'énergie qu'ils en consomment (présent):

**Si ! Le [premier principe de la thermodynamique](w:) est démontré depuis un siècle, et par une dame en plus !**

## Notes :

\* j'ai repris plusieurs passages de [la wikipedia](w:Emmy_Noether#Physique) n'ayant pas pu mieux dire...

\*\* le théorème de Noether a été "facilement" étendu aux [Hamilltoniens](w:Opérateur_hamiltonien) plus utilisés en mécanique quantique, physique statistique etc.

## Références

1. <span id="ref-1"></span>Lavoisier, Traité élémentaire de chimie , 1789
2. <span id="ref-2"></span>Pierre Curie, « Sur la symétrie dans les phénomènes physiques : Symétrie d’un champ électrique et d’un champ magnétique », Journal de Physique théorique et appliquée, 3e série, vol. 3,‎ septembre 1894, p. 393-417 {{< altmetric doi="10.1051/jphystap:018940030039300" >}}
3. <span id="ref-3"></span>Noether, E.. "Invariante Variationsprobleme." Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen, Mathematisch-Physikalische Klasse 1918 (1918): 235-257. <https://web.archive.org/web/20180621015646/http://eudml.org/doc/59024>.
4. <span id="ref-4"></span>Kosman-Schwarzbach, Y. (2004). Les théorèmes de Noether : invariance et lois de conservation au XXe siècle (avec une traduction de l’article original : “ Invariante Variationsprobleme ”). \_Book. Éd. de l’École polytechnique. Retrieved from http://www.editions.polytechnique.fr/?recherche=&keywords=noether&Submit=OK
5. <span id="ref-5"></span>Noether, E., & Tavel, M. A. (2005). Invariant Variation Problems. {{< altmetric doi="10.1080/00411457108231446" >}}
6. <span id="ref-6"></span>Kosmann-Schwarzbach, Y. (2011). The Noether Theorems. (J. Z. Buchwald, J. L. Berggren, C. Fraser, T. Sauer, & A. Shapiro, Eds.), \_Book. Springer. {{< altmetric doi="10.1007/978-0-387-87868-3" >}}
7. <span id="ref-7"></span>Philippe Etchecopar, "Emmy Noether, mathématicienne (1882-1935)"
8. <span id="ref-8"></span>Irène, "[Emmy Noether, mathématicienne de génie.](https://www.podcastscience.fm/dossiers/2018/03/02/emmy-noether-mathematicienne-de-genie/)" sur Podcast Science
9. <span id="ref-9"></span>http://www.cafe-sciences.org/?s=noether
10. <span id="ref-10"></span>https://histoireparlesfemmes.com/2016/09/27/emmy-noether-genie-mathematique/
