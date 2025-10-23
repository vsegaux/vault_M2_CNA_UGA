---
prof: BERTOLOTTI Marcella
date: 2025-10-22
publish: true
---
# iEEG
Méthode invasive, utilisée uniquement dans le cadre clinique, principalement sur des sujets épileptiques pharmaco résistants. L'iEEG permet de faire le dernier bilan pré-chirurgicale dans les cas de chirurgie d'ablation des foyer épilleptogènes dans le cerveau. Cette pratique fonctionne très bien pour les patients épileptiques. Les chercheurs "profitent" de tels patients pour travailler sur leurs signaux. L'implentation des éléctrodes est toujours faite uniquement en fonction des besoins cliniques du patient, et non ceux de la recherche.

Deux méthodes d'implantation:
- ECoG: electrode implantées directement sur le cerveau après une craniotomie. 
- SEEG: Stereo-EEG, les éléctrodes sont plantées directement dans la tête. Cette technique permet d'aller en profondeur dans le cerveau.
	- ![[SEEG_recap.png]]
	- L'objectif principal (clinique) est de repérer le foyer épileptogène, on attend pour cela une crise spontanée du patient, une fois les électrodes implantées afin d'en déterminer l'origine et les patterns de propagation.
	- L'objectif secondaire est de déterminer la balance "bénéfice/risque" d'une potentielle ablation de la région concernée, selon son importance dans la vie du patient.
		- Afin de mapper les fonctions corticales, il est possible de stimuler le cerveau du patient avec les electrodes pendant la réalisation de certaines taches (*Direct Electrical Stimulation DES*).
			- Selon la localisation de la stimulation et la tâche du patient, la stimulation peut être activatrice ou inhibitrice.
				- Importance majeur que le patient puisse raconter ses ressentis. Ex: stimulation dans une région impliquée dans la lecture (causant une inhibition de la lecture), le patient raconte être capable de voir les lettre sans pouvoir former des mots pour les lire.
				- ![[DES_funtionalmappinng.png]]
				- **Limitation de la DES**:
					- Similar functional disruption in different cortical region (pas très fin)
					- Time-consuming method, may occasionally lead to seizures (Lesser et al., 1984) and therefore restrict repetition (reduces intra-subject reproducibility) 
					- Does not always trigger objective clinical signs, especially in associative cortices supporting high level cognitive functions such as language areas (dependent also of the patient abilities to explains symptoms) 
					- Elicited signs can be subtle, especially in the language domain (e.g., a specific lexico-semantic deficit) and therefore difficult to detect or interpret symptoms 
					- Limited spatial sampling (cognitive functions are supported by large brain networks)
			- Mais la SEEG permet d'avoir une très bonne résolution spatiale (en plus de la résolution temporelle déjà caractéristique de l'EEG).

Rappel:
Le potentiel de champ local (LFP) correspon au courant extracellulaire qui reflète la sommation linéaire de potentiels post-synaptique d'un groupe de cellules proches. On peut considérer que l'activité enregistrée est le reflet (le plus pure en neuroimagerie) de l'activité neuronale, en particulier dans les haute fréquences (High Frequency Activity, HFA): 40 à 150Hz, qui correspond à une activité induite, souvent filtrée par les moyennages habituellement effectué en EEG standard. D'où l'interêt de la iEEG.

Distinction induced VS evoced gamma (high freq): des analyses en temps/fréquences permettent de mettre en évidence les gamma induits. (à mieux expliquer):
![[Evoc_invoc.png]]

Plusieurs méthodes pour estimer les HFA:
- Wavelet analysis: Représentation temps-fréquence (2-200Hz):  is to convolve the signal to be analyzed with several oscillatory filter kernels representing different frequency bands (…) ≫ -Bruns, J. of NM. 2004 => carte temps-frequence.
- Hilbert Transform: Band-limited amplitude envelope (20-60Hz): by decomposing the signal into neighboring frequency components (i.e. bandpass signals) and by computing the so-called analytic signal of each component via the Hilbert transform ≫ Bruns, J. of NM. 2004


# Résultats des HFA
## Exquisitely stimulus- and task-sensitive

A permis la mise en évidence l'implication spécifique de certaines régions du cerveau pour certaines taches:
- la 'Visual word form area' (VWFA), activité Gamma particulière et sélective pour les mots et pseudo-mots: 
![[mot_psuedo_mot.png]]

- de la même manière, réponse sélectives aux visages dans la 'Fusiform face Area' (FFA).

