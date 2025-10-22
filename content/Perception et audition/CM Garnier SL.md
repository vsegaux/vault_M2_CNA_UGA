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

**Définition**  
Le **timbre** est un attribut de la sensation auditive qui permet à un auditeur de distinguer deux sons ayant **la même hauteur** et **la même intensité**, lorsqu’ils sont présentés de façon similaire.  
Selon McAdams et Bregman (1979), il s’agit de « _the psychoacoustician’s multidimensional waste-basket category_ », c’est-à-dire une catégorie multidimensionnelle rassemblant de nombreux paramètres perceptifs difficilement isolables.

Il existe **deux types de timbres** principaux :

> [!NOTE] Notion importante  
> **Timbre :**
> 
> - **Timbre causal** → identification ou catégorisation de la **source sonore**.
>     
> - **Timbre qualitatif** → évaluation **analytique de la qualité sonore**.
>     


## Timbre identitaire (ou causal)

Le **timbre identitaire** concerne la capacité à identifier la **catégorie de la source sonore** ou le **mode de production du son**.  
C’est une compétence **irrépressible** chez tout auditeur : nous reconnaissons spontanément la nature d’un son (voix, instrument, bruit d’objet…).

### Comment reconnaît-on une source ?

Deux grands types de **critères** sont impliqués :

#### _Critère 1 :_ Mode d’excitation → Dynamique temporelle → Geste d’excitation

Le **mode d’excitation** du son (comment il est produit) influence directement sa **dynamique temporelle**.

- **Geste continu** → son entretenu (ex. : violon, orgue).
    
- **Choc unique** → son impulsionnel, caractérisé par une **enveloppe dynamique asymétrique** (ex. : percussion).
    
    - _Exception notable :_ certains instruments comme le **steel-drum** présentent un comportement particulier.
        
- **Itération rapide d’impacts** (10 à 20 Hz) → son **rugueux**, accompagné d’une **modulation d’amplitude**.
    

![[temporal_dynamic.png]]

#### _Critère 2 :_ Modes propres de la structure → Distribution spectrale → Matière / taille / entité excitée

Ce critère concerne la **structure du spectre** et la manière dont l’énergie sonore est répartie.

- **Structure spectrale :**
    
    - (A)périodicité du signal
        
    - (In)harmonicité : concentration de l’énergie sur les harmoniques (harmonique) ou entre elles (inharmonique)
        
    - Fréquence fondamentale (_f₀_)
        
- **Distribution de l’énergie spectrale :**  
    Répartition de l’énergie dans le spectre fréquentiel.
    
- **Variation temporelle de cette enveloppe spectrale :**  
    Changements dans le temps :
    
    - Variations de _f₀_ (modulations de fréquence)
        
    - Variations **formantiques** (spectral flux)
        

![[distri_spectrale_timbre.png]]


### Indices et dimensions discriminantes du timbre

Différents chercheurs ont identifié des **indices perceptifs** servant à différencier les timbres :

**Grey (1975)**

- Largeur spectrale
    
- Synchronicité des transitoires des harmoniques hautes fréquences
    
- Centroïde spectral des attaques
    

**McAdams et al. (1979)**

- Durée de l’attaque
    
- Centroïde spectral
    
- Flux spectral
    

**Pas de consensus général** : les dimensions du timbre varient selon les stimuli et les contextes expérimentaux.


### Méthodes expérimentales d’étude du timbre

1. **Expériences de catégorisation à partir de stimuli transformés ou synthétiques**  
    → Permettent d’identifier la **hiérarchie** et la **complémentarité** des indices perceptifs.
    
2. **Expériences de catégorisation libre**  
    → Permettent d’explorer les **dimensions discriminantes verbales** et d’en dégager des **corrélats acoustiques objectifs**.
    
3. **Tests de similarité**  
    → Mesurent les **distances perceptives** entre sons et permettent une **analyse en composantes principales (ACP)** pour identifier les dimensions du timbre.
    

## Timbre qualitatif

Le **timbre qualitatif** correspond à l’**évaluation des variations de qualité sonore**.  
Il s’appuie sur une **écoute analytique** et fait souvent appel à une **forme d’expertise musicale ou acoustique**.  
Cette approche du timbre cherche à qualifier finement les différences de sonorité : ronde, métallique, douce, nasale, etc.

## Apports de la psycholinguistique

La psycholinguistique étudie la manière dont le **langage** structure notre perception et notre description du timbre.

- Le **lexique du timbre** varie selon :
    
    - La **catégorie de la source sonore** (instrument, voix, bruit, etc.)
        
    - Le **contexte d’écoute** (écoute causale ou analytique)
        
    - La **langue** (certains termes n’ont pas d’équivalent exact)
        
    - Le **niveau d’expertise de l’auditeur** et le **but de l’écoute**
        

Exemples :

- Le terme **« nasal »** peut décrire aussi bien une voix qu’un instrument à vent.
    
- Les descriptions d’une **voix** varient selon l’expert (professeur de chant, acousticien, orthophoniste…).
    

Ainsi, le **timbre** engage des processus **cognitifs de haut niveau** : langage, sémantique, culture, expériences passées.  
Il ne peut donc pas être expliqué uniquement par la **physique acoustique**, contrairement à la hauteur ou à l’intensité.


### Méthodologie psycholinguistique

1. **Inventaire et analyse sémantique du lexique**
    
    - Réaliser un inventaire des termes employés pour décrire les sons selon leur **catégorie de source**, **style musical**, **genre vocal**, et **profil d’auditeur**.
        
    - Méthodes :
        
        - Verbalisation libre ou catégorisation libre
            
        - Études psycholinguistiques : fréquence d’utilisation, consensus sémantique (synonymie, antonymie, inclusion, causalité…)
            
2. **Tests d’écoute avec échelles sémantiques**
    
    - Échelles **antinomiques** (chaud ↔ froid, brillant ↔ mat, etc.)
        
    - Échelles **unipolaires** (un seul terme, ex. : brillant)
        
    - Échelles **binaires** avec un nombre de **graduations** défini selon la précision attendue.
        