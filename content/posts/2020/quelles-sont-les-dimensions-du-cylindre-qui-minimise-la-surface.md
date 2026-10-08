---
title: Quelles sont les dimensions du cylindre qui minimise la surface ?
slug: quelles-sont-les-dimensions-du-cylindre-qui-minimise-la-surface
date: '2020-06-03'
draft: false
categories:
- Quora
tags:
- sciences
- mathematiques
- geometrie
- calcul-mathematique
- post
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Quelles-sont-les-dimensions-du-cylindre-qui-minimise-la-surface/answer/Dr-Goulu)*

il manque "pour un volume V fixé"

on a $V=\pi.r^2.h$ , donc $h=V/(\pi.r^2)$ (1)

et $S=2\pi.r^2 + 2\pi.r.h$ (2) pour la surface $$

En introduisant (1) dans (2) on obtient

S(r)=$2\pi.r^2 + 2V/r$

en dérivant par rapport à r on obtient

S'(r)=4$\pi.r - 2V/r^2$

S'(r)=0 a [une seule solution réelle positive](https://web.archive.org/web/20200603/https://www.wolframalpha.com/input/?i=solve+4*pi*x+-+2*v/x^2=0) pour $r=\sqrt[3]{V/2\pi}$

en introduisant dans (1) on obtient $h=V/\left(\pi.(V/2\pi)^{2/3}\right)$

soit $h=\sqrt[3]{4V/\pi}$
