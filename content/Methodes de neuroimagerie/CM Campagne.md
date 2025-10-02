---
prof: CAMPAGNE Aurélie
date: 2025-09-29
publish: true
---
 
> [!NOTE] Examen
> Question de cours + application; question de méthodo

# Introduction
Cours de neuroimagerie; mesures de surfaces EEG et MEG.

## Anatomie du cerveau

![[anat_cerveau.png]]
Note: Le cerveau n'est pas lisse, il présente des *circonvolutions* (*gyrus*) qui vont avoir un impact sur les mesures de surfaces (EEG, MEG). Ces circonvolutions sont séparées par des *sillons* (*sulcus*). Les plus profonds de ces sillons sont les *scissures*:

Les lobes cérébraux sont délimités par des *scissures*:
- scissure de *Sylvius* entre le lobe *Frontal* et le lobe *Temporal*
- scissure de de *Rolando* (scissure *centrale*) entre le lobe *Frontal* et le lobe *Pariétal*
- scissure *Pariéto-Occipitale* entre le lobe *Pariétal* et le lobe *Occipital*

![[Scissures.png]]

## Organisation fonctionnelle

On sépare le cerveau en:
- *Aires primaires*
	- Aires *primaires sensorielles* (visuelle, au niveau du lobe occipital; somesthésique, à l'avant du lobe pariétal; ...), qui réceptionnent les messages nerveux depuis les systèmes périphériques. 
	- Aire *primaire motrice*, à l'arrière du lobe frontal.
- *Aires associatives*, responsables de fonctions plus haut niveau, comme la mémoire par exemple.

Attention toutes fois, certaines régions étant effectivement plutôt impliquées dans certaines fonctions, il ne faut pas spécifiquement associer région et fonction. La sollicitation des différentes régions du cerveau dépend aussi de la dynamique d'activation.

## Organisation cérébrale

Le cerveau est constitué du cortex (substance grise) au niveau de sa partie extérieure. Les différentes régions du cortex sont reliées par des fibres (matière blanche):
- Fibres d'association: entre différentes zones d'un même hémisphère
- Fibre commissurales: entre les deux hémisphères
- Fibres de projection: entre le cerveau et les structures sous-jacentes

![[couches_fibres.png]]

Le cortex lui-même est constitué de six couches différentes, numérotées de l'extérieur vers l'intérieur:
- Couches 2 et 4: beaucoup de cellules *étoilées*, dont le rôle est de traiter l'*information qui arrivent* depuis les autres zones du cerveau/système nerveux.
- Couches 3 et 5: beaucoup de cellules *pyramidales*, dont le rôle est l'*intégration et la transmission d'information des autres couches*.

### Structure du neurone

![[Structure_neurone.png]]

*Synapse*: Lieu de connexion entre deux neurones.

![[synapse.png]]

**Potentiels locaux**: Variation de potentiel dus à l'entrée d'ions. Ils varient selon le type (positif/négatif) et la quantité d'ions entrants. On parle de *dépolarisation (effet excitateur)* en cas d'entrée d'*ions positifs* et d'*hyperpolarisation (effet inhibiteur)* en cas d'entrée d'*ions négatifs*. Lorsque ces potentiels se trouvent sur le neurone post-synaptique, on par le *potentiels post-synaptique* (*PPS*). Par défaut, le *potentiel de repos* d'un neurone est d'environ *-70mV*.

Les ions positifs entrant vont venir 'pousser' les ions positifs déjà présents (par répulsion de charges) et, de cette manière, créer des courants locaux. Ceux-ci sont naturellement atténués du fait du milieu aqueux dans lequel ils se trouvent.

**Segment initial**: Au niveau de la base de l'axone des neurones se trouve une région particulière: la *zone gâchette*. Lors de la dépolarisation du neurones, elle est responsable de la création de potentiels d'actions (*PA*) en cas d'atteinte du seuil de dépolarisation. Après la création du PA, le neurone retrouve son potentiel de repos (en l'absence de l'entrée d'autres ions) très rapidement (de l'ordre de la ms). (PEPS sur l'image suivante: potentiel excitateur post-synaptique)

![[gachette.png]]


Note: L'EEG et la MEG vont être particulièrement sensibles aux courant locaux (et moins aux potentiels d'action).

