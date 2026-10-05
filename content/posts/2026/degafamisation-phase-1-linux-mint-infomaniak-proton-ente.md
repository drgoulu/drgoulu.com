---
title: 'DeGAFAMisation Phase 1 : Linux Mint, Infomaniak, Proton, Ente'
date: 2026-10-04
draft: true
tags:
  - GAFAM
  - Linux
  - informatique
categories:
  - Comment
slug: ''
coverImage: https://images.frandroid.com/wp-content/uploads/2025/11/gemini-generated-image-l4o6mtl4o6mtl4o6-768x429.jpg
---

## Adieu Windows

Dès sa sortie en 1985, j'ai trouvé [Microsoft Windows](w:) gros et moche. Je travaillais l'été dans une boutique qui vendait des Apple [Macintosh](w:) puis des Commodore [Amiga](w:), et Windows était juste gros et moche en comparaison. 

Mais surtout, en Suisse on avait le  [Smacky 8](https://www.smaky.ch/chapitre-4-smaky-8/) dès 1981 déjà, avec système multitâche et interface graphique. Windows était gros, moche, et arriéré.

Windows n'a pas arrêté de devenir encore plus gros à force de copier les autres, très gourmand en ressources pour tenter d'être beau, et depuis peu il est devenu intrusif en plus en forçant l'adoption d'outils gros et moches comme Internet Explorer puis Edge, et maintenant l'IA Copilot.

Mais surtout il est devenu instable et non fiable. En revenant de voyage, après une mise à jour majeure, mon "vieux" PC de bureau n'a plus démarré. Ca c'est résolu en mettant  `BypassSecureBootCheck` et `BypassTPMCheck`dans le registre, mais quel utilisateur lambda sait faire ça ? Et jusqu'à quand ça va marcher ?

## Bonjour Linux (Mint)

Le bon côté de ce problème, ça a été de justifier l'achat d'un nouveau PC il y a un an.  Un laptop Asus Tuf Gaming A15. Le dernier du magasin, modèle d'exposition, avec rabais. Le vendeur me dit de repasser le lendemain car il doit réinitialiser Windows. Je lui dis non, je le prends comme ça parce que je vais installer Linux. Il me fait un grand sourire, me dit "bienvenue au club" et me fait encore un rabais !

J'avais déjà touché un peu Linux, notamment il y a vingt ans pour installer un serveur pour ma jeune boîte sur ma seule machine bi-processeur, que Windows 2000 ne savait pas gérer. Il m'aurait fallu dépenser une somme astronomique pour un Windows NT Server, j'avais donc choisi un Linux, Ubuntu je crois, ramé quelques jours à installer un serveur Samba avec toutes les permissions, un serveur d'email et quelques autres trucs, et puis il y a eu un incendie qui a tout détruit ...

J'étais donc un peu inquiet quand même en installant [Linux Mint](w:), une distribution choisie pour la similitude de l'interface avec celle de Windows, parce qu'après 40 ans, c'est difficile de changer ses habitudes...

Et c'est passé comme une lettre à la poste. Depuis plus dun an je n'utilise plus que Linux et ses logiciels libres, sans aucun problème ni regret. Au point que j'ai carrément viré la partition Windows du laptop, et installé aussi Mint sur mon "vieux" PC de bureau en ne gardant qu'un Windows minimal fait avec [Tiny11 builder](https://github.com/ntdevlabs/tiny11builder) "au cas où".

### Ya même les jeux ! (Wine, Proton, Steam ...)

La vraie raison pour laquelle je n'ai plus retouché à Linux en 20 ans , ce sont les jeux. "Hardcore Gamer", j'avais absolument besoin d'un système capable de faire tourner les derniers jeux, et Linux ne l'était pas, ou pas facilement.

Puis il y a eu [Wine](w:), qui signifiait initialement "WINdows Emulator", mais maintenant c'est "Wine Is Not an Emulator", parce que de fait c'est une couche de compatibilité qui permet à des logiciels Windows de tourner sur Linux. Même le vénérable [wpanorama](http://www.wpanorama.com/wpanorama.php) écrit en Delphi il y a un certain temps fonctionne sans anicroche :

{{< figure link="http://www.wpanorama.com/wpanorama.php" src="./images/497db1a8-a3e9-4def-a2bd-e4c76c6952dc.jpeg" >}}

Mais surtout, il y a [Steam](w:) et son [Proton](w:Proton_\(logiciel\))
