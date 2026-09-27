---
title: Comment apprendre SQL pour le métier de test logiciel ?
slug: comment-apprendre-sql-pour-le-metier-de-test-logiciel
date: '2025-08-06'
draft: false
categories:
- Comment
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Comment-apprendre-SQL-pour-le-m%C3%A9tier-de-test-logiciel/answer/Dr-Goulu)*

Je ne vois pas vraiment le rapport avec le test logiciel, mais je dirais que tout développeur devrait être capable de faire au moins une requête SELECT simple dans une base de données SQL.

Ah si, je vois pour le test : il faut que vous soyez aussi capable de faire une requête

```
DELETE FROM Clients.

```

Si elle marche et que votre boîte fait faillite, c'est que vous avez trouvé un bug au niveau des permissions de la base ;-)

Donc commencez par apprendre à faire un backup de la base. Puis à utiliser ROLLBACK plutôt que COMMIT. Puis à faire des requêtes qui défont ce que font vos requêtes de test.

C'est difficile et DANGEREUX de faire des tests sur une base de production. Faites les sur une copie.