Plusieurs activités ont lieu en parallèle de l'activation des neurones, en particulier la consommation d'oxygène, ainsi que d'éléments nutritifs. Ces activités vont provoquer des variations de débit sanguin (variation hémodynamiques, de l'ordre de la s) dans les zones concernées. (CF les autres cours)

## Les techniques d'imagerie

*Résolution temporelle*: Capacité de la technique à discriminer deux signaux dans un temps aussi bref que possible.
*Résolution spatiale*: Capacité de la technique à mesurer une activité dans un volume/une surface la plus petite possible.

![[tech_image.png]]


# Nature, origine et topographie des signaux EEG de surface et MEG

L'activité mesurée en EEG/MEG de surface est la résultante de l'activité cumulée de tous les neurones à proximité de l'endroit où est positionnée l'électrode. On observe alors typiquement une activité oscillatoire, résultante de l'activité d'une population de neurones synchrones.


| Technique | Objet mesuré           | Mesure   | Résolution temporelle | Ordre de grandeur | Capteur                             |
| --------- | ---------------------- | -------- | --------------------- | ----------------- | ----------------------------------- |
| EEG       | Potentiels électriques | Relative | 1ms                   | quelques µV       | Electrodes de surface               |
| MEG       | Champs magnétiques     | Absolue  | 1ms                   | $10^{-13}$ tesla  | Capteurs SQUID couplé à des bobines |
En EEG, on mesure des différences de potentiels électriques, soit par mesure *monopolaire* (électrode VS référence, le plus souvent utilisé en recherche), soit par mesure *bipolaire* (électrode VS électrode, plutôt utilisé en médecine). Dans le cas monopolaire se pose le soucis de la référence, plusieurs méthodes sont possibles:
- Sur le nez, mais gênée par le mouvement des yeux
- Derrière l'oreille (sur les mastoïdes), souvent utilisé
- Sur les lobes d'oreilles (moyenne des deux côtés), potentiellement complexe selon la taille du lobe/la présence de piercings...
- Obtenue par moyenne (seulement possible sur un grand nombre d'électrode (>64)), l'avantage est que les différences obtenues avec cette référence sont bien dues à des activités d'"intérêt".
## Activités oscillatoires

![[rythmes.png]]

### Origine des signaux

Origine des activités oscillatoires:
- Boucles thalamo-corticales: Thalamus, relais sensoriel, ("chef d'orchestre")
- Boucles cortico-corticales: synchronisation de différentes régions du cerveau selon l'activité
- Activité neuronale modulée par les cellules gliales (ép. les astrocytes).. Pas plus de détail donné...

![[sommeSPatiTemp.png]]


Sur un seul neurone, l'entrée d'ions provoque des courants locaux (*courants primaires* sur l'image suivante) et des *courants secondaires* qui sont dus à la présence de *canaux de sorties* d'ion (toujours ouverts):
![[courantPrimaires.png]]

Les champs dipolaires dus au PPS (potentiels post synaptiques) diminuent moins en amplitude avec la distance (contrairement aux champs dus aux PA). Ainsi, l'activité électrique due aux PA ne permet pas la synchronisation neuronale, contrairement à celle des *PPS* qui est *favorable* à la *synchronisation temporelle* d'un *grand nombre* de *neurones*. C'est cette activité qui est *nécessaire à une visualisation en EEG* ou MEG. A noter aussi que les signaux observés en EEG sont principalement générés par les cellules pyramidales (P), à cause de leur architecture plutôt en colonne:
![[pyramidVSetoile.png]]

Note: La synchronisation temporelle est due à la fois aux boucles thalamo-corticales et cortico-corticales (synchronisation des messages nerveux afférents) et à l'activité électrique due aux PPS.

Finalement, l'activation synchronisée de millier de neurone pyramidaux va résulter en la création d'un *macro-dipôle*, dont la *direction* et perpendiculaire à la surface corticale locale et dont l'amplitude correspond à "l'intégrale des densités de courants dans la colonne considéré soit en moyenne":
![[macro_dipole.png]]

### En EEG et en MEG

Selon le positionnement du macro-dipôle sur le gyrus, il peut être radial ou tangentiel, les variations de potentiel résultantes vont être impactées: 
![[Dipoles_rad_tang]]
![[topographie.png]]

Et en MEG, les champs magnétiques étant perpendiculaires aux courants électrique:
![[MEG_EEG.png]]

Le signal électrique, même s'il est issu d'un seul point, va apparaitre de manière "étalée" sur la surface du scalp en EEG. En MEG, les *champs magnétiques* relevés sont moins dispersés, car ils sont beaucoup *moins sensibles aux milieux traversés*, c'est pour ça que la MEG a une meilleure résolution spatiale que l'EEG. Par rapport à la source du signal:
- L'amplitude du signal va diminuer en s'éloignant de la source (aussi si celle-ci est profonde)
- La dispersion du signal va augmenter avec la distance à la source.

### Sensibilité

| Type de source | MEG  | EEG   |                                        |
| -------------- | ---- | ----- | -------------------------------------- |
| Radiale        | 1/10 | 2     | Par rapport à une source tengencielle  |
| Profonde       | 1/3  | 1/100 | Par rapport à une source superficielle |

### Cas des sources multiples
Les observations réalisées en surface sont la résultante de la somme de plusieurs macro-dipôles. Exemple: dans le cas d'une onde auditive perçue, on a de fortes activation sur le dessus du crâne alors que ces zones ne sont pas impliquées dans son traitement.

## Résumé EEG-MEG

| MEG                                                        | EEG                                                  |
| ---------------------------------------------------------- | ---------------------------------------------------- |
| Mesure un champ magnétique                                 | Mesure un potentiel électrique                       |
| Réponse dipolaire perpendiculaire à la direction du dipôle | Réponse dipolaire parallèle à la direction du dipôle |
| Réponse focale                                             | Réponse diffuse                                      |
| Peu affecté par les tissus cérébraux                       | Très affecté par les tissus                          |
| Séléctif pour les sources tangentielles                    | Sensible à toutes orientations                       |
| Peu sensible aux sources profondes                         | Sensible aux sources profondes                       |
| Coûteux                                                    | Moins cher                                           |

# Dispositifs et principe de mesure des signaux

## MEG

Nécessite une chambre blindée (cage de Faraday) pour supprimer toutes les ondes électromagnétiques environnantes (téléphone portable, prises électrique etc...).

La détection est faite par des bobines, le signal est ensuite amplifié par des SQUIDS (supraconducting quantom interference device) qui doivent être refroidis ) l'hélium liquide (d'où le cout de la manipulation):
![[MEG_dispositif.png]]

