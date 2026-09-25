---
title: Quelles sont les cinq fractions unitaires qui totalisent 1 ?
slug: quelles-sont-les-cinq-fractions-unitaires-qui-totalisent-1
date: '2021-09-15'
draft: false
categories:
- Quora
tags:
- mathematiques
- probleme-mathematique-integral
- questions
- probleme
- solutions
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Quelles-sont-les-cinq-fractions-unitaires-qui-totalisent-1/answer/Dr-Goulu)*

Ca me rappelle celle des chameaux.

Le Grand Sage Ghouli Al'Methi est appelé par trois frères qui se chamaillent les 17 chameaux que leur père leur a laissé en héritage. Le père a été très clair : la moitié des chameaux reviennent à l'ainé, le tiers au puiné, et le neuvième au cadet. Mais comment faire sans faire boucherie ?

Le Grand Sage Ghouli Al'Methi leur dit alors : prenez mon chameau. Toi l'ainé prends la moitié des 18 chameaux : 9. Toi le puiné prends-en le tiers : 6. Et toi le cadet, le neuvième des 18 chameaux te revient : prends en 2.

9+6+2 = 17, le Grand Sage Ghouli Al'Methi remonte dignement sur le 18ème chameau et s'éloigne dispenser sa Grande Sagesse plus loin.

Donc je dirais 1/2 + 1/3 + 1/9 + 1/18 + 0/1 =1

Mais je vais réfléchir, il doit y avoir une méthode générale …

(edit du 17/9) j'ai pas trouvé de méthode générale alors … Python !

```
n = 100
for a in range(2, n):
	for b in range(a+1, n):
		for c in range(b+1, n):
			for d in range(c+1, n):
				for e in range(d+1, n):
					s = 1/a+1/b+1/c+1/d+1/e
					if s == 1.0:
						print('1/', a, '+ 1/', b, '+ 1/', c,
 							'+ 1/', d, '+ 1/', e, '= 1')

```

et à ma grande surprise on obtient pas mal de solutions:

1/ 2 + 1/ 3 + 1/ 8 + 1/ 40 + 1/ 60 = 1

1/ 2 + 1/ 3 + 1/ 8 + 1/ 42 + 1/ 56 = 1

1/ 2 + 1/ 3 + 1/ 9 + 1/ 30 + 1/ 45 = 1

1/ 2 + 1/ 3 + 1/ 10 + 1/ 20 + 1/ 60 = 1

1/ 2 + 1/ 3 + 1/ 12 + 1/ 15 + 1/ 60 = 1

1/ 2 + 1/ 3 + 1/ 12 + 1/ 16 + 1/ 48 = 1

1/ 2 + 1/ 3 + 1/ 12 + 1/ 18 + 1/ 36 = 1

1/ 2 + 1/ 3 + 1/ 12 + 1/ 20 + 1/ 30 = 1

1/ 2 + 1/ 4 + 1/ 5 + 1/ 30 + 1/ 60 = 1

1/ 2 + 1/ 4 + 1/ 5 + 1/ 36 + 1/ 45 = 1

1/ 2 + 1/ 4 + 1/ 6 + 1/ 15 + 1/ 60 = 1

1/ 2 + 1/ 4 + 1/ 6 + 1/ 16 + 1/ 48 = 1

1/ 2 + 1/ 4 + 1/ 6 + 1/ 18 + 1/ 36 = 1

1/ 2 + 1/ 4 + 1/ 6 + 1/ 20 + 1/ 30 = 1

1/ 2 + 1/ 4 + 1/ 7 + 1/ 12 + 1/ 42 = 1

1/ 2 + 1/ 4 + 1/ 8 + 1/ 9 + 1/ 72 = 1

1/ 2 + 1/ 4 + 1/ 8 + 1/ 10 + 1/ 40 = 1

1/ 2 + 1/ 4 + 1/ 8 + 1/ 12 + 1/ 24 = 1

1/ 2 + 1/ 4 + 1/ 9 + 1/ 12 + 1/ 18 = 1

1/ 2 + 1/ 4 + 1/ 10 + 1/ 12 + 1/ 15 = 1

1/ 2 + 1/ 5 + 1/ 6 + 1/ 12 + 1/ 20 = 1
