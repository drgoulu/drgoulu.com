---
title: '"jeu de l''année" 2012 et autres : c''est fini.'
date: 2012-01-18
draft: false
tags:
  - casse-tetes
  - maths
  - programmation
  - python
categories:
  - Comment
slug: jeu-de-lannee-2012-et-autres-cest-fini
coverImage: ./images/09a817e0eb516e6d72357bbf47b564a3.jpg
---

*(mis à jour plusieurs foirs après correction de bugs et améliorations, cf commentaires...)* 

Je m’apprêtais à passer une soirée tranquille quand je suis tombé sur un tweet de [@ElJj](http://twitter.com/intent/user?screen_name=ElJj) disant: "Qui va me battre au "jeu de l'année" ? [http://eljjdx.canalblog.com/archives/2012/01/15/23243094.html](http://eljjdx.canalblog.com/archives/2012/01/15/23243094.html)".

{{< figure src="./images/09a817e0eb516e6d72357bbf47b564a3.jpg" alt="Python bouffant du matheux" caption="Python bouffant du matheux" width="250" >}}

Un seul click m'a torpillé non pas une, mais trois soirées et un certain nombre d'heures de réflexion la journée. Mais ma vengeance est terrible : ni ElJj ni aucun autre mathématicien ne passera plus jamais des heures à former les entiers de 1 à 100 en n'utilisant que les chiffres de l'année (2,0,1,2) une et une seule fois chacun, les opérations de base +,-,\*,/,^ et quelques autres. Fi-ni. Et c'est rapé aussi pour toutes les années futures ou passées, parce que j'ai fait un programme qui résout ce problème une fois pour toute. Amis [matheux de tous pays](http://mathforum.org/yeargames/), je vous fais ci-dessous économiser des milliers d'heures que vous allez pouvoir utiliser pour résoudre de [vrais problèmes](/2007/04/14/les-problemes-mathematiques-difficiles/) (Pensez à moi si vous en résolvez un, merci...)

Pour être honnête, la première soirée a été grillée à péniblement trouver 50 formules, ce qui m'a à la fois décidé à faire autrement et inspiré beaucoup de respect pour ElJj et les autres fous qui sont parvenus à obtenir des scores de 4000 et quelques points à la main. Bravo !

Pour 2012, mes solutions sont donc : 

| \[1, '(((2\*0)-1)^2)', 0\] \[2, '(((2-0)-1)\*2)', 0\] \[3, '(((2-0)-1)+2)', 0\] \[4, '(((2-0)^1)^2)', 0\] \[5, '(((2-0)+1)+2)', 0\] \[6, '(((2-0)+1)\*2)', 0\] \[7, '((2^0)+((1+2)!))', 0\] \[8, '(2^(0+(1+2)))', 0\] \[9, '(((2-0)+1)^2)', 0\] \[10, '((((2+0!)!)-1)\*2)', 0\] \[11, '(((2+0!)!)+(1/.2))', 1\] \[12, '((((2-0)+1)!)\*2)', 0\] \[13, '(2+sqrt((0!+((1/.2)!))))', 1\] \[14, '((((2+0!)!)+1)\*2)', 0\] \[15, '(((2-0)+1)/.2)', 1\] \[16, '(((2+0!)+1)^2)', 0\] \[17, '(((((2+0!)!)-1)!!)+2)', 5\] \[18, '(((2+0!)!)\*(1+2))', 0\] \[19, '((2^0)+(((1+2)!)!!!))', 5\] \[20, '(((2^0)/.1)\*2)', 1\] \[21, '(((((2+0!)!)!!!)+1)+2)', 5\] \[22, '((((2+0!)+1)!)-2)', 0\] \[23, '((.2^(-(0!+1)))-2)', 1\] \[24.0, '((((2-0)^1)^2)!)', 0\] \[25, '((((2+0!)!)-1)^2)', 0\] \[26, '((((2+0!)+1)!)+2)', 0\] \[27, '((2+0!)^(1+2))', 0\] \[28, '(((2+0!)/.1)-2)', 1\] \[29, '(((2+0!)/\[.1\])+2)', 30\] \[30, '((((2-0)+1)!)/.2)', 1\] \[31, '(((2+0!)/.1)+(Gamma(2)))', 31\] \[32, '(2^(-(0!-((1+2)!))))', 0\] \[33, '((((2+0!)!)!!)-((1/.2)!!))', 11\] \[34, '(sqrt((2^(0!/.1)))+2)', 1\] \[35, '((((2+0!)!)+1)/.2)', 1\] \[36, '((((2-0)+1)!)^2)', 0\] \[37, '(0!+(((1+2)!)^2))', 50\] \[38, '(((((2+0!)!)!!!)+1)\*2)', 5\] \[39, '(((.2^(-0!))!)-(\[.1\]^(-2)))', 31\] \[40, '(((2-0)/.1)\*2)', 1\] \[41, '(0!+(2/(.1/2)))', 51\] \[42, '((((2+0!)!)!!)-((1+2)!))', 5\] \[43, '((((2+0!)!)!!)-(1/.2))', 6\] \[44, '(-((.2-(0!/\[.1\]))/.2))', 32\] \[45, '(((((2+0!)!)!!)-1)-2)', 5\] \[46, '(((((2-0)+1)!)!!)-2)', 5\] \[47, '(((((2+0!)!)!!)+1)-2)', 5\] \[48, '((((2+0!)+1)!)\*2)', 0\] \[49, '((((2+0!)!)+1)^2)', 0\] \[50, '((.2^(-(0!+1)))\*2)', 1\] | \[51, '((.2+(0!/.1))/.2)', 3\] \[52, '(2+(0!/(.1\*.2)))', 2\] \[53, '((((2+0!)!)!!)+(1/.2))', 6\] \[54, '((((2+0!)!)!!!)\*(1+2))', 5\] \[55, '(sqrt((((.2^(-0!))!)+1))/.2)', 2\] \[56, '(((((2+0!)!)+1)!!!)\*2)', 5\] \[57, '((((2+0!)!)!!)+sqrt((\[.1\]^(-2))))', 35\] \[58, '((((2+0!)!)/.1)-2)', 1\] \[59, '((((2+0!)!)/.1)-(Gamma(2)))', 31\] \[60, '(((((2+0!)!)-1)!)/2)', 0\] \[61, '((((2+0!)!)/.1)+(Gamma(2)))', 31\] \[62, '((((2+0!)!)/.1)+2)', 1\] \[63, '((((2+0!)!)!!)+((1/.2)!!))', 11\] \[64, '(2^((0+(1+2))!))', 0\] \[65, '(0!+(2^((1+2)!)))', 50\] \[66, '((((2+0!)!)!!)+(((1+2)!)!!!))', 10\] \[67, '((((.2^(-0!))!!)-\[.1\])/\[.2\])', 66\] \[68, '(20+(((1+2)!)!!))', 15\] \[69, '((((0!+2)!)!!)+21)', 65\] \[70, '(((((2+0!)!)!)\*.1)-2)', 1\] \[71, 'sqrt((((((2+0!)!)+1)!)+(Gamma(2))))', 30\] \[72, 'sqrt((((((2+0!)!)!)\*.1)^2))', 1\] \[73, '(((((2+0!)!)!)\*.1)+(Gamma(2)))', 31\] \[74, '(((((2+0!)!)!)\*.1)+2)', 1\] \[75, '(((((2+0!)!)-1)!!)/.2)', 6\] \[76, '(-((.2^(-0!))-(\[.1\]^(-2))))', 31\] \[77, '((((2^2)!!)!!!)-sqrt((0!/\[.1\])))', 90\] \[78, '((((-2)+(0!/.1))!!!)-2)', 6\] \[79, '(-(2-(0!/(\[.1\]^2))))', 30\] \[80, '(-((.2-0!)/(.1^2)))', 2\] \[81, '((((.2^(-0!))!!!)-1)^2)', 6\] \[82, '(2+(((0!/.1)-2)!!!))', 6\] \[83, '(2+(0!/(\[.1\]^2)))', 30\] \[84, '((((.2^(-0!))!!!)!!!)\*(.1+.2))', 13\] \[85, '(((((2+0!)!)!!!)-1)/.2)', 6\] \[86, '((.2^(-0!))+(\[.1\]^(-2)))', 31\] \[87, '(((2+0!)!)+(\[.1\]^(-2)))', 30\] \[88, '(-((((2+0!)!)!)\*(.1-\[.2\])))', 31\] \[89, '(-((.2-((sqrt((0!/\[.1\]))!)!!!))/.2))', 37\] \[90, '(((((2-0)+1)!)!!!)/.2)', 6\] \[91, '(((.2^(-0!))!!!)+(\[.1\]^(-2)))', 36\] \[92, '(2\*(((sqrt((0!/\[.1\]))!)!!)-2))', 35\] \[93, '93', 500\] \[94, '(-(((2+0!)!)-(.1^(-2))))', 1\] \[95, '(-((.2^(-0!))-(.1^(-2))))', 2\] \[96, '(-((.2-0!)\*((1/.2)!)))', 2\] \[97, '(-(2+(0!-(.1^(-2)))))', 1\] \[98, '(-(2-(0!/(.1^2))))', 1\] \[99, '(-((2^0)-(.1^(-2))))', 1\] \[100, '(((2^0)/.1)^2)', 1\] |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

C'est un peu "brut de décoffrage" et mérite quelques explications. Chaque triplet comporte le nombre à obtenir, la "meilleure" formule qui le donne, et le coût de cette formule en points calculés selon les règles décrites dans l'article d'El Jj. Les formules qui utilisent les chiffres 2,0,1,2 dans l'ordre et les opérations arithmétiques de base et la factorielle (saviez-vous que 0!=1 ?) ont le coût minimum de 0. L'utilisation du point décimal bien utile avec une division ne coute qu'un point. Les formules qui utilisent des opérateurs plus compliqués comme les [multifactorielles](w:en:Factorial#Multifactorials) (notées !! et !!!) et la [fonction gamma](w:) sont pénalisées de 5 points.

La formule pour 77 est la plus coûteuse (90 points) car elle utilise les chiffres dans le désordre (50 points), le développements décimal périodique \[.1\] = 0.11111111... = 1/9 qui vaut 30 points chacun, plus deux multifactorielles. A noter que l'on a eu besoin d'inverser l'ordre des chiffres que dans 4 cas seulement.

Et enfin, les nombre pour lesquels on ne trouve pas de solution sont pénalisés de 500 points, ce qui n'est le cas pour 93, pour lesquel je suis quasi certain qu'il n'existe pas de solution avec les opérations autorisées. Mais seulement "quasi", pour des raisons que j'explique plus loin.

Le total des pénalités que j'obtiens est de 1637 points

Enfin, les formules ne sont pas très jolies d'une part à cause d'une "surparenthésation" qui simplifie l'écriture du programme (pas besoin de gérer la [précédence des opérateurs](w:Ordre_des_opérations#En_informatique)), et d'autre part car le choix de la "meilleure" formule lorsqu'on en trouve plusieurs de score égal se fait par la longueur de la chaîne, sans tenir compte de l'ordre d'insertion ou de la priorité des opérateurs. Donc (((2\*0)-1)^2) peut paraître plus compliqué que (((2\*0)-1)+2) pour obtenir 1, mais pour une machine, c'est le même prix.

Comme il se fait tard je coupe/colle le programme ci-dessous, je le commenterai plus tard (comme d'hab...)

{{< highlight python >}}

# -_- coding: utf-8 -_-

"""
Created on Mon Jan 16 17:19:27 2012

@author: Philippe Guglielmetti
solves
http://eljjdx.canalblog.com/archives/2012/01/15/23243094.html
"""

import sys

from math import sqrt,pow
from scipy import factorial,factorial2,factorialk
from itertools import permutations

class f:
"""a formula"""
def **init**(self, m,p=0,v=None,parenthesis=False):
#print m,'=',
self.isdigit=isinstance(m, (int, long))
self.math=str(m) #convert to string in case it's a digit
self.points=p
if v is None:
v=eval(self.math)
self.isint=isinstance(v, (int,long))
if isinstance(v, float): #try to convert to int
self.isint=abs(v-round(v))<1e-9
if self.isint:
v=int(round(v))
if isinstance(v, long): #we don't want bignums, for performance
if abs(v)<sys.float_info.max:
v=float(v)
self.isint=True
self.value=v

        if parenthesis:
            self.math='('+self.math+')'
        #print self.value

    def __cmp__(self,other):
        if self.value<other.value:return -1
        if self.value>other.value:return +1
        if self.points<other.points:return -1
        if self.points>other.points:return +1
        if len(self.math)<len(other.math):return -1
        if len(self.math)>len(other.math):return +1
        return 0

    def __repr__(self):
        return str([self.value,self.math,self.points]);

class results(dict):
"""dictionary of formulas indexed by their result. we keep only the simplest entry for each result"""

    def __init__(self):
        dict.__init__(self)

    def add(self, f):
        if f.value in self.keys() and f>self[f.value] :
            pass
        else:
            self[f.value]=f

    def merge(self,d):
        for i in d.itervalues():
            self.add(i)

    def score(self):
        return sum(map(lambda x: x.points,self.itervalues()))

    def notfound(self,p=500):
        return [i for (i,v) in self.iteritems() if v.points>=p]

    def refine(self,recurse=2):
        """add combinations of monadic operators"""
        r=results()
        for a in self.itervalues():
            if recurse==0 and a.value<>0:
                r.add(f('-'+a.math,a.points,-a.value,True))
            if a.isint:
                if a.value==0:
                    r.add(f(a.math+'!',a.points,1)) # 0! == 1 is very useful...
                if a.value>1:
                    s=f('sqrt('+a.math+")",a.points,sqrt(a.value))
                    if s.isint:
                        r.add(s)
                if a.value>1 and a.value<19:
                    r.add(f(a.math+'!',a.points,factorial(int(a.value),True),True))
                    r.add(f('Gamma('+a.math+')',a.points+30,factorial(int(a.value)-1,True),True))
                if a.value>3 and a.value<29:
                    r.add(f(a.math+'!!',a.points+5,factorial2(int(a.value),True),True))
                if a.value>4 and a.value<39:
                    r.add(f(a.math+'!!!',a.points+5,factorialk(int(a.value),3,True),True))
        self.merge(r)
        if recurse>0: self.refine(recurse-1)

class monadic(results):
"""combinations of monadic operators around a formula"""

    def __init__(self, a):
        results.__init__(self)
        self.add(a)
        if a.value!=0:
            if a.isdigit:
                self.add(f('.'+a.math,a.points+1))
            if a.value<10:
                self.add(f('[.'+a.math+']',a.points+30,a.value/9.))
        self.refine();

class diadic(results):
"""combinations of diadic operators of 2 operands"""

    def __init__(self, a,b):
        results.__init__(self)
        for i in a.itervalues():
            for j in b.itervalues():
                if i.isdigit and j.isdigit:
                    if i.value!=0: self.add(f(int(i.math+j.math),10))
                    self.add(f(i.math+'.'+j.math,11))
                self.add(f(i.math+'+'+j.math,i.points+j.points,i.value+j.value,True))
                self.add(f(i.math+'-'+j.math,i.points+j.points,i.value-j.value,True))
                self.add(f(i.math+'*'+j.math,i.points+j.points,i.value*j.value,True))
                if j.value!=0:
                    self.add(f(i.math+'/'+j.math,i.points+j.points,float(i.value)/float(j.value),True))
                try: #so many things can go wrong with next line...
                    self.add(f(i.math+'^'+j.math,i.points+j.points,pow(i.value,j.value),True))
                except:
                    pass
                if i.isint:
                    try: #so many things can go wrong with next line...
                        self.add(f('root('+i.math+','+j.math+')',i.points+j.points+5,pow(j.value,1./i.value),True))
                    except:
                        pass
                if i.isint and j.isint and i.value>=0 and j.value>0 and i.value/j.value<10:
                    try: #so many things can go wrong with next line...
                        self.add(f(i.math+'!'+j.math,i.points+j.points+5,factorialk(i.value,j.value),True))
                    except:
                        pass

        self.refine();

print 'building list of monadics'
m=map(monadic,map(f,range(0,10))) #list of all monadics of digits

#use @Memoized here to improve performance
def d(a,b): return diadic(a,b)

def year(n,display=True,verbose=True):
solution=results()
for i in range(1,101):
solution.add(f(i,500))

    def addresults(a,p):
        if verbose :
            print 'formulas',len(a),
        improved=0
        found=0
        for (i,v) in a.items():
            if isinstance(i, (int, long)) and i>0 and i<101:
                v.points+=p
                if v<solution[i]:
                    if solution[i].points==500:
                        found+=1
                    else:
                        improved+=1
                    solution[i]=v
        if verbose:
            print('found :'+str(found)+' improved :'+str(improved)+' score:'+str(solution.score()))

    def combine (a,p):
        m0=m[a[0]]; m1=m[a[1]]; m2=m[a[2]]; m3=m[a[3]]
        if solution.notfound():addresults(d(d(d(m0,m1),m2),m3),p)
        if solution.notfound():addresults(d(d(m0,d(m1,m2)),m3),p)
        if solution.notfound():addresults(d(m0,d(m1,d(m2,m3))),p)
        if solution.notfound():addresults(d(m0,d(d(m1,m2),m3)),p)
        if solution.notfound():addresults(d(d(m0,m1),d(m2,m3)),p)

    y=[int(i) for i in str(n)]
    combine(y,0)
    y.sort()
    for i in permutations(y):
        combine(i,50)

    if display:
        for i in solution.itervalues():print i
    print n,solution.score(),solution.notfound()

year(2012)
{{< /highlight >}}
