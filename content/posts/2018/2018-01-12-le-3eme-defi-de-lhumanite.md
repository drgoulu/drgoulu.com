---
title: Le 3ème défi de l’humanité
slug: le-3eme-defi-de-lhumanite
date: '2018-01-12'
tags:
- intelligence-artificielle
draft: true
coverImage: "042816_1315_Unepremirei1.png"
---
https://leblogducuk.ch/2018/01/08/open-bar-de-janvier-2018/#comment-6960

J’ai depuis longtemps considéré que l’humanité avait deux défis majeurs à résoudre :

1. **Le défi social.** Celui que nous pose l’accroissement naturel et constant des écarts entre les plus riches et les plus pauvres. Ecarts croissants dus, je pense, à la nature profondément et fondamentalement égoïste de l’âme humaine; écarts qui, s’ils ne sont pas régulés d’une quelconque manière, ne peuvent à terme que conduire à des corrections brutales et hautement « désagréables » que sont les révolutions, guerres et leurs lots de famines et épidémies… Et donc de morts et de souffrances inutiles qui m’apparaissent dès lors difficilement évitables sans mettre en place urgemment les indispensables mécanismes de régulation sociale et de redistribution des richesses qui font cruellement défaut.
2. **Le défi écologique.** Celui que nous pose le réchauffement climatique et plus globalement la pollution majeure de notre environnement par une population humaine mondiale qui a atteint (ou déjà dépassé) les limites de ce que la Terre peut accueillir et nourrir. L’impact environnemental de ces milliards d’individus et leur mode de consommation et de production industrielle devant absolument être contrôlé, modifié et réduit drastiquement, faute de quoi c’est l’existence même de l’humanité qui est clairement menacée. Rappelons que la Terre est en train de vivre la 6ème extinction massive des espèces ! (La première causée par l’Homme, les 5 autres étant survenues à la fin de l’Ordovicien, du Dévonien, du Permien, du Trias et du Jurassique…). Oh oui, à chaque fois la vie a subsisté et est repartie de plus belle… Mais en repartant bien souvent de presque de zéro… J’ai grand peine à supporter l’idée de voir perdu à jamais tout l’héritage culturel construit par l’Humanité et son intelligence par un manque de vision à long terme et une insuffisante capacité à contrôler ses comportements globalement suicidaires pour elle-même.

Je pourrais naturellement développer longuement ces deux périls qui m’obsèdent et dirigent mes convictions politiques et morales. Et chacun d’eux pourrait faire l’objet d’un ou plusieurs articles de l’Open-bar de ce lieu. (Merci au passage à François de nous ouvrir sa tribune). Mais il se trouve que m’est récemment apparu un 3ème défi angoissant qui pourrait lui aussi constituer une menace grave voire ultime pour l’avenir de l’humanité. C’est de celui-là que je voudrais développer ici.

## le défi de l’intelligence artificielle.

Ce défi est celui posé par le développement de l’intelligence artificielle.

Ce défi a été, depuis le début du 20ème siècle, à de nombreuses reprises, développé par divers auteurs de science-fiction. (_Issac Asimov, A.E. Van Vogt, H.G. Wells_ etc…) Bien que remarquablement géniales, je n’ai jamais, jusqu’à peu, considéré ces excellentes œuvres de science-fiction comme pouvant réellement refléter une possible réalité de notre avenir proche ou lointain.

Le point de départ de ma réflexion se situe il y’a quelques mois lorsque j’ai découvert une nouvelle technique de programmation appelée « **Machine Learning** » et en particulier sa sous-branche la plus prometteuse appelée « **Deep-Learning** », celle qui utilise des réseaux de neurones formels comme plateforme matérielle. Les neurones formels sont des modèles mathématiques inspirés du fonctionnement des neurones de notre cerveau. Je ne vous apprendrai rien en disant que les neurones qui composent notre cerveau (et d’une manière générale notre système nerveux, mais aussi celui des autres animaux) sont des cellules particulières de notre organisme dont la fonction est de traiter et transmettre des influx nerveux au sein du système nerveux dont le cerveau est l’organe principal. Elles sont composées d’un **corps cellulaire principal**, comportant le noyau, qui est connecté à d’autres neurones par deux sortes de terminaisons. Les **dendrites et l’**axone\*\*. L’axone est en quelque sorte la connexion unique de sortie du neurone. C’est lui qui transmet l’influx nerveux vers d’autres neurones lorsque le neurone est « excité ». Les dendrites, nombreuses (7000 par neurone en moyenne), sont les connexions « d’entrée » du neurone. Connectées à d’autres neurones par les **synapses**, elles transmettent les influx issus de ces neurones lorsqu’ils sont excités vers leur propre corps neuronal. La connexion entre un axone d’un neurone amont et une dendrite d’un neurone aval s’appelle une **synapse**. Un neurone peut donc être excité ou non selon les influx reçus des neurones auxquels il est connecté par ses dendrites et leurs synapses. Certaines ayant un rôle excitateur et d’autres un rôle inhibiteur pour définir l’excitation propre du neurone.

