
## I. Les Dilemmes Fondamentaux des Systèmes de Mémoire

Les systèmes de mémoire sont confrontés à deux dilemmes structurels majeurs qui déterminent leurs enjeux et leurs solutions possibles :

1. **Information Générale vs. Spécifique** : Comment un système peut-il à la fois capturer les structures de connaissances générales (sémantiques) et retenir les détails uniques d'événements spécifiques (épisodiques) ?
2. **Stabilité vs. Plasticité** : Comment le système peut-il rester **stable** et conserver les anciennes connaissances tout en étant suffisamment **plastique** pour intégrer rapidement de nouvelles informations ?

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

Pour que les capacités d'apprentissage d'un modèle Hebbien simple soient excellentes, les deux (exemple ci-dessus) entrées doivent être **orthogonales** entre elles (ex: $(-1, 1)$ et $(1, 1)$ (orthogonaux car -1x1 + 1x1 = 0)).

- **Conséquence sans Orthogonalité** : Sans orthogonalité, le système finit par souffrir d'**oubli catastrophique**.
- **Conséquence d'une Orthogonalité Totale** : Si toutes les entrées étaient systématiquement orthogonales, le système serait **incapable de généraliser** (c'est-à-dire de faire le lien entre différentes entrées).
- **Solution pour la Spécificité** : Pour obtenir une mémoire spécifique (évitant l'interférence), il faut un encodage orthogonal, rendu possible par un codage de type **'sparse'** (seuls certains neurones sont activés, augmentant les chances d'orthogonalité entre les patterns (plutôt que d'activer TOUS les neurones de manière partielle)).
	- Ainsi, pour savoir si une nouvelle entrée est orthogonale, il faut la comparer à toutes les autres entrées déjà présentes: pour être sur qu'elle soit bien orthogonale à chacune d'entre elle. On ne stockerait finalement (dans l'**hyppocampe**) que les entrées complètement nouvelles (celles qui ont des similitudes avec d'autres ne 'valent pas la peine' d'être apprises).
	- Et dans le reste du **cortex**, on stocke les points communs, la sémantique entre tous les différents éléments.

## III. Les Systèmes d'Apprentissage Complémentaires (Hippocampe/Néocortex)

Pour résoudre le dilemme stabilité/plasticité et gérer à la fois l'information générale et spécifique (dans un cadre Hebbien), la solution consiste à utiliser deux structures complémentaires, une idée développée par plusieurs modèles (Squire & Alvarez (95), Mc Clelland & Al. (95), Nadel & Moscowitch (97)).
![[nadel_mosco_rappe.png]]

### A. Rôles et Processus

| Système            | Cortex (Néocortex) / Trace System                                                                             | Hippocampe / Link System (Lobe Temporal Interne)                                                                                |
| :----------------- | :------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------ |
| **Rôle Principal** | Stockage **général** (sémantique). Apprend lentement la structure de cooccurrence. Trouve les points communs. | Stockage **spécifique** (épisodique). Apprend très rapidement les traces spécifiques. Crée instantanément une trace épisodique. |
| **Mécanisme**      | Basé sur l'accumulation **lente** et **intercalée** des changements synaptiques.                              | Permet un apprentissage **rapide** (One Shot Learning). Utilise un codage _sparse_ pour l'orthogonalité.                        |
| **Enseignement**   | Apprend à partir des traces épisodiques, qui servent de « professeur interne ».                               |                                                                                                                                 |

### B. Le Modèle TraceLink : Architecture et Dynamique

Le modèle TraceLink (Martijn Meeter & Jaap M.J. Murre, 1996-2006) met en œuvre cette complémentarité.

![[tracelink_general.png]]
#### 1. Architecture et Plasticité

- **Trace System (Cortex)** : 200 cellules, implémentant un système Hebbien dynamique. Un événement est décomposé en $K=10$ composants sémantiques. Ici, les activations des neurones correspondent à des *représentations fortes*.
- **Link System (Hippocampe)** : 42 cellules. Un événement active $K=7$ cellules (spécifié par les auteurs, arbitraire). Il est connecté à un système de modulation.
- **Fonctionnement** : Les unités utilisent une fonction sigmoïde pour déterminer leur activation ($a_i = 1$ ou $0$) en fonction de leur entrée nette $net_i$, modulée par l'inhibition pour assurer un codage _sparse_. L'inhibition permet aussi d'éviter que le système finisse par être complètement activé après plusieurs boucle d'apprentissage.
- **Règle de Plasticité** : La règle $\Delta W_{ij}=(\mu^{+}a_{i}a_{j})-(\mu^{-}a_{i}(1-a_{j}))$ induit à la fois l'apprentissage (terme $\mu^{+}$) et l'oubli (terme $\mu^{-}$).

#### 2. Différences des Taux d'Apprentissage (Réponse à Q1, 2022/2023)

Le **taux d'apprentissage $\mu$** doit être radicalement différent entre les systèmes pour respecter leurs rôles fonctionnels :

| Connexions                  | Taux $\mu$ (Acquisition) | Rôle / Justification                                                                                                         |
| :-------------------------- | :----------------------- | :--------------------------------------------------------------------------------------------------------------------------- |
| **Intra Link / Link-Trace** | **Élevé** ($\mu=0.4$)    | Assurer l'apprentissage **rapide** et _one-shot_ des associations spécifiques. Le Link System doit être hautement plastique. |
| **Intra Trace**             | **Faible** ($\mu=0.06$)  | Assurer l'apprentissage **lent et intercalé** de la structure sémantique pour éviter l'oubli catastrophique.                 |

#### 3. Modes d'Opération

- **Consolidation (Mode Interne)** : La trace est consolidée dans le Cortex (Trace System) par des activations générées à partir de bruit aléatoire.
    - Un très faible taux d'apprentissage est appliqué dans le Trace System ($\mu=0.0025$).
- **Apprentissage (Mode Externe)** : Le système utilise les taux $\mu$ élevés du Link System pour enregistrer rapidement l'épisode. Peu/Pas discuté dans le cours...

#### 4. Analogie avec l'apprentissage séquentiel humain

La mémoire humaine est capable d'apprendre séquentiellement: on peut apprendre de nouvelles choses sans oublier celles qui ont été apprises dans le passé.

**Probabilité de consolidation en fonction de l'ordre d'apprentissage**:
![[proba_consolidation_ordre.png]]

Malgré la consolidation plus courante du premier élément appris, celui-ci fini quand même pas être "le plus oublié" au final, après un long moment.

### C. Évidences Neuropsychologiques (Lésions)

- Les souvenirs les plus anciens sont maintenus (car consolidés dans le cortex), tandis que les souvenirs les plus récents (dépendants de l'hippocampe) sont perdus. ![[lesion_hypo.png]]![[oubli_lesion_control.png]]
	- Pour les patients lésionnés (link-system), la *courbe d'oubli* est croissante car les souvenirs ne sont retenus que par consolidations, aucun nouveau souvenir ne peut venir "écraser" les anciens (comme sur la courbe de consolidation du sujet sain vue ci-dessus).
	- **Amnésie Antérograde** : L'incapacité de former de nouveaux souvenirs survient immédiatement après la lésion du Link System.


- **Ictus Amnésique Transitoire (TGA)** : Simulé par $K=0$ dans le Link System. Pendant l'ictus, l'apprentissage est impossible, mais la récupération progressive de $K$ permet de retrouver les fonctions mnémoniques, à l'exception du souvenir appris pendant la période d'amnésie.![[ictus_simulation_result.png]]
	- Sur les graphes ci-dessus, la période d'amnésie est représentée en blanc (K=0). Le test de la mémoire est réalisé avec différentes valeurs de K. On reconnait la courbe de lésion dans le cas K=0. Dans la courbe en bas à droite, le patient a complètement récupéré au moment du test, le seul souvenir oublié est celui correspondant à l'apprentissage pendant l'ictus.

## IV. Réseaux à Hyperplans Séparateurs et Généralisation

Le fonctionnement des réseaux de neurones distribués, et notamment leur capacité à généraliser, repose sur la notion d'hyperplan séparateur.

### A. Principe de l'Hyperplan Séparateur

Dans un réseau de neurones à propagation avant :

1. **Calcul de l'Entrée Totale** : L'entrée totale d'une cellule de sortie est la somme des activations des cellules sources multipliées par leurs poids de connexion respectifs: $E_{tot} = \sum_{j}E_j*W_j$
2. **Seuil d'Activation** : La cellule de sortie ($S_1$) applique une fonction de seuil ($f$) à cette somme pondérée pour déterminer son activation ($0$ ou $1$): $S=f(E_{tot}) = f(\sum_{j}E_j*W_j)$
3. **L'Hyperplan** : Le réseau définit une frontière (point, droite, plan ou **hyperplan** en haute dimension) qui sépare l'espace d'entrée entre les sorties $S=0$ et $S=1$. ![[separation_E_S.png]]
4. **Apprentissage** : L'apprentissage consiste à ajuster les poids de connexion [W] (les seuls paramètres libres) de manière automatique et locale pour positionner l'hyperplan séparateur et minimiser l'erreur pour tous les exemples.
	1. *Modifier les poids de connexion revient à modifier la projection de l'espace d'entrée sur la première couche du réseau.*
	2. L'apprentissage est séquentiel, on apprend en regardant l'erreur sur un exemple, on modifie les poids, puis on présente l'exemple suivant. L'objectif est de minimiser l'erreur pour tous les exemples.
	3. En réalité, il y a des hyperparamètres pour ajuster l'apprentissage, les nouveaux poids sont calculés selon un paramètre d'inertie et un paramètre de 'rapidité' (à quel point les gros changements de poids sont autorisés ou pas).
	4. **Le point fondamentalement différent de l'apprentissage humain est que dans un réseau de neurone, il n'y a aucun stockage des exemples d'apprentissage. Ceux-ci ont simplement été des contraintes permettant de positionner l'hyperplan séparateur, ils ne sont pas gardés en mémoire.**

### B. Mémorisation et Réfutation du Stockage (Réponse à Q2, 2022/2023)

Dans les systèmes fonctionnant par séparation par hyperplan, l'assertion qu'un item est stocké en mémoire est fausse.

- **Pas de Stockage Explicite des Items** : **Il n'y a aucun stockage des exemples d'apprentissage dans le réseau de neurones**. Les exemples ne servent que de **contraintes** pour positionner l'hyperplan séparateur.
- **Mémoire = Fonction** : La mémoire réside dans la **fonction de re-création** (la configuration des poids) induite par l'apprentissage, et non dans les items eux-mêmes. Le réseau produit une sortie pour n'importe quelle entrée, même non entraînée.
- L'information est distribuée sur tous les paramètres du réseau de neurone et pas 'stockée' dans certaines cellules/neurones spécifiques.

Les système fonctionnant par séparation par hyperplan favorisent même des niveau de structuration dépassant largement la simple juxtaposition des relations entrées/sorties. En effet l'espace d'entrée est projeté sur les couches intérieures "où" une structure logique est extraites à partir des différents exemples appris (exemple des 'oiseaux' catégorisés ensemble car ils peuvent tous voler, sans forcément se ressembler physiquement; CF juste après). Ce genre de structure permet au réseau de neurones de faire des inférences bien au delà de simple rappel (par exemple, si j'apprends qu'un "torti" est un oiseau, alors je sais qu'il peut voler).

### C. Rôle des Couches Cachées et Nature de la Généralisation

Un réseau à une seule couche est limité aux problèmes linéairement séparables.
![[hyperplan_soucis_couche.png]]
L'ajout de couches cachées permet de dépasser cette limite et de transformer la nature de la généralisation.

- **Fonction des Couches Cachées** : Elles permettent de **projeter les entrées dans un nouvel espace façonné en fonction des contraintes d'apprentissage** (transformation non-linéaire). La fonction d'activation utilisée doit être non-linéaire et continue (e.g., Sigmoïde) pour permettre cette projection.
- **Généralisation par Découverte de Structure** : La non-linéarité permet de dépasser la simple juxtaposition des relations entrée-sortie (associationnisme). Le réseau capture la **structure** du domaine (les régularités logiques) à travers la succession d'exemples élémentaires.
	- **Déformation de l'Espace d'Entrée** : L'espace d'entrée est déformé dans les couches cachées de telle sorte que les concepts liés par la structure (e.g., les oiseaux) sont rapprochés, même s'ils ne se ressemblent pas physiquement.
	- **Inférer les Propriétés** : Une fois la structure apprise, l'apprentissage d'une nouvelle entité (ex: "torti" est un oiseau) permet au réseau d'inférer immédiatement ses propriétés associées, car il projette cette nouvelle entité dans la zone de l'espace caché correspondant à la catégorie apprise.

#### Exemple pédagogique McClelland & al. 1997

Le but est d'étudier comment un réseau peut capturer une structure simplement au travers de succession d'exemples élémentaires, et ceci *sans fonctionner en suivant la structure hiérarchique globale* (sans parcourir l'arbre total des catégories possibles).

![[mcclelland_97.png]]

- Il n'y a pas de ressemblance physique entre les éléments appris, mais une structure commune entre tous les exemples appris. Ils partagent systématiquement les mêmes caractéristique 'logiques'. 
- L'espace d'entrée d'éléments qui ne se ressemblent pas du tout entre eux est déformé dans la première couche cachée. Sur la figure suivante, les activations de la couche cachée (8 neurones) sont données pour divers exemples d'entrée (au fil de 25, 200 et 500 époques d'apprentissage):![[projection_couche_cachee.png]]
	- On observe qu'au fil des époques, les activations de la couche intermédiaire se spécialisent et laissent apparaitre des catégories (les animaux donnent des activations similaires entre elles; et celles-ci sont très différentes des activations provoquées par les entrée étant des végétaux;; de la même manière que les activations des poissons sont très similaires entre elle, et plus proche de celle des oiseaux que les activation des végétaux).
	- L'espace d'entrée à donc été déformé de telle sorte que les oiseaux et les végétaux soit 'déplacés' dans deux 'zones' différentes.

On comprends donc que si par la suite, on lui apprend qu'un "torti" est un oiseaux, il va le projeter du même coté de l'espace que les oiseaux. **Non pas parce qu'il ressemble à un oiseau**, mais parce que le réseau a "l'habitude" de faire cette association entre les entrées 'oiseaux' et les sorties. **C'est la répétition de relation entre entrée et sortie qui défini le comportement du réseau**, pas la ressemblance des entrées entre elles.
- **La couche cachée n'est pas un encodage des entrées, mais une projection de celle-ci; projection correspondant à celle qui a été utile pour résoudre la tâche (après apprentissage).** Autrement dit, la projection est influencée par le comportement attendu de toutes les couches entre elles (donc sur l'apprentissage des liens entre entrée et sorties).


> [!NOTE] Important
*Pourquoi cette généralisation n'est pas comme la généralisation "habituelle/basique" (celle basée sur la ressemblance des éléments d'entrée)?*
La généralisation est réalisée ici par une adaptation de **fonction** et non pas par un catégorisation dans l'espace des entrées. On a ici une généralisation sans avoir de représentation au sens fort (les neurones (de la couche cachée) ne sont pas là pour représenter/séparer les végétaux et les animaux; ni les oiseaux et les poissons); ils répondent juste à la fonction qui leur a été donnée.

## V. L'Oubli Catastrophique et la Solution des Pseudo-Exemples

### A. Sensibilité à l'Oubli Catastrophique (Réponse à Q3, 2022/2023)

Les réseaux distribués fonctionnant par séparation par hyperplan sont particulièrement sensibles à l'**oubli catastrophique**.

- **Définition** : L'oubli catastrophique est l'oubli dramatique des exemples antérieurement appris lors de l'apprentissage de nouveaux exemples.
- **Cause Principale** : Étant donné que la mémoire est codée dans les poids de connexion (la fonction de re-création), l'apprentissage séquentiel modifie ces poids pour satisfaire les nouvelles contraintes. Les anciens exemples **ne contraignent plus** la fonction, et les poids établis précédemment pour les anciens items sont largement altérés.
### B. L'Auto-Rafraîchissement par Pseudo-Exemples (PE)

La solution la plus efficace est l'auto-rafraîchissement par pseudo-exemples (PE), introduite par Robins (1995).

- **Principe Général** : Puisque nous ne disposons généralement pas des anciens exemples pour les répéter, on génère des **Pseudo-Exemples** à partir de bruit aléatoire. Ces PE sont des exemples de la **fonction de re-création** du réseau.
- **Processus de Création** : Un bruit aléatoire est injecté en entrée, et la sortie calculée par le réseau est le pseudo-exemple correspondant. Cette association Entrée-Bruit/Sortie-PE est un reflet de la fonction apprise.
- **Méthode** : Les PE sont créés, stockés dans une mémoire tampon, et ré-introduits lors de l'apprentissage des nouveaux exemples afin que **les connaissances passées continuent à contraindre la fonction**: ![[creationde_PE_auto_rafraich.png]]

### C. Améliorations Architecturales et Processus de Réverbération (Réponse à Q3)

Pour pallier les limites d'une mémoire tampon non neuromimétique et améliorer la résolution de l'oubli catastrophique, des architectures plus complexes sont utilisées :

#### 1. Proposition des Deux Structures Connectionnistes (Réseau Principal/Secondaire)

- **Principe de l'Architecture** : Utiliser un **Réseau Secondaire** pour apprendre les Pseudo-Exemples générés par le Réseau Principal: ![[prop_1_deux_structures.png]]
- **Fonctionnement** : Le Réseau Principal transfère sa fonction au Réseau Secondaire via des PE générés à partir de bruit. Ensuite, le Réseau Principal apprend les Nouveaux Exemples (apprentissage en situation réelle) en les couplant avec un pseudo-rafraîchissement provenant du Réseau Secondaire (ses propres connaissances antérieures).

#### 2. Rôle de la Réinjection (Réverbération)

- **Objectif** : Maximiser la capture de la **structure** dans les Pseudo-Exemples.
- **Méthode** : La sortie auto-associative (obtenue par injection de bruit) est réinjectée comme nouvelle entrée dans le réseau. L'enchaînement de plusieurs réinjections successives est appelé **réverbération**.
- **Bénéfice** : La réverbération permet à la sortie de converger vers les **points attracteurs** (souvent des minimums locaux) qui constituent d'excellents pseudo-exemples, même s'ils n'ont jamais été appris spécifiquement. La réverbération est cruciale, car l'auto-rafraîchissement **avec réverbération** réduit considérablement l'oubli catastrophique par rapport à l'auto-rafraîchissement simple:![[Apprentissage_sys.png]]

Finalement, *l'ordre des choses apprise a une importance*: lors de l'apprentissage de nouveaux exemples, ce n'est pas simplement l'exemple en soit qui est important, mais l'ensemble des connaissances préalables à cet exemple.

#### Résultats expérimentaux
**Cas d'école** (MacCloskey, 1989):
![[oubli_cata_fini.png]]
- Sans auto-raffraichissement: oubli catastrophique
- Avec auto-raffraichissement:
	- Sans réverbération: oubli partiel de l'ancienne base 
	- Avec réverbération: très peu d'oubli de l'ancienne base


## VI. Apprentissage Séquentiel et Transfert de Connaissances

### A. Transfert de Structure et Généralisation

L'apprentissage séquentiel permet d'étudier le transfert de structure entre domaines. La méthode est donnée sur l'image suivante: ![[sans_oubli_cata_transfert.png]]
En terme d'encodage dans le réseau, les opérations le sont tel qu'indiqué ci-dessous: ![[codage_no_oubli_.png]]

Et les résultats sont donnés ici:![[perf_max_add_octal_VS_decim.png]]
- A gauche sur l'image (condition compatible): on observe un oubli catastrophique de l'opération d'addition décimale lors de l'apprentissage de l'opération d'addiction octale sans rafraichissement, mais celui-ci n'est pas total (car la fonction réalisée reste une addition). On voit que l'oubli catastrophique n'as pas lieu avec rafraichissement.
- A droite sur l'image (condition incompatible): oubli catastrophique total de la fonction initialement apprise (max) dès les premiers cycles d'apprentissage de la fonction d'addition octale sans rafraichissement. Avec auto-rafraichissement, l'ancienne fonction est maintenue.

On teste ensuite la généralisation 'pure': on apprend sur la base de 229 items de la base octale, et on test sur la généralisation aux 687 autres éléments de cette base.
![[generalisation_add_dec_oct.png]]
(L'étoile correspond au cas où le pourcentage de réponse correcte est de 99% (arbitraire). On remarque qu'on observe pas de baisse de généralisation malgré un surapprentissage (parce que le signal d'entrée n'est absolument pas bruité, du fait de l'encodage présenté ci-dessus))

- **Observations**: Sur la courbe verte, on a déjà appris add-dec; on remarque que la généralisation à add-oct est possible dès le premier cycle d'apprentissage. On considère (une interprétation possible est) que la règle de calcul est apprise (la structure du problème), et que sa transmission/son adaptation sur une nouvelle base est plus rapide. En réalité, **le réseau de neurone n'as pas extrait la règle de calcul**, pourtant, les résultats sont similaire à "si il l'avait fait".

### B. Résistance aux Lésions

L'apprentissage de structures compatibles améliore la robustesse de la mémoire dans les réseaux connexionnistes distribués: ![[resist_lesion_.png]]

- **Meilleure Performance** : Le rappel des items appris et la généralisation sont plus résistants aux lésions dans la condition d'apprentissage **compatible** (Add-Dec puis Add-Oct, ou concurrent) que dans la condition incompatible (Max et Add-Oct) ou isolée (Oct-Add seul).


### C. Transfert à partir de Pseudo-Exemples

#### Qu'apprennent les Systèmes Distribués ?

L'enjeu central est de déterminer la nature de ce qui est encodé dans un système connectionniste distribué (et, par extension, dans la mémoire humaine). Deux hypothèses s'affrontent :

1. **Hypothèse des Exemplaires/Prototypes** : Le système mémorise les caractéristiques physiques des items vécus. La performance dépendrait alors de la ressemblance entre les nouveaux items et les exemplaires stockés.
2. **Hypothèse Fonctionnelle (Hyperplan)** : Le système n'apprend pas les items eux-mêmes, mais une **fonction de re-création** (la configuration des poids [W]). La mémoire réside dans la capacité à projeter n'importe quelle entrée vers un état stable (attracteur) défini par cette fonction.

#### Le Paradigme Expérimental (Musca, Rousset & Ans, 2004)

Pour trancher entre ces hypothèses, l'étude utilise le transfert par **Pseudo-Exemples (PE)** entre deux réseaux (ou entre un réseau et un humain).

##### A. Procédure et Architecture

![[transfert_pseudo_ex.png]]
- **Net 1** : Ce premier réseau apprend une liste d'**Items Sources** (Liste 1). Ces stimuli sont des formes géométriques aléatoires (8x8 pixels) conçues pour ne rien évoquer de connu afin d'éviter les biais d'apprentissage antérieurs:![[forme_PE_humain.png]]
- **Génération et Filtrage des PE** : On injecte du bruit aléatoire dans Net 1 pour générer des Pseudo-Exemples. Un **filtrage crucial** est opéré : on ne conserve que les PE qui ressemblent physiquement aux **Items Contrôles** (Liste 2, que Net 1 n'a jamais vus) et qui sont physiquement éloignés des Items Sources.
- **Apprentissage de Net 2 (ou de l'Humain)** : On entraîne Net 2 (ou le sujet humain) exclusivement sur ces **PE filtrés**.

##### B. Les Prédictions

- **Si la mémoire est basée sur les exemplaires** : Net 2 devrait être plus performant sur les **Items Contrôles**, car son entraînement (les PE filtrés) leur ressemblait physiquement.
- **Si la mémoire est basée sur la fonction** : Net 2 devrait être plus performant sur les **Items Sources**. En effet, les PE, bien que ressemblant physiquement aux items contrôles, sont le produit de la fonction de Net 1 (ses attracteurs). Net 2 devrait donc "capturer" la structure logique de Net 1 au-delà des apparences.

#### III. Résultats et Interprétation

##### A. Simulations Connectionnistes (Net 2)

![[resultats_l1_l2.png]]
Les résultats montrent sans ambiguïté que **Net 2 présente une erreur (RMS) bien plus faible pour les Items Sources** que pour les Items Contrôles. Le réseau a donc bien appris la "fonction" de Net 1 via les pseudo-exemples, et non les caractéristiques physiques superficielles du matériel d'entraînement.

##### B. Études Comportementales chez l'Humain

Les mêmes tests ont été appliqués à des participants humains via deux tâches :

1. **Tâche de Fluidité Perceptive** : On présente des items pendant une durée identique. Les sujets ont tendance à juger comme étant "plus longs" les stimuli qu'ils reconnaissent le mieux (car ils s'y adaptent plus vite). Les résultats montrent que les **Items Sources sont jugés plus longs** que les items contrôles.
2. **Tâche de Reconnaissance d'Occurrences** : Les sujets identifient plus fréquemment les items sources, bien qu'ils n'aient été exposés qu'à des pseudo-exemples ressemblant aux items contrôles.

##### C. Conclusion sur la Nature de la Mémoire

Ces résultats confirment que la mémoire humaine, dans ce contexte, fonctionne comme un **système distribué apprenant un hyperplan séparateur**.

- Le transfert d'information ne se fait pas par la copie d'exemplaires, mais par la capture de la **structure interne** du domaine (la fonction).
- Cela valide l'idée que le cerveau peut extraire des régularités logiques à partir de stimuli qui ne se ressemblent pas physiquement, en utilisant des attracteurs créés par l'apprentissage.
