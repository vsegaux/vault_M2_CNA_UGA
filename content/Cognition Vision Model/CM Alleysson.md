---
prof: ALLEYSSON David
date:
publish: true
---


> [!NOTE] Examen 8 points, les 12 autres viennent de la partie d'Alan Chauvin
> Compréhension générale du cours, parfois une question difficile.

# Introducion - Psychophysics

Il peut y avoir plusieurs perceptions identiques d'un objet, liées à plusieurs modes physique pour y arriver. Par exemple, un même objet sous différentes ambiances lumineuses. Cela illustre que notre système perceptif n'est pas simplement perceptif, mais des traitements sont réalisé et les perceptions effectives varient selon le contexte.

Moi de Weber-Fechner:
![[fechner_stimuli.png]]
Les seuils de sensation différentes pour des stimulis augmente de manière logarithmique avec l'intensité de la sensation. Sensation = k * log(Intensité) + a


## Color space as geometry space

L'oeil n'est pas capable de distinguer de différence de couleur en dessous de 3-4nm de différence de longueur d'onde.
Expérience en 1924:
- Presentation de deux lumières à différentes longueurs d'onde, on demande au sujet de régler l'intensité de l'une des lumières pour que les deux aient la meme intensité perçue.
- On arrive finalement à tracer la courbe de l'intensité relative perçue des lumières monochromatiques du spectre: ![[intensite_relative_percu.png]]
- Pour une même quantité d'énergie, une lumière de longueur d'onde proche du vert est perçue comme plus intense que les autres longueurs d'ondes.

Color matching experiment:
- On présente une lumière (W) d'une couleur donnée
- Puis, on présente une lumière composée de 3 composantes primares R, G, B qui reproduit la couleur de la lumière W. On obtient alors des ratios de RGB pour obtenir les différentes couleurs (longueur d'onde) possibles W. ![[RGB_into_W.png]]
- On remarque des contributions négatives parfois, elles sont obtenu en égalisant W+ R/G/B avec les deux autre restante (GB/RB/RG).
- Il existe une transformation dans laquelle les trois couleurs primaires ont des composantes qui restent positives, on passe alors de RGB à XYZ, qui dépendent de la longueur d'onde de la couleur cible: ![[XYZ_color.png]]
- Ces primaires XYZ sont la base de l'industrie des couleurs, tous les systèmes (numériques en particulier) sont basés dessus.

## Mosaique des cones
Chaque oeil est différent, la position des cones et des batonnets est différentes selon les individus. On est capable d'obtenir des images de fond de l'oeil avec des précisions à 5min d'arc (1min d'arc = 1/60 de degré).

Luminance et chrominance:
![[luminance-chrominance.png]]

Par défaut, il est difficile d'extraire la luminance d'une image car l'image du capteur est obtenu par filtrage (Bayer), chaque pixel est donc modulé selon sa couleur) (A expliquer mieux..). Une possibilité est de passer par la transfromée de fourier de l'image:
![[fourier_chromi.png]]
Sur la transformée de Fourier, on trouve la luminance au centre (R+2G+B) et la chrominence sur les bords. On retrouve cette forme de transformée à cause de la répartition des pixels respectivement R,G,B, sur le filtre **Bayer** (donc sur la manière d'obtenir l'image de base):
![[Bayer_filter.png]]


Avec d'autres type de filtrage, on aurait d'autre formesde spectre:
![[spectr_non_bayer.png]]


On peut récupérer la luminance seule par filtrage:
![[filtrage_lumi.png]]

A noter que selon le filtrage, la limitation entre luminance et chrominance n'est pas forcément si évidente à extraire. 
En particulier avec le filtrage Bayer, il y a des zones où leurs limites sont proche donc des informations de luminances peuvent se retrouver dans la chrominance et inversement.
Or un filtrage en domaine spectrale est une convolution dans le domaine de base, ce qui permet d'obtenir l'image de luminance par convolution de l'image originale.

## Analogie avec l'anatomie du système visuel
Voies parvo- et magnoecellulaire. A expliquer mieux..! Rôle de filtrage des cellules parasoles, des cellules naines etc...

## Développement du système visuel

Mauvaise résolution pour la vision des bébé; bonne vision des couleurs correcte à partir de 4 mois. Une hypothèse est qu'ils ne sont pas capable de décoder la mosaïque extraite des récepteurs (leur cerveau n'est pas encore capable de décoder les informations issues des batonnets et cônes, répartis "aléatoiremNent" en R,G,B). On suppose que les neurones apprennent à retrouver la cohérence spatiale dans les images à partir d'une mosaïque spécifique: le réseau de neurone évolue pour interpréter les entrées perceptives de la bonne manière.
Une manière de simuler cette hypothèse est de décoder une image avec une mosaïque incongruente, on obtient une image dans laquelle les contours sont bien définis mais les couleurs ne sont pas rendues:
![[decoding_mosaique.png]]

### Discrimination des couleurs
Grande variabilité selon les individus, une étude de 1942 a tenter de montrer pour différents "points" dans l'espace des couleurs, les variations nécessaires à la discrimination d'une différence. On obtient des ellipses comme indiqué sur la figure suivante:
![[ellipse_var_discri.png]]

## Projection de l'espace des couleurs
![[projection_couleur_plan_sphere_hyperboloide.png]]
Chaque point de l'image correspond à une couleur qui peut etre décrite selon ses coordonées X,Y,Z (vues précedement). On peut alors projeter ces coordonées sur des plans (x+y=z=1), des sphère (x²+y²+z²) ou encore hyperboloïque (-x²-y²+z²).
Expérimentalement, le modèle de la vision des couleurs par l'Humain se projette plutôt sur des hyperboloïdes... ok.. *à expliquer mieux*

Les voies parvo, magno et konio sont respectivement responsable de l'hyperboloÏde, de la distance à l'origine et de la position de l'origine des projections, telles que représenter sur la figure ci-dessous (à expliquer mieux!):

![[magno_parvo_konio_projection.png]]
Selon la longueur d'onde, la réponse des différentes voies varient, ces variations de réactions sont modélisées par les projections précedentes.
