---
prof: CAMPAGNE Aurélie
date: 2025-10-11
publish: true
---
 > [!NOTE] Examen  
> Question de cours + application; question de méthodo

# Introduction

Cours de neuroimagerie, principes et bases des mesures de surface (EEG : électroencéphalographie ; MEG : magnétoencéphalographie).  

## Anatomie du cerveau

![[anat_cerveau.png]]

Le cortex cérébral n'est pas une surface lisse : il comporte des **circonvolutions** (ou _gyrus_) séparées par des **sillons** (_sulci_). Les sillons les plus profonds sont souvent appelés **scissures**.  
La géométrie des gyrus et des sillons influence la direction des courants neuronaux et donc la topographie des signaux EEG et MEG (amplitude, signe, dispersion).

Les principales scissures (repères anatomiques) :

- **Scissure de Sylvius** (sillon latéral) : séparant les lobes _frontal_ et _temporal_.
    
- **Scissure de Rolando** (sillon central, ou scissure centrale) : sépare les lobes _frontal_ et _pariétal_ (repère entre cortex moteur et somesthésique).
    
- **Scissure pariéto-occipitale** : sépare le lobe _pariétal_ du lobe _occipital_.
    

![[Scissures.png]]

## Organisation fonctionnelle

On distingue classiquement deux grands types d'aires corticales :

- **Aires primaires**
    
    - _Aires sensorielles primaires_ — reçoivent directement les afférences périphériques :
        
        - Vue : cortex visuel primaire (V1), situé au niveau du lobe occipital (sillon calcarin).
            
        - Somesthésie : cortex somesthésique primaire, situé dans le gyrus postcentral (partie antérieure du lobe pariétal, juste derrière la scissure centrale).
            
    - _Aire motrice primaire_ — située dans le gyrus précentral (partie postérieure du lobe frontal, immédiatement en avant du sillon central).
        
- **Aires associatives**
    
    - Interviennent dans des traitements de niveau supérieur (intégration multimodale, mémoire, attention, langage, etc.). Ces aires reçoivent et intègrent des informations provenant de plusieurs régions primaires et associatives.
        

**Remarque importante :** certaines régions sont plutôt _préférentiellement_ impliquées dans certaines fonctions, mais il ne faut pas associer rigidement une région à une unique fonction. Les fonctions émergent de réseaux dynamiques : l'activation dépend du contexte, des boucles thalamo-corticales et cortico-corticales, et de la synchronisation entre régions.

## Organisation cérébrale

Le cerveau est composé, en surface, du **cortex** (substance grise) et, en profondeur, de la **matière blanche** (faisceaux de fibres reliant les régions corticales et sous-corticales).

![[couches_fibres.png]]

Types de fibres dans la matière blanche :

- **Fibres d'association** : relient différentes zones d'un même hémisphère (ex. faisceau arqué).
    
- **Fibres commissurales** : relient les deux hémisphères (ex. corps calleux).
    
- **Fibres de projection** : relient le cortex aux structures sous-corticales et à la moelle (ex. tractus corticospinal).
    

### Organisation en couches du cortex

Le cortex est organisé en **six couches** (numérotées de l'extérieur vers l'intérieur, I → VI), avec des distributions cellulaires et des connexions spécifiques :

- **Couche I** : couche moléculaire (peu de corps cellulaires, essentiellement des dendrites et des terminaisons axonales).
    
- **Couches II (externe) et IV (interne)** : riches en **cellules étoilées (stellées)** — principalement réceptrices d'**afférences** (par ex. entrées thalamiques, afférences cortico-corticales). Elles jouent un grand rôle dans le **traitement des informations entrantes**.
    
- **Couches III et V** : riches en **cellules pyramidales** — principales cellules projectives du cortex ; rôle majeur dans **l'intégration** et la **transmission** des signaux vers d'autres aires corticales (III) et vers des structures sous-corticales ou la moelle (V ; couche V contient les grandes pyramides de Betz, impliquées dans les projections motrices).
    
- **Couche VI** : projetée vers le thalamus (rôle dans la régulation thalamo-corticale).
    

Les cellules pyramidales sont souvent organisées en **colonnes corticales** : cette architecture favorise la sommation synchrone des courants et est centrale pour la génération de dipôles observables en EEG/MEG.

### Structure du neurone

![[Structure_neurone.png]]

