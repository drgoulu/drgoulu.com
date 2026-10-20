---
title: Zotero et Pour la Science
date: 2026-10-20
draft: false
tags:
  - internet
  - livres
  - degafamisation
  - pour la science
  - vibe coding
categories:
  - comment
slug: ''
coverImage: ./images/zotero-et-pour-la-science.jpg
---

Depuis 1990 environ j'utilise des gestionnaires de références bibliographiques pour retrouver mes lectures et les citer proprement. Pendant ma thèse c'était [EndNote](w:) sur Mac, puis j'ai [jonglé entre](/2013/10/25/comment-gerer-ses-articles/) [Zotero](w:) et [Mendeley](w:) pendant mes années Windows, entassant environ 9430 références d'articles, livres scientifiques et brevets, et 4827 fichiers .pdf totalisant 3.4 Gb. 

C'est pas beaucoup, mais trop pour le stockage gratuit offert par Mendeley (2 Gb) ou Zotero (300 Mb). Donc j'avais mis mes .pdf sur Google Drive et spécifié le dossier synchronisé sur mon PC comme dossier pour les pièces attachées de Mendeley. J'y avais donc un accès transparent sur mon PC, et possible depuis mon smartphone.

## Mais :

1. j'ai migré sous Linux et Proton Drive : plus de synchro bidirectionnelle (ou pas encore...)
2. Mendeley avait une app Android utilisable, mais ils l'ont retirée et la version web est inutilisable sur smartphone
3. Par contre [Zotero a une app](https://play.google.com/store/apps/details?id=org.zotero.android&hl=en), un peu minimale mais utilisable
4. et surtout Zotero permet de stocker les .pdf sur un serveur [WebDAV](w:) alors que Mendeley ne permet que de payer pour un stockage plus gros.
5. Mais encore, Mendeley appartient à Elsevier alors que Zotero est open source

## Et ça, ça change tout.

Parce qu'en 30 ans de collecte d'articles en tous genres migrés de PC en sites et de logiciels en autres logiciels et vice-versa, ma bibliothèque avait quant même pas mal souffert, et [zotero offre plein de manières de la réparer](https://www.zotero.org/support/dev/)

D'abord, j'avais une multitude de références duplifiées, voire triplifiées, et Zotero ne permet que de fusionner des références une par une à la main. Heureusement ChenglongMa a créé 

### [zoplicate](https://github.com/ChenglongMa/zoplicate)

un plugin qui automatise ces fusions. Je l'installe illico mais malheureusement, il ne fusionnait que les références du même type, or j'avais pas mal de duplicates de types différents comme "Rapport" et "Article".

L'Open Source à l'ère du Vibe Coding, c'est génial : j'ai forké et cloné ce plugin chez moi, et en ne connaissant strictement rien à l'API de Zotero ou à l'écriture de plugins pour ce logiciel, j'ai juste donné un "prompt" du genre:

> autorise la fusion de références de types différents, en choisissant le type qui minimise la perte d'information

Quelques minutes plus tard je pushe un [commit qui fait ça](https://github.com/goulu/zoplicate/commit/6d94dc1a2a417d032bccd9ecb6b8b29c4791c5ab#diff-d04c18892ed72223035966c81d45fafcad02d90913fa5e57f6591fe1c213f06f) (avec documentation en chinois...) et le même jour [ChenglongMa accepte ma Pull Request 223](https://github.com/ChenglongMa/zoplicate/pull/223) et dorénavant zoplicate est goulument plus puissant.

## [zotero-tools](https://github.com/goulu/zotero-tools)

Mais les doublons n'étaient pas le seul problème de ma bibliographie.

Toujours en pur Vibe Coding, j'ai trois outils regroupés dans un seul projet "zotero-tools" :

1. [zotero-cleaner](https://github.com/goulu/zotero-tools#2-zotero-cleaner-zotero-cleaner) qui nettoie les titres, tags, pièces jointes
2. [pdf-importer](https://github.com/goulu/zotero-tools#1-pdf-importer-pdf-importer--zotero-import-pdf) qui a raccroché tous mes .pdf isolés à des articles, ou les a créés à partir du .pdf
3. pour-la-science, qui devait importer des articles depuis [le site du journal](https://www.pourlascience.fr), mais j'ai finalement décidé de faire autrement

### Pour la Science

En fait 4617 de mes références sont des articles du journal [Pour la Science](w:) auquel j'ai été abonné très longtemps avant de [me fâcher](/2016/12/12/bye-bye-pour-la-science/) pendant 10 ans. Mais ce journal est vraiment bien, et en espérant que leur service client ce soit amélioré, je me suis réabonné...

Mais le plugin [zotero-connector](https://chromewebstore.google.com/detail/zotero-connector/ekhagklcjbdpajgpjgmbionohlpdbjgc) pour Vivaldi (et Chrome) ne reconnaît hélas pas le site de pour la science pour importer correctement les articles.

Sauf qu'on peut lui apprendre... 

Fork de [https://github.com/zotero/translators](https://github.com/zotero/translators), clone, vibe coding en mentionnant [cette page](https://www.zotero.org/support/dev/translators/coding#web_translators) à l'IA comme référence,  [commit](https://github.com/goulu/zotero-translators/commit/ee322a3a512bbb9359cf9faac3b3ddc349eb59d0), et [pull request 3699](https://github.com/zotero/translators/pull/3699) : une heure plus tard Zotero sait importer les articles de Pour la Science !

###### Références

1. [Zotero vs Mendeley: Le Duel Ultime (et les astuces 2026)](https://www.stagepfe.com/2026/03/zotero-vs-mendeley-le-duel-ultime-et.html)
