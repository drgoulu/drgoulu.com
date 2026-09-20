---
title: de rien, désolé… en Python ça donnerait ça:, pour vous motiver:from random impor...
slug: de-rien-desole-en-python-ca-donnerait-ca-pour-vous-motiver-from-random-impor
date: '2020-08-25'
draft: true
categories:
- Quora
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Est-ce-quelquun-peut-maide-à-faire-le-fit-en-utilisant-la-methode-des-splines-cubiques-en-fortran/answer/Dr-Goulu)*

de rien, désolé… en Python ça donnerait ça:, pour vous motiver:

from random import random

from scipy.interpolate import CubicSpline

n=15769

x=range(n)

y=[random() for _ in range(n)] # aléatoires

s=CubicSpline(x,y)

for i in range(n-1):

with open(r"out/srf_v%05d.asc"%i,"w") as f:

f.write("%f %f %f"%(s.c[0,i],s.c[1,i],s.c[2,i]))
