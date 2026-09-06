---
title: "Comment dire 33 avec 3 cubes ?"
slug: "comment-dire-33-avec-3-cubes"
date: 2012-06-20
categories:
  - "Comment"
tags: 
  - "algorithmes"
  - "casse-tetes"
  - "informatique"
  - "nombres"
  - "python"
coverImage: "9b493f196263e591d63658b2997f5b5b.jpg"
---

Le gars qui m'a pourri ma dernière soirée du printemps s'appelle Mike Croucher. [Sur son blog "Walking Randomly"](http://www.walkingrandomly.com/?p=4353) il a négligemment posé le problème suivant:

> Il est possible d'écrire beaucoup d'entiers comme la somme des cubes de 3 entiers, par exemple: 99 = (-5)^3 + 2^3+ 6^3 Un exemple plus compliqué est: 91 = (-67134)^3 + (-65453)^3+(83538)^3 Votre tâche est de trouver les entiers x,y, et z tels que: 33 = x^3 + y^3 + z^3

Comme j'ai bien vu que la solution pour 91 impliquait de grands entiers, je me suis dit que 33 demanderait probablement des nombres encore plus grands, mais j'ai quand même vite pondu le programme Python suivant pour voir:

{{< highlight python >}}
res={} #dictionary of results
def store(n,x,y,z):
    if n>=0 and n<100 and n not in res:
        res[n]=(x,y,z)
        print n,res[n]

cube=[]
x=0
while True:
    x3=x*x*x
    cube.append(x3)
    for y in range(x+1):
        y3=cube[y]
        for z in range(x+1):
            z3=cube[z]
            store(x3+y3+z3,x,y,z)
            store(x3-y3+z3,x,-y,z)
            store(x3+y3-z3,x,y,-z)
            store(x3-y3-z3,x,-y,-z)
            store(-x3+y3+z3,-x,y,z)
            store(-x3-y3+z3,-x,-y,z)
            store(-x3+y3-z3,-x,y,-z)
            # store(-x3-y3-z3,-x,-y,-z) #you're right Neamar, it's useless
    x+=1
    if x==50: #show "small" results
        for n in range(100):
            if n in res:
                print n,res[n]
            else:
                print n,'?'
{{< /highlight >}}

En moins d'une seconde il trouve les 69 des 100 premiers entiers qui sont des sommes de cubes d'entiers inférieurs à 100. Le plus "compliqué" est 78=-55³+53³+26³ .

Ensuite il mouline pendant des heures pour trouver 51=-796³+659³+602³ et 16=1626³-1609³-511³, et pendant ce temps j'ai exploré les liens émaillant les premiers commentaires [de l'article de "Walking Randomly"](http://www.walkingrandomly.com/?p=4353).

Il s'avère que le problème soumis par Mike Croucher est extrêmement difficile, voire impossible. [Cette page](http://www.asahi-net.or.jp/~KC2H-MSM/mathland/math04/matb0100.htm) liste les solutions trouvées par mon programme, et d'autres qui ont nécessité des algorithmes beaucoup plus fûtés que le mien pour résoudre cette [équation diophantienne](w:) :

- 87 = 4271³ - 4126³ - 1972³ , découvert en 1964 [[1]](#ref-1)
- 96 = -15250³ + 13139³ + 10853³
- 91 = 83538³ - 67134³ - 65453³
- 80 = -112969³ + 103532³ + 69241³
- 39 = -159380³ + 134476³ + 117367³ découvert en 1991 [[2]](#ref-2)
- 75 = - 435203231³ + 435203083³ + 4381159³  découvert en 1993 [[3]](#ref-3)
- 84 = 41639611³ - 41531726³ - 8241191³ découvert en 1994 [[4]](#ref-4)
- 30 =  2220422932³ - 2218888517³ - 283059965³ ainsi que 52 = -61922712865³ + 60702901317³ + 60702901317³ par la même équipe, qui a mis au point l'algo le plus performant du moment [[5]](#ref-5)
- 24 =15584139827³ - 15550555555³ - 2901096694³ a été découvert avec l'algo précédent en 2001 par D. J. Bernstein, dont la page [http://cr.yp.to/threecubes.html](http://cr.yp.to/threecubes.html) est consacrée à ce problème et son historique

A part ça, les matheux démontrent (essayez...) que les nombres de la forme 9n+4 et 9n+5 ne peuvent pas être la somme de trois cubes, ce qui règle le cas de 4,5,13,14,22,23 etc.

{{< figure src="images/9b493f196263e591d63658b2997f5b5b.jpg" alt="Bon... je n ai pas vraiment le droit d'utiliser ce dessin, mais il va tellement bien là que j espère que vous ne m en voudrez pas, cher Docteur G..." caption="Bon... je n ai pas vraiment le droit d'utiliser ce dessin, mais il va tellement bien là que j espère que vous ne m en voudrez pas, cher Docteur G..." link="http://www.geluck.com/" align="aligncenter" width="412" >}}

Reste 33 (et 42 et beaucoup d'autres), qui résistent effrontément aux informaticiens cherchant à les obtenir, ainsi qu'aux mathématiciens essayant de prouver que c'est peine perdue...

C'est énervant qu'un petit problème tout bête comme celui-ci puisse résister ainsi aux ordinateurs les plus puissants.  Et motivant de penser qu'une solution est peut-être à la portée d'amateurs éclairés. Des idées ?

### Références:

1. <span id="ref-1"></span>Gardiner, V. L., Lazarus, R. B., & Stein, P. R. "[Solutions of the diophantine equation x^3+z^3=z^3-d](http://cr.yp.to/bib/1964/gardiner.pdf). ", 1964, Mathematics of Computation, 18, 408-413
2. <span id="ref-2"></span>Heath-Brown, D. R., Lioen, W. M., & te Riele, H. J. J."[On Solving the Diophantine Equation $x^3 + y^3 + z^3 = k$ on a Vector Computer](http://cr.yp.to/bib/1993/heath-brown-solving.pdf)", 1993, Mathematics of Computation, 61, 235-244
3. <span id="ref-3"></span>Andrew Bremner, "[On sums of three cubes](http://cr.yp.to/bib/1995/bremner.html)", 1993
4. <span id="ref-4"></span>B. Conn and L. Vaserstein, "On sums of three integral cubes", 1994, Contemp. Math. 166, 285-294.
5. <span id="ref-5"></span>Eric Pine, Kim Yarbrough, Wayne Tarrant and Michael Beck, Noam D. Elkies, "[Rational points near curves and small nonzero |x3\-y2| via lattice reduction](http://arxiv.org/pdf/math.NT/0005139.pdf)", 2000, ANTS IV
6. <span id="ref-6"></span>Michael Beck, Eric Pine, Wayne Tarrant, Kim Yarbrough Jensen "New integer representations as the sum of three cubes", 2007, Math. Comp. 76, 1683-1690 ([page AMS](http://www.ams.org/journals/mcom/2007-76-259/S0025-5718-07-01947-3/))
7. <span id="ref-7"></span>{{< openbook booknumber="ISBN:978-0444866622" templatenumber="5" >}} ([online](http://www.scribd.com/mdrougui/d/53093903/87-Sums-of-three-cubes))
