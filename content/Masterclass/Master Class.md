---
prof:
date: 2025-11-19
publish: true
---
 
> [!NOTE] Examen
> Basé sur la lecture d'un article, comprendre les manières d'utiliser les techniques présentées, à quoi elles servent et quelles sont leur limites?


# Principe général
On s'interesse au rôle d'une zone cérébrale précise. On la stimule pendant une tâche et on mesure les performances avec ou sans stimulation.
La perturbation ne reste jamais locale, mais se répend dans le réseau neuronale.

## Techniques de stimulation
### Invasives
- Stimulation electrique direct (DES), avec des sondes, intracranienne
- iEEG, implantation d'électrodes profonde dans le cerveau, reliée à l'extérieur
- DBS, deep brain stimulation, implantation profonde dans le cerveau, "semi permanante"

### Non invasive
- TMS, transcranial magnetique stimulation
- TODO

## Développement historique
OK SLIDE


# Principe biophysique
## tES
Application d'un champ electrique

## TMS
Application d'un champ magnétique, beaucoup plus localisé que le champ électrique de la tES. Le champ appliqué est très bref, on parle de *pulse* à 1 ou 2 Tesla pendant 200-300 $\micro s$.

Le champ électrique induit est dépendant des différentes couches physiologiques qui sont présentent. Un IRM est nécessaire pour chaque individu afin de pouvoir modéliser le champ électrique réellement induit, selon les surfaces traversées. 

### Design experimental
#### Online
On induit une perturbation cibéler et on en musre les interactions sur les comportement/sur l'activité neurophysio en cours pendant une tâche cognitive. On mesure alors les différences avec/sans stimulation sur l'indicateur de performance (TR, ...)

#### Offline
On induit de la plasticité fonctionnelle (neuromodulation) et on en mesure les conséquences sur le comportement/sur l'activité neurophisio à moyen et long terme. On demande au participant de réaliser une tache, on mesure ses performances. Puis on applique la neuromodulation (sans tâche), et finalement on lui demande de refaire la tâche par la suite (sans stimuler). On compare les performances avant et après.


### Paramètres du protocole
On s'interesse à:
- Où? Quelle aire participe au réseau fonctionnel responsable de l'execution d'une tâche. On compare avec un CTRL
	- Peut aussi être prédéterminer avant la tâche, par IRMf etc..
- Quand? Quel est le timing supposé de l'implication de l'aire stimulée par rapport à une tâche cognitive? On contrôle avec plusieurs latence différentes. Protocoles online uniquement
	- Peut aussi être prédeterminer avant, typiquement par EEG
- Comment? Choix du type de stimulation: simple ou double impulsion, rTMS, cTBS, tDCS, tACS, .. On peut aussi faire varier la puissance de stimulation. Ici encore, on controle avec des cas placebo et autre...

# TMS
## Neurophysiologie
Activation d'un neurone, PA si on dépasse le seuil au niveau du P membranaire... OK cool.
La TMS induit donc assez de courant pour générer la production de PA.

En tES, on fait varier le potentiel de repos, ce qui va faciliter ou inhiber la génération de PA selon le sens de variation.


## Approches online
Plusieurs type de protocoles possibles: single pulse, paired pulse, burst (à une certaine fréquence). Ces impulsions sont séparées de plusieurs secondes avant d'être reproduites.

### Exemple: Protocole single pulse
Stimulation du cortex moteur primaire au niveau de la zone activatrice de la main. On peut alors observer un potentiel évoqué moteur (PEM) au niveau des muscles effecteurs de la main. On observe un seuil moteur (Resting motor threshold rMT), nécessaire à la production de PA au niveau du neurone moteur; la valeur de ce seuil dépend de l'excitabilité corticale du patient (selon état cérébrale, neuroanatomie, neurochimie, pathologies,...).

La puissance de stimulation est donc paramétrée selon les patients, les mesures sont données en % de seuil moteur (%rMT).

## Approches offline
On applique typiquement plusieurs stimulations consécutives, et on observe l'effet à posteriori.

Selon la fréquence de stimulation, l'effet sera plutot inhibiteur (basse fréquence, 1Hz) ou facilitateur (>5Hz).