## EEG

Les électrodes sont positionnées de manière standardisée directement sur la tête, il existe plusieurs types d'électrodes:

| Type d'électrode | Passive                            | *Active*                                            | *Humide*                             | Sèche                                                            |
| ---------------- | ---------------------------------- | --------------------------------------------------- | ------------------------------------ | ---------------------------------------------------------------- |
|                  | Simple réception du signal nerveux | Pré-Amplification du signal directement à la source | Posées sur un gel conducteur         | Sans gel                                                         |
|                  |                                    |                                                     | Long à poser car application du gel; | Présentent souvent des artéfacts de mesure; désagréable à porter |

![[EEG_dispo.png]]

Système international 10-20 (pour <21 voies):
![[10_2.png]]
Positionnement des électrodes par rapport à une répartition du scalp à partir de 4 points de références: *Nasion*, *Inion*, *Préaurical* (Gauche et Droit). La première électrode posée est l'électrode centrale, au niveau du "*vertex*". L'espacement entre les électrodes et de 10 ou 20 % des distances Nasion-Inion.
Ces quatres points sont la référence pour tous les systèmes actuels, mais la répartition est plutôt de 5% actuellement, pour une meilleure résolution spatiale.

### Dispositif de mesure de la position du casque par rapport à la tête

Idéalement, il faudrait un IRM du cerveau du patient. Certaines références ont été créée à partir de moyenne sur 1000 cerveaux sinon. La position précise des électrodes est reconstruite numériquement par rapport aux points de référence (Nasion, Péri-auriculaire Droit et Gauche) et au contour de la peau.

