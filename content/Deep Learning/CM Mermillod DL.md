---
prof: MERMILLOD Martial
date: 2025-11-12
publish: true
---
# Les origines des réseaux de neurones artificiels

Alan Mathison Turing (1912-1954) : Mathématicien et logicien anglais.
*Machine de Turing* : Concept d’algorithme, *succession* d’instructions agissant en séquence sur une mémoire. -> Machine séquentielle

Warren Sturgis McCulloch & Walter Pitts :  premier neurone formel. Neurones binaires -> somme pondérée des entrées (qui valent aussi 0 ou 1, ou parfois normalisé $[-1;1]$) puis fonction d'activation à seuil : si la somme pondérée dépasse une certaine valeur, la sortie du neurone est 1, sinon elle vaut 0.

![[neuroneFormel.png]]

Réseau de neurones à spike (STDP: Spike Time Dependent Plasticity) (Hodgkin & Huxley, 1952) sont une alternative qui est potentiellement plus économe en énergie, mais qui présente d'autres contraintes.

Donal Hebb (1904-1985).: Loi de Hebb: *L’efficacité des connexions entre les neurones augmente en fonction de leurs activités pré et post-synaptiques*. 

Frank Rosenblatt (1928 - 1971), psychologue et concepteur du premier réseau de neurones artificiels: le Perceptron. Le perceptron était composé de deux couches et son but était de reconnaitre des formes géométriques basiques (triangle, rond, carré). Le perceptron est capable d'apprendre à les reconnaitre en modifiant les poids associés aux liens entre ses neurones.

![[perceptron_2_couches.png]]

Mais le perceptron présente des limites: il ne peut résoudre que des problèmes linéairement séparables:
![[non_lineaire_2_neurones.png]]

Or: Shepard, Hovland & Jenkins (1961) ont montré que l'être humain pouvait résoudre des problèmes non-linéairement séparables.

John McCarthy (1927-2011), mathématicien : Père de l'IA symbolique (par opposition au connexionisme) et du langage LISP. Qui fonctionne plutôt bien dans un environnement contrôlé, mais pas en dehors.

## Du perceptron au perceptron multi-couches
John Joseph Hopfield (1982), physicien américain : inventeur des réseaux neuronaux de Hopfield.
Teuvo Kohonen, chercheur finlandais : inventeur des cartes auto-organisatrices. Similaire au clustering, à la recherche de similarité entre différents signaux d'entrée. Il s'agit d'algorithme non supervisés.

Widrow & Hoff (1960): correction des poids synaptiques locaux par la méthode des moindres carrés->évolution de la loi de Hebb. Par descente de gradient:
![[descente_gradient.png]]

Rumelhart & McClelland: Parallel Distributed Processing Group. Conception du perceptron multicouche: la connaissance réside dans les connections (connexionisme).
Le fait d'avoir plusieurs couche permet de résoudre les problèmes non-linéairement séparables par modification de l'espace d'entrée.

Exemple avec un perceptron multicouche: base de donnée MNIST. Architecture en H : 784, 400, 100, 2, 100, 400, 784. L'image d'entrée contient 784 pixels, l'image de sortie aussi, c'est encore un autoassociateur (dont le but est de reconstruire). 

Dans le cas d'un hétéro-associateur, l'espace latent est différent, pour une tache de classification par exemple, l'architecture en H est alors 784, 400, 100, 2, 100, 400, *10*. Avec *10* classes possibles en sortie.

## Apprentissage dans un Perceptron Multi-Couches (MLP)
### Etape 1: Transduction
Il s'agit de transformer la richesse du monde physique qui nous entoure en une matrice d’activité électrique interprétable par le cerveau.

Différentes méthodes:
- *Traits caractéristiques binaires ou continus*
- *Mesures physiques* 
	- Exemple: Mesures biométriques pour la reconnaissance de visages dans le but de les catégoriser entre masculin et féminin. Les différentes entrées sont donc la largeur entre les yeux, la largeur du visage, sa hauteur, etc...
