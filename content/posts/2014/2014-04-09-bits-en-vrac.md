---
title: "Bits en vrac"
slug: "bits-en-vrac"
date: 2014-04-09
categories:
  - "Comment"
tags: 
  - "casse-tetes"
  - "google"
  - "graphes"
  - "informatique"
  - "internet"
  - "programmation"
coverImage: "form-editor1.png"
---

Quelques découvertes informatiques en vrac

### Les formulaires Google Drive

Le [quiz sur les poissons d'avril](/2014/03/31/poisson-davril-ou-pas/ "Poisson d’Avril, ou pas ?") m'a permis d'expérimenter la puissance et la facilité d'utilisation des [formulaires Google Drive](https://support.google.com/drive/topic/1360904) . C'est simplement génial :

1. dans [Google Drive](https://drive.google.com/), on crée un document de type formulaire
2. on se retrouve dans un éditeur permettant de composer le formulaire. On peut définir le type de chaque champ : texte, choix multiple, cases à cocher, échelle d'évaluation, tout y est. On peut ajouter des règles de validation et des actions à effectuer en fonction des réponses
    
    {{< figure src="images/form-editor1.png" alt="Editeur de Formulaire Google Drive" caption="Editeur de Formulaire Google Drive" link="/wp-content/uploads/2014/04/form-editor1.png" align="aligncenter" width="480" >}}
3. En cliquant le bouton "afficher le formulaire en ligne" on peut voir à quoi ça ressemble pour les utilisateurs et même tester le système, car la collecte des réponses est immédiate : rien à faire de particulier !
4. Lorsque le formulaire  est prêt, il suffit d'envoyer le lien disponible par "Envoyer le formulaire" à des personnes choisies, ou d'intégrer la page sur un site web dans un <iframe>. Plusieurs blogs du C@fé des sciences l'ont même fait simultanément sans aucun problème car le formulaire n'existe en réalité (virtuelle...) que chez Google.
5. Les réponses sont automatiquement collectées dans un document "tableur" sur Google Drive : une ligne est créée pour chaque formulaire rempli, chaque colonne correspondant à un champ. Notez la colonne "horodateur" remplie automatiquement, bien utile.
    
    {{< figure src="images/googleform1.png" alt="Table des résultats" caption="Table des résultats" align="aligncenter" width="480" >}}
    
    Ce que j'ai trouvé assez impressionnant est que l'on peut modifier le tableau sans perturber les votes suivants. Apparemment chaque champ du formulaire est attaché à une colonne par un lien invisible, mais solide : même si on ajoute ou déplace des colonnes, les réponses suivantes restent cohérentes avec les réponses précédentes. Pour le quiz, j'ai ajouté la ligne 2 avec les bonnes réponses ainsi que la colonne D Score. Notez au passage la  géniale formule qui compte le nombre de réponses correctes avec [arrayformula](https://support.google.com/drive/answer/71291?hl=fr) et sumproduct. Elle n'est pas de moi, et il parait qu'elle est possible aussi en Excel...
6. {{< figure src="images/stats.png" alt="stats" caption="résumé des réponses" width="300" >}}
    
    Une petite dernière pour la route : dans le menu "Formulaire" on peut "afficher le résumé des réponses" qui présente les résultats sous une forme graphique qui peut être bien utile.

Les formulaires Google Drive permettent de réaliser facilement des sondages, quiz et concours divers avec toute la puissance et la sécurité (...) de l'infrastructure Google. Ca fait déjà des [émules](http://www.scoop.it/u/goulu) dans le C@fé ...

### Curation V.3.0‎

Rien à faire, il n'y a toujours pas mieux pour suivre les sites intéressants que les [flux RSS](w:). J'ai longtemps utilisé [Google Reader](w:) avec lequel j'ai commencé à faire de la [curation de contenu](w:). En effet, en cochant simplement les articles que je trouvais intéressants, Google Reader les agrégeait dans un flux RSS "de sortie" que je pouvais publier sur [ma page Facebook](http://www.facebook.com/pages/Dr-Goulu/78830919192).

Puis Google a annoncé la fermeture de Reader (toujours incompréhensible pour moi) et j'ai utilisé [Scoop.it](http://www.scoop.it/u/goulu). C'était une bonne idée : Scoop.it permet d'agréger non seulement des flux RSS, mais aussi des tweets, le contenu de pages Facebook et de recherches Google. On peut créer ainsi plusieurs "topics" thématiques, et de jolis widgets comme celui ci-contre à droite. Mais le point fort de Scoop.it, c'est ses possibilités de partage : chaque contenu "scoopé" peut être partagé automatiquement sur Twitter, Facebook, Gogle+ et Tumblr, entre autres.

Scoop.it, c'est vraiment bien, mais ... il y a un problème rédhibitoire : les liens du contenu partagé sont modifiés pour conduire les visiteurs sur la page Scoop.it du topic, et pas directement vers l'article original. Ceci a trois conséquences que je trouve gênantes:

1. La première n'est pas trop grave : les lecteurs doivent cliquer deux fois pour arriver à l'article qui les intéresse, une fois sur la page où ils voient le contenu partagé, puis une seconde fois sur la page Scoop.it.
2. La seconde fausse les analyses de trafic, qui semble provenir de Scoop.it plutôt que du site de partage. Ainsi par exemple mon site a accueilli plus de 2000 visiteurs passés par Scoop.it en un an sans qu'il me soit possible de déterminer où ces 2000 personnes ont initialement découvert l'article qui les intéressait.
3. La troisième touche le droit d'auteur : les outils de partage qui changent les liens diffusent le contenu d'autrui en coupant le lien vers la source, qui est parfois le seul élément identifiant l'auteur. Je me suis soudain aperçu que [mon Tumblr](http://drgoulu.tumblr.com/) "rebloguait" automatiquement les articles que je trouvais intéressants, parfois en me les attribuant implicitement puisqu'il n'y avait plus de mention du site original.

Je me suis donc mis en chasse de nouveaux outils de curation, et après quelques essais j'ai choisi le "trio de la curation V.3" :

- [CommaFeed](https://www.commafeed.com) comme agrégateur de flux. Il offre grosso-modo les fonctionnalités de Google Reader,  une [extension Chrome](https://chrome.google.com/webstore/detail/commafeed/bpbfpjiciblcfeganojjkfapnllbhdga), plus une [application Android](https://play.google.com/store/apps/details?id=com.commafeed.newsplus&hl=fr) (en fait un plugin d'un agrégateur plus général). Chaque jours je parcours une centaine d'articles en sautant d'un à l'autre en pressant la touche \[j\], et si je le trouve intéressant je le lis et je presse \[s\] comme "star". Ca le marque comme favori et l'ajoute à mon [flux RSS de sortie](https://www.commafeed.com/rest/category/entriesAsFeed?id=starred&apiKey=a060bdd5f1c977aa960861ffb2ca6347d824508b).
- [![ifttt](images/ifttt.png)](http://ifttt.com)Je pourrais utiliser directement CommaFeed pour partager le contenu sur Facebook, Twitter, Google+ et autres (mais pas Tumblr). Mais surtout, il me faudrait le faire manuellement : 6 ou 8 clicks de plus, c'est trop. Alors j'ai utilisé [IFTTT.com](https://ifttt.com/), un service qui permet d'automatiser des tâches internet en créant des "recettes" de la forme If This Then That . J'ai ainsi créé des "recettes" qui partagent automatiquement le contenu de mon flux de sortie vers mes pages Facebook, Google+, App.net et Tumblr. Automatiquement. Rien d'autre à faire :-)  (Pour Twitter j'hésite encore...)
- Et j'utilise toujours Scoop.it pour atteindre les utilisateurs de cette plateforme et profiter des beaux widgets, mais je n'utilise plus les outils de partage. En attendant qu'IFTTT permette de "scooper" automatiquement, j'utilise le flux de sortie comme unique source dans Scoop.it et je "scoope" à la main tout ce que j'ai préalablement sélectionné dans CommaFeed.

Tout ça ne me demande en définitive pas plus d'efforts que de tourner les pages d'un journal en papier, et je peux me concentrer sur la lecture tout en gardant une trace dont vous pouvez profiter où vous le souhaitez.

### NetworkX

[NetworkX](http://networkx.github.io/) est une librairie Python permettant de représenter et traiter des problèmes de graphes. Je l'utilise professionnellement assez intensivement ces temps-ci pour un [problème de postiers chinois](/2013/11/22/le-postier-chinois-de-konigsberg/), mais l'autre jour il m'a permis de résoudre le [problème 107](https://projecteuler.net/problem=107) du [Project Euler](/2009/02/23/project_euler/) en quelques lignes seulement. En fait la plupart servent à lire le fichier des données, puis la partie intéressante tient en une seule ligne :

{{< highlight python >}}
print G.size(weight='weight') - minimum_spanning_tree(G, weight='weight').size(weight='weight')
{{< /highlight >}}

Fort non ? Hélas il me semble que peu de problèmes du Project Euler concernent les graphes, donc je ne vais pas pouvoir améliorer mon score rapidement ...

### 2048

[![](images/280px-2048_Screenshot.png)](https://fr.wikipedia.org/wiki/2048_\(jeu_vid%C3%A9o\))Cet article serait paru il y a trois jours si je n'étais pas tombé sur [2048](http://gabrielecirulli.github.io/2048/), le jeu addictif du moment. C'est un jeu tellement simple qu'il aurait du être inventé avant Pac-Man. Et on voit tout de suite comment faire : placer les puissances de 2 les unes à côté des autres pour former une chaîne croissante et propager ainsi les sommes pour arriver à former enfin, après 1024 coups au minimum, la tant convoitée pièce 2048. Il m'a fallu 3 jours. Enfin 3 soirs. 3 nuits...

A un certain moment j'en ai eu marre et voulu utiliser la bonne vieille méthode pour résoudre les problèmes compliqués : programmer. Mais Matt Overlan a été plus rapide et efficace : [son solveur fonctionne très bien](http://ov3y.github.io/2048-AI/) et est très instructif. Je crois que c'est la première fois de ma vie qu'un ordinateur m'apprend à résoudre un casse-tête plutôt que l'inverse. Peu après avoir observé le solveur parvenir au 2048, j'ai appris à dominer ma tentation d'additionner coûte que coûte les nombres les plus élevés et à conserver des lignes ou des colonnes de 4 cases "bloquées", et j'ai gagné.

Après certains passent au [4096](http://martijnkorteweg.github.io/4096/) voire au [9007199254740992](http://www.csie.ntu.edu.tw/~b01902112/9007199254740992/), mais je crois que je vais plutôt attaquer la version "[échelle du vivant](http://sciencedecomptoir.cafe-sciences.org/jeu-2048-echelles-du-vivant/)" de Valentine. Un peu déroutant de prime abord, mais j'aime beaucoup l'idée un peu holiste qu'il y a là derrière... Bravo !
