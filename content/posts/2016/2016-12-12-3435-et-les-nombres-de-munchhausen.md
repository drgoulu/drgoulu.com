---
title: 3435 et les nombres de Münchhausen
slug: 3435-et-les-nombres-de-munchhausen
date: 2016-12-12
categories:
  - cat2
tags:
  - nombres
  - programmation
  - python
coverImage: 220px-Munchhausen-AWille.jpg
draft: false
---

{{< figure src="images/220px-Munchhausen-AWille.jpg" alt="Le baron de Münchausen se déplaçait en chevauchant des boulets de canon..." caption="Le baron de Münchausen se déplaçait en chevauchant des boulets de canon..." width="220" >}}

8208 est un [nombre narcissique](w:) parce que 8208 = 84 + 24 + 04 + 84  : il est égal à la somme de ses chiffres élevée à la puissance correspondant au nombre de ses chiffres. Il y en a beaucoup ([A005188](https://oeis.org/A005188)) mais pas une infinité : 115132219018763992565095597973971522401 est le plus grand

3435 = 33 + 44 + 33 + 55  D'autres nombres possèdent-ils cette étonnante propriété ? C'est la question posée dans [cet article de John D. Cook](http://www.johndcook.com/blog/2016/09/19/munchausen-numbers/) [[1]](#ref-1)

La réponse est "oui, mais ça dépend". Il y a de toutes façons le 1 parce que 11 = 1, mais il y a aussi 0 et 34664084 si on définit 00 = 0, alors que tout le monde sait que 00 = 1 . [Ou pas](http://eljjdx.canalblog.com/archives/2011/05/29/21255118.html).

Et voilà, ce sont les seuls [nombres de Münchhausen](w:nombre_de_Münchhausen) ([A046253](https://oeis.org/A046253)), ainsi nommés dans l'article qui les a découverts [[2]](#ref-2) par similitude avec les  ([A005188](https://oeis.org/A005188)) comme .

Les chiffres des nombres narcissiques sont élevés à la puissance , [Baron de Münchhausen](https://fr.wikipedia.org/wiki/Baron_de Münchhausen) étant considéré comme le Narcisse ultime.

 

[mon code](https://gist.github.com/goulu/5121c161d224229b76a38485c4122794#file-munchausen-py) est vachement proche de https://oeis.org/A005188 trouvé après

{{< gist "goulu" "5121c161d224229b76a38485c4122794" >}}

base 2 : \['1'\] 0:00:00 base 3 : \['1', '12', '22'\] 0:00:00 base 4 : \['1', '130', '131', '313'\] 0:00:00.001000 base 5 : \['1', '103', '2024'\] 0:00:00 base 6 : \['1', '22352', '23452'\] 0:00:00.001000 base 7 : \['1', '13454'\] 0:00:00.004001 base 8 : \['1', '401'\] 0:00:00.016001 base 9 : \['1', '30', '31', '156262', '1647063', '1656547', '34664084'\] 0:00:00.0 70007 base 10 : \['1', '3435', '438579088'\] 0:00:00.293030 base 11 : \['1', '66501', '517503', '18453278', '18453487'\] 0:00:01.211121 base 12 : \['1', '3a67a54832'\] 0:00:05.128513 base 13 : \['1', '33660', '33661', '2aa834668a', '4ca92a233518', '4ca92a233538'\] 0:01:13.514350 base 14 : \['1', '23'\] 0:01:29.025902 base 15 : \['1', '4b1648420dcd2', '5acbc41c19e402', '1243eed3419110e', '5acbc41c19e333', '5a99e538339a43'\] 4:11:52.097591 base 16 : \['1', 'c4ef722b7820c2f', 'c76712ffc311e6e', '123b2309ff572f6b', 'c4ef722b782c26f'\] 4 days, 19:39:16.014207

Note : \* Idée pour un conte : expliquer comment le Baron de Münchhausen a honteusement perdu un umlaut et un H en traversant l'Atlantique ...

### Références:

1. <span id="ref-1"></span>John D. Cook "[Munchausen Numbers](http://www.johndcook.com/blog/2016/09/19/munchausen-numbers/)", 2009
2. <span id="ref-2"></span>Daan Van Berkel "[On a curious property of 3435](http://arxiv.org/pdf/0911.3038v2.pdf)", 2009 {{< altmetric arxiv="0911.3038" >}}