En clinique, on multiplie les séances de rTMS plusieurs fois par jour afin d'obtenir un effet cumulatif au fil des jours, le but étant de moduler à long terme le fonctionnement d'une aire/d'un réseau. 

Effet anti-dépresseur reconnu/testé; effet analgésique aussi; réduction des TOCs aussi.


## Exemples d'application
### TMS single pulse pour la lecture des symboles du Braille
On observe lors de la lecture d'une symbole Braille à l'IRMf une activation du cortex sensori-moteur chez les patients voyant et du cortex visuel principal chez les patients aveugles.

Tâches: applicquer la main à la surface en bois. Le but du patient est soit de percevoir les points (oui/non), soit de lire les points. On stimule en single pulse soit le cortex visuel primaire, soit sur le cortex sensori-moteur avec des délais de 0 a 110ms (+10ms).
Résultats:
- Chute des performances en stimulant le cortex sensori moteur à 30ms à la fois pour la lecture et la perception des symboles.
- En stimulation du cortex visuel: peu de perturbation de la perception, mais baisse significative e la performance de lecture lors de stimulations à +70ms.
- Validation causale du role du cortex visuel dans la lecture du braille.


### Trains d'impulsion appliqué à l'encodage de la mémoire verbale
But: déterminer le lien causale entre oscillation bêta et performances mnésiques.
Lors de la stimulation en burst, on observe une synchronisation locale de l'activité neuronale avec la fréquence de stimulation.

Les mesures ont été faite par couplage TMS-EEG. Des stimulations controle avec des fréquences theta et alpha pour vérifier l'impact spécifique des ondes bêta.

Protocole:
Fixation d'une crois, affichage d'un mot cible, puis application du pulse. Le patient doit ensuite exprimer le mot lu. Finalement on demande au patient de rappeler le mot à plus long terme.

Résultats:
Pas de perturbation de l'encodage: lecture OK et capacité de manipuler le concept directement après.
Mais baisse de performance de mémoire à long terme dans le cas de stimulation avec burst bêta.
*Par EEG, on observe un écho de la stimulation beta (et pas dest autres stimulations) => Spécificité de certaines régions à certains rythmes d'onde.*

### Protocole offline, application au cortex visuel
Objectif:
Tester la neuromodulation permettant d'augmenter la plasticité synaptique entre V1 et V5, selon les deux voies (top-down ou bottom-up).
Méthode:
RTMS à deux bobines, on stimule 2 zones différentes pour forcer une plasticité directionnelle (par stimulation délayée de 20ms des deux zones) V1->V5 (bottom up) ou V5->V1 (top-down).

V1 et V5 ont été déterminée par IRMf au préalable pour chaque patient.


Résultats:
Pas d'influence de la stimulation bottom-up.
La stimulation de la voie top-down améliore les performances à la taches (discrimination spatiale).


# tES (tDCS, tACS, tRNS)

## Neurophysiologie
### tDCS
Application d'un Courant continue, 1 à 4 mA

Trois types de stimulations possibles:
- Conventionnelle: un anode, une cathode, courant très faible, diffus dans le crane
- Haute définition individuelle
- Haute définition: 3,4,5,6,7cm, électrodes rapprochées, stimulation selective.

La stimulation peut etre anodale ou cathodale (+ ou -), pour avoir un effet respectivement excitateur ou inhibiteur.

#### Applications courantes
- en clinique, car relativement facile à mettre en place. Dans une étude récente, réduction des symptomes dépressifs pour les patients ayant reçu la tDCS; à noter que l'effet placebo est aussi important (même similaire) pour les patients ne l'ayant pas réellement reçu.
-  

#### Conclusion
Technique prometteuse, portable, peu couteuse, relativement facile d'utilisation, grande variété d'application
Modifie le potentiel de repos et peut induire des effets à long terme sur la plasticité neuronale
Présente des risques minimes, a été approuvé dans plusieurs pays pour le traitement du trouble dépressif majeur.


### tACS
Courant alternatif avec une fréquence spécifique.
Plusieurs montages possibles:
- conventionnel, pour viser une zone particuliere
- par paire, pour stimuler deux zones à la fois

Le but ici est de syncrhoniser l'activité ryhtmique des neurones en imposant des oscillations. Avec le montage par paire, on peut jouer sur le déphasage ou la réinitialisation de phase entre deux régions cérébrales qui interagissent.

