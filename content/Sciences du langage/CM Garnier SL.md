---
prof: GARNIER Maeva
date: 2025-10-03
publish: true
---


# Perception de la hauteur


> [!NOTE] Notion importante
> Hauteur tonale et spectrale!


## Hauteur spectrale

Correspond à la distribution de l'énergie acoustique en fréquence, elle est typiquement plus '*diffuse*' que la hauteur tonale. La perception des ces différentes variations est due à la [[Tonotopie]] de notre système auditif. 

On appelle *barycentre spectral* l'endroit où se concentre l'énergie (il correspond à la fréquence 'médiane' telle qu'il y ait autant d'énergie de plus haute fréquence que de plus basse fréquence, i.e. l'intégrale de $[0;Barycentre]$ est égale à celle de $[Barycentre; +\infty]$).


![[spectralHeight.png]]
## Hauteur tonale

Correspond à la sensation de hauteur d'un son complexe périodique, elle est liée à la fréquence fondamentale du son, cette sensation est plus précise et permet typiquement d'identifier la 'note' jouée. (La notion de hauteur tonale n'est pas applicable sans périodicité dans les signaux). Exemple d'une note produite par la voix humaine sur un spectrogramme:
![[spectro_hauteurTonale.png]]

La hauteur tonale repose sur le phénomène de codage temporel:
![[codage_temp.png]]

### Exemple de son à fondamentale filtrée
Notre cerveau est capable de reconstituer la période sous jacente à la série harmonique entendu. Cet exemple illustre précisément la différence entre hauteur spectrale et tonale:
- *Hauteur spectrale*:
	- Sans la première harmonique, le spectre *objectif* ne contient plus la fréquence fondamentale
	- la hauteur perçue est diffuse, il ne reste plus que l'empilement d'harmoniques
	- *Le barycentre augmente lorsque la fondamentale est retirée*
- *Hauteur tonale*:
	- Grâce à l'espacement régulier des harmoniques ($2*F0, 3*F0, 4*F0,...$), le système auditif reconstruit une fréquence fondamentale $F0$ virtuelle.
	- La hauteur tonale reste donc précise, perçue comme $F0$
	- Le codage temporel permet de reconstituer la fondamentale.
### Exemple du chant diphonique

Le chant *diphonique* où un chanteur produit deux sons distincts en même temps : une note de base (la fondamentale) et une mélodie parallèle constituée d’harmoniques aiguës:
- Comme tout son voisé, la voix humaine contient une fréquence fondamentale (F0) et un ensemble d’harmoniques (multiples de F0).
- Dans le chant normal, ces harmoniques sont tous présents, mais mélangés et perçus globalement comme le timbre de la voix.
- Dans le chant diphonique, le chanteur *renforce sélectivement une harmonique particulière* grâce à son conduit vocal, de sorte qu’elle devient audible comme une seconde « voix » claire et mélodique.
	- La *hauteur tonale* renvoie dans ce cas généralement à la perception de la  fréquence fondamentale $F0$.
	- La *hauteur spectrale* renvoie dans ce cas généralement à la perception (souvent) diffuse d'une harmonique particulière.

### Autres éléments intervenant dans la perception de la hauteur

- Nécessité d'une durée minimale pour percevoir la fréquence d'un son
- La sensation de hauteur varie avec:
	- la durée de stimulation (un son très bref à tendance à être perçu comme plus grave).
	- l'intensité, en particulier dans les basses fréquences où un son joué plus fort peut être perçu comme plus aigu.
	- le spectre du son (~le timbre): un sifflement est perçu différemment d'une voix

## Perception des intervalles

La *perception des intervalles* dépend du *rapport de fréquence* plutôt que de la différence de fréquence:
![[intervalleF.png]]

Par exemple, on perçoit une *octave* entre $440 Hz$ et $880 Hz$ (+440, *x2*) et on perçoit de la même manière une octave entre $880 Hz$ et $1760 Hz$ (+880, *x2*). Cela est du à la disposition logarithmique de la tonotopie dans la cochlée.

Au delà de $2000 Hz$, la perception des intervalles n'est plus directement en relation avec la fréquence (les instruments de musique son accordés en conséquence).

### Capacité de discrimination de l'oreille

![[discriOreil.png]]

(*JND*= Just Noticeable Difference)

## Perception de deux sons simultanés

Plusieurs cas sont possibles:
### Perception d'un seul des deux sons (*masquage*)

> [!NOTE] Notion importante
> Masquage énergétique/simultané

![[soundmaska.png]]

La *largeur* du 'triangle' *de masquage* correspond à la *bande critique*. 

D'un point de vue physiologique, la bande critique dépend de la fréquence du masqueur:
![[bandeCritique.png]]

La *bande critique* due aux *fréquences élevée* est plus *réduite* que celle provoquée par des fréquences *faibles* du fait de la variation de *rigidité de la membrane basilaire*; celle-ci étant plus rigide à la base (rayon de courbure plus grand; sensible aux hautes fréquences) et plus souple à son apex (rayon de courbure plus faible; sensible aux basses fréquences).

Les seuils de masquage ne sont pas symétrique autour des fréquences (échelle linéaire): ![[seuilTriangels.png]]

Le **masquage énergétique** (simultané) dépend donc de:
- la *fréquence* des deux sons
- l'*amplitude relative* des deux sons
### Perception de sons, avec un battement ou rugosité

- Due à la rigidité de la membrane basilaire:
- **Battements**: Lorsque les fréquences des deux sons sont très proches (différence < 12 Hz):
	- Fréquence perçue et amplitude altérée: ![[battement.png]]
- **Rugosité**: 12 Hz < différence < Bande critique:
	- Rugosité <=> un seul son perçu toujours, mais forte modulation en amplitude
- **Polyphonie**: différence > Bande critique. -> Perception de deux sons distincts


# Perception de l'intensité

Il y a un rapport de $10^{-12}$ entre le seuil de perception et le seuil de douleur ($[watt/m^2]$). On utilise donc le décibel (dB): $n_{dB} = 10*log(\frac{I}{I_{seuil perception}})$.

![[zoneaudtiion.png]]

## Sonie

La sonie correspond à l'intensité réelle, perçue par le système auditif, elle varie en fonction de la fréquence du son.

Courbe de variation de la sensibilité auditive avec la fréquence:
![[sonie.png]]
Exemple pour un son de 1000 Hz, entendu à 20 dB; il faudrait le présenter à 35 dB pour qu'il soit entendu de la même intensité à 100 Hz.

### Influence de la durée
- durée < 0.5s: augmentation de la sonie avec la durée
- durée > 0.5s: sonie constante
- durée > plusieurs secondes: sonie décroissante pour les sons de faible intensité

### Influence du contenu spectral
Augmentation de la sonie avec la largeur spectrale (à partir d'une largeur spectrale définie: la **bande critique**):
![[bandecritsonie.png]]


## Masquage proactif
Masquage d'un son par un son qui précède, masquage plus important avec:
- proximité fréquentielle des deux sons
- proximité temporelle des deux sons

![[masquagepro.png]]

## Discrimination en intensité

![[audibilité.png]]
Sur le graphique de droite, les courbes de niveau indiquent notre capacité de discrimination de sons, par exemple, on peut distinguer 5500 sons différents dans la zone 'G'.

La zone de sensibilité de l'oreille est triple:
- capacité de détection
- capacité de discrimination:
	- de la hauteur
	- de l'intensité

## Fatigue et perte auditive

### Fatigue
Après l'audition d'un son intense, le seuil d'audition est plus élevé que normalement:
![[fatigue_aud.png]]

### Pertes auditives

![[perteaudit.png]]



> [!NOTE] *TODO* Fiche sur les 6 points clefs du cours
> - les trois facteurs qui contribuent à la sensibilité particulière de notre système auditif à 2-3kHz
> - le principe de tonotopie
> - encodage de la fréquence des sons
> - encodage de l'intensité des sons
> - distinction et définition des hauteurs spectrale/tonale
> - masquage énergétique
