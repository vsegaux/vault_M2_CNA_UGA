---
prof: CONGEDO Marco
date: 2025-11-25
publish: true
---
 Toute la première partie porte sur des rappels de l'EEG, cf [[CM Campagne]].
# EEG Analysis
## Blind Source Separation (BSS)
- Signal x(t), pour N capteurs
- L'objectif est de retrouver s(t), le signal source de x(t) -> *A expliquer mieux...*

# EEG Classification
On fait rarement le traitement sur les signaux bruts, plutôt sur la matrice de covariance, qui correspond à la multiplication de la matrice et de sa transposée (divisée par le nombre de capteurs). Chaque case hors de la diagonale va alors donner la corrélation entre une paire de capteurs.

**Géodésique**: Extension dans un espace non euclidien de la ligne droite qui minimise le chemin entre deux points.
- Par exemple, le chemin le plus cours pour aller de Berlin à Lyon est une géodésique.
- Si on prend les deux pôles, il y a une infinité de géodésiques pour les relier.
- Dans des espaces non euclidiens, il peut exister des triangles avec 2 angles droits.

Les matrices de covariance permettent d'être sensibles à des variations très faibles comme grande. Les notions de distances ($\delta$) et de barycentre existent dans ces espaces non euclidiens. -> *A expliquer mieux...*. Le barycentre est le point qui minimise les distances : B=$\delta^2(M,A)+\delta^2(M,B)$, on parle de moyenne géométrique ($\sqrt{XY}$, plutôt que la moyenne arithmétique ($\frac{X+Y}{2}$))

*Variété Remannienne*: En mathématiques, et plus précisément en géométrie, la **variété riemannienne** est l'objet de base étudié en géométrie riemannienne. Il s'agit d'une variété, c'est-à-dire un espace courbe généralisant les courbes (de dimension 1) ou les surfaces (de dimension 2) à une dimension _n_ quelconque, et sur laquelle il est possible d'effectuer des calculs de longueur. 

### Remannian Procrustes Analysis (RPA)
*A expliquer mieux...*
L'objectif est de reformater les données pour pouvoir mieux les comparer. Typiquement pour mieux les catégoriser en machine learning. Les transformations appliquées sont 'rigides' (sauf la standardisation), c'est à dire que les relations entre les points ne sont pas modifiées.

- *Recentrage:* Des données d'origine, on recentre chaque donnée sur l'identité (point central typiquement la moyenne). 
	- Par exemple: {1,2,3} et {10,20,30} deviennent : {-1,0,1} et {-10,0,10}
	- Avec des matrices : $G^{-1/2}C_kG^{-1/2}$ 
- *Standardisation/stretching:* Ensuite, on adapte la variance pour que l'écart type soit équivalents dans toutes les données.
	- Avec des matrices : $C_k^p$ 
- *Rotation:* 
	- Avec des matrices : $UC_kU^{T}$ 
- Finalement:
	- $UG^{-1/2}C_k^pG^{-1/2}U^T$ 
Sur l'exemple suivant, les données transformées sont/semblent plus difficile à classifier.
![[RPA_EEG_signal.png]]

Ce genre de transformation est utile typiquement dans les cas où on a des données sur de nombreux sujets *réalisant la même tâche*, l'objectif est d'apprendre au algorithmes de machine learning à détecter l'effet de la tâche, indépendamment du sujet. On applique alors les transformations ci-dessus aux données de chaque sujet.

## Brain-Computer Interfaces (BCI)
### Applications
On ne peut utiliser que les données EEG en guise d'interface. Les applications sont variées:
- remplacement d'habilité motrices (prothèses, CEA)
- mobilité (commander un fauteuil roulant)
- communication (débit limité pour l'instant, environ 5 lettre par minute)
- divertissement (contrôle de jeux vidéo...)

### Paradigmes
- Event-Related De/Synchronization
	- Typiquement en se basant sur les cortex moteurs et somatosensoriels (et plus particulièrement sur leur organisation topographique): déynchronisation du Cortex Moteur Contro latéral lors de la volonté de bouger un membre, la main par exemple.
- Event-Related Potential

> [!NOTE] Examen
> - Question posée

- Typiquement en réponse visuelle, on repère le potentiel P300. 
- Dans le jeu Brain Invaders, la cible va s'allumer 2 fois uniquement parmi 12 flash successifs de plusieurs monstres. Dans les données EEG, on retrouve les flash qui correspondent à la cible (P300), l'algorithme doit ensuite faire la différence entre un flash normal et un flash de la cible. Le sujet doit simplement regarder spécifiquement la cible parmi les monstres possibles. L'activité P300 n'est pas volontaire pour le participants, elle est mesurée "malgré lui".