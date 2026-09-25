---
title: Existe-t-il toujours un chiffre (de 1 à 9) qui ajouté à gauche d'un nombre premier (>5) forme un nouveau nombre premier. Si la réponse est négative, pouvez-vous me donner le premier contre-exemple ?
slug: existe-t-il-toujours-un-chiffre-de-1-a-9-qui-ajoute-a-gauche-d-un-nombre-premier-5-forme-un-nouveau-nombre-premier
date: '2024-10-31'
draft: true
categories:
- Quora
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Existe-t-il-toujours-un-chiffre-de-1-%C3%A0-9-qui-ajout%C3%A9-%C3%A0-gauche-d-un-nombre-premier-5-forme-un-nouveau-nombre-premier-Si-la-r%C3%A9ponse-est-n%C3%A9gative-pouvez-vous-me-donner-le-premier-contre/answer/Dr-Goulu)*

53.

Ah je me suis trompé, ça c'est en ajoutant un chiffre à droite…

À gauche c'est 149

Code python mal formaté (mon premier code python sur smartphone…)

```
d ef is_prime(n):
   if n == 2 or n == 3: return True
   if n < 2 or n%2 == 0: return False
   if n < 9: return True
   if n%3 == 0: return False
   r = int(n**0.5)
   f = 5
   while f <= r:
   if n % f == 0: return False
   if n % (f+2) == 0: return False
   f += 6
   return True
n=7
 while True:
   if is_prime(n):
   found=True
   for d in "123456789":
   n2=int(d+str(n))
   if is_prime(n2):
   print(n2, "is prime")
   found=False
   break
   if found:
   print(n)
   exit()
   n+=2

```

Il y en a beaucoup, c'est [A155762 - OEIS](https://oeis.org/A155762)
