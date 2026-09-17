---
title: Quelles sont les pires erreurs d'algorithmes ?
slug: quelles-sont-les-pires-erreurs-d-algorithmes
date: '2022-02-16'
draft: false
categories:
- Quora
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Quelles-sont-les-pires-erreurs-d-algorithmes/answer/Dr-Goulu)*

Les algorithmes ne font pas d'erreurs, ce sont les programmeurs qui en font.

Les "pires" sont de ne pas traiter tous les cas possibles, et donc de laisser la porte ouverte à des plantages de la machine, voir à compromettre sa sécurité.

Le cas le plus simple et connu est la [Bombe de décompression](w:): un petit fichier .zip ou image compressée qui devient absolument énorme à la décompression si l'algo de décompression n'est pas assez prudent…

Les curieux en trouveront de belles ici : [A better zip bomb](https://www.bamsoftware.com/hacks/zipbomb/) (pour tester que leur logiciel de décompression détecte le cas bien sur, je décline toute responsabilité si vous utilisez un vieux décompresseur mal foutu qui va remplir votre disque dur …)

Et si l'algo de décompression utilise un buffer de taille limitée, on peut même viser un [Dépassement de tampon](w:)qui peut permettre d'insérer du code malveillant. Ca s'est vu : [IrfanView TIFF Image Decompression Buffer Overflow Vulnerability | HKCERT](https://www.hkcert.org/security-bulletin/irfanview-tiff-image-decompression-buffer-overflow-vulnerability)

Bref, à mon sens la pire "erreur d'algorithme" est de coder soi-même un algo déjà disponible souvent gratuitement sur GitHub ou ailleurs, testé et validé par de nombreux utilisateurs. Il vaut bien mieux ajouter des tests à ce code que d'en réécrire un qui aura peut-être des bugs, et probablement des failles.
