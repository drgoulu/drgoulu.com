---

title: Je suis un historien qui travaille sur un groupe d'individus qui ont des relations professionnelles et/ou personnelles entre eux, ainsi que des rapports hiérarchiques. Quel outil informatique pourrais-je utiliser pour rendre compte de ces liens ?
slug: je-suis-un-historien-qui-travaille-sur-un-groupe-d-individus-qui-ont-des-relations-professionnelles-et-ou-personnelles-entre-eux-ainsi-que-des-rapports-hierarchiques-quel-outil-informatique-pourrais-je-utiliser-pour-rendre-compte-de
date: '2023-05-25'
draft: true
categories:
- Quora
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Je-suis-un-historien-qui-travaille-sur-un-groupe-d-individus-qui-ont-des-relations-professionnelles-et-ou-personnelles-entre-eux-ainsi-que-des-rapports-hi%C3%A9rarchiques-Quel-outil-informatique/answer/Dr-Goulu)*

Vous voulez obtenir des représentations graphiques de ces relations ?

Regardez les exemples de [GraphViz](https://graphviz.org/gallery/) pour voir si ça correspond à ce que vous aimeriez montrer, par exemple [Family Tree](https://graphviz.org/Gallery/directed/kennedyanc.html) ou [Siblings](https://graphviz.org/Gallery/directed/siblings.html) .

GraphViz est ce qu'il y a de mieux pour placer automatiquement les noeuds (= vos individus …) de manière à minimiser les croisement des arêtes du graphe (= les relations) même quand il y en a des centaines, voire des milliers.

Tout ce que vous devez faire, c'est décrire votre graphe dans le [Langage DOT](https://graphviz.org/doc/info/lang.html) .

Sous chaque [exemple](https://graphviz.org/gallery/), vous trouverez le code DOT correspondant.

Ce langage est devenu une sorte de standard pour les graphes, par exemple [l](https://networkx.org/documentation/stable/reference/generated/networkx.drawing.nx_pydot.write_dot.html)e package python [NetworkX a une fonction write_dot](https://networkx.org/documentation/stable/reference/generated/networkx.drawing.nx_pydot.write_dot.html) qui peut vous permettre d'exporter un graphe tiré d'une base de données ou même d'une feuille Excel par exemple

Mais graphViz est un peu vieux, il a eu de la peine à s'adapter à internet, alors [Mermaid](https://mermaid.js.org/intro/) fait la même chose sur des pages web à partir d'un langage très proche de DOT.

Vous pouvez l'essayer en ligne ici : [Online FlowChart & Diagrams Editor](https://mermaid.live/edit) .

Ca marche bien sur des "petits" graphes de quelques dizaines de nœuds.

Donc je dirais :

- si vous avez de petits graphes de moins de 10 individus, peut-être que l'éditeur en ligne de Mermaid suffit
- si vous avez entre 10 et 100 individus, écrivez un fichier DOT ou Mermaid à la main.
- au dessus de 100 nœuds, mettez tout dans un fichier Excel et utilisez [Excel to Graphviz](https://web.archive.org/web/20210814035027/https://sourceforge.net/projects/excel-to-graphviz/) (que je viens de trouver, pas testé…) pour générer un fichier DOT à partir de vos données