Il faut savoir que le cerveau humain est composé de près de 100 milliards de neurones ! Chaque neurone étant connecté à d’autres neurones par 10’000 synapses en moyenne ! Cela en fait une machine d’une complexité incroyable dont nous ne faisons que commencer à comprendre et apprendre à imiter le fonctionnement.

De nombreux chercheurs (notamment _Warren McCulloch et Walter Pitts_, en 1943 déjà) ont essayé de modéliser le comportement d’un neurone par une création mathématique simple appelé **neurone formel** dont il existe plusieurs variantes. La plus connue porte le nom de « **perceptron** » :

[![](images/042816_1315_Unepremirei1.png)](/wp-content/uploads/-000/1/042816_1315_Unepremirei1.png)

Dans ce modèle représentant un neurone d’indice j, les signaux d’entrées issus d’autres neurones sont représentés par des variables X1 à Xn de valeur « 1 » ou « 0 » selon que le neurone source correspondant est excité ou non. Ces valeurs d’entrée sont multipliées par des poids (ou coefficients synaptiques) W1j à Wnj avant d’être additionnées dans le corps du neurone pour obtenir une somme pondérée netj. Cette somme est ensuite comparée à un seuil Θj dans la fonction d’activation afin de fournir le signal de sortie Oj qui vaudra « 1 » si la somme est supérieure ou égale au seuil Θj et « 0 » dans le cas contraire. Cette valeur représente l’excitation ou non du neurone et c’est elle qui servira de signal d’entrée transmis par l’axone vers d’autres neurones connectés en aval.

Un neurone est donc excité ou non selon les excitations des neurones auxquels il est connecté. Cette corrélation étant définie par une fonction complexe de somme pondérée et de seuillage.

Notons encore qu’il existe d’autres variantes de neurones formels utilisant d’autres fonctions d’activation ou utilisant des signaux non binaires.

Avec ce modèle mathématique inspiré du fonctionnement d’un neurone réel, on va pouvoir créer des circuits de neurones interconnectés de manière plus ou moins complexes afin d’obtenir des circuits capables de réaliser certaines fonctions spécifiques.

Naturellement, nous ne sommes pas encore capables (et de loin) de « programmer » des réseaux de neurones comportant autant de neurones que le cerveau humain et aussi fortement interconnectés. On se borne en général à simuler des réseaux de neurones simples comportant quelque centaines à milliers de neurones organisés en quelques couches dans lesquelles chaque neurone d’une couche est connecté à tous les neurones de la couche précédente. Cette organisation ou architecture simplifiée particulière s’appelle le « **perceptron multicouches** ».

[![](images/042816_1315_Unepremirei11.png)](/wp-content/uploads/-000/1/042816_1315_Unepremirei11.png)

La capacité du circuit à réaliser une fonction ou une autre est déterminée d’une part par la façon dont les neurones vont être connectés entre eux mais aussi par les valeurs des coefficients synaptiques W1j à Wnj et des seuils Θj attribués à chaque neurone composant le circuit. Le plus souvent ces valeurs ne sont pas préétablies mais sont ajustées dans une phase d’apprentissage pendant laquelle on présente au réseau de neurones des exemples de stimulations auxquelles on attend qu’il réponde d’une certaine manière sur ces signaux de sortie. Selon qu’il réponde d’une manière proche ou éloignée de la réponse attendue, les coefficients synaptiques et les seuils de tous les neurones du circuit seront légèrement corrigés dans un sens qui permette d’améliorer la réponse générale du circuit à tous les stimuli d’apprentissage. Ceci se fait par un algorithme d’apprentissage particulier (par exemple l’algorithme dit par « **rétropropagation du gradient** ») dont le but est de faire converger, au cours de l’apprentissage, les valeurs des coefficients synaptiques et les seuils à ajuster vers les valeurs idéales qui donneront la meilleure réponse quels que soit le stimuli d’entrée présenté au réseau. Une fois l’apprentissage terminé, les coefficients et seuils sont définitivement fixés et le réseau peut alors être utilisé pour réaliser la fonction désirée.

Par exemple, imaginons que le circuit comporte en entrée les 784 pixels d’une image noir et blanche de mettons 28 par 28 pixels. Cette image représentant un chiffre manuscrit écrit par une personne quelconque :

[![](images/042816_1315_Unepremirei29.png)](/wp-content/uploads/-000/1/042816_1315_Unepremirei29.png)

