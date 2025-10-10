---
sujet: Modèles de mémoires
prof: GRANDCHAMP Romain
date: 2025-09-23
publish: true
---
Domaines mis en jeu:
- Statistiques: quantifier/décrire des observations
- Data Mining: expliquer/découvrir les motifs/structures
- Machine learning: prédire avec des modèles
- Artificial Intelligence: agir/prendre des décisions

![[Terminologie]]

## Donnée - Information - Connaissance

Une *donnée* est l'enregistrement d'une observation destinée à être interprétée/traitée par l'humain (ex. température, temps de réaction, âge, ...)
Une *information* est le signifiant attaché à la donnée ou à un ensemble de données par association. L'information est définie selon un contexte (ex. temps chaud pour T=40°C; nourrisson pour âge=2mois, ...)
Une *connaissance* est une information nouvelle, apprise par association d'information de base, de règles, de raisonnement, d'expérience (ex. T=35°C et avec cette température, nous devons ajuster le système de refroidissement; âge=2mois alors il ne faut pas lui donner d'alcool, ...)

## IA et apprentissage

![[AI_ML_DL.png]]


| Type d'apprentissage | Supervisé                                                                                                                     | Non Supervisé                                                                                                                                                | Par renforcement                                                                                                                    |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| Description          | Les données d'entrée ont été labelisée (i.e. elles ont déjà été traitées)<br>- Prediction<br>- Classification<br>- Regression | Données non labelisées, l'algorithme doit trouver des structures cachées<br>- Clustering<br>- Estimation de distribution de proba<br>- Reduction de dimesion | On qualifie la sortie du système (note de performance, ex: qté d'argent, distance parcourue...) afin de l'entrainer par essai-errur |
| Exemple              | k-NN (NearestNeighbours); reconnaissance de chiffre manuscrits, ...                                                           | Clustering, segmenter une clientèle selon leurs comportements, ...                                                                                           | Alpha-Go, Checkers, apprentissage de la marche pour les robots, ...                                                                 |
| Avantage             | Efficace lorsque les étiquettes sont disponibles et les relations bien définies                                               | Aucune étiquette nécessaire, ce qui est pratique pour des ensembles de données massifs où l'étiquetage est impossible.                                       |                                                                                                                                     |
| Inconvénients        | Nécessite un grand nombre de données étiquetées: coûteux et chronophage.                                                      | Les résultats peuvent être difficiles à interpréter et moins précis sans supervision claire.                                                                 |                                                                                                                                     |

*Deep learning*: Relatif à la méthode d'implémentation (des réseaux de neurones) plutôt qu'au type d'apprentissage (ex: reconnaissance d'image, traduction automatique, ChatGPT).


## Notion d'intelligence

*Intelligence*: Capacité à comprendre un contexte nouveau, et à réagir à cette nouvelle situation de façon adaptée (Richard Atkinson).
Plusieurs définition possibles, certains points communs entre les définitions:
- Capacité à s'adapter à l'inconnu
- Capacité à apprendre
- Capacité à relier, à dégager des formes

Que permet l'IA aujourd'hui:

| OUI                                                       | NON                                                 |
| --------------------------------------------------------- | --------------------------------------------------- |
| Traitement du langage naturel                             | Conscience et émotions                              |
| Automatisation industrielle                               | Autonomie totale dans la conduite - Doucement si!   |
| Jouer à des jeux vidéos                                   | Conduite autonome                                   |
| Diagnostique médical assisté                              | Prise de décisions éthiques complexes               |
| Reconnaissance d'images et de visages                     | Créativité réelle                                   |
| Prévisions et recommandations                             | Adaptation à des environnements totalement inconnus |
| Résolution de problèmes complexes nécessitant du bon sens |                                                     |
| Compréhension profonde et raisonnement générale           |                                                     |
*IA généralisée*: Capable d'étendre les apprentissages réalisés dans un domaine à un autre.

## IA, c'est quoi?