# Protocoles d'étude et traitement des données
## Pré-traitement des données
### Identification & Correction des artéfacts 
([vidéo youtoube]( https://www.youtube.com/watch?v=zH3fim2uIHs)). 
Les principales causes d'artéfacts *physiologiques* sont:
- Mouvement oculaires
- Activité cardiaque
- Activité musculaire
- Activité liée à un état de fatigue (onde Alpha)

Sources *extra-physiologiques*:
- Mouvement transitoires du sujet, mouvement de tête
- Bruits électroniques (50Hz, déplacement de câbles, ...)

L'*Analyse en Composantes Principale* (*PCA*) permet aussi de filtrer les artéfacts (typiquement cardiaque), en particulier si ceux-ci sont très différents (orthogonaux) du signal d'intérêt.


- *Recourt à l'EOG* (Electro-Oculographie):
	- Mesure bipolaire, au moins 4 éléctrodes pour séparer l'EOG verticale (clignement + mouvements oculaires verticaux) et horizontale (mouvement oculaires horizontaux). Idéalement, la composante horizontale ne mesure strictement QUE de l'horizontale et pareil pour la verticale; ce résultat est obtenu en plaçant parfaitement les 4 électrodes (le sens de variation dépend du montage, il n'y a pas de convention): ![[position_electrodes.png]]
- *Recourt à l'ECG* (Electro-Cardiographie): 
	- Mesure bipolaire
	- Rarement nécessaire car le signal émit par le cœur est de forme très typique (simplement fréquence variable). Deux électrodes (+ la masse) suffisent.
- *Recourt à l'EMG* (Electro-myographie):
	- Mesure bipolaire
	- Attention, toute correction liée à l'activité musculaire est un potentiel biais pour la mesure initiale (car l'EMG va elle-même présenter des artéfacts). En cas de mesure à artéfacts, il est souvent préférable de simplement supprimer les mesures concernées.

### Filtrage

![[filtrage_eeg.png]]

*Attention*:
- au filtrage avant les autres traitements, si on se *limite* à certaines *gammes de fréquences* on perd potentiellement beaucoup du signal. 
- Le filtrage *déforme* les artéfacts (et le signal d'intérêt), qui seront potentiellement plus difficile à discriminer par la suite.
- Le filtrage 'sans risque' typique serait : 
	- Retirer $50 Hz$ avec un filtre fente
	- Appliquer un passe bande sur $[0.5; 100] Hz$.

### Correction de la ligne de base

Souvent, on enregistre pour chaque sujet l'activité EEG avant et après la période de tâche, pendant 5 minutes (avant et après). On fait ensuite la moyenne de ces deux périodes afin de la soustraire/diviser/Zscore au reste du signal.
(Z score: différence normalisée)

![[lignedebase.png]]

## Traitement des données

L'analyse des signaux est spécifique du but de l'étude, on peut typiquement distinguer deux types d'analyses:
- *globale* (évolution d'état de vigilance dans différents contextes; évolution d'état émotionnels; ...)
- *locale*, discrimination des processus cérébraux (capacité de discrimination d'un visage; impact d'une condition expérimentale sur un processus de traitement; ...)


> [!NOTE] Examen
> Questions sur les analyses pas plus détaillées que l'image suivante, on est allé trop vite sur la suite du cours pour être interrogé dessus. --> Potentiels et champs évoqué? Pour mesurer quoi? Pareil pour Analyse spectrale; connectivités; analyse de sources.

![[analyses_EEG.png]]

### Potentiels et champs évoqués et induits

![[PE_CE.png]]

*Nomenclature des réponses*:
- Nxxx: onde EEG négative à xxx ms
- Pxxx: onde EEG positive à xxx ms
- Mxxx: champ magnétique à xxx ms
- Positive/négative dans le *sens de variation* (vers le positif/vers le négatif), pas en valeur absolue!

> [!NOTE] Examen
> Pas d'interrogation sur les potentiels évoqués spécifiques (juste savoir ce que c'est/comment ça s'obtient)

### Activité oscillatoire: analyse spectrale


> [!NOTE] Examen
> Pas d'interrogation sur les méthodes d'analyse spectrale

![[spectrale_event.png]]


### Activité oscillatoire: connectivités

Différents types de méthodes existent.

> [!NOTE] Examen
> Pas d'interrogation sur les méthodes d'analyse de connectivité

![[connectivites.png]]

### Localisation des sources du signal

> [!NOTE] Examen
> Pas d'interrogation sur les méthodes de localisation des sources


Le principe est de produire différents modèles et d'essayer de voir lequel est le plus probable.

![[sourcedusignalEEG.png]]