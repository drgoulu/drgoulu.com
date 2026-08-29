---
title: "Google ouvre son infrastructure"
slug: "google-ouvre-son-infrastructure"
date: 2008-04-08
categories: 
  - "non-classe"
tags: 
  - "google"
  - "internet"
  - "programmation"
---

Stupéfaction : Google vient de permettre à 10'000 programmeurs d'utiliser [AppEngine](http://code.google.com/appengine/), un environnement permettant de développer (en Python) des applications qui fonctionneront directement sur les serveurs de Google, en utilisant certaines technologies propriétaires de Google, et tout ça gratuitement.

Jusqu'ici, Google gardait jalousement sa technologie permettant de stocker et d'indexer pratiquement toute l'information du web sur des milliers d'ordinateurs disséminés à travers le monde. On connaissait cependant l'architecture et les principales briques du système :

- le [Google File System](w:) (GFS), permettant de gérer d'énormes fichiers répartis et redondants
- [BigTable](w:), la base de données "orienté colonnes" et reposant sur GFS. Bigtable est utilisé par énormément d'applications Google, l'index du moteur de recherche n'étant pas le moindre : c'est Bigtable qui retrouve en quelques secondes toutes les pages internet contenant des mots donnés...
- [MapReduce](w:) est un programme général permettant de faire simultanément 2 choses avec un très grand nombre de données : une transformation de chaque donnée (Map) et une agrégation des résultats (Reduce). MapReduce sert par exemple à compter le nombre de liens pointant vers chaque page (web link graph reversal), information utilisée pour calculée le [PageRank](w:).

Tout ceci est expliqué cette passionnante vidéo d'une heure, à regarder absolument si vous voulez comprendre.

{{< youtube id="oRwFpQKgRps" width="640" >}}

Pourquoi Google met-il ceci à disposition gratuitement ? Lorsqu'on sait qu' ils n'arrivent pas à recruter autant qu'ils aimeraient, que les 10'000 comptes ont été réservés en quelques minutes, et qu'ils ont les moyens de contrôler puis de racheter toute application intéressante qui résulterait de cette initiative, on peut commencer à apprécier ce coup à sa juste valeur...

sources:

- Michael Arrington "[Google s’apprête à lancer BigTable comme service Web"](http://fr.techcrunch.com/2008/04/05/google-sapprete-a-lancer-bigtable-comme-service-web/), TechCrunch, 5 avril 2008
- Fay Chang & al, "[Bigtable: A Distributed Storage System for Structured Data](http://static.googleusercontent.com/media/research.google.com/fr//archive/bigtable-osdi06.pdf)", [OSDI 2006](http://osdi2006.blogspot.com/2006/10/paper-bigtable-distributed-storage.html)
- Jeffrey Dean and Sanjay Ghemawat, "[MapReduce: Simplified Data Processing on Large Clusters](http://static.googleusercontent.com/media/research.google.com/fr//archive/mapreduce-osdi04.pdf)", OSDI 2004
