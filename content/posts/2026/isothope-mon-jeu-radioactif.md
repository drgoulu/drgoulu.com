---
title: ISOThOPE, "mon" jeu radioactif
date: 2026-11-06
draft: false
tags:
  - jeu
  - radioactivite
  - vibe coding
categories:
  - comment
slug: ''
coverImage: ./images/isothope.png
---

C'est une vieille idée que j'avais eue en écrivant "[comment transformer du plomb en or](/2013/03/15/comment-transformer-le-plomb-en-or/)" puis [plusieurs](/2023/04/27/est-il-possible-de-modifier-le-nombre-de-protons-d-un-atome-si-oui-cela-est-il-possible-alors-de-transformer-le-plomb-en-or/) [réponses](/2025/05/12/que-penser-des-physiciens-du-cern-qui-ont-reussi-a-transformer-du-plomb-en-or-malheureusement-pour-une-fraction-de-seconde-certes-mais-est-ce-une-avancee-spectaculaire/) [sur](/2020/02/15/peut-on-fabriquer-de-l-or-en-laboratoire/) [Quora](/2020/09/02/peut-on-obtenir-de-l-or-numero-atomique-79-en-bombardant-deux-autres-elements-par-exemple-ba-56-avec-va-23/) : créer un petit jeu tout simple basé sur la transmutation des isotopes.

Ca a l'air compliqué dit comme ça, mais en gros il suffit de cliquer sur un, deux voire trois boutons dans la bonne séquence pour transmuter un élément en un autre. La seule difficulté est qu'il se désintègre tout seul pendant le jeu, en suivant les règles de la physique. Enfin presque, parce que pour 

Un bon coup de vibe coding plus tard, c'est fait, vous pouvez jouer à [ISOThOPE sur itch.io](https://uluog.itch.io/isothope) ou [sur GitHub](https://goulu.github.io/isotope/), où se trouve aussi le [code source](https://github.com/goulu/isotope).

J'ai mis "mon" jeu entre guillements parce qu'honnêtement, je n'ai pas codé une seule ligne de ce jeu. Je me suis défini comme concepteur et product owner dans  [AGENTS.md](https://github.com/goulu/isotope/blob/master/AGENTS.md), et Gemini a fait le reste.

