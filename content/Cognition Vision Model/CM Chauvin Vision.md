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

# Introduction et Plan du cours

L'objectif est de comprendre comment le système visuel transforme un signal physique en une perception sémantique.

1. **Qu'est-ce que voir ? (L'environnement visuel)**
    
    - Définition de l'image numérique (pixel).
        
    - Introduction à l'espace de Fourier : pourquoi est-ce un outil pertinent ?
        
    - _Nuance importante_ : Le système visuel n'effectue pas une Transformée de Fourier (TF) globale sur toute l'image. Il fonctionne de manière **locale**. Cependant, le filtrage local effectué par le cerveau extrait les mêmes caractéristiques (features) que l'analyse de Fourier. C'est donc un excellent modèle d'approximation.
        
2. **Du signal à la rétine (Traitement précoce)**
    
    - Projection optique.
        
    - Transduction par les photorécepteurs (dynamique, adaptation).
        
    - Traitement rétinien : couches plexiformes, cellules bipolaires et ganglionnaires (filtrage, compression).
        
3. **De la rétine au Cortex (Traitement central)**
    
    - Transmission via le Corps Genouillé Latéral (CGL) vers V1.
        
    - Architecture de V1 : hypercolonnes, sélectivité (orientation, fréquence).
        
    - Modélisation par filtres de Gabor.
        
    - Aires extrastriées (V2, V3, etc.) : construction de la complexité.
        

---

# 1. Définir l'environnement visuel

## Le "Gist" d'une scène

Le système visuel est capable d'extraire le **"gist"** (l'essentiel) d'une scène visuelle en quelques millisecondes (reconnaissance _rapide_ et _automatique_). Ce gist comprend :

- **La catégorie sémantique** (ex: scène de plage, ville, forêt).
    
- **La structure spatiale globale** (ex: ouvert vs fermé, naturel vs artificiel).
    
- **Les surfaces dominantes** (sable, eau, bitume).
    
- **Les objets principaux** (barque, voiture).
    
- **Les affordances émotionnelles** (sensation de chaleur, danger, bien-être).
    

## Approches de la vision

### Approche descendante (Top-down)

Elle part de nos connaissances préalables pour décrire une scène (ex : "Je sais qu'une classe contient des chaises, donc je cherche des chaises").

- _Limite_ : Cette approche est contrainte par la nécessité de posséder des schémas préexistants.
    

### Approche ascendante (Bottom-up)

C'est l'approche privilégiée dans ce cours. On décrit la scène en s'appuyant uniquement sur les informations extraites par le système visuel, étape par étape, du signal brut vers la sémantique.

#### Vision structurale (Modèle de Marr, 1982)

David Marr propose une vision séquentielle par étapes de complexité croissante :

1. **Primal Sketch (Esquisse primaire - 2D)** : Extraction des primitives de base (lignes, jonctions, contours, contrastes, mouvement).
    
2. **2.5D Sketch** : Reconstruction des surfaces centrée sur l'observateur (texture, ombres, disparité binoculaire, profondeur locale). _Note : Ce n'est pas encore de la 3D complète car on ne voit pas "derrière" les objets._
    
3. **Modèle 3D** : Représentation centrée sur l'objet (indépendante du point de vue). Utilisation des axes de symétrie et d'élongation pour structurer les volumes.
    
4. **Catégorisation (Palmer)** : Identification de l'objet, de sa fonction et de ses affordances (ce que l'objet permet de faire).
    

---

# 2. Modélisation de l'image numérique

Pour étudier la vision, on utilise l'image numérique comme modèle de l'image rétinienne (échantillonnage discret).

## Le Pixel : brique élémentaire

Un pixel ("Picture Element") à une position $(x, y)$ est défini par **5 dimensions** d'information :

1. **Luminance (2D)** : Intensité lumineuse spatiale.
    
