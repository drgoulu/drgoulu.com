---
title: TRIZ
slug: triz
date: '2014-07-21'
draft: true
---
### Introduction

- but: démocratiser TRIZ
- approche: appliquer TRIZ à l'innovation dans 2 petits exemples pratiques:
    - la cuillère à thé
    - une prise multiple
- TRIZ permet de systématiser le processus de créativité, en minimisant le risque d'échec
- la démarche TRIZ s'oppose au brainstorming
- TRIZ = Théorie de Résolution des Problèmes Inventifs (acronyme russe) de [Altshuller](w:en:G._S._Altshuller) est basée sur 2 axiomes:
    1. il existe des lois d'évolution des systèmes, qui sont invariantes dans le temps
    2. tout problème peut s'exprimer sous la forme d'une contradiction, au sens dialectique (pas de contradiction = pas de problème)

la démarche TRIZ est constituées d'étapes séquentielles (qui vont plus loin que la fameuse table qui fait l'essentiel de l'[article Wikipédia](w:TRIZ)

Il existe des logiciels comme [STEPS](https://web.archive.org/web/20140104064836/http://www.time-to-innovate.com/content/steps) pour formaliser la démarche et effectuer certaines opérations automatiquement

### 1 Analyse de la Situation Initiale

- but : objectif clairement défini, sous une forme mathématiquement exploitable
- outil : "Problem graph" dans lequel on définit tous les problèmes rencontrés historiquement (yc par les concurrents) et leurs "solutions partielles", qui débouchent sur d'autres problèmes etc.
- le "problème clé" est celui qui se trouve à la racine de la plus longue chaîne du graphe
    - parfois le problème n'est pas celui qu'on croit initialement
- important : passer beaucoup de temps (~50% du projet) à générer ce graphe en interviewant tout le monde : clients, ingénieurs, IP, production etc.
- note : on peut utiliser TRIZ "à l'envers" pour générer les problèmes plutôt que les solutions, par exemple dans une étude [AMDEC](w:Analyse_des_modes_de_défaillance,_de_leurs_effets_et_de_leur_criticité)

### 2 Fonction Principale Utile

- but : bien comprendre le problème clé en définissant la "fonction principale utile" (FPU) ou "most useful function" (MUF) du produit
- formalisme : (TODO : dessin)
    - le "système" offre la FPU au "client"
    - le système comprend toujours 4 éléments : un "moteur" qui reçoit de l'énergie, un "travail" qui est en contact avec le client, une "transmission" entre les deux et un "contrôle" qui régule

pas évident:

- la FPU d'un stylo n'est pas d'écrire, mais de déposer de l'encre sur du papier : client = papier
- la FPU d'une cuillère est de brasser un liquide : client = liquide. moteur=poignée de la cuillère, travail = pelle de la cuillère, transmission = manche de la cuillère

rester très basique ! On a plutôt tendance à penser au "supersystème" qui inclut la cuillère et son environnement tasse+sucre+humain+...

### 3 Multi-écrans

(esquissé [sur wikipédia](w:TRIZ#9_.C3.A9crans))

représenter le présent, le passé et l'avenir (pour définir des hypothèses d'évolution) du système, des sous-systèmes et du supersystème. Remplir le tableau dans l'ordre des chiffres:

|  | Passé | Présent | Futur |
| --- | --- | --- | --- |
| supersystème | 6 | 3 | 7 |
| système | 4 | 1 | 8 |
| sous-systèmes | 5 | 2 | 9 |

Pour la colonne "passé" remonter d'un deltaT correspondant à la dernière évolution notable du produit, pour le futur tenter d'extrapoler du même deltaT

Dans chaque case indiquer :

- les "doléances" : ce qui ne va pas
- le positif: les solutions aux doléances de la colonne précédente qui ne doivent pas être dégradées dans le futur

Dans la colonne "futur", on a en principe positivé toutes les doléances du présent

note : pour TRIZ l'innovation "de rupture" est une innovation au niveau du super(super...)système

### 4 Lois d'évolution

- l'évolution de tous les produits suit une courbe "logistique" en S. Lorsqu'elle plafonne, un nouveau produit démarre en suivant lui aussi un S. Exemple : Walkman -> iPod -> ?
- important : positionner son produit sur cette courbe car il n'est parfois pas où on croit qu'il est. Il existe des outils mathématiques pour ce faire, utilisant le "niveau d'inventivité", le nombre de brevets déposés et la marge.
- 9 lois "scientifiquement établies" par Altshuller [voir wikipédia](w:en:Laws_of_Technical_Systems_Evolution) permettent de positionner ma direction d'innovation et celles de mes concurrents (très utilisé dans la bataille Samsung/Apple selon Ondo)

### 5 Les contradictions

- sont de deux types:
    - techniques : lorsqu'on améliore un paramètre, un autre se dégrade. 70% de ces contradictions ont déjà trouvé une solution dans le passé : exploiter cette connaissance ! Seuls 30% se ramènent à des contradiction physiques
    - physiques : pas de compromis possible
- outil : formalisation dialectique : SI (le paramètre) EST (plus grand/petit etc.) QUE (une valeur numérique) ALORS (liste d'avantages ET d'inconvénients) SINON (liste d'avantages ET d'inconvénients)
- [exemple en ligne](https://web.archive.org/web/20140116071947/http://www.time-to-innovate.com/steps_matrix)

### 6 La Matrice

Outil le plus connu de TRIZ[\[1\]](https://fr.wikipedia.org/wiki/TRIZ#Matrice_des_contradictions_techniques), donne des pistes pour résoudre les contradictions techniques, basées sur l'analyse de milliers de brevets.

Expérience faite (cuillère + multiprise), donne des solutions apparues spontanément en discussion/brainstorming, mais permet d'être plus sur de ne pas avoir oublié une possibilité.

### Conclusions personnelles

- démarche assez attrayante pour le scientifique/ingénieur
- un peu "russe" ou "asiatique" à première vue : comment (copier) faire du neuf en utilisant les recettes du passé
- parait facilement applicable à des cas simples. Je propose de l'utiliser ponctuellement dans SIMPSON plutôt que le brainstorming (qui n'est souvent pas fait de façon rigoureuse...)
- application à plus large échelle demande formation et coaching externe pour commencer. Le rôle du coach est essentiellement de challenger aux premières étapes.
- Exelop/Ondo insistent (évidemment) sur l'application à large échelle de Triz chez Samsung, Nestlé comme véritable système de management de l'innovation à grande échelle
- Un aspect qui me parait particulièrement intéressant est le fort aspect IP : TRIZ est basé sur l'analyse sémantique de très nombreux brevets. Effort toujours en cours, la recherche actuelle permet de cartographier des domaines couverts par des brevets, et TRIZ d'identifier des failles, des contournements possibles etc. je préconise un contact IP/Exelop pour en savoir plus à ce sujet.