Application: 
- amélioration des capacités de rotation mentale par exemple.
- pour la maladie de parkinson: stimulation anti-phase pour la réduction du tremblement (mais plus contraignant à mettre en place au quotidien que la stimulation profonde)
- amélioration symptomatique dans la depression aussi
- récupération partielle de la vision pour les patients présentant des hemianopsies suite à AVC
### tRNS
Courant alternatif avec des fréquences aléatoires.
Equivalent à l'ajout d'un bruit neuronal.

- faible niveau de bruit ➔ trop faible pour provoquer une réponse précise. 
- niveau de bruit optimal, la réponse de sortie correspond au timing exact des stimuli d'entrée. 
- bruit excessif ajouté aux stimuli entraîne de fausses alarmes dans la réponse de sortie.
*La précision de détection de l'activation cellulaire en fonction du stimulus est améliorée lorsque le niveau de bruit est optimal.*

![[tRNS_bruit_threshold.png]]

Application: Boost de la perception visuelle pour des stimuli qui sont normalement légèrement sous le seuil d'activation.


## Limitations
- variabilité inter sujet importantes
- effet variables selon l'aire stimulée
- limité à la surface du cortex
- L’espace des paramètres est grand, peu de recul sur les effets réels de ceux-ci (rTMS: nombre d’impulsions, puissance, frequence, motifs etc, tES: frequence, intensité, durée, état du sujet etc…)



# Cours 2: Futurs développements et applications des NIBS basées sur l'électromagnétisme
(Non Invasive Brain Stimulation)
## Rappels et limites des NIBS conventionnelles
La stimulation corticale se base sur l'application d'un champ électrique à la surface du cortex, soit par tES (champ electrique), soit pas TMS (impulsions magnétiques). (CF cours 1)

Le principe général est le suivante:
- application de la stimulation
- induction d'une activité neuronale de la région ciblée
	- et de région voisines, qui vont mener à la coactivation de tout un réseau.
	- la perception de la stimulation (auditive en TMS, sensorielle de manière générale) va aussi donner lieu à des modifications de comportement, d'où l'interet de bien contrôler avec des essais placebo.
- modification du comportement
- Expérimentalement:
	- ONLINE: on compare la tâche avec ou sans stimulation
	- OFFLINE: on compare la tache avant et après la stimulation.
- Limites:
	- Neuromodulation: entraine des phénomène de plasticité par modulation de la balance excitation/inhibition et/ou de la connectivité. ![[neuromodulation_consequences.png]]
	- Mais cette modulation est très variable:
		- Répondeurs VS non Répondeurs (variabilité inter-sujet)
		- Sens de l'effet
		- Variabilité de l'effet selon la zone stimulée
		- Variabilité intra-sujet:
			- selon le rythme circadien
			- selon l'historique de l'activation synaptique
			- selon la génétique
			- âge (même si facile à contrôler)
## Couplage avec la neuroimagerie fonctionnelle
Pourquoi le couplage? 
- Mieux comprendre les mécanismes d'action 
- Trouver des marqueurs physiopathologiques (sans effet observable) 
- Observer les modulations des activités fonctionnelles soutenant un processus cognitif 
- Personnaliser le site de stimulation 
- Prendre en compte l’état cérébral en temps réel pour adapter la stimulation (closed-loop)
### Principe
Comment?
- **Matériel**:
	- Couplage tES - fMRI/EEG
	- TMS - EEG
	- TMS - fMRI, compliqué à mettre en place
- **Méthode**:
	- Problématique des artéfacts liés à la stimulation, plusieurs solutions pour contrer ce problème en IRM:
		- Insérer les stimulations entre les acquisitions de coupes de l'IRM
		- Effectuer un jeu complet d'acquisition IRM, puis stimuler, et refaire l'acquisition IRM
	- Le soucis est similaire en EEG, pour arriver à extraire les ERP (potentiels évoqué), des analyses en composantes indépendantes sont nécessaires. Grâce à ces analyses, les artéfacts liées à la stimulation peuvent être retirées.