2. **Couleur (+1D)** : Codée sur 3 canaux (Rouge, Vert, Bleu).
    
3. **Temps (+1D)** : Pour les vidéos, variation temporelle (frames).
    
4. **Profondeur/3D (+1D)** :
    
    - _Indices binoculaires_ : Disparité rétinienne (décalage image œil gauche/droit).
        
    - _Indices monoculaires_ : Ombres, occlusions, perspective linéaire, gradients de texture, taille relative.
        

**Propriétés de l'image :**

- **Résolution** : Taille de la matrice (nombre de pixels).
    
- **Quantification** : Encodage de l'intensité (ex: 8 bits = 256 niveaux de gris).
    

## Mesurer la similitude entre deux images

Comment comparer mathématiquement deux scènes ?

### 1. La Moyenne (Averaging)

Peu efficace. La moyenne de toutes les images de "plages" donne une bouillie grise qui ne permet pas de discriminer finement les catégories.

### 2. Le MSE (Mean Squared Error)

On calcule la différence d'intensité pixel par pixel entre deux images.

- Peut être généralisé par la norme $L_p$.
    
- **Avantage** : Efficace pour détecter du bruit (neige) sur une image identique.
    
- **Inconvénient majeur** : Le MSE est très sensible aux transformations spatiales. Si on prend une image et qu'on la décale de quelques pixels ou qu'on effectue une rotation, l'image reste _perceptivement_ identique pour un humain, mais le MSE explose. Le pixel n'est donc pas la bonne unité de mesure pour la sémantique.
    

### 3. L'espace de Fourier

La Transformée de Fourier (TF) offre une représentation plus robuste aux translations.

#### Principe théorique

Tout signal complexe peut être décomposé en une somme de signaux sinusoïdaux simples.

Une sinusoïde est définie par : $x(t) = A \cdot \sin(\frac{2\pi}{T}t + \phi)$

- $A$ : Amplitude (contraste maximal).
    
- $T$ : Période (inverse de la fréquence $f$).
    
- $\phi$ : Phase (décalage temporel ou spatial).
    

La Transformée de Fourier convertit le signal du domaine spatial vers le domaine fréquentiel :

$$X(f)= \int_{-\infty}^{\infty} x(t)\exp(-j2\pi ft) dt$$

#### Application à l'image (2D)

Pour une image, on décompose les variations de luminance. On obtient deux spectres :

