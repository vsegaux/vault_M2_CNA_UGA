---
sujet: Modèles de mémoires
prof: GRANDCHAMP Romain
date: 2025-09-23
publish: true
---


> [!NOTE] Examen
> Notions à retenir:
> - Linéaire / Non linéaire
> - Supervisé = prédire / Non supervisé = explorer.
> - Biais ↔ Variance = compromis à gérer.
> - Notion de surapprentissage et comment l'éviter.
> - Normaliser avant KNN, SVM, K-means.
> - ROC/AUC pour juger la performance globale d’un classifieur.
> - Accuracy ≠ toujours fiable, regarder sensibilité/spécificité selon le contexte.
> - Quel type d'algorithme utiliser selon les données d'entrée.

# Domaines mis en jeu

- **Statistiques** : quantifier et décrire des observations.
    
- **Data Mining** : découvrir des motifs ou structures sous-jacentes dans les données.
    
- **Machine Learning (ML)** : prédire à partir de modèles appris.
    
- **Intelligence Artificielle (IA)** : agir, raisonner et prendre des décisions de manière autonome.
    

# Terminologie

- **Big Data** : données massives caractérisées par les **3V** :
    
    - **Volume** : quantité de données.
        
    - **Vélocité** : vitesse d’arrivée ou de production des données.
        
    - **Variété** : diversité des formats (texte, image, audio, JSON, etc.).
        
- **Machine Learning (ML)** : apprentissage automatique à partir de données, sans programmation explicite.
    
- **Pattern Recognition** : reconnaissance de motifs ou structures caractéristiques.
    
- **Data Mining** : fouille de données (terme historique, ancêtre du ML).
    
- **Deep Learning (DL)** : sous-catégorie du ML utilisant des réseaux de neurones profonds.
    
- **Agent** : entité capable de percevoir et d’agir.
    
- **Agent rationnel** : agent agissant pour maximiser sa réussite dans une tâche donnée.
    

**Terminologie croisée :**

- En _ML_, la cible s’appelle un **label**.
    
- En _statistiques_, c’est une **variable dépendante**.
    
- Une **feature** en ML = une **variable** en statistiques.
    
- Une **feature creation** en ML = une **transformation** en statistiques.
    


## Donnée – Information – Connaissance

- **Donnée** : observation brute (ex. température, âge, temps de réaction).
    
- **Information** : signification contextualisée d’une donnée (ex. “40°C = très chaud”).
    
- **Connaissance** : information intégrée dans un raisonnement ou une expérience (ex. “à 35°C, ajuster le système de refroidissement”).
    

# IA et apprentissage

![[AI_ML_DL.png]]

|Type d'apprentissage|Supervisé|Non supervisé|Par renforcement|
|---|---|---|---|
|**Description**|Données étiquetées (on connaît la réponse).Exemples : prédiction, classification, régression.|Données non étiquetées : l’algorithme découvre les structures cachées (clustering, réduction de dimension, estimation de distributions).|L’agent apprend par essai-erreur via une **récompense** (performance, score, gain, etc.).|
|**Exemples**|k-NN, régression linéaire, reconnaissance de chiffres manuscrits.|K-means, segmentation de clientèle, détection de motifs.|AlphaGo, robots apprenant à marcher.|
|**Avantages**|Efficace avec des étiquettes et relations claires.|Aucune étiquette nécessaire, utile pour grands ensembles.|Permet un apprentissage autonome basé sur la performance.|
|**Inconvénients**|Nécessite beaucoup de données annotées.|Résultats plus difficiles à interpréter.|Lent, dépend des signaux de récompense.|

> _Le Deep Learning correspond à une méthode d’implémentation (réseaux de neurones), pas à un type d’apprentissage._


# Notion d’intelligence

**Définition (Atkinson)** : capacité à comprendre un contexte nouveau et à y réagir de manière adaptée.  
Points communs entre les différentes définitions :

- Apprendre et s’adapter à l’inconnu.
    
