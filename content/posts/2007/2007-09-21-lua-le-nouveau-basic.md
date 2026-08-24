---
title: "Lua, le nouveau Basic"
date: 2007-09-21
categories: 
  - "non-classe"
tags: 
  - "programmation"
---

[![](images/522870916653c28ad6c489b73105ed5f.gif)](http://www.lua.org)

Me suis mis à programmer un peu en [Lua](http://www.lua.org), un "langage de script" [très utilisé dans les jeux video](http://www.lua.org/uses.html), mais aussi par Hyperion.

LUA présente plusieurs caractéristiques étonnantes:

1. il est très rapide, presque autant que JAVA mais environ 6x plus que Python ou 15x plus que PHP (voir [ici](http://www.timestretch.com/article/mandelbrot_fractal_benchmark) par exemple)
2. l'interpréteur LUA est très petit : moins de 100k, contre 800k pour Python et beaucoup plus pour les autres langages.
3. LUA est à la fois un langage très simple, genre "Basic des années 80'", et offre des notions beaucoup plus avancées décrites plus bas
4. LUA est le premier langage de programmation brazilio-catholique : il a été créé à la [Pontifícia Universidade Católica do Rio de Janeiro](http://www.puc-rio.br/index.html) et est donc mieux documenté en portugais qu'en français.

<!--more-->

### Outils

Télécharger LUA depuis le site [www.lua.org](http://www.lua.org) ne sert à rien, à moins que vous aimiez programmer dans une fenêtre DOS...

Le mieux est de vous initier à LUA avec [LuaEdit,](http://luaedit.luaforge.net/index.html) un petit IDE simple mais avec ce qu'il faut pour éditer, compiler et déboguer du code LUA. Comme l'interpréteur LUA est tout petit, il est fourni avec !

J'ai investigué d'autres environnements de développement LUA, y compris certains censés s'intégrer au Microsoft Visual Studio, mais aucun n'a fonctionné correctement :-(

### Un langage (très) simple

- En LUA comme avec beaucoup de langages de script, les variables peuvent prendre n'importe quel type sans déclaration préalable : `a=1 -- un nombre entier a=3.14 -- un nombre réel a="hello" -- une chaine`
- comme Pascal, LUA veut qu'on ferme les blocs avec end: `function chose(x) if x<10 then return x+10 else return x end end while not quelque do for i=debut,fin do quelque=chose(i) end end`
- voilà, vous savez tout ce qu'il faut pour programmer en LUA ;-). En fait, toutes les fonctions de LUA permettant de faire des choses utiles proviennent de [librairies standard](http://www.lua.org/manual/5.1/manual.html#5) comme math, os et string, ou d'extensions programmées en C comme celles développées dans le cadre du [projet Kepler](http://www.keplerproject.org/).

### Subtilités

- Les variables non initialisées valent "nil". On peut tester si une variable vaut nil.
- On peut appeler une fonction avec moins de paramètres qu'elle n'en accepte. Les paramètres surnuméraires servent donc de paramètres optionnels et prennent la valeur nil, donc on peut leur affecter une valeur par défaut...
- Les fonctions peuvent être référencées par des variables: `function sinus(x) return math.sin(x) end function tabule(f,de,a,pas) -- le paramètre f est une fonction ! for i=de,a,pas do print(i,f(i)) end end tabule(sinus,0,2*math.pi,0.1) -- la fonction est passée en paramètre`
- Les "tables" de LUA sont bien plus sophistiquées que des tableaux ou vecteurs car on peut y combiner des types différents, y compris des fonctions, mettre des tables dans des tables, assigner les indices etc. ce qui permet de créer de puissantes structures de données : `a = { [f(1)] = g; "x", "y"; x = 1, f(x), [30] = 23; 45 }`
- Les [métatables](http://www.lua.org/manual/5.1/manual.html#2.8) sont des tables contenant des références aux fonctions appelées lorsqu'on manipule une variable, que l'on peut "attacher" à celle ci. La variable devient donc un "objet" même si LUA n'est pas un langage "orienté objet" stricto-sensu (très belle "phrase à la con" lue dans Joystick : j'aime bien "stricto-sensu": ça fait karatéka !).
- Avec ce mécanisme, on peut même redéfinir les opérateurs d'addition, de multiplication etc comme avec C++ ! En fait, LUA peut servir aux néophytes que vous êtes à comprendre comment marche la programmation objet. Pour cela, lire dans l'ordre les 3 tutoriels [Object Orientation](http://lua-users.org/wiki/ObjectOrientationTutorial) puis [Metamethods](http://lua-users.org/wiki/MetamethodsTutorial) et enfin [Inheritance](http://lua-users.org/wiki/InheritanceTutorial)
- LUA est en principe multithread grâce au support de coroutines, mais je n'ai pas encore expérimenté ces fonctionnalités...

### Pièges

- LUA est rapide parce qu'il ne vérifie rien, même pas qu'une variable existe (il n'y a pas de "option explicit" comme dans Visual Basic...). Il faut donc être très prudent et utiliser le debug de LuaEdit intensivement: `somme=2+2 print(somne) -- génère une erreur`
- les variables de type "table" sont toujours des références aux tables, et en raison de la complexité potentielle des tables, il n'y a pas de fonction prédéfinie pour copier une table. Donc: `a = { "x", "y"} b=a -- crée une 2ème référence à la table print(b[1]) -- affiche "x" b[1]="modifié!" -- change aussi a[1] !!! print(a[1]) -- affiche "modifié!"`

### Conclusion

- rapide, léger et puissant, LUA est un langage idéal pour être embarqué dans d'autres applications, comme les jeux ou Hyperion.
- Il est moins adapté pour réaliser des applications qui en pilotent d'autres. Python, beaucoup plus riche en librairies sophistiquées et plus robuste au niveau du traitement des exceptions et erreurs semble mieux armé dans ce cas (voir [Lua versus Python](http://lua-users.org/wiki/LuaVersusPython) qui compare avantages/inconvénients de ces 2 langages)

[](http://www.geeks3d.com/20080504/enlighten/)
