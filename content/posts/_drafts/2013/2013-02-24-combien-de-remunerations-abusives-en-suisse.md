---
title: Combien de rémunérations "abusives" en Suisse
slug: combien-de-remunerations-abusives-en-suisse
date: '2013-02-24'
categories:
- cat3
tags:
- economie
- inegalites
- politique
- suisse
draft: true
coverImage: "3b859275c96f23b5c494c801b065e63e.png"
---
Le 3 mars, les suisses voteront sur l'[initiative populaire](view-source:/2009/12/13/initiatives-populaires/) lancée par M. Minder "[contre les rémunérations abusives](http://www.remunerationsabusives.ch/)". C'est l'occasion de poursuivre la [série d'articles sur les inégalités](/tags/inegalites/) en examinant particulièrement le cas suisse. Rappel des épisodes précédents:

1. La mesure scientifique des inégalités la plus utilisée au niveau international est le [coefficient de Gini](http://fr.wikipedia.org/wiki/Coefficient_de_Gini) qui [tient compte de toute la distribution des revenus](/2009/10/11/calculateur-dinegalite/), et non seulement des [cas extrêmes](http://pauleetmick.blog.tdg.ch/index-1.html) ou des [déciles](http://fr.wikipedia.org/wiki/In%C3%A9galit%C3%A9s_de_revenu_en_France#Distribution_en_d.C3.A9ciles) ou quintiles souvent cités dans les media.
2. Les variations du coefficient de Gini montrent que [les inégalités n'augmentent pas partout ni en même temps](/2009/03/21/combien-dinegalite/) . En particulier, selon les dernières mesures de l'OCDE [[1]](#ref-1), les inégalités n'ont pas augmenté en 20 ans en France, Suisse, Belgique et Hongrie. Elles ont diminué en Turquie et Grèce (jusque vers 2009...), et ont effectivement augmenté dans les autres pays de l'OCDE.
3. Les [inégalités globales diminuent](http://www.gapminder.org/videos/gapmindervideos/gapcast-4-globalization/).
4. Et, surprise, [la Suisse est plus égalitaire que la France](/2012/07/13/encore-plus-dinegalite/), surtout au niveau des revenus avant impôts.
    
    > "Les pays nordiques et la Suisse se caractérisent par une inégalité des revenus disponibles inférieure à la moyenne grâce à une faible disparité des salaires, en particulier au sommet de l’échelle..." ([[1]](#ref-1), page 9)
    

Voyons maintenant si l'initiative Minder adresse un problème réel. L'[Office Fédéral de la Statistique](http://www.bfs.admin.ch/) m'a aimablement et rapidement\* fourni les 6 [courbes de Lorenz](http://fr.wikipedia.org/wiki/Courbe_de_Lorenz) des 10 dernières années [[2]](#ref-2), mais hélas pas les données correspondantes, trop volumineuses. Effectivement, les revenus de tous les ménages suisses pourraient mettre à genoux mon propre [calculateur d'inégalités](https://www.box.com/shared/njhn3h3out), mais ici je m'intéresse essentiellement aux variations de la courbe de Lorenz, dont j'ai extrait les valeurs numériques des graphiques avec [un peu de Python](http://stackoverflow.com/questions/14154233/image-analysis-curve-fitting)\*\*.

{{< figure src="images/3b859275c96f23b5c494c801b065e63e.png" alt="Une courbe de Lorenz suisse (en bleu) : l'axe Y donne la proportion du revenu touché par la fraction de la population (axe X) correspondante. La droite noire correspond à une société parfaitement égalitaire." caption="Une courbe de Lorenz suisse (en bleu) : l'axe Y donne la proportion du revenu touché par la fraction de la population (axe X) correspondante. La droite noire correspond à une société parfaitement égalitaire." link="/wp-content/uploads/HLIC/3b859275c96f23b5c494c801b065e63e.png" align="aligncenter" width="619" >}}

### Notes:

\* J'ai envoyé ma demande à l'OFS le 19 décembre 2012 persuadé que je n'aurai de réponse qu'en 2013. Ils m'ont envoyé les documents 2 jours plus tard. Cette année je paie mes impôts plus volontiers en pensant qu'une partie finance l'OFS ! Bravo !

\*\* le code a été développé par [Thorsten Kranz](http://stackoverflow.com/users/1156006/thorsten-kranz) en une heure chrono à partir de [ma question sur StackOverflow](http://stackoverflow.com/questions/14154233/image-analysis-curve-fitting) ! Comme quoi le bénévolat sur internet est encore plus rapide que les meilleurs fonctionnaires.

### Références

1. <span id="ref-1"></span>OCDE 2012, « [Inégalités de revenus et croissance : le rôle des impôts et des transferts](http://www.oecd.org/dataoecd/28/27/49446673.pdf) », OCDE Département des Affaires Économiques, Note de politique économique, no 9, janvier 2012.
2. <span id="ref-2"></span>Office Fédéral de la Statistique , "Lorenzkurve und Gini Koeffizient, Privater Sektor und Bund" 2000,2002,2004,2006,2008,2010 [Fichier zip](/wp-content/uploads/2013/01/Lorentz.zip)
