---
title: Quelle est la logique derrière la conception des exceptions ?
slug: quelle-est-la-logique-derriere-la-conception-des-exceptions
date: '2021-09-26'
draft: false
categories:
- Quora
tags:
- developpement-de-logiciels
- exception
- langages-orientes-objet
- observation-des-erreurs
- langage-et-programation
- gestion-des-exceptions
- programmation-orientee-objet
- ingenerie-logiciel
- conception-de-logiciels
- conception-orientee-objet
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Quelle-est-la-logique-derri%C3%A8re-la-conception-des-exceptions/answer/Dr-Goulu)*

La logique est de se concentrer sur le fonctionnement normal du logiciel, et de ne pas l'alourdir par des multitudes de tests pour savoir si un fichier existe ou si un diviseur ne vaut pas 0 toutes les 3 lignes.

Le mécanisme des exceptions permet de traiter les cas anormaux de manière plus centralisée, en permettant au logiciel de continuer à fonctionner, par exemple en demandant à l'utilisateur de ré-entrer des données plutôt que de crasher tout le programme.

Et même dans ce cas, on peut encore produire un fichier de log ou des informations pour le service après vente plus parlant qu'un stack dump en hexadécimal.
