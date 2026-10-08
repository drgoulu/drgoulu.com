---
title: 'Migration : de Quora à Hugo'
date: 2026-09-17
draft: false
tags:
  - Quora
  - Hugo
  - Informatique
  - Migration
categories:
  - Comment
slug: 'migration-de-quora-a-hugo'
coverImage: ./images/fea4d197-1588-4364-a829-955e901a8c18.jpeg
---

Pendant les années 2019-2026, j'ai délaissé ce blog, mais j'ai été extrêmement [actif sur Quora](https://fr.quora.com/profile/Dr-Goulu).

Initialement, je cherchais une solution plus adaptée à [Kidi'Sciences](https://kidiscience.cafe-sciences.org), le site du C@fé des sciences dédié aux enfants. WordPress étant peu adapté à gérer les Questions/Réponses, j'étais tombé sur Quora alors en plein lancement, mais ils n'étaient pas intéressés ("quoi ? un site où des adultes répondent à des enfants, mais vous êtes inconscients..." m'avaient répondu les amerloques...)

## de DrGoulu à Quora...

Mais à la réflexion ils n'avaient pas tort, et en me prenant peu à peu au jeu, je me suis rendu compte que mes articles de blogs visaient parfois un public trop restreint, et qu'il était peut-être plus constructif de répondre aux questions d'autrui plutôt qu'aux miennes.

Mes quelques 15'000 réponses sur Quora depuis 2019 sont vues environ 50'000 fois par semaine et drainent un trafic non négligeable vers drgoulu.com, mais Quora me semble être devenu un "réseau social comme les autres". 

Initialement, on devait utiliser son nom réel et des humains remarquables (Silhem puis Amaury) s'occupaient de la modération avec des critères stricts qui garantissait une grande qualité du contenu.

Puis le "business model" de Quora est devenu plus clair : drainer le trafic des questions posées à Google vers Quora. En acceptant absolument n'importe quelle question stupide, et sans réel intérêt pour la qualité des réponses

## ... et retour

Ma décision de relancer le blog drgoulu.com est très lié à un raz-le-bol de Quora, mais alors, outre la [migration du vieux contenu de drgoulu.com de WordPress](/2026/08/24/migration/), il me fallait logiquement aussi migrer mon contenu Quora sur le nouveau site drgoulu.com

Heureusement, les auteurs de réponses sur Quora restent propriétaires de leur contenu et peuvent l'obtenir sur simple demande.

J'ai donc obtenu sur simple demande 23 fichiers .zip totalisant 222 Mb, chacun contenant un unique fichier .html avec un millier de mes contributions et un dossier avec les images correspondantes.

### (Quora-importer...)

A ce moment là, je pensais encore conserver drgoulu.com sous WordPress et j'ai commencé par créer (en pur vibe coding) une extension d'importation (en PHP) de Quora sous WordPress : [quora-importer](https://github.com/goulu/quora-importer).

Elle marche relativement bien, ajoutant directement les articles et les images dans la base de données de WordPress, mais j'ai buté sur un problème :

Les sujets de chaque article ne sont pas inclus dans les fichier .html (inclus dans les .zip si vous avez suivi...) donc il faut les chercher sur la page Quora correspondant à chaque réponse.

Sauf que l'URL de cette page n'est pas non plus dans le fichier .html ...

Donc l'importateur doit retrouver cet url à partir du titre de la réponse et du nom de l'auteur.

Sauf que Quora limite la longueur de ce titre, et convertit certains caractères spéciaux en tirets, et pas d'autres, et que cette conversion a changé au cours du temps...

Donc cette recherche en nécessite parfois plusieurs, est assez compliquée, et qu'un hébergeur n'aime pas trop qu'un site aille très souvent en visiter un autre. En fait WordPress a carrément refusé d'accepter mon extension dans la liste officielle...

### (... et Quora2Wordpress)

J'ai donc "vibe codé" [quora2wordpress](https://github.com/goulu/quora2wordpress), un autre outil, en Python, qui réalise la conversion des .zip en fichiers .xml au format WXR de WordPress, prêts à être importés.

C'est là que j'ai réalisé que la mise au point de cet outil était très fastidieuse, car il fallait plusieurs opérations pour finalement visualiser les articles Quora convertis, voir ce qui n'était pas correct, et tout recommencer.

### Quora2Hugo

Alors qu'avec un site statique comme Hugo, je pouvais voir le résultat immédiatement, et éventuellement faire des corrections directement sur les fichiers markdown déjà convertis  au lieu de devoir tout recommencer.

C'est une des raisons qui a fini de me décider à abandonner WordPress pour un générateur de site statique, Hugo en l'occurrence.

Une fois cette décision prise, j'ai simplement demandé à mon IA préférée de réaliser [quora2hugo](https://web.archive.org/web/20260917/https://github.com/drgoulu/quora2hugo) sur la base de quora2wordpress en générant des fichiers markdown contenant chaque article, avec les images placées au bon endroit, des shortcodes hugo pour les images, les liens, les références bibliographiques, etc.

De plus je ne voulais pas noyer drgoulu.com sous 15'000 articles Quora dont beaucoup sont des réponses lapidaires, donc j'ai défini que toutes les réponses de moins de 500 caractères devaient être considérées comme des brouillons que je publierai le cas échéant.

Quelques jours de mise au point plus tard, le nouveau drgoulu.com sous Hugo contient:

- les 695 "anciens" articles de drgoulu.com sous Wordpress
- 6832 nouveaux articles convertis de Quora !
- et 11815 brouillons ...
