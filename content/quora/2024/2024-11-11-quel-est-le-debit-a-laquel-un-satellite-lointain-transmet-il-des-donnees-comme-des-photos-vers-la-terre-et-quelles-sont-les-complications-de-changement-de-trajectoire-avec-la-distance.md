---
title: Quel est le débit a laquel un satellite lointain transmet-il des données comme des photos vers la terre et quelles sont les complications de changement de trajectoire avec la distance a cause des délais ?
slug: quel-est-le-debit-a-laquel-un-satellite-lointain-transmet-il-des-donnees-comme-des-photos-vers-la-terre-et-quelles-sont-les-complications-de-changement-de-trajectoire-avec-la-distance
date: '2024-11-11'
draft: false
categories:
- Quora
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Quel-est-le-d%C3%A9bit-a-laquel-un-satellite-lointain-transmet-il-des-donn%C3%A9es-comme-des-photos-vers-la-terre-et-quelles-sont-les-complications-de-changement-de-trajectoire-avec-la-distance-a/answer/Dr-Goulu)*

Ça fait plein de questions dont vous trouverez les réponses détaillées en googlant. Vous trouverez par exemple :

[https://next.ink/946/comment-son...](https://next.ink/946/comment-sondes-voyager-communiquent-avec-terre-a-20-milliards-km/#:~:text=Lancée en 1977 (août et,ont pris des directions différentes).

Les sondes lointaines transmettent quelques kbits par seconde avec des antennes très directionnelles braquées en permanence vers la Terre.

Sur Terre, le [Deep Space Network](w:)combine la sensibilité en réception et la puissance en émission nécessaire pour transmettre des informations à la sonde même si elle se désaligne un peu.

Les protocoles de transmission sont très redondants, avec plein de codes de correction d'erreur pour ne pas devoir attendre d'accusé de réception ACK / NOACK pendant des heures.

Le délai de transmission pose surtout des problèmes pour la télécommande de rovers sur Mars, c'est pour ça qu'ils avancent très lentement. Pour les sondes on utilise des commandes basées sur le "prédicteur de Smith", une astuce d'automaticien.