|                    | Fidelity                                                                                                                                                                    | Performance                                                                                                            |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Reasoning/internal | *Think like people*<br>The automation of activities that we associate with human thinking, activities such as decision-making, problem solving, learning... (Bellman, 1978) | *Think rationally*<br>The study of the computations that make it possible to perceive, reason and act. (Winston, 1992) |
| behaviour/external | *Act like people*<br>The study of how to make computers do things at which, at the moment, people are better. (Rich and Knight, 1991)                                       | *Act rationally*<br>Computational Intelligence is ths study of the design of intelligent agents. (Poole et al. 1998)   |
Répétition du tableau...: **Deux approches de l'IA**:
- *Reproduction du comportement* : L'IA est jugée uniquement sur sa capacité à imiter les actions humaines de manière efficace, sans tenir compte des processus qu'elle utilise pour arriver à ces actions. Ce qui compte, c'est le comportement observable. 
- *Modélisation du fonctionnement* : L'IA est jugée sur sa capacité à imiter les processus cognitifs humains, c'est-à-dire la manière dont elle pense ou raisonne, même si ses actions ne sont pas directement les mêmes que celles d’un humain.

## Thinking humanly
Pour comprendre comment pense l'Humain:
- *Introspection*, investigation expérimentale, nécessite des théories sur l'activité du cerveau
- Nécessite d'exprimer ces théories en tant que programmes informatiques
Pour valider ces théories:
- Prédiction et test du comportement humain (*top-down*)
- Identification directement depuis les données neurobiologiques (*bottom-up*)

**Test de Turing**:
Permet de tester la capacité d'une entité à agir comme un humain. Il consiste en 30 minutes d'interrogation libre d'un humain via un ordinateur. A l'issu de ces 30 minutes, si l'interrogateur est capable de distinguer son interlocuteur d'un réel humain, alors la machine a passé le test. Afin de réussir, l'entité a besoin de:
- Natural Language Processing (*NLP*)
- *Knowledge representation*
- *Automated reasoning*
- *Machine Learning*
Mais aussi, pour un test plus évolué:
- Computer Vision
- Robotics

Différents domaines de l'IA:
- Système experts: systèmes d'inférences (raisonnement logique)
- Vie Artificielle: auto-réparation, reproduction..
- Informatique bio-inspirées: exemples: algorithmes génétiques (s'inspirent de la notion de sélection naturelle et l'appliquent à une population de solutions potentielles au problème donné. La solution est alors approchée par bonds successifs.)
- Systèmes multi-agents: Notion d'*émergence*: des comportements simples mais coordonnés peuvent donner un comportement global très complexe.

Différents types de problèmes:
 - *Classification* : Attribuer des objets ou événements à des catégories prédéfinies (par exemple, reconnaître des images de chien ou de chat, distinguer deux espèces de plantes en fonction de la largeur et de la longueur des sépales). 
 - *Régression* : Modélisation des relations entre les variables pour prédire une valeur numérique continue. 
 - *Clusterisation (Clustering)* : Regrouper des données similaires ensemble sans qu'il y ait des catégories prédéfinies (exemple : segmenter les clients d'une entreprise en groupes similaires). 
 - *Association* : Identifier des relations entre des variables dans les données (par exemple, la découverte de règles d’association dans les ventes, comme « les gens qui achètent du lait achètent aussi du pain »). 
 - *Détection d'anomalies* : Identifier des données qui ne suivent pas les schémas attendus (utile pour la détection de fraude, par exemple).

**Fléau de la dimensionalité**:
 Introduite pour la première fois par Bellman (1961), elle indique que le nombre d'échantillons nécessaires pour estimer une fonction arbitraire avec un niveau de précision donné croît de manière exponentielle par rapport au nombre de variables d'entrée (c'est-à-dire la dimensionnalité) de la fonction.
Ex: Dans un volume à 1D, on a 2 bordures, à 2D, on a 4 bordures (des lignes). Dans un cube 3D, on a 8 arêtes et 6 faces qui constituent les bordures.

**Motifs aléatoires**:
*Principe de Bonferroni*, il est possible de découvrir des motifs aléatoires qui n'ont pas réellement de sens simplement en 'considérant' énormément de possibilités.

![[supervise.png]]

Exemple de la régression mathématiques:
- Linéaire: On cherche à prédire Y en fonction de X, selon un modèle linéaire, en minimisant les couts (erreurs/résiduels) qui correspondent aux distances entre chaque point et la droite produite.
- On peut, par transformation (sur les données d'entrée; log/exp/...), retomber sur des modèles linéaire même pour des problèmes non linéaires au départ: ![[linearire.png]]

En rajoutant des termes de degrés supérieurs, on peut modéliser des relations encore plus complexes. On arrive alors dans les problèmes d'**overfitting**:![[overfitting.png]]

### Compromis biais-variance
- **Erreur totale** d'un modèle (=erreur moyenne du modèle sur l'ensemble des données):
	- $Err_{tot}$ = Biais² + Variance + Erreur irréductible
	- Erreur irréductible: C'est l'erreur due à du bruit dans les données, qui ne peut pas être réduite par un modèle. Elle est indépendante du modèle et est souvent liée à la variabilité inhérente des données.
- **Biais**: Le biais mesure *à quel point les prédictions du modèle s'écartent de la vraie* valeur (c'est-à-dire, la moyenne des prédictions par rapport à la moyenne des vraies valeurs). Un modèle avec un biais élevé fait des suppositions simplistes sur la relation entre les variables d'entrée et de sortie. 
- **Variance**: La variance mesure *la sensibilité du modèle aux variations des données d'entraînement*. Un modèle avec une variance élevée sera très influencé par les fluctuations des données d'entraînement, entraînant des prédictions très différentes pour des ensembles d'entraînement légèrement différents. (Variance faible => Faible capacité de généralisation)


![[biais-variance.png]]
![[err_complex.png]]

### Rasoir d'Occam
Entre deux modèles qui expliquent les données de la même manière, on choisit toujours *le plus simple*.

### Régularisation
Plusieurs types de "régulariseurs" existent, il permettent de pénaliser les modèles trop complexes (avec trop de paramètres). Ils donnent un score au modèles, en fonction de l'erreur empirique et d'un terme de régularisation (qui dépend donc de la complexité des modèles).

# ML Workflow
## Prétraitement
Les objectifs du prétraitement sont:
- Corriger des différences de mesures/attribut
	- Certains algorithmes en sont très dépendants: KNN (K Nearest Neighbours), SVM (Support Vector Machine), Lasso, Ridge,...
	- D'autres comme les arbres de décisions ou les régression linéaire le sont moins
- Aider à visualiser les données (échelle commune)
- Aider à interpréter les données (poids, coefficients comparables)

### Prétraitements principaux
- *Standardisation*: Consiste à transformer les données pour qu'elles aient une distribution avec une moyenne de 0 et un écart type de 1. Souvent utilisée lorsque les données suivent une distribution normale (car leur distribution ne sera pas altérée). Transformation des données par la formule : $z = \frac{x-\mu}{\sigma}$ avec x la valeur originale, $\mu$ la moyenne et $\sigma$ l'écart-type.
	- Pertinente avec des algorithmes sensibles à la distribution des données (regréssion linéaire, SVM, K-means)
- *Normalisation*: Change l'échelle des données pour qu'elles soient comprises entre 0 et 1, ou parfois entre -1 et 1. La formule la plus courante est : $x' = \frac{x-x_{min}}{x_{max} - x_{min}}$ avec x' la nouvelle valeur, x la valeur originale et les valeurs minimales et maximales dans les données.
	- Surtout utile lorsque les données ont des gammes très différentes, ce qui pourrait biaiser les résultats d'algorithmes comme (réseaux de neurones, méthodes basées sur la distance comme le KNN)
- *Mise à l'échelle* (scaling): manière plus générale d'ajuster les données pour les amener dans une certaine plage spécifique. *Inclut à la fois la standardisation et/ou la normalisation*, et consiste à redimensionner les valeurs selon une plage ou un intervalle défini.
	- La mise à l'échelle est **nécessaire pour les réseaux de neurones** et **les modèles qui calculent des distances** entre les points de données (par exemple, les algorithmes basés sur des distances euclidiennes, KNN, SVM).

