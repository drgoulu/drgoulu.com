---
title: Pourquoi Quora ne réalise pas la frustration qu’apporte le fait qu’on ne peut pas zoomer les photos sur leur site ?
slug: pourquoi-quora-ne-realise-pas-la-frustration-quapporte-le-fait-quon-ne-peut-pas-zoomer-les-photos-sur-leur-site
date: '2022-07-13'
draft: false
categories:
- Pourquoi
tags:
- quora
- fonctionnalite
- frustration
- site-web
- experience-client
- photos
- zoom
- experience-utilisateur
- insatisfaction
- images
coverImage: ./images/qimg-5fcb98ad039a59387b738bebefa2639c.jpg
---

*Réponse publiée [sur Quora](https://fr.quora.com/Pourquoi-Quora-ne-r%C3%A9alise-pas-la-frustration-qu-apporte-le-fait-qu-on-ne-peut-pas-zoomer-les-photos-sur-leur-site/answer/Dr-Goulu)*

C'est pour vous motiver à apprendre vous-même comment faire :-)

Si vous avez Chrome, cliquez avec le bouton droit sur l'image et sélectionnez "inspect"

Une fenêtre va s'ouvrir en indiquant le code HTML de la page, le code de l'image étant sélectionné

Par exemple sur l'image de mon profil vous allez obtenir quelque chose comme ça :

```
<img class="q-image qu-display--block qu-size--40 qu-minWidth--40" src="https://qph.fs.quoracdn.net/main-thumb-9739516-200-xxWhk3As1uaiu13gopjkor5E0mBPQvYv.jpeg" size="40" alt="Photo de profil pour Philippe Guglielmetti" style="box-sizing: border-box; max-width: 100%; position: relative;">

```

avec le lien en bleu vers l'image cliquable. Cliquez dessus :

![](./images/qimg-5fcb98ad039a59387b738bebefa2639c.jpg)

et voilà !
