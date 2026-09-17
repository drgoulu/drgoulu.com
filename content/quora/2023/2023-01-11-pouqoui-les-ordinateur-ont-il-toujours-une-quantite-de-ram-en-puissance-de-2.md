---
title: Pouqoui les ordinateur ont-il toujours une quantité de RAM en puissance de 2?
slug: pouqoui-les-ordinateur-ont-il-toujours-une-quantite-de-ram-en-puissance-de-2
date: '2023-01-11'
draft: false
categories:
- Quora
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Pouqoui-les-ordinateur-ont-il-toujours-une-quantit%C3%A9-de-RAM-en-puissance-de-2/answer/Dr-Goulu)*

parce que pour accéder à une donnée en RAM, le processeur utilise une [Adresse mémoire](w:Adressage_mémoire) qui est elle-même un nombre binaire sur N bits.

Le processeur peut donc accéder à 2^N données au maximum, chacune de ces données ayant 2^n bits comme l'expliquent les autres réponses qui confondent n et N.

Les barrettes de 32Go actuelles stockent des données de n=32 bits soit 4 octets et en contiennent donc 8G, ce qui correspond à N=33 bits d'adresse.

Comme les processeurs actuels travaillent avec des données de 64 bits, il faut toujours mettre deux barrettes "en parallèle" pour obtenir n=64 bits, mais on aura toujours N=33 bits d'adresse et n=64 bits de données pour cette mémoire.

Si on a ajoute un deuxième "banc" de 2 barrettes identique, c'est le 34ème des bits d'adresse qui permettra de distinguer entre les deux bancs, et on aura N=34.

Maintenant si on met un deuxième banc de barrettes de taille différente, par exemple de 16Go ou des 64Go, on peut très bien se retrouver avec 32+16=48 ou 32+64=96 Go qui ne sont pas des puissances de 2, mais il n'y a pas de justification économique à faire ça avec un ordinateur neuf, et si on le fait en mettant à jour un vieil ordinateur on risque de limiter la vitesse d'accès à la RAM à la RAM la plus lente…