- *Simulation du système perceptif humain*
- Autre
	- Exemple: Encodage du niveau de gris de pixels

### Etape 2: Conception de l'architecture du réseau
Combien de couches, combien de neurones etc...
- Dans un réseau de neurone biologique, processeur=mémoire; ce n'est pas le cas en électronique (d'où les soucis de temps de latence/consommation énergétique)
- Travail au niveau des électroniciens pour effectuer les calculs localement (développement de memristor)

### Etape 3: Définition des données d'entrées/sortie
Exemple: des pixels d'une image en entrée et des classes en sortie (MNIST)

### Etape 4: Diffusion de l'information dans le réseau de neurone
Comment est calculée l'activité de chaque neurone au sein du réseau. Typiquement, chaque neuronne est activé selon la somme pondérée des activations de ces neurones d'entrées (McCulloch & Pitts) et de la *fonction de transfert* (ou d'activation) qui le défini.

La fonction de transfert est responsable de déterminer l'activation du neurone de sortie et sa normalisation. Il s'agit typiquement:
- d'une sigmoïde: $f(a)=\frac{1}{1+e^{-a}}$ , mathématiquement couteuse. ![[sigmoid.png]]
- d'une 'Relu', Rectified Linear Unit, mathématiquement plus simple, mais pas dérivable dans sa partie négative. ![[Relu.png]]

Grande variété de fonctions d'activations:
![[Fct_activation.png]]
### Etape 5: Descente du gradient
Rétropropagation du gradient d'erreur. Dans le cas le plus simple possible: deux neurones reliés par une synapse avec une LOSS: MSE (*Mean Square Error*) = $\frac{1}{N}\sum_{i=1}^{N}(y_{i}- t_i)^2$  . L'erreur correspond à (Sortie observée - sortie attendue)². La MSE est typiquement utilisée pour des sorties analogiques.

![[2neurone_descent_grad.png]]
On utilise la dérivée pour chercher les minimums d'erreur. D'où l'interet que les fonctions d'activations soient dérivables.

Une autre manire de calculer l'erreur est la *Cross-Entropy*, plus efficace pour les données binaires (classification 0/1 typiquement).


Finalement, deux fonctions de coût:
- MSE (pour des données continues)
- Cross-Entropy (pour des données binaires)

---
La forme générale de l'équation de la descente de gradient pour un poids Wj dans le réseau de neurones : 
$W(j+1) = Wj - α (δE/δW)$
où :
- Wj+1 : *poids à venir* de la connexion synaptique 
- Wj : *poids actuel* de la connexion synaptique 
- α : taux d'apprentissage (une valeur positive qui contrôle la vitesse de mise à jour des poids) 
- δE/δW : dérivée de la fonction d’erreur par rapport au poids Wj 
- 
La dérivée de la fonction d’erreur par rapport à un poids donné nous donne la direction dans laquelle la fonction d’erreur change le plus rapidement. En utilisant cette information, nous pouvons mettre à jour les poids dans la direction opposée, ce qui réduit l’erreur.

La **règle de la chaine** permet de rétro propager la descente du gradient dans des couches profondes de neurones. Elle a été démontrée par des mathématiciens (Rumelhart):
![[chaine_de_regle.png]]



#### Le faux problème des minima locaux
Lié surtout à notre incapacité à nous représenter un monde au delà de 3D. Dans ces conditions, il n'y a pas réellement de problème des minima locaux, la preuve mathématique à été proposée en 2014 par Dauphin, Pascanu etc...: A haute dimensionnalité, il y a toujours un chemin pour atteindre le minimum d'erreur.

#### Le faux problème de la boite noire
Torralba & al. ont essayé d'identifier quels sont les traits caractéristiques qui provoquent les prises de décisions dans les couches intérieures des réseaux neuronaux.
On explore, dans la reconnaissance d'image par exemple, les cartes de saillances (zone d'interet).
- En psycho: yeux et bouches pour les émotions
- En neuro: localisation des activations cérébrales 

