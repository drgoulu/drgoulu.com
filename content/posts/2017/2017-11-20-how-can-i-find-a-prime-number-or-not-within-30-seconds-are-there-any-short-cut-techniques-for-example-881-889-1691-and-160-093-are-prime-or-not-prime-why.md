---
title: How can I find a prime number or not within 30 seconds? Are there any short cut techniques? For example, 881,889,1691, and 160,093, are prime or not prime, why?
slug: how-can-i-find-a-prime-number-or-not-within-30-seconds-are-there-any-short-cut-techniques-for-example-881-889-1691-and-160-093-are-prime-or-not-prime-why
date: '2017-11-20'
draft: true
categories:
- Quora
tags:
- english
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://www.quora.com/How-can-I-find-a-prime-number-or-not-within-30-seconds-Are-there-any-short-cut-techniques-For-example-8818891691-and-160093-are-prime-or-not-prime-why/answer/Dr-Goulu)*

Check [Chris Taylor’s answer to “a quick way to determine whether a number is prime by hand”](https://math.stackexchange.com/a/783414/131826)on StackExchange :

There's no super-fast way to determine if an arbitrary number is prime by hand. However, you can often quickly determine when a number *isn't* prime, which is often good enough, especially if you are only dealing with smallish numbers, as you often are in math competitions.

- If a number ends in 0, 2, 4, 5, 6 or 8 then it's not prime (except for 2 and 5)
- If the sum of the digits is a multiple of 3, then the number is not prime (except for 3)

Those two rules knock about nearly 75% of numbers.

For numbers below 100, the only false positives are 49=72, 77=7⋅11 and 91=7⋅13 which you can learn.

**Divisibility by 7**

A number of the form 10x+y is divisible by 7 exactly when x−2y is divisible by 7. This allows you to quickly reduce the size of a number until you reach a number that obviously is or isn't a multiple of 7. For example, consider n=847=84×10+7. Then x−2y is 84−14=70 which is obviously divisible by 7, so 847 is also divisible by 7.

**Divisibility by 11**

There is also a simple test for multiples of 11 - starting from the units place, add the first digit, subtract the next digit, add the next one and so on. If you end up with a negative number, treat it as positive. If the result is a multiple of 11, so is the original number.

For example, take n=539. You calculate 9−3+5=11, which is a multiple of 11, and so 539 is a multiple of 11.

Using these rules to check for divisibility by 2, 3, 5, 7 and 11 the only false positive less than 200 is 169, which is easy to remember as it is 132. The only false positives below 300 are 221=13×17, 247=13×19, 289=17×17 and 299=13×23.
