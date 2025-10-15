---
prof: GARNIER Maeva
date: 2025-10-03
publish: true
---
# Perception de la hauteur

> [!NOTE] Notion importante  
> Hauteur **tonale** et **spectrale** : deux dimensions essentielles de la perception sonore.

## Hauteur spectrale

La hauteur spectrale correspond à **la distribution de l’énergie acoustique en fréquence**. Elle est généralement plus _diffuse_ et moins précise que la hauteur tonale. Sa perception est fortement liée à la Tonotopie du système auditif.

Le **barycentre spectral** désigne la fréquence autour de laquelle l’énergie est équilibrée :

- intégrale de l’énergie de $[0;Barycentre]$ égale à celle de $[Barycentre;+∞]$
    

![[spectralHeight.png]]

## Hauteur tonale

La hauteur tonale correspond à la **sensation de hauteur d’un son complexe périodique**, liée à sa fréquence fondamentale $F_0$. Elle permet d’identifier précisément une note. Sans périodicité, la hauteur tonale n’est pas définissable.

Exemple : note produite par la voix humaine (spectrogramme) :  
![[spectro_hauteurTonale.png]]

Cette perception repose sur le **codage temporel** du signal :  
![[codage_temp.png]]

## Exemple : Son à fondamentale filtrée

Lorsqu’une fondamentale est retirée du spectre :

- **Hauteur spectrale** :
    
    - Le spectre ne contient plus $F_0$
        
    - Hauteur perçue plus diffuse
        
    - Barycentre spectral **augmente**
        
- **Hauteur tonale** :
    
    - Les harmoniques régulières 2$F_0$,3$F_0$,... permettent de reconstruire une **fondamentale virtuelle** $F_0$
        
    - Hauteur perçue reste précise grâce au codage temporel
        

## Exemple : Chant diphonique

Dans le chant diphonique, le chanteur produit simultanément :

- Une fondamentale $F_0$
    
- Harmonique élevée fortement amplifiée par le conduit vocal
    

Effets :

- **Hauteur tonale** perçue sur $F_0$
    
- **Hauteur spectrale** perçue sur l’harmonique amplifiée (plus diffuse)
    

## Facteurs influençant la perception de hauteur

- **Durée minimale** nécessaire pour identifier la fréquence
    
- Variation de perception selon :
    
    - Durée de stimulation (sons brefs → plus grave)
        
    - Intensité (sons forts dans les basses → perçus plus aigus)
        
    - Spectre/timbre (ex. sifflement vs voix)
        

## Perception des intervalles

La perception des intervalles est fondée sur **le rapport de fréquence**, pas sur la différence absolue.  
![[intervalleF.png]]

Exemples :

- 440Hz→880Hz → octave (x2)
    
- 880Hz→1760Hz → octave (x2)
    

Cela découle de l’**organisation logarithmique** de la tonotopie cochléaire.

Au-delà de 2000 Hz, la perception des intervalles est moins directement reliée à la fréquence — d’où l’accord spécifique des instruments.

## Discrimination de l’oreille

![[discriOreil.png]]  
(JND = Just Noticeable Difference)

## Perception de deux sons simultanés

Plusieurs scénarios :

## 1. Masquage énergétique/simultané

> [!NOTE] Notion importante  
> Masquage énergétique/simultané

![[soundmaska.png]]

La largeur du triangle de masquage = **bande critique**, dépendant de la fréquence du son masqueur :

- Fréquences élevées → bande critique plus étroite (membrane basilaire plus rigide à la base)
    
- Fréquences basses → bande critique plus large (membrane plus souple à l’apex)
    

![[bandeCritique.png]]

Seuils de masquage : non symétriques (échelle linéaire)  
![[seuilTriangels.png]]

Facteurs principaux :

- **Fréquences des deux sons**
    
- **Amplitude relative**
    

## 2. Battements et rugosité

- **Battements** : deux fréquences proches (< 12 Hz) → modulation de l’amplitude  
    ![[battement.png]]
    
- **Rugosité** : différence entre 12 Hz et la bande critique → modulation plus prononcée
    
- **Polyphonie** : différence > bande critique → perception de deux sons distincts
    

# Perception de l’intensité

Entre seuil de perception et seuil de douleur : rapport $10^{-12}$$[watt/m^2]$. Utilisation du **décibel** : $n_{dB} = 10*log(\frac{I}{I_{seuil perception}})$. 
![[zoneaudtiion.png]]

## Sonie

La sonie est l’**intensité perçue** par l’audition, variant selon la fréquence.

Courbes d’isosonie :  
![[sonie.png]]

Exemple :

- 1000 Hz à 20 dB → équivalent à 100 Hz à 35 dB
    

## Influence de la durée

- < 0.5 s : sonie ↑ avec la durée
    
- 0.5 s – quelques s : sonie constante
    
- Plusieurs secondes (faible intensité) : sonie ↓
    

