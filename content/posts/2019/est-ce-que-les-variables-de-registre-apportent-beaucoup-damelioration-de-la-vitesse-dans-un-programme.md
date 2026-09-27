---
title: Est-ce que les variables de registre apportent beaucoup d’amélioration de la vitesse dans un programme ?
slug: est-ce-que-les-variables-de-registre-apportent-beaucoup-damelioration-de-la-vitesse-dans-un-programme
date: '2019-07-04'
draft: false
categories:
- Quora
tags:
- informatique
- vitesse
- architecture
- ordinateurs
- processeurs
coverImage: ./images/quora.png
---

*Article initialement publié sur [Quora](https://fr.quora.com/Est-ce-que-les-variables-de-registre-apportent-beaucoup-d-am%C3%A9lioration-de-la-vitesse-dans-un-programme/answer/Dr-Goulu)*

Oui, mais ne vous en occupez pas, le compilateur fait ça beaucoup mieux que vous.

Selon [Architecture des processeurs - Reactive, Java, Android, POO](http://www.prados.fr/architecture/architecture-des-processeurs):

> En architecture 64 bits, le nombre de registres est suffisamment important pour que pratiquement tous les paramètres et toutes les variables locales utilisent un registre dédié. Le protocole d’appel entre les méthodes s’appuie également fortement sur les registres. L'appelant alimente des registres avant l'appel. La pile est utilisée pour sauver l'état des registres avant l'appel et pour les paramètres complémentaires n'ayant pas trouvés de place dans un registre.

Ensuite il donnent un tableau des temps d'accès en fonction de la [Hiérarchie de mémoire](w:):

- registres : 1 cycle processeur (~1 nanoseconde)
- cache L1 : 1 microseconde (1000x plus lent…)
- cache L2 : 4 microsecondes
- cache L3 : 10 à 20 microsecondes
- RAM : > 200 microsecondes (~200'000x plus lent que le registre…)
