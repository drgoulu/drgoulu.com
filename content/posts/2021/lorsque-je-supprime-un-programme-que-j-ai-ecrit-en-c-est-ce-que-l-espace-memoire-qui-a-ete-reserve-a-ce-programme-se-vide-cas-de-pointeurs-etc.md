---
title: Lorsque je supprime un programme que j'ai écrit en C est ce que l'espace mémoire qui a été réservé à ce programme se vide ? (cas de pointeurs etc ..)
slug: lorsque-je-supprime-un-programme-que-j-ai-ecrit-en-c-est-ce-que-l-espace-memoire-qui-a-ete-reserve-a-ce-programme-se-vide-cas-de-pointeurs-etc
date: '2021-12-18'
draft: false
categories:
- Quora
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Lorsque-je-supprime-un-programme-que-jai-%C3%A9crit-en-C-est-ce-que-lespace-m%C3%A9moire-qui-a-%C3%A9t%C3%A9-r%C3%A9serv%C3%A9-%C3%A0-ce-programme-se-vide-cas-de-pointeurs-etc/answer/Dr-Goulu)*

Oui avec des système d'exploitation récents.

Quand votre programme est lancé par le système d'exploitation, l'OS lui alloue un "process heap", un bloc de mémoire dans lequel votre programme va faire ses propres allocations dynamiques. Quand ce heap est plein, l'OS en fournit un autre etc mais en gardant une liste des blocs alloués. A la fin normale ou anormale de votre programme, l'OS considères ces blocs comme libres et peut les réallouer.

Vous pouvez voir ça comme une hiérarchie d'allocateurs : l'OS en a un qui alloue de la mémoire à d'autres allocateurs, chacun ayant sa propre gestion en fonction du langage par exemple. Et vous pourriez même écrire votre propre [Allocateur](w:Allocateur_(C++))gérant une partie de la mémoire pour des besoins spécifiques.

Au niveau de l'OS, l'utilisation d'un [Gestionnaire de mémoire virtuelle](w:)permet d'isoler la mémoire allouée aux différents processus pour qu'ils n'aillent pas se perturber mutuellement, donc normalement vous ne pouvez pas lire, et encore moins écrire dans une adresse mémoire qui n'a pas été allouée à votre programme.

[https://stackoverflow.com/questi...](https://web.archive.org/web/20230106004828/https://stackoverflow.com/questions/2213627/when-you-exit-a-c-application-is-the-malloc-ed-memory-automatically-freed)
