---
title: "La reconnaissance vocale est morte : pet à son âme."
slug: "la-reconnaissance-vocale-est-morte"
date: 2010-06-26
categories: 
  - "cat3"
  - "cat2"
tags: 
  - "futur"
  - "informatique"
  - "traduction"
coverImage: "9a440aa4e1cd0fe13d8938d79cc00f26.jpg"
---

D'après "2001 l'Odyssée de l'Espace", nos ordinateurs devraient comprendre notre voix depuis 9 ans. Depuis 1997, on trouve des logiciels de reconnaissance vocale pour PC, et depuis peu nos téléphones disposent de cette fonction. Mais on ne l'utilise pas. Je ne connais personne qui dicte ses e-mails, et vous ?

Comme tous les geeks j'ai essayé de temps en temps, parfois passé une heure à lire des textes d'apprentissage de la voix la plus monocorde possible à la nouvelle version d'un soft, et puis abandonné devant ses piètres performances. Ca ne marche pas, ou pas assez bien.

Robert Portner analyse cet échec dans  "[Rest in Peas: The Unrecognized Death of Speech Recognition](http://robertfortner.posterous.com/the-unrecognized-death-of-speech-recognition)", titre subtilement traduit en français dans le présent article.

Le problème, c'est qu'après une phase de progrès rapides à la fin du siècle passé, le [taux d'erreur de mots](w:) plafonne à 10% depuis 2001 , soit environ le triple du taux d'erreur d'un être humain. Et encore, c'est pour l'anglais "standard". Le taux d'erreur est bien plus élevé pour d'autres langues, et catastrophique pour une conversation entre supporters de foot à la sortie du match.

{{< figure src="images/892b91f37608e5959549c3c4a87512f4.png" alt="NIST_Benchmarks_revised.jpg.scaled1000" caption="Source: National Institute of Standards and Technology Benchmark Test History (1)" link="http://www.itl.nist.gov/iad/mig/publications/ASRhistory/index.html" align="aligncenter" width="480" >}}

Pourtant dans les années 1990, des systèmes très fiables avaient été mis au point pour distinguer quelques mots bien choisis dans des cockpits d'avion ou des chiffres au téléphone, et on s'était légitimement attendus à ce que la Loi de Moore permette de traiter rapidement le langage naturel. Et effectivement, aujourd'hui on sait bien reconnaitre des mots isolés. On sait à peu près éliminer les absurdités non conformes à la grammaire dans des phrases simples comme "le chat ment je la sous rit." Mais pour distinguer entre "le chas mange la souris", "le chat mange là, sous l'riz" et  "le chaman gela, sourit" et , il faut comprendre le sens de la phrase, voire le contexte dans lequel elle est prononcée...

Si l'ordinateur doit connaitre la différence entre un quadrupède carnivore et le trou d'une aiguille pour traiter une phrase triviale, on imagine que ce n'est pas demain qu'on dictera des contrats\* ou des rapports à une machine.  De gros projets ont été lancés par des poids lourds de l'informatique pour tenter de modéliser la connaissance humaine. Par exemple le projet MindNet de Microsoft [[2]](#ref-2) a analysé des millions de pages de textes existants pour construire un graphe sémantique gigantesque, duquel il ressort effectivement que dans une phrase comportant "chat" et "souris", [le plus probable est que le chat chasse la souris](http://stratus.research.microsoft.com/mnex/ShowPath.aspx?l=e&d=d&from=cat&to=mouse). Un tel graphe peut certainement être utile en [traduction automatique](/2009/05/14/tels-que-le-corbeau-le-renard/) car on dispose d'un texte de départ, mais pour la reconnaissance vocale il faudrait étendre le graphe à la structure des phrases utilisées en conversation courante, qui peut être bien distincte du langage écrit. Et pour faire ça automatiquement, il faudrait la reconnaissance vocale...

Comme le note Portner, on pensait au début que la reconnaissance vocale était un premiers pas vers l'intelligence artificielle. Aujourd'hui de nombreux chercheurs estiment que l'intelligence artificielle est indispensable pour atteindre une reconnaissance vocale de qualité acceptable [[2]](#ref-2). Les gros projets de recherche ont été abandonnés les uns après les autres, bloqués devant le mur si bien décrit par les [Perlisismes](/2008/01/21/perlisismes-les-dictons-informatiques-dalan-perlis/) sur l'intelligence artificielle comme:

> "Une année de travail sur l’intelligence artificielle est suffisante pour vous faire croire en Dieu"

Le nombre de recherches sur "reconnaissance vocale" ou "[Dragon Naturally Speaking](http://www.nuance.com/dragon/index.htm)" sur Google  baisse régulièrement depuis 2001. Comme aucune  idée fondamentalement nouvelle ne vient relancer la recherche, la reconnaissance vocale est morte, en toute discrétion.

Note\* : me rappelle l'histoire de la secrétaire d'un célèbre ingénieur de la génération disctaphone qui avait commandé "310 mètres d'isolation entre 2 étages" au lieu de "3 centimètres" . Ca c'est avec les 2% d'erreurs de transcription humaines...

### Références:

1. <span id="ref-1"></span>[The History of  Automatic Speech Recognition Evaluations at NIST](http://www.itl.nist.gov/iad/mig/publications/ASRhistory/index.html)
2. <span id="ref-2"></span>Microsoft Research : [MindNet](http://research.microsoft.com/en-us/projects/mindnet/)
3. <span id="ref-3"></span>Janet M. Baker et al. " [Research Developments and Directions inSpeech Recognition and Understanding](http://research.microsoft.com/pubs/80528/SPM-MINDS-I.pdf)", IEEE Signal Processing Magazine \[75\] MAY 2009
