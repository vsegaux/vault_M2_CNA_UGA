
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


## 1. Origine et modélisation des champs récepteurs visuels

### Justification Neuro-anatomique

Le système visuel humain traite l'information de manière hiérarchique, en commençant par la rétine1.

- **Mécanisme de base** : Les photorécepteurs activent des cellules bipolaires qui, à leur tour, activent ou inhibent les **cellules ganglionnaires**2.
    
- **Organisation Centre/Bord** : Ces cellules fonctionnent selon un modèle "centre ON / bord OFF" (ou inversement), créant une structure de filtrage initiale3.
    
- **Hiérarchie du traitement** : L'information circule par convergence et filtrages successifs : de la rétine vers les cellules ganglionnaires, puis vers le Corps Genouillé Latéral (LGN), pour atteindre enfin les cellules simples et complexes du cortex visuel primaire (V1)4444.
    
    +2
    

### Justification Statistique et Modélisation

La forme particulière de ces champs récepteurs n'est pas arbitraire : elle répond à un besoin d'efficacité du signal5.

- **La Différence de Gaussiennes (DoG)** : On modélise les champs récepteurs du LGN par une soustraction de deux fonctions gaussiennes6. Ce profil est surnommé le **"chapeau mexicain"**7.
    
    +1
    
- **Extraction de contrastes** : Statistiquement, ce type de filtrage permet de mettre en évidence les contrastes et les contours dans une image, plutôt que les zones de luminosité uniforme8.
    
- **Cellules simples de V1 (Filtres de Gabor)** : Dans le cortex V1, les champs récepteurs deviennent sensibles à l'orientation99. On les modélise par des **fonctions de Gabor** (une sinusoïde modulée par une gaussienne) qui agissent comme des détecteurs de barres orientées10101010. Chaque cellule est spécifiquement sensible à une orientation et une fréquence spatiale donnée11111111.
    
    +3
    
- **Cellules complexes** : Elles agrègent l'information de plusieurs cellules simples pour devenir insensibles à la position exacte (la phase) tout en restant sensibles à l'orientation12.
    

---

## 2. Les attaques adverses : mécanismes et solutions

### Qu'est-ce qu'une attaque adverse et pourquoi fonctionne-t-elle ?

Une attaque adverse consiste à modifier une image de base par une perturbation quasi invisible pour l'humain, mais qui trompe totalement un réseau de neurones convolutifs (CNN)13.

- **Mécanisme technique** : On ajoute à l'image authentique un "bruit" spécifique ou une texture provenant d'une autre catégorie14. Par exemple, ajouter un bruit calculé à partir du "barycentre" de la catégorie "gibbon" à une image de "panda" forcera le CNN à prédire "gibbon"15.
    
    +1
    
- **Origine de la faille** : Les CNN actuels ont un **biais vers les textures** plutôt que vers les formes globales16. Contrairement aux humains, ils manquent de mécanismes de compréhension de l'environnement (liés aux aires pariétales) et de traitements descendants (top-down)17.
    
    +1
    

### Solutions proposées pour limiter ces attaques

Pour rendre les modèles plus robustes, les chercheurs s'inspirent des neurosciences et de la psychologie cognitive18:

- **Catégories sur-ordonnées** : Apprendre au modèle que certaines catégories partagent des traits communs (ex: chien et chat sont des "animaux terrestres") pour stabiliser la classification19.
    
- **Connexions descendantes (Top-Down)** : Intégrer des connexions récurrentes (comme dans les architectures RNN ou SRN) pour permettre au réseau d'affiner sa perception en fonction du contexte20202020.
    
    +1
    
- **Le "Primal Sketch" (Basses Fréquences)** : S'inspirer du circuit cérébral où les informations de **Basses Fréquences Spatiales (LSF)** sont envoyées rapidement au cortex orbitofrontal pour guider la reconnaissance dans le cortex inférotemporal212121212121212121.
    
    +2
    
    - L'idée est de construire une ébauche globale de l'objet qui résiste aux attaques adverses, lesquelles se cachent souvent dans les Hautes Fréquences (HF)22.
        
- **Anticipation et Récurrence** : L'utilisation de réseaux récurrents simples (SRN) montre de meilleures performances que les perceptrons multicouches (MLP) classiques, notamment pour reconnaître des stimuli subtils (ex: émotions non exagérées), car l'architecture de traitement est plus proche du fonctionnement dynamique du cerveau23232323.
    
    +1
    