---
title: "Mort aux Virus, Spam, Hoaxes et Popups !"
date: 2004-06-21
categories: 
  - "non-classe"
---

Il y a au moins deux millions de pages sur la sécurité informatique sur Internet, mais celle-ci est unique : elle a été spécialement écrite pour ma maman, qui voulait une explication sans jargon...

Si je vous ai demandé de visiter cette page, c’est probablement parce que vous avez les mêmes compétences en sécurité informatique que ma maman et que vous m’avez envoyé un mail qui le prouve (contenant un virus ou un canular) :-)

<!--more-->

Je commence par définir le jargon :

- **Virus** petit programme capable de se reproduire lui-même et de se propager d’une machine à une autre, par e-mail, mais aussi par l’échange de disques etc. Certains virus effectuent aussi des opérations malveillantes telles que la destruction de fichiers après un certain temps.
- **Anti-Virus** programme capable de détecter l’arrivée ou l’activité de virus sur votre machine, d’empêcher leur propagation et de réparer les dommages causés par certains.
- **Cheval de Troie** (trojan) petit programme greffé sur un autre et permettant à un intrus d’accéder à votre machine à votre insu
- Pare-feu (Firewall) programme surveillant l’activité sur le réseau (local ou Internet), bloquant les tentatives d’intrusions, notamment via les chevaux de Troie
- **Canular** (Hoax) e-mail avertissant d’une menace fictive, destiné à être propagé manuellement à vos connaissances. Dans certains cas, contient des instructions à suivre qui peuvent être néfastes (effacement de fichiers soi-disant contaminés...)
- **Spam** e-mails non désirés, publicitaires voire pornographiques, pouvant contenir des virus, des programmes chevaux de Troie, des canulars...
- **Cookies** petits fichiers contenant les données personnelles que vous donnez en vous inscrivant sur des sites web et en principe destinées à vous éviter de les retaper lors d’une visite suivante.
- **Addware** / Spyware Logiciels qui, en plus de remplir des fonctions utiles, collectent des données sur vous en lisant les cookies et les utilisent à des fins publicitaires, souvent en transmettant ces informations à des bases de données
- **Popups** Fenêtres publicitaires de couleur dominante rose qui s’ouvrent sans demander votre avis pendant que vous surfez avec Internet Explorer. En fermer une provoque en général l’ouverture de 2 autres...

Maintenant, pour ne pas être embêté sur internet il faut (par ordre d’importance décroissante)

#### 1\. Avoir un anti-virus à jour

- J'utilise actuellement  [AVG de Grisoft](https://www.avg.com/en-us/homepage) qui est excellent et gratuit pour les privés
- [Norton Antivirus de Symantec](https://www.symantec.com) et [VirusScan de McAfee](https://www.mcafee.com/us/index.html) sont devenus des dinosaures. Lourds et il faut payer chaque année pour avoir une protection permanente...
- Ne pas oublier les mises à jour ! De nouveaux virus apparaissent chaque jour. Une mise à jour par mois est un minimum.

Contre les spywares/adwares,il faut bien noter que les anti-virus ne les enlèvent pas ! Une fois par mois il faut lancer un logiciel comme ["Ad-aware se" de LavaSoft](https://www.adaware.com/) qui les enlève.

#### 2\. Avoir une protection contre le spam.

pour ne pas recevoir de spam, il y a plusieurs méthodes à combiner:

- enlever les spyware/aware (paragraphe précédent) car vos adresses e-mail sont les premières choses qu’ils transmettent.
- ne pas donner votre adresse e-mail sur Internet ! Lorsqu’un site vous demande un adresse e-mail ou lorsque vous mettez un message sur un forum, utilisez une adresse e-mail fictive, ou une adresse secondaire que vous n’utilisez que lorsque c’est nécessaire. Vous pouvez obtenir des adresses e-mail gratuites partout, par exemple sur www.hotmail.com. Pour ma part, j’ai enregistré des noms de domaines entiers (comme goulu.net) ce qui me donne une infinité d’adresses e-mail (n’importe quoi @ goulu.net). Ceci me permet de donner sur internet des adresses qui ne seront utilisées qu’une fois, de bloquer celles qui sont spammées et de trier mon courrier automatiquement, tout ça pour environ $10 par an (le prix du domaine=.
- Surtout, ne mettez jamais votre adresse e-mail sur votre site web ! Ou alors utilisez une combine pour éviter les programmes qui collectent automatiquement les emails depuis le web.
- Si vous recevez beaucoup de spam, commencez par vous assurer que le filtre de votre fournisseur d'accès est bien configuré. Si vous recevez encore du spam, envisagez un logiciel anti-spam spécial:
    - SpamNet ne fonctionne que sur Outlook et est payant, mais c’est le meilleur dans le cas ou vous voulez recevoir des mails d’expéditeurs inconnus. Le principe est génial : les utilisateurs eux-mêmes marquent les messages qu’ils considèrent comme du spam et ces informations sont partagées automatiquement sur le serveur de Cloudmark. Ansi, seuls les messages envoyés en masse seront rejetés, il n’y a aucun risque qu’un message qui vous est réellement destiné ne finisse à la poubelle
    - Norton AntiSpam est payant aussi et fonctionne avec tous les programmes de mail, mais il considérera comme spam tout ce qui provient d’expéditeurs inconnus, ce qui vous condamne à regarder attentivement votre poubelle pour en sortir les premiers messages de vos nouveaux correspondants. Les messages suivants provenant d’expéditeurs désormais connus seront reçus sans problèmes
    - 0Spam est un service gratuit qui vous fournit une adresse e-mail qui sera filtrée pour vous. Cette solution est utile si votre boîte se remplit de spam entre deux fois où vous vous y connectez, mais je n’ai pas testé l’efficacité de leur filtre.
    - SpamPal est un logiciel gratuit qui se base sur des listes de serveurs connus pour être à l’origine de spam. Donc il suffit que des spammeurs utilisent une fois ou l’autre, disons par exemple une adresse @bluewin.ch pour envoyer leurs messages pour que tous les messages provenant de tous les autres utilisateurs de bluewin.ch soient mis à la poubelle comme étant du spam. Il est apparemment possible d’arranger ça à coups de configuration fine...
