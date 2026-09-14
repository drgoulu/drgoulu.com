---
title: Salaires extrêmes, médians et moyens
slug: salaires-extremes-medians-et-moyens
date: '2014-07-10'
categories:
  - "Combien"
tags:
- inegalites
- statistiques
- suisse
coverImage: "./images/UBS_Burr.png"
draft: true
---
[Selon Travail Suisse](http://www.travailsuisse.ch/themes/travail/salaires_des_managers), l'écart salarial s'est creusé l'an dernier en Suisse. Dans des entreprises comme UBS, Novartis ou Nestlé, le CEO touche plus de 200 fois plus que le plus modeste de ses salariés, et ce rapport a encore augmenté dans nombre d'entreprises l'an passé. L'organisation syndicale considère que cette "dégradation inquiétante" montre que "le décalage entre la population et l’économie se poursuit" et "sollicite le politique". Le problème, c'est que pour le politique sage comme pour le statisticien, il ne faut pas tirer de conclusions générales de cas extrêmes, or le rapport salaire max/salaire min est la pire mesure d'inégalité possible, car elle ne dit absolument rien de la distribution des 99% et plus des salaires compris entre ces extrêmes. De plus cette mesure dépend de la taille de l'entreprise : les écarts de salaire entre les habitants de votre rue sont à coup sur plus faibles que ceux entre les habitants de votre ville. Il paraît "normal" que le salaire du CEO d'une entreprise mondiale employant plus de 100'000 personnes gagne plus que le patron de votre garage.

Il existe une mesure des inégalités qui ne souffre pas de ces inconvénients : l'[indice de Gini](https://fr.wikipedia.org/wiki/indice de_Gini) dont j'ai [déjà causé](/tags/Gini/) plusieurs fois.Cette mesure est abondamment utilisée au niveau international, notamment pour les comparaisons entre pays. Par exemple dans à la page "[Niveau de vie, situation sociale et pauvreté – Données, indicateurs](http://www.bfs.admin.ch/bfs/portal/fr/index/themen/20/03/blank/key/02/06.html)" de l'Office Fédéral de la Statistique on peut lire:

> Selon les résultats de 2012, la Suisse, avec 28,7, se trouve dans la moyenne européenne en ce qui concerne l'inégalité de distribution des revenus. L’indice de Gini varie chez nos voisins, entre 28,3 (Allemagne), 30,5 (France) et 31,9 (Italie). Il est en moyenne de 30,6 pour l’ensemble de l’Union Européenne.

Hélas, l'indice de Gini n'est pas utilisé par les entreprises, qui y auraient pourtant tout intérêt pour relativiser les salaires exhorbitants de leurs top managers.Pourtant depuis 2009 je mets à disposition une [feuille de calcul](/2009/10/11/calculateur-dinegalite/) Excel de l'indice de Gini très simple à utiliser : il suffit de coller tous les salaires de l'entreprise dans un colonne, de la trier par ordre croissant et voilà : le coefficient de Gini de l'entreprise apparaît. A ma connaissance une seule entreprise l'a utilisée : mon employeur actuel. Mais il hésite à rendre la valeur publique\*, faute de valeurs de référence dans d'autres entreprises.

Je me suis donc demandé comment obtenir une valeur approximative de l'indice de Gini sans connaître tous les salaires versés par une entreprise, mais seulement les données publiquement disponibles, dans les rapports d'activité des entreprises elles-mêmes. En effet, on y trouve systématiquement:

- le nombre N d'employés
- le montant S total versé en "compensations", donc en salaires bruts
- S/N donne le salaire moyen de l'entreprise
- le salaire le plus élevé B est également indiqué, c'est une obligation légale en Suisse du moins
- quant au salaire le plus bas A, il figure rarement dans un rapport d'activité mais on peut l'obtenir également assez facilement car il est souvent fixé dans les conventions collectives. Les [données de Travail Suisse](http://www.travailsuisse.ch/system/uploadedfile4s/3037/original/2014_06_23_Managerloehne_Beilagen_f.pdf?1403509913) fournissent ce chiffre pour les plus grandes entreprises suisses.

Mais comment obtenir une distribution statistique réaliste de salaires à partir de ça. J'ai posé [la question sur StackExchange](http://math.stackexchange.com/questions/851112/income-distribution-from-n-min-max-and-mediansalary-and-total-compensation/) et à [Arthur Charpentier](http://freakonometrics.hypotheses.org/). Ce dernier m'a suggéré de fitter une  [GB2](w:en:Generalized_beta_distribution#Generalized_beta_of_the_second_kind_.28GB2.29)

Selon les [données de Travail Suisse](http://www.travailsuisse.ch/system/uploadedfile4s/3037/original/2014_06_23_Managerloehne_Beilagen_f.pdf?1403509913), les salaires à l'UBS par exemple s'échelonnent entre CHF 50'000 et CHF 11'430'000. Selon la page 332 du [Rapport d'Activité 2013 de l'UBS](http://www.ubs.com/global/en/about_ubs/investor_relations/annualreporting/2013/_jcr_content/par/teaserbox_6c86/teaser_acb3/linklist/link_9f50.1705024293.file/bGluay9wYXRoPS9jb250ZW50L2RhbS9zdGF0aWMvZ2xvYmFsL2ludmVzdG9yX3JlbGF0aW9ucy9hbm51YWwyMDEzL0FSMjAxMy1lbi5wZGY=/AR2013-en.pdf), l'UBS a payé au total 15.182 milliards de francs à 60205 employés, soit CHF 252'171 par employé en moyenne.

{{< figure src="./images/UBS_Burr.png" alt="Loi de Burr fittée sur les salaires de l'UBS" caption="Loi de Burr fittée sur les salaires de l'UBS" link="./images/UBS_Burr.png" align="aligncenter" width="380" >}}

Même en tenant compte d'environ 15% de charges sociales payées par l'employeur en Suisse, cette moyenne est proche du double du salaire médian des employés des grandes banques suisses, qui est de CHF 110'000 en tenant compte des bonus, selon [ce document de l'ASEB](http://www.aseb.ch/fileadmin/user_upload/Themen/Loehne/Lohnumfrage/ASEB_Enquete-2013-sur-les-salaires-des-employes-de-banque.pdf) (p. 12)

Une chose est sure : les distribution statistiques des salaires possèdent une [asymétrie positive](w:Asymétrie_(statistiques)) bien connue

 

 

Note \* : je ne la connais pas

### Références

1. <span id="ref-1"></span>Dalgaard, C.-J., Hansen, H., & Larsen, T. "[Income Skewness, Redistribution and Growth: A Reconciliation](http://www.econ.ku.dk/epru/files/wp/wp-03-14.pdf)", 2003, EPRU Working Paper Series.
2. <span id="ref-2"></span>http://www.ge.ch/statistique/tel/publications/2012/analyses/communications/an-cs-2012-43.pdf
