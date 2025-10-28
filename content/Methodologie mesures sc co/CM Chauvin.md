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
![[Variable indépendante (VI)]]
## Variable dépendante (VD)
![[Variable dépendante (VD)]]
## Variable contrôle (VC)
![[Variable contrôle (VC)]]
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
![[P-value et seuil alpha (α)]]
## Types d’effets
![[Types d’effets]]

## Taille d’effet
![[Taille d’effet]]
## Erreurs de décision

- **Erreur de type I (α)** : rejet à tort de H₀ → _faux positif_.
    
- **Erreur de type II (β)** : non-rejet de H₀ alors qu’elle est fausse → _faux négatif_.
    

> La **puissance statistique** d’un test = 1 − β → probabilité de détecter un effet réel.

## Plan d’expérience
![[Plan d’expérience]]
## Hypothèses pour les tests statistiques
![[Hypothèses pour les tests statistiques]]
## Population et échantillon
![[Population et échantillon]]
## Validité des recherches
![[Validité des recherches]]
## Test t de Student
![[Test t de Student]]
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