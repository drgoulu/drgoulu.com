---
title: Comment les premier ordinateurs ont compris les alphabets les chiffres que tel touches correspond à tel caractere etc?
slug: comment-les-premier-ordinateurs-ont-compris-les-alphabets-les-chiffres-que-tel-touches-correspond-a-tel-caractere-etc
date: '2021-02-26'
draft: false
categories:
- Comment
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Comment-les-premier-ordinateurs-ont-compris-les-alphabets-les-chiffres-que-tel-touches-correspond-%C3%A0-tel-caractere-etc/answer/Dr-Goulu)*

Les ordinateurs n'ont jamais rien compris. (ou pas encore)

On les a construits pour manipuler des groupes de bits, des "octets" de 8 bits dans les ordinateurs modernes (=des années 70...)

On a créé des tables de correspondance entre certains octets et des caractères, le système le plus connu est l'ASCII

[American Standard Code for Information Interchange](w:American_Standard_Code_for_Information_Interchange)

Par exemple le "a" correspond à 01100001

Quand vous pressez la touche "a" de votre clavier, ces 8bits sont transmis à l'ordinateur. Le programme qui gère le clavier range les octets successifs en mémoire les uns après les autres, formant une

[Chaîne de caractères](w:Chaîne_de_caractères)

Qui peut être traitée par un programme qui "sait" que cette mémoire contient des caractères, et pas des nombres à additionner par exemple. C'est la programmation qui permet de distinguer les différents types de données (nombre entier, nombre flottant, caractères, image, code (un programme est ausdi formé d'octets…))

[Type (informatique)](w:Type_\(informatique\))
