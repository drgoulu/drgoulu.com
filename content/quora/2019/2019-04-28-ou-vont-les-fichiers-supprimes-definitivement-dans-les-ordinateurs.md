---
title: Où vont les fichiers supprimés définitivement dans les ordinateurs ?
slug: ou-vont-les-fichiers-supprimes-definitivement-dans-les-ordinateurs
date: '2019-04-28'
draft: false
categories:
- Quora
tags:
- informatique
- la-corbeille
- fichiers-supprimes
- systeme-d-exploitation
- supports-de-stockage-informatique
- gestion-de-fichiers-numeriques
- ordinateurs
- stockage-de-donnees
- suppression-de-fichier
- gestion-de-fichier
coverImage: ./images/quora.png
---

*Article initialement publié sur [Quora](https://fr.quora.com/O%C3%B9-vont-les-fichiers-supprim%C3%A9s-d%C3%A9finitivement-dans-les-ordinateurs/answer/Dr-Goulu)*

Comme un fichier est immatériel, il ne “va” nulle part. Il est “oublié” puis son contenu est détruit en 3 voire 4 étapes:

1. La “poubelle” est un dossier comme les autres. Quand on y met un fichier, il y reste intact, on peut le ressortir etc.
2. Quand on vide la poubelle, ou que le système efface un fichier ou en ré-écrit un de même nom, les [Blocs](w:Bloc_(disque_dur)) contenant les données du fichier sont simplement marqués comme étant libres dans le [Système de fichiers](w:). Mais le contenu des blocs n’est pas modifié, ce qui fait qu’il est encore possible de récupérer les fichiers avec un logiciel type “restore”.
3. Mais si le système en a besoin il peut écrire de nouveaux fichiers dans ces blocs et donc le contenu correspondant de l’ancien fichier sera perdu. Certains outils “forensiques” peuvent encore récupérer les blocs non écrasés. Et dans certains cas (vieux disques durs), il est même possible de retrouver les anciennes données “sous” les nouvelles…
4. C’est pourquoi pour les données critiques il est conseillé d’utiliser un logiciel d’[Effacement de données](w:) qui va réécrire plusieurs fois des données aléatoires sur les blocs libres pour être bien sur qu’il soit physiquement impossible d’accéder.

[La pénible mort des données - Pourquoi Comment Combien](/2012/10/31/la-penible-mort-des-donnees/)
