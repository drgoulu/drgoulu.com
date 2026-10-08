---
title: Peut-on trouver des nombres premiers, utilisés ensemble, lors de la décomposition du nombre résultant ?
slug: peut-on-trouver-des-nombres-premiers-utilises-ensemble-lors-de-la-decomposition-du-nombre-resultant
date: '2021-10-08'
draft: false
categories:
- Quora
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Peut-on-trouver-des-nombres-premiers-utilis%C3%A9s-ensemble-lors-de-la-d%C3%A9composition-du-nombre-r%C3%A9sultant/answer/Dr-Goulu)*

Je ne suis pas sur de comprendre la question, mais un algo de factorisation doit essayer plusieurs divisions successives par un diviseur premier trouvé pour définir sa puissance. Par exemple ma fonction [Goulib.math2.prime_factors](https://web.archive.org/web/20230925195105/https://goulib.readthedocs.io/en/latest/_modules/Goulib/math2.html#prime_factors) fait ça dans la boucle des lignes 9 à 11 :

```
def prime_factors(num, start=2):
	'''generates all prime factors (ordered) of num'''
	for p in primes_gen(start):
		if num==1: break
		if is_prime(num): #because it's fast
			yield num
			break
		if p>num: break
		while num % p==0:
			yield p
			num=num//p

```

Ensuite

```
def factorize(n):
	return itertools2.compress(prime_factors(n))

```

regroupe les termes consécutifs pour faire par exemple

```
>>>factorize(786456)
[(2,3), (3,3), (11,1), (331,1)]

```

qui signifie $786456=2^3*3^3*11*331$