- **Synapse** : zone de connexion entre deux neurones (pré- et post-synaptique) où se produisent la libération et la réception de neurotransmetteurs.  
    ![[synapse.png]]
    

**Potentiels locaux (post-synaptiques)**

- L'entrée d'ions modifie localement le potentiel membranaire : on parle de **potentiels post-synaptiques (PPS)** — en anglais PSP (postsynaptic potentials).
    
    - **Dépolarisation** (effet excitateur) : entrée d'ions positifs (ex. Na⁺) → le potentiel devient moins négatif.
        
    - **Hyperpolarisation** (effet inhibiteur) : entrée d'ions négatifs ou sortie d'ions positifs (ex. K⁺) → le potentiel devient plus négatif.
        
- Le **potentiel de repos** d'un neurone est d'environ **−70 mV**.
    
- Les PPS génèrent des **courants locaux** qui se propagent (et s'atténuent) dans le milieu intracellulaire et extracellulaire ; la géométrie cellulaire et l'environnement liquide influencent fortement cette atténuation.
    

**Segment initial / zone gâchette**

- La **zone gâchette** (au niveau du segment initial de l'axone) est le site où, si la dépolarisation locale dépasse un **seuil**, est déclenché le **potentiel d'action (PA)**.
    
- Le PA est bref (durée de l'ordre de la milliseconde), tout-ou-rien, et se propage le long de l'axone ; après émission, la membrane revient rapidement au potentiel de repos en l'absence d'inputs supplémentaires.  
    ![[gachette.png]]
    

**Conséquence pour EEG/MEG** :

- EEG et MEG sont **particulièrement sensibles aux courants transmembranaires synchrones générés par les PPS** des populations de cellules (sommation spatiale et temporelle).
    
- Les potentiels d'action, étant très courts et localisés, contribuent peu au signal de surface mesurable.
    

**Remarque métabolique / hémodynamique** :  
L'activité neuronale s'accompagne d'une demande accrue en oxygène et en nutriments ; ceci entraîne des variations du débit sanguin local (réponses hémodynamiques, de l'ordre de la seconde) — c'est le principe exploité par l'IRMf (voir autres cours).

# Les techniques d’imagerie cérébrale

L’étude du cerveau repose sur plusieurs méthodes d’imagerie qui se distinguent par leur **résolution temporelle** et **spatiale**. Ces deux caractéristiques déterminent la précision des mesures :

- **Résolution temporelle** → capacité à distinguer deux événements très proches dans le temps.
    
- **Résolution spatiale** → capacité à localiser précisément l’activité dans une région du cerveau.
    

![[tech_image.png]]

Certaines techniques offrent une **excellente précision temporelle** (comme l’EEG et la MEG, de l’ordre de la milliseconde), tandis que d’autres fournissent une **meilleure précision spatiale** (comme l’IRM fonctionnelle, de l’ordre du millimètre, mais avec un délai temporel de plusieurs secondes).  
Les méthodes électrophysiologiques (EEG/MEG) et les méthodes hémodynamiques (IRMf, PET) sont donc complémentaires.

# Nature, origine et topographie des signaux EEG et MEG

L’activité mesurée à la surface du scalp (EEG) ou à proximité du crâne (MEG) correspond à la **sommation** de l’activité électrique synchronisée de **milliers de neurones**, principalement les **cellules pyramidales corticales**.  
Ces signaux se traduisent souvent par des **oscillations** reflétant la dynamique temporelle de réseaux neuronaux.

| Technique | Objet mesuré           | Type de mesure | Résolution temporelle | Ordre de grandeur | Capteurs utilisés                    |
| --------- | ---------------------- | -------------- | --------------------- | ----------------- | ------------------------------------ |
| **EEG**   | Potentiels électriques | Relative       | ≈ 1 ms                | quelques µV       | Électrodes de surface                |
| **MEG**   | Champs magnétiques     | Absolue        | ≈ 1 ms                | ~10⁻¹³ Tesla      | Capteurs SQUID couplés à des bobines |

## Mesure EEG : principe et références

L’**EEG** mesure des **différences de potentiel électrique** entre une ou plusieurs électrodes.

Deux montages principaux :

- **Monopolaire** : chaque électrode est comparée à une électrode de référence fixe (méthode la plus utilisée en recherche).
    
- **Bipolaire** : mesure de la différence de potentiel entre deux électrodes actives (souvent utilisée en clinique).
    

### Choix de la référence en EEG monopolaire

Le choix du point de référence influence grandement le signal obtenu :

- **Sur le nez** : référence centrale, mais sensible aux artefacts liés aux mouvements oculaires.
    
- **Sur les mastoïdes** (derrière les oreilles) : très fréquemment utilisé.
    
- **Sur les lobes d’oreilles** (moyenne des deux côtés) : pratique, mais sensible à la morphologie ou aux piercings.
    
- **Référence moyenne** : calculée sur un grand nombre d’électrodes (>64). C’est la méthode la plus “neutre”, car elle reflète davantage l’activité cérébrale globale.
    

## Activités oscillatoires

![[rythmes.png]]

Les signaux EEG/MEG présentent des **rythmes oscillatoires** (alpha, bêta, gamma, etc.), reflétant la coordination temporelle des réseaux neuronaux.

### Origine des signaux oscillatoires

Plusieurs structures et boucles neuronales participent à la génération de ces rythmes :

- **Boucles thalamo-corticales** :  
    Le thalamus agit comme un **relais sensoriel** et un “chef d’orchestre” de l’activité corticale. Il régule la fréquence et la synchronisation des signaux corticaux.
    
- **Boucles cortico-corticales** :  
    Permettent la **synchronisation** de différentes régions du cortex selon la tâche ou l’état cognitif.
    
- **Rôle des cellules gliales (astrocytes)** :  
    Elles modulent l’activité neuronale via la régulation du métabolisme, des échanges ioniques et du recyclage des neurotransmetteurs.
    

![[sommeSPatiTemp.png]]

### Origine physique des signaux EEG/MEG

Lorsqu’un neurone reçoit une entrée synaptique, l’entrée d’ions dans la membrane crée des **courants locaux** (dits _courants primaires_).  
Pour maintenir la neutralité électrique, d’autres ions circulent en sens inverse dans le milieu extracellulaire : ce sont les **courants secondaires**.

![[courantPrimaires.png]]

Les PPS (potentiels post-synaptiques) génèrent des **champs dipolaires** qui se propagent relativement loin (leur amplitude décroît peu avec la distance), contrairement aux potentiels d’action.  
Ainsi :

- Les **PPS** favorisent la **synchronisation temporelle** de larges populations de neurones → signal mesurable en EEG/MEG.
    
- Les **potentiels d’action**, trop brefs et dispersés, n’y contribuent presque pas.
    

![[pyramidVSetoile.png]]

Les **cellules pyramidales** jouent un rôle central : leur orientation verticale (par rapport à la surface corticale) permet la **sommation constructive** des courants électriques dans une même direction.  
C’est pourquoi elles sont les principales contributrices aux signaux EEG/MEG, contrairement aux cellules étoilées, orientées aléatoirement.

La **synchronisation temporelle** observée dépend à la fois :

- des **boucles thalamo-corticales et cortico-corticales**,
    
- et de l’activité synchrone des PPS.
    
### Le macro-dipôle cortical

L’activation simultanée de milliers de cellules pyramidales dans une colonne corticale crée un **macro-dipôle**.  
Sa direction est **perpendiculaire à la surface corticale locale**, et son amplitude dépend de la **somme des densités de courants** au sein de cette colonne.

![[macro_dipole.png]]

## EEG et MEG : géométrie des dipôles

Selon la position du **macro-dipôle** sur le cortex, il peut être :

- **Radial** (orienté perpendiculairement à la surface du scalp, souvent sur les gyrus), ou
    
- **Tangentiel** (orienté parallèlement au scalp, souvent au fond des sillons).
    

Ces orientations déterminent la manière dont les signaux apparaissent en EEG et en MEG :

![[Dipoles_rad_tang]]  
![[topographie.png]]

Les champs magnétiques étant **perpendiculaires aux courants électriques**, la MEG capte principalement les **composantes tangentielles**.

![[MEG_EEG.png]]

### Différences spatiales entre EEG et MEG

- En **EEG**, le signal électrique issu d’une source unique apparaît **étalé** sur le scalp à cause de la conductivité variable des tissus (os, peau, liquide céphalorachidien).
    
- En **MEG**, les champs magnétiques sont **moins déformés** par les milieux traversés → **meilleure résolution spatiale**.
    

Effets de la distance à la source :

- **Amplitude** du signal diminue avec la profondeur.
    
- **Dispersion spatiale** augmente avec la distance à la source.
    
### Sensibilité relative des deux techniques

|Type de source|MEG|EEG|Commentaire|
|---|---|---|---|
|**Radiale**|~1/10|2|L’EEG est plus sensible aux sources radiales (gyrus).|
|**Profonde**|~1/3|1/100|La MEG perd moins de signal en profondeur que l’EEG, mais reste surtout sensible aux sources superficielles.|
### Sources multiples

En pratique, les signaux mesurés résultent de la **sommation de plusieurs macro-dipôles** actifs simultanément.  
Ainsi, une activité observée sur une zone donnée du scalp ne signifie pas forcément que la région sous-jacente est activée.  
Exemple : une onde auditive peut apparaître sur le sommet du crâne alors que les sources réelles se trouvent dans les régions temporales.

---

## Résumé EEG vs MEG

|**MEG**|**EEG**|
|---|---|
|Mesure les **champs magnétiques**|Mesure les **potentiels électriques**|
|Réponse dipolaire **perpendiculaire** à la direction du dipôle|Réponse dipolaire **parallèle** à la direction du dipôle|
|Réponse **focale**|Réponse **diffuse**|
|Peu affecté par les tissus (crâne, peau, liquide céphalorachidien)|Fortement influencé par la conductivité des tissus|
|Sélectif pour les **sources tangentielles**|Sensible à **toutes les orientations**|
|Peu sensible aux **sources profondes**|Peut détecter des sources plus profondes (mais avec une précision limitée)|
|**Très coûteux**, nécessite un environnement contrôlé|**Moins coûteux**, plus facilement déployable|
# Dispositifs et principes de mesure des signaux

## MEG — Magnétoencéphalographie

La **MEG** mesure les champs magnétiques extrêmement faibles produits par l’activité neuronale. Ces champs sont de l’ordre de **10⁻¹³ Tesla**, soit environ un milliard de fois plus faibles que le champ magnétique terrestre.  
Pour pouvoir détecter de tels signaux, l’installation doit être **extrêmement isolée** et dotée de capteurs ultra-sensibles.

### Environnement expérimental

L’enregistrement MEG s’effectue dans une **chambre blindée** (une cage de Faraday) qui bloque les champs électromagnétiques externes :

- champs électriques des prises,
    
- ondes radios,
    
- signaux des téléphones, etc.
    

### Principe de détection

La détection se fait via des **bobines** sensibles aux variations de champ magnétique. Ces bobines sont couplées à des capteurs appelés **SQUIDs** (_Superconducting Quantum Interference Devices_).  
Les SQUIDs fonctionnent uniquement à **très basse température**, en **supraconductivité**, ce qui nécessite un **refroidissement à l’hélium liquide**. C’est l’un des principaux facteurs de coût et de complexité du dispositif MEG.

![[MEG_dispositif.png]]

Le signal est amplifié par ces capteurs puis traité numériquement. Les MEG modernes comportent plusieurs centaines de capteurs, couvrant presque entièrement le crâne du participant.

## EEG — Électroencéphalographie

L’**EEG** enregistre directement les différences de potentiel électrique à la surface du scalp.  
C’est une méthode **moins coûteuse** et **plus accessible** que la MEG, mais également **plus sensible aux artefacts** (mouvements, conductivité variable du crâne, etc.).

### Types d’électrodes

Les électrodes EEG sont placées directement sur la tête selon des systèmes standardisés. Elles peuvent être classées selon deux dimensions principales :  
**passives vs actives** et **humides vs sèches**.

|Type d’électrode|**Passive**|**Active**|**Humide**|**Sèche**|
|---|---|---|---|---|
|**Principe**|Simple réception du signal nerveux|Pré-amplification du signal directement à la source|Utilisent un gel conducteur entre l’électrode et la peau|Fonctionnent sans gel|
|**Avantages**|Simples, peu coûteuses|Réduction du bruit, meilleure qualité du signal|Excellente conductivité|Installation rapide|
|**Inconvénients**|Sensibles au bruit et à la distance du fil|Plus chères|Longues à poser, inconfort possible|Artefacts fréquents, signal moins stable|

![[EEG_dispo.png]]

Les électrodes **actives** intègrent un petit amplificateur qui réduit les interférences dues à la distance entre la tête et l’amplificateur principal, ce qui améliore la qualité du signal.

### Système international 10-20

Le positionnement des électrodes est normalisé par le **système international 10-20**, valable pour les casques jusqu’à environ 21 voies.  
Ce système repose sur quatre points de référence anatomiques :

- **Nasion** (creux entre les yeux, à la racine du nez),
    
- **Inion** (protubérance occipitale, à l’arrière du crâne),
    
- **Points préauriculaires gauche et droit** (devant les oreilles).
    

La première électrode posée est la **centrale**, située au **vertex** (sommet du crâne).  
Les distances entre électrodes correspondent à **10 % ou 20 %** des distances entre ces points de référence, d’où le nom du système.

![[10_2.png]]

Aujourd’hui, les systèmes modernes utilisent souvent un espacement de **5 %** pour une meilleure **résolution spatiale**, ce qui permet d’augmenter le nombre total d’électrodes (jusqu’à 128, 256 ou plus).

### Mesure de la position des électrodes par rapport au cerveau

Pour une interprétation fiable des signaux EEG, il faut connaître précisément la position des électrodes par rapport au cerveau.  
Idéalement, on dispose d’une **IRM individuelle** du participant, permettant une **reconstruction anatomique personnalisée**.  
Si cette IRM n’est pas disponible, on utilise un **modèle de tête standardisé** construit à partir de la moyenne de plusieurs centaines ou milliers d’IRM.

La position exacte des électrodes est alors reconstruite numériquement à partir de :

- leurs coordonnées 3D,
    
- les points de référence anatomiques (nasion et préauriculaires),
    
- et la forme du contour crânien du participant.
    

Ces informations permettent de **co-localiser** les mesures EEG/MEG avec l’anatomie cérébrale pour l’analyse de sources.

# Protocoles d’étude et traitement des signaux EEG/MEG

## Structure d’une expérience EEG/MEG

Les signaux EEG/MEG sont toujours enregistrés **en contexte expérimental contrôlé**.  
L’objectif est de relier l’activité cérébrale mesurée à des **événements précis** (stimuli visuels, sons, actions, réponses, etc.).

### Organisation typique d’une étude

1. **Planification du protocole**
    
    - Choix des stimuli et du type de tâche (visuelle, auditive, motrice…).
        
    - Définition de la durée et du nombre d’essais (trials).
        
    - Contrebalancement des conditions expérimentales.
        
2. **Acquisition**
    
    - Enregistrement simultané du signal EEG ou MEG et des marqueurs d’événements.
        
    - Les marqueurs (ou _triggers_) sont envoyés par l’ordinateur de présentation de la tâche au système d’enregistrement pour aligner précisément le signal avec les stimuli.
        
3. **Prétraitement**
    
    - Nettoyage du signal, suppression du bruit et des artefacts.
        
    - Segmentation des données en **époques** autour des événements d’intérêt.
        
    - Alignement temporel des essais.
        
4. **Analyse**
    
    - Calcul d’**ERPs (potentiels évoqués)** ou **ERFs (champs évoqués)**.
        
    - Études fréquentielles (oscillations, synchronisation).
        
    - Analyses de source (modélisation de l’origine du signal dans le cerveau).
        
## Prétraitement du signal

Le prétraitement vise à **rendre les signaux interprétables** sans introduire d’artéfacts artificiels.  
Il comprend plusieurs étapes essentielles.

### 1. Filtrage

Les signaux EEG/MEG contiennent des composantes de fréquence variées (0 à plusieurs centaines de Hz).  
Un **filtrage** est nécessaire pour :

- supprimer les **bruits très lents** (mouvements, dérives de l’amplificateur),
    
- éliminer les **hautes fréquences parasites** (musculaires, électriques).
    

Types de filtres courants :

- **Filtre passe-bas** (low-pass) → supprime les hautes fréquences (ex. > 30 Hz).
    
- **Filtre passe-haut** (high-pass) → supprime les très basses fréquences (ex. < 0.1 Hz).
    
- **Filtre notch (anti-parasite)** → retire une fréquence spécifique (ex. 50 Hz ou 60 Hz du courant électrique).
    

> [!NOTE]  
> Un filtrage mal paramétré peut **détruire l’information** temporelle ou créer de **faux décalages de phase**.  
> Il est donc crucial de vérifier la stabilité des résultats avec différents paramètres.

### 2. Correction des artefacts
([Identification et correction des artéfacts]( https://www.youtube.com/watch?v=zH3fim2uIHs))
Les signaux EEG/MEG sont sensibles à de nombreuses sources de bruit non cérébral :

- **Mouvements oculaires** (clignements, saccades), 
    
- **Activité musculaire** (mâchoire, cou, front),
    
- **Bruits cardiaques**,
    
- **Micro-mouvements du capteur ou du participant**.
    

#### Méthodes de correction

- **Rejet manuel d’essais contaminés** : suppression des segments trop bruités.
    
- **Correction automatique** :
    
    - **ICA (Independent Component Analysis)** : séparation des composantes indépendantes du signal, permettant d’isoler et retirer celles correspondant à des artefacts (ex. composante “clignement”).
- **Recourt à l'EOG** (Electro-Oculographie):
	- Mesure bipolaire, au moins 4 éléctrodes pour séparer l'EOG verticale (clignement + mouvements oculaires verticaux) et horizontale (mouvement oculaires horizontaux). Idéalement, la composante horizontale ne mesure strictement QUE de l'horizontale et pareil pour la verticale; ce résultat est obtenu en plaçant parfaitement les 4 électrodes (le sens de variation dépend du montage, il n'y a pas de convention): ![[position_electrodes.png]]
-  **Recourt à l'ECG** (Electro-Cardiographie): 
	- Mesure bipolaire, rarement nécessaire car le signal émit par le cœur est de forme très typique (simplement fréquence variable). Deux électrodes (+ la masse) suffisent.
- **Recourt à l'EMG** (Electro-myographie):
	- Mesure bipolaire, attention, toute correction liée à l'activité musculaire est un potentiel biais pour la mesure initiale (car l'EMG va elle-même présenter des artéfacts). En cas de mesure à artéfacts, il est souvent préférable de simplement supprimer les mesures concernées.
### 3. Segmentation et moyennage

Une fois le signal nettoyé, on le découpe en **époques temporelles** centrées sur chaque événement d’intérêt (par ex. de -200 à +800 ms autour du stimulus).  
Les époques sont ensuite **moyennées** pour augmenter le rapport signal/bruit :  
les réponses aléatoires s’annulent, tandis que les réponses stables (évoquées par le stimulus) se renforcent.

Ce moyennage donne les **potentiels évoqués (ERP - Event Related Potentiel)** en EEG, ou les **champs évoqués (ERF - Event Related Field)** en MEG.

![[PE_CE.png]]

> [!NOTE]  
> Ce traitement suppose que la réponse cérébrale est **temporellement stable et phasée** par rapport à l’événement.  
> Pour des phénomènes plus variables dans le temps (ex. oscillations), on utilisera plutôt des **analyses fréquentielles**.

### 4. Correction de la ligne de base

Souvent, on enregistre pour chaque sujet l'activité EEG avant et après la période de tâche, pendant 5 minutes. On fait ensuite la moyenne de ces deux périodes afin de la soustraire/diviser/Zscore au reste du signal (Z score: différence normalisée).

![[lignedebase.png]]



## Analyses des signaux

L'analyse des signaux est spécifique du but de l'étude, on peut typiquement distinguer deux types d'analyses:
- **globale** (évolution d'état de vigilance dans différents contextes; évolution d'état émotionnels; ...)
- **locale**, discrimination des processus cérébraux (capacité de discrimination d'un visage; impact d'une condition expérimentale sur un processus de traitement; ...)


> [!NOTE] Examen
> Questions sur les analyses pas plus détaillées que l'image suivante, on est allé trop vite sur la suite du cours pour être interrogé dessus. --> Potentiels et champs évoqué? Pour mesurer quoi? Pareil pour Analyse spectrale; connectivités; analyse de sources.

![[analyses_EEG.png]]


### 1. Analyses temporelles — ERP / ERF

Les ERP (EEG) et ERF (MEG) sont des moyennes temporelles qui révèlent les **composantes évoquées**.  
Elles sont nommées selon :

- leur **polarité** (P = positive, N = négative),
    
- leur **latence moyenne** (en millisecondes après le stimulus).
    

Exemples :

- **P100** : pic positif à ~100 ms, souvent visuel.
    
- **N170** : pic négatif à ~170 ms, associé à la perception des visages.
    
- **P300** : pic positif vers 300 ms, lié à la détection d’un événement rare ou significatif.
    

Les **latences** renseignent sur le délai de traitement, et les **amplitudes** sur l’intensité ou l’implication des processus cognitifs.

### 2. Analyses fréquentielles — Oscillations cérébrales

Les signaux EEG/MEG reflètent aussi des **oscillations spontanées** ou **induites** dans différentes bandes de fréquences :

|Bande|Fréquence (Hz)|Signification fonctionnelle approximative|
|---|---|---|
|**Delta**|0.5 – 4|Sommeil profond, processus lents|
|**Theta**|4 – 8|Mémoire, navigation, attention interne|
|**Alpha**|8 – 13|Repos, inhibition, traitement visuel|
|**Beta**|13 – 30|Mouvement, attention, prédiction|
|**Gamma**|> 30|Intégration perceptive, conscience|

![[spectrale_event.png]]

Les analyses temps-fréquence (par ondelettes, transformée de Fourier, etc.) permettent d’observer comment la puissance oscillatoire varie au cours du temps et selon les conditions expérimentales. Ces analyses permettent aussi de rendre compte de la *dynamique cérébrale* et des *interactions neuronales*:

![[connectivites.png]]


### 3. Analyses de source

L’objectif ici est de **retrouver où dans le cerveau** se trouvent les générateurs des signaux mesurés en surface.  
Ce problème est appelé **problème inverse** (on part du signal mesuré pour inférer la source).

Deux approches principales :

- **Modèles dipolaires** : estiment un ou plusieurs dipôles équivalents (modèle simplifié).
    
- **Méthodes distribuées** : estiment une carte continue de sources sur tout le cortex (ex. MNE – _Minimum Norm Estimate_).


![[sourcedusignalEEG.png]]

> [!NOTE]  
> Le problème inverse n’a **pas de solution unique** : plusieurs distributions de sources peuvent produire la même topographie de surface.  
> On doit donc imposer des **contraintes** (anatomiques, physiques, statistiques) pour rendre la solution plausible.




# Résumé

## 1. Différences EEG - MEG

| Caractéristique            | **EEG**                                                                                             | **MEG**                                                                |
| -------------------------- | --------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| **Signal mesuré**          | Différences de potentiel électrique à la surface du scalp                                           | Champs magnétiques induits par les courants neuronaux                  |
| **Unités**                 | Microvolts (µV)                                                                                     | Femtoteslas (fT)                                                       |
| **Capteurs**               | Électrodes en contact avec la peau                                                                  | Bobines SQUID refroidies (sans contact direct)                         |
| **Orientation sensible**   | Sensible aux **composantes radiales** du dipôle neuronal (perpendiculaires à la surface du crâne)   | Sensible aux **composantes tangentielles** (parallèles à la surface)   |
| **Influence des tissus**   | Le signal est atténué et déformé par les couches du scalp, du crâne et du liquide céphalo-rachidien | Le champ magnétique traverse les tissus sans déformation majeure       |
| **Résolution temporelle**  | Excellente (millisecondes)                                                                          | Excellente (millisecondes)                                             |
| **Résolution spatiale**    | Moyenne (1–3 cm)                                                                                    | Bonne (quelques mm à 1 cm)                                             |
| **Coût / logistique**      | Faible, portable, installation simple                                                               | Très coûteuse, nécessite une chambre blindée et du hélium liquide      |
| **Sensibilité anatomique** | Bon accès aux régions **corticales superficielles** et radiales                                     | Meilleure sensibilité aux **sources tangentielles** (dans les sillons) |
| **Usage clinique typique** | Épilepsie, sommeil, pathologies psychiatriques                                                      | Recherche cognitive, cartographie fonctionnelle préchirurgicale        |

## 2. Complémentarité EEG / MEG

Les signaux EEG et MEG proviennent de la même activité neuronale (courants postsynaptiques des cellules pyramidales), mais offrent **des perspectives différentes** :

- L’**EEG** capture mieux les sources orientées radialement, situées sur les _crêtes des gyrus_.
    
- La **MEG**, au contraire, est plus sensible aux sources tangentielles, situées dans les _sillons_.
    

Ainsi, leur **combinaison** permet une **meilleure couverture spatiale** du cortex et une estimation plus robuste des sources neuronales.
