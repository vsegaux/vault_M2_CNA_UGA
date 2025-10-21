---
prof: COUSIN Emilie
date: 2025-10-09
publish: true
---
 IRM:
 - But *clinique*: jamais de diagnostique directement depuis l'imagerie; IRM pour compléter une démarche diagnostique
	 - Outil d'investigation pré chirurgical
	 - Epilepsie: Pour les patients résistants aux médicaments, la seule solution est de déconnecter la zone épileptogène pour éviter sa propagation.
 - But *recherche*:
	 - Représentation des fonctions cérébrales (par interprétation des activations)

Carte *cytoarchitectoniques* de Brodmann: Région du cerveau classées selon leur 'architecture' cellulaire.


> [!NOTE] Examen
> Très peu de questions sur la physique/principe de fonctionnement des machines -> Connaitre les principes généraux, pas besoin de détails.
> => Beaucoup plus important de comprendre et d'interpréter les images obtenues
> *Examen*: Manipulation à interpréter + critiquer.

# Tomodensitométrie et TEP
## Tomodensitométrie
Méthode anatomique, basée sur l'absorption des rayons X (scanner CT scan).
Principe général:
- Rayon X (1 à 4mm de large) généré par un tube qui tourne autour de la région à étudier.
- De l'autre coté du tube se trouvent des détecteurs qui mesure le faisceau n'ayant pas été absorbé, on déduit la structure anatomique selon l'absorption.
- La rotation permet de discriminer les différents couches de la région à étudier.
- Plus une zone est dense, plus elle est blanche sur l'image produite.


| Pros       | Cons                       |
| ---------- | -------------------------- |
| Peu chère  | Mauvais ratio signal/bruit |
| Disponible | Rayons X                   |

## Tomographie par Émission de Positon (TEP)
Méthode fonctionnelle
Principe général:
- Réponse hémodynamique: augmentation du débit sanguin et de l'oxygénation sanguine lors de l'activité neuronale.
- Mesure de cette augmentation grâce à un traceur radioactif: Oxygène 15 (marqueur de l'eau): 15O-eau
- L'isotope 15O se désintègre rapidement (~2min) en émettant un positon; lorsque celui-ci rencontre un électrons, les deux s'annihilent en émettant deux photons sur un axe (dans des directions opposées). Les photons sont finalement détecté par les capteurs.

| Pros                                        | Cons                           |
| ------------------------------------------- | ------------------------------ |
| Mesure directe du traceur->données absolues | Injections multiples           |
|                                             | Faible signal                  |
|                                             | Moyennage sur plusieurs sujets |
|                                             | Radioactivité                  |
- D'autres traceurs existent:
	- Fluor 18, permettant de suivre la synthèse de dopamine, *utilisé dans les études sur la maladie de Parkinson*
		- Permet aussi de suivre le métabolisme du glucose (typiquement mis en jeux pour les muscles, le cerveau, et les *cellules cancéreuses*)

# IRM: Bases physiques
## Technique d'IRM et Imageur
- Non invasif
- Image 3D du cerveau
- Basé sur la **résonance magnétique nucléaire** (RMN)


La RMN eploite les propriétés magnétiques de certains noyaux atomqies, comme le noyau d'hydrogène. L'hydrogène est composé d'un noyau qui contient un seul proton, il tourne sur lui-même et a donc un moment magnétique (spin nucléaire - moment microscopique).
En l'absence de champ magnétique:
- Les spins des noyaux ont des directions *aléatoires*: aimantation longitudinale nulle (en moyenne)
### Principe de la**RMN**:
1. *Magnétisation*: on impose un champ magnétique (3Tesla - 60000 fois le champ magnétique terrestre), les spins nucléaires s'alignent sur ce champ magnétique, soit dans le même sens, soit dans le sens opposé. Le *moment magnétique* résultant est une *aimantation longitudinale* ($M_0$) non nulle, orientée *dans le sens du champ provoqué* ($B_0$). (les spins sont toujours en rotation, soumis à un mouvement de *précession*, ils tournent alors à une fréquence de résonnance (de Larmor), selon l'axe du champs)
2. *Résonance*: perturbation de l'état d'équilibre thermique par application d'une onde (champ) radio-fréquence $B_1$. Ce champ est produit par un courant sinusoïdal à la fréquence de drésonance du système de spins étudié (fréquence de Larmor, spécifique à l'hydrogène). Le champ $B_1$ est perpendiculaire à $B_0$. Cette perturbation n'est active que très momentanément et permet de basculer l'aimantation longitudinale dans le *plan transversal*, ce qui permet sa mesure.
3. *Relaxation*: retour à l'équilibre par arrêt du champ $B_1$
	- *Relaxation longitudinale*: Alignement de $M_0$ sur $B_0$, de constante de temps $T_1$.
	- *Relaxation transversale*: Diminution de l'amplitude de la composantes $M_{x,y}$ (plan transversal), vers sa valeur d'équilibre (0). La constante de temps associée est $T_2$. On parle aussi de *déphasage des spins*. Deux phénomènes principaux sont à l'origine de ce déphasage:
		- l'Interaction avec l'environnement des protons de l'eau
		- l'inhomogénéités du champ statique $B_0$ due à:
			- des défauts de fabrication
			- la présence d'un objet dans le champ
			- la présence d'agents paramagnétiques (*désoxyhémoglobine*)
			Dans ces cas là, la relaxation transversale est encore plus rapide, on la note alors $T_2*$
	- Note: T2 < T1