1. **Le Spectre d'Amplitude (SA)** :
    
    - Indique "combien" il y a de chaque fréquence.
        
    - Représentation visuelle :
        
        - Le centre = Basses Fréquences (BF) = structure globale, formes grossières.
            
        - La périphérie = Hautes Fréquences (HF) = détails fins, contours précis.
            
        - L'orientation des points indique l'orientation des motifs dans l'image (ex: une scène de ville avec des immeubles verticaux aura de l'énergie sur l'axe horizontal du spectre).
            
    - **Propriété fondamentale** : Les scènes naturelles suivent une loi en $1/f$ (beaucoup d'énergie en BF, peu en HF).
        
2. **Le Spectre de Phase (SP)** :
    
    - Indique "où" sont les sinusoïdes (leur position). Contient l'information sur la structure des bords.
	    
    - Souvent moins lisible 'naturellement'.
        

![[Fourier_basique.png]] ![[fourier_image.png]] ![[fourier_representation2D.png]]

> Expérience clé (Images Hybrides) :
> 
> Si on mélange le Spectre d'Amplitude d'une scène A avec le Spectre de Phase d'une scène B, l'image résultante ressemble structurellement à B, mais on perçoit la texture de A.
> 
> Cependant, pour la catégorisation rapide (plage vs ville), le cerveau semble s'appuyer prioritairement sur les régularités du Spectre d'Amplitude (ex: horizon dégagé vs lignes verticales).

Finalement, le spectre d'amplitude semble être un bon indicateur de la catégorie des scènes:
![[img_2_fourier_examples.png]]

#### Lien avec le système visuel (Filtrage local)

Le cerveau ne fait pas une TF mathématique globale. Il utilise des **filtres locaux** (les champs récepteurs des neurones) qui pavent le champ visuel.

- Opération mathématique : **Convolution**.
    
- **Théorème de convolution** : Une convolution dans l'espace spatial équivaut à une multiplication dans l'espace fréquentiel (Fourier).
    
- En balayant l'image avec des filtres spécifiques (ex: Gabor), le cerveau analyse localement les fréquences et orientations, simulant ainsi une analyse de Fourier locale.
    

![[TF8locale.png]] ![[visuel_lien_fourier_humain.png]]

---

# 3. Le traitement de l'information visuelle (Rétine)

L'information lumineuse traverse l'œil pour atteindre la rétine, où elle subit plusieurs étapes de traitement et de compression avant d'être envoyée au cerveau.

## A. Les Photorécepteurs (Transduction)

Ils convertissent la lumière en signal électrique.

- **Modèle 1 : Dynamique de réponse (Adaptation à la luminance)**
    
    - La réponse des photorécepteurs n'est pas linéaire. Elle suit une courbe quasi-logarithmique (équation de Naka-Rushton) qui sature aux extrêmes.
        
    - Le système s'adapte au niveau de lumière ambiante ($L_0$) pour maximiser la sensibilité aux contrastes autour de cette valeur moyenne. C'est ce qui nous permet de voir aussi bien en plein soleil que dans une pièce sombre (après adaptation).
        
        ![[dynamique_reponse_photorecept.png]]
        
- **Modèle 2 : Répartition et Échantillonnage (Rétinotopie)**
    
    - **Fovéa (Centre)** : Très forte densité de **Cônes**. Vision photopique (jour), couleur, haute résolution.
        
    - **Périphérie** : Forte densité de **Bâtonnets**, peu de cônes. Vision scotopique (nuit), détection de mouvement, faible résolution, pas de couleur.
        
    - Conséquence : La résolution spatiale n'est pas homogène. Elle est maximale au centre et chute drastiquement en périphérie.
        
        ![[Répartition_photorecepteur_retine.png]]
        
- **Phénomène de Convergence** :
    
    - En fovéa : 1 Cône $\to$ 1 Bipolaire $\to$ 1 Ganglionnaire (Acuité maximale, pas de perte).
        
    - En périphérie : ~1000 Bâtonnets $\to$ quelques Bipolaires $\to$ 1 Ganglionnaire. (Gain de sensibilité à la lumière par sommation, mais perte de précision spatiale).
        
        ![[convergence_photorecepteur.png]]
        

## B. Couche Plexiforme Externe (OPL) & Cellules Bipolaires

C'est la première étape de traitement du signal.

- **Modèle 4 : Modèle électrique**
    
    - Les cellules horizontales connectent les photorécepteurs entre eux latéralement via des _Gap junctions_.
        
    - Cela crée un réseau électrique qui lisse le signal (filtre passe-bas).
        
    - La cellule bipolaire soustrait ce signal moyen (venant des cellules horizontales) du signal direct du photorécepteur.
        
        ![[modele_4_elec_bg.png]] ![[resume_filtre_cellule_bipo.png]]
        
- Champs Récepteurs (CR) Centre-Périphérie :
    
    Ce mécanisme crée des champs récepteurs antagonistes.
    
    - **Centre ON / Périphérie OFF** : S'active si la lumière touche le centre, s'inhibe si elle touche la périphérie.
        
    - **Centre OFF / Périphérie ON** : Inverse.
        
    - **Fonction** : Détecter les **contrastes locaux** (bords) plutôt que la luminosité absolue.
        

## C. Cellules Ganglionnaires (Sortie de la rétine)

Elles récupèrent l'info des bipolaires et envoient les potentiels d'action vers le cerveau.

- **Modèle 3 : Différence de Gaussiennes (DoG)**
    
    - Le champ récepteur est modélisé mathématiquement par une différence de deux gaussiennes (une étroite positive pour le centre, une large négative pour la périphérie). C'est un filtre "Chapeau Mexicain".
        
        ![[model_ganglio_1.png]] ![[model_ganglion_2.png]]
        
- **Blanchiment Spectral (Spectral Whitening)** :
    
    - Dans les images naturelles, les Basses Fréquences (BF) ont une énergie énorme (loi $1/f^2$).
        
    - Le filtrage par les cellules ganglionnaires (passe-bande) atténue ces BF dominantes et rehausse les Hautes Fréquences (HF). Cela "égalise" (blanchit) le spectre pour rendre les détails (HF) perceptibles et compresser l'information redondante.
        

### Les 3 voies parallèles (Magno, Parvo, Konio)

Les cellules ganglionnaires sont spécialisées :

|**Type**|**Nom**|**Caractéristiques**|**Fonction (Extraction)**|
|---|---|---|---|
|**M**|**Magnocellulaire** ("Parasol")|Gros corps cellulaire, gros champ récepteur. Très rapide (phasique). Sensible au contraste de luminance, mais aveugle à la couleur. Principalement en périphérie.|Mouvement, scintillement, **Basses Fréquences (BF)**, contours grossiers.|
|**P**|**Parvocellulaire** ("Midget")|Petit corps cellulaire, petit champ récepteur. Plus lente (tonique). Sensible à la couleur (Rouge/Vert) et aux détails. Principalement en fovéa.|Couleur, forme fine, textures, **Hautes Fréquences (HF)**.|
|**K**|**Koniocellulaire**|Propriétés intermédiaires.|Couleur (Bleu/Jaune).|

> Principe "Coarse-to-Fine" (Du grossier au détail) :
> 
> Comme la voie Magno (BF) est plus rapide que la voie Parvo (HF), le cerveau reçoit d'abord une structure grossière de la scène (le "gist", les formes globales) avant de recevoir les détails fins et la couleur.
> 
> Preuve expérimentale : Images hybrides (BF d'une scène + HF d'une autre). En présentation très courte, on ne perçoit que la scène en BF.
 
 ![[spatio_temp_rep.png]]Sur la courbe ci-dessus, chaque couleur correspond à un type de cellule:
- Magno cellulaire Y (orange): Passe très bas puis passe haut (2 passe bandes)
- Magno cellulaire LF-X (rouge): Passe bas
- Parvo cellulaire HF-X (bleu): Passe haut
Finalement, les prédictions qui peuvent être faites:  ![[prediction_magno_parvo.png]]

### Smart Retina ?

La rétine ne fait pas que transmettre. Elle effectue des traitements complexes très tôt :

- Détection de mouvement local.
    
- Anticipation de la trajectoire (pour compenser les délais de transmission neuronaux).
    
- Ségrégation précoce du mouvement objet vs mouvement oculaire.
    
    ![[smart_retina_mvmnt.png]]
    

### Résumé des voies optiques

![[synthese_couche_photorecept.png]] ![[resume_ganglionaires.png]]

---

# 4. De la rétine au cortex visuel primaire

## Le trajet optique

1. **Nerf Optique** : Sortie de la rétine.
    
2. **Chiasma Optique** : Décussation partielle.
    
    - Les hémi-rétines **nasales** (vision périphérique) croisent vers l'hémisphère opposé.
        
    - Les hémi-rétines **temporales** restent du même côté.
        
    - Résultat : Le champ visuel droit est traité par l'hémisphère gauche (et vice-versa).
        
        ![[champ_visuel.png]]
        
3. **Corps Genouillé Latéral (CGL)** (Thalamus) : Reçoit 90% des fibres.
    
4. **Colliculus Supérieur** (Tronc cérébral) : Reçoit 10% des fibres. Gère les réflexes oculaires et l'orientation inconsciente (blindsight).
    

## Le Corps Genouillé Latéral (CGL)

Ce n'est pas un simple relais passif.

- **Organisation** : 6 couches alignées (rétinotopie conservée).
    
    - Couches 1-2 : Entrées **Magnocellulaires**.
        
    - Couches 3-6 : Entrées **Parvocellulaires**.
        
- **Rôle** : Porte d'entrée vers le cortex. Modulation attentionnelle.
    
- Feedback : 90% des connexions entrant dans le CGL viennent... du cortex (V1) ! Cela suggère un fort contrôle top-down (le cerveau module ce qu'il veut voir).
    
    ![[resume_retineècgl_magno_parvo.png]]
    

---

# 5. Le Cortex Visuel Primaire (V1)

Situé dans le lobe occipital, c'est le premier centre de traitement cortical.

## Propriétés fondamentales

1. **Rétinotopie** : La carte de la rétine est préservée sur la surface du cortex.
    
2. **Magnification corticale** : La fovéa (1% de la rétine) occupe environ 50% de la surface de V1. C'est une sur-représentation des informations centrales. ![[V1_repartition.png]]
    
3. **Organisation laminaire** : Les entrées du CGL arrivent dans la couche 4 (IVC), en gardant la séparation Magno($\alpha$)/Parvo($\beta$). ![[V1_laminaire_magno_parvo.png]]
    

## Cellules de V1 et Sélectivité

Hubel & Wiesel (Prix Nobel) ont découvert que les neurones de V1 ne répondent plus à des points (comme la rétine), mais à des **lignes orientées**.

- **Cellules Simples** (Couches 4 & 6) :
    
    - Champs récepteurs allongés avec zones ON/OFF distinctes.
        
    - Sensibles à l'**orientation** et à la **position exacte** (phase) de la barre lumineuse dans le champ récepteur.
        
    - Modèle : On peut créer une cellule simple en alignant plusieurs cellules ganglionnaires centre-surround.
        
        ![[champ_recept_bars.png]]
        
- **Cellules Complexes** (Couches 2, 3, 5) :
    
    - Sensibles à l'**orientation** mais **insensibles à la position exacte** (invariance de phase). Elles répondent tant que la barre orientée est quelque part dans le champ récepteur (souvent sensible aussi au mouvement de cette barre).
        
    - _Modèle_ : Sommation de plusieurs cellules simples.        

> Preuve par adaptation (Aftereffect) :
> 
> Fixer longtemps des lignes inclinées vers la gauche fatigue les neurones sélectifs à cette orientation. Si on regarde ensuite des lignes verticales, elles sembleront pencher vers la droite (les neurones "gauches" étant fatigués, les neurones "droits" dominent relativemet).
> 
> Cela prouve l'existence de populations de neurones dédiées (canaux) pour l'orientation et la fréquence spatiale.
> 
> ![[adaptation_orientation.png]] ![[adaptation_freq_spatiale.png]]

## Organisation fonctionnelle : L'Hypercolonne

V1 est organisé en modules répétitifs appelés **Hypercolonnes**. Une hypercolonne traite **une petite portion de l'espace visuel** et contient toute la machinerie nécessaire pour l'analyser complètement :

1. **Colonnes d'orientation** : Ensemble de neurones couvrant toutes les orientations possibles (360°), disposés en "pinwheels".
    
2. **Colonnes de dominance oculaire** : Neurones préférant l'œil gauche ou l'œil droit.
    
3. **Blobs (tâches)** : Zones riches en cytochrome oxydase, traitant la **couleur**.
    
4. **Sélectivité à la fréquence spatiale** : Neurones répondant à différentes finesses de détails.
    

Ainsi, l'organisation spatiale garantit la permanence de l'objet : si un objet tourne ou bouge légèrement, l'activité se déplace simplement vers la colonne voisine au sein du même module ou vers le module adjacent.

![[couche_colonne_V1.png]] ![[hypercolone_simplifie.png]]

## Modélisation mathématique de V1 : Le filtre de Gabor (Modèle 5)

La fonction de Gabor est le meilleur modèle mathématique pour décrire le champ récepteur d'une cellule simple de V1.

C'est le produit d'une Sinusoïde (sélectionne la fréquence et l'orientation) et d'une Gaussienne (localise le filtre dans l'espace).

Formule simplifiée : $G(x,y) = \text{Gaussienne}(x,y) \times \text{Sinusoïde}(x,y)$

- **Cellules simples** : Modélisées par la partie Réelle (symétrique/paire) ou Imaginaire (antisymétrique/impaire) du filtre. ![[gabor_reel_imag.png]]
    
- **Cellules complexes** : Modélisées par l'énergie du filtre (Module = $\sqrt{Réel^2 + Imaginaire^2}$). Cela explique leur insensibilité à la phase (position précise). ![[gabor_representation.png]]
    

En vision artificielle, on utilise un banc de filtres de Gabor (plusieurs tailles et orientations) pour simuler le traitement effectué par une hypercolonne.

![[gabor_banc_filtre.png]]

Un autre moyen d'arriver à cette forme pour les cellules simples est de procéder par analyse d'images en composantes indépendantes. Les travaux de Hosoya & Hyvärinen ont utilisé cette méthode (cet algorithme) pour extraire les composantes indépendantes d'images. La décomposition ainsi obtenue donne les différentes sources élémentaires qui composent une image, et ces sources ressemblent beaucoup aux filtre élémentaires tels que présentés ci-dessus. Ces filtres/cette décomposition permettraient donc bien d'extraire les composantes élémentaires des images:
![[decompo_indepdnante_image_.png]] 
*Les propriétés et l’organisation spatiale des champs récepteurs émergent des régularités statistiques des scènes naturelles en cherchant à maximiser l’information transmises.*

---

# 6. Au-delà de V1 : Cortex Extrastrié

L'information est redistribuée vers des aires spécialisées (organisation hiérarchique mais avec beaucoup de connexions parallèles et retours).

- **V2** : Traitement des contours illusoires (remplissage des surfaces), début de la mise en relation des formes.
    
- **V4** : Traitement de la couleur et des formes complexes (qui ne sont pas forcément "captées" par les zones précédentes).
    
- **V5 / MT (Middle Temporal)** : Traitement du mouvement global.
    

On distingue deux grandes voies corticales :

1. **Voie Dorsale ("Where" / "How")** : Vers le lobe pariétal. Extension de la voie Magno. Traite le mouvement, la position spatiale, guide l'action.
    
2. **Voie Ventrale ("What")** : Vers le lobe temporal (IT - Inféro-Temporal). Extension de la voie Parvo. Traite la reconnaissance d'objets, les visages, les couleurs.

![[audela_V1_extrastrie.png]]

A partir des caractéristiques élémentaires, on reconstruit des contours et remplis la forme via les propriétés de surface. Fonctionnellement, cela nous permet de compléter le contours d'objets masqués/de ségréguer des objets.

![[audela_V1_detail.png]]

# 7. Extraction du mouvement
 Il existe dans **V1** des *cellules simples* sélectives à la direction du mouvement. La réponse de ces cellules est séparable en une composante spatiale et une composante temporelle: RF(X,T) = G(X)H(T)
 ![[spatial_temporal_resp.png]]
 On reconnait la forme de filtre de Gabor, et celle-ci évolue au fil du temps, tel que montré dans les travaux de DeAngelis, Ohzawa, Freeman (1993)

Dans **V3**, les activités de V1 sont combinées pour extraire des informations de mouvements et rendre possible l'extraction de bords à partir de mouvement (typiquement dans du bruit, où l'extraction serait impossible sans mouvement) (Zeki, 1993). Ici encore, les informations des premières aires visuelles sont combinées dans les aires supérieures.

**Akinétopsie**: Agnosie visuelle du mouvement. -> La vie est comme un filme stroboscopique.
**Mouvement apparent**:
- Une variation de position discrète au cours du temps. (typiquement effet stroboscopique)
- Par opposition au mouvement constant qui est continue.


# 8. Aire Inféro-Temporale (IT)
Neurones qui répondent sélectivement à certaines catégories d’objets, invariance de la réponse à la taille, la position, l’angle de vue, aux caractéristiques de surface…
- Les réponses évoquent un continuum dans la représentation de l’espace des objets. Cette **organisation** (des neurones) permet d’avoir un continuum de réponse lors de transformations type rotation, translation dans l’espace 3D des objets:![[invariance_rotation_objet_IT.png]]

## Limite du modèle hierarchique

### Représentation fortes
*Logiquement la finalité d’un modèle hiérarchique est la reconstruction des objets et en particuliers des exemplaires : le neurone grand-mère*... C'est une limite de ce modèle, qui fini par conclure que nous aurions des représentations fortes et que le but du système visuel est d'y accéder. Or il est peu probable que chaque concept soit codé de manière invariante:
- S’il existe un neurone “grand mère/Jennifer Aniston” et sachant qu’on estime le nombre neurone chez l’humain à ~86 millions, quelle est la probabilité de tomber dessus? 
- Si par malheur ce neurone dysfonctionne? On oublierai le concept..?
- Degré d’invariance de la réponse du neurone? On ne peut pas s’assurer que le neurone n’aurait pas répondu à d’autres stimuli un peu différents étant donné le nombre limité de stimuli testés

Au contraire, l'hypothèse courante est plutôt celle du "sparse-coding":  représentation d’un concept par l’activation conjointe d’un ensemble de neurones relativement petit => neurone enregistré est commun aux réseaux actives par les différentes représentations de Jennifer Aniston.
-  Avantage: réduit les couts de traitements

### Ascendance
*Le traitement de l’information visuelle ne se fait pas uniquement de manière « ascendante »*. En réalité:
- Deux fois plus de connexions feedbacks que de connexions ascendantes + connexions horizontales 
- Nombreuses connexions qui « sautent » des niveaux 
- La réponse des aires visuelles n’est pas toujours expliquée par les propriétés des stimuli

Les connections feedback jouent différents rôles:
- attentional modulation, 
- the comparison of internally generated predictions of sensory input with actual inputs; 
- imagining sensory-like representations from concepts of e.g. visual objects


### Limite générale de l'approche
Attention : nous sommes encore sur des modèles de traitement de l’information, avec des espaces, des métriques, des algorithmes d’optimisation informés.


# 9. Hallucinations
Pour expliquer les hallucinations, il est nécessaire d'avoir une activité spontanée ou non corrélée avec les informations rétiniennes. Les hallucinations sont souvent concentriques, rappelant l'organisation du cortex visuel et la déformation du champ visuel qui existe entre la rétine et le cortex:
![[champ_visuel_forme_retine.png]]
![[hallucination_forme_retine_cortex.png]]
De plus, l'activité spontanée d'une cellule dans le cortex visuel va provoquer l'activité de cellules voisines (dans l'hypoercolonne) qui codent généralement pour des formes/orientation similaires et va donc provoquer l'hallucination de contour illusoires. Finalement, les hallucinations sont dues à:
- *Activité spontanée* : Nous avons vu qu’une activité spontanée ou auto-initée du cortex visuel est possible dans les tâches d’imagerie. 
- *Déformation du champ visuel* : Les formes des hallucinations rappelle l’organisation du cortex visuel et la déformation qui existe entre la rétine et le cortex. 
- *Connections pour des neurones « alignés »* : On rajoute en plus les connections entre es neurones distants