---
title: Salut Morgane.J'ai répondu un peu vite parce que je connais bien NetworkX pour l...
slug: salut-morgane-j-ai-repondu-un-peu-vite-parce-que-je-connais-bien-networkx-pour-l
date: '2021-02-12'
draft: false
categories:
- Quora
tags:
- intelligence-artificielle
- bibliotheques-python
- sciences-informatiques
- python-langage-de-programmation
- systeme-de-recommandation
- algorithmes-de-graphe
- traitement-de-donnees
- science-des-donnees
- theorie-de-graphe
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Quelles-sont-les-meilleures-libraires-Python-pour-réaliser-des-calculs-de-graphe-dans-le-cadre-dun-moteur-de-recommandations/answer/Dr-Goulu)*

Salut Morgane.

J'ai répondu un peu vite parce que je connais bien NetworkX pour l'avoir étendu aux graphes euleriens ( [Goulib.graph](https://goulib.readthedocs.io/en/latest/modules/Goulib.graph.html)) et entendu parler de igraph par un collègue, mais d'après [Benchmark of popular graph/network packages v2](https://www.timlrx.com/blog/benchmark-of-popular-graph-network-packages-v2) il y a aussi [NetworKit](https://networkit.github.io/) et [graph-tool](https://graph-tool.skewed.de/) (tous deux en C++ avec interface python) qui régatent en performance.

Le benchmark montre d'importantes différences selon l'algo, donc peut-être que ça vaut la peine de bien regarder la lib la plus efficace sur ton problème …
