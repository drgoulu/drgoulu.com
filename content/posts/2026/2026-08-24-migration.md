---
title: 'Migration : de Wordpress à Hugo'
slug: migration
date: 2026-08-24T16:30:48+02:00
draft: false
summary: drgoulu.com ressuscite en migrant de  WordPress à Hugo
tags:
  - Wordpress
  - Hugo
coverImage: "2a62d67153ec2834b7d7f23250a1c260-1.jpg"
---
Après plusieurs années de quasi abandon, j'ai décidé de faire revivre ce site pour plusieurs raisons :

1. il tombait en loques et c'était dommage
2. je veux y transférer une bonne partie de l'énorme contenu que j'ai publié [sur Quora](https://fr.quora.com/profile/Dr-Goulu) ces dernières années.
3. j'ai du temps à perdre, et des IA pour m'aider. Ca s'est révélé indispensable.

## Les problèmes de WordPress

Depuis 2010 ce blog était propulsé par WordPress, qui est devenu un monstre, notamment à cause de la foison de plugins que j'utilisais. Il devenait de plus en plus difficile de gérer les versions, les conflits entre plugins, les mises à jour, et les failles de sécurité, sans compter les bugs de certains, qui ont notamment causé la perte de nombreuses images.

Pourtant, devant l'ampleur de la tâche, j'étais assez réticent à changer de solution. J'ai commencé par copier le site en local sous [LocalWP](https://localwp.com/), ce qui me permettait de farfouiller dans les fichiers sans passer par FTP, et surtout de ne pas abîmer le site en production. J'ai ainsi pu remettre à jour certains plugins indispensables, notamment

* [OpenBook](https://github.com/goulu/openbook) qui a été accepté comme [plugin officiel](https://wordpress.org/plugins/openbook-book-data/) (même si la bannière dit qu'il est obsolète...)
* [Reference 2 Wiki](https://github.com/goulu/reference-2-wiki) pour gérer les milliers de liens vers Wikipédia de drgoulu.com
* [Altmetric](https://github.com/goulu/Altmetric) qui était abandonné
* et le thème [Customizr](https://github.com/goulu/customizr) qui à l'air de l'être car mes "Pull Requests" qui le rendent compatible avec les dernières versions de WP sont ignorées...

Mais même avec tout ça, j'étais encore insatisfait, et attiré par la curiosité : comment faire un blog moderne en 2026 ?

## Le choix : Hugo

La tendance actuelle, est clairement au [générateur de site statique](w:) : le site est considéré comme un projet informatique qui est "compilé" en pages HTML fixes, "comme dans le temps". Plus de base de données, plus de PHP, plus de failles de sécurité potentielles, et en plus la navigation devient hyper rapide, comme vous vous en apercevez en parcourant ce site...

Je suis assez rapidement tombé sur [Hugo](https://gohugo.io/) , mais par acquit de conscience j'ai aussi essayé [Quarto](https://quarto.org/) qui m'a bien tenté pour son orientation scientifique basée sur Python, Jupyter, etc. mais il est surtout utilisé dans le monde académique, et moins pour les blogs généralistes comme le mien. De plus il faut installer [Positron, un n-ième IDE](https://positron.posit.co) à la VS Code pour l'éditer...

J'ai aussi examiné [Astro](https://astro.build) , dont la technologie a l'air plus moderne encore, peut-être trop...

Après avoir demandé un [tableau comparatif à une IA](https://share.google/aimode/XGNJvQjEpjzur8hLx), j'ai choisi Hugo dans sa mouture [HuboBlox](https://hugoblox.com), à la fois complète et facile à démarrer.

## Markdown

Un "inconvénient" de ces générateurs de sites statiques est que les articles doivent être écrits en [Markdown](w:), un format de texte enrichi autrefois réservé à de simples fichiers readme.md qui devient très à la mode avec les IA, mais qui n'est pas [wysiwyg](w:). L'idée est d'éditer les articles soit:

* avec un éditeur de texte avec un système de prévisualisation du résultat. c'est notamment l'idée de plugins de VS Code comme :
  * [Hugo IntelliSense](https://marketplace.visualstudio.com/items?itemName=hugoblox.hugo), qui est tout neuf et pas très convaincant pour l'instant
  * [Ownable](https://ownable.dev) plus abouti actuellement me semble t'il
* [Cloudcannon](cloudcannon.com), un éditeur wysiwyg et gestionnaire du site Hugo en ligne via GitHub, que jutilise pour écrire ces lignes parce qu'il est gratuit pendant 20 jours, mais assez cher ensuite, ce qui fait que je ne vais pas le garder, hélas

{{< figure src="/wp-content/uploads/2008/04/2a62d67153ec2834b7d7f23250a1c260-1.jpg" title="Galaxie" alt="Galaxie" caption="Galaxie" attrlink="https://galaxie.com" width="600" height="400" >}}

{{< vimeo id="335988321" title="Hugo Explainer Video" >}}

## Commentaires Disqus

L'intégration des commentaires historiques du blog repose sur [Disqus](https://disqus.com/). Lors de la migration vers Hugo Blox / Tailwind CSS, un problème d'incompatibilité est apparu :

### Incompatibilité OKLCH et Disqus `embed.js`

Le script d'intégration de Disqus (`embed.js`) analyse automatiquement l'environnement de la page (`getComputedStyle`) pour adapter les couleurs du fil de discussion (mode clair/sombre, couleur des liens).

Or, Tailwind CSS et Hugo Blox utilisent désormais le format de couleur moderne `oklch(...)`. Le parseur interne de Disqus (`parseColor`), n'étant pas compatible avec `oklch`, échouait avec l'erreur :

```text
Uncaught Error: parseColor received unparseable color: oklch(...)
```

### Solution mise en place

Pour isoler Disqus des styles `oklch` globaux, des règles CSS explicites ont été ajoutées dans `assets/css/custom.css` afin de forcer des formats de couleurs traditionnels (Hex / RGB) sur le conteneur `#disqus_thread`, son texte d'arrière-plan et ses liens internes (`#disqus_thread a`), pour les thèmes clair et sombre :

```css
/* Forcer des couleurs standards (Hex/RGB) pour Disqus */
#disqus_thread,
#disqus_thread * {
  color: #111827 !important;
}

#disqus_thread {
  background-color: #ffffff !important;
}

#disqus_thread a,
#disqus_thread a:link,
#disqus_thread a:visited,
#disqus_thread a:hover,
#disqus_thread a:active,
.dsq-brlink,
.dsq-brlink a {
  color: #2563eb !important;
}

.dark #disqus_thread,
.dark #disqus_thread * {
  color: #f8fafc !important;
}

.dark #disqus_thread {
  background-color: #0f172a !important;
}

.dark #disqus_thread a,
.dark #disqus_thread a:link,
.dark #disqus_thread a:visited,
.dark #disqus_thread a:hover,
.dark #disqus_thread a:active,
.dark .dsq-brlink,
.dark .dsq-brlink a {
  color: #60a5fa !important;
}
```