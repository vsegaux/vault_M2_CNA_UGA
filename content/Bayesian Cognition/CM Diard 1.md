---
prof: DIARD Julien
date: 2025-11-18
publish: true
---

> [!NOTE] Examen
> 1 feuille manuscrite autorisée 
> Site du prof, avec cours et TD: https://diard.wordpress.com/lectures

# Introduction

## Illusions et perception

Le cerveau ne perçoit pas la réalité physique brute, mais réalise une **inférence** basée sur des informations sensorielles incomplètes.

- **Inattentional blindness (Cécité inattentionnelle)** :
    - _Information is sensed but not perceived._
    - On peut regarder quelque chose sans le voir si notre attention est focalisée ailleurs (ex: le gorille dans le jeu de passe).
- **Color from context** :
    - _Information is not processed veridically._
    - La perception de la couleur dépend du contexte (ex: illusion de l'échiquier d'Adelson). Le cerveau interprète la luminosité en fonction des ombres supposées.
- **Shape from image** :
    - Le système visuel infère la 3D à partir de la 2D.
    - **Cube de Necker** : Ambiguïté bistable (deux interprétations possibles pour la même image).        
    - **Chambre d'Ames** : Fausse perspective qui trompe notre prior sur la taille des objets/personnes.
    - **Conclusion** : L'information est manquante (**incomplétude**). Les systèmes de traitement de l'information (cerveau ou machine) doivent **inférer** les éléments manquants pour fonctionner.
        
# Fondements Théoriques

## Intelligence Artificielle (IA)

Classification des approches en IA (selon Russell & Norvig) :

- **IA 1 : Penser comme des humains** (_Think like humans_) -> Approche sciences cognitives.
- **IA 2 : Agir comme des humains** (_Act like humans_) -> Test de Turing.
- **IA 3 : Penser rationnellement** (_Think rationally_) -> Logique pure (Aristote).
- **IA 4 : Agir rationnellement** (_Act rationally_) -> Agent rationnel (le but est de prendre la meilleure décision, pas forcément comme un humain).
    
Problème fondamental : Le monde réel n'est pas un "monde de blocs" (monde fermé, logique). Il est incertain et continu.

Solution : Les modèles sont forcément incomplets. L'approche bayésienne utilise les probabilités comme outil pour transformer cette incomplétude structurelle en incertitude quantifiable.

## Considérations générales sur la modélisation

- **Attention aux lois normales** : Ne pas utiliser de loi normale pour modéliser des variables qui ne peuvent pas être négatives (ex: temps de réaction).
    - Les temps de réaction suivent souvent des lois _ex-Gaussian_ ou _Log-Normal_.
    - Utiliser une ANOVA (qui suppose la normalité) sur des temps de réaction est une erreur méthodologique courante en psychologie.
- **Théorème d'approximateur universel** : Avec suffisamment de gaussiennes (ou de neurones), on peut approximer n'importe quelle distribution.
    - _Danger_ : On tombe vite dans l'**overfitting** (sur-apprentissage) si le modèle est trop complexe pour les données.
        
## Règles de calcul probabiliste

Notation : $P(A)$ est la probabilité que la variable $A$ soit vraie.

Règle du produit (Conjointe) :

$$P(A \land B) = P(A)P(B|A) = P(B)P(A|B)$$

Théorème de Bayes (Inversion) :

$$P(B|A) = \frac{P(B)P(A|B)}{P(A)} \quad \text{si } P(A) \neq 0$$

Règle de la somme (Normalisation) :

$$\sum_{A}P(A)=1$$

Règle de marginalisation (Obtenir une variable seule à partir de la conjointe) :

$$P(B) = \sum_{A}P(A \land B)$$

Règle de l'union :

$$P(A \cup B) = P(A) + P(B) - P(A \land B)$$

## Deux conceptions des probabilités