## Influence du contenu spectral

Sonie ↑ avec la largeur spectrale au-delà de la bande critique :  
![[bandecritsonie.png]]

## Masquage proactif

Masquage par un son précédent, accentué si :

- Fréquences proches
    
- Intervalle temporel court  
    ![[masquagepro.png]]
    

## Discrimination en intensité

![[audibilité.png]]

Exemple : 5500 sons différents discriminables dans zone “G” sur le graphique de droite.

Triple sensibilité de l’oreille :

1. Détection
    
2. Discrimination de la hauteur
    
3. Discrimination de l’intensité
    

## Fatigue et pertes auditives

## Fatigue

Un son intense augmente temporairement le seuil auditif :  
![[fatigue_aud.png]]

## Pertes auditives

![[perteaudit.png]]

> [!NOTE] _TODO_ Fiche sur les 6 points clefs du cours
> 
> - Sensibilité accrue à 2–3 kHz (3 facteurs)
>     
> - Principe de tonotopie
>     
> - Encodage de la fréquence
>     
> - Encodage de l’intensité
>     
> - Distinction hauteur spectrale / tonale
>     
> - Masquage énergétique
> 
> - Notion de timbre (causal + qualitatif)


# Perception du timbre

**Définition**: Attribut de la sensation auditive qui permet à l’auditeur de différencier deux sons de même hauteur et de même intensité et présentés de façon similaire.  « the psychoacoustician's multidimensional waste-basket category » (McAdams and Bregman 1979)

Il existe deux types de timbres:

> [!NOTE] Notion importante
> Timbre: 
> - Timbre causal: identification ou catégorisation de la source sonore
> - Timbre qualitatif: évaluation analytique de qualité sonore

## Timbre identitaire (causal)

- identification de catégories de sources ou de modes de production
- Irrépressible chez tous les auditeurs

Comment reconnaît on une source?
- *Critère 1*: Mode \frac{d'excitation}{Dynamique temporelle}-> Geste d'excitation
	- Geste continu: son entretenu
	- Choc unique: son impulsionnel (enveloppe dynamique asymétrique, sauf quelques exceptions comme le steel-drum)
	- Itération d'un impact à une cadence entre 10 et 20 Hz: son rugueux + modulation d'amplitude
	- ![[temporal_dynamic.png]]
- *Critère 2*: Modes propres de la structure/Distribution spectrale -> Matière/taille/vivant excitée
	- Structure du spectre: 
		- (a)périodicité
		- (in)harmonicité: concentration de l'énergie dans les harmoniques ou entre les harmoniques (=inharmonique)
		- f0
	- Distribution de l’énergie spectrale: 
	- Variation de cette enveloppe spectrale au cours du temps: variation de f0 (en particulier modulation en fréquence), variations formantiques…. (spectral flux)
	- ![[distri_spectrale_timbre.png]]


### Quels indices et dimensions discriminantes?
**Grey (1975)**:
- Largeur spectrale
- Synchronicité des transitoires des harmoniques HF
- Centroîde spectral des attaques
**McAdams et al. (1979)**:
- Durée de l’attaque 
- Centroïde spectral 
- Flux spectral

Pas de consensus.

**Méthode expérimentales**
1. Expériences de catégorisation à partir de stimuli transformés ou synthétiques
	- Hiérarchie d’indices, complémentarité, … 
2. Expériences de catégorisation libre 
	- Dimensions discriminantes (verbales)
	- Corrélats objectifs correspondants 
3. Tests de similarité 
	-  Distances
	- Analyse en composantes principale


## Timbre qualitatif

- Evaluation de variation de qualité sonores
- Fait appel à une forme d'expertise (musicale)

## Apport de la psycholinguistique

- Spécificité et polysémie du lexique en fonction de la catégorie de source sonore
	- (lien écoute causale / écoute analytique) 
	- Exemple : « Nasal » 
- Problème de traduction d’une langue à l’autre 
- Spécificité du lexique en fonction de l’expertise de l’auditeur et du but de son écoute 
	-  Exemple voix : prof de chant, acousticien, orthophoniste, … 
- => problème haut niveau faisant appel au langage, sémantique, culture, expériences passées). Le timbre n’est pas du tout un percept explicable par la physique principalement, comme pourraient l’être la hauteur et l’intensité.

**Méthodologie**: 
1. Inventaire et étude sémantique du lexique propre à la description de chaque catégorie pertinent à chaque catégorie de source (incluant style musical, ou genre pour la voix, et pas seulement l’instrument) et d’auditeur 
	-  • Verbalisation libre ou catégorisation libre 
	-  Psycholinguistique : fréquence d’utilisation, consensus sémantique (antonymie, synonymie, inclusion, causalités, …) 
2. Tests d’écoute à l’aide d’échelles sémantiques (antinomiques, un seul terme, ou échelles binaires, nombre de graduations de l’échelle, …)