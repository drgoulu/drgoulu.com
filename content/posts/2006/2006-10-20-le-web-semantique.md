---
title: "Le Web Sémantique"
slug: "le-web-semantique"
date: 2006-10-20
categories:
  - "Comment"
tags: 
  - "futur"
  - "informatique"
  - "internet"
coverImage: "fdd88ca55a8f211b9fc8f978d988744c.jpg"
---

{{< figure src="images/3f39dd5cf16a7533af8313bbcfa9707a.png" >}}

En faisant des recherches sur un sujet d'intérêt encore top secret, je suis tombé sur le concept intéressant de "web sémantique" et quelques outils s'y rapportant. Ca pourrait bien devenir quelque chose d'important bientôt...

L'objectif du "web sémantique" est de créer un "web des données" dans lequel il serait possible de combiner des données disponibles depuis de multiples sources.

La base du "web sémantique" est le "Resource Description Framework" (RDF), qui décrit des métadonnées par des triplets {sujet, objet prédicat} :

- le sujet représente la donnée. C'est par exemple l'URL de cette page
- l'objet serait une métadonnée, par exemple "auteur"
- le prédicat serait alors la valeur de l'auteur de cette page, par exemple "Ph. Guglielmetti"

Concrètement, un fichier RDF est un fichier XML dont voici un petit exemple:

> @@http://en.wikipedia.org/wiki/Category%3ABusiness\_schools\_in\_India">Business\_schools\_in\_IndiaGurubrahma2006-02-12 18:52:04.0@@

C'est un extrait d'un énorme fichier RDF de 3.6 Gigabytes (oui, Gigas!) qui contient la description des millions de pages de la fabuleuse Wikipedia!

### Ontologies

Comme on le devine, les tags du format XML dépendent du domaine d'application du fichier RDF : "title" , "contributor" etc sont spécifiques à une encyclopédie en ligne. RDF n'est donc pas un dialecte XML mais un format plus général. Pour décrire les tags RDF spécifiques à un domaine, on doit définir une "ontologie", terme un peu ampoulé pour décrire en fait un "modèle de données" adapté à la modélisation de connaissances. Il existe même un dialecte XML pour décrire des ontologies : OWL (Ontology Web Language)

Des exemples d'ontologies RDF sont :

- [FOAF](http://www.foaf-project.org/) (Friend of a Friend), pour modéliser les relations entre personnes (ça serait bien si [LinkedIn](http://www.linkedin.com) pouvait exporter sous ce format...)
- [SIOC](http://sioc-project.org/) (Semantically-interlinked Online Communities), pour le partage de contenus de forums
- [DOAP](http://trac.usefulinc.com/doap) (Description of a project), pour les infos sur les projets de développement OpenSource

### Applications

La première application qui vient à l'idée est la représentation de graphes montrant les relations entre les données

### Alternatives

Les "Topics Maps" sont une approche similaire, proposant le format XTM

### Références

- [Wikipedia : Web sémantique (français, très sommaire)](w:Web_sémantique)
- [Wikipedia : Semantic Web (anglais, détaillé)](w:en:Semantic_Web)
- [page du W3C sur le web sémantique](http://www.w3.org/2001/sw/)
- [W3C semantic web roadmap](http://www.w3.org/DesignIssues/Semantic.html)
- [Drive, a RDF parser for .NET](http://www.driverdf.org/)
- [TopicsMaps.org](http://www.topicmaps.org/)
- [BigBlogZoo, un système de syndication basé sur RDF](http://www.syndicatescape.com/)
- [liste de fichiers RDF](http://pingthesemanticweb.com/)
