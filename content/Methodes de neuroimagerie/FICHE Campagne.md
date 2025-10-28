---
prof: CAMPAGNE Aurélie
date: 2025-10-02
publish: true
---
## 📌 Objectifs pour l’examen
- Comprendre les notions clés et ordres de grandeur (résolution temporelle/spatiale, principe de mesure).
- Expliquer le principe et les dispositifs nécessaires pour l’EEG et la MEG.
- Comprendre les méthodes de pré-traitement (filtrage, segmentation, correction d’artéfacts…).
- Connaître avantages et limites des techniques (EEG, MEG, électrodes, pré-traitements, etc.).

---

## 🧠 Principes généraux
### Résolutions
- **Résolution temporelle** : capacité à distinguer deux événements rapprochés dans le temps.
- **Résolution spatiale** : capacité à localiser précisément l’origine du signal dans le cerveau.

| Technique | Objet mesuré           | Capteur                  | Résolution temporelle | Résolution spatiale | Ordre de grandeur du signal |
|-----------|------------------------|--------------------------|-----------------------|---------------------|-----------------------------|
| **EEG**   | Potentiels électriques | Électrodes de surface    | ~1 ms                 | Faible à moyenne    | quelques µV                 |
| **MEG**   | Champs magnétiques     | SQUID + bobines (blindage) | ~1 ms                 | Bonne               | 10⁻¹³ Tesla                 |

---

## ⚡ Origine des signaux
[[Origine des signaux oscillatoires]]
[[Origine physique des signaux EEGMEG]]
- EEG/MEG mesurent l’activité **synchrone** de populations de neurones pyramidaux.
- Sensibles aux **potentiels post-synaptiques (PPS)**, moins aux potentiels d’action.
- Synchronisation assurée par :
  - **Boucles thalamo-corticales** (chef d’orchestre sensoriel).
  - **Boucles cortico-corticales** (coordination interrégions).

---

## 🎛️ EEG
[[EEG — Électroencéphalographie]]
### Dispositifs
- Mesure **monopolaire** (électrode vs référence) ou **bipolaire** (électrode vs électrode).
- Référence possible : nez, mastoïdes, lobes d’oreilles, moyenne globale (>64 électrodes).
- **Types d’électrodes** :
  - *Passives* : simple réception.
  - *Actives* : amplification locale.
  - *Humides* : avec gel conducteur (bonne conductivité, mais longue préparation).
  - *Sèches* : sans gel (rapide, mais plus d’artéfacts).

### Positionnement
- **Système international 10-20** (ou 5% pour plus de précision).
- Repères : Nasion, Inion, points pré-auriculaires droit/gauche.

---

## 🌀 MEG
[[MEG — Magnétoencéphalographie]]
### Dispositifs
- Mesure de champs magnétiques via **SQUID** (Superconducting Quantum Interference Device).
- Nécessite une **chambre blindée (cage de Faraday)**.
- Refroidissement à l’hélium liquide (coût élevé).

---

## 🔍 Comparatif EEG vs MEG

| Critère              | EEG                                      | MEG                                       |
|-----------------------|------------------------------------------|-------------------------------------------|
| Signal mesuré        | Potentiels électriques                   | Champs magnétiques                        |
| Réponse dipolaire    | Parallèle au dipôle                      | Perpendiculaire au dipôle                  |
| Réponse spatiale     | Diffuse                                  | Focale                                    |
| Sensibilité          | Toutes orientations (y compris profondes)| Sources tangentielles, peu sensibles profondes |
| Influence milieux    | Très affecté par les tissus              | Peu affecté par les tissus                |
| Coût                 | Relativement faible                      | Très élevé                                |

---

## ⚙️ Pré-traitements & gestion des données

### Filtrage
[[Filtrage]]
- **Risques** :
  - Perte d’information utile selon bandes filtrées.
  - Déformation du signal/artéfacts.
- **Pratique sûre** : 
  - Filtre en fente 50 Hz.
  - Passe-bande [0.5 – 100 Hz].

### Segmentation

- **Avant pré-traitement** : plus rapide, mais risque d’effets de bords.
- **Après pré-traitement** : plus sûr, mais plus coûteux.

### Correction de la ligne de base
[[Correction de la ligne de base]]
- Moyenne des périodes pré- et post-tâche → soustraction / division / Z-score.

---

## 🚫 Artéfacts
[[Correction des artefacts]]
### Sources physiologiques
- Mouvements oculaires → correction via **EOG** (4 électrodes).
- Activité cardiaque → correction via **ECG** (facile à discriminer).
- Activité musculaire → correction via **EMG**, mais risque de biais.
- Fatigue → ondes alpha.

### Sources externes
- Mouvements de tête, câbles, bruit électronique 50 Hz.

### Méthodes de correction
- Rejet des segments contaminés.
- PCA (Analyse en Composantes Principales) → utile pour artéfacts orthogonaux au signal d’intérêt.

---

## 📊 Types d’analyses
[[Analyses des signaux]]

- **Globale** : vigilance, états émotionnels.
- **Locale** : discrimination de visages, effet d’une condition expérimentale.
- **Potentiels et champs évoqués** : réponses temporellement verrouillées.
- **Analyse spectrale / connectivité** : (pas demandées en détail à l’examen).

---

