---
title: "La tête dans les étoiles"
slug: "la-tete-dans-les-etoiles"
date: 2014-11-18
categories:
  - "Comment"
  - "Pourquoi"
tags: 
  - "astro"
  - "galaxies"
  - "pedagogie"
  - "physique"
coverImage: "./images/15786846832_406cc5f5b4_z_d.jpg"
---

Comment ça, deux mois sans article ? Je pourrais raconter que j'habite trop près d'un trou noir, comme dans "Interstellar", dont je causerai très bientôt, mais en réalité je suis occupé par plusieurs sujets qui provoqueront des articles un jour peut-être, et surtout un qui provoque l'article d'aujourd'hui:

### Le MOOC "Introduction à l'Astrophysique" de l'EPFL

Je voulais depuis longtemps suivre un [MOOC (ou FLOT ou CLOM ?)](w:Formation_en_ligne_ouverte_à_tous), pour voir à quoi ça ressemble. Voyant que le [Laboratoire d'astrophysique de l'EPFL](http://lastro.epfl.ch/) propose le premier [cours d'introduction à l'astrophysique en français sur edX](https://www.edx.org/course/introduction-lastrophysique-introduction-epflx-phys-209x-1), je me suis immédiatement inscrit et je le suis assidûment depuis deux mois en y consacrant une bonne soirée par semaine.

Ce qui m'a surpris temporairement, c'est que le cours ne suit pas le plan des livres d'astronomie de ma jeunesse qui partaient du Soleil et s'en éloignait en décrivant d'abord les planètes, puis les autres étoiles, les nébuleuses, les galaxies etc. Mais comme l'indique très bien le descriptif "Le cours met l'accent sur le lien entre les prédictions théoriques et les observations",

Voici la table des matières du cours, semaine par semaine, avec mes petites remarques personnelles

1. Après un bref aperçu, [Frédéric Courbin](http://people.epfl.ch/frederic.courbin?lang=fr) présente les [lois de Képler](w:) et le [théorème du viriel](w:) que j'ignorais totalement ou avais oublié, et qui permet notamment de lier la taille d'un [amas globulaire](w:) à la vitesse des étoiles qui le forment et réciproquement
2. La deuxième semaine est consacrée au processus de [rayonnement](w:), au [corps noir](w:) et aux [raies d'absorbtion et d'émission](w:raie_spectrale) ainsi qu'aux magnitudes [absolues](w:magnitude_absolue) et [apparentes](w:magnitude_apparente). Là, pour simplifier et vérifier mes calculs pour les exercices, j'ai découvert et commencer à utiliser le module Python [Astropy](http://www.astropy.org/), qui définit de nombreuses constantes et unités bien utiles. Il permet notamment de convertir des unités du [système CGS](w:) comme l' [erg](w:erg_(unité))"que les astrophysiciens continuent d'utiliser, à mon grand dam.
3. On aborde ensuite l'[effet Doppler-Fizeau](w:) et les [milieu interstellaire](w:) et [milieu intergalactique](w:), avant de passer aux [force de marée](w:). Légère déception à ce niveau, j'espérais qu'on aborde le phénomène de ralentissement de la rotation et d'échauffement des astres soumis aux marées, mais j'imagine que ça doit être compliqué...
4. Suit logiquement la [limite de Roche](w:), puis le cours parle des [comètes](w:) avant d'aborder le bilan énergétique des planètes, et en particulier l'effet de leur atmosphère. Là j'ai eu le plaisir de voir esquissé le "[graphique qui vaut 10000 mots](/2011/11/13/climat-le-graphique/)", et la demi surprise de voir que la température de corps noir de la Terre, Vénus et Mars sont beaucoup plus proches que leurs températures au sol. A ce sujet et au passage, [vu ici](http://www.universetoday.com/116274/comet-landing-side-by-side-pics-of-all-alien-surfaces-humanity-explored/) ce beau montage des surfaces de tous\* les astres sur lesquels des engins humains se sont posés en douceur: [![%image\_alt%](./images/15786846832_406cc5f5b4_z_d.jpg)](https://www.flickr.com/photos/31678681@N07/15786846832/)
5. La cinquième semaine est consacrée aux étoiles, leur formation, leur classification et leur distribution dans le [diagramme de Hertzsprung-Russell](w:) illustré de magnifique manière par cette video\[embed\]{{< youtube id="lhSFQXrVr48" width="640" >}}
    
    la formation des étoiles est illustrée dans le [diagramme de Hayashi](w:en:Hayashi_track), puis les réactions nucléaires des différents types d'étoiles ainsi que les morts correspondantes sont décrites. J'ai particulièrement apprécié la méthode de datation d'un amas d'étoile via le "coude" apparaissant dans la distribution des étoiles de la [séquence principale](w:)
6. La sixième semaine est consacrée aux galaxies. Ca commence par leur classification (avec un peu de pub pour [Galaxy Zoo](http://www.galaxyzoo.org/) dans un exercice), leur formation et leur évolution, le tout illustré par de [belles simulations](http://obswww.unige.ch/~revaz/pNbody/rst/Movies.html) faites par Yves Revaz à l'aide de [pNbody](http://obswww.unige.ch/~revaz/pNbody/), un package Python que je vais me dépêcher d'explorer dès que les journées auront 36 heures (il y a de l'espoir : les marées freinent la rotation de la Terre ...). Ensuite le cours aborde le mouvement des étoiles dans les galaxies via les [constantes d'Oort](w:), et se termine par un exposé sur la [matière noire](w:)
7. (ajouté le 24.11.14) La dernière semaine est consacrée à une introduction à la cosmologie : âge de l'univers, galaxies primordiales, [énergie sombre](w:), [fonds diffus cosmologique](w:), échelles des grandes distances et moyens de mesure ([céphéide](w:), [supernova de type Ia](w:)) et le cours se termine avec l'étude des [lentilles gravitationnelles](w:)

Je suis très content d'avoir suivi ce cours, je le recommande vivement aux passionnés de l'espace qui ont (encore) de bonnes notions de maths et de physique. Outre la matière enseignée, l'intérêt du cours réside pour moi dans les liens qui sont établis entre divers domaines de la physique : en jonglant avec la mécanique classique, la thermodynamique et un soupçon de mécanique quantique, on développe une vision cohérente, multidisciplinaire de connaissances qui peuvent paraître disparates lorsqu'on les rencontre la première fois en cours. A mon goût il ne manque qu'un soupçon de relativité assaisonné de trous noirs et d'étoiles à neutrons pour que ce cours soit parfait, mais peut-être sera-ce le sujet d'un cours suivant.

Sinon, la [plateforme edX](https://www.edx.org/) utilisée pour les MOOC de l'[EPFL et beaucoup d'universités prestigieuses](https://www.edx.org/schools-partners) est performante et agréable. On peut passer les vidéos en accéléré ou ralenti, commuter entre la vidéo et la page des exercices à volonté, et une zone de discussion permet de poser des questions ou de râler comme dans une vraie salle d'exercices, en plus calme.

Si mon rythme de publication reste bas, ce sera surement à cause d'un autre MOOC.

Note\* : En fait il existe un 8ème objet : [NEAR Shoemaker](w:) a été crashée sur [l'astéroïde Eros](w:(433)_Éros) en 2001 alors que ce n'était pas prévu initialement, et la sonde a survécu et transmis quelques images avant sa mort.
