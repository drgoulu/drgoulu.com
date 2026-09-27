---
title: Bonjour, comment écrire une requête SQL me permettant de trouver le top 3 des communes de plusieurs départements du prix moyen des biens immobiliers ?
slug: bonjour-comment-ecrire-une-requete-sql-me-permettant-de-trouver-le-top-3-des-communes-de-plusieurs-departements-du-prix-moyen-des-biens-immobiliers
date: '2022-07-14'
draft: true
categories:
- Comment
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Bonjour-comment-%C3%A9crire-une-requ%C3%AAte-SQL-me-permettant-de-trouver-le-top-3-des-communes-de-plusieurs-d%C3%A9partements-du-prix-moyen-des-biens-immobiliers/answer/Dr-Goulu)*

```
Select *
From communes
Where département in ["Ain", "Haute-Savoie" ]
Order by prixmoyendesbiensimmobiliers
Limit 3

```
