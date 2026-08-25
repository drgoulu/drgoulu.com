---
title: "2011, siteswap et jonglerie"
slug: "2011-siteswap-et-jonglerie"
date: 2011-01-12
categories: 
  - "cat2"
tags: 
  - "annee"
  - "nombres"
coverImage: "juggling.gif"
---

En préparant comme à [l'accoutumée](/2010/01/01/2010-2/) un article sur le nombre 2011 et avant qu' [ElJi ne me devance](http://eljjdx.canalblog.com/archives/2011/01/02/20004672.html), je suis tombé sur l'étrange propriété [A071160](http://oeis.org/A071160) selon laquelle 2011 est un "mot de Lukasiewicz qui est aussi une séquence siteswap de jonglerie asynchrone valide"...

Comme je n'y ai rien compris, j'ai cherché, en commençant par la jonglerie via un vieil article de Pour la Science \[1+2\] . On y apprend que le grand [Claude Shannon](http://fr.wikipedia.org/wiki/Claude_Shannon) en personne s'est intéressé au sujet de la notation des figures de jonglerie [[3]](#ref-3), un domaine étonnamment actif qui a abouti dans les années 1980 au "siteswap" ou "notation d'échange de position". La jonglerie "asynchrone" est le type le plus courant, dans laquelle la main gauche et la main droite jettent chacune une balle alternativement. Une séquence est définie en notation "siteswap" par un nombre dont chaque digit correspond à un temps et indique après combien de temps la balle lancée sera relancée. Donc si ce chiffre est impair la balle sera relancée par l'autre main, s'il est pair par la même main.

- "1" définit ainsi la séquence triviale dans laquelle une seule balle passe alternativement de la main gauche à la main droite.
- "333" est la séquence à 3 balles que vous avez essayé au moins une fois dans votre vie. Mais comme tous les temps sont identiques, on peut noter la séquence simplement "3". Si vous laissez tomber une balle, la séquence devient "330", le 0 indiquant un temps mort
- "44" consiste à jongler avec 2 balles avec la main droite, et deux autres avec la main gauche
- "[53145305520" est la séquence décrite sur la Wikipedia](http://fr.wikipedia.org/wiki/Siteswap) [[4]](#ref-4). La voici simulée par [ce génial simulateur de jongleur en ligne](http://jugglinglab.sourceforge.net/bin/example_gen.html) :

{{< youtube id="537p77vdZxs" width="640" >}}

Avez vous remarqué que la moyenne arithmétique des chiffres d'une séquence est un nombre entier égal au nombre de balles à utiliser ? Ceci explique pourquoi beaucoup d'entiers ne définissent pas une séquence valide.

- "2011" est justement valide, mais comme la moyenne des chiffres est 1 et qu'il y a un 0, ce n'est pas une figure très acrobatique...

Le siteswap permet de décrire des jongleries existantes, mais surtout d'en découvrir de nouvelles comme vous pourrez vous en convaincre en utilisant le générateur du [génial simulateur de jongleur en ligne](http://jugglinglab.sourceforge.net/bin/example_gen.html). Avec l'extension de la notation à plusieurs jongleurs, cet outil a permis d'innover de façon spectaculaire dans un art millénaire et bien loin des maths en apparence.

Les "mots de Lukasiewicz" c'est compliqué au point de dépasser l'objectif de ce blog. (Autrement dit, j'ai pas tout compris, mais vous pouvez essayer en consultant [[7]](#ref-7) p. 77). En deux mots, ils permettent de décrire des arbres planaires, des structures très utilisées en analyse syntaxique ou lexicale, dans les compilateurs par exemple.

Et comme je ne parvenais pas à trouver le moindre lien entre les "mots de Lukasiewicz" et la jonglerie, j'ai posé la question à [Antti Karttunen](http://ndirty.cute.fi/%7Ekarttu/), qui a soumis la séquence [A071160](http://oeis.org/A071160). Voici sa réponse :

> There's no other relation except that they have a non-empty intersection, which A071160 gives. Quite simple. I just happened to play with both...

Bon, eh bien dans ces conditions cet article est terminé...

### Reférences et liens

1. <span id="ref-1"></span>Peter J. Beek and Arthur Lewbel "[The Science of Juggling](https://www2.bc.edu/~lewbel/jugweb/science-1.html)", Scientific American, November, 1995, Volume 273, Number 5, pages 92-97.
2. <span id="ref-2"></span>Peter J. Beek etArthur Lewbel "La science de la jonglerie", Pour la Science, Janvier  1996, No 219, pages 80-86.
3. <span id="ref-3"></span>[Arthur Lewbel](https://www2.bc.edu/~lewbel/default.html) "[The Invention of Juggling Notations](http://www.jugglingdb.com/compendium/geek/notation/invention.html)", Jugglers World, Winter 1993-94, pp. 34-35
4. <span id="ref-4"></span>[Siteswap sur Wikipedia.fr](http://fr.wikipedia.org/wiki/Siteswap)
5. <span id="ref-5"></span>Colin Wright and Andrew Lipson "[SiteSwaps - How To Write Down A Juggling Pattern: A Guide For The Perplexed](http://www.juggling.org/bin/mfs/JIS/help/siteswap/ssintro/)", Solipsys Ltd, 1996
6. <span id="ref-6"></span>l'[Internet Juggling Database](http://www.jugglingdb.com/), une mine de [videos](http://www.jugglingdb.com/videos/) et autres infos sur la jonglerie
7. <span id="ref-7"></span>Flajolet and Sedgewick "[Analytic Combinatorics](http://algo.inria.fr/flajolet/Publications/books.html)", Cambridge University Press, 2009
