
## I. Les Dilemmes Fondamentaux des Systèmes de Mémoire

Les systèmes de mémoire sont confrontés à deux dilemmes structurels majeurs qui déterminent leurs enjeux et leurs solutions possibles :

1. **Information Générale vs. Spécifique** : Comment un système peut-il à la fois capturer les structures de connaissances générales (sémantiques) et retenir les détails uniques d'événements spécifiques (épisodiques) ?
2. **Stabilité vs. Plasticité** : Comment le système peut-il rester **stable** et conserver les anciennes connaissances tout en étant suffisamment **plastique** pour intégrer rapidement de nouvelles informations ?

---

## II. Fondements Connectionnistes et Mémorisation Distribuée

### A. La Loi de Hebb Stricte et son Application

La mémorisation dans les réseaux de neurones est traditionnellement régie par la Loi de Hebb.

- **Principe de la Loi de Hebb (Stricte)** : Lorsque deux neurones sont activés simultanément, le poids de la connexion qui les relie est modifié proportionnellement au produit de leur activation.
- **Règle d'Apprentissage Simple** : La modification du poids de connexion $\Delta W$ entre deux neurones activés par une entrée externe est calculée comme suit : $$\text{Nouveau poids} = \text{ancien poids} + \left(\frac{1}{\text{nombre de connexions}} \times (\text{Activation Neurone Entrée} \times \text{Activation Neurone Sortie})\right)$$ _(Exemple de calcul de poids)_ : Dans l'état initial où le poids est $0$, si le neurone d'entrée est activé à $-1$ et le neurone de sortie à $0.5$ (pour 2 connexions), le nouveau poids est $0 + (\frac{1}{2} \times (-1 \times 0.5)) = -1/4$.
- ![[exeple_appren_HEBB.png]]
- **Calcul de l'Activation (Phase de Récupération)** : L'activation d'un neurone en sortie est la somme des entrées pondérées par les poids de connexion : $$\text{Activation} = \sum (\text{Activation Entrée} \times \text{Poids de connexion})$$ _(Exemple de calcul d'activation)_ : Si les entrées sont $-1$ (poids $-1/4$) et $1$ (poids $1/4$), l'activation est $(-1 \times -1/4) + (1 \times 1/4) = 0.5$.

### B. Mémorisation Distribuée et Orthogonalité

La mémorisation dans ces systèmes est dite **distribuée**.

