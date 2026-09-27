---
title: What is the number that the square of its half is equal to the number reversed?
slug: what-is-the-number-that-the-square-of-its-half-is-equal-to-the-number-reversed
date: '2018-01-18'
draft: true
categories:
- Quora
tags:
- english
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://www.quora.com/What-is-the-number-that-the-square-of-its-half-is-equal-to-the-number-reversed/answer/Dr-Goulu)*

```
# python code
from itertools import count
from Goulib.math2 import reverse
for i in count(1):
  if i*i==reverse(2*i):
    print(2*i,i*i)

```

gives:
4 4
18 81
and nothing more, which can easily be demonstrated
