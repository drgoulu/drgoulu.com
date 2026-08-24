---
title: "Lean Bicycle Factory"
date: 2011-11-19
categories: 
  - "cat3"
  - "cat2"
tags: 
  - "jeux"
  - "optimisation"
  - "production"
  - "simulation"
coverImage: "Capture.png"
---

Une fois n'est pas coutume, je vais causer un petit peu boulot. Depuis quelques temps je m'occupe d'un système dynamique assez complexe : une usine de production de machines. Avec quelques collègues, nous y appliquons la "philosophie" [lean](http://fr.wikipedia.org/wiki/Lean), dont je suis pour ma part assez heureux de pouvoir valider les principes par quelques calculs et simulations avant de bouleverser les habitudes de gens employés dans la boite depuis 10x plus longtemps que moi.

Une de mes tâches est d'animer des journées de formation offertes à tout le personnel par groupes de 8 personnes, journées pendant lesquelles nous introduisons des notions "lean" comme le [juste-à-temps](http://fr.wikipedia.org/wiki/Juste-%C3%A0-temps_\(gestion\)) par un jeu dans lequel les collaborateurs construisent des modèles réduits de machines en améliorant peu à peu le système de production.

Il me manquait un moyen d'expliquer ce qu'est le lean à des gens qui ne travaillent pas du tout dans ce domaine (vous ?) d'une manière ludique. C'est mon collègue Alex qui l'a trouvée sous la forme du "[Lean Bicycle Factory Demonstration Game](http://ludosity.com/library/lean-game/)" de Ludosity, un "[serious game](http://fr.wikipedia.org/wiki/Jeu_s%C3%A9rieux)" assez fun et rapide pour devenir addictif, et même générer une petite compétition entre collègues...

_(Ajout du 9.12.2013_: comme le lien de téléchargement original ne fonctionne plus, essayez [celui-ci](http://drgoulu.local/wp-content/uploads/2011/11/LeanBicycleFactory-1.zip).)

Si j'en parle, c'est que j'ai le "high score" actuel : 68768\*. Voilà comment j'ai fait (spoiler alert ! essayez de faire mieux _avant_ de copier...) :

{{< figure src="images/Capture.png" alt="Essayez de faire mieux... ou cliquez pour le film pour tricher" caption="Essayez de faire mieux... ou cliquez pour le film pour tricher" link=\"https://www.youtube.com/watch?v=fWkBvanJoz4\" align="aligncenter" width="622" >}}

Le début du jeu sert à observer et à comprendre le flux, mais j'ai remarqué que ce n'est pas du tout évident, alors voici quelques infos utiles :

1. les clients (en haut à droite) commandent des vélos de 3 tailles et de 3 couleurs différentes. S'ils ne sont pas livrés rapidement, ils attendent un moment puis partent dans un nuage de fureur
2. la commande arrive au responsable de la production, en bas, qui peut soit lancer la production du vélo commandé, soit (par défaut) produire des vélos selon des prévisions de vente. Il envoie des blocs de métal à la machine de droite
3. la machine produit des cadres soit dans l'ordre des commandes (FIFO), soit en regroupant les cadres par taille pour minimiser le temps de changement des matrices pour cadres homme/femme/enfant
4. le montage se fait à l'établi rouge
5. la peinture se fait à la machine en haut à gauche, qui peint des lots de 4 (modifiable) vélos
6. le contrôle de qualité se fait à la table verte. Je n'ai pas bien compris ce qui arrive aux vélos défectueux, je pense qu'ils ne ne génèrent qu'un surcoût et peut être un temps supplémentaire pour les réparer
7. les vélos arrivent au stock, d'où ils sont livrés aux clients qui les attendent encore...
8. les transports se font aussi par lots de 4 (modifiable), mais cette valeur est un minimum : s'il y a plus de pièces à transporter, le chariot les prend.

Le plus énervant lorsqu'on tente d'optimiser ce processus tout simple est la limitation à 2 modifications par tour de jeu, et leur coût associé qui est clairement affiché alors que le bénéfice ne l'est pas. C'est hélas très réaliste...

Il y a des choses qui ne me plaisent pas dans ce jeu, notamment que j'atteins mon meilleur score en n'utilisant pas du tout deux principes fondamentaux du lean : le flux tiré par le client et la production à l'unité, donc il doit y avoir moyen de faire mieux.  J'ai lancé une [discussion sur LinkedIn](http://www.linkedin.com/groups/Did-you-play-Lean-Bicycle-37987.S.81249105) à ce sujet si ça vous dit.

Note\* : les scores publiés sur internet ne valent pas tripette car le jeu a été hacké. Si vous me battez, je veux une image ou une vidéo pour le prouver :-)
