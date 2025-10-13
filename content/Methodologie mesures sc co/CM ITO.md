---
prof: " ITO Takayuki"
date: 2025-10-10
publish: true
---

> [!NOTE] Examen
> Savoir quelle technique utilisée pour étudier quel organe. 
> Savoir quelles sont les limites et spécificités de chaque technique.


# Introduction

**Purpose**:
- *Descriptive*: Know how articulatory organs are moved
- *Functional*: How articulatory organs are controlled

**Challenges**:
- Multiple articulator organs, requiring specific measurement devices
- Most articulator organs are interior
- Measurements should not impair speech movement

Speech production : [[Physiologie de la production de la parole]] [[Consonnes et voyelles]]
Speech production study is usually made in the [[Modèle source-filtre]]

# Mesure des mouvements des articulateurs non visibles

The tongue is as *muscular hydrostat*, by opposition to most other muscles which aim to make bones move.
## Electromagnétométrie

ElectroMagnetic Midsagittal Articulometer (EM(M)A):
![[EMMA_liptongue.png]]

EMA uses *sensor coils* (~3mm) placed on the tongue and other parts of the mouth to measure *their position and movement over time* during speech and swallowing. (Three) *Induction coils around the head* produce an *electromagnetic field* (at different frequencies around 60kHz) that creates, or induces, a current in the sensors in the mouth. Because the *current induced* is inversely proportional to the cube of the distance, a computer is able to analyse the current produced and determine the sensor coil's location in space.
$$ i(t) = \frac{k*\phi(t)}{d^3}$$

Depending on the system used, head movement can be corrected in order to extracted just the tongue and other articulators movement.

Based on the measured current, the position of every sensor coil can be deduced and movement characterisics such as velocity and acceleration can then be computed for each articulatory organ.

> [!NOTE] TODO
> Get pictures from slides!

## Echographie - Ultrasound

Ultrasound pulses are sent and echo at tissues edges are then recorded and studied:
![[Echo_tongue.png]]

Transducer frequency effect (2-4MHz):
- Lower frequency has worth resolution
- Higher frequency has shorter range
Sampling frequency is about 28Hz, every 'impulse' is spaced by $\frac{1}{28}s$.

Results are analysed using:
- Contour Analysis and Visualization Technique (*CAVITE*) (ok...?).
- Speckle Tracking: comparing variations between successive images, alows tracking of specific movements.

This technique is used both in research and orthophonic applications.

This technique is affected by the following *limits*:
- *Bone* cast *shadows*
- Measurement is heavily dependent on *head movement*
	- This can be addressed by compensating for such movements (typically using IREDs LED to track head position)

## Endoscopie & Transillumination

L'endoscopie permet d'observer directement les cordes vocales en temps réelle. Elle consiste en l'insertion d'une caméra (soit directement par la bouche, soit par le nez) équipée de LED directement dans la trachée du patient.
La transillumination consiste à mesurer la lumière (émise par une LED insérée via un câble souple par le nez) qui passe à travers les cordes vocales via un capteur placé sur l'extérieur du cou. Cette méthode ne permet pas de mesurer directement les vibrations des cordes vocales, mais simplement de détecter quand elles sont ouvertes ou non.

![[endoscopie.png]]
## Electroglottographie - EGG

Mesure de l'impédance entre deux points de part et d'autre du cou par l'intermédiaire de deux électrodes:

![[electroglottographie.png]]

Les mesures de variations d'impédance ont la forme suivante:
![[mesureImpedance.png]]

## Electropalatographie - EPG

L'électropalatographie (EPG) est une technique utilisée pour surveiller les contacts entre la langue et le palais dur, en particulier lors de l'articulation et de la parole. Un palais artificiel sur mesure est moulé pour s'adapter au palais dur d'un locuteur. Le palais artificiel contient des électrodes exposées à la surface linguale.

![[EPG.png]]

L'EPG permet de mesurer et de visualiser en direct les dynamiques de prononciation et de coarticulation:
![[EPG_measures.png]]

# Mesures dynamiques
## Capteurs de force

Le capteur est inséré dans la bouche pour mesurer la force appliquée par la langue lors de la parole. Le soucis de ces capteurs est qu'ils gênent la production de la parole. 

En terme de technologie, ils sont basés sur des jauges de contraintes, dont la résistance électrique varie avec la déformation. Ce genre de capteur nécessite une phase de calibration.

On utilise plusieurs jauges de contraintes placées sur le palais, de manière spécifique pour chaque patient:
![[capteurforce_palais.png]]

Les mesures obtenues ont la forme suivante:
![[capteurForce_mesure.png]]

## Electromyographie - EMG

### Principes
L'unité motrice consiste en l'ensemble des fibres motrices innervées par un même motoneurone provenant de la colonne vertébrale, on parle de signaux efférents alpha. Ces signaux efférents s'additionnent et, si le seuil est atteint, provoque la production de potentiels d'action (PA) par le motoneurone. Les PA vont alors être transmis aux fibres motrices et causer la contraction du muscle; plus d'unités motrices sont recrutées, plus la contraction sera forte.
Le fuseau neuromusculaire permet aussi un retour neuronale donnant le niveau d'étirement du muscle (signal afférent).

![[uniteMotrice_principe.png]]

### Méthode
Des électrodes sont placées à la surface des muscles (parfois directement sur les fibres musculaires, avec une aiguille):
![[nappe_electrode.png]]
Avec l'EMG de surface, on mesure souvent l'activité de muscles voisins, en particulier selon la taille des électrodes et la taille/proximité des muscles ciblés.


# Exemples de paradigmes expérimentaux

## Tongue perturbation experiment
Le principe est de perturber la langue pour comprendre quels mécanismes de contrôle sont à l'œuvre dans la production de la parole. Ici, la langue est légèrement tirée vers l'extérieur par un robot. Des mesures EMG sont réalisée sur la partie basse et inférieure de la langue.
![[tonguePerturbExpe.png]]

On observe que lorsque la langue est tirée, les patients ont le réflexe de la ramener vers sa position initiale afin de continuer de produire de la parole (Ito, Bouguerra, Bourhis, Perrier, Scientific Reports, 2024,):
![[mesures_reponse_perturb_langue.png]]
![[EMG_speech_nSpeech_rest_volun.png]]
Lorsque le sujet ne doit pas produire de parole, on observe pas/très peu d'activation réflexe. La conclusion de ces observations est que le reflexe n'est activé que pendant la production de la parole.