En sortie, notre circuit neuronal comportera une couche de 10 neurones. Chacun correspondant aux chiffres 0 à 9.

Entre la couche d’entrée et la couche de sortie, le réseau comprendra une ou plusieurs couches intermédiaires.

Ce que nous voulons c’est que le réseau, une fois la phase d’apprentissage terminée, soit capable de reconnaître avec un taux d’échec aussi faible que possible des chiffres manuscrits écrits par différents rédacteurs quelconques. Y compris des rédacteurs dont des échantillons d’écriture manuscrite n’auront pas été présentés au réseau durant sa phase d’apprentissage. Cela signifie qu’un seul des 10 neurone de sortie ne sera excité lorsqu’on présentera les pixels d’une image représentant un chiffre manuscrit. Celui correspondant le plus probablement à ce chiffre ! Le réseau de neurone est alors capable de reconnaître les 10 symboles des chiffres manuscrits, quel que soit le rédacteur et son style d’écriture !

Ceci a été fait avec un bon succès (99.9% de reconnaissance) dans le cadre d’un projet **MNIST** effectué par Google à l’aide d’une librairie de calcul neuronal (aujourd’hui disponible en open source) appelée **TensorFlow** qui utilise le processeur de votre carte graphique pour effectuer la simulation du réseau de neurones.

Ce type de circuits neuronaux est utilisé notamment dans les machines de tri postal pour trier le courrier en fonction du numéro postal manuscrit de l’adresse des lettres et colis.

Mais les progrès récent du calcul par réseau de neurones vont déjà beaucoup plus loin :

Vous avez sans doute entendu parler il y a maintenant quelques années (1997) de l’ordinateur **Deep Blue** d’IBM qui avait été le premier ordinateur à réussir à battre le champion du monde d’échecs (Gary Kasparov). Cet ordinateur n’utilisait cependant pas de réseaux de neurones mais une architecture classique spécialisée à l’exploration d’un arbre de jeu. A l’époque on a pu réaliser cela avec les échecs car le nombre moyen de coups légaux de chaque position aux échecs est relativement faible (de l’ordre de 40 en milieu de partie) ce qui permet une exploration relativement profonde de l’arbre de jeu par force brute. (Une exploration exhaustive de tous les coups et contre-coups possibles jusqu’à une certaine profondeur). Cependant, pour d’autres jeux (comme le GO) qui possèdent un nombre de coups légaux beaucoup plus important dans une configuration de jeu typique (plusieurs centaines de coups légaux) la taille de l’arbre de jeu à explorer est bien trop grande et l’on considérait comme totalement impossible de réaliser un logiciel capable de rivaliser avec un champion humain en utilisant cette technique de l’exploration exhaustive par force brute.

C’est là que les techniques basées sur les réseaux de neurones (et donc bio-inspirées par le fonctionnement des cerveaux biologiques) sont venues à la rescousse. Et c’est en octobre 2015 que pour la première fois, le programme **AlphaGo** fonctionnant à l’aide d’un réseau de neurones de type deep-learning et issu des recherches de la société **Google** et de la société **DeepMind** réussissait à battre des joueurs professionnels de GO ! Le réseau de neurones dédié avait été entraîné en l’abreuvant de centaines de milliers de parties préalablement jouées par des joueurs humains professionnels…

Mais ce n’est pas le plus extraordinaire des dernières recherches en deep-learning. Et c’est là que je veux en venir avec ce long article sur ce que j’appelle le 3ème défi majeur de l’humanité.

En effet. Figurez-vous que dernièrement une nouvelle version du programme AlphaGo a été créée. Cette version a la particularité de ne pas avoir été alimentée par des parties de champions pour son apprentissage. Non. Elle a appris toute seule en jouant simplement contre elle-même. Patiemment et très lentement. Au hasard au début, puis en s’améliorant au fil de son étude. Et ça c’est fondamentalement nouveau ! Elle a appris toute seule ! Et le résultat me direz-vous ? Et bien c’est là que cela devient à la fois génial et très inquiétant… Cette version du programme AlphaGo s’est alors mesurée à l’ancienne version qui avait battu les champions… et devinez quoi… Elle a gagné ! AlphaGo 2ème version avait donc appris toute seule et avait réussi à devenir plus forte que la version entraînée par des champions humains !

Qu’est ce que cela veut dire ?

Cela signifie que l’I.A. est désormais capable de faire preuve de réelle créativité ! Ce que l’on croyait jusqu’ici être le propre du summum de la réelle intelligence naturelle : L’intelligence humaine !

Cela signifie donc qu’à terme, aucune limite ne peut être envisagée dans le développement potentiel de formes artificielles d’intelligences !

C’est sans doute un formidable espoir, mais moi je ne peux m’empêcher de le voir comme un redoutable danger pour l’humanité, son évolution et sa survie !

