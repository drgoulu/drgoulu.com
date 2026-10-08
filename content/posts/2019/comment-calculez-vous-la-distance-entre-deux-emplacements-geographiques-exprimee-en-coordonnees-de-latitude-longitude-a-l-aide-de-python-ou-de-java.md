---
title: Comment calculez-vous la distance entre deux emplacements géographiques exprimée en coordonnées de latitude-longitude à l'aide de Python ou de Java ?
slug: comment-calculez-vous-la-distance-entre-deux-emplacements-geographiques-exprimee-en-coordonnees-de-latitude-longitude-a-l-aide-de-python-ou-de-java
date: '2019-04-30'
draft: true
categories:
- Comment
tags: []
coverImage: ./images/quora.png
---

*Article initialement publié sur [Quora](https://fr.quora.com/Comment-calculez-vous-la-distance-entre-deux-emplacements-g%C3%A9ographiques-exprim%C3%A9e-en-coordonn%C3%A9es-de-latitude-longitude-%C3%A0-l-aide-de-Python-ou-de-Java/answer/Dr-Goulu)*

le package [geopy](https://pypi.org/project/geopy/) a deux [fonctions distance](https://geopy.readthedocs.io/en/stable/#module-geopy.distance) (grand cercle et géodésique) dont le [code est là](https://github.com/geopy/geopy/blob/master/geopy/distance.py)

La version plus simple est là : [Getting distance between two points based on latitude/longitude](https://web.archive.org/web/20210725081956/https://stackoverflow.com/a/19412565)
