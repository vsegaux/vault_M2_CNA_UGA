---
prof: DIARD Julien
date: 2025-11-18
publish: true
---
 
> [!NOTE] Examen
> 1 feuille manuscrite autorisée
> Site du prof, avec cours et TD: https://diard.wordpress.com/lectures

# Introduction

- Inattentional blindness 
	- Information is sensed but not perceived 
- Color from context 
	- Information is not processed veridically 
- Shape from image 
	- Necker cube
	- False perspective, Ames room 
	- Information is lacking: incompleteness: Les systèmes de traitement de l'information doivent inférer certains éléments pour pouvoir fonctionner.

# Theoretical foundations
## Artificial Intelligence
- AI 1:
- AI 2: Act like humans (Turing test)
- AI 3: Think rationally (Logic reasoning)
- AI 4:


Les modèles et robots créés sont forcément incomplets. Une solution est d'utiliser les probabilités comme un outil pour transformer l'incomplétude en incertitude.

## Règles de clacul
$$P(A\cap B) = P(A)P(B|A) = P(B)P(A|B)$$
**Théorème de Bayes**
$$P(B|A)=\frac{P(B)P(A|B)}{P(A)} si P(A) \neq 0$$
$$\sum_{A}P(A)=1$$
Règle de marginalisation:
$$\sum_{A}P(A\cap B)=P(B)$$
$$P(A\cup B) = P(A) + P(B) - P(A\cap B)$$


## Deux conceptions des probabilités


| Probabilité Fréquentistes                                                                                          | Probabilité subjectives                                                                                 |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------- |
| Une probabilité est une propriété d'un objet physique.                                                             | Une probabilité est une propriété d'un sujet qui observe un objet                                       |
| Statistiques classiques: population parente, tirage représentatif.. Calculer las probabilité de H0 n'a pas de sens | Pas de référence à la fréquence, pas de problème du nombre d'observation                                |
|                                                                                                                    | Statistiques bayesiennes: calcul des distributions de probabilité sur l'espace des paramètres           |
| Conception ontologique, **probabilité intrinsèques** P(A)                                                          | Conception épistémique, P("il pleut"\|Jean) ou P("il pleut"\|Pierre) -> **Probabilité conditionnelles** |

### Théorème:
Soit trois variables:
- S= S_1, ..., S_a
- F = F_1, ..., F_b
- K = K_1, ..., K_c

Si on connait la distribution conjointe P(S F K); on peut calculer P(S|K).

#### Démonstration
Avec P(K) $\neq$ 0:
$$P(S|K) = \sum_{F}P(S F|K) = \frac{\sum_FP(SFK)}{P(K)} = \frac{\sum_FP(SFK)}{\sum_{S,F}P(SFK)} = \frac{1}{Z}\sum_FP(SFK)$$

Si un modèle est très incomplet, il y aura beaucoup d'incertitudes. Si très complet, peu d'incertitudes. OK..

### Exemple minimal:
Raisonnement plausible:
- S'il pleut, alors Alise a son parapluie
- Alice a son parapluie
- Il pleut, vraisemblablement

Et ça donne quoi en probabilité?
1. *Deux variables:*
	- A= {il pleut, il ne pleut pas}
	- B= {Alice a son parapluie, Aline ne l'a pas}

2. *Modèle probabiliste sur ces variables:*
	- P(AB) = P(A)P(B|A)

3. *On défini les termes du modèles:*
	- P(A) 
		- P({A=Il pleut}) = 0.4
		- P({A= Il ne pleut pas}) = 1 - 0.4 = 0.6
	  P(B|A)
		- Quel objet mathématique?

| P(B\|A)                       | A=Il pleut | A=Il ne pleut pas |
| ----------------------------- | ---------- | ----------------- |
| B=Alice n'a pas son parapluie | 0.05       | 0.9               |
| B=Alice a son parapluie       | 0.95       | 0.1               |

*Attention:* P(B|A) n'est:
- Ni P(AB) (= somme à 1 sur les 4 cases, pas le cas ici!)
- Ni P(A|B) (=somme à 1 en ligne, pas le cas ici!)
Ici, ça somme à 1 sur les colonnes (P(B|A), la distribution de B peut être sommée à 1, dans toutes les conditions différentes de A). Note: si on écrivait P(A|B) dans ce tableau, les lignes devraient se sommer à 1.

On peut alors calculer: P(AB)= P(B|A)P(A)

| P(AB)                         | A=Il pleut | A=Il ne pleut pas |
| ----------------------------- | ---------- | ----------------- |
| B=Alice n'a pas son parapluie | 0.02       | 0.54              |
| B=Alice a son parapluie       | 0.38       | 0.06              |
Ici, la somme des 4 cases est bien égales ) 1. On a bien un distribution conjointe (P(AB)).
A partir de ce tableau, on peut retrouver P(A) à partir de la règle de marginalisation:
$P(A) = \sum_BP(AB)$ -> On somme les colonnes. De même, on peut obtenir P(B) par marginalisation en sommant les lignes: P(B=Alice n'as pas son parapluie)=0.56; P(B=Alice a son parapluie)=0.44); on remarque alors que la somme des probabilités de l'univers B vaut 1.

Finalement, quelle est la probabilité qu'il pleuve, sachant qu'Alice a son parapluie?
P($A_{pluie}$|$B_{parapluie}$): Par application du théorème de Bayes, puis règles de calculs de probabilités (marginalisation, conjointes)
![[apluie_bparapluie_calcul.png]]

Dans cet exemple, on a *3 paramètres libres* (Proba de pluie, proba de parapluie si pluie, proba de parapluie si non pluie), un pour chaque distribution de probabilité (les autres sont obtenus par règles mathématiques):
![[modele_exemple_pluie_parapluie.png]]


Définition d'un programme Bayésien complet:
![[prgm_bayesien.png]]

Une variable probabiliste doit être:
- exhaustive (Au moins un 'True' parmi ses valeurs possibles)
- mutuellement exclusive (Maximum un 'True')

Une distribution jointe peut être décomposées de plusieurs manières en applicant la règle des produits (Théorème de Bayes):
P(ABCD)=P(A)P(B|A) * P(C|BA) * P(D|CBA) 
Et celle-ci peut toujours être représentée dans une forme graphique:
![[Graphique_ABCD.png]]

> [!NOTE] Important examen
> Savoir décomposer selon les probas connues et les représenter dans un graphique. Attention à l'ordre des flèches.

### Indépendant et indépendance conditionnelle
![[inde_indeCond.png]]
*Attention, on peut avoir indépendance et pas indépendance conditionnelle et inversement!*

![[inde_NindeCond.png]]Et:
![[indeCond_Ninde.png]]


### Formes paramétriques
#### Loi de succession de Laplace
Pour représenter (histogramme typiquement) les probabilités d'une variable de prendre différentes valeurs, selon des observations expérimentales. Elle permet de gérer les cas où certaines valeurs n'ont pas encore été observées (pour pas que leur proba soit nulle par défaut). Par défaut, la distribution est uniforme, en l'absence d'observation.
$$\frac{n_i+1}{N+k}$$
Avec:
- $n_i$ observations réalisées
- N, nombre total d'observations
- k, valeurs possibles

### Apprentissage


### Inférences