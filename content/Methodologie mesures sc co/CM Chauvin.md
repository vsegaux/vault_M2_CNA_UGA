---
sujet: Methodo Mesures
prof: CHAUVIN Alan
date: 2025-09-17
publish: true
---

> [!NOTE] Examen  
> Article(s) à interpréter → VI, VD, VC, Résultats, Analyse critique

# La Méthode Expérimentale

## Définition générale

La méthode expérimentale vise à **étudier l’influence d’une variable (VI)** sur une autre (**VD**), tout en **contrôlant les variables parasites (VC)**.  
Le but est d’établir un **lien de causalité** : si la VI varie, la VD change-t-elle de manière significative ?

## Variable indépendante (VI)

Variable dont on cherche à **vérifier l’influence sur la VD** (le comportement ou la performance observée).  
Elle représente la **cause supposée** du phénomène étudié.

### Caractéristiques :

- Possède **plusieurs modalités** (souvent 2 ou 3).
    
- Peut être de **nature différente** :
    
    - **Provoquée** : sa valeur est imposée par l’expérimentateur.  
        → ex. condition de test, quantité d’alcool donnée.
        
    - **Invoquée** : sa valeur est propre aux participants.  
        → ex. niveau d’anxiété, âge, couleur des yeux.
        

## Variable dépendante (VD)

Variable mesurée, censée refléter l’effet de la VI.  
C’est **l’objet de la mesure** dans l’expérience.

### Échelles de mesure (Stevens, 1946)

| Type           | Nature                         | Exemples                       | Mesure                            |
| -------------- | ------------------------------ | ------------------------------ | --------------------------------- |
| **Nominale**   | Catégorielle, sans ordre       | Sexe, Catégorie Socio-Pro      | Effectif, Mode, χ²                |
| **Ordinale**   | Ordre sans intervalle constant | Classement, échelle de douleur | Médiane, quantiles                |
| **Intervalle** | Ordre + écart constant         | Température, score de test     | Moyenne, écart-type               |
| **Rapport**    | Intervalle + zéro absolu       | Temps de réaction, vitesse     | Moyenne, coefficient de variation |

→ Le **type d’échelle** détermine le **modèle d’analyse statistique** (gaussien, binomial, multinomial, etc.).

### Qualités psychométriques d’une bonne VD :

1. **Validité** : mesure réellement ce qu’elle prétend mesurer.
    
2. **Sensibilité** : détecte de faibles variations.
    
3. **Fidélité** : stabilité dans le temps (faible erreur de mesure).
    
4. **Objectivité** : indépendante de l’expérimentateur (standardisation).
    

## Variable contrôle (VC)

Source d’influence **potentielle** sur la VD, non étudiée pour elle-même, mais **contrôlée** pour éviter la confusion avec la VI.

### Types de contrôle :

- **Fixé** : même valeur pour tous les sujets (ex. durée constante du test).
    
- **Aléatoire** : distribution aléatoire des sujets dans les conditions → neutralise les différences individuelles.
    
- **Contrebalancé** : chaque sujet passe toutes les conditions, mais dans un ordre différent.
    

### Types de VC selon leur nature :

- **Invoquée** : propriété intrinsèque des participants (ex. genre, anxiété).
    
- **Provoquée** : manipulation expérimentale (ex. ordre de présentation, contexte sonore).
    

> Objectif : respecter le principe **« toute chose égale par ailleurs »**.

## Hypothèses

### Hypothèse nulle ($H_0$)

Affirme **l’absence d’effet** de la VI sur la VD :  
$$ H_0 : \mu_1 = \mu_2 $$  
→ La variabilité observée est due au **hasard** (distribution *normale* attendue).

### Hypothèse alternative ($H_1$)

Affirme **l’existence d’un effet** :  
$$ H_1 : \mu_1 \neq \mu_2 $$

Les deux hypothèses sont **complémentaires** : rejeter $H_0$ revient à accepter $H_1$.

## P-value et seuil alpha (α)

- **P-value** : probabilité, _sous H₀_, d’obtenir un résultat au moins aussi extrême que celui observé.
    
- **Seuil α** : niveau de risque que l’on accepte de prendre pour rejeter H₀ (souvent **0.05**).
    

### Décision :

- Si _p ≤ α_ → effet **significatif** → rejet de H₀.
    
- Si _p > α_ → effet **non significatif** → on conserve H₀.
    

> Diminuer α réduit les faux positifs mais **augmente les faux négatifs** (perte de puissance).


## Types d’effets

- **Effet principal** : effet d’une VI sur la VD, indépendamment des autres VI.
    
- **Effet d’interaction** : effet combiné de plusieurs VI → la variation de la VD dépend de la combinaison des VI.
    
