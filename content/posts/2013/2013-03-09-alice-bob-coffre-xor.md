---
title: "Alice, Bob et le coffre de XOR"
slug: "alice-bob-coffre-xor"
date: 2013-03-09
categories:
  - "Comment"
tags: 
  - "informatique"
coverImage: "alice-bob-coffre-xor-L-e5xUNf.jpeg"
---

Pendant des siècles, la [cryptographie](w:) a principalement consisté à inventer des systèmes de [chiffrement](w:) des messages rendant très difficile le [décryptage](w:décrypter) du message par quelqu'un ne possédant pas la clé, et à trouver des moyens de transmettre la clé au destinataire.

Aujourd'hui il existe des moyens de chiffrer des message de manière absolument indécryptable, et de les envoyer à un destinataire qui pourra les lire sans qu'on ait besoin de lui transmettre la clé ! Impossible ou très compliqué, pensez-vous ? Voici pourtant une méthode ultra-simple.

{{< figure src="images/alice-bob-coffre-xor-L-e5xUNf.jpeg" alt="Deux cadenas, c'est beaucoup mieux qu'un" caption="Deux cadenas, c'est beaucoup mieux qu'un" link="/wp-content/uploads/2013/03/alice-bob-coffre-xor-L-e5xUNf.jpeg" width="321" >}}

Il y a très longtemps, [Alice et Bob](w:) ont trouvé un moyen pour s'envoyer des objets précieux dans des coffres fermés à clé sans jamais avoir besoin de se transmettre les clés, ni d'en faire des doubles. Tout ce dont ils ont besoin, c'est d'un coffre que l'on peut fermer avec deux cadenas:

1. Alice envoie un précieux cadeau d'anniversaire à Bob dans le coffre qu'elle ferme avec un cadenas A dont elle garde la clé.
2. Bob ne peut pas ouvrir le coffre, mais il peut y ajouter son propre cadenas B dont il garde la clé et renvoie le coffre fermé à double à Alice
3. Alice ouvre son cadenas A et renvoie à Bob le coffre qui n'est plus fermé que par le cadenas B
4. Bob peut enfin ouvrir le coffre en enlevant le cadenas B, mais son anniversaire est déjà passé parce qu'il a fallu trois trajets au messager au lieu d'un seul, et ce dernier a eu tellement peur en traversant trois fois la forêt des brigands qu'il a démissionné.

Au XXIème siècle, la vitesse des communications est telle qu'un coffre numérique à deux cadenas peut devenir utilisable, à condition de résoudre un problème qui n'existe pas avec le coffre:

1. Alice chiffre un bon d'achat pour un précieux cadeau d'anniversaire X avec une fonction utilisant la clé A. Elle transmet à Bob le message A(X) .
2. Bob [surchiffre](w:surchiffrement) le message avec sa fonction clé B et envoie à Alice le message B(A(X))
3. Alice déchiffre le message avec sa clé, ce qui produit un message qu'elle renvoie à Bob.
4. Mais là, Bob ne pourra le déchiffrer correctement que si les fonctions A et B sont commutatives, c'est à dire que le résultat des deux chiffrements A et B est indépendant de leur ordre, donc que A(B(X)) = B(A(X). Dans ce cas seulement le message A\-1(B(A(X))) transmis par Alice à l'étape 3 sera égal à B(A\-1(A(X))), donc à à B(X) et Bob pourra alors déchiffrer son cadeau.

Alice et Bob ont donc besoin de créer des fonctions/clés de chiffrement A et B qui soient à la fois inviolables, et commutatives. Or il existe une fonction toute bête qui combine ces deux avantages : le [OU exclusif binaire, XOR](w:Fonction_OU_exclusif#Exemple_d.27utilisation_en_cryptographie) pour les intimes.

Claude Shannon a démontré en 1949 quelque chose d'intuitivement évident : en effectuant un XOR bit a bit entre un message et une clé aléatoire de même longueur à usage unique, le message crypté est absolument inviolable.

Illustrons ceci avec un message d'une seule lettre codé sur 8 bits selon le code ASCII:

1. Alice veut envoyer à Bob la lettre "x", soit la séquence de bits  X=01111000
    - Elle utilise un générateur aléatoire, quantique tant qu'à faire, qui produit la clé A=11010001
    - Alice calcule XOR(X,A) qui donne le message M1=10101001 et transmet ce message
    - Eve la curieuse intercepte le message, mais ne peut y trouver aucune anomalie statistique lui permettant d'en déduire la clé. En effet le message peut tout aussi bien correspondre à la lettre "y" (01111001) codée avec la clé 11010000, ou n'importe quelle autre combinaison lettre/clé.
2. Bob reçoit le message, génère une clé B aléatoire de même longueur B=00000101 et transmet le message M2=XOR(M1,B)=10101100
3. Alice génère le message M3=XOR(M2,A)=01111101, ce qui "enlève le cadenas A" car XOR est sa propre réciproque : XOR(A,XOR(A,X))=X
4. Bob calcule alors XOR(M3,B)=01111000 et obtient bien le code ASCII de la lettre "x"

Le seul problème, c'est qu'Eve a finalement aussi réussi à décrypter le message, Comment a-t-elle fait ?

Vous le saurez en lisant les commentaires que d'autres ne manqueront pas d'écrire, et vous apprendrez comment Alice et Bob préserveront leur intimité dans la suite de leurs aventures, bientôt sur drgoulu.com.
