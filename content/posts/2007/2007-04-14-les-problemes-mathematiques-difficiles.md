---
title: "les problèmes mathématiques difficiles"
slug: "les-problemes-mathematiques-difficiles"
date: 2007-04-14
categories:
  - "Pourquoi"
tags: 
  - "maths"
coverImage: "logo.png"
---

{{< figure src="images/logo.png" >}}

Le dossier sur "[les problèmes difficiles en mathématiques](http://www.larecherche.fr/editorial/problemes-difficiles-01-04-2007-81359)" dans le journal "[la Recherche](http://www.larecherche.fr/)" d'avril 2007 indique 7, pardon plus que 6 manières de devenir millionnaire en résolvant des problèmes de maths.

Pour commencer, l'article présente un intéressant "arbre de la complexité" des problèmes mathématiques qui ressemble à çà:

- problèmes ouverts (n'ayant pas encore de réponse)
    - non formulé : n'ayant pas d'énoncé précis en termes mathématiques. Exemple : justifier les [équations de Navier-Stokes](w:) (voir plus bas)
    - conjectures : problèmes formulés non résolus.
        
        - indécidables : problèmes dont on a démontré qu'ils sont indémontrables. Exemple : le [second problème de Hilbert](w:), qui propose de démontrer la cohérence de l'arithmétique, donc que ses axiomes ne sont pas contradictoire. Gödel a montré en 1931 que ce n'était pas possible sans sortir de l'arithmétique en ajoutant des axiomes.
        
        - décidables : problèmes pour lesquels on sait qu'il existe une solution, positive ou négative
            - preuve (négative) avec contre-exemple. Le [troisième problème de Hilbert](w:) postule qu'étant donné deux polyèdres de même volume, il est toujours possible de découper l'un d'eux en polyèdres et de former l'autre en les réassemblant. Max Dehn montra qu'il est impossible de passer du tétraèdre au cube.
            - Théorèmes:
                
                - autres théorèmes (que ceux dits "d'existence", ci-dessous). Exemples : le [Grand Théorème de Fermat](w:), démontré par Wiles en 1993, et la [Conjecture de Poincaré](w:), qui vient d'être démontrée (voir plus bas)
                
                - théorèmes d'existence, postulant l'existence d'un objet mathématique ayant certaines propriétés, objet qu'il suffit de trouver...
                    
                    - démonstration par l'absurde : on démontre que la négation du théorème aboutit à une contradiction. Exemple : en 1761 J.H. Lambert prouva la [transcendance de pi, puis celle de e](http://www.pi314.net/lindemann.php)^a, quel que soit a.
                    
                    - méthode, ou "algorithme" : une séquence finie d'opérations permet d'obtenir une solution
                        
                        - complexité inconnue : le [problème du voyageur de commerce](w:) (un problème qui me poursuit...)
                        
                        - non polynomiale : l'[arithmétique de Presburger](w:)
                        - polynomiale
                            
                            - grand degré : le [test de primalité AKS](w:) permet de savoir avec certitude si un nombre de n chiffres est [premier](/2007/01/20/les-nombres-premiers/) ou pas en n^12 opérations, ce qui peut être beaucoup plus court que d'effectuer les divisions
                            
                            - petit degré : tous les algorithmes "classiques", par exemple le [calcul du PGCD](w:algorithme_d'Euclide)

### de Hilbert à Clay

en 1900 David Hilbert présenta [23 problèmes très difficiles](w:problèmes_de_Hilbert). 17 ont été résolus pendant le XXème siècle. En 2000, Landon Clay a offert 1 million de dollars pour la résolution de chacun des 7 [problèmes du millénaire](w:)

1. La [Conjecture de Poincaré](w:). [Grigori Perelman](w:) a démontré cette conjecture en 2003. Après avoir refusé la [médaille Fields](w:) en 2006, refusera-t-il aussi le million de dollars de la fondation Clay ?
2. La [Conjecture de Birch et Swinnerton-Dyer](w:)
3. la [Conjecture de Hodge](w:)
4. l'[Hypothèse de Riemann](w:)
5. la [Théorie de Yang-Mills](w:) qui a d'importantes conséquences en physique des particules
6. une meilleure compréhension des [équations de Navier Stokes](w:) qui décrivent les écoulements turbulents de fluides, mais paraissent trop compliquées pour décrire un phénomène physique si fondamental. C'est le type même d'énoncé difficile à formuler en termes mathématiques, c'est pourquoi la fondation Clay a du définir clairement certains aspects de ce problème pour pouvoir proposer le prix.
7. le [Problème P = NP](w:), un problème fondamental en informatique théorique posé en 1970 : est-il possible de résoudre un problème de la classe "NP-complet" en temps polynomial, ou est-ce impossible ?
