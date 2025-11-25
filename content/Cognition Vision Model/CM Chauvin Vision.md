---
prof: CHAUVIN Alan
date: 2025-11-17
publish: true
---
 
> [!NOTE] Examen
> Surement 30% de la note vient du TP
> 70% sur un examen classique de question de cours + analyse d'expérience

# Définir l'environnement visuel

Le "*gist*": informations sémantiques et perceptives d'une scène visuelle extraites en quelques millisecondes. Composé de :
- catégorie (scène de plage, ...)
- surface (plage, eau, ..)
- objet (barque, ..)
- affordances émotionnelles (chaleur, bien-être, ;..)

Tous ces éléments sont extraits *rapidement* et *automatiquement*, nous sommes capables de catégoriser en très peu de temps à partir d'une grande variabilité potentielles (scènes de plage, scènes de villes, ..).

Chaque scène peut être décomposée en plusieurs sous-scènes ou éléments.

"Creating consistent scene graphs using a probabilistic grammar" (2014).

-> Limites de l'approche déscendantes où l'on part de nos connaissance pour dérire une scène visuelle.

## Approche ascendante
Décrire une scène en s'appuyant sur les into extraites apr le système visuel à différentes étapes de traitement
### Vision structurale (Marr 1982)
Vision par étapes:
- *Primal sketch (2D)*: 
	- lignes, jonctions, contours, couleurs, mouvement
- *2.5D*: 
	- Surface: texture, ombre, disparité
	- Centrée sur l'obeservateur
	- Non organisée en structure
- *3D*:
	- Axes d'élongation/symétrie de l'objet
	- Structuration des surfaces en objet perceptif en utilisant les axes de l'objet comme référentiel spatial
	- Représentation structurale centrée sur l'objet
- *Catégorisation (Palmer)*:
	- Propriétés, fonctions XX de/des objets
	- Utilisation, affordance

### Hypothèses de l'approche (CF slides):

### Modèle utilisé
On considère l'image comme un ensemble discret de pixels. Ses propriétés sont:
- Sa *résolution*: dimensions de la matrice
- Sa *quantification* intensité des pixels, classiquement encodé sur 8 bits, donc 256 valeurs de nuances de gris possibles.
- Pour les images *couleurs*, chaque pixel est représenté par 3 valeurs de luminance de:
		- Rouge
		- Vert
		- Bleu
- Pour les films, le *mouvement* est aussi encodé, il correspond au déplacement d'éléments au fil du temps
- La *profondeur*, principalement grâce à des indices monoculaires:
	- Ombres, occlusions, perspectives, hauteur et tailles relatives des objets et des gradients de textures
	- Mais aussi à des indices binoculaires (décalage de l'information visuelle entre l'œil droit et le gauche)

*Pixel*: "Picture element", élément de base d'une image. Chaque pixel, à une position (x,y) a donc
- Une luminance à 2 dimensions
- Une couleur (+1 dimension), sur 3 canaux
- Le temps (+1 dimension)
- La 3D (+1 dimension)

5 dimensions finalement, donc une énorme variabilité potentielle. Comment catégoriser les différences et similitudes efficacement?
- Moyennage: Peu efficace (CF slides pour images)
- Calcul du MSE (Mean Squared Error), sur les différences entre 2 matrices d'images.
	- Peut être généralisée au calcul de la norme $L_p$, plus pratique dans des problèmes avec plus de dimensions.
	- Mais la MSE n'est performante que dans le cas de l'ajout de bruit, si l'on applique une rotation ou autre transformation (translation), la MSE calculée est très grande alors que l'image reste perceptivement très similaire. Autrement dit, *la MSE est très sensible aux variations de déplacement dans l'espace, mais pertinente pour les variations de luminance.*
- L'espace de Fourier permet un autre espace de représentation de l'image, qui rend mieux compte des positions des pixels.

#### Transformé de Fourier
Le principe de base vient du traitement de signal, n'importe quel signal peut être décomposé en une somme de signaux sinusoïdaux. Pour faire le lien avec les images, on s'intéresse à la représentation trigonométrique des sinusoïdes. Les sinusoïdes sont définies de la manière suivante:
$$x(t)=A*sin(\frac{2\pi}{T}t+\phi)$$
Avec:
- A, l'amplitude du signal (distance maximale par rapport à 0)
- T, période (en seconde)
- $\Phi$, déphasage (en radiant)

La transformée de Fourier (TF) est une *fonction complexe* de la variable réelle f définie par:
$$X(f)= \int_{-\infty}^{\infty} x(t)exp(-j2\pi ft) dt$$
Elle exprime la *répartition de l'amplitude et de la phase de l'énergie* d'un signal en *fonction des fréquences*.
![[Fourier_basique.png]]