### Contraste T1
Les différentes tissus sont représentés en nuances de gris
- Hypersignal: tissu en blanc (Substance blanche), T1 plus court
- Hyposignal en noir (Lésion en général (qui contiennent beaucoup d'eau) et Liquide céphalo Rachidien (LCR)), T1 plus long
- Isosignal en gris (Substance grise)

Le contraste en T1 est dit '**anatomique**' (car substance blanche en blanc, grise en gris); plus le signal est fort, plus T1 est court.
### Contraste T2
Le contraste T2 est dit 'inverse', plus le signal est faible, plus T2 est court:
- Substance blanche en gris foncé
- Substance grise en gris clair
- LCR en blanc
- Lésions en blanc -> Interet particulier de ce type de contraste, pour mettre en évidence les lésions)

## IRMf: BOLD
L'IRMf étudie la fonction.
### TEP vs IRMf
Tous les deux mesurent **indirectement** l'activité cérébrale par l'intermédiaire de la réponse *cérébro-vasculaire* ou *hémodynamique*.
- La TEP mesure directement l'augmentation du débit sanguin régional (grâce au traceut $O_{15}$)
- L'IRMf observe les *variations de l'oxygénation sanguine* (par effet **BOLD**) sans injection de traceur radioactif, le traceur étant endogène (l'hémoglobine, ou plutôt sa version paramagnétique: la *désoxyhémoglobine*). Il permet donc des examens répétés, sans inconvénient. Mais les mesures en IRMf **sont contrastive** (relatif) et est donc toujours basé sur des modèles (nécessité d'analyse statistiques).

### Effet BOLD
L'hémoglobine possède des propriétés magnétiques différentes selon qu'il transporte ou non l'oxygène dans le sang:
- Oxyhémoglobine: fixation de l'$o_2$ par l'hémoglobine: union diamagnétique, non perturbateur d'un champ magnétique externe appliqué sur les tissus
- Désoxyhémoglobine: hémoglobine dé-oxygénée: molécule paramagnétique, perturbateur d'un champ magnétique externe appliqué sur les tissus


Lors de nécessité forte d'oxygène, l'afflux en oxy-hémoglobine est largement augmentée, bien plus que ce qui est consommé effectivement par les neurones. On observe alors une baisse de concentration en désoxy-hémoglobine dans les régions actives (de *1 à 5%*) (et donc une baisse de perturbation du champ magnétique, donc augmentation du temps de relaxation transversal (**T2* **)).

#### La réponse hémodynamique
Lors de l'entrée en activité des neurones:
1. Forte consommation instantanée de l'oxygène, donc augmentation de la concentration en désoxy-hémoglbine
2. Compensation de la surconsommation par une forte augmentation du débit sanguin après quelques secondes
3. Forte augmentation de la réponse: déséquilibre entre l'apport en oxygène et sa consommation
	- Chute de la concentration en désoxy-hémoglobine (avec un pic autour de 5 à 9 secondes)
4. Retour à l'équilibre après 15-30 secondes.


## Contre indication en IRM
Liées au champ magnétique: ABSOLUES:
- pace makers et défibrillateurs implantables
- neuro-stimulateur
- stimulateur de croissance
- pompe implantée
- implant cochléaires
- prothèses ossiculaires métallique
- tout corps étrangé métallique mobilisable
Liées au patient: RELATIVES
- Claustrophobie
- anxiété importante
- agitation
- impossibilité de se tenir en décubitus dorsal
- enfant de moins de 6 ans
- intubation-ventilation (en l'absence de matériel adapté)

## Effet biologiques
Possible échauffement tissulaire car les tissus absorbent l'énergie des radio fréquences.
- Vertiges
- Gout métallique
- Effets cardiovasculaires
- Déconseillé aux femmes enceintes

# Considérations psychologiques et Inférence inverse

Attention à la tendance à associer certaines régions du cerveau à des processus (réseau de la douleur; du langage; etc.), on parle d'afférence inverse: par exemple dans l'étude de Kross et al. 2011, ils font une afférence car les zones activées dans le cas du rejet amoureux sont les mêmes/similaires à celle impliquées dans la douleur. Mais ces zones ne sont *pas typiques* de ces processus, elles sont simplement aussi recrutées dans les différents processus.

-> Observer quelles régions s'activent ne nous apprends pas grand chose sur le fonctionnement mental en général. Mais il faut *regarder quelles théories/modèles sont remis en cause (ou non) par les observations*.

En neuroimagerie, on se pose la question de quelles régions sont plus actives dans une tâche que dans une autre (approche de **cartographie cérébrales**). On est alors dans le paradigme d'inférence directe:
1. On demande au sujet de réaliser une tâche. 
2. On regarde quelles zones sont plus impliquées (contraste statistique). 
Et non pas dans l'autre sens!

*Qu'une région cérébrale cible soit active ou non doit contraindre votre théorie à vous apprendre quelque chose de nouveau.*

*Si une région est* **sensible** *mais non* **spécifique**, *elle s'active souvent, mais pour plein de raison.*
*Si elle est **spécifique** mais peu **sensible**, elle s'active rarement, même lors de la condition.*

**Inférence directe**:
Etant donné un état psychologique induit, on *observe* l'activité cérébrale
**Inférence indirecte**:
Compte tenu de l'activité cérébrale, pouvons nous en déduire l'état psychologique?


Conclusion sur les inférence inverses:
- L'inférence inverse est la pratique consistant à traiter le cerveau comme un marqueur de quelque chose.
- Lorsque les gens font des inférences inverses, il supposent une valeur prédictive positive élevée (**VPP**).
- La VPP peut être calculée mais nécessite l'évaluation de plusieurs tâches/états potentiellement confondus
- pour que l'activation cérébrale régionale ait une VPP élevé:
	1. **TODO**
	2. **TODO**


Quels types de théories la neuroimagerie peut-elle tester?
1. Théories de localisation fonctionnelles (question "où?")
	- Cartes d'activation
	- Contraste tâche/contrôle
2. Théories de connectivité et d'architecture fonctionnelle (question "avec qui?")
	- Analyse de connectivité, graph theory, ICA (Analyse en Composantes Indépendantes)
3. Théories mécanistes/computationnelles (question "comment?")
	- Relier les modèles cognitifs/neuronaux aux données IRMf
	- RSA, modèles de décodages multivariés (MVPA), modélisation computationnelles couplée à l'IRM

# Réalisation pratique d'un examen IRMf
1. Scan de repérage
2. Scan fonctionnel
	- Acquisition des volumes fonctionnels (contraste tâche/contrôle)
	- Séquence d'acquisition: ensemble des coupes réalisées avec les mêmes paramètres d'acquisition.
3. Scan anatomique

# Expérience sur la perception olfactive et la motricité
Les réseaux primaires sont assez bien connus.
## Imagerie olfactive et motrice
Représentation mentale d'une sensation perceptive sans stimulation externe:
- imagerie olfactive, souvent moins vivace
- imagerie motrice, typiquement assez vivace

Passation du QQME par les sujet: pour mesurer l'aphantasie dans les différents sens.

## Matériel et méthode
4 tâches cognitives: moteur, olfaction, imagerie motrice, imagerie olfactive.