Même le titre ! Quand j'ai dit à Gemini de créer le titre "Isotope" avec des carreaux définissant des éléments chimiques, il a proposé"ISOThOPE" ? parce qu''il n'y a bizarrement ni élément "T" ni élément "To" ou "Ot". Et parce que [le thorium c'est fantastique](/2013/05/18/latome-vert-le-thorium/)...

{{< figure align="aligncenter" src="./images/isothope%20game.png" >}}

[Le manuel](https://github.com/goulu/isotope/blob/master/src/i18n/manual/fr.md) est aussi l'oeuvre de l'IA, et il me scie littéralement car il agrège plusieurs de mes "prompts" utilisés dans le développement en donnant vraiment l'impression de "comprendre" le jeu. Gemini a été jusqu'à trouver que ma "carte des isotopes" s'appelle un [carte de Segrè](w:Carte_des_nucléides) , ce que j'ignorais.

## Les données

L'IA a trouvé "toute seule" une version digitale de cette carte et la façon de l'intégrer dans le jeu sans base de données, et l'explique elle même :

> Les données de [isotopes.json](https://github.com/goulu/isotope/blob/master/public/isotopes.json) ont été extraites à l'aide du script Python [fetch_real_isotopes.py](https://github.com/goulu/isotope/blob/master/src/fetch_isotopes.py), qui s'appuie sur la bibliothèque Python [**`mendeleev`**](https://mendeleev.readthedocs.io/), qui intègre une base de données nucléaires issue principalement de :
> 1) [NUBASE](https://www-nds.iaea.org/relnsd/nubase/nubase_min.html) (évaluations des propriétés nucléaires et de désintégration publiées avec l'[AIEA](w:) **/** IAEA et l'Atomic Mass Data Center).
> 2) Les données de l'AME (_Atomic Mass Evaluation_) et de la CIAAW (_Commission on Isotopic Abundances and Atomic Weights_).

## Les niveaux

J'ai aussi demandé à l'IA de fabriquer des niveaux de jeu de difficulté progressive et elle m'en a pondu une vingtaine, avec description détaillée

- **Tutoriel 1 : Capture Électronique** : L'atome de Tellure 123 (Te-123) est un cas particulier d'isobare stable. Ajoutez-lui un électron (Clic Droit ou Flèche Bas) pour transmuter un proton en neutron. Vous obtiendrez instantanément de l'Antimoine stable !
- **Tutoriel 2 : Radioactivité Beta-** : L'Oxygène 18 est stable. Ajoutez-lui un neutron (Clic Gauche, Espace ou Flèche Droite) pour le transformer en Oxygène 19. Il deviendra instable et se désintégrera tout seul (Beta-) vers cet élément !
- **Niveau 3 : Le rêve de l'alchimiste** : Transmutation du Mercure 196 en Or stable. C'est la réaction réalisée en 1941 par Sherr, Bainbridge et Anderson en bombardant le mercure avec des neutrons.
_(notez la référence scientifique [1] que l'IA a trouvée "toute seule", mais peut-être dans une de mes réponses Quora...)_

etc. jusqu'à

- **Niveau 13 : La grande course du Néon** : Le Néon 22 est stable. Ajoutez un neutron (⚛), puis tirez de manière extrêmement rapide deux autres neutrons (⚛, ⚛) et enfin deux électrons (⚡, ⚡) sans attendre que les isotopes intermédiaires ne se désintègrent. Vous atteindrez l'Oxygène 25 instable, qui subira une cascade de désintégrations spectaculaire jusqu'au Magnésium 24 stable !

## Jouabilité et difficulté

vous de me dire ce que vous en pensez, mais je trouve le jeu sympa, didactique, mais facile. Voire trop facile. En fait dans les 13 tableaux initiaux, l'ordre dans lequel on tire les particules n'a que peu d'importance voire pas du tout. Et le moment où on tire des particules non plus, donc on arrive presque chaque fois au résultat quoi qu'on fasse.

La raison est que chaque niveau fait une petite excursion dans la zone "rose" du tableau ou dans la zone "bleue" , donc que la nature produit une chaîne de désintégrations β⁻ ou β⁺ toujours identique, les neutrons ou électrons ajoutés produisant eux-aussi le même décalage quelque soit l'ordre où ils sont absorbés.

Bref, je vais demander à l'IA de me générer des tableaux plus complexes en utilisant plusieurs modes de désintégration, notamment $\alpha$ qui doit rendre ça plus intéressant...

Mais ça implique probablement d'agrandir notablement la table des isotopes supportés, donc la taille du jeu, donc va falloir que je trouve une combine pour que ça reste petit et rapide ...

### Le temps logarithmique

Dans la réalité, les demi-vies (`T½`) des isotopes s'étendent de quelques microsecondes (`10⁻⁶ s`) à plusieurs milliards d'années (`10¹⁷ s`). Pour compresser ces 23 ordres de grandeur en quelques secondes de jeu tout en respectant l'ordre de stabilité réel de chaque isotope, j'ai 

`Temps_Jeu = clamp(Base + Pente × log10(T½), Min, Max)`

Les paramètres sont actuellement ajustables au bas de la page du manuel, mais je voudrais fixer des valeurs correspondant à des niveaux de difficulté.

Il y a donc encore un peu de boulot, votre feedback dans les commentaires est bienvenu, voire votre aide dans GitHub aussi...

## itch.io

[itch.io](w:) est le site de référence pour les jeux "indépendants". il en contient des centaines de milliers. Et avec l'IA, ce nombre s’accroît de 6000 par jour !!!

Avec ISOThOPE, ça a fait 6001 hier...

Mon but n'est pas de faire fortune (le jeu est gratuit) mais de voir ce que ça donne de le placer sur un tel site. Dès que le nombre de joueurs dépassera celui des visites sur cette page, ça aura valu le coup.

## Traductions

Pour que le jeu soit intéressant pour un large public, il est traduit en anglais, espagnol et chinois, par un [script translate.ts](https://github.com/goulu/isotope/blob/master/scripts/translate.ts) généré par IA, et utilisant l'IA pour la traduction. (ok je vais ajouter l'allemand et l'italien dans la prochaine version...)

Mais en y pensant, je me suis dit que cette page elle-même méritait d’être au moins en anglais... Donc qu'il faudrait que je passe mon site en multilingue... ce que Hugo supporte nativement... Donc voilà c'est fait aussi : drgoulu.com a désormais un certain nombre de pages traduites en anglais grâce à ISOThOPE !

## Références

1. R. Sherr, K. T. Bainbridge et H. H. Anderson, « _Transmutation of Mercury by Fast Neutrons_ », _Physics Review_, vol. 60, no 7,‎ 1941, p. 473-479 {{< altmetric doi="10.1103/PhysRev.60.473" >}}
