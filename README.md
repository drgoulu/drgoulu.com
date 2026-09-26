# Dr. Goulu (drgoulu.com)

> *Pourquoi, Comment, Combien — Blog de vulgarisation scientifique, mathématiques, informatique et curiosités par le Dr. Goulu (Philippe Guglielmetti).*

Site web officiel : [drgoulu.com](https://drgoulu.com/)

---

## 📖 À propos du site

**Dr. Goulu** est un blog personnel et technique créé en 2004, consacré à la science, aux technologies, à l'histoire des découvertes, aux énigmes mathématiques, à l'ingénierie et aux voyages.

Après avoir évolué sur divers CMS (SPIP, WordPress), le site a été migré vers une architecture **statique moderne** propulsée par le générateur [Hugo](https://gohugo.io/) et le framework [Hugo Blox](https://hugoblox.com/) avec [Tailwind CSS](https://tailwindcss.com/).

### Points clés :
* **Près de 800 articles** documentés, illustrés et enrichis de code, équations et diagrammes.
* **Génération statique ultra-rapide** et sans dépendance à une base de données.
* **Recherche intégrée côté client** avec [Pagefind](https://pagefind.app/).
* **Déploiement direct** par Git push vers le serveur de production Infomaniak.

---

## 🛠️ Modules et Extensions

Le site intègre un ensemble d'extensions et de shortcodes personnalisés pour enrichir le contenu Markdown :

### 1. Formules Mathématiques (LaTeX / KaTeX)
Le rendu mathématique est assuré nativement par KaTeX :
* **En ligne :** `$f(x) = ax + b$`
* **En bloc centré :**
  ```latex
  $$f(x) = \left(\frac{1}{\varphi}\right)^{\frac{1}{\varphi}} x^\varphi$$
  ```

---

### 2. Reference 2 Wiki (`w:` / `wiki:`)
Remplace et modernise l'ancien plugin WordPress *reference-2-wiki*. Tous les liens vers Wikipédia s'ouvrent dans un nouvel onglet et sont automatiquement stylisés avec le symbole **ⓦ**.

* **Syntaxe Markdown recommandée :**
  * `[fusion thermonucléaire](w:)` : article FR basé sur le texte du lien.
  * `[Paul Davies](w:Paul_Davies_(physicien))` : article FR avec titre spécifique.
  * `[Bigelow Aerospace](w:en)` : article Wikipédia en anglais.
  * `[Dr. Hal E. Puthoff](w:en:Harold_E._Puthoff)` : article EN avec page spécifique.
* **Via Shortcode :**
  * `{{</* w "fusion thermonucléaire" */>}}`
  * `{{</* w "Harold_E._Puthoff" "en" "Dr. Hal E. Puthoff" */>}}`

---

### 3. Images Flottantes et Légendes (Figure)
Remplace les balises WordPress `[caption]` pour insérer des images flottantes avec légende, redimensionnement et adaptation responsive sur smartphone :

```go
{{</* figure src="images/photo.jpg" caption="Légende de l'image" alt="Description" align="alignright" width="400" link="https://..." */>}}
```

* `align` : `alignright` (flottant à droite, par défaut), `alignleft` (flottant à gauche), ou `aligncenter` (centré).
* `width` : Largeur maximale en pixels (ex: `400` ou `400px`).
* `caption` : Légende textuelle affichée sous l'image.
* `link` : Lien optionnel pour rendre l'image cliquable.

---

### 4. Diagrammes Mermaid
Permet de générer des diagrammes et schémas directement à partir de texte Markdown :

* **Organigrammes (Flowcharts) :**
  ```mermaid
  graph TD
  A[Début] -->|Action| B(Étape suivante)
  B --> C{Choix}
  C -->|Option 1| D[Résultat 1]
  C -->|Option 2| E[Résultat 2]
  ```
* **Diagrammes de séquence :**
  ```mermaid
  sequenceDiagram
  Alice->>Bob: Bonjour Bob !
  Bob-->>Alice: Salut Alice !
  ```
* **Diagrammes de classes et d'états :** `classDiagram`, `stateDiagram`, etc.

---

### 5. Graphiques Interactifs (Plotly)
Intègre des visualisations interactives au format JSON Plotly :

```go
{{</* chart data="line-chart" */>}}
```
*(Le fichier de données `line-chart.json` doit être placé dans le dossier du post).*

---

### 6. Tableaux de Données (CSV / Data Frames)
Permet d'importer et d'afficher un fichier CSV directement dans un article :

```go
{{</* table path="results.csv" header="true" caption="Tableau des résultats" */>}}
```

---

### 7. Vidéos YouTube
Intégration responsive respectant la vie privée (via `youtube-nocookie.com`) :

```go
{{</* youtube id="yfwb39VCNcQ" width="640" */>}}
```

---

### 8. Rétroliens (Backlinks)
La section « Sur le même sujet » met en avant en priorité les articles qui citent la page consultée grâce au module [`backlinks4hugo`](https://github.com/drgoulu/backlinks4hugo).

---

## 💻 Développement local

### Prérequis
* [Hugo Extended](https://gohugo.io/installation/) (>= 0.160)
* [Node.js](https://nodejs.org/) (>= 20) & [pnpm](https://pnpm.io/)

### Commandes utiles
```bash
# Installer les dépendances
pnpm install

# Mettre à jour l'index des rétroliens
pnpm run backlinks

# Lancer le serveur de développement local (met à jour les rétroliens puis lance Hugo)
pnpm run dev
# ou
hugo server --disableFastRender

# Construire le site et générer l'index de recherche
pnpm run build
```

---

## 📄 Licence

Contenu © [Dr. Goulu](https://drgoulu.com/) - Tous droits réservés.
Code du site sous licence MIT.
