---
title: 3D Kaya Identity
date: 2026-10-05
draft: false
tags:
  - kaya identity
  - 3d
  - vibe coding
  - visualization
  - world
  - co2
categories:
  - How
  - Numbers
slug: 'kaya-en-3d'
coverImage: ./images/Capture d’écran du 2026-10-05 10-48-45.png
---

In just one hour of initial coding and a second hour of polishing, I brought a long-standing project to life:

Plotting the [Kaya identity](w:Kaya_identity) in 3D with country bubbles inspired by [Gapminder](https://www.gapminder.org/tools/#$chart-type=bubbles&url=v2).

The core idea is to map the key factors of each country's CO2 emissions onto three spatial axes:

- **X axis**: [GDP per capita](w:Gross_domestic_product#Per_capita) (GDP/POP in constant $/person)
- **Y axis**: [Energy intensity](w:Energy_intensity) of GDP—the quantity of energy required to generate one dollar of goods or services (E/GDP in kWh/$)
- **Z axis**: [Carbon intensity](w:Emission_intensity) of energy—the amount of CO2 emitted per unit of energy consumed (CO2/E in g CO₂/kWh).

Bubble size represents population (POP), though the app also allows toggling bubble size to represent per-capita emissions (CO2/POP) or total national emissions.

The live interactive result is embedded below (and hosted on [https://goulu.github.io/kaya/](https://goulu.github.io/kaya/)):

<div style="position: relative; width: 100%; height: 640px; border-radius: 12px; overflow: hidden; border: 1px solid #e5e7eb; margin: 2rem 0;">
  <iframe 
    src="https://goulu.github.io/kaya/?embed=true" 
    style="width: 100%; height: 100%; border: none;" 
    title="3D Kaya Identity Visualization" 
    loading="lazy" 
    allowfullscreen>
  </iframe>
</div>

*(The [source code is on GitHub](https://github.com/goulu/kaya) if you'd like to contribute or file issues...)*

You can uncover a wealth of insights here, but most importantly (and this was the main objective), you see that each country's situation is VASTLY different. Consequently, their decarbonization priorities to slow and ultimately reverse emissions must necessarily differ.

Where my AI pair programmer stunned me yet again was by adding a temporal animation scrubber "all by itself." I had simply asked to "visualize like Gapminder" thinking of country bubbles, but the temporal animation slider clearly illustrates the [broad global trend toward higher energy efficiency](/2013/05/11/400-parties-par-million-et-moi-et-moi-emoi/) and (gradual) emissions decoupling. Take a close look—it really shows!

**October 7 Update:** Following an interesting exchange with PFC, I added selectable "consumption-based emissions" metrics to the bubble sizes, sourced from the [Global Carbon Project](w:Global_Carbon_Project) which published:

Friedlingstein et al., "Global Carbon Budget 2025," [Earth System Science Data](https://www.earth-system-science-data.net/), [Volume 18, issue 5](https://essd.copernicus.org/articles/18/issue5.html), 3211–3288, 2026, {{< altmetric doi="10.5194/essd-18-3211-2026" >}}

The underlying dataset is available [globally here](https://web.archive.org/web/20260903075210/https://ourworldindata.org/grapher/consumption-co2-emissions) and [per capita here](https://web.archive.org/web/20261005/https://ourworldindata.org/explorers/co2?tab=map&Gas+or+warming=CO%E2%82%82&Accounting=Consumption-based&Count=Per+capita&Relative+to+world+total=false&country=CHN~USA~IND~GBR~OWID_WRL). Because this data is not available for every nation prior to 1990, the chart renders small dots at the XYZ coordinates whenever historical consumption data is missing.
