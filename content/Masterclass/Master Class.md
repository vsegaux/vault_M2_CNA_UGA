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
- 