Grâce à la transformée de Fourier, on peut représenter des sinusoïdales (représentée normalement par une infinité de points) à partir de seulement les informations d'amplitude et de fréquence (donc 2 point par sinusoïde).

Pour repasser aux images, on peut considérer que 
- l'amplitude correspond à l'intensité des pixels (luminance)
- la fréquence exprimée en cycles/images correspond à l'espace
- Et il faut ajouter une information d'orientation des sinusoïdes pour reconstruire n'importe quelle image.

![[fourier_image.png]]
Une autre représentation d'une image dans le domaine de Fourier est le suivant:
![[fourier_representation2D.png]]
Sur la partie droite de l'image (*Spectre d'Amplitude, SA*), le centre correspond à la valeur moyenne de l'image (en intensité), les points fonctionnent toujours par paires, symétriques au centre. Chaque *paire correspond à une sinusoïde*, leur *espacement* donne l'information de *fréquence*. Et leur position donne l'*orientation* de la sinusoïde. On remarque sur cette image là (et c'est vrai en général aussi, pour toutes les images de scènes naturelles) une concentrations de basses fréquences (plus de points au centre).
Une autre représentation existe (*Spectre de Phase, SP*), souvent moins lisible. CF slides pour explication/illustration.

Une expérience basée sur un amorçage en SA ou SP puis catégorisation d'image a montré que notre système perceptif se *base plutôt sur le SA pour catégoriser des scènes* (de plages et de villes, dont les spectres sont clairement différents (horizontal plage VS vertical ville).

Le SA semble donc être un bon descripteur de la catégorie des scènes. 
![[img_2_fourier_examples.png]]
Pour analyser complètement des scène, on pourrait donc modéliser le système perceptif humain par un système d'extraction en parallèle d'une information localisée à différentes orientations et différentes fréquences spatiales.

Possibilité aussi de réaliser des TF de manière localisée sur l'image:
![[TF8locale.png]]

Pour extraire uniquement une information spécifique de l'image (une certaines gamme de fréquence), on peut appliquer la transformée de Fourier et la coupler à un filtrage (HF, BF, ...), le filtrage est alors fréquentiel. Un autre moyen est le filtrage par convolution, dans le domaine spatial plutôt que fréquentiel, on balaye alors l'image avec un filtre de convolution.
Mais une multiplication en fréquentiel équivaut à une convolution en spatial (par la transformée de Fourier inverse du filtre fréquentiel) et inversement. 

Aux différents niveaux de traitement de l'information visuelle, les cellules du système visuel agissent comme des filtres spatiaux (de convolution) permettant d'extraire ("filtrer") différents types d'information.

![[visuel_lien_fourier_humain.png]]



# Définir le traitement de l'information visuelle

## CF Cours vision KAUFMANN
Rétine, cones, batonets, champ recepteurs, résolution non homogène sur la rétine, cellule bipolaire : centre ON/periph OFF etc...

Modèle: 
- Photorecepteur (sensibilité etc.. TODO: des nouvelles slides)
- Cellule ganglionnaires
![[model_ganglio_1.png]]

![[model_ganglion_2.png]]

- Forme de « compression »: fortes corrélations entre des points voisins dans le champs visuel → n’extraire que les différences de luminance les plus importantes (=forts contrastes) pour éviter une redondance de l’information 
- « Blanchiment spectral » : réhaussement du contraste des HFS

Différents types de cellules ganglionaires:
- Les cellules « Parasol » ou de type M (Magno): Grand corps cellulaire. Plus présentes en périphérie qu’en fovéa, intègrent l’information d’un grand nombre de cellules bipolaires → Large champ récepteur. Elle présentent une réponse phasique à de faibles ou rapides changements de contraste véhiculée rapidement le long du nerf optique. ~10 à 20% des cellules du primate.
	- Extraction de contours grossiers: BF
- Les cellules « Midget » ou de type P (Parvo): Petit corps cellulaire. Plus présentes au centre de la rétine qu’en périphérie, intègrent l’information d’une ou quelques cellules bipolaires → Petit champ récepteur. Elles présentent une réponse soutenue (tonique) à des forts contrastes de couleur ou de luminance véhiculée plus lentement le long du nerf optique. ~70 à 80% des cellules du primate
	- Extraction de contours grossiers: HF
- Les cellules Non-M/non-P ou K (konio): propriétés moins bien connues, ~7 à 10% des cellules du primate.