- Établir des liens et reconnaître des formes.
    
- Tirer des conclusions de contextes nouveaux.
    

### Ce que l’IA sait / ne sait pas faire :

|Capable de|Pas encore capable de|
|---|---|
|Traitement du langage naturel|Conscience, émotions|
|Automatisation industrielle|Jugement moral/éthique|
|Jeux complexes (Go, échecs, etc.)|Créativité authentique|
|Diagnostic médical assisté|Compréhension profonde|
|Reconnaissance d’images|Adaptation totale à l’inconnu|
|Prédiction, recommandation|Autonomie totale|

> **IA généralisée** : une IA capable de transférer ses apprentissages d’un domaine à un autre.


# Qu’est-ce que l’IA ?

|Perspective|Fidélité à l’humain|Performance|
|---|---|---|
|**Raisonnement (interne)**|_Penser comme un humain_ : automatisation de la prise de décision et du raisonnement.|_Penser rationnellement_ : formalisation computationnelle du raisonnement.|
|**Comportement (externe)**|_Agir comme un humain_ : imitation du comportement humain observable.|_Agir rationnellement_ : conception d’agents intelligents rationnels.|

Deux approches :

- **Comportementale** : imiter les actions humaines efficacement.
    
- **Cognitive** : imiter la manière dont un humain raisonne.
    

## Thinking humanly

Pour comprendre la pensée humaine :

- **Top-down** : tester des théories cognitives à partir du comportement observé.
    
- **Bottom-up** : identification de modèles directement à partir des données neuronales.
    

### Test de Turing

Évalue si une machine peut se faire passer pour un humain dans une conversation.  
Compétences nécessaires :

- **NLP (Natural Language Processing)**
    
- **Représentation des connaissances**
    
- **Raisonnement automatique**
    
- **Apprentissage machine**
    

Pour une version plus avancée :

- **Vision par ordinateur**
    
- **Robotique**
    

# Domaines et types de problèmes en IA

- **Systèmes experts** : raisonnement logique à base de règles.
    
- **Vie artificielle** : reproduction, auto-réparation.
    
- **Algorithmes bio-inspirés** : ex. algorithmes génétiques (sélection naturelle de solutions).
    
- **Systèmes multi-agents** : comportements collectifs complexes émergeant de règles simples (_émergence_).
    

### Types de problèmes

- **Classification** : attribuer à une catégorie.
    
- **Régression** : prédire une valeur continue.
    
- **Clustering** : regrouper des éléments similaires.
    
- **Association** : trouver des corrélations.
    
- **Détection d’anomalies** : repérer les cas atypiques.
    

# Notions fondamentales du Machine Learning

## Fléau de la dimensionnalité

Plus on ajoute de variables, plus le volume de l’espace croît exponentiellement → les données deviennent “éparses”.  
Conséquence : les modèles nécessitent beaucoup plus d’échantillons pour rester fiables.

## Motifs aléatoires

_Principe de Bonferroni_ : plus on teste de relations, plus on risque de trouver des corrélations purement aléatoires.


## Linéaire vs Non linéaire

### Modèle linéaire
Un **modèle linéaire** suppose une relation **proportionnelle** entre les variables d’entrée (features) et la sortie (target).

**Formule générale :**  
$$\hat{y} = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_n x_n  $$
- Une transformation des données (log, exp, polynomiale) peut rendre un problème non linéaire **linéarisable**.

![[linearire.png]]

> En ajoutant des termes d’ordre supérieur, on peut modéliser la complexité, mais attention au **surapprentissage**.

![[overfitting.png]]


**Exemples :**

- Régression linéaire
    
- SVM linéaire
    
- Régression logistique (linéaire sur un espace transformé)
    

**Avantages :**

- Interprétable et rapide à entraîner.
    
- Moins sujet au surapprentissage.
    

**Limites :**

- Ne capture pas les relations complexes (non linéaires).


### Modèle non linéaire

Un **modèle non linéaire** capture des relations **courbes, complexes ou interactives** entre variables.

