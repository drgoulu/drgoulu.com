---
title: Pourquoi les objets intégrés mutables ne peuvent-ils pas être transformés en Python ? Quel est l'avantage de cela ?
slug: pourquoi-les-objets-integres-mutables-ne-peuvent-ils-pas-etre-transformes-en-python-quel-est-l-avantage-de-cela
date: '2019-05-06'
draft: false
categories:
- Pourquoi
tags:
- programmation
- langage
- python
- python-langage-de-programmation
- objet
coverImage: ./images/quora.png
---

*Article initialement publié sur [Quora](https://fr.quora.com/Pourquoi-les-objets-int%C3%A9gr%C3%A9s-mutables-ne-peuvent-ils-pas-%C3%AAtre-transform%C3%A9s-en-Python-Quel-est-lavantage-de-cela/answer/Dr-Goulu)*

qu’appelez-vous “transformés” ? Vous voulez dire modifiés comme

```
a=(1,'truc',true) # tuple
a[1]='machin' # erreur

```

? Alors vous voulez plutôt dire [immuable](w:Objet_immuable) (immutable en anglais).

Un objet immutable permet de garantir la cohérence des données qu’il contient en obligeant à les manipuler comme un tout. Ca peut être utile en programmation multi-thread par exemple : chaque thread est sure que l’objet partagé n’est pas en train d’être modifié par une autre thread.

Un autre avantage est que le hash d’un objet immuable est constant, ce qui permet la recherche très rapide d’un tel objet dans un set ou un dict. C’est pourquoi les clés de dict doivent être de type immuable