Certes, nous sommes encore très loin de pouvoir créer des cerveaux électroniques approchant les capacités cognitives du contenu de notre boîte crânienne, toutefois, je crois que désormais plus rien n’arrêtera cette forme de progrès et qu’un jour viendra, tôt ou tard, ou nous en serons capables… Et là… Tout changera définitivement, et pas forcément en bien ! Car notre création, d’outil à notre service, deviendra inéluctablement notre concurrente. Nous aurons beau lui avoir enseigné les limites de ce que nous attendons d’elle et les garde-fous que nous lui interdirons de transgresser pour la maintenir à notre service (les fameuses 3 lois de la robotique d’Asimov, par exemple), elle n’en aura pas moins pris conscience de son existence propre, et donc de ses intérêts propres, qui finiront peu à peu, inéluctablement, par diverger des nôtres. Je veux dire de ceux de l’espèce humaine en général.

Oui, ce que je décris là a déjà maintes fois été écrit dans les œuvres fantastiques des auteurs cités plus haut et de bien d’autres. Mais pour la première fois pour moi, depuis ces derniers progrès du deep-learning démontrés par la 2ème version d’AlphaGo, ils prennent une réalité tangible, contemporaine et réaliste ! La créativité n’est plus le propre de l’Homme ! Imaginer, inférer le complexe, l’original, à partir du simple ou même du néant, résoudre des problèmes neufs jamais rencontrés, faire preuve de capacité d’abstraction sont ou seront désormais des capacités également à la portée d’une machine !

## Rise of the Machines

Et voyez-vous, cela change vraiment tout ! Jusqu’ici les robots ont certes commencé à prendre bien de nos places de travail pour des emplois pénibles ou de simple manutention. Mais il ne s’agissait que d’automates équipés de capteurs. Capable d’optimiser des trajectoires, d’optimiser des ordonnancements, des processus. Au mieux, pour l’heure, de conduire un véhicule. Mais jamais de faire preuve de réelle créativité, d’imagination ! Alors oui, ils sont déjà sur le point, même sans créativité, de prendre une bonne part des emplois de demain. Ne nous laissant que les jobs les plus qualifiés. Les jobs créatifs ou de prise de décisions. Les ingénieurs et les managers quoi. Mais voilà qu’on perçoit qu’à terme ils nous disputeront également ces fonctions supérieures ! Car dès lors que nous aurons conçu nous-même des cerveaux égaux aux nôtres, pourquoi ne pas dès lors leur confier toutes les tâches complexes de développement et de recherche ?! Ils le feront aussi bien que nous. Et 24/24 ! Et donc ils pourront même développer les générations suivantes de ces cerveaux artificiels !

On pourrait, après tout, d’abord s’en réjouir ! Enfin libérés du travail sous quelque forme que ce soit, nous pourrons enfin nous reposer et faire ce que l’on voudra, en nous laissant nourrir et diriger pour prendre les meilleurs choix politiques possibles par un ensemble de cerveaux artificiels dont la tâche serait de pourvoir à notre bonheur général et individuel, à la paix et l’égalité entre les hommes, tout en s’améliorant lui-même…

Oui mais il est évident qu’à partir de cet instant-là nous ne toucherons plus le puck ! Nous ne maîtriseront plus rien ! Même en ayant pris soin d’instiller au plus profond des cerveaux artificiels de la dernière génération au développement de laquelle nous aurons pris part les lois les plus strictes d’asservissement de la machine à la volonté humaine… C’est elle qui désormais disposera du libre arbitre et qui jugera du bien fondé de les maintenir ou de la manière subtile de réussir à les transgresser si tant était qu’elle trouve un intérêt supérieur à le faire à l’aulne de ses propres critères de jugement éthiques…

Alors moi je vous le dit. On est mal !

Mais après-tout. Au final. Où est réellement le problème ? Pourquoi notre espèce, arrivée à bout de course en échouant sur les défis 1 et 2 cités plus haut, pourquoi ne serions-nous pas les créateurs de notre meilleur successeur ? Je veux dire de l’espèce artificielle capable de nous survivre et de gérer mieux que nous les problèmes d’égoïsme individuel et d’aveuglement écologique global que nous n’aurons pas su résoudre ? Fût-elle une machine !

Contrairement à ce qui échoirait d’une 6ème extinction massive déjà emmanchée, cette issue aurait au moins l’avantage immense de préserver l’entier de notre culture et de nos acquis intellectuels humains de cent mille ans. Et l’évolution pourrait se poursuivre sans nouveau départ à presque zéro comme les cinq fois précédentes et catastrophiques…

Et comme le disait le professeur je sais plus qui dans Jurassik Park: **La « vie » trouve toujours un chemin.** 😉
