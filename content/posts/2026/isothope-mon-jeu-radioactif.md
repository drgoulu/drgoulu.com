---
title: ISOThOPE, "mon" jeu radioactif
date: 2026-11-06
draft: true
tags:
  - jeu
  - radioactivite
  - vibe coding
categories:
  - comment
slug: ''
coverImage: ''
---

C'est une vieille idée que j'avais eue en écrivant "[comment transformer du plomb en or](/2013/03/15/comment-transformer-le-plomb-en-or/)" puis [plusieurs](/2023/04/27/est-il-possible-de-modifier-le-nombre-de-protons-d-un-atome-si-oui-cela-est-il-possible-alors-de-transformer-le-plomb-en-or/) [réponses](/2025/05/12/que-penser-des-physiciens-du-cern-qui-ont-reussi-a-transformer-du-plomb-en-or-malheureusement-pour-une-fraction-de-seconde-certes-mais-est-ce-une-avancee-spectaculaire/) [sur](/2020/02/15/peut-on-fabriquer-de-l-or-en-laboratoire/) [Quora](/2020/09/02/peut-on-obtenir-de-l-or-numero-atomique-79-en-bombardant-deux-autres-elements-par-exemple-ba-56-avec-va-23/) : créer un jeu basé sur la transmutation des isotopes.

Un bon coup de vibe coding plus tard, c'est fait, vous pouvez jouer à [ISOThOPE sur itch.io](https://uluog.itch.io/isothope) ou [sur GitHub](https://goulu.github.io/isotope/), où se trouve aussi le [code source](https://github.com/goulu/isotope).

## Manuel

Bienvenue dans **ISOThOPE**, le jeu de puzzle et de transmutation nucléaire basé sur les données scientifiques réelles de l'AIEA (NUBASE / LiveChart).

### 🎯 1. But du jeu

Vous contrôlez un noyau atomique représenté au centre de la [**carte de Segrè**](w:Carte_des_nucléides) (le tableau périodique des physiciens nucléaires) :

- L'axe horizontal représente le nombre de neutrons (`N`).
- L'axe vertical représente le nombre de protons (`Z`), qui définit l'élément chimique.

Dans chaque niveau, vous partez d'un **isotope initial** et devez atteindre un **isotope cible** (repéré par un cadre doré sur la grille) en utilisant judicieusement vos particules et les désintégrations radioactives naturelles.

> **Astuce :** Laissez parfois la nature travailler pour vous ! Une désintégration radioactive gratuite économise vos précieuses particules.

### ⚡ 2. Actions et contrôles

Utilisez les boutons situés sous la grille pour bombarder votre noyau avant qu'il ne se désintègre :

| Action | Effet sur le noyau | Déplacement sur la grille | Raccourci PC |
| --- | --- | --- | --- |
| **⚛ +n** (Neutron) | Ajoute 1 neutron (`N + 1`) | **➔ Droite** (même élément, plus lourd) | `N` ou `→` |
| **⚡ +e⁻** (Électron) | Capture électronique (`Z - 1, N + 1`) | **↘ Diagonale bas-droite** | `E` ou `↓` |
| **🔴 +p** (Proton) | Ajoute 1 proton (`Z + 1`) | **↑ Haut** (élément suivant) | `P` ou `↑` |
| **Recommencer** | Réinitialise le niveau en cours | Retour au noyau de départ | `R` |

### ☢️ 3. Stabilité et désintégrations radioactives

Chaque case de la grille est colorée selon le comportement physique réel de l'isotope :

- **⬛ Noir (Stable)** : Le noyau ne se désintègre pas. Le chronomètre s'arrête et vous avez tout le temps de réfléchir. _Attention : si vous atterrissez sur un isotope stable qui n'est pas la cible et que vous n'avez plus de particules, la partie est perdue !_
- **🟦 Bleu (β⁻ — Bêta moins)** : Excès de neutrons. Un neutron se transforme en proton (`Z + 1, N - 1` ➔ déplacement en **↖ diagonale haut-gauche**).
- **🟧 Orange (β⁺ / ε — Bêta plus ou Capture électronique)** : Excès de protons. Un proton se transforme en neutron (`Z - 1, N + 1` ➔ déplacement en **↘ diagonale bas-droite**).
- **🟨 Jaune (α — Alpha)** : Noyau lourd qui éjecte une particule alpha (`⁴He`) composée de 2 protons et 2 neutrons (`Z - 2, N - 2` ➔ recul de **↙ 2 cases en bas à gauche**).
- **🟥 Rouge (p — Émission de proton)** : Noyau extrêmement riche en protons qui éjecte directement 1 proton (`Z - 1` ➔ **↓ 1 case vers le bas**).
- **🟪 Violet (n — Émission de neutron)** : Noyau extrêmement riche en neutrons qui éjecte directement 1 neutron (`N - 1` ➔ **← 1 case vers la gauche**).
- **🟩 Vert (SF — Fission spontanée)** : Le noyau trop lourd se brise spontanément.

### 🧭 4. Niveaux et Mode Libre (Niveau 0)

- **Explications du niveau** : Cliquez n'importe où sur le **bloc de description du niveau** (situé sous la barre de titre) pour ouvrir le briefing scientifique et historique de la mission.
- **Sélecteur de niveaux** : Cliquez sur le bouton numéroté (ex. `1/13`) à gauche du bloc de niveau pour changer de mission.
- **Niveau 0 — Mode Libre (Sandbox)** : Accessible tout en haut de la liste des niveaux, il vous offre des particules illimitées (`∞`) et vous permet de cliquer directement sur n'importe quelle case de la grille ou de la bannière `ISOThOPE` pour explorer la carte des nucléides.

### 📈 5. La Loi Logarithmique du Temps

Dans la réalité, les demi-vies (`T½`) des isotopes s'étendent de quelques microsecondes (`10⁻⁶ s`) à plusieurs milliards d'années (`10¹⁷ s`). Pour compresser ces 23 ordres de grandeur en quelques secondes de jeu tout en respectant l'ordre de stabilité réel de chaque isotope, **ISOThOPE** applique une loi logarithmique :

`Temps_Jeu = clamp(Base + Pente × log10(T½), Min, Max)`
