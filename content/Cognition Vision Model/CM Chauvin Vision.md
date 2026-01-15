---
prof: CHAUVIN Alan
date: 2025-11-17
publish: true
---

> [!NOTE] Examen
> 
> - **Répartition de la note** : Environ 30% TP / 70% Examen.
>     
> - **Format de l'examen** : Questions de cours classiques + analyse d'expérience.
>     

# Introduction : De la physique à la perception

L'objectif de ce cours est de comprendre les mécanismes par lesquels le système visuel transforme un signal physique (lumière) en une perception sémantique (sens).

## Vue d'ensemble du cours

1. **L'environnement visuel** : Définition de l'image, statistiques des scènes naturelles et modélisation par l'espace de Fourier.
2. **Traitement précoce (Rétine)** : Transduction, compression de l'information et filtrage initial.
3. **Traitement central (Cortex)** : Architecture de V1, extraction des traits (orientation, fréquence), et spécialisation des aires supérieures (V2, V4, V5, IT).
    
# 1. L'environnement visuel et l'approche computationnelle

## A. Comprendre la scène visuelle

### 1. Le "Gist" (L'essence d'une scène)

Le système visuel extrait le **"gist"** d'une scène en quelques millisecondes de manière automatique. Ce concept englobe :
- **La catégorie sémantique** (ex: plage, rue, forêt).
- **La structure globale** (ex: espace ouvert/fermé).
- **Les surfaces et objets dominants**.
- **Les affordances émotionnelles** (danger, chaleur, navigation possible).
    
### 2. Les approches théoriques