- **Design expérimental**:
	- On applique la neuroimagerie pendant (ONLINE) ou avant et après (OFFLINE), comme pour les protocoles standards de TMS. Idéalement, on souhaite trouver des corrélations entre l'activité cérébrale et les comportements observés.
### Application
#### Mieux comprendre les mécanismes d'action de la TMS
Le pulse TMS provoque la dépolarisation de certains neurones, on s'interesse à la dynamique évoquée par le pulse: 
![[application_Tms_evoquee.png]]
On remarque que la stimulation a un impacte pendant 300-500ms, et plus le temps passe, plus la perturbation se propage dans le cerveau, toujours de manière variable selon la cytoarchitecture des zones traversées.

Selon le nœud stimulé, la propagation est très variable. Le cerveau comporte des clusters spécialisés dans certaines tâches; connectés par des "hubs" d'interconnexion. En cas de stimulation d'un de ces 'hubs', la propagation est très grande. 

#### Personnalisation des stimulations
L'objectif est de sortir du «one-size-fits-all» pour aller vers des traitements personnalisés, adaptés au patient. Par défaut, une grande variabilité anatomique ET fonctionnelle est observée entre les différents individus.
- Exemple : dépression sévère, cure de rTMS sur le DLPFC gauche
![[personnalisation_stimulation.png]]

