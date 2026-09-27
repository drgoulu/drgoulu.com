---

title: Est-il possible qu'un hacker malveillant, ou hacker éthique si test, passe d'une VM (machine virtuelle) à l'autre, après avoir réussi à entrer dans le réseau virtuel d'une machine physique ? Peut-on éviter ça ? (Windows, Linux…)
slug: est-il-possible-qu-un-hacker-malveillant-ou-hacker-ethique-si-test-passe-d-une-vm-machine-virtuelle-a-l-autre-apres-avoir-reussi-a-entrer-dans-le-reseau-virtuel-d-une-machine-physique-peut-on-eviter-ca-windows-linux
date: '2025-08-12'
draft: true
categories:
- Quora
tags: []
coverImage: ./images/quora.png
---

*Réponse publiée [sur Quora](https://fr.quora.com/Est-il-possible-qu-un-hacker-malveillant-ou-hacker-%C3%A9thique-si-test-passe-d-une-VM-machine-virtuelle-%C3%A0-l-autre-apr%C3%A8s-avoir-r%C3%A9ussi-%C3%A0-entrer-dans-le-r%C3%A9seau-virtuel-d-une-machine-physique/answer/Dr-Goulu)*

Absolument. Pire encore, une [Blue Pill](w:en:Blue_Pill_(software))peut virtualiser votre OS sans que vous ne vous en rendiez compte, intercepter absolument tour ce que vous faites et être quasi indétectable.

Lisez cet article édifiant :

[https://korben.info/joanna-rutko...](https://korben.info/joanna-rutkowska-blue-pill-qubes-os-histoire-complete.html)

Le seul (?) moyen d'éviter ça est d'utiliser [Qubes OS](w:), un os compartimenté en beaucoup de machines virtuelles.
