---
title: "Retour sur Wordpress.com"
slug: "retour-sur-wordpresscom"
date: 2007-09-25
tags: 
  - "internet"
coverImage: "./images/wordpress_logo_cristal.jpg"
---

{{< figure src="./images/wordpress_logo_cristal.jpg" link="http://wordpress.com" >}}

Le blog "Dr. Goulu" a encore un peu changé. En fait je l'ai rapatrié sur le site [WordPress.com](http://wordpress.com) après l'en avoir sorti il y a quelques mois pour l'héberger chez [infomaniak.ch](http://www.infomaniak.com/) sur mon site "professionnel".

A l'époque, le but était d'avoir plus de souplesse et de pouvoir essayer de nombreux thèmes et plugins WordPress non disponibles sur le site de l'éditeur. Mais après quelques mois, je me suis aperçu que ceci se payait en terme de référencement : mes blogs restés sur WordPress.com sont beaucoup plus lus. Comme de plus l'offre de plugins et thèmes s'est bien étoffée, ma décision a été vite prise et vite exécutée. En pratique, j'ai procédé ainsi:

1. exporté tout le contenu de mon ancien blog au format XML, importé sur le nouveau.
2. redirigé le site depuis le registrar du nom de domaine goulu.net ([godaddy.com](http://www.godaddy.com)), et, par sécurité et souci de rapidité, modifié la redirection depuis le très vieux site chez entryhost et utilisé la [même redirection par PHP](http://www.webrankinfo.com/dossiers/debutants/initiation-aux-redirections)
3. modifié le flux [http://feeds.feedburner.com/drgoulu](http://feeds.feedburner.com/drgoulu) pour qu'il pointe sur le flux de ce blog plutôt que l'ancien. Les "Goulu News" provenant de l'[aggrégateur Xfruit](/2007/08/13/aggregation-rss-en-ligne/) se mettent à jour toutes seules puisqu'elles prennent le flux feedburner.

Total : 1h à tout casser.