| **Probabilités Fréquentistes**                                                                          | **Probabilités Subjectives (Bayésiennes)**                                                                    |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Propriété d'un **objet** physique (ex: un dé).                                                          | Propriété d'un **sujet** qui observe (degré de croyance).                                                     |
| Définie comme la limite de la fréquence d'un événement sur un grand nombre de tirages ($N \to \infty$). | Pas besoin de répétition. On peut évaluer la probabilité d'un événement unique (ex: "Il va pleuvoir demain"). |
| Conception **Ontologique**. $P(A)$ existe dans l'absolu.                                                | Conception **Épistémique**. Toujours conditionnelle à des connaissances : P(A\|Pierre) ou P(A\|Jean)          |
| Interdit de parler de probabilité sur une hypothèse ou un paramètre (soit vrai, soit faux).             | On calcule des distributions de probabilité sur l'espace des paramètres.                                      |

## Inférence Bayésienne : Définition formelle

Soit trois ensembles de variables :
- **S** (Search) : Les variables cherchées (Question).
- **F** (Free) : Les variables libres (ni connues, ni cherchées, on doit les "oublier" par sommation).
- **K** (Known) : Les variables connues (Observations).
    

Si on connait la **distribution conjointe** $P(S \land F \land K)$, on peut répondre à n'importe quelle question $P(S|K)$ :

#### Démonstration

> [!NOTE] Examen
> A connaitre


$$P(S|K) = \sum_{F}P(S \land F | K) = \frac{\sum_{F}P(S \land F \land K)}{P(K)}$$

Comme $P(K)$ est une constante de normalisation (indépendante de S), on écrit souvent :

$$P(S|K) = \frac{1}{Z} \sum_{F} P(S \land F \land K)$$

Note : Si le modèle est très incertain (distributions uniformes), l'inférence donnera des résultats plats. Si le modèle est très informé (Dirac), la réponse sera précise.

## Exemple minimal : Alice et son parapluie

**Problème** : On veut modéliser le raisonnement "S'il pleut, Alice a souvent son parapluie. Alice a son parapluie. Donc il pleut probablement."

**1. Variables :**
- $A \in \{\text{Pluie}, \text{PasPluie}\}$
- $B \in \{\text{Parapluie}, \text{PasParapluie}\}$
    
**2. Décomposition (Structure du modèle) :**

$$P(A \land B) = P(A)P(B|A)$$

**3. Formes Paramétriques (Données) :**
- **Prior** $P(A)$ :
    - $P(A=\text{Pluie}) = 0.4$
    - $P(A=\text{PasPluie}) = 0.6$