- **Effet simple** : effet d’une VI pour un seul niveau d’une autre VI.
    

## Taille d’effet

Permet d’évaluer **l’ampleur réelle** de la différence observée. C'est _une mesure de la force de l'effet observé d'une variable sur une autre_.

- **d de Cohen** :  
    $$ d = \frac{M_1 - M_2}{S_p} $$  
    où $S_p$ est l’écart-type pondéré.
    
- Relation avec la statistique t :  
    $$ t = \sqrt{n} \times d = \frac{M_1 - M_2}{S_p / \sqrt{n}} $$
    


## Erreurs de décision

- **Erreur de type I (α)** : rejet à tort de H₀ → _faux positif_.
    
- **Erreur de type II (β)** : non-rejet de H₀ alors qu’elle est fausse → _faux négatif_.
    

> La **puissance statistique** d’un test = 1 − β → probabilité de détecter un effet réel.

## Plan d’expérience

Le plan définit la structure de l’étude (VI, VD, VC, nombre de sujets, passation...).

| Plan             | Description                              | Notation      | Exemple                     |
| ---------------- | ---------------------------------------- | ------------- | --------------------------- |
| **Inter-sujets** | Chaque sujet dans une seule condition    | `S < A >`     | 10 sujets par condition     |
| **Intra-sujets** | Chaque sujet passe toutes les conditions | `S * A`       | 10 sujets × 2 conditions    |
| **Mixte**        | Combinaison intra/inter                  | `S < A > * B` | 2 VI : une intra, une inter |
    

> Le plan conditionne entièrement l’analyse statistique.


## Hypothèses pour les tests statistiques

1. **Normalité** : les résidus doivent suivre une loi normale.  
    → Vérifié via Q-Q plot (si points alignés = normalité respectée).  
    → Sinon : transformation (ex. log).
    
2. **Indépendance** : les observations ne doivent pas être corrélées entre elles.
    
3. **Homogénéité des variances** : variances égales entre groupes.  
    → Sinon : utiliser **test de Welch** ou **test U de Mann–Whitney** (non paramétrique, sans interaction possible).
    

## Population et échantillon

- **Population** : ensemble complet des individus concernés par la recherche.
    
- **Échantillon** : sous-ensemble de la population, choisi pour être représentatif.  
    → On suppose un échantillonnage **aléatoire indépendant et identiquement distribué (a.i.i.d.)**.
    

> [!NOTE]  
> Un échantillon _a.i.i.d._ signifie que chaque individu est sélectionné :
> 
> - **indépendamment** des autres ;
>     
> - selon la **même loi de probabilité** que les autres (identiquement distribués).
>
## Validité des recherches

- **Validité interne** : le changement observé dans la VD est bien dû à la VI (et non à un facteur externe).
    
- **Validité externe** : possibilité de **généraliser** les résultats à d’autres populations, contextes ou situations.
    

## Test t de Student

Permet de comparer des **moyennes** entre deux groupes.

### Formule :

t=$\frac{M_1 - M_2}{S_p / \sqrt{n}}$

- Si $t$ observé dépasse la valeur critique (table Student) → rejet de H₀.
    
- **Unilatéral** : hypothèse directionnelle (effet dans un sens).
    
- **Bilatéral** : test des deux directions possibles.


# Étude de cas : Agressivité et alcool (Zerhouni et al., 2013)

### Question

L’agressivité liée à l’alcool est-elle **uniquement d’origine pharmacologique**  
ou aussi influencée par **la croyance d’avoir bu** ?

### Plan expérimental

- **Participants** : 117 hommes, 18–44 ans.
    
- **VI1 (provoquée)** : quantité d’alcool **consommée** (nulle, faible, forte).
    
- **VI2 (provoquée)** : quantité d’alcool **attendue** (nulle, faible, forte).
    
- **VD** : quantité de **sel et tabasco** donnée à un provocateur (mesure d’agressivité).
    

###  Hypothèse :

→ L’agressivité dépend à la fois de l’effet pharmacologique _et_ de la croyance d’avoir bu.

###  Résultats

|Attente|Aucune|Faible|Importante|Moyenne|
|---|---|---|---|---|
|Aucune|5.25|4.44|4.45|4.73|
|Faible|6.95|6.47|7.32|6.91|
|Importante|9.86|8.54|8.89|9.11|

Après test T pour comparer les moyennes:    
→ Effet **significatif de l’alcool attendu**, mais pas de l’alcool consommé.  
→ Interaction non significative.

###  Interprétation :

> L’exposition à des indices liés à l’alcool suffit à **augmenter l’agressivité**,  
> même sans consommation réelle (effet non pharmacologique).