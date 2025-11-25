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
	- 