La selectivité de certain petits groupe de neurone à certaine stimulation est mise en évidence par le contraste entre les réponses mesurée sur des éléctrodes voisines dans le cerveau. On remarque, sur la figure suivante, des différences de réponses sur des électrodes espacées de 5mm seulement (ligne '2' et '3'):
![[selectivite_5mm.png]]


## Timing reveals function
En bleu sur la figure suivante, l'apparition du stimuli, et en jaune, la réponse du sujet:
- en A, on remarque une activation très rapide directement après le stimuli, on peut donc supposer qu'il s'agit d'une activité purement visuelle (primaire), dans le Gyrus Fusiform
- en B, on remarque une activitée concentrée autour de la réponse du sujet (Motor cortex), qu'on peut inférer comme motrice, pour que le sujet réponde effectivement
- en C et D, dans les régions respective FEF et DLPFC, on remarque une activité quasi continue sur l'intégralité du temps entre la stimulation et la réponse; on infère donc que ces deux régions sont impliquée directement dans la tâche (prise de décision sur une recherche de 'T' parmis les 'L' ici)
![[timing_function.png]]
## HFA reveal neural activity suppression in DMN

On donne de la signification à de la desactivation cérébrale (similaire à activation, mais simplement désactivation?) à expliquer mieux...

## Opens windows to functional connectivity and plasticity
Les patients apprennent à prononcer des sylabes à partir d'icones présentés (pendant 5-10min). Puis test en demendant aux patients de lire dans leur tête.

On compare l'activité pour les icones connus (sylabes nativs, appris et non apris. On remarque que
- dans certaines régions (plutot visuelles), pas de différence entre avant et après apprentisage dans l'activité
- différence avant/après apprentissage pour ceux qui ont été appris. En particulier l'activation des régions continu plus longtemps que pour ceux qui sont simplement déjà connus
	- Lorsqu'on lit, on met en relation la vision et le langage
	- on observe que la corrélation entre ces deux régions n'est présente que dans les cas où les icones sont connus/appris.
	- Pour les icones apprisent, les deux régions ont besoin de communiquer plus longtemps pour traiter l'information, d'ou la prolongation de l'activité au moment de la lecture.
	- Pour les icones déjà connu, le système est beaucoup plus efficace et l'activité générée est donc plus courte
- pas de différences pour ceux non-appris (pas appris donc pas de communication entre aire visuel et langage)


D'autres études ont aussi mis en évidence certaines régions de la perception auditive qui répondent spécifiquement à la parole humaine (indépendamment de la langue parlée). 
Attention-Ignorance:
- Lors de la lecture (dans sa tete) avec attention:
	- Activité de l'aire visuelle
	- Suivie de l'activité du cortex auditif primaire (inatendu)
		- -> Le cerveau "écoute" notre 'parole' même dans la lecture
	- Puis de l'activité d'aires auditives associatives
- Lors de la "lecture" qui doit être ignorée:
	- Simple légère activation de l'aire visuelle
![[auditif_visuel_lecture.png]]



## HFA in real time
Les patients doivent jouer à trouver les différences, on enregistre leur mouvement oculaires (qu'on voit donc se déplacer sur les deux images) et ils doivent regarder en haut à gauche à chaque fois qu'ils trouvaient une différence. On observe en parallèle avec l'iEEG l'activité de la Visual Word Form Area.

Une autre experience a permis de mettre en évidence une zone très spécifique qui ne s'active que dans le cas de la parole intérieure ET qui plus est, de manière proportionnelle à l'intensité de la voix intérieur.

## Desavantage de la HFA
On ne travaille que sur des patients, donc des cerveaux pathologiques et les résultats sont difficiles à généraliser à la population.
On essaye de faire les recherches en dehors des zones épileptogène et donc dans des régions théoriquement saine, mais la généralisation reste limitée.

## Avantages de la HFA pour le mapping fonctionnel du cerveau

- Spatial and temporal precision 
- Induce HFA responses 
- Selective neural Response 
- De-activation 
- Pre-operative and pre-stimulation guide (Localizer task) 
- Real-time functional mapping (BTV) 
- Exploration of subtle cognitive symptoms 
- Exploration of the « deep » cognition and “covert” behaviors (inner speech, mind wandering, mental imagery…) 
- Can reduce the DES functional mapping time.



> [!NOTE] Examen
> Dans quel contexte on utilise ce type d'outil. 
> Savoir lire les cartes/graphiques pour pouvoir être critique en lisant des papiers.
> Connaitre les limites de généralisations.