- **Vraisemblance** $P(B|A)$ (Modèle du comportement d'Alice) :

|**P(B\|A)**|**A=Pluie**|**A=PasPluie**|
|---|---|---|
|**B=PasParapluie**|0.05 (Erreur/Oubli)|0.9 (Normal)|
|**B=Parapluie**|0.95 (Logique)|0.1 (Précaution)|

_Attention aux sommes :_
- Dans $P(B|A)$, la somme doit faire 1 **par colonne** (pour chaque état de A, la somme des probas de B vaut 1).
- Ce n'est pas $P(A \land B)$ (somme totale à 1).
- Si on avait exprimé $P(A|B)$, la somme par ligne aurait du faire 1.

**4. Calcul de la Conjointe $P(A \land B)$ :**

On multiplie chaque case de $P(B|A)$ par le $P(A)$ correspondant.

|**P(AB)**|**A=Pluie (×0.4)**|**A=PasPluie (×0.6)**|
|---|---|---|
|**B=PasParapluie**|$0.05 \times 0.4 = \mathbf{0.02}$|$0.9 \times 0.6 = \mathbf{0.54}$|
|**B=Parapluie**|$0.95 \times 0.4 = \mathbf{0.38}$|$0.1 \times 0.6 = \mathbf{0.06}$|

_Vérification_ : $0.02 + 0.54 + 0.38 + 0.06 = 1$.

**5. Question (Inférence) :**

Quelle est la probabilité qu'il pleuve sachant qu'Alice a son parapluie ? $P(A=\text{Pluie} | B=\text{Parapluie})$.

$$P(A_{pl}|B_{par}) = \frac{P(A_{pl} \land B_{par})}{P(B_{par})} = \frac{P(A_{pl} \land B_{par})}{\sum_{A} P(A \land B_{par})}$$

Application numérique :

$$P(\text{Pluie}|\text{Parapluie}) = \frac{0.38}{0.38 + 0.06} = \frac{0.38}{0.44} \approx 0.86$$

Conclusion : L'observation du parapluie fait passer la croyance de pluie de 40% (prior) à 86% (posterior).

![[apluie_bparapluie_calcul.png]]

![[modele_exemple_pluie_parapluie.png]]

## Méthodologie : Programme Bayésien

Un programme bayésien se définit toujours selon cette structure :

1. **Description** :
    - **Variables** : Choisir les variables pertinentes ($X_1, ..., X_n$).
    - **Décomposition** : Écrire la conjointe $P(X_1...X_n)$ comme un produit de distributions plus simples (utilisation de l'indépendance conditionnelle).
    - **Formes Paramétriques** : Choisir les lois mathématiques pour chaque distribution (Uniforme, Gaussienne, Table...).
2. **Identification** : Fixer les valeurs des paramètres libres (Learning).
3. **Question** : Calculer une distribution conditionnelle $P(Search | Known)$.

![[prgm_bayesien.png]]

![[Programme_bayes_préci.png]]

> [!NOTE] Important examen
> 
> Savoir décomposer selon les probas connues et les représenter dans un graphique.
> 
> Règle : Si on écrit $P(A)P(B|A)P(C|B)$, les flèches vont de A vers B, et de B vers C.

![[Graphique_ABCD.png]]

### Indépendance vs Indépendance Conditionnelle

- **Indépendance** : $P(A \land B) = P(A)P(B)$ ou $P(A|B) = P(A)$. (A ne donne aucune info sur B).
- **Indépendance Conditionnelle** : $P(A|B \land C) = P(A|B)$. (Si je connais B, connaître C ne m'apprend rien de plus sur A).

![[inde_indeCond.png]]
Attention : L'un n'implique pas l'autre.
- Exemple Alice : Pluie et Imper sont dépendants. Mais conditionnellement à "Température", ils peuvent devenir indépendants.
![[inde_NindeCond.png]]![[indeCond_Ninde.png]]

### Formes Paramétriques

#### Loi de succession de Laplace

Utilisée pour estimer des probabilités à partir de comptages, en évitant les probabilités nulles si un événement n'a jamais été observé ("Add-one smoothing").

$$P(X=k) = \frac{n_k + 1}{N + K}$$
Où :
- $n_k$ : nombre d'observations de la valeur $k$.
- $N$ : nombre total d'observations.
- $K$ : nombre de valeurs possibles (cardinalité).
    Au départ (0 observation), la loi est Uniforme ($1/K$).
    
# Cours 2: Bayesian Robot Programming (BRP)

Application de la méthodologie pour contrôler un robot Khepera.

![[robot_Khepera.png]]

Capteurs : 8 Proximité (IR), 8 Lumière. Actionneurs : 2 roues ($V_{rot}, V_{trans}$).

## 1. Comportement de Phototaxie (Suivre la lumière)

Le robot doit s'orienter vers la lumière.
- **Variables** :
    - $ThetaL$ (Angle lumière, capteur) : 8 valeurs.
    - $V_{rot}$ (Vitesse rotation moteur) : 21 valeurs.
- **Décomposition** :
    - $P(ThetaL \land V_{rot}) = P(ThetaL) \times P(V_{rot} | ThetaL)$
- **Formes Paramétriques** :
    - $P(ThetaL)$ : Uniforme (tous les angles possibles a priori).
    - $P(V_{rot} | ThetaL)$ : **Gaussiennes**. Pour chaque angle de lumière perçu, on définit une gaussienne de vitesse centrée sur la réaction désirée (ex: si lumière à droite, vitesse de rotation positive).
- **Identification** : On fixe les moyennes/écarts-types des gaussiennes à la main ou par apprentissage.
![[phototaxy_program.png]]

## 2. Évitement d'obstacles (Pushing & Contour Following)

Deux comportements basés sur les mêmes variables mais avec des apprentissages différents.

![[pushing_objs.png]]

- **Variables** : $Dir$ (Direction obstacle), $Prox$ (Proximité), $V_{rot}$.
- Décomposition :$$P(Dir \land Prox \land V_{rot}) = P(Dir) P(Prox) P(V_{rot} | Dir \land Prox)$$
    Note : On suppose ici que $Dir$ et $Prox$ sont indépendants (c'est une hypothèse forte mais simplificatrice).
- **Comportement 1 : Pushing objects (Pousser)**
    - On apprend la distribution $P(V_{rot} | ...)$ avec des données où le robot pousse des objets.
    - Résultat : Si obstacle en face ($Dir=0$), $V_{rot}$ reste autour de 0 (=pas de delta entre gauche et droite).
- **Comportement 2 : Contour following (Longer les murs)**
    - On change juste le dataset d'apprentissage ($\delta_2$).
    - Résultat : Si obstacle en face, $V_{rot}$ commande de tourner pour mettre l'obstacle sur le côté.
![[gaussian_apprise_push_follow.png]]
L'image montre bien que pour les mêmes entrées (Dir, Prox), la distribution apprise de Vrot est différente.

## 3. Fusion de Capteurs (Sensor Fusion)

Comment savoir où est la lumière ($ThetaL, DistL$) à partir de 8 capteurs de lumière individuels ($Lm_0 ... Lm_7$) ?
Modèle individuel d'un capteur :
$P(Lm_i | ThetaL \land DistL)$. C'est une gaussienne. Si la lumière est en face du capteur et proche, $Lm_i$ est élevé. Sinon il est faible.

Modèle de Fusion :

On combine les 8 modèles.
$$P(ThetaL \land DistL | Lm_0...Lm_7) \propto P(ThetaL \land DistL) \times \prod_{i=0}^{7} P(Lm_i | ThetaL \land DistL)$$
C'est un produit de 8 distributions.

- **Résultat** : Même si chaque capteur est peu précis ("pourri"), le produit des 8 donne un pic de probabilité très fin et précis. L'incertitude diminue drastiquement.
    

![[fusion_model_resultats.png]]

## 4. Combinaison de comportements (Homing)

Le robot doit rentrer à la base (Phototaxie) tout en évitant les murs.

On introduit une variable interne H (Comportement) :

- $H \in \{\text{Phototaxie}, \text{Evitement}\}$.
- $P(H | Prox)$ : "Probabilistic If-Then-Else".
    - Si $Prox$ est élevé (obstacle proche), $P(H=\text{Evitement})$ devient proche de 1.
    - Sinon, $P(H=\text{Phototaxie})$ domine.
- Le moteur tire une vitesse qui est une somme pondérée par $P(H)$ des vitesses proposées par chaque sous-modèle.
![[homing_behaviour.png]]

# Cours 3: Bayesian Cognitive Modeling

## Apprentissage chez les enfants

Les enfants se comportent comme des statisticiens bayésiens dès le plus jeune âge.

### Expé 1 : Urne (Xu & Garcia, 2008)

- **Sujets** : Bébés de 8 mois.
- **Obs** : L'expérimentatrice tire 4 boules rouges et 1 blanche.
- **Test** : Elle montre le contenu de l'urne.
    - Condition cohérente : Urne majoritairement rouge.
    - Condition incohérente : Urne majoritairement blanche.
- **Résultat** : Les bébés regardent plus longtemps (surprise) la condition incohérente. Ils ont inféré la distribution cachée de l'urne à partir du petit échantillon.
- *Critique*: peut etre que les bébés réagissent simplement différemment à la vue de moyenne de couleur (blanche VS rouge).. Mais bon ça fait quand même une moyenne de couleur... ok...
![[expe_apprent_bayes.png]]

### Expé 2 : Blicket Detector (Gopnik et al.)
![[bayes_structure_enfant_30.png]]
- **Sujets** : 30 mois.
- **Tâche** : Déduire la structure causale (quel objet active la machine ?).
- **Phénomène "Backward Blocking"** :
    1. A et B sur la machine -> La machine sonne. (Hypothèses : A seul, B seul, ou A+B).
    2. A seul -> La machine sonne.
    3. Question : Est-ce que B est un "blicket" ?
    4. Réponse enfant : Non. (Le fait que A suffise "explique" le son en 1, donc la probabilité que B soit cause diminue).
- Cela prouve l'apprentissage de structures causales complexes, pas juste des associations.
    
## Perception et Psychophysique

### La sagesse des foules (et foule intérieure)

- **Wisdom of crowds** : La moyenne des estimations d'un groupe est souvent meilleure que les estimations individuelles (les erreurs s'annulent).
- **Inner Crowd (Vul & Pashler, 2008)** :
    - On demande à un sujet une estimation (Guess 1). Puis une seconde (Guess 2).
    - La moyenne quadratique (G1+G2)/2 est meilleure que G1 ou G2 seuls.
    - **Délai** : Si on attend 3 semaines entre G1 et G2, le gain est encore plus grand (car les échantillons sont plus indépendants, l'oubli a "décorrélé" l'erreur).
- Dans un casino, on demande à une foule de deviner le nombre de boule. Les sujets peuvent voter plusieurs fois (une fois par jour). L'experience a été répété 3 années consécutive.
	- L'erreur quadratique moyenne de chaque individu décroit de manière quadratique, mais tend vers un minimum, qui correspond au biais individuel. 
	- L'erreur quadratique moyenne de la foule, elle, tend vers 0.
![[crowd_wisdom.png]]

### Estimation des probabilités et Prospect Theory

Les humains évaluent mal les probabilités et les valeurs (Tversky & Kahneman).
1. **Aversion à la perte** : Perdre 100€ fait plus mal que gagner 100€ ne fait plaisir. (Courbe d'utilité asymétrique).
2. **Distorsion des probabilités** :
    - **Sous-estimation** des probabilités fortes (on traite 99% comme incertain).
    - **Sur-estimation** des probabilités faibles (on joue au loto comme si on avait une chance réelle).
![[proba_percu_proba_relle.png]]

![[perte_sensib_gain.png]]

### Négligence du taux de base (Base Rate Neglect)

Exemple classique du diagnostic médical (Eddy, 1982) :

- **Données** :
    - Prévalence Cancer $P(C) = 1\%$ (Prior).
    - Sensibilité Test $P(+|C) = 80\%$.
    - Faux Positifs $P(+|\neg C) = 9.6\%$.
- **Question** : Une patiente a un test positif. Proba qu'elle ait le cancer $P(C|+)$ ?
- **Réponse Médecins** : Souvent 75-80%.
- Réponse Bayésienne :    $$P(C|+) = \frac{P(+|C)P(C)}{P(+|C)P(C) + P(+|\neg C)P(\neg C)} = \frac{0.8 \times 0.01}{(0.8 \times 0.01) + (0.096 \times 0.99)} \approx 7.8\%$$
    L'erreur vient de l'oubli du prior (1% seulement de malades).
## Intégration Multisensorielle (Ernst & Banks, 2002)

> [!NOTE] Examen
> 
> Étude de cas fondamentale. À connaître parfaitement.

Problème : Estimer la hauteur d'une barre en utilisant la Vision (V) et le Toucher (Haptique, H).

Les deux sens sont bruités (Gaussiennes de variances $\sigma_V^2$ et $\sigma_H^2$).

Modèle Bayésien (MLE) :

Le cerveau combine les deux estimations pour minimiser l'erreur (variance). L'estimation combinée est une somme pondérée :

$$\hat{S}_{VH} = w_V \hat{S}_V + w_H \hat{S}_H$$

Avec les poids inversement proportionnels aux variances (on fait plus confiance au sens le plus précis) :

$$w_V = \frac{1/\sigma_V^2}{1/\sigma_V^2 + 1/\sigma_H^2}$$

Résultat fondamental (Variance optimale) :

La variance combinée est inférieure à la variance de chaque sens pris isolément.

$$\sigma_{VH}^2 = \frac{\sigma_V^2 \sigma_H^2}{\sigma_V^2 + \sigma_H^2} \le \min(\sigma_V^2, \sigma_H^2)$$
> [!NOTE] Examen
> Démonstration potentiellement demandée à l'examen: 
> 

Démontrer : $\sigma_{VH}^2 <= \sigma_V$ et <= $\sigma_H$ 
Avec $\sigma_{VH}^{2}= \frac{\sigma_V^2\sigma_H^2}{\sigma_V^2+\sigma_H^2}$


**Expérience** :
- Ils introduisent du bruit artificiel dans la vision.
- **Prédiction** : Si la vision devient floue (bruit augmente), $w_V$ doit diminuer et $w_H$ augmenter. Le sujet doit se fier davantage au toucher ("Haptic capture").
- **Données** : Les humains se comportent exactement comme prédit par l'optimalité bayésienne.
![[multi_modal_result.png]]

[[Ernst&Banks en détail]]

## Inférence Causale

Quand on entend un son et voit un flash, viennent-ils de la même source ($C=1$) ou de deux sources différentes ($C=2$) ? ![[expe_visu_audit_.png]]
- Le cerveau calcule la probabilité de $C=1$ vs $C=2$ (Inférence causale).
- Si les stimuli sont proches dans l'espace/temps -> Fusion ($C=1$).
- Si trop éloignés -> Ségrégation ($C=2$).
- Le modèle de Körding (2007) montre que le cerveau réalise cette inférence de structure causale à la volée.
# Part IV: Sélection de Modèles

Comment choisir le meilleur modèle ?

Ce n'est pas celui qui "fit" le mieux les données (car risque d'overfitting), mais celui qui généralise le mieux.

## Le Rasoir d'Ockham

En modélisation : À pouvoir explicatif égal, on préfère le modèle le plus simple.

## Complexité vs Généralisation

- Un modèle trop simple **sous-apprend** (Underfitting).
- Un modèle trop complexe **sur-apprend** (Overfitting) : il apprend le bruit des données expérimentales au lieu de la loi physique.
- Le "Sweet Spot" est l'équilibre entre complexité et fidélité aux données.

![[generalisation_risk_2nd_courbe.png]]

## Méthodes de sélection

1. **Cross-Validation (Validation croisée)** :
    - On coupe les données en 2 : Entraînement (80%) / Test (20%).
    - On estime les paramètres sur l'entraînement, on évalue l'erreur sur le Test.
    - Cela simule la capacité de généralisation.
2. **Critères Bayésiens** :
    - Le **Facteur de Bayes** ou l'**Evidence** ($P(Data | Model)$) pénalise naturellement les modèles complexes. Un modèle complexe "dilue" sa probabilité sur un immense espace de données possibles. Un modèle simple concentre sa probabilité. C'est le **Rasoir d'Ockham Automatique**.
        
# Astuces Mathématiques

- Log-vraisemblance :
    
    Pour éviter les erreurs numériques (underflow) quand on multiplie beaucoup de petites probabilités (ex: Sensor Fusion), on travaille avec les logarithmes :
    
    $$\log(P(A)P(B)) = \log P(A) + \log P(B)$$
    
    Le produit devient une somme.
    
- Odds (Cotes) :
    [video explicative](https://www.youtube.com/watch?v=lG4VkPoG3ko)
    Plutôt que des probabilités, on utilise des ratios.
    
    $$Odds(A) = \frac{P(A)}{P(\neg A)}$$
    
    Forme Odds du théorème de Bayes :
    
    $$\text{Posterior Odds} = \text{Likelihood Ratio} \times \text{Prior Odds}$$
    
    ![[odds_proba_.png]]