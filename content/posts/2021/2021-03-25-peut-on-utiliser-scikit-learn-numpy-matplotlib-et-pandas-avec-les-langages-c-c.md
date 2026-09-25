---
title: Peut-on utiliser Scikit-learn, Numpy, Matplotlib et Pandas avec les langages C/C++ ?
slug: peut-on-utiliser-scikit-learn-numpy-matplotlib-et-pandas-avec-les-langages-c-c
date: '2021-03-25'
draft: true
categories:
- Quora
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Peut-on-utiliser-Scikit-learn-Numpy-Matplotlib-et-Pandas-avec-les-langages-C-C/answer/Dr-Goulu)*

Oui : vous linkez un interpréteur python dans votre code C++ :-)

Ou ce qui revient au même, vous faites une librairie python en C/C++ et vous l'utilisez depuis un programme python.

C'est d'ailleurs comme ça que sont faites les librairies que vous mentionnez, ce qui prouve que c'est très efficace.

[https://docs.python.org/3/extend...](https://docs.python.org/3/extending/extending.html)
