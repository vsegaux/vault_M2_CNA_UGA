---
prof: ALLEYSSON David
date:
publish: true
---

> [!NOTE] Examen 8 points, les 12 autres viennent de la partie d'Alan Chauvin
> 
> Compréhension générale du cours, parfois une question difficile.

# Introduction - Psychophysique

Notre perception visuelle ne correspond pas à une mesure physique brute. Il peut y avoir plusieurs perceptions identiques pour des situations physiques différentes, ou inversement, une même composition spectrale peut être perçue différemment selon le contexte (ex : un même tissu sous différents éclairages apparaît différent, c'est la constance des couleurs). Cela illustre que notre système visuel n'est pas un simple capteur passif : des traitements neuronaux complexes (gain, adaptation) transforment le signal physique en perception.

### Loi de Weber-Fechner

![[fechner_stimuli.png]]

Cette loi fondamentale de la psychophysique relie l'intensité du stimulus physique à la sensation perçue.

- **Le constat (Weber) :** Le seuil de discrimination (la plus petite différence perceptible, ou _JND - Just Noticeable Difference_) est proportionnel à l'intensité du stimulus ($\Delta I / I = k$).
- **La loi (Fechner) :** En intégrant la relation de Weber, on déduit que la sensation varie comme le logarithme de l'intensité du stimulus4.

$$S = k \cdot \log(I) + a$$

Où $S$ est la sensation, $I$ l'intensité physique, et $k, a$ des constantes.


# L'espace des couleurs comme espace géométrique

L'œil humain a une discrimination fine : il est capable de distinguer des différences de longueur d'onde de l'ordre de 3-4 nm.

### Efficacité lumineuse spectrale V($\lambda$)

Expérience de 1924 :
- On présente deux lumières monochromatiques à différentes longueurs d'onde.
- Le sujet doit ajuster l'intensité de l'une pour égaliser la luminosité perçue avec l'autre.
- Résultat : On trace la courbe de sensibilité spectrale de l'œil.
    
    ![[intensite_relative_percu.png]]
    
- **Interprétation :** Pour une même quantité d'énergie physique (radiance), une lumière verte (autour de 550 nm) est perçue beaucoup plus intensément qu'une lumière bleue ou rouge.
    

### Expérience de "Color Matching"

Cette expérience fonde la colorimétrie moderne (Trichromie).
1. On présente une lumière test $(W)$ d'une couleur donnée.
2. On demande au sujet de reproduire cette sensation colorée en mélangeant trois lumières primaires ($R, G, B$) d'intensités réglables.
3. On obtient les fonctions colorimétriques (Color Matching Functions) qui définissent les quantités de R, G, B nécessaires pour chaque longueur d'onde.
    ![[RGB_into_W.png]]
Le problème des valeurs négatives :

Sur le graphe ci-dessus, on observe des contributions négatives pour certaines longueurs d'onde. Physiquement, on ne peut pas ajouter de la "lumière négative".
- _Explication :_ Pour égaliser certaines couleurs très saturées (comme un cyan pur), le mélange $R+G+B$ ne suffit pas car il est toujours moins saturé que la couleur pure. On doit alors ajouter de la lumière (par exemple du Rouge) _du côté de la lumière test_ pour la désaturer. L'équation devient $W + R = G + B$, ce qui mathématiquement équivaut à $W = G + B - R$.
    

**Passage à l'espace XYZ :**
Pour standardiser l'industrie et éviter les valeurs négatives, on applique une transformation linéaire (changement de repère) vers un espace théorique : l'espace XYZ.
- Les composantes X, Y, Z sont toujours positives.
- Y correspond exactement à la courbe de luminance $V(\lambda)$ vue plus haut.
    ![[XYZ_color.png]]
    


# Mosaïque des cônes et échantillonnage
**Articles de référence**:
- Roorda & Williams, 1999 
- Hofer & al. 2005
La rétine n'est pas un capteur uniforme. La répartition des cônes (L, M, S) diffère selon les individus, formant une mosaïque unique. On peut imager cette mosaïque in-vivo avec une optique adaptative (précision de 0.5 min d'arc(1min d'arc = 1/60 de degré)).
### Luminance et Chrominance : Le problème du Démosaïçage

Dans un capteur numérique (comme dans l'œil), chaque "pixel" (ou cône) ne capte qu'une seule couleur (Rouge, Vert ou Bleu) à travers un filtre (mosaïque de Bayer pour les caméras).

![[Bayer_filter.png]]

L'image brute est donc une mosaïque entrelacée. Pour obtenir une image couleur complète, il faut séparer l'information de Luminance (intensité achromatique, détails fins) et de Chrominance (information couleur).

![[luminance-chrominance.png]]

**Analyse fréquentielle (Transformée de Fourier)** :
C'est ici que le traitement du signal intervient pour comprendre comment l'œil ou une caméra reconstruit l'image.
Si l'on regarde la Transformée de Fourier (FFT) d'une image issue d'une matrice de Bayer :

![[fourier_chromi.png]]
- **Luminance ($R+2G+B$) :** L'information de luminance est concentrée au centre du spectre (basses fréquences spatiales).
- **Chrominance :** À cause de la périodicité de la grille de Bayer (alternance des pixels), l'information de couleur est modulée et repoussée vers les hautes fréquences.
    

**Conséquence pour l'extraction** :
Avec ce type de mosaïque (Bayer), la luminance et la chrominance sont bien séparées dans le domaine fréquentiel. On peut donc récupérer la luminance par un simple filtrage passe-bas (on garde le centre) et la chrominance par un passe-haut (on garde les bords).

![[filtrage_lumi.png]]

> [!NOTE] Note sur les autres mosaïques
> 
> Avec d'autres arrangements de filtres (ex: aléatoire ou hexagona), le spectre aurait une forme différente, rendant la séparation luminance/chrominance potentiellement plus complexe (chevauchement des fréquences).
> 
> ![[spectr_non_bayer.png]]

# Analogie avec l'anatomie du système visuel

Le traitement du signal décrit ci-dessus (séparation luminance/chrominance par filtrage spatial) trouve un écho direct dans l'anatomie de la rétine. Les informations des cônes sont traitées par différentes voies ganglionnaires.

1. **Voie Parvocellulaire (Cellules naines / Midget) :**
    - Petits champs récepteurs.
    - Sensibles aux hautes fréquences spatiales (détails) et aux oppositions de couleurs (Rouge/Vert).
    - _Analogie :_ Elles transmettent l'information de **Chrominance** (et les détails fins).
2. **Voie Magnocellulaire (Cellules parasols) :**
    - Grands champs récepteurs.
    - Très sensibles au contraste de luminance et au mouvement, mais aveugles à la couleur.
    - _Analogie :_ Elles transmettent l'information de **Luminance** (basses fréquences spatiales, haute résolution temporelle).

L'organisation spatiale des champs récepteurs (centre ON / périphérie OFF) réalise physiquement une opération de convolution (filtrage spatial) similaire à ce qu'on fait en traitement d'image.

# Développement du système visuel

Les bébés ont une très mauvaise résolution spatiale à la naissance, mais une vision des couleurs qui devient correcte vers 4 mois.

Problème théorique : Les cônes sont répartis de manière quasi-aléatoire ("random mosaic"). Comment le cerveau sait-il que tel cône est rouge et son voisin vert pour reconstruire une image cohérente ?

**Hypothèse :** Le cerveau doit **apprendre** la structure de sa propre mosaïque rétinienne. Il n'y a pas de plan préétabli "câblé". Le système visuel utilise les statistiques des scènes naturelles (bords continus, corrélations spatiales) pour déduire la position et le type de chaque cône.

Simulation (Démosaïçage incongruent) :

Si on essaie de décoder une image avec une mosaïque incorrecte (le logiciel pense que le pixel est rouge alors qu'il est vert), on obtient l'image de droite ci-dessous :

![[decoding_mosaique.png]]

- Les contours (luminance) sont à peu près préservés.
- Les couleurs sont totalement fausses ou absentes.
    Cela suggère que la bonne vision des couleurs dépend de la capacité du cerveau à décoder correctement la mosaïque spatiale des cônes.

# Discrimination des couleurs et Géométrie

La capacité à différencier deux couleurs n'est pas uniforme dans tout l'espace des couleurs.

### Ellipses de MacAdam (1942)

MacAdam a mesuré les seuils de discrimination (JND) autour de différentes couleurs cibles.
- Si l'espace des couleurs était euclidien (repère orthonormé), les seuils de tolérance seraient des cercles de même rayon partout.
- Observation : Ce sont des ellipses de tailles et d'orientations variables.
    ![[ellipse_var_discri.png]]
    Cela prouve que l'espace perceptif des couleurs est Riemannien (courbe), et non Euclidien. La métrique (la notion de distance) change localement.

# Projection de l'espace des couleurs (Modèle Projectif)

Pour unifier ces observations (lois de Weber, réponse non-linéaire des neurones, géométrie hyperbolique), on peut utiliser la **géométrie projective**.

### Analogie avec la perspective

![[projection_couleur_plan_sphere_hyperboloide.png]]
Chaque point de l'image correspond à une couleur qui peut être décrite selon ses coordonnées X,Y,Z (vues précédemment). On peut alors projeter ces coordonnées sur des plans (x+y=z=1), des sphère (x²+y²+z²) ou encore hyperboloïque (-x²-y²+z²).
Expérimentalement, le modèle de la vision des couleurs par l'Humain se projette plutôt sur des hyperboloïdes (voir la partie suivante).

### Le lien Physiologie - Géométrie Projective
**Articles de référence**:
- Yilmaz, 1962

Le modèle projectif permet de lier mathématiquement les réponses neuronales aux dimensions perceptives. Les axes de l'espace projectif s'alignent avec les voies physiologiques:

![[magno_parvo_konio_projection.png]]
Pour comprendre ce schéma, il faut visualiser l'espace des couleurs non pas comme un cube (RGB), mais comme un **cône** dans un espace 3D.

Dans l'article de Yilmaz, l'auteur propose que la perception des couleurs fonctionne mathématiquement comme la Relativité Restreinte d'Einstein :
- En relativité, il y a une limite infranchissable (la vitesse de la lumière $c$).
- En vision, il y a une limite infranchissable (la saturation maximale d'une couleur pure).
    
Le modèle projectif consiste à dire que notre cerveau sépare l'information en deux types de données géométriques distinctes : **l'intensité** et **la chromaticité**.

1. Axe Temporel / Échelle (Rayon) $\leftrightarrow$ Voie Magno (Luminance) :
    - **Concept mathématique :** Dans la géométrie de Yilmaz, c'est l'équivalent de l'axe du **Temps** ($t$) ou de l'amplitude du vecteur. C'est la distance par rapport à l'origine $(0,0,0)$ dans le cône.
	- **Signification :** En s'éloignant de l'origine le long de cet axe, on ne change pas de couleur (ce n'est pas plus rouge ou plus vert), on change juste la **Luminosité**.
	- **Lien Physiologique (Magno) :** La voie Magnocellulaire (cellules parasols) est "aveugle" à la couleur mais très sensible au contraste de luminance et au mouvement. Elle code l'énergie globale du signal. C'est elle qui définit l'échelle d'intensité de la perception.
2. Plan Chromatique $\leftrightarrow$ Voie Parvo (Rouge/Vert) :
	- **Concept mathématique :** C'est la **surface de projection**. Imaginons que l'on coupe le cône de lumière par une surface courbe (une hyperboloïde). Les coordonnées sur cette surface ($x, y$) définissent la teinte et la saturation.
	- **Signification :** C'est l'information "couleur" pure, débarrassée de l'intensité.
	- **Lien Physiologique (Parvo) :** La voie Parvocellulaire (cellules naines) gère l'opposition Rouge/Vert et les détails fins. Dans le modèle projectif, c'est elle qui donne les coordonnées précises sur la "carte" des couleurs (l'hyperboloïde). C'est la voie principale pour distinguer les objets par leur couleur.
3. Origine / Axe vertical $\leftrightarrow$ Voie Konio (Bleu/Jaune) :
    - **Concept mathématique :** Dans l'espace des couleurs, pour définir un plan de projection (le plan où les couleurs existent), il faut définir l'orientation de l'axe "Blanc" (l'axe achromatique), ou le 'plan pourpre'.
	- **Lien Physiologique (Konio) :** La voie Koniocellulaire gère l'information des cônes S (Bleu) opposée au Jaune (L+M).
	- **Explication du "Plan pourpre" :** Cette voie servirait à "caler" ou "aligner" le système. Contrairement à la voie Parvo qui donne la richesse des détails chromatiques, la voie Konio (plus primitive et moins résolue) définirait l'axe vertical ou l'origine de la projection. Elle permet de définir où se trouve le "Blanc" par rapport au "Bleu". Sans cette référence, le système ne saurait pas comment orienter l'hyperboloïde.
    
### Pourquoi une hyperboloïde ?
Le modèle de Naka-Rushton (qui décrit la réponse saturante d'un neurone : $R = \frac{I}{I + \sigma}$) est mathématiquement équivalent à une projection sur une métrique hyperbolique (Disque de Poincaré). OK...?