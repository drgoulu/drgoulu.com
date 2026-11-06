---
title: 'ISOThOPE, "my" radioactive game'
date: 2026-11-06
draft: false
tags:
  - game
  - radioactivity
  - vibe coding
categories:
  - comment
slug: 'isothope-my-radioactive-game'
coverImage: ./images/isothope.png
---

It's an old idea I had while writing "[how to turn lead into gold](/2013/03/15/comment-transformer-le-plomb-en-or/)" and later [several](/2023/04/27/est-il-possible-de-modifier-le-nombre-de-protons-d-un-atome-si-oui-cela-est-il-possible-alors-de-transformer-le-plomb-en-or/) [answers](/2025/05/12/que-penser-des-physiciens-du-cern-qui-ont-reussi-a-transformer-du-plomb-en-or-malheureusement-pour-une-fraction-de-seconde-certes-mais-est-ce-une-avancee-spectaculaire/) [on](/2020/02/15/peut-on-fabriquer-de-l-or-en-laboratoire/) [Quora](/2020/09/02/peut-on-obtenir-de-l-or-numero-atomique-79-en-bombardant-deux-autres-elements-par-exemple-ba-56-avec-va-23/): creating a simple little game based on the transmutation of isotopes.

It sounds complicated when put like that, but basically you just click one, two, or maybe three buttons in the right sequence to transmute one element into another. The only difficulty is that it decays on its own during the game, following the laws of physics. Well, almost, because...

A good dose of vibe coding later, it's done: you can play [ISOThOPE on itch.io](https://uluog.itch.io/isothope) or [on GitHub](https://goulu.github.io/isotope/), where you can also find the [source code](https://github.com/goulu/isotope).

I put "my" game in quotes because honestly, I didn't code a single line of this game. I defined myself as designer and product owner in [AGENTS.md](https://github.com/goulu/isotope/blob/master/AGENTS.md), and Gemini did the rest.

Even the title! When I asked Gemini to create the title "Isotope" using tiles representing chemical elements, it suggested "ISOThOPE"? Because oddly enough, there is no element "T", nor "To" or "Ot". And because [thorium is fantastic](/2013/05/18/latome-vert-le-thorium/)...

{{< figure align="aligncenter" src="./images/isothope%20game.png" >}}

Even the manual (below) is the AI's work, and it completely blows me away because it aggregates several of the "prompts" I used during development, genuinely giving the impression of "understanding" the game. Gemini even went so far as finding out that my "isotope map" is called a [Segrè chart](w:Table_of_nuclides), which I didn't know.

## The Data

The AI found a digital version of this chart "all by itself" as well as how to integrate it into the game without a database, and explains it itself:

> The data in [isotopes.json](https://github.com/goulu/isotope/blob/master/public/isotopes.json) was extracted using the Python script [fetch_real_isotopes.py](https://github.com/goulu/isotope/blob/master/src/fetch_isotopes.py), which relies on the Python library [**`mendeleev`**](https://mendeleev.readthedocs.io/), integrating a nuclear database primarily sourced from:
> 1) [NUBASE](https://www-nds.iaea.org/relnsd/nubase/nubase_min.html) (nuclear and decay property evaluations published with the [IAEA](w:International_Atomic_Energy_Agency) and the Atomic Mass Data Center).
> 2) Data from the AME (_Atomic Mass Evaluation_) and CIAAW (_Commission on Isotopic Abundances and Atomic Weights_).

## The Levels

I also asked the AI to craft gameplay levels with progressive difficulty, and it churned out about twenty of them, with detailed descriptions:

- **Tutorial 1: Electron Capture**: The Tellurium-123 atom (Te-123) is a special case of a stable isobar. Add an electron (Right Click or Down Arrow) to transmute a proton into a neutron. You will instantly obtain stable Antimony!
- **Tutorial 2: Beta- Radioactivity**: Oxygen-18 is stable. Add a neutron (Left Click, Space, or Right Arrow) to turn it into Oxygen-19. It will become unstable and spontaneously decay (Beta-) into Fluorine-19!
- **Level 3: The Alchemist's Dream**: Transmutation of Mercury-196 into stable Gold. This reaction was achieved in 1941 by Sherr, Bainbridge, and Anderson by bombarding mercury with neutrons.
_(note the scientific reference [1] that the AI found "all by itself", though perhaps in one of my Quora answers...)_

etc. all the way to:

- **Level 13: The Great Neon Race**: Neon-22 is stable. Add a neutron (⚛), then very rapidly fire two more neutrons (⚛, ⚛) and two electrons (⚡, ⚡) without waiting for intermediate isotopes to decay. You will reach unstable Oxygen-25, which will undergo a spectacular decay cascade all the way to stable Magnesium-24!

## Gameplay and Difficulty

It's up to you to let me know what you think, but I find the game fun, educational, yet easy. Perhaps too easy. In fact, in the initial 13 puzzles, the order in which you fire particles barely matters, if at all. Nor does the timing of particle shots, so you almost always reach the goal no matter what you do.

The reason is that each level takes a short detour into the "pink" area of the chart or into the "blue" area, meaning nature always triggers an identical chain of β⁻ or β⁺ decays; the added neutrons or electrons also cause the exact same shift regardless of the order in which they are absorbed.

In short, I will ask the AI to generate more intricate puzzles using multiple decay modes, especially $\alpha$ which should make things more interesting...