#### Autres paramètres d'optimisation

- *Learning rate*: paramètre alpha qui intervient dans le calcul des poids lors de la descente du gradient.
	- S'il est faible, le réseau va converger plus lentement
	- S'il est trop élevé, il va "rebondir" dans la fonction d'apprentissage et ne jamais converger.
- Le *momentum*: Paramètre additionnel qui tient ajoute une notion d'inertie dans la descente du gradient. Ce qui lui permet d'avoir des variations rapides au début, et de plus en plus faible à mesure qu'on s'approche du minimum d'erreur.
- *Fahlman offset*: Moins utilisé de nos jours. Prinipalement utilisé pour les sigmoïdes.
- *Optimizer*
	- Adam (algorithme particulier qui remplace l'offset de Fahlmann)
- *Batch size*

#### Conclusion sur l'optimisation
S’informer de la mode du moment mais surtout des contraintes associées (généralisation à d’autres bases ou d’autres fonctions d’apprentissage, surapprentissage, etc.).

### Etape 6: L'apprentissage itératif

Le réseau de neurones apprends mais surtout doit être capable de généraliser son apprentissage à de nouveau stimuli.
Au départ, les poids sont aléatoires donc les sorties le sont aussi. On calcul l'erreur, on modifie les poids en renforçant celles qui "vont dans le bon sens" par propagation du gradient. Et puis on itère jusqu'à convergence. 

#### Mesures
- *Accuracy*
	- Winner take all: Sélection de la plus haute valeur.
	- Soft max: normalisation de l'activité de sortie pour que la somme des sorties soit égale à 1 (ie pour donner la probabilité de réponse)
- *Matrice de confusion*:
	- Pour chaque classe possible, on affiche les match/mismatch donné par le modèle avec chaque autre classe possible ![[matrice_confusion.png]]
- *Loss* :
	- Erreur produite ![[Loss_sur_apprentissage.png]]
	- On peut utiliser la loss pour quantifier le degré d'erreur d'un modèle.


# Chapitre 3: Du perceptron au perceptron multi couches au deep learning


> [!NOTE] Examen! Champs récepteur de V1 et pourquoi ils sont comme ça? (biologiquement, depuis les récepteurs de la rétine!)
> Contents

Une possibilité est de passé de l'image à des features (les "*gabor*" par exemple) et de les donner ensuite au réseau de neurone. Cette approche est inspirée du système visuel humain (avec les cellules ganglionnaire centre OFF, bord ON; en réalité, les photorecepteurs sont activateurs des cellules bipolaires, qui elles même sont à leur tour soit activatrice (ON) soit inhibitrice (OFF) de la cellule ganglionnaire).
Pooling/convergence et convolution successives donnent finalement un filtrage depuis la rétine vers les cellules ganglionnaires, puis des cellules simples vers les cellules complexes de V1).
![[gabor_to_rn.png]]

Ces champs recepteurs peuvent être modélisés par une différence de Gaussienne:
![[double_gauss_convol.png]]
On parle aussi de chapeau mexicain. Ce type de filtrage permet de mettre en évidence les contrastes dans l'image.

Les champs récepteur des cellules simples de V1 forment les Gabor, des détecteurs de barres orientées: ![[GABOR_V1.png]]
Sur cette figure, le champ récepteur excitateur correspond aux barres bleues et blanches, les champs inhibiteur sont les barres jaunes et noires.


Une autre possibilité est de prendre des filtres de convolution très simple en entrée, et laisser le réseau de neurone choisir quelles features il utilise, c'est cette deuxième option qu'ont proposé LeCun, Bengio & Hinton (2015) (Deep learning). Au final, on remarque que des gabors sont quand même extraits dans les premières couches internes.

