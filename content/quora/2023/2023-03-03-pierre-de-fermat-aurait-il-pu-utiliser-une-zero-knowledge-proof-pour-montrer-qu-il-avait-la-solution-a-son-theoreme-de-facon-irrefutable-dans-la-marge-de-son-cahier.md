---
title: Pierre de Fermat aurait-il pu utiliser une "Zero Knowledge Proof" pour montrer qu'il avait la solution à son théorème, de façon irréfutable, dans la marge de son cahier ?
slug: pierre-de-fermat-aurait-il-pu-utiliser-une-zero-knowledge-proof-pour-montrer-qu-il-avait-la-solution-a-son-theoreme-de-facon-irrefutable-dans-la-marge-de-son-cahier
date: '2023-03-03'
draft: false
categories:
- Quora
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Pierre-de-Fermat-aurait-il-pu-utiliser-une-Zero-Knowledge-Proof-pour-montrer-qu-il-avait-la-solution-%C3%A0-son-th%C3%A9or%C3%A8me-de-fa%C3%A7on-irr%C3%A9futable-dans-la-marge-de-son-cahier/answer/Dr-Goulu)*

Non.

La [Preuve à divulgation nulle de connaissance](w:)(ZKP) consiste à prouver qu'on dispose d'une information, or le [Dernier théorème de Fermat](w:)dit qu'il n'existe PAS d'entiers strictement positifs x,y,z tels que $x^n+y^n=z^n$ pour $n>2$

S'il existait de tels nombres, Fermat aurait simplement pu écrire 3987^12 + 4365^12 = 4472^12 dans la marge et vous auriez pu vérifier avec une calculatrice, sans que Fermat ait eu besoin d'expliquer comment il avait trouvé ce contre-exemple[[1]](#tENZQ) .

Donc l'information est en l'occurence une démonstration rigoureuse et complète de l'inexistence de ces nombres, et là on ne voit pas comment prouver qu'on a une démonstration correcte sans la donner…

De plus, un "protocole Sigma" tel que nécessaire dans une ZKP est un protocole itératif dans lequel le "vérifieur" envoie plusieurs "défis" au "prouveur" qui doit envoyer à chaque fois une preuve.

Par exemple, si je dis que j'ai un algorithme de factorisation capable de factoriser le produit de deux nombres premiers de 100 chiffres en moins d'une seconde, c'est assez facile à vérifier. Vous m'envoyez par exemple

102060915909124202848345556015335528256145778885989048697479580691505561772139279388440678440403388772992468052128919574714434398645027062989067429802870690087639059498978907074730930731336576614050997341416501459436070571985733865245515767605378903319609957456625221256463847171670614791587066757623004106591

et si je vous renvoie

a=10306966840478983714718101511898742882242606574974431928793967416315999626689934146738670704006734002443608489916065875070851311504009032250181012747170489

et

b=9902129063644221861668778823952636626210676620744802042696556071156788063678707127166878617189064221726923619008361963862830224922376150169694626256725719

en moins d'une seconde, vous pouvez vérifier ensuite que a*b = le nombre que vous m'avez donné (et que a et b sont premiers…), donc que j'ai bien un algo capable de casser RSA[[2]](#tjTZk)

Mais vous le voyez bien, il n'y a pas de manière de faire ça pour une démonstration mathématique de l'inexistence de quelque chose, encore moins en une seule étape dans une petite marge.

En fait le fameux "j'en ai découvert une démonstration véritablement merveilleuse que cette marge est trop étroite pour contenir" parle certainement d'une des nombreuses démonstrations faites entre 1670 et 1994, mais qui étaient incorrectes.

[https://fr.wikipedia.org/wiki/De...](w:Dernier_théorème_de_Fermat)

Notes de bas de page

[[1]](#cite-tENZQ)[20 ans de Science Simpson - Pourquoi Comment Combien](https://www.drgoulu.com/2010/03/08/20-ans-de-science-simpson/#.ZAGzTnbMKCo)

[[2]](#cite-tjTZk)[Alice et Bob et les clés asymétriques - Pourquoi Comment Combien](https://www.drgoulu.com/2017/02/15/alice-et-bob-et-les-cles-asymetriques/#.ZAG7r3ZsOCo)
