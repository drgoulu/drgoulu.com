---
title: "Calculateur d&#039;(in)égalité"
slug: "calculateur-dinegalite"
date: 2009-10-11
categories:
  - "Combien"
tags: 
  - "economie"
  - "gini"
  - "inegalites"
  - "maths"
  - "programmation"
  - "societe"
  - "suisse"
coverImage: "ceff2742634f4ddd3d5251efaaf85934.png"
---

Les inégalités de revenu sont un sujet d'actualité politique brûlant. En Suisse, les [Jeunesses Socialistes](http://juso.ch/) viennent de lancer une initiative populaire visant à limiter le salaire maximal dans les entreprises à 12 fois le salaire minimal.Dans une petite boite c'est presque toujours le cas, mais plus on travaille dans une grande entreprise, plus on aimerait gagner en une année ce que gagne notre CEO en un mois...

C'est le problème du rapport max/min : il ne tient pas compte de tous les revenus intermédiaires. Dans une entreprise de 100 personnes, 98% des salaires sont compris entre celui du patron et celui de la technicienne de surface. Comment mesurer les inégalités de revenu en tenant compte de tous les revenus d'une société ?

La mesure d'(in)égalité des revenus la plus utilisée au niveau international s'appelle "coefficient (ou indice) de Gini". J'en ai déjà parlé dans [plusieurs articles](/tags/gini/). L'indice de Gini vaut 0 si les revenus d'une société sont divisées de façon parfaitement égale, et 1 (ou 100%) si un seul esclavagiste empoche la totalité du revenu. En pratique, l'indice de Gini de la plupart des pays membre de l'OCDE se situe entre 0.5 et 0.4, mais les impôts réduisent les inégalités pour obtenir un Gini du revenu disponible entre 0.25 et 0.35 .

Le coefficient de Gini pourrait facilement être utilisé au niveau des entreprises. J'ai d'ailleurs créé une [feuille de calcul](http://www.box.net/shared/njhn3h3out) permettant de le calculer en ligne pour des entreprises de moins de 100 personnes\*. C'est tout simple : copiez/coller les montants des salaires de votre entreprise dans la première colonne, triez-la dans l'ordre croissant, et voilà !

Le petit graphique associé (dont il faut changer l'échelle horizontale à la main au besoin) trace en bleu la [courbe de Lorenz](w:) qui montre la progressivité des revenus. L'indice de Gini est défini par la fraction de la surface entre la courbe bleue et la droite rouge par la surface sous la droite rouge.

En jouant avec cet outil, vous constaterez que l'initiative "1:12" des jeunesses socialistes n'implique pas du tout une distribution équitable des revenus. Comme le montrent les cas extrêmes ci-dessous, le coefficient de Gini peut varier énormément même si le salaire le plus élevé vaut 12x le salaire minimal:

{{< figure src="images/f2cec9deffecb61c69a24e0fa13bb3b7.png" alt="Lorenz 1-12-1" caption="société de 10 personnes ou les 9 employés ont un salaire égal et le patron un revenu 12 fois supérieur. Indice de Gini = 0.52" link="/wp-content/uploads/HLIC/f2cec9deffecb61c69a24e0fa13bb3b7.png" align="aligncenter" width="454" >}}

{{< figure src="images/c69c69aa7491ec6b0c8d49f93197af76.png" alt="Lorenz 1-12-2" caption="société de 10 personnes ou 9 cadres ont un salaire égal, et un employé un salaire 12x moins élevé. Indice de Gini = 0.1" link="/wp-content/uploads/HLIC/c69c69aa7491ec6b0c8d49f93197af76.png" align="aligncenter" width="455" >}}

Pour des revenus réellement équitables, il faudrait que le coefficient de Gini des entreprises corresponde, ou soit même inférieur à celui du pays considéré. Ceci laisse encore une grande flexibilité à la politique salariale. Voici par exemple quelques distributions de revenus donnant un indice de Gini = 0.33, le même que celui de la Suisse entière (avant impôts):

- 10% du personnel touche un salaire 6x supérieur aux 90%
- 50% du personnel touche un salaire 4x supérieur aux autres 50%
- [distribution uniforme](w:Loi_uniforme_continue)des salaires : 10% touchent un salaire de base, 10% touchent 2x plus, 10% touchent 3x plus etc jusqu'aux 10% qui touchent 10x le salaire de base:
    
    {{< figure src="images/4a57146795bddaf647e74921f592a4c3.png" alt="Lorenz 1-12-3" caption="distribution uniforme des revenus : Gini = 0.33" link="/wp-content/uploads/HLIC/4a57146795bddaf647e74921f592a4c3.png" align="aligncenter" width="457" >}}

On voit au passage que la courbe de Lorenz permettent d' illustrer de manière fine la politique salariale des entreprises. En particulier, les différences de statut entre employés provoquent des "cassures" dans la courbe, alors que des revenus abusifs dans le haut de l'échelle sont détectables par la pente de la courbe à droite.

Il serait très intéressant de connaitre le coefficient de Gini des entreprises. je n'en ai trouvé aucun sur internet, pourtant je suis persuadé que les grandes entreprises (et les grands patrons) pourraient défendre leur politique de rémunération en publiant ce chiffre, qui est beaucoup plus parlant que le rapport max/min ou le montant total de la rémunération de la direction.

Si vous connaissez celui de votre entreprise ou si vous le calculez à l'aide de ma [feuille de calcul](http://www.box.net/shared/njhn3h3out), je vous serais très reconnaissant de le communiquer à l'aide des commentaires ci-dessous. Pas besoin de nommer l'entreprise, le secteur d'activité et la région suffisent. Merci d'avance !

Note : _cette  [feuille de calcul](http://www.box.net/shared/njhn3h3out)_ _est mise à disposition gratuitement uniquement pour utilisation privée, non commerciale. Je m'en réserve tous les droits pour les autres usages. Veuillez me contacter en déposant un commentaire ci-dessous si vous envisagez utiliser cette feuille professionnellement._
