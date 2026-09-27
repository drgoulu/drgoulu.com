---
title: Quel est le chiffre de rang n de 0.123456789101112131415161718192021…? En particulier, quel est le chiffre de rang 2025 ?
slug: quel-est-le-chiffre-de-rang-n-de-0-123456789101112131415161718192021-en-particulier-quel-est-le-chiffre-de-rang-2025
date: '2025-01-24'
draft: true
categories:
- Quora
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Quel-est-le-chiffre-de-rang-n-de-0-123456789101112131415161718192021-En-particulier-quel-est-le-chiffre-de-rang-2025/answer/Dr-Goulu)*

C'est la [Constante de Champernowne](w:), ses décimales sont listées par [A033307 - OEIS](https://oeis.org/A033307), où le n-ième terme est

$$a(n) = (10^{(n + (10^i - 10)/9) mod i - i + 1} * \lceil{(9n + 10^i - 1)/(9i) - 1}\rceil ) mod 10$$

avec

$i = \lceil{W(log(10)/10^{1/9} (n - 1/9))/log(10) + 1/9} \rceil$

où W est la branche principale de la fonction W de Lambert.

a(2025)=7
