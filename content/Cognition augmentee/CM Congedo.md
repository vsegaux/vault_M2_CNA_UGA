---
prof: CONGEDO Marco
date: 2025-11-25
publish: true
---
## I. Introduction à l'EEG

L'électroencéphalographie (EEG) permet de mesurer les potentiels électriques cérébraux instantanés avec une **haute résolution temporelle (~1 ms)**. C'est une méthode non invasive, silencieuse et relativement peu coûteuse, bien qu'elle souffre d'une **faible résolution spatiale** et d'une sensibilité accrue aux artéfacts (biologiques comme les clignements d'yeux, instrumentaux ou environnementaux).

## II. Analyse du Signal : La Séparation Aveugle de Sources (BSS)

L'objectif de la **Blind Source Separation (BSS)** est de passer des signaux enregistrés par les capteurs aux signaux produits par les sources réelles dans le cerveau.

- **Le problème :** On enregistre un signal $x(t)$ via $N$ capteurs. Ce signal est un mélange de $P$ sources $s(t)$ (où $P \le N$).
- **Le modèle :** $x(t) = As(t)$, où $A$ est la matrice de mélange.
- **La solution :** L'objectif est de trouver une matrice de "démélange" $B$ telle que l'on puisse estimer les sources : $\hat{s}(t) = Bx(t)$.

## III. Classification et Géométrie Riemannienne

En EEG, on travaille rarement sur les signaux bruts. On utilise généralement la **matrice de covariance**, notée $C = \frac{1}{T} XX^T$, où chaque élément hors de la diagonale représente la corrélation entre une paire de capteurs. Ces matrices sont des matrices symétriques définies positives. Elles forment un espace qui n'est pas euclidien.

### 1. Concepts Fondamentaux (Espace Non-Euclidien)

Pour mieux catégoriser les données en _machine learning_, on utilise la géométrie riemannienne, qui étudie des espaces courbes appelés **variétés riemanniennes**.

- **Géodésique :** Dans un espace courbe, c'est l'équivalent de la ligne droite ; elle représente le **chemin le plus court entre deux points**. Par exemple, sur Terre, les méridiens reliant les pôles sont des géodésiques.
- **Barycentre (Moyenne Riemannienne) :** Dans ces espaces non euclidiens, le barycentre est le point qui minimise la somme des carrés des distances géodésiques aux autres points. On utilise ici une **moyenne géométrique** ($\sqrt{XY}$) plutôt qu'arithmétique ($\frac{X+Y}{2}$).
- **Avantages :** Cette approche est robuste au bruit, ne nécessite souvent pas de calibration (parameter-free) et permet une meilleure sensibilité aux variations très faibles du signal.

### 2. Riemannian Procrustes Analysis (RPA)

La RPA consiste à reformater les données de différents sujets ou sessions pour les rendre comparables sans modifier les relations intrinsèques entre les points (transformations "rigides").

Les trois étapes de transformation sont (avec C, la matrice de covariance initiale)s :
1. **Recentrage :** On centre les données de chaque sujet sur l'identité (le point central/moyen) via la formule $G^{-1/2} C_k G^{-1/2}$.
	- Par exemple: {1,2,3} et {10,20,30} deviennent : {-1,0,1} et {-10,0,10}
2. **Standardisation (Stretching) :** On adapte la variance pour que l'écart-type soit équivalent dans toutes les données, corrigeant les différences d'échelle: $C_k^p$ 
3. **Rotation :** Une correction finale par rotation ($UC_kU^T$) pour aligner parfaitement les distributions.
- ![[RPA_EEG_signal.png]]

L'objectif final est de permettre aux algorithmes de **détecter l'effet d'une tâche indépendamment du sujet**.

## IV. Paradigmes des Interfaces Cerveau-Machine (BCI)

Les BCI utilisent les données EEG pour commander des interfaces (prothèses motrices, fauteuils roulants, communication ou jeux vidéo).

### 1. ERD/ERS (Imagerie Motrice)

Ce paradigme repose sur l'organisation topographique des cortex moteurs et somatosensoriels (homonculus).
![[ERD_ERS.png]]
- **ERD (Event-Related Desynchronization) :** On observe une baisse d'énergie (désynchronisation, dans une certaine bande spectrale) dans le cortex moteur **controlatéral** lors de l'intention ou de l'imagination d'un mouvement (ex: bouger la main droite provoque une ERD à gauche).
- **ERS (Event-Related Synchronization) :** Augmentation d'énergie (synchronisation), souvent observée après l'arrêt du mouvement (rebond Beta).

### 2. Potentiels Évoqués (ERP) et P300

Un **ERP** (Event-Related Potential) est obtenu par *moyennage* d'essais, il ne conserve donc que le *signal en phase d'un essai à l'autre*; il reflète le traitement neuronal temporellement stable et synchronisé avec l'évènement.

Le **P300** est un potentiel qui apparaît environ 300 ms après un stimulus cible "rare" parmi des stimuli non-cibles.

- **Exemple (Brain Invaders) :** Le joueur regarde une cible parmi plusieurs monstres. La cible s'allume aléatoirement( parmi plusieurs flash de présentation). L'algorithme détecte le P300 généré par ce flash pour identifier la cible du regard, même si l'activité n'est pas "volontaire" de la part du sujet.

## V. Neurofeedback

Le neurofeedback est une boucle fermée où une caractéristique de l'EEG est extraite en temps réel et traduite en un feedback sensoriel (visuel ou auditif) pour que le sujet apprenne à réguler son propre état cérébral.

- **Application classique (TDAH) :** Utilisation du ratio de puissance **Theta/Beta** comme indice d'inattention. Le patient s'entraîne à réduire ce ratio pour améliorer sa concentration.
- **Spécificité via BSS :** L'utilisation de la séparation de sources (BSS) permet de cibler des signaux très spécifiques et d'éliminer les interférences, rendant le neurofeedback plus efficace.