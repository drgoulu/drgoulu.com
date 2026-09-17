---
title: 2 programmes d’IA sont ils capables de débattre l’un avec l’autre où sont ils juste capable de répondre à des questions en fouillant des bases d’informations ?
slug: 2-programmes-dia-sont-ils-capables-de-debattre-lun-avec-lautre-ou-sont-ils-juste-capable-de-repondre-a-des-questions-en-fouillant-des-bases-dinformations
date: '2023-07-12'
draft: false
categories:
- Quora
tags:
- informatique
- les-questions-et-les-reponses
- debat
- intelligence-artificielle
- recuperation-d-informations
- recherche-sur-internet
- science-de-l-informatique
- repondre-a-des-questions
- l-intelligence-artificielle
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/2-programmes-d-IA-sont-ils-capables-de-d%C3%A9battre-l-un-avec-l-autre-o%C3%B9-sont-ils-juste-capable-de-r%C3%A9pondre-%C3%A0-des-questions-en-fouillant-des-bases-d-informations/answer/Dr-Goulu)*

C'est exactement comme ça qu' [AlphaGo](w:)est devenu champion du monde de go : en jouant contre des millions de parties contre une autre instance de lui-même.

[https://www.deepmind.com/blog/al...](https://www.deepmind.com/blog/alphago-zero-starting-from-scratch)

Dans l'article ci-dessus, on présente une nouvelle version [AlphaGo Zero](w:) qui commence de zéro : elle ne connait que les règles du jeu et un petit programme auxiliaire fait l'arbitre qui détecte la fin de la partie et qui a gagné.

- en trois jours il atteint le même niveau que le programme qui a battu Lee Sedol en 2012
- en 21 jours il a atteint le niveau de la version "Master" qui a battu tous les meilleurs 60 joueurs professionnels en 2017 (et qui avaient étudié les parties de 2012…)
- en 40 jours il a atteint un niveau "stable" encore plus élevé, qu'aucun humain ne pourra atteindre, la vie étant beaucoup trop courte (voir [L'espace infini entre les mots](https://www.drgoulu.com/2014/05/18/lespace-infini-entre-les-mots/))

[AlphaZero](w:)est un programme identique, mais non spécifique au go. On peut simplement lui programmer les règles d'un jeu, et il apprend tout seul à jouer, contre lui même.

> Selon DeepMind, **AlphaZero a atteint en 24 heures un niveau de jeu supérieur aux humains au jeu d'échecs, au shogi et au go** en battant les programmes champions du monde [Stockfish](w:Stockfish_(programme_d'échecs)) (échecs), [Elmo](https://fr.wikipedia.org/w/index.php?title=Elmo_(programme_de_shogi)&action=edit&redlink=1) (shogi) et la version d’AlphaGo Zero ayant eu trois jours d'apprentissage.
>
>
>
> Stockfish, le logiciel champion du monde d'échecs est battu après 4 heures d'apprentissage et 44 millions de parties jouées.
>
>
>
> Le [programme de shogi](w:Shogi_en_informatique) Elmo est terrassé après deux heures de pratique et 24 millions de parties

Plus fort encore [MuZero](w:)**apprend à jouer à n'importe quel jeu sans même en connaître les règles !** il démarre sans aucune connaissance des règles, en ayant simplement l'information selon laquelle un mouvement qu'il tente est ou non permis, et quelles en sont les conséquences.

L'humain n'est donc nécessaire que comme "arbitre", pour dire laquelle des instances d'IA a "gagné".

Vous vous rappelez de tous ces sites (de Google…) où vous deviez prouver que vous étiez humain en identifiant des images contenant un mouton, un passage piéton ou un bus ? Ca servait à ça : entraîner des IA à reconnaître des choses dans des images ! ( [les Ordinateurs Humains : des Captchas à PeekaSearch - Pourquoi Comment Combien](https://www.drgoulu.com/2008/03/07/les-ordinateurs-humains-des-captchas-a-peekasearch/) ) Par exemple pour les voitures autonomes …

Votre idée de "2 programmes d’IA capables de débattre l’un avec l’autre" ne pose aucun problème technique. Elles pourraient faire des millions de débats par jour. Le problème est de définir les règles de ce qui est permis dans un débat, et qui a "gagné" à la fin pour renforcer l'apprentissage.

C'est cette connaissance humaine qui rend les IA "intelligentes", mais aussi biaisée au point d'être potentiellement dangereuse : le contenu de la base de donnée de ce qui est "juste" ou "bien" est crucial pour les résultats futurs. Remarquez que c'est la même chose pour les cerveaux humains, on s'en aperçoit chaque fois qu'on juge un criminel en série …

Si on imagine que les fils de discussion sur Quora puissent être un jour utilisés pour définir les règles d'un bon débat, on peut se faire du souci …

Pour l'instant les essais de ChatGPT causant avec lui-même ne sont pas très concluants

[https://www.techradar.com/featur...](https://www.techradar.com/features/i-made-chatgpt-talk-to-itself-and-the-results-werent-what-i-expected)
