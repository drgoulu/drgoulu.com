---
title: Comment s'effectue une insertion dans une table ? Est-ce que le système de gestion de base de données (SGBD) lit toute la table avant l'insertion de la nouvelle ligne pour déterminer son emplacement ?
slug: comment-s-effectue-une-insertion-dans-une-table
date: '2023-05-03'
draft: false
categories:
- Comment
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Comment-seffectue-une-insertion-dans-une-table-Est-ce-que-le-syst%C3%A8me-de-gestion-de-base-de-donn%C3%A9es-SGBD-lit-toute-la-table-avant-linsertion-de-la-nouvelle-ligne-pour-d%C3%A9terminer-son/answer/Dr-Goulu)*

Je vois que vous avez posé plusieurs questions sur le fonctionnement des bases de données, je vais essayer de répondre à toutes d'un coup en vous expliquant le principe de base.

Les bases de données sont étudiées pour stocker les données :

1. volumineuses, donc souvent plus grosses que ce qu'il est possible de stocker en mémoire, même provisoirement
2. de manière permanente, donc sur disque, soit dans des fichiers, soit dans une partition spécifique.
3. efficacement, donc en minimisant au maximum le nombre d'accès et les transferts de données avec le disque.

Donc non, un [Système de gestion de base de données](w:)ne lit jamais une table complète (= souvent un énorme fichier) pour faire une insertion, un effacement ou une mise à jour (update) d'un enregistrement.

Comme les enregistrements ont une taille fixe, le SGBD peut utiliser intensivement l'[Accès direct](w:)à la donnée pour la modifier, la marquer comme effacée ou écrire une nouvelle ligne à la place d'une effacée, ou l'ajouter à la fin.

Tout ce qu'il faut, c'est gérer un "index" de la table, si possible assez petit pour tenir en RAM.

Le plus simple pourrait être simplement un tableau d'entiers (1,2,3,4,..1548) qui dit où sont les lignes valables de la table. Si on supprime la 3ème ligne, on écrit un 0 dedans : (1,2,0,4…1548) et c'est tout.

Quand on veut insérer une ligne, on parcourt l'index (qui est en RAM) et on voit que le 3ème est un 0, donc on écrit dans le fichier à accès direct de la table à la position (3–1)*(taille d'un enregistrement) et on remet le 3 dans l'index.

Mais en pratique on associe plutôt le fichier d'index à la [Clé primaire](w:) de la table en mettant deux éléments dans chaque enregistrements de l'index : (la clé, la position dans le fichier). En utilisant un simple nombre qui s'incrémente comme clé, on aurait

(1,1)(2,2)(3,3)(4,4)…(1548,1548) après avoir inséré les 1548 enregistrements

(1,1)(2,2)(0,3)(4,4)…(1548,1548) après avoir effacé le 3ème

(1,1)(2,2)(1549,3)(4,4)…(1548,1548) après avoir inséré une nouvelle ligne,

ce qui explique pourquoi "SELECT * FROM TABLE" ne garantit pas que vous aurez les résultats dans l'ordre d'insertion.

Alors que se passe-t'il si vous ajoutez "ORDER BY id" où id est votre clé ?

Ben le SGBD va simplement trier l'index par clé et obtenir (1,1)(2,2)(4,4)…(1548,1548),(1549,3)

qu'il suffit de parcourir pour vous renvoyer les lignes dans l'ordre des clés.

En fait c'est tellement pratique que la plupart des SGBD utilisent une liste triée, ou encore mieux une [Table de hachage](w:) pour stocker l'index, et si vous avez une clé qui n'est pas simplement un nombre entier mais par exemple nom+prénom+date de naissance, ils utilisent une [Fonction de hachage](w:)pour obtenir un (grand) nombre entier très probablement unique correspondant à votre clé primaire.

Tout ceci explique aussi pourquoi vous pouvez créer plusieurs index de la même table, par exemple en PostgreSQL:

CREATE INDEX name ON table USING hash (column);

va créer un index de votre table en utilisant les valeurs hachées de column, et le gérer ensuite automatiquement en cas de modification de la table. Cet index sera peut-être

(27346274,4)…(45123476,1)…(47527348,1549)…(5468378654, 765)(5468378654, 2)…(912347634, 1548)

Ensuite, si vous faites SELECT * FROM table WHERE column="tartempion"

votre SGBD va voir qu'il a un index qui correspond au WHERE, donc il va calculer la FonctionDeHachage("tartempion") qui va retourner la valeur de hash 5468378654 par exemple, et en faisant une recherche (dichotomique dans l'index si c'est une liste triée par clé=hash, ou directe si c'est une table de hachage) il saura qu'il y a deux lignes de table qui correspondent, la 765 et la 2. Deux accès directs et hop ! il vous donne vos 2 lignes en 2 accès disques seulement.

Vous voyez donc qu'un SGBD utilise au maximum les (petits) index pour minimiser le nombre d'accès (disque) aux données. N'hésitez donc pas à créer des index, mais sachez que le SGBD va parfois les créer lui-même s'il s'aperçoit que c'est utile, notamment quand on fait des contraintes (FOREIGN_KEY) ou des jointures (JOIN).

Je dois avouer que j'ai mis très longtemps (~30 ans) à comprendre pourquoi l'antique SQL continue à être utilisé. Et un jour j'ai du mettre le nez dans des [Plans d'exécution](w:Plan_d'exécution) pour optimiser des requêtes musclées, et là j'ai compris : les SGBD modernes n'exécutent pas le SQL, elles le "compilent" avec une optimisation des opérations extrêmement performante. En fait un SGBD est souvent plus performant qu'un système de gestion de fichiers à accès direct "maison"…

Voilà, si vous vous imprégnez de ce qui précède, les bases de données ne devraient plus avoir de mystère pour vous.