Pour modéliser ces Gabor, nous utilisons des fonction de Gabor, qui correspondent à des sinusoïdes modulées par des gaussiennes: ![[gabor_model_function.png]]

Dans le cerveau, chaque cellule simple de V1 est spécifiquement sensible à une certaine orientation de a stimulation.
Les cellules complexes vont quant à elle "aggrégé l'information" issue de plusieurs cellules simples, leur permettant d'être insensibilisé à la phase (donc à la position exacte de la stimulation dans l'image). Elle reste cependant sensible à l'orientation et la fréquence spatiale.


Plus loin dans la chaine de traitement visuel du cerveau (cortex inferotemporal IT), certains neurones ont une activité spécifique par rapport à des formes géométriques.


Typiquement, un lion est détecté quelque soit sa position, taille ou orientation dans le champ visuel.

### Traitement de données dynamique
Exemple des chaines de Markov: Chaine de probabilité, typiquement pour les modèles de langages.

**Simple Recurrent Network** SRN: 
Typiquement utilisé pour les séries temporelles, ces réseaux de neurones utilisent des couches de neurones récurrents, qui retiennent l'information accumulée au fil des étapes. Ces valeurs de neurones sont ré-introduites en entrée du réseau.

Problème du vanishing gradient des RNN:
- l'utilisation de la descente du gradient n'est pas efficace sur des apprentissages à long terme. L'accumulation de donnée réduit l'efficacité de cette descente.
- une réponse a été de proposer une variente du SRN, avec des entrées d'oubli et des entrée d'apprentissage (Long Short-term memory LSTM)
- une autre proposition de réponse est la Gated Recurrent Unit (GRU), une version simplifiée du LSTM avec simplement 2 portes.
#### Des RNN aux transformers
**Transformer**: Du papier 'Attention is all you need.'
- Des tokens (querry, key, value) sont extraits des données et des "têtes attentionnelles" sont calculées. Querry * Key, donne les interdépendances entre ces tokens.
- Dans les transformers, les convolutions sont remplacées par ces couches attentionnelles (multiplcation des vecteurs QK, pour ensuite multiplier la matrice obtenue par V).
- Les transformers demandent beaucoup de place/de ressource (de manière quadratique avec l'augmentation du volume d'entrée), mais il permet de comprendre les relations même à long terme dans les entrées.

# Le deep learning depuis 2012
## La belle histoire

En 2012:
- Poussée du marketing
- Développement de GPU
- Début du BigData

### Catégorisation visuelle
(2012, Imagenet classification with deep convolutional neural networks), parmis 1000 catégories d'images.
DeepNeuralNetwork stratégique pour Google et Facebook avec la reconnaissance faciale.
- Les modèles de deep learning (CNN ici) apprennent d'eux même (par exemple l'âge selon al taille des oreilles)
- Pour la génération d'image, deux modèles fonctionnent en parallèle, un embedder qui doit extraire des traits caractéristiques; et un générateur, qui synthétise des nouvelles images. Ces images synthétisées sont données à l'embedder pour voir s'il arrive à reconnaitre l'image de synthèse comme étant réelle ou non: ![[generative_dnn.png]]

### Intelligence et jeux
Eléboration de stratégies avancées pour obtenir un maximum de points avec un minimum d'actions. Les enchainements d'actions sont appris et généralisés afin de remplir un but.
Typiquement pour Alpha Go, des IA sont entrainées en jouant les unes avec les autres, et seulement les meilleures sont conservées pour la génération suivante etc.. Puis AlphaStart sur Starcraft: '99.8%' de victoire face aux humains. Puis sur des jeux de coopération, comme Dota 2, l'IA développe des stratégies de coopérations, de camping etc..

### Autres domaines
- 21 juillet 2025, meilleur que les humains en mathématiques
- Décryptage et génèse de protéines: AlphaFold
	- Attention alerte éthique: cette IA peut aussi tout à fait créer des virus. A surveiller son utilisation
