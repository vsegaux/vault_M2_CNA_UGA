---
sujet: Modèles de mémoires
prof: GRANDCHAMP Romain
date: 2025-09-23
publish: true
---
## 1. Fondamentaux et Terminologie
- **Big Data (3V)** : Volume (quantité), Vélocité (vitesse), Variété (formats divers).
- **Data vs Information vs Connaissance** :
    - **Donnée** : Observation brute (ex: 40°C).
    - **Information** : Donnée contextualisée ("il fait très chaud").
    - **Connaissance** : Information intégrée pour agir ("ajuster le refroidissement").
- **IA vs ML vs DL** :
    - **IA** : Agir, raisonner, décider de façon autonome.
    - **Machine Learning (ML)** : Apprendre à partir des données sans programmation explicite.
    - **Deep Learning (DL)** : Sous-catégorie du ML utilisant des réseaux de neurones profonds.
- **Test de Turing** : Évalue si une machine peut se faire passer pour un humain via le NLP, le raisonnement, et l'apprentissage.
## 2. Types d'Apprentissage

| **Type**           | **Fonctionnement**                                                           | **Exemples d'algorithmes**                                    |
| ------------------ | ---------------------------------------------------------------------------- | ------------------------------------------------------------- |
| **Supervisé**      | Prédire à partir de données étiquetées (input/output connus)                 | k-NN, SVM, Régression linéaire/logistique, Arbres de décision |
| **Non supervisé**  | Explorer et découvrir des structures cachées dans des données non étiquetées | K-means, PCA, Clustering hiérarchique, t-SNE                  |
| **Renforcement**   | Apprentissage par essai-erreur via un système de récompenses/pénalités.      | AlphaGo, robotique (apprendre à marcher).                     |
| **Semi-supervisé** | Mélange de peu de données étiquetées et beaucoup de données brutes.          | -                                                             |

## 3. Modèles Linéaires vs Non Linéaires

- **Modèle Linéaire** : Suppose une relation proportionnelle  
    - **Avantages** : Interprétable, rapide, moins de surapprentissage.
    - **Exemples** : Régression linéaire, SVM linéaire, Régression logistique.
- **Modèle Non Linéaire** : Capture des relations complexes ou courbes.
    - **Avantages** : Très flexible, s'adapte à des motifs riches.
    - **Inconvénients** : Risque élevé de surapprentissage, plus difficile à interpréter.
    - **Exemples** : KNN, Arbres de décision, Réseaux de neurones, K-means.
## 4. Compromis Biais-Variance et Surapprentissage
- **Équation d'erreur** : Erreur totale = Biais² + Variance + Erreur irréductible. (Avec Biais: écart à la réalité; variance: sensibilité aux variations de données)
- **Biais élevé (Sous-apprentissage)** : Modèle trop simple. _Solution : Complexifier, ajouter des features_
- **Variance élevée (Surapprentissage / Overfitting)** : Modèle trop sensible au bruit des données d'entraînement. _Signe : Erreur faible en training, forte en test_. 
**Comment éviter le surapprentissage ?** 
- **Validation croisée (k-fold)** : Tester sur différents "plis" de données.
- **Régularisation** : Ridge (L2 - pénalise les grands coefficients) ou Lasso (L1 - favorise la parcimonie)    
- **Simplification** : Appliquer le rasoir d'Occam (le plus simple est le mieux).
- **Data Augmentation** : Créer des données synthétiques (bruit, rotations, SMOTE, GANs)
## 5. Prétraitement et Workflow
**Normalisation obligatoire pour :** KNN, SVM, K-means, Réseaux de neurones.
- **Standardisation (Z-score)** : Moyenne=0, Écart-type=1. Idéal pour modèles linéaires et PCA
- **Normalisation (Min-Max)** : Valeurs entre 0 et 1. Idéal pour méthodes basées sur la distance (KNN).
- **Partitionnement** : Training set (paramètres), Validation set (hyperparamètres), Test set (évaluation finale).
## 6. Mesures de Performance
- **Matrice de Confusion** : Compare les prédictions (TP, TN) aux erreurs (FP, FN).
- **Accuracy** : Attention, trompeuse si les classes sont déséquilibrées.
- **Sensibilité (Recall / TPR)** : Capacité à détecter les positifs.
- **Spécificité (TNR)** : Capacité à détecter les négatifs.
- **ROC / AUC** : Courbe TPR vs FPR. L'AUC (Aire sous la courbe) juge la performance globale : 0.5 = hasard, 0.9 = excellent.
## 7. Principes des Algorithmes
- **k-NN** : Un point prend la classe de ses K voisins les plus proches (distance euclidienne). _Petit k = variance, Grand k = biais_
- **SVM** : Trouve l'hyperplan avec la marge maximale. Utilise des "kernels" pour le non-linéaire. Paramètre C : grand C = surapprentissage
- **Arbres de décision** : Règles "Si... Alors...". Très interprétables mais instables. **Forêts aléatoires** : Moyenne de plusieurs arbres pour réduire la variance.
- **K-means** : Partitionne en K clusters sphériques via des centroïdes. Nécessite de fixer K à l'avance.
- **PCA (Composantes Principales)** : Réduction de dimension linéaire en projetant les données.
- **Naive Bayes** : Basé sur le théorème de Bayes, suppose l'indépendance des features. Très rapide pour le texte/spam