But that probably means significantly expanding the table of supported isotopes, and thus the game's footprint, so I'll need to find a trick to keep it lightweight and fast...

### Logarithmic Time

In reality, isotope half-lives (`T½`) range from a few microseconds (`10⁻⁶ s`) to billions of years (`10¹⁷ s`). To compress these 23 orders of magnitude into a few seconds of gameplay while preserving the real stability ranking of each isotope, I used:

`Game_Time = clamp(Base + Slope × log10(T½), Min, Max)`

The parameters are currently adjustable at the bottom of the manual page, but I would like to lock in preset values corresponding to difficulty levels.

So there is still a bit of work ahead; your feedback in the comments is welcome, as is your help on GitHub...

## itch.io

[itch.io](w:Itch.io) is the benchmark platform for indie games. It hosts hundreds of thousands of them. And with AI, that number grows by 6,000 every single day!!!

With ISOThOPE, it hit 6,001 yesterday...

My goal isn't to make a fortune (the game is free), but to see how it fares on such a platform. As soon as the player count surpasses the number of visits to this page, it will have been well worth it.

## Translations

To make the game accessible to a wide audience, it is translated into English, Spanish, and Chinese via an AI-generated [script translate.ts](https://github.com/goulu/isotope/blob/master/scripts/translate.ts), using AI for the translations. (Okay, I'll add German and Italian in the next version...)

Reflecting on it, I thought this very post deserved to be available in English as well... Which meant turning my website multilingual... something Hugo supports natively! So that's done too: drgoulu.com now has several pages translated into English thanks to ISOThOPE!

## User Manual

Welcome to **ISOThOPE**, the nuclear transmutation puzzle game built on real scientific data from the IAEA (NUBASE / LiveChart).

### 🎯 1. Goal of the Game

You control an atomic nucleus displayed at the center of the [**Segrè Chart**](w:Table_of_nuclides) (the nuclear physicist's periodic table):

- The horizontal axis represents the number of neutrons (`N`).
- The vertical axis represents the number of protons (`Z`), which defines the chemical element.

In each level, you start from an **initial isotope** and must reach a **target isotope** (highlighted with a golden border on the grid) by smartly combining particle bombardments and natural radioactive decays.

> **Tip:** Sometimes let nature do the work for you! A natural radioactive decay saves your precious particles.

### ⚡ 2. Actions and Controls

Use the buttons below the grid to bombard your nucleus before it decays:

| Action | Effect on Nucleus | Grid Movement | PC Shortcut |
| --- | --- | --- | --- |
| **⚛ +n** (Neutron) | Adds 1 neutron (`N + 1`) | **➔ Right** (same element, heavier) | `N` or `→` |
| **⚡ +e⁻** (Électron) | Electron capture (`Z - 1, N + 1`) | **↘ Bottom-right diagonal** | `E` or `↓` |
| **🔴 +p** (Proton) | Adds 1 proton (`Z + 1`) | **↑ Up** (next element) | `P` or `↑` |
| **Restart** | Resets the current level | Returns to start nucleus | `R` |

### ☢️ 3. Stability and Radioactive Decays

Each cell on the grid is colored according to the real physical behavior of the isotope:

- **⬛ Black (Stable)**: The nucleus does not decay. The timer stops and you have unlimited time to think. _Warning: if you land on a stable isotope that is not your target and run out of particles, it's Game Over!_
- **🟦 Blue (β⁻ — Beta minus)**: Neutron excess. A neutron turns into a proton (`Z + 1, N - 1` ➔ moves **↖ top-left diagonal**).
- **🟧 Orange (β⁺ / ε — Beta plus or Electron capture)**: Proton excess. A proton turns into a neutron (`Z - 1, N + 1` ➔ moves **↘ bottom-right diagonal**).
- **🟨 Yellow (α — Alpha)**: Heavy nucleus that ejects an alpha particle (`⁴He`) made of 2 protons and 2 neutrons (`Z - 2, N - 2` ➔ moves **↙ 2 cells down and 2 left**).
- **🟥 Red (p — Proton emission)**: Extremely proton-rich nucleus that directly ejects 1 proton (`Z - 1` ➔ **↓ 1 cell down**).
- **🟪 Purple (n — Neutron emission)**: Extremely neutron-rich nucleus that directly ejects 1 neutron (`N - 1` ➔ **← 1 cell left**).
- **🟩 Green (SF — Spontaneous fission)**: The heavy nucleus splits apart spontaneously.

### 🧭 4. Levels and Free Mode (Level 0)

- **Level Briefing**: Click anywhere on the **level description bar** (located below the title bar) to open the scientific and historical briefing for the current mission.
- **Level Selector**: Click the numbered button (e.g. `1/13`) on the left of the level bar to switch missions.
- **Level 0 — Free Mode (Sandbox)**: Located at the very top of the level list, it gives you unlimited particles (`∞`) and lets you click directly on any cell in the grid or the `ISOThOPE` title banner to explore the chart of nuclides.

## References

1. R. Sherr, K. T. Bainbridge and H. H. Anderson, "_Transmutation of Mercury by Fast Neutrons_", _Physical Review_, vol. 60, no. 7, 1941, pp. 473-479 {{< altmetric doi="10.1103/PhysRev.60.473" >}}