- GNoME: Synthèse de nouveaux matériaux, 800 ans de recherches humaines en quelques semaines d'IA.
	- Ici encore, la question de l'utilisation de ces matériaux pose potentiellement problème.
- AlphaDogfight (2024), pilotage d'avion de chasse. Attention aux dérives, l'IA pour atteindre son objectif est prête à tuer/détruire, même à faire des opérations kamikazes. IA plus efficaces pour le combat aérien car sans contraintes (accélération etc...).
- Drone de combat.
- Autres soucis éthiques: Fake News, manipulation d'opinion etc...

## L'histoire honteuse

Retournement de veste 'ne faite pas de réseaux de neurones' avant 2012, puis engouement ensuite.
Architecture développée pour gagner des pourcentages de performance sur Imagenet/MNIST etc... Pas forcément intéressant réellement (resnet50 avec 152 couches par exemple).

Question de l'intelligence des IA, mais quelle est la définition de l'intelligence?
Thurstone, Spearman et Wechsler s'y sont intéressés pour dresser des échelles composites d'intelligence.

## Limite des CNN actuels

> [!NOTE] Examen potentiellement!!! Attaque adverses et solution!
> Contents



On modélise bien le système visuel avec les CNN, mais les aires pariétales qui permettent de comprendre l'environnement (les intentions d'autrui etc...) ne sont pas simulées/modélisées, alors qu'on y gagnerait bcp.
### Attaques adverses
Des combinaisons d'images perturbent fortement les CNN:
- Par sommation de l'image de base avec 
	- Texture d'une autre image
	- Bruit correspondant au barycentre d'une autre catégorie (gibbon sur l'exemple ci-dessous) (barycentre obtenu par 'affichage' des résultats d'apprentissage du CNN)
	- Modification des couleurs
	- ![[attaque_adverse.png]]

Pourquoi ça marche sur les CNN?  Les CNN actuels ont un **biais vers les textures** plutôt que vers les formes globales16. Contrairement aux humains, ils manquent de mécanismes de compréhension de l'environnement (liés aux aires pariétales) et de traitements descendants (top-down).

Plusieurs solutions inspirées de la psychologie, des neurosciences (plutôt que simplement ajouter des couches comme dans resnet50):
- Donner la capacité aux modèles de creer des catégories sur-ordonnées (chien, chat appartiennent à 'animaux terrestres')
- Ajouter des 'connexions descendantes' (typiquement dans les RNN) dans le traitement des images. Inspirés des circuits de prédiction du cerveau humain (Kauffman L. Ramanoël S, Pyrin C (2014)): les infos BF de V1 sont envoyée au cortex orbitofrontal (en parallèle d'un envoi au cortex inférotemporal qui s'occupe de la reconnaissance) afin qu'il participe à guider la reconnaissance visuelle (effectuée dans le cortex inférotemporal): ![[kauffmanL_orbitofrontal.png]] Sur la base des basses fréquence, on se construirait un 'primal sketch' qui permet de bien mieux résister aux attaques adverses (typiquement HF).
- Finalement, ça revient à ajouter des traitements top-down.
#### Solution proposée : anticipation
"Mermillod, M., Bourrier, Y., David, E., Kauffmann, L., Chauvin, A., Guyader, N., ... & Peyrin, C. (2019). The importance of recurrent topdown synaptic connections for the anticipation of dynamic emotions. Neural Networks, 109, 19-30"

Comparaison d'un MLP (multi layer perceptron) classique et d'un SRN (simple recurring network) pour la reconnaissance d'émotion:
- meilleure performance pour les émotions non "exagérées" avec le SRN
- Pas de différence de performance pour les émotions exagérée
- Limite de l'étude de base: le SRN a plus de couches/neurones que le MLP
	- Correction du MLP pour augmenter son nombre de neurones/couche pour être équivalent au SRN. La seule différence étant alors dans l'architecture de traitement de l'information
	- Le SRN reste plus performant pour les visages 'non exagérés'

### Oubli catastrophique
Incapacité des IA à apprendre de manière sérielle. Si on apprends à un réseau de neurone à faire une tâche (jouer aux échecs), puis qu'on veut lui faire apprendre une nouvelle tâche, il va en quelque itérations oublier complètement à faire la première tâche (modification totale des poids/neurones).
![[oubli_catastr_VS_humains.png]]

Dans le cerveau humain, l'hyppocampe permet la mémoire épisodique: il indexe les souvenirs contenus dans le néocortex. Les souvenirs sont maintenus par réactivation aléatoire (rêves) de certaines traces. (CF cours de Rousset de la première partie du semestre). Modélisé dans un réseau de neurone (ou plutôt dans 2 réseaux):
![[hypo_cortex_réseau_neurone.png]]
Dans l'exemple ci-dessus, le learning net seul est soumis à l'oubli catastrophique, mais ses sorties sont injectées dans le memory net dont les sorties sont elle-meme redonnées en entrée au learning net. Le mémory net aggrège les différentes classes possible. Avec un tel système, il est possible d'apprendre de nouvelles classes (discriminer de nouvelles émotions par exemple) de manière sérielle. On suppose donc au départ avoir suffisamment de neurones de sorties pour accueillir toutes les 'nouvelles' classes possibles (seulement certains sont actives au départ).

#### Exemple d'application
Prédiction de consommation énergétique pour les pompes à chaleurs (soucis d'oubli catastrophique avec/sans télétravail). -> 40% d'économie d'énergie cool.

#### Application aux données de psychologie
![[donne_psycho_DL.png]]
Reconnaissance d'émotion, de genre à partir de photos de visages. A partir des CNN, on déduis les cartes de saillance et on déduit les éléments qui ont été les plus important (gradients plus hauts) (attention, les cartes de saillance ne sont valable que pour la tâche 'courante').

En neurosciences aussi pour les données IRM, typiquement pour desceller alzheimer.
Collaboration CEA LIST/CLinatec/LPNC pour des exosquelettes pour des sujets tétraplégiques.

# Avantages biologiques et computationnels de systèmes PDP pour la cognition humaine
## Neurone grand-mère
Plusieurs données plaident en faveur d’un traitement parallèle et distribué dans le cerveau humain. Concept de neurones «grand-mère» (Bowers, 2010), McCLelland (2010) et Quiroga & Kreiman (2010) (Jennifer Aniston). L'information est distribuée, donc résiliante, résistante à l'altération physique (dans le cas d'alzheimer, on peut atteindre 50 à 60 de destruction du système avant de percevoir des symptomes).


## Résistance au bruit inhérent des réseaux de neurones biologiques
- The probability that a synapse fails to release neurotransmitter in response to an incoming signal is remarkably high, between 0.5 and 0.9
- The spontaneous firing of spikes accounts for almost 80% of the metabolic energy consumed by the brain
- *La structure parallèle / distribuée du système permet un fonctionnement efficient malgré le taux d’échec et de bruit de la matrice synaptique*

## Rapidité des processus cognitifs malgré la lenteur des processurs biochimiques de communication entre les neurones

Dans les ordinateurs (machine de Turing etc..), goulot d'étranglement au niveau du CPU (64bits) pour traiter des mémoires à plusieurs GHz. Dans le cerveau, le CPU=La mémoire, tous les processus sont parallèles et distribués.


## Réseau de neurones artificiels et MEMRISTOR

![[memristor.png]]
[Débouché stylée](https://www.inp.cnrs.fr/fr/cnrsinfo/le-gdr-biocomp-un-reseau-thematique-sur-le-calcul-bio-inspire)


Fin du cours slide 217/286.