- **Information Distribuée** : L'encodage d'un concept est **distribué** sur l'ensemble des paramètres variables du modèle (les poids de connexion), et les mêmes paramètres sont modifiés pour tous les exemples à apprendre. Ceci est fondamentalement différent de l'idée de "cellules Grand-mère".
- **Terminologie : Distribution vs. Répartition** :
    - **Distribution** : Manière dont la mémorisation est effectuée sur les poids (l'apprentissage est _distribué_).
    - **Répartition** : Localisation des activations dans l'espace d'entrée (l'entrée est _répartie_ (d'une manière spécifique sur les capteurs d'entrée)).

### C. Limites de l'Orthogonalité et Oubli Catastrophique

Pour que les capacités d'apprentissage d'un modèle Hebbien simple soient excellentes, les deux entrées doivent être **orthogonales** entre elles (ex: $(-1, 1)$ et $(1, 1)$ (orthogonaux car -1x1 + 1x1 = 0)).

- **Conséquence sans Orthogonalité** : Sans orthogonalité, le système finit par souffrir d'**oubli catastrophique**.
- **Conséquence d'une Orthogonalité Totale** : Si toutes les entrées étaient systématiquement orthogonales, le système serait **incapable de généraliser** (c'est-à-dire de faire le lien entre différentes entrées).
- **Solution pour la Spécificité** : Pour obtenir une mémoire spécifique (évitant l'interférence), il faut un encodage orthogonal, rendu possible par un codage de type **'sparse'** (seuls certains neurones sont activés, augmentant les chances d'orthogonalité entre les patterns).

---

## III. Les Systèmes d'Apprentissage Complémentaires (Hippocampe/Néocortex)

Pour résoudre le dilemme stabilité/plasticité et gérer à la fois l'information générale et spécifique (dans un cadre Hebbien), la solution consiste à utiliser deux structures complémentaires, une idée développée par plusieurs modèles (Squire & Alvarez (95), Mc Clelland & Al. (95), Nadel & Moscowitch (97)).
![[nadel_mosco_rappe.png]]

### A. Rôles et Processus

|Système|Cortex (Néocortex) / Trace System|Hippocampe / Link System (Lobe Temporal Interne)|
|:--|:--|:--|
|**Rôle Principal**|Stockage **général** (sémantique). Apprend lentement la structure de cooccurrence. Trouve les points communs.|Stockage **spécifique** (épisodique). Apprend très rapidement les traces spécifiques. Crée instantanément une trace épisodique.|
|**Mécanisme**|Basé sur l'accumulation **lente** et **intercalée** des changements synaptiques.|Permet un apprentissage **rapide** (One Shot Learning). Utilise un codage _sparse_ pour l'orthogonalité.|
|**Enseignement**|Apprend à partir des traces épisodiques, qui servent de « professeur interne ».||

### B. Le Modèle TraceLink : Architecture et Dynamique

Le modèle TraceLink (Martijn Meeter & Jaap M.J. Murre, 1996-2006) met en œuvre cette complémentarité.

#### 1. Architecture et Plasticité

- **Trace System (Cortex)** : 200 cellules, implémentant un système Hebbien dynamique. Un événement est décomposé en $K=10$ composants sémantiques.
- **Link System (Hippocampe)** : 42 cellules. Un événement active $K=7$ cellules. Il est connecté à un système de modulation.
- **Fonctionnement** : Les unités utilisent une fonction sigmoïde pour déterminer leur activation ($a_i = 1$ ou $0$) en fonction de leur entrée nette $net_i$, modulée par l'inhibition pour assurer un codage _sparse_.
- **Règle de Plasticité** : La règle $\Delta W_{ij}=(\mu^{+}a_{i}a_{j})-(\mu^{-}a_{i}(1-a_{j}))$ induit à la fois l'apprentissage (terme $\mu^{+}$) et l'oubli (terme $\mu^{-}$).

#### 2. Différences des Taux d'Apprentissage (Réponse à Q1)

Le **taux d'apprentissage $\mu$** doit être radicalement différent entre les systèmes pour respecter leurs rôles fonctionnels :

|Connexions|Système Concerne|Taux $\mu$ (Acquisition)|Rôle / Justification|
|:--|:--|:--|:--|
|**Intra Link / Link-Trace**|Hippocampe|**Élevé** ($\mu=0.4$)|Assurer l'apprentissage **rapide** et _one-shot_ des associations spécifiques. Le Link System doit être hautement plastique.|
|**Intra Trace**|Cortex|**Faible** ($\mu=0.06$)|Assurer l'apprentissage **lent et intercalé** de la structure sémantique pour éviter l'oubli catastrophique.|

#### 3. Modes d'Opération

- **Apprentissage (Mode Externe)** : Le système utilise les taux $\mu$ élevés du Link System pour enregistrer rapidement l'épisode.
- **Consolidation (Mode Interne)** : La trace est consolidée dans le Cortex (Trace System) par des activations générées à partir de bruit aléatoire.
    - La plasticité dans les connexions Link/Link-Trace est coupée ($\mu=0$).
    - Un très faible taux d'apprentissage est appliqué dans le Trace System ($\mu=0.0025$).
    - Ce processus de réinstanciation permet l'**incorporation graduelle** des nouvelles connaissances dans le système cortical, où elles sont **intercalées** avec l'exposition continue aux connaissances existantes pour découvrir la structure partagée et éviter l'interférence.

### C. Évidences Neuropsychologiques (Lésions)

Les modèles complémentaires expliquent les résultats observés après des lésions du lobe temporal interne (hippocampe) :

- **Amnésie Rétrograde Gradée (Ribot Gradient)** : Les patients amnésiques (lésion Link System) montrent une amnésie rétrograde **gradée**. Les souvenirs les plus anciens sont maintenus (car consolidés dans le cortex), tandis que les souvenirs les plus récents (dépendants de l'hippocampe) sont perdus.
- **Amnésie Antérograde** : L'incapacité de former de nouveaux souvenirs (amnésie antérograde) survient immédiatement après la lésion du Link System.
- **Ictus Amnésique Transitoire (TGA)** : Simulé par $K=0$ dans le Link System. Pendant l'ictus, l'apprentissage est impossible, mais la récupération progressive de $K$ permet de retrouver les fonctions mnémoniques, à l'exception du souvenir appris pendant la période d'amnésie.

---

## IV. Réseaux à Hyperplans Séparateurs et Généralisation

Le fonctionnement des réseaux de neurones distribués, et notamment leur capacité à généraliser, repose sur la notion d'hyperplan séparateur.

### A. Principe de l'Hyperplan Séparateur

Dans un réseau de neurones à propagation avant :

1. **Calcul de l'Entrée Totale** : L'entrée totale d'une cellule de sortie est la somme des activations des cellules sources multipliées par leurs poids de connexion respectifs.
2. **Seuil d'Activation** : La cellule de sortie ($S_1$) applique une fonction de seuil ($f$) à cette somme pondérée pour déterminer son activation ($0$ ou $1$).
3. **L'Hyperplan** : Le réseau définit une frontière (point, droite, plan ou **hyperplan** en haute dimension) qui sépare l'espace d'entrée entre les sorties $S=0$ et $S=1$.
4. **Apprentissage** : L'apprentissage consiste à ajuster les poids de connexions [W] (les seuls paramètres libres) de manière automatique et locale pour positionner l'hyperplan séparateur et minimiser l'erreur pour tous les exemples.

### B. Mémorisation et Réfutation du Stockage (Réponse à Q2)

Dans les systèmes fonctionnant par séparation par hyperplan, l'assertion qu'un item est stocké en mémoire est fausse.

- **Pas de Stockage Explicite des Items** : **Il n'y a aucun stockage des exemples d'apprentissage dans le réseau de neurones**. Les exemples ne servent que de **contraintes** pour positionner l'hyperplan séparateur (la fonction mathématique du réseau).
- **Mémoire = Fonction** : La mémoire réside dans la **fonction de re-création** (la configuration des poids) induite par l'apprentissage, et non dans les items eux-mêmes. Le réseau produit une sortie pour n'importe quelle entrée, même non entraînée.

### C. Rôle des Couches Cachées et Nature de la Généralisation

Un réseau à une seule couche est limité aux problèmes linéairement séparables. L'ajout de couches cachées permet de dépasser cette limite et de transformer la nature de la généralisation.

- **Fonction des Couches Cachées** : Elles permettent de **projeter les entrées dans un nouvel espace façonné en fonction des contraintes d'apprentissage** (transformation non-linéaire). La fonction d'activation utilisée doit être non-linéaire et continue (e.g., Sigmoïde) pour permettre cette projection.
- **Généralisation par Découverte de Structure** : La non-linéarité permet de dépasser la simple juxtaposition des relations entrée-sortie (associationnisme). Le réseau capture la **structure** du domaine (les régularités logiques) à travers la succession d'exemples élémentaires, même si cette structure n'était pas inscrite dans l'architecture.
- **Déformation de l'Espace d'Entrée** : L'espace d'entrée est déformé dans les couches cachées de telle sorte que les concepts liés par la structure (e.g., les oiseaux) sont rapprochés, même s'ils ne se ressemblent pas physiquement.
- **Inférer les Propriétés** : Une fois la structure apprise, l'apprentissage d'une nouvelle entité (ex: "torti" est un oiseau) permet au réseau d'inférer immédiatement ses propriétés associées, car il projette cette nouvelle entité dans la zone de l'espace caché correspondant à la catégorie apprise.

---

## V. L'Oubli Catastrophique et la Solution des Pseudo-Exemples

### A. Sensibilité à l'Oubli Catastrophique (Réponse à Q3)

Les réseaux distribués fonctionnant par séparation par hyperplan sont particulièrement sensibles à l'**oubli catastrophique**.

- **Définition** : L'oubli catastrophique est l'oubli dramatique des exemples antérieurement appris lors de l'apprentissage de nouveaux exemples.
- **Cause Principale** : Étant donné que la mémoire est codée dans les poids de connexion (la fonction de re-création), l'apprentissage séquentiel modifie ces poids pour satisfaire les nouvelles contraintes. Les anciens exemples **ne contraignent plus** la fonction, et les poids établis précédemment pour les anciens items sont largement altérés.
- **Lien avec la Mémoire Distribuée** : La solution à l'oubli catastrophique doit être intimement liée à la nature de la mémoire dans un système distribué. Puisque la mémoire est la fonction, la solution est de **rafraîchir la fonction elle-même**.

### B. L'Auto-Rafraîchissement par Pseudo-Exemples (PE)

La solution la plus efficace est l'auto-rafraîchissement par pseudo-exemples (PE), introduite par Robins (1995).

- **Principe Général** : Puisque nous ne disposons généralement pas des anciens exemples pour les répéter, on génère des **Pseudo-Exemples** à partir de bruit aléatoire. Ces PE sont des exemples de la **fonction de re-création actuelle** du réseau.
- **Processus de Création** : Un bruit aléatoire est injecté en entrée, et la sortie calculée par le réseau est le pseudo-exemple correspondant. Cette association Entrée-Bruit/Sortie-PE est un reflet de la fonction apprise.
- **Méthode** : Les PE sont créés, stockés dans une mémoire tampon, et ré-introduits lors de l'apprentissage des nouveaux exemples afin que **les connaissances passées continuent à contraindre la fonction**.

### C. Améliorations Architecturales et Processus de Réverbération (Réponse à Q3)

Pour pallier les limites d'une mémoire tampon non neuromimétique et améliorer la résolution de l'oubli, des architectures plus complexes sont utilisées :

#### 1. Proposition des Deux Structures Connectionnistes (Réseau Principal/Secondaire)

- **Principe de l'Architecture** : Utiliser un **Réseau Secondaire** pour apprendre les Pseudo-Exemples générés par le Réseau Principal.
- **Fonctionnement** : Le Réseau Principal transfère sa fonction au Réseau Secondaire via des PE générés à partir de bruit. Ensuite, le Réseau Principal apprend les Nouveaux Exemples en les couplant avec un pseudo-rafraîchissement provenant du Réseau Secondaire (ses propres connaissances antérieures).

#### 2. Rôle de la Réinjection (Réverbération)

- **Objectif** : Maximiser la capture de la **structure** dans les Pseudo-Exemples.
- **Méthode** : La sortie auto-associative est réinjectée comme nouvelle entrée dans le réseau. L'enchaînement de plusieurs réinjections successives est appelé **réverbération**.
- **Bénéfice** : La réverbération permet à la sortie de converger vers les **points attracteurs** (souvent des minimums locaux) qui constituent d'excellents pseudo-exemples, même s'ils n'ont jamais été appris spécifiquement. La réverbération est cruciale, car l'auto-rafraîchissement **avec réverbération** réduit considérablement l'oubli catastrophique par rapport à l'auto-rafraîchissement simple.

---

## VI. Apprentissage Séquentiel et Transfert de Connaissances

### A. Transfert de Structure et Généralisation

L'apprentissage séquentiel permet d'étudier le transfert de structure entre domaines.

- **Condition Compatible (Addition Décimale puis Octale)** : L'apprentissage de l'Addition Octale (Base B) est beaucoup plus rapide et généralise mieux si la structure de l'Addition Décimale (Base A) a été apprise auparavant, même si les items sont différents.
- **Observation** : Le réseau n'a pas explicitement extrait la règle de calcul, mais la fonction qu'il a développée pour la Base A facilite l'apprentissage et l'adaptation à la Base B. Ce transfert de connaissances améliore la généralisation sur les items non appris de la Base B.

### B. Résistance aux Lésions

L'apprentissage de structures compatibles améliore la robustesse de la mémoire dans les réseaux connectionnistes distribués.

- **Meilleure Performance** : Le rappel des items appris et la généralisation sont plus résistants aux lésions dans la condition d'apprentissage **compatible** (Add-Dec puis Add-Oct, ou concurrent) que dans la condition incompatible (Max et Add-Oct) ou isolée (Oct-Add seul).