### Autres prétraitements
- *Encodage* d'attributs catégoriques sur la base des données ou sur la base de dictionnaires (ex: One Hot Encoding).
- *Discrétisation*: convertir une variable continue (une variable qui peut prendre une infinité de valeurs, comme la température ou l'âge) en une variable discrète.
- *Binarisation* d'attributs : convertir des variables continues ou catégorielles en valeurs binaires, c'est-à-dire en deux catégories : 0 ou 1.
- *Imputation*: Remplacer les valeurs manquantes.

### Résumé

![[résumé.png]]

## Généralisation/Partitionnement

**Attention**, *il ne faut jamais présenter lors du test d'un modèle des données qui lui ont été présentées pendant l'entrainement.*

### Partitionnement

Répartition du jeu de donnée en:
- **Training set**: jeu d'entraînement pour déterminer les hyperparamètres de l'algorithme (ensemble de règles)
- **Validation set**: jeu complémentaire du training set pour valider le choix des hyperparamètres.
- **Test set**: jeu mis de côté initialement pour mesurer la performance de l'algorithme après optimisation de ses hyperparamètres.

Aucun soucis pour les gros jeux de données (60%/20%/20%), mais sinon, plusieurs autres méthodes sont possibles.

#### Validation croisée à k-plis

Combien de plis? k=5 à 10, si le jeu de test le permet (suffisamment gros). Avec 10 plis, on a une meilleure robustesse du modèle.
##### Interne
Recherche d'hyperparamètres sur différents plis des données d'entrainement puis test avec les meilleurs paramètres. Chaque 'split' dans la figure suivante correspond à un set d'hyperparamètres: 
![[validation_croisee_inner.png]]

| Pros                                                                                                                                                                                             | Cons                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| *Évaluation Robuste* : Elle permet d'obtenir une estimation plus fiable des performances du modèle en utilisant plusieurs itérations de validation.                                              | *Coût Computationnel* : La validation croisée interne peut être coûteuse en termes de calcul, car plusieurs modèles doivent être entraînés et évalués.                                           |
| *Réduction du Risque de Surapprentissage* : En évaluant le modèle sur des sous-ensembles de données, elle aide à réduire le risque que le modèle ne soit trop ajusté aux données d'entraînement. | *Complexité* : La gestion des hyperparamètres et des différentes combinaisons peut rendre le processus complexe et difficile à gérer, surtout pour des modèles avec de nombreux hyperparamètres. |
| *Optimisation des Hyperparamètres* : Elle facilite l'optimisation des hyperparamètres en fournissant une méthode systématique pour tester différentes configurations.                            |                                                                                                                                                                                                  |

##### Imbriquée
La boucle interne permet l'optimisation d'hyperparamètres, c'est dans cette boucle, que chaque ligne (orange sur la figure ci-dessous) correspond à un set d'hyperparamètres.
![[nested_CV.png]]


| Pros                                                                                                                                                                                                                              | Cons                                                                                                                                                                                          |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Estimation Précise de la Performance* : En séparant la sélection des hyperparamètres et l'évaluation des performances, la validation croisée imbriquée fournit une estimation plus précise de la performance générale du modèle. | *Coût Computationnel Élevé* : La validation croisée imbriquée est coûteuse en termes de calcul, car elle nécessite l'entraînement de plusieurs modèles à chaque niveau de validation croisée. |
| *Éviter le Surapprentissage* : Elle réduit le risque de surapprentissage en garantissant que les données de test ne sont jamais utilisées lors de la sélection des hyperparamètres.                                               | *Complexité* : La mise en œuvre de cette technique peut être complexe et nécessiter une gestion attentive des hyperparamètres et des plis.                                                    |
| *Optimisation des Hyperparamètres* : Elle permet une optimisation des hyperparamètres de manière systématique et rigoureuse.                                                                                                      |                                                                                                                                                                                               |


#### Bootstrap

Sous échantillonnage avec remise à répéter plusieurs fois (100 à 10000):![[bootstrap.png]]