**Exemples :**

- Arbres de décision / Random Forests
    
- KNN
    
- Réseaux de neurones
    
- K-means (non linéaire dans la structure des données)
    

**Avantages :**

- Grande flexibilité, s’adapte à des motifs complexes.
    

**Inconvénients :**

- Risque élevé de surapprentissage.
    
- Interprétation plus difficile.
    

## Types d'apprentissage
![[supervise.png]]
### Apprentissage supervisé
L’algorithme apprend à partir de **paires (entrée → sortie)** connues.

**Exemples de tâches :**

- Classification (ex. spam / non-spam)
    
- Régression (ex. prédire un prix, une température)
    

**Algorithmes :**

- Régression linéaire / logistique
    
- SVM
    
- KNN
    
- Arbres de décision
    
- Naive Bayes

### Apprentissage non supervisé
Aucune sortie (label) connue.  
L’objectif est de **découvrir des structures cachées** dans les données.

**Exemples de tâches :**

- Clustering (regroupement)
    
- Réduction de dimension
    
- Détection d’anomalies
    

**Algorithmes :**

- K-means
    
- Affinity Propagation
    
- Clustering hiérarchique
    
- Manifold learning (PCA, t-SNE, UMAP)


## Compromis Biais – Variance

- **Erreur totale** = Biais² + Variance + Erreur irréductible
    
- **Biais** :  Le biais mesure *à quel point les prédictions du modèle s'écartent de la vraie* valeur (c'est-à-dire, la moyenne des prédictions par rapport à la moyenne des vraies valeurs).
	Simplification excessive → sous-apprentissage.
    
- **Variance** : La variance mesure *la sensibilité du modèle aux variations des données d'entraînement*.
	Trop grande sensibilité aux données → surapprentissage.
    
- **Erreur irréductible** : bruit aléatoire non modélisable.
    

![[biais-variance.png]]  
![[err_complex.png]]

> ⚖️ Objectif : trouver l’équilibre optimal entre biais et variance (bonne généralisation).


|Terme|Description|Effet typique|Solutions|
|---|---|---|---|
|**Biais élevé**|Modèle trop simple (apprend mal les motifs)|Sous-apprentissage|Complexifier le modèle, plus de features.|
|**Variance élevée**|Modèle trop sensible aux données|Surapprentissage|Régularisation, plus de données, modèles plus simples.|

**Impact selon les algorithmes :**

- **Haute variance** → KNN (petit k), arbre profond, SVM avec grand C.
    
- **Haut biais** → régression linéaire, KNN avec grand k, SVM avec petit C.

## Surapprentissage (Overfitting)
**Définition :**  
Le modèle apprend **trop fidèlement les données d’entraînement**, y compris le bruit, et perd sa capacité à généraliser.

**Signes :**

- Erreur faible sur le training set.
    
- Erreur forte sur le test set.
    

### Comment l’éviter ?

- **Validation croisée (k-fold)**
    
- **Régularisation** (Introduction de pénalité sur les modèles trop complexes:
	- **Ridge (L2)** : pénalise les grands coefficients.
    
	- **Lasso (L1)** : favorise la parcimonie (certains coefficients deviennent 0).
	    
	- **Elastic Net** : combinaison des deux.
    
- **Simplifier le modèle** (Occam: Entre deux modèles équivalents, on choisit toujours le plus simple.).
    
- **Arrêt anticipé (early stopping)** pour réseaux de neurones.
    
- **Augmentation de données**.
    
- **Dropout / bagging / ensemble learning.**
    

# Workflow du Machine Learning

## Prétraitement des données

**Objectifs :**

- Uniformiser les échelles de mesure.
    
- Améliorer la visualisation et la comparabilité.
    
- Préparer les données pour les algorithmes sensibles à la distance.
    

### Principales transformations

- **Standardisation** :  
    $$z = \frac{x - \mu}{\sigma}$$
    → Moyenne = 0, Écart-type = 1.  
    Utilisée pour : régression linéaire, SVM, K-means; qui sont sensibles à la distribution des données.
    
- **Normalisation** :  
    $$x' = \frac{x - x_{min}}{x_{max} - x_{min}}$$ 
    → Valeurs entre 0 et 1.  
    Utile pour réseaux de neurones, KNN, méthodes basées sur distances; souvent basés sur des données dont les gammes sont très variées.
    
- **Mise à l’échelle (scaling)** : généralisation des deux précédentes.
    

### Autres prétraitements

- Encodage des variables catégorielles (ex. _One Hot Encoding_).
    
- Discrétisation, binarisation, imputation des valeurs manquantes.
    

![[résumé.png]]

## Généralisation et Partitionnement

> Ne jamais tester un modèle sur des données vues à l’entraînement.

- **Training set** : apprentissage des paramètres.
    
- **Validation set** : réglage des hyperparamètres.
    
- **Test set** : évaluation finale.
    
### Validation croisée à k-plis

Recherche d'hyperparamètres sur différents plis des données d'entrainement puis test avec les meilleurs paramètres. Chaque 'split' dans la figure suivante correspond à un set d'hyperparamètres:
![[validation_croisee_inner.png]]

> k = 5 à 10 selon la taille du jeu de données.

| Pros                                                                                                                                                                                             | Cons                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| *Évaluation Robuste* : Elle permet d'obtenir une estimation plus fiable des performances du modèle en utilisant plusieurs itérations de validation.                                              | *Coût Computationnel* : La validation croisée interne peut être coûteuse en termes de calcul, car plusieurs modèles doivent être entraînés et évalués.                                           |
| *Réduction du Risque de Surapprentissage* : En évaluant le modèle sur des sous-ensembles de données, elle aide à réduire le risque que le modèle ne soit trop ajusté aux données d'entraînement. | *Complexité* : La gestion des hyperparamètres et des différentes combinaisons peut rendre le processus complexe et difficile à gérer, surtout pour des modèles avec de nombreux hyperparamètres. |
| *Optimisation des Hyperparamètres* : Elle facilite l'optimisation des hyperparamètres en fournissant une méthode systématique pour tester différentes configurations.                            |                                                                                                                                                                                                  |

#### Validation croisée imbriquée

La boucle interne permet l'optimisation d'hyperparamètres, c'est dans cette boucle, que chaque ligne (orange sur la figure ci-dessous) correspond à un set d'hyperparamètres.
![[nested_CV.png]]

> Sépare l’optimisation d’hyperparamètres (interne) de l’évaluation finale (externe).  
> Plus coûteuse mais plus fiable.

| Pros                                                                                                                                                                                                                              | Cons                                                                                                                                                                                          |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Estimation Précise de la Performance* : En séparant la sélection des hyperparamètres et l'évaluation des performances, la validation croisée imbriquée fournit une estimation plus précise de la performance générale du modèle. | *Coût Computationnel Élevé* : La validation croisée imbriquée est coûteuse en termes de calcul, car elle nécessite l'entraînement de plusieurs modèles à chaque niveau de validation croisée. |
| *Éviter le Surapprentissage* : Elle réduit le risque de surapprentissage en garantissant que les données de test ne sont jamais utilisées lors de la sélection des hyperparamètres.                                               | *Complexité* : La mise en œuvre de cette technique peut être complexe et nécessiter une gestion attentive des hyperparamètres et des plis.                                                    |
| *Optimisation des Hyperparamètres* : Elle permet une optimisation des hyperparamètres de manière systématique et rigoureuse.                                                                                                      |                                                                                                                                                                                               |

### Bootstrap

![[bootstrap.png]]

- Tirage avec remise (de 100 à 10000 fois).
    
- Permet d’évaluer la stabilité d’un modèle sur de multiples sous-échantillons.
    

| Taille du jeu de données   | >1000                              | Petit                                                                     |
| -------------------------- | ---------------------------------- | ------------------------------------------------------------------------- |
| Partitionnement recommendé | Classique après brassage aléatoire | - Validation croisée à 5 ou 10 plis<br>- Bootstrap répété 100 à 1000 fois |


## Augmentation de données
Permet d'augmenter la taille/variété du jeu de donnée, à partir d'un jeu initialement limité. Différentes méthodes existent:

1. **Ajout de bruit** : améliore la généralisation.
	Ex: En image, léger flou, variation de luminosité; en texte: synonymes aléatoires, suppression de mots rares...
    
2. **Transformations réalistes** : création de nouvelles données réalistes.
	Ex: rotation, miroir, décalage temporel, modification du ton...
    
3. **Synthèse artificielle** :
    
	- *SMOTE* (Synthetic Minority Oversampling Technique): Creer de nouveux exemples de la classe minoritaire pour équilibrer les classes
	- *GANs* (Generative Adversarial Networks): génèrent des donnés réalists à partir du modèle (image ou texte souvent)
	- *VAE* (Variational Autoencoders) Apprennent une distribution latente pour produire des exemples plausibles
        
4. **Mélange d’échantillons** :
    
    - _Mixup_: combiner aléatoirement deux exemples et leurs étiquettes: créer des points intermédiares pour lisser la frontière de décision
    - _CutMix_, _Cutout_.
        
## Sélection et réduction d’attributs

### Sélection d’attributs
 - Pour faciliter le travail de l'algorithme 
 - Pour trier les attributs importants dans l'analyse supervisée et obtenir un modèle plus simple (rasoir d'occam) 
 
Réduire la dimension sans altérer les variables :

- Suppression d’attributs peu informatifs (faible variance).
    
- Tests statistiques (χ², corrélation).
    
- Rejet des attributs trop corrélés entre eux.
    

### Extraction d’attributs

Transformation des données brutes en features exploitables.  
Exemple : _Bag of Words_ pour le texte: un échantillon est un document, un attribut la fréquence d'un« token » et la matrice celle d'un corpus de documents

### Réduction de dimension

- **Feature Agglomeration** : regroupe des attributs similaires.
    
- **PCA / t-SNE / UMAP** : projections dans un espace réduit.
    

## Vérification de la robustesse

Un bon modèle :

- Généralise sur différents sous-ensembles.
    
- Est stable et peu sensible aux fluctuations.
    
- Donne des résultats cohérents sur des échantillons différents.
    

# Mesures de performance
## Matrice de confusion

|     | -                        | +                        |
| --- | ------------------------ | ------------------------ |
| -   | True Negatives (**TN**)  | False Negatives (**FN**) |
| +   | False positives (**FP**) | True positives (**TP**)  |

## Accuracy

$$Accuracy=\frac{TP + TN}{TP + TN + FP + FN} $$  
Elle correspond à la proportion correcte globale.

## Sensibilité / Spécificité

- **Sensibilité (Recall, TPR)** : capacité à détecter les vrais positifs  
    $$\frac{TP}{TP + FN}  $$
- **Spécificité (TNR)** : capacité à détecter les vrais négatifs  
    $$\frac{TN}{TN + FP}  $$

## Courbe ROC et AUC

**ROC (Receiver Operating Characteristic)** :
- Représente le compromis entre **TPR (sensibilité)** et **FPR (1 - spécificité)**.
    
- Aire sous la courbe (Area Under the Curve AUC) ∈ [0,1].
    
    - 0.5 : hasard
        
    - > 0.9 : excellente performance
        
- Permet de comparer des modèles indépendamment du seuil choisi.
    

![[ROC_AUC.png]]


Plus la courbe suit la bordure gauche et la bordure supérieure, plus le test est précis.
Plus la courbe est proche de la diagonale, moins le test est précis.

# Principes des principaux algorithmes

## K-Nearest Neighbors (KNN)

- Principe : un point est classé selon les **k voisins les plus proches**.
    
- Mesure : distance euclidienne (ou autre).
    
- **Pas de phase d’entraînement réelle**, mais prédiction lente si grand dataset.
    

