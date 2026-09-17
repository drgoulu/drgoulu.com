---
title: no, that’s definitely not how it is done. Say you want to find a prime of 512 bi...
slug: no-thats-definitely-not-how-it-is-done-say-you-want-to-find-a-prime-of-512-bi
date: '2016-11-02'
draft: false
categories:
- Quora
tags:
- english
- mathematics
- search-algorithms
- large-prime-numbers
- computational-mathematics
- number-theorist
- algorithms-and-computation
- mathematical-sciences
- prime-number-theory
- algorithms
- computational-number-theory
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://www.quora.com/How-do-they-search-for-new-prime-numbers/answer/Steve-Mutuanomine)*

no, that’s definitely not how it is done. Say you want to find a prime of 512 bits for a RSA key. Using the form on [Online RSA key generation](http://www.mobilefish.com/services/rsa_key_generation/rsa_key_generation.php) you get for example 7695569724472218968357329983247783518365587380788656749355931322901061644229490935790270202575436100837766691896209961622963876832779623061869802179230227 which has 154 decimals. So its square root has 77 decimals, which means your method consists in trying to divide the number above by all primes up to 10^77 . Now if you use a [Prime-counting function - Wikipedia](w:en:Prime-counting_function) you’ll find there are about 5.67*10^74 such primes. No supercomputer can try the divisions in the lifetime of the Universe.

Sorry, but I downvote you because you should “know” your answer is good, not “believe” it.