#### Physiopathologie
Exploring brain dynamics to assess excitability, excitation/inhibition balance, connectivity.
Typiquement sur les patients parkinsonnien, pas stimulation profonde, on arrive à diminuer les tremblement et symptômes moteurs (difficulté d'initiation de mouvement). Par couplage Stimulation et EEG, on peut mesurer l'activation de certaines zones en fonction de l'activation ou non d'autres zones (typiquement des zones qui inhibent le système moteur).

Même genre d'exemple pour des patients d'AVC, on observe l'activité du cortex moteur impacté et la compare par rapport à une activité standard. On peut alors utiliser la stimulation pour désinhiber (réveiller) ces zones.
#### Perception du mouvement
- **Contexte** : Comprendre comment des perturbations focales provoquent une réorganisation du réseau cérébral 
	- mécanismes neuronaux soustendant la perception 
	- réhabilitation 
![[perception_mvmt_couplage.png]]
- Burst de TMS online, au moment du traitement visuel précoce ou tardif 
- Couplage IRMf pour observer la perturbation au niveau des réseaux
	- L'experience montre une diminution des performances lors de la stimulation précode ET tardive.




## Stimulation en boucle fermée
### Principe

![[close_loop_principe.png]]
On mesure en temps réel en EEG, on analyse le signal pour gérer la stimulation en conséquence, on atteint alors des états d'activations cérébraux que l'on mesure par EEG, et ainsi de suite pour converger vers la stimulation/l'activité souhaitée.

### Applications
#### Cartographie motrice TMS-EMG
![[TMS_EMG_carto.png]]
On peut réaliser des cartographies motrices grâce à l'EMG et la stimulation du cortex moteur primaire. On découvre que certaines zones vont déclencher une cascade d'activation qui code pour certains mouvement (plutot que strictement pour un muscle spécifique systématiquement).

Par exemple, on peut mesurer l'amplitude pic à pic, et grâce à un modèle bayesien, on prédit la position idéale de la stimulation sur le 'hotspot' correspondant au muscle/mouvement d'interet:
![[bayesian_hotspot_spotting.png]]

#### Excitabilité corticale phase-dependant
Etat cérébrale = 'phase' du signal
L'objectif est de délivrer la stimulation selon certaines phases des oscillations cérébrales:
![[phase_dep_cl.png]]
Typiquement dans des moments de pics ou de creux du signal EEG, correspondant à différent états d'excitabilité/d'activité neuronale: les taux de décharge des neurones évoluent dans le temps et produisent des pics/creux dans les ondes mesurées. 
- Par exemple avec les ondes alpha, les pics correspondent à des phase d'excitabilité basse (faible taux de décharge) et les creux à des phases d'excitabilité haute.

#### Plasticité rTMS phase-dependent
Travail sur les ondes $\theta$ préfrontale et la plasticité indutie par rTMS, neuromodulation des processus liés à la mémoire de travail (OFFLINE). La neuromodulation est significative pour les creux du signal (comparaison avec les pics et une condition sans spécification de phase).

#### Sommeil et tACS adaptative
tACS (stimulation par courant alternatif sur le scalp).
- Contexte : thérapie pour traiter les insomnies, le but est de favoriser l'apparition de certaines ondes pour maintenir le patient dans un sommeil aussi profond que possible.
- tACS « classique » vs. tACS adaptative selon les différents stades du sommeil 
- tACS adaptée en boucle fermée pour définir : site & fréquence de stimulation

- Les résultats ont montré une latence diminuée pour atteindre le stade profond et une meilleure stabilité du sommeil profond. D'autant plus avec l'adaptation en boucle fermée.

## Vers une stimulation en boucle fermée de la perception multistable

Multistable-> Same sensory input, but perception is changing over multiple stable perceptions (shapes on a picture, movement directions...)
Such stimuli require activity of multiple areas:
- *decision-making* and integrating prior knowledge (frontal)
- perceptual selection and *attention* (parietal)
- motion sensitive neurons and correlation with *dominant percept* (occipital)

The aims of the study are:
- conduct an open-loop TMS-EEG study to: 
	- Identify the network of regions that are causally involved in perceptual switches. 
	- Identify the behavioral and neurophysiological signatures of the switch. 
- developing a real-time TMS-EEG cleaning pipeline for carrying out the closed-loop brain-state-dependent experiment.

### Method
- Aquire stimulation target location for each patient individually
- Intensity calculation, also individually
- Task training for the patient
- First stimulation block
	- For each trial, the participant reports their perceived stimulation in real time, while their brain signals are being recorded.
- Break
- ...
- Fifth stimulation block

### Result
- Behavioural:
	- Stimulation shortens the percept duration.
- EEG signals
	- No correlation on sensor level
	- Correlation on source level (V5 and FEF (FEF..?))
		- Connectivity
	- State-dependency results:
		- Brain response to TMS When it was delivered during a stable period (offSwitch) and when it was close to the transition period (onSwitch) were separated 
		- The brain response to TMS in IPS is different when it is delivered in stable periods compared to transition periods 
		- Decrease of excitability in IPS might be an indicator of a switch 
		- This indicator can inform closed-loop state-dependent stimulation


# Cours 3: Deep Brain stimulation
## Deep TMS

La bobine classique utilisée pour la TMS ne permet pas de stimuler en profondeur (même pas au delà de des gyrus), en particulier pas pour stimuler des surfaces qui ne sont pas parallèles à la surface du crâne.
Il existe d'autres types de bobines (H1-Coil, H7, H4 aussi), qui permettent de stimuler plus en profondeur mais de manière beaucoup moins focale ($17cm^3$ vs $3cm^3$ pour la bobine classique.)
Une autre manière de faire est de combiner deux champs magnétiques (TI-TMS) pour creer un pattern d'interférences afin de stimuler jusqu'à 5cm de profondeur.

Au final cette technique est mieux que la TMS standard mais ne permet toujours pas d'aller profondement dans le cerveau.


## Transcranial Temporal Interference Stimulation (tTIS)
### Principes
Stimulation via deux bobines qui génère chacune un champ haute fréquence >2000, de part et d'autre du crâne.
Hypothèses:
- Les courants rapides qui traversent les tissus n'active pas les neurones
- La région où les deux courants se superposent voit apparaitre une oscillation lente efficace pour stimuler les neurones -> Enveloppe basse fréquence à $\Delta$f. On peut donc choisir ce $\Delta$ pour stimuler une certaine gamme de fréquence.
- la simulation devient donc focalisée en profondeur

### Neurophysiologie
Ces hypothèses ont été prouvées (chez le rongeur d'abord, puis chez l'Homme):
- Excitabilité similaires par stimulation par interférence à $\Delta$f =10 Hz que par stimulation électrique par courant alternatif à 10Hz.
- Pas d'excitabilité déclenchée par le champ à 2000kHz seul.

### Exemples d'applications
- Neuroplasticité
	- Pattern de stimulation par burst espacés de 10secondes dans le striatum
	- Différence entre contrôle et tTIS dans une tâche d'apprentissage de séquences
		- Effet bénéfique sur l'apprentissage et augmentation de l'activité neuronale dans le striatum (IRMf), plus particulièrement sur le Putamen.
- Modifier l'activité oscillatoire
	- Montre un effet sur l'encodage d'item lors d'une tâche et d'autres effets à plus long terme, potentiellement avec application pour des maladies comme alzheimer (mais pas plus de détail donné...)
- Interférer avec un processus neuronal/cognitif en cours
	- traitement de la récompense sensible au high gamma (80Hz)
	- tâche de force manuelle: appliquer une pression pour suivre une cible mouvante
	- selon les condition:
		- renforcement positif/négatif visuel selon la distance à la cible
		- pas d'information sur la distance à la cible
	- La stimulation a 80Hz permet d'éliminer l'interet du renforcement (qui est d'habitude bénéfique pour les sujets).
	- Activation du striatum en corrélation avec ces effets.

*Deep tTIS - Conclusion*
- Cette technique étend l'utilisation de la stimulation cérébrale non invasive aux structures cérébrales profondes (hippocampe, ganglions de la base, etc…). 
- Premières applications chez des patients (TBI, Ploumitsakou et al. en préparation ; Parkinson, Liu et al. 2024 ; Zhang et al. 2024). 
- Les prochaines étapes nécessitent un développement technologique supplémentaire et l'acquisition de preuves cliniques solides et une transposition dans la pratique clinique quotidienne

## Transcranial ultrasound stimulation (TUS)
### Principes
Stimulation par ultrason, focalisation de l'ordre du milimètre, à plusieurs centimètre de profondeur.
Attention, deux techniques à ultrason:
- High intensity focused ultrasound -> Bruler les tissus, typiquement pour les tremblements dans le syndrome de 'holmes' (..?)
- Low intensity focused ultrasound -> Utilisé pour la neuromodulation

Les ultrasons provoquent des variations de pression, les stimulations sont typiquement réalisée par trains d'impulsion, plusieurs mesures:
- intensité spatiale; intensité maximale sur le point focale
- intensité temporelle; liée à l'intensité spatiale par un facteur (proportionnelle donc)

Défis physique:
- le son peut etre diffusé, réfracté, réfléchis lors de sa transmission dans la boite cranienne
	- Impact sur la focalité et la précision de la stimulation
### Neurophysiologie
Deux mécanismes plausibles:
- Thermique: échauffement des tissus et provocation de neuromodulation (mais plutôt évité car peu sûr en terme de sécurité)
- Mécanique: 
	- Par déplacement des tissus -> Objectif de la manipulation; il y a des mécanocepteur dans les neurones qui vont réagir à la déformation/pression et qui sont donc impliqué dans leur activation
	- Par cavitation: bulles d'air soumises à des ondes mécaniques grossissent et s'effondre sur elle meme, provoquant potentiellement des lesions -> Cette conséquence est plutot évitée (par surveillance de l'index mécanique) pour ne pas riquer de lésion

### Exemples d'applications
- Comprendre comment la voie indirecte Prefrontal-Striatal contribue à l’action de stopper une réponse inappropriée:
	- Le protocol de TUS employé réduit l’activité corticale du cortex moteur primaire pour au moins 60 minutes (réduction de 30% des potentiels moteurs évoqués)
	- Le protocol de TUS employé réduit l’inhibition de réponse dans la tâche du Stop-Trial Effet Offline (stop trial: signal pour arreter d'appuyer sur un bouton, mesure du temps de réaction)
- 1) Quel est le mécanisme par lequel la modulation du TUS se traduit en neuromodulation excitatrice ou inhibitrice dans le cerveau humain ? 2) Quels sont les effets de cette neuromodulation sur la connectivité à grande échelle du cerveau humain ?

## Limites et perspectives
- Stimulation à l’aveugle? Application des principles de stimulation en boucle fermée aux NI-DBS? 
- Facteurs confondants (difficulté de masquage des sensation, du bruits?) rendant difficile les études en double-aveugle? (effet placebo etc..)
- Importance de la modélisation du champ électrique (DeepTMS, tTIS) et du champ de pression (TUS) pour des aspects de sécurité et de ciblage 
- Problème de ciblage, nécessité d’une précision accrue pour des structures profondes de petites tailles, sans possibilité de monitoring en ligne de la précision du ciblage