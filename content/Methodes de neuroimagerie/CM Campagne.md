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
- Derrière l'oreille/sur les lobes d'oreilles (moyenne des deux côtés), potentiellement complexe selon la taille du lobe/la présence de piercings...
- Obtenue par moyenne (seulement possible sur un grand nombre d'électrode (>64)), l'avantage est que les différences obtenues avec cette référence sont bien dues à des activités d'"intérêt".
## Activités oscillatoires

![[rythmes.png]]

Origine des activités oscillatoires:
- Boucles thalamo-corticales: Thalamus, relais sensoriel, ("chef d'orchestre")
- Boucles cortico-corticales: synchronisation de différentes régions du cerveau selon l'activité
- Activité neuronale modulée par les cellules gliales (ép. les astrocytes).. Pas plus de détail donné...

![[sommeSPatiTemp.png]]


Sur un seul neurone, l'entrée d'ions provoque des courants locaux (courants primaires sur l'image suivante) et des courants secondaires qui sont dus à la présence de canaux de sorties d'ion (toujours ouverts).

![[courantPrimaires.png]]

Les champs dipolaires dus au PPS (potentiels post synaptiques) diminuent moins en amplitude avec la distance (contrairement aux champs dus aux PA). Ainsi, l'activité électrique due aux PA ne permet pas la synchronisation neuronale, contrairement à celle des *PPS* qui est *favorable* à la *synchronisation temporelle* d'un *grand nombre* de *neurones*. C'est cette activité qui est *nécessaire à une visualisation en EEG* ou MEG. A noter aussi que les signaux observés en EEG sont principalement générés par les cellules pyramidales (P), à cause de leur architecture plutôt en colonne:
![[pyramidVSetoile.png]]

Note: La synchronisation temporelle est due à la fois aux boucles thalamo-corticales et cortico-corticales (synchronisation des messages nerveux afférents) et à l'activité électrique due aux PPS.