**Paramètres :**

- k : nombre de voisins (petit → bruit, grand → biais)
    
- Poids des distances possibles.
    

**Sensible à :**

- Normalisation (indispensable).
    
- Données bruitées.
    

Exemples:
![[knn_nonlineare.png]]Les **frontières de décision** observées pour la classification (figure de gauche) ne sont **pas linéaires**, ce qui montre que le modèle s’adapte à des formes complexes.

En **régression**, lorsque les **poids sont uniformes** (figure de droite, en haut), la prédiction correspond à la **moyenne des 5 points voisins** (fenêtre glissante).

En revanche, si les **poids dépendent de la distance** (figure de droite, en bas), les **points les plus proches** influencent davantage la prédiction. Ce mode donne en général une **courbe de prédiction plus fidèle aux données réelles**, mais il présente aussi un **risque plus élevé de surapprentissage**, car le modèle devient trop sensible aux variations locales.
## Support Vector Machine (SVM)

- Trouve l’**hyperplan** séparant au mieux les classes, avec **marge maximale**.
    
- Fonctionne en linéaire ou avec **noyaux (kernel)** pour non-linéaire.  ![[svm_diff_kernel.png]]
    

**Paramètres :**

- **C** : contrôle la pénalité des erreurs (grand → surapprentissage). ![[SVM_C_value.png]]
    

**Sensible à :**

- Normalisation obligatoire.
    

## Régression linéaire

- Modélise une relation linéaire entre variables.
    
- Objectif : minimiser l’erreur quadratique moyenne (MSE).
    

**Régularisations :**

- Ridge (L2), Lasso (L1), Elastic Net.
    

**Sensible à :**

- Outliers (points extrêmes).
    

### Régression logistique

- Utilisée pour la **classification binaire**.
    
- Sortie : probabilité entre 0 et 1.
    

$$P(y=1|x)= \frac{1}{1+e^{-(\beta_{0}+\beta_1x_1+...+\beta_px_p)}}$$
**Avantages :**

- Interprétable, rapide, robuste.
    

## Arbre de décision

- Divise les données selon des **règles conditionnelles** (ex. “si température > 30°C…”).
    
- Facile à interpréter, mais instable et sensibles à la balance des classes.
    

**Forêts aléatoires :**

- Moyenne de plusieurs arbres aléatoires.
    
- Moins de variance, meilleur pouvoir prédictif.
    

## K-means

- Partitionne les données en **k clusters** en minimisant la distance intra-cluster.
    
- Chaque cluster a un **centroïde** moyen.
    

**Paramètre :**

- k (nombre de clusters) → fixé à l’avance.
    

**Limites :**

- Sensible aux valeurs initiales et à l’échelle.
    
- Suppose des clusters sphériques.
    

## Affinity Propagation

- Pas besoin de fixer k, le nombre de cluster est définit par l'algorithme.
    
- Plutôt adapté aux petits jeux de données.
## Clustering hiérarchique

- Regroupe les points **de proche en proche** (agglomératif, bottom-up) ou les **divise** (divisif, top-down).
    
- Produit un **dendrogramme** (arbre) visualisant la structure hiérarchique.
    

**Avantages :**

- Interprétable visuellement.
    


## Manifold Learning

- Objectif : **projeter les données** d’un espace complexe vers un espace plus simple tout en préservant les distances locales.
    

**Méthodes de projection :**

- **PCA (linéaire)** (Projection en Composantes Principales)
- **Isomap**
- **Aléatoire**

**Utilité :**

- Visualisation 2D/3D, réduction de dimension avant apprentissage.
    

## Naive Bayes

- Basé sur le **théorème de Bayes** en supposant l’**indépendance des features**.
    
- Très rapide et efficace pour le texte, le filtrage de spam, etc.
    
$$P(x_i|y)=\frac{1}{\sqrt{2\pi\sigma_y^2}} e^{\frac{-(x_i-\mu_y)^2}{2\sigma_y^2}}$$
