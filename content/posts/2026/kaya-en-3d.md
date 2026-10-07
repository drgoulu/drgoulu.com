---
title: Kaya en 3D
date: 2026-10-05
draft: false
tags:
  - equation de kaya
  - 3d
  - vibe coding
  - visualisation
  - monde
  - co2
categories:
  - comment
  - combien
slug: ''
coverImage: ./images/Capture d’écran du 2026-10-05 10-48-45.png
---

J'ai réalisé en une heure et fignolé en une deuxième heure un très vieux projet :

Représenter l'[équation de Kaya](<w:identité de Kaya>) en 3D, avec des bulles par pays à la façon [Gapminder](https://www.gapminder.org/tools/#$chart-type=bubbles&url=v2).

L'idée est de représenter les 4 facteurs des émissions de CO2 de chaque pays sur les 3 axes :

- X pour le [produit intérieur brut par habitant](w:) (PIB/POP en $ constants / personne)
- Y pour l' [intensité énergétique](<w: Intensité énergétique (économie)>) du PIB, la quantité d'énergie utilisée pour produire un dollar de biens ou services (E/PIB , en kWh / $)
- Z pour l' [intensité carbone de l'énergie](<w:Facteur d'émission>), la quantité de CO2 émise pour produire  l'énergie (CO2/E, en g CO₂ / kWh)..

et la taille de la bulle pour la population (POP), mais l'app permet de sélectionner plutôt les émissions par habitant (CO2/POP) ou les émissions totales par pays

Le résultat est ci-dessous (et sur [https://goulu.github.io/kaya/](https://goulu.github.io/kaya/) ): 

<div style="position: relative; width: 100%; height: 640px; border-radius: 12px; overflow: hidden; border: 1px solid #e5e7eb; margin: 2rem 0;">
  <iframe 
    src="https://goulu.github.io/kaya/?embed=true" 
    style="width: 100%; height: 100%; border: none;" 
    title="Visualisation 3D de l'Identité de Kaya" 
    loading="lazy" 
    allowfullscreen>
  </iframe>
</div>

(le [source est sur GitHub](https://github.com/goulu/kaya), si vous voulez contribuer ou remonter des bugs...)

On y voit plein de choses intéressantes, mais surtout (c'était le but) que les situations des pays sont TRES différentes, et que par conséquent leurs priorités pour limiter, puis réduire leurs émissions sont forcément différentes aussi.

Là où mon IA de codage m'a une fois de plus scotché, c'est qu'elle a ajouté "toute seule" l'échelle de temps. J'avais juste dit "visualise façon Gapminder" en pensant aux bulles par pays, mais cette fonction d'animation montre de façon très claire la [tendance générale à l'efficacité énergétique](/2013/05/11/400-parties-par-million-et-moi-et-moi-emoi/) et à la (lente) réduction des émissions. Si si, regardez bien ...

Edit du 7 octobre : suite à une discussion avec PFC, j'ai ajouté dans les volumes des sphères sélectionnables les données d' "émissions basées sur la consommation" selon le [Global Carbon Project](w:) qui publie  

Friedlingstein et al., « Global Carbon Budget 2025 ». [Earth System Science Data](https://www.earth-system-science-data.net/), [Volume 18, issue 5](https://essd.copernicus.org/articles/18/issue5.html), 3211–3288, 2026, {{< altmetric doi="10.5194/essd-18-3211-2026" >}}

Les données [globales sont là](https://ourworldindata.org/grapher/consumption-co2-emissions) et ici [par personne](https://ourworldindata.org/explorers/co2?tab=map&Gas+or+warming=CO%E2%82%82&Accounting=Consumption-based&Count=Per+capita&Relative+to+world+total=false&country=CHN~USA~IND~GBR~OWID_WRL)
Comme ces données ne sont pas disponibles pour tous les pays et pas avant 1990, le graphique affiche de petits points  aux coordonnées XYZ en cas de données indisponibles