Il existe deux manières principales d'aborder la vision :
- **Approche Descendante (Top-down)** : La perception est guidée par les connaissances préalables et le contexte (ex: chercher des chaises parce qu'on est dans une classe). _Limite : nécessite des schémas préexistants._
- **Approche Ascendante (Bottom-up)** : _Approche privilégiée dans ce cours._ La perception se construit étape par étape à partir du signal brut.
    
### 3. La vision structurale (Modèle de Marr, 1982)

David Marr propose un modèle de reconstruction 3D séquentiel (Bottom-up) :
1. **Primal Sketch (Esquisse 2D)** : Extraction des contours, lignes et contrastes de base.
2. **2.5D Sketch** : Reconstruction des surfaces du point de vue de l'observateur (profondeur locale, texture, ombres). _Ce n'est pas encore de la 3D car les faces cachées sont inconnues._
3. **Modèle 3D** : Représentation centrée sur l'objet (indépendante du point de vue), utilisant des axes de symétrie.
4. **Catégorisation (Palmer)** : Identification sémantique et fonctionnelle de l'objet.
    
## B. Modélisation de l'image numérique

Pour étudier la vision, l'image numérique (matrice de pixels) sert de modèle à l'image rétinienne. Elle possède deux propriétés principale: sa *résolution* (nombre de pixels) et sa *quantification* (encodage, par exemple 8 bits = 256 niveaux de gris).

### 1. Le Pixel : Information locale

Un pixel à une position $(x, y)$ contient 5 dimensions d'information :
- **Luminance (2D)** : Intensité lumineuse.
- **Couleur (+1D)** : 3 canaux (RGB).
- **Temps (+1D)** : Variation temporelle (vidéo).
- **Profondeur (+1D)** : Indices *binoculaires* (disparité) et *monoculaires* (ombres, perspective, taille).
    
### 2. Mesurer la similitude entre deux images

Comment le cerveau (ou un ordinateur) compare-t-il deux images ?

- **La Moyenne** : Inefficace, mélange tout en gris.
- **Le MSE (Mean Squared Error)** : Différence pixel par pixel. Très efficace pour détecter du bruit.
    - _Problème majeur_ : Le MSE est trop sensible aux transformations spatiales. Un simple décalage de quelques pixels change totalement le score MSE alors que l'image est perceptivement identique pour un humain. **Le pixel n'est pas la bonne unité de mesure sémantique.**
        
### 3. L'espace de Fourier : Une représentation fréquentielle

La Transformée de Fourier (TF) est un outil puissant car elle est robuste aux translations et sépare l'information de manière pertinente.

**Principe théorique :** Tout signal complexe est une somme de sinusoïdes définies par :

$$x(t) = A \cdot \sin(\frac{2\pi}{T}t + \phi)$$

Où $A$ est l'amplitude (contraste), $T$ la période (inverse de la fréquence) et $\phi$ la phase (position).

La TF convertit l'image du domaine spatial vers le domaine fréquentiel :

$$X(f)= \int_{-\infty}^{\infty} x(t)\exp(-j2\pi ft) dt$$
![[Fourier_basique.png]] ![[fourier_image.png]]

**Décomposition de l'image en deux spectres :**
1. **Spectre d'Amplitude (SA) - "Le Quoi"** :
	- ![[fourier_representation2D.png]]

    - Indique la quantité d'énergie pour chaque fréquence et orientation.
    - **Centre** = Basses Fréquences (BF) $\to$ Formes globales, "Gist".
    - **Périphérie** = Hautes Fréquences (HF) $\to$ Détails, bords fins.
    - **Loi en $1/f$** : Les scènes naturelles ont beaucoup d'énergie en BF et peu en HF.
    - L'orientation des points indique l'orientation des motifs dans l'image (ex: une scène de ville avec des immeubles verticaux aura de l'énergie sur l'axe horizontal du spectre).
    - _Lien perceptif_ : Le cerveau utilise le SA pour la catégorisation rapide (ex: ville = lignes verticales/horizontales; nature = orientations variées).
2. **Spectre de Phase (SP) - "Le Où"** :
    - Contient la position des ondes. C'est lui qui encode la **structure des bords** et l'identité précise des objets.
    - Moins lisible 'naturellement'
 

> [!NOTE] Expérience des Images Hybrides
> 
> Si on mélange l'Amplitude de l'image A avec la Phase de l'image B :
> 
> - L'image ressemble structurellement à B (la phase donne la forme).
>     
> - Mais on perçoit la "texture" de A.
>     
> - Pour la catégorisation ultra-rapide, le cerveau s'appuie d'abord sur les régularités statistiques de l'Amplitude.
>     

Finalement, le spectre d'amplitude semble être un bon indicateur de la catégorie des scènes:
![[img_2_fourier_examples.png]]

### 4. Le lien avec le système visuel (Filtrage local)

Attention : Le cerveau ne calcule pas une TF globale sur toute l'image.

Il fonctionne par filtrage local (convolution). Cependant, grâce au théorème de convolution (convolution spatiale <=> multiplication fréquentielle), appliquer des filtres locaux (comme ceux de Gabor) revient à analyser les fréquences locales. Le modèle de Fourier est donc une excellente approximation de ce que fait le cortex visuel.

![[TF8locale.png]] ![[visuel_lien_fourier_humain.png]]


# 2. La Rétine : Traitement et compression

La rétine n'est pas une simple caméra. Elle effectue un pré-traitement complexe (compression, accentuation des contrastes, adaptation) avant d'envoyer l'info au cerveau.

## A. Transduction : Les Photorécepteurs

Conversion de la lumière en signal électrique.
- **Modèle 1 : Dynamique et Adaptation (Naka-Rushton)**
    - La réponse n'est pas linéaire mais quasi-logarithmique (saturation aux extrêmes).
    - Adaptation : Le système ajuste sa sensibilité autour de la luminosité ambiante ($L_0$) pour maximiser la perception des contrastes, que l'on soit en plein soleil ou dans l'obscurité.
        ![[dynamique_reponse_photorecept.png]]
- **Modèle 2 : Rétinotopie et Échantillonnage**
    - **Fovéa (Centre)** : Densité maximale de **Cônes**. Vision des détails (haute résolution), couleur, vision diurne.
    - **Périphérie** : Dominée par les **Bâtonnets**. Vision du mouvement, basse résolution, vision nocturne.
    - Conséquence : La résolution spatiale chute drastiquement dès qu'on s'éloigne du centre du regard.
        ![[Répartition_photorecepteur_retine.png]]
- **Phénomène de Convergence**
    - _Fovéa_ : 1 Cône $\to$ 1 Bipolaire $\to$ 1 Ganglionnaire (Pas de perte de détails).
    - Périphérie : ~1000 Bâtonnets $\to$ 1 Ganglionnaire (Sommation spatiale = gain de sensibilité à la lumière, mais perte de précision).
        ![[convergence_photorecepteur.png]]
## B. Traitement du signal : Couche Plexiforme & Bipolaires

- **Modèle 4 : Filtrage électrique et inhibition latérale**
    - Les **cellules horizontales** connectent les photorécepteurs entre eux et lissent le signal (moyenne locale). On parle de '*gap junction*'.
    - Les cellules bipolaires soustraient ce signal moyen du signal direct. Cela crée des champs récepteurs antagonistes (centre ON/Périphérie OFF ou inversement).
        ![[modele_4_elec_bg.png]] ![[resume_filtre_cellule_bipo.png]]
- **Champs Récepteurs (CR) Centre-Périphérie**
    - **Centre ON / Périphérie OFF** : S'active si la lumière est au centre, s'inhibe si elle est autour.
    - **Fonction** : Détecter les **contrastes locaux** (bords) plutôt que la lumière absolue.
        
## C. La Sortie : Cellules Ganglionnaires

- **Modèle 3 : Différence de Gaussiennes (DoG)**
    - Le champ récepteur est modélisé par un filtre "Chapeau Mexicain" (une gaussienne centrale positive moins une gaussienne périphérique large négative).
        ![[model_ganglio_1.png]] ![[model_ganglion_2.png]]
- **Blanchiment Spectral (Spectral Whitening)**
    - Les images naturelles ont trop de Basses Fréquences (redondance).
    - Le filtre ganglionnaire atténue ces BF et rehausse les Hautes Fréquences. Cela "égalise" (blanchit) le spectre pour rendre l'information plus efficace à transmettre.
        
### Les 3 voies parallèles (M, P, K)

L'information est séparée dès la rétine en canaux distincts :

|**Type**|**Nom**|**Propriétés**|**Fonction**|
|---|---|---|---|
|**M**|**Magnocellulaire** ("Parasol")|Gros corps, gros CR, rapide (phasique).|**Mouvement**, Scintillement, **Basses Fréquences (BF)**. Aveugle à la couleur.|
|**P**|**Parvocellulaire** ("Midget")|Petit corps, petit CR, lente (tonique).|**Détails fins (HF)**, Forme, Couleur (Rouge/Vert).|
|**K**|**Koniocellulaire**|Intermédiaire.|Couleur (Bleu/Jaune).|

> [!NOTE] Principe "Coarse-to-Fine"
> 
> La voie Magno (BF, rapide) transmet la structure globale ("gist") avant que la voie Parvo (HF, lente) n'apporte les détails.

![[spatio_temp_rep.png]]

Sur la courbe ci-dessus, chaque couleur correspond à un type de cellule:
- Magno cellulaire Y (orange): Passe très bas puis passe haut (2 passe bandes)
- Magno cellulaire LF-X (bleu): Passe bas
- Parvo cellulaire HF-X (rouge): Passe haut
Finalement, les prédictions qui peuvent être faites:  

![[prediction_magno_parvo.png]]

### La "Smart Retina"

La rétine effectue des calculs prédictifs :
- Détection de mouvement local.
- Anticipation de trajectoire pour compenser les délais neuronaux.
- Distinction entre le mouvement d'un objet et le mouvement de l'œil.
    ![[smart_retina_mvmnt.png]]
    

### Synthèse des couches rétiniennes

![[synthese_couche_photorecept.png]]

1. **Photorécepteurs** (Transduction).
2. **Couche Plexiforme Externe** : Synapses Photorécepteurs / Horizontales / Bipolaires.
3. **Couche Plexiforme Interne** : Synapses Bipolaires / Amacrines / Ganglionnaires.
4. Cellules Ganglionnaires (Émission des potentiels d'action via le nerf optique).
    ![[resume_ganglionaires.png]]
    

# 3. De la Rétine au Cortex (V1)

## A. Le trajet optique

1. **Nerf Optique** : Sortie de l'œil.
2. **Chiasma Optique** :
    - Décussation partielle : Les hémirétines nasales croisent, les temporales restent du même côté.
    - Résultat : L'hémisphère gauche traite le champ visuel droit (et inversement).
        ![[champ_visuel.png]]
3. **Corps Genouillé Latéral (CGL - Thalamus)** : Relais principal (90% des fibres).
4. **Colliculus Supérieur** : Orientation réflexe et inconsciente (10% des fibres).

## B. Le Corps Genouillé Latéral (CGL)

- **Organisation** : 6 couches qui conservent la rétinotopie et la séparation Magno (couches 1-2) / Parvo (couches 3-6).
- **Rôle** : Porte d'entrée vers le cortex, *modulation attentionnelle*.
- Feedback : Reçoit plus de connexions descendantes du cortex (V1) que d'entrées rétiniennes ! Cela prouve l'importance des processus Top-down.
    ![[resume_retineècgl_magno_parvo.png]]
    

# 4. Le Cortex Visuel Primaire (V1, strié)

V1 décompose l'image en traits élémentaires (orientations, fréquences).

## A. Propriétés architecturales

1. **Rétinotopie** : Conservation de la carte spatiale de la rétine.
2. **Magnification corticale** : La fovéa (1% de la rétine) mobilise ~50% des neurones de V1.
    ![[V1_repartition.png]]
3. **Organisation laminaire** : Les entrées du CGL arrivent dans la couche 4 (IVC), en conservant la ségrégation Magno (Alpha)/Parvo (Beta).
    ![[V1_laminaire_magno_parvo.png]]
    

## B. Les Cellules de V1 (Hubel & Wiesel)

Hubel & Wiesel (Prix Nobel) ont découvert que les neurones de V1 ne répondent plus à des points (comme la rétine), mais à des **lignes orientées**.

### 1. Cellules Simples (Sélectivité), couche 4 & 6

- Sensibles à l'**orientation**, à la **fréquence spatiale** et à la **position exacte** (phase) de la barre lumineuse dans le champ récepteur.
- Modélisation : Alignement de plusieurs cellules ganglionnaires (Centre-ON) pour former un champ récepteur allongé.
    ![[champ_recept_bars.png]]
    
- **Modèle Mathématique (Filtre de Gabor)** :
    - Le CR est le produit d'une Gaussienne (localisation) et d'une Sinusoïde (fréquence/orientation).
    - $G(x,y) = \text{Gaussienne}(x,y) \times \text{Sinusoïde}(x,y)$.
    - Correspond à la partie Réelle ou Imaginaire du filtre.
        ![[gabor_reel_imag.png]]
    
### 2. Cellules Complexes (Invariance)

- Sensibles à l'**orientation** mais **insensibles à la position exacte** (invariance de phase). Elles répondent tant que la barre orientée est quelque part dans le champ récepteur (souvent sensible aussi au mouvement de cette barre).
- **Modélisation** : Sommation de plusieurs cellules simples.
- Mathématiquement : Correspond au module (l'énergie) du filtre de Gabor ($\sqrt{Réel^2 + Imaginaire^2}$).
    
    ![[gabor_representation.png]]
    

### 3. Preuves expérimentales (Aftereffects)

Fixer longtemps des lignes inclinées vers la gauche fatigue les neurones sélectifs à cette orientation. Si on regarde ensuite des lignes verticales, elles sembleront pencher vers la droite (les neurones "gauches" étant fatigués, les neurones "droits" dominent relativemet).
Cela prouve l'existence de populations de neurones dédiées (canaux) pour l'orientation et la fréquence spatiale.

![[adaptation_orientation.png]] ![[adaptation_freq_spatiale.png]]

## C. Organisation fonctionnelle : L'Hypercolonne

V1 est pavé de modules appelés **Hypercolonnes**. Chaque hypercolonne analyse une petite portion de l'espace visuel et contient :
1. **Colonnes d'orientation** : Ensembles de neurones sensibles à certaines orientations, couvrant, ensemble, toutes les orientations possibles.
2. **Colonnes de dominance oculaire** (Œil gauche/droit).
3. **Blobs** : Traitement de la couleur.
4. **Fréquences spatiales** : Ensembles de neurones répondant à différentes finesses de détails.

Ainsi, l'organisation spatiale garantit la permanence de l'objet : si un objet tourne ou bouge légèrement, l'activité se déplace simplement vers la colonne voisine au sein du même module ou vers le module adjacent.

![[couche_colonne_V1.png]] ![[hypercolone_simplifie.png]]

**Modélisation**:
En vision artificielle, on utilise typiquement un banc de filtres de Gabor (plusieurs tailles et orientations) pour simuler le traitement effectué par une hypercolonne.
![[gabor_banc_filtre.png]]

Mais d'autres approches sont aussi possibles:
> Approche ICA (Independent Component Analysis) : Des algorithmes comme ceux de Hosoya & Hyvärinen montrent que si l'on cherche à extraire statistiquement les composantes indépendantes des images naturelles, on retrouve exactement ces formes de filtres de Gabor. L'architecture de V1 est donc une adaptation statistique optimale à notre environnement visuel.
> ![[decompo_indepdnante_image_.png]]

## D. Résumé du flux Rétine $\to$ V1

1. **Rétine/CGL** : Analyse par points (Champs récepteurs circulaires, Différence de Gaussiennes (filtre chapeau méxicain)). Formation des voies P/M/K au niveau du CGL.
2. **V1 (Cellules Simples)** : Convergence des points (cellule ganglionnaires ON/OFF) $\to$ Détection de lignes orientées (Filtres de Gabor, phase précise).
3. **V1 (Cellules Complexes)** : Convergence des lignes (cellules simples) $\to$ Invariance de position (Énergie de Gabor, phase ignorée), mais toujours préférence à une orientation et fréquence spécifique.
    


# 5. Au-delà de V1 : Le Cortex Extrastrié

L'information est ensuite distribuée vers deux grandes voies corticales.

![[audela_V1_extrastrie.png]]
![[audela_V1_detail.png]]

## A. La Voie Dorsale ("Where" / "How") - Pariétale

_Origine principale : Voie Magno (Basses Fréquences)._
- **Fonction** : Localisation spatiale, guidage de l'action, détection du mouvement.
- **V5 / MT (Middle Temporal)** : Le centre du mouvement.
    - Détecte la **cohérence du mouvement** globale (combien de pixels vont dans la même direction).
    - Très sensible : Les neurones répondent même avec seulement 1-2% de points cohérents dans un nuage de bruit (Newsome & Paré, 1988).
    - Lésion de V5 : **Akinétopsie** (vision saccadée/stroboscopique, incapacité à percevoir la fluidité).
        
## B. La Voie Ventrale ("What") - Temporale

_Origine principale : Voie Parvo (Hautes Fréquences + Couleur)._
- **Fonction** : Reconnaissance d'objets, visages, lecture.
- **Hiérarchie d'abstraction (Pooling)** :
    1. **V1** : Barres orientées.
    2. **V2** : Formes simples, contours illusoires, angles.
    3. **V4** : Formes 3D, courbures complexes, **couleur**.
    4. Cortex IT (Inféro-Temporal) : Objets complets, concepts.
        ![[voie_ventrale.png]]
        

### Focus sur l'Aire Inféro-Temporale (IT)

Les neurones y répondent à des objets spécifiques avec une grande **invariance** (taille, position, angle de vue).
- L'organisation en colonnes permet un continuum de représentation (ex: rotation d'un visage).
    ![[invariance_rotation_objet_IT.png]]
    


# 6. Approfondissement : Mouvement et Intégration

## Le Mouvement dans V1 et V3

- **V1** : Contient des cellules simples sélectives à la direction du mouvement.
    - Leur champ récepteur est orienté dans l'espace $(X)$ et dans le temps $(T)$.
    - $RF(X,T) = Gabor(X) \times \text{Fonction}(T)$.
    - Cela permet de détecter une direction locale.
        ![[spatial_temporal_resp.png]]
        
- **V3** : Les activités de V1 sont combinées pour extraire des informations de mouvements et rendre possible l'extraction de bords à partir de mouvement (typiquement dans du bruit, où l'extraction serait impossible sans mouvement) (Zeki, 1993). Ici encore, les informations des premières aires visuelles sont combinées dans les aires supérieures.

**Akinétopsie**: Agnosie visuelle du mouvement. -> La vie est comme un filme stroboscopique.

## Types de Mouvement
- **Mouvement Constant** : Déplacement continu.    
- **Mouvement Apparent** : Illusion de mouvement créée par une succession rapide d'images statiques (stroboscope, cinéma).
    

# 7. Limites du modèle et Phénomènes complexes

## A. Limites de la hiérarchie pure

Le modèle classique (V1 $\to$ V2 $\to$ IT $\to$ Concept) a des limites.

### 1. Le mythe du "Neurone Grand-Mère"

*Logiquement la finalité d’un modèle hiérarchique est la reconstruction des objets et en particuliers des exemplaires : le neurone grand-mère*... C'est une limite de ce modèle, qui fini par conclure que nous aurions des représentations fortes et que le but du système visuel est d'y accéder. Or il est peu probable que chaque concept soit codé de manière invariante:
- S’il existe un neurone “grand mère/Jennifer Aniston” et sachant qu’on estime le nombre neurone chez l’humain à ~86 millions, quelle est la probabilité de tomber dessus? 
- Si par malheur ce neurone dysfonctionne? On oublierai le concept..?
- Degré d’invariance de la réponse du neurone? On ne peut pas s’assurer que le neurone n’aurait pas répondu à d’autres stimuli un peu différents étant donné le nombre limité de stimuli testés.

- **Hypothèse actuelle : Sparse Coding (Codage clairsemé)**. Un concept est représenté par l'activation simultanée d'un _petit groupe_ de neurones. Un même neurone peut participer à plusieurs "assemblées". Cela réduit le coût énergétique.
    

### 2. L'importance du Feedback

Le cerveau n'est pas qu'une machine ascendante (Feedforward).
- Il y a **2x plus de connexions descendantes** (Feedback) que montantes.
- De nombreuses connexions 'sautent' des niveaux.
- Rôles du feedback : Modulation de l'attention, prédiction sensorielle (Predictive Coding), imagerie mentale.
    

## B. Les Hallucinations Géométriques

Pourquoi les hallucinations (migraines, psychédéliques) ont-elles souvent des formes de spirales, tunnels ou toiles d'araignées ?
1. **Organisation de V1** : Les neurones sont organisés en hypercolonnes détectant des orientations.
2. **Activité spontanée** : Une activation anormale se propage entre neurones voisins (qui codent souvent des orientations similaires).s
3. Déformation Rétino-Corticale : La transformation mathématique de la rétine vers le cortex (log-polaire) fait qu'une ligne droite ou une onde plane sur le cortex correspond physiquement à une spirale ou un cercle dans le champ visuel.
    ![[champ_visuel_forme_retine.png]]
    ![[hallucination_forme_retine_cortex.png]]


