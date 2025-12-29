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


## Considérations générales
Attention à ne pas utiliser de loi normales pour modéliser des éléments non continus. Souvent typiquement pas applicable aux temps de réponses (car un temps ne peut pas être négatif), attention aux Anova en psycho...! **A expliquer mieux...**
Il existe d'autres fonctions pour le faire.

Théorème d'approximateur universel: le cadre mathématique peut tout approximer avec des distributions de probabilités. Mais on tombe vite dans l'overfitting.

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

Plus précisément:
![[Programme_bayes_préci.png]]


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

![[forme_parametrique.png]]
Ces expressions indiquent simplement qu'on peut exprimer une distribution de probabilité selon/en fonction d'autres distributions de probabilités basées sur d'autres modèles (typiquement plus petits).

### Questions
Given a description, a question is obtained by partitioning the set of variables into 3 subsets: the searched variables (not empty), the known variables and the free variables. We define the Search, Known and Free as the conjunctions of the variables belonging to these three sets. We define the corresponding question as the distribution: 
- P (Search | Known ∧ δ ∧ π
- Pour y répondre:
	- For instance, compute P(X1 X2 | X4 $\delta$  $\pi$) OR compute first P(X1 | X4 $\delta$ $\pi$ ) then P(X2 | X4 $\delta$  $\pi$ )? Le principe général est que:
	- If you know the joint probability distribution P(X1 X2 … Xn) then any question P(xi … xj | xk … xl) can be computed


A partir d'une distribution de probabilité P(X|Y), on peut réaliser 2 opérations:
- *Tirer* aléatoirement un échantillon x selon la distribution P(X|Y)
- *Calculer* la probabilité P({X=x}|Y), c'est à dire, pour une valeur donnée, calculer la probabilité de l'observer selon la distribution.


## Panorama of Bayesian modeling frameworks
Dans les slides.. il va très vite qu'il dit.. !
### Recursive bayesian filters
Décomposition: $$\prod_{i=1}^{T}P(S_i|S_{i-1})P(O_i|S_i)$$
Visuellement, avec X et Y plutot que respectivement S et O:
![[recursive_bayes.png]]

Les questions sont alors typiquement: P($S_{t+k}|O_0...O_t$ )=P($S_{t+k}|O_{0:t}$) 
$$= P(O_t|S_{t}) * \sum\limits_{S_{t-1}}P(S_t|S_{t-1})P(S_{t-1}|O_{0:t-1})$$
$$=Observation * (Prédictions;simulation du système)$$


# Cours 2: Bayesian Robot Programming
## Learning reactive behaviors

![[robot_Khepera.png]]
- 8 capteurs de proximité infrarouge (IR)
- 8 capteurs de lumière
- 2 roues, liées à deux moteurs indépendants

### Phototaxy behavior
Premier cas simple, le robot s'oriente et va vers la lumière. Le programme bayesien est défini selon:
![[phototaxy_program.png]]

Spécification:
- Variables:
	- ThetaL: {-170, -90, -45, -10, +10, +45, +90, +170}, 8 valeurs possibles, angle de la source lumineuse
	- Vrot: {-10..+10}, 21 valeurs possibles, vitesse de rotation
	- 8 * 21 valeurs possibles.
	- Nombres de paramètres libres: 8 * 21 - 1.
- Décomposition:
	- P(ThetaL Vrot | $\pi_{Photo}$) = P(ThetaL | $\pi_{Photo}$) P(Vrot | ThetaL $\pi_{Photo}$)
- Formes paramétriques:
	- P(ThetaL | $\pi_{Photo}$) -> Uniform, 8 valeurs possibles donc 1/8 chance pour chacune
	- P(Vrot | $\pi_{Photo}$) -> Gaussienne, 8 gaussiennes différentes, une pour chaque valeur de ThetaL, elles sont imposées pour pouvoir réaliser le comportement attendu.
- Calcul:
	- P(Vrot | ThetaL $\pi_{Photo}$)

### Pousser des obstacles
![[pushing_objs.png]]

Décomposition:
P(Dir Prox  Vrot |   $\pi_{wall}$)
= P(Dir | $\delta$  $\pi_{wall}$)P(Prox | Dir $\delta$  $\pi_{wall}$)P(Vrot | Dir  Prox  $\delta$  $\pi_{wall}$) 
Les simplifications suivantes sont dues à des indépendances conditionnelles (spécifiques au modèle ici, par exemple: la direction ne dépend pas du delta (arbitraire ok, mais ça marche...))
= P(Dir | $\delta$  $\pi_{wall}$)P(Prox | $\delta$  $\pi_{wall}$)P(Vrot | Dir  Prox  $\delta$  $\pi_{wall}$) 
= P(Dir | $\pi_{wall}$)P(Prox | $\pi_{wall}$)P(Vrot | Dir  Prox  $\delta$  $\pi_{wall}$)
$\delta$ correspond à un jeu de données expérimentales.
A partir de cette dernière équations, les formes paramétriques sont les suivantes:
P(Dir | $\pi_{wall}$) -> Uniformes (ne dépend de rien), 21 valeurs possibles
P(Prox | $\pi_{wall}$) -> Uniforme (pareil), 16 valeurs possibles
P(Vrot | Dir  Prox  $\delta$  $\pi_{wall}$) -> Gaussienne, *(2 * )* 16 * 21 valeurs possibles (x2 car il y a deux paramètres par gaussienne), avec $\mu = f_1(\delta); \sigma = f_2(\delta)$


![[gaussian_apprises.png]]

### Contour following
![[contour_follow__.png]]
Ici, les paramètres (variables) sont les memes. Mais l'objectif est différent, le jeu de données expérimentale est différent, matérialisé par $\delta_2$:
La décomposition prend finalement la forme (calcul similaire à l'exemple précedent):
= P(Dir | $\pi_{wall}$)P(Prox | $\pi_{wall}$)P(Vrot | Dir  Prox  $\delta2$  $\pi_{wall}$)

Avec ce nouveau jeu de données expérimentales, les gaussiennes apprises sont différentes:
![[gaussian_apprise_push_follow.png]]
En pushing, on veut maintenir l'objet en face, donc la rotation à 0 lorsque la direction est 0. En following, on veut le maintenir sur le côté.


## Sensor fusion 

### Catégorisation perceptive
![[bayes_categ_percep.png]]
L'objectif est de catégoriser la distance de la lumière: proche ou loin.

La décomposition peut s'écrire:
P(DistL ^ C | $\delta_3$ ^ $\pi_{cat}$) 
= P(C | $\pi_{cat}$)P(DistL | C ^ $\delta_3$ ^ $\pi_{cat}$)

En termes de formes paramétriques:
P(C | $\pi_{cat}$) -> Distribution discrète (dans une table)
P(DistL | C ^ $\delta_3$ ^ $\pi_{cat}$) -> Gaussiennes, la gaussienne pour C=proche a typiquement une moyenne plus faible de DistL; celle pour C=loin, typiquement une moyenne plus grande de DistL.

La question est donc de déterminer:
P(C| {DIstL=d} ^ $\delta_3$ ^ $\pi_{cat}$). On a par défaut, 31 distributions binaires possible (31 valeur de distance, pour 2 catégories.)

![[distL_Category.png]]

Si les gaussiennes se croisent plusieurs fois, on peut avoir des artéfacts dans les probabilités de catégorisations:
![[artefact_categori.png]]


### Fusion de capteurs
On commence par réaliser le modèle d'un seul capteur:
![[model_light_sensor.png]]
La mesure Lm correspond à 0 si la lumière est présente et bien en face, 500 si aucune lumière n'est détectée.

### Fusion
On réalise un modèle qui interroge les 8 modèles précédemment formulés:
![[sensor_fusion.png]]
Il a dont 10 variables: ThetaL, DistL et les 8 $Lm_x$ des différents capteurs.
Dans la *décomposition*, on a 36 * 31 * 501^7 possibilités pour les gaussiennes par défaut.
Mais on peut faire des hypothèse conditionnelles: pour connaitre des infos sur chaque capteur, on a besoin que de ThetaL et DistL, pas réellement de l'infos des autres capteurs, on peut donc simplifier toutes les informations $Lm_x$.

Finalement, le calcul revient à 9 termes: P(ThetaL DistL) * P($Lm_{0-7}$|ThetaL DistL).

En terme de résultat, avec 8 modèles "pourris", on obtient au final une capacité de discrimination très précise en les fusionnant tous:
![[fusion_model_resultats.png]]



## Object recognition, home recognition 

![[object_recog.png]]
Variables:
- Les objets sont caractérisés par O={1,2,3...}
- Nlt Number of left turn
- Nrt right turns
- Per perimeter
- Llsl longueur du segment linéaire le plus long

Parametrical forms:
- Laplace succession laws
	- Pour un objet nouveau, on n'a pas de connaissance au départ. Par défaut, on y associe des distributions uniformes pour toutes les grandeurs sensorielles (Nlt, Nlr, Per, Llsl)
	- Pour les objets connus, on peut associer des approx. discretes de Gaussiennes

## Behavior combination 

Objectif:
- Retourner à la base
- Eviter les obstacles sur le chemin

Variables:
- Direction de la base,
- Proximité à un obstacle
- ThethalL l'angle de la lumière
- Vrot la rotation des roues
- H: comportement: évitement ou phototaxie (aller vers la lumière)

![[homing_behaviour.png]]
Parametrical form:
- La proba de H selon la proximité est définie comme une fonction 'sigmoide', dont la forme est donnée sur la figure ci-dessus (on ne voit que la distribution de P(H=Evitement|prox), car elle est complémentaire à celle de P(H=Phototaxie|prox)).


## Integration: nightwatchman Khepera 

Dans un modèle complexe, plusieurs solutions sont possibles:
- Inférence exacte 
	- sommation, propagation des incertitudes 
- Inférence approximée 
	- *décisions intermédiaires* (tirage de points), propagation d’une partie des incertitudes
	- On tire une ou quelques valeurs plutôt que de propager et faire tous les calculs avec les probabilités.

# Part III: Bayesian cognitive modeling
## Bayesian modeling of cognition: generalities

## Apprentissage bayésien chez les enfants
### Expe 1
- Enfants de 8 mois
- ![[expe_apprent_bayes.png]]
- L'experimentatrice pioche des boules dans une urne, elle en a déjà piocher des rouges, elle en tire une blanche, puis une rouge
- On ouvre ensuite l'urne et on observe la réaction de l'enfant dans les deux conditions:
	- L'urne contient une vaste majorité de boules blanches
	- L'urne contient une vaste majorité de boules rouges
- On observe que les bébés sont stupéfaits à la découverte de l'urne majoritairement blanche. Il y aurait donc bien des traces d'estimations de probabilités chez les enfants déjà à 8 mois.
- Critique: peut etre que les bébés réagissent simplement différemment à la vue de moyenne de couleur (blanche VS rouge).. Mais bon ça fait quand même une moyenne de couleur... ok...


### Expe 2
- Enfants de 30 mois
- ![[bayes_structure_enfant_30.png]]
- Certains objets sont référencés par le label "blicket" (pseudomot que l'enfant ne connait pas). On lui apprend qu'il y a un détecteur de blicket qui sonne lorsqu'un blicket est déposé dessus. Dans différentes conditions telles que spécifiées dans l'image ci-dessus.
	- En la condition (b), il y a des incertitudes dans la réponse des enfants.
- Les auteurs déduisent que les enfants apprennent des structures causales à partir d'observations.

## Bayesian modeling of perception
### Expé 3
Le but est de regarder l'évolution de l'erreur quadratique moyenne en agrégeant les réponses d'un même sujet. On leur pose des questions de cultures générales pendant une première séance, en double dans cette unique séance (guess 1 et guess 2 sur l'image ci-dessous). Puis une nouvelle fois 3 semaines après.
![[bayesian_sampling.png]]

En moyenne, le guess 2 est moins bon que le guess 1. Mais la moyenne quadratique de l'erreur aux deux première réponse est plus faible. On retrouve cet effet, et même amplifié dans le cas où la deuxième évaluation est faite après 3 semaines (du fait de la meilleur indépendance entre les 'guess').


### Expé 4
Dans un casino, on demande à une foule de deviner le nombre de boule. Les sujets peuvent voter plusieurs fois (une fois par jour). L'experience a été répété 3 années consécutive.

Les graphes suivants montrent les sujets qui sont venu 5, 10 ou plus de fois (ligne 1, 2, et 3 respectivement).
![[crowd_wisdom.png]]

- L'erreur quadratique moyenne de chaque individu décroit de manière quadratique, mais tend vers un minimum, qui correspond au biais individuel. 
- L'erreur quadratique moyenne de la foule, elle, tend vers 0.

### Estimation cognitive de probabilités
Des comportements « erronés » dans le raisonnement sous incertitude : 
- Je vous donne 3000$ (option A), ou bien 4000$ à 80% de chance (option B) ? 
	- .8x4000=3200€, le calcul de l’espérance de gain (gain moyen par expérience si on la répétait) est en faveur de l’option B 
	- Expérience : 80% des sujets choisissent l’option A, 20% l’option B (le 80% est une coïncidence numérique) 
- Vous devez payer 3000€ (option A), ou bien 4000$ avec 80% de chance 
	- 8% des sujets choisissent l’option A, 92% l’option B
[vidéo YT d'un mec stylé sur le sujet](https://www.youtube.com/watch?v=MCg2lw4Nxno)

Un agent économique parfait resterait sur la droite suivante, les biais observés en réalité sont représentés sur la courbe en S:
![[perte_sensib_gain.png]]

A espérance égale:
- Gagner 6000$ à 45% (A) ou 3000$ à 90% (B) 
	- 14% des sujets choisissent A, 86% B –
- Gagner 6000$ à 0,1% (A) ou 3000$ à 0,2% (B) 
	- 73% des sujets choisissent A, 27% choisissent B
	- Les gens préfèrent avoir moins de chance de gagner de très grosses sommes, à chances faibles.
	- Typiquement au loto:
		- Payer 1$ sûrement pour avoir 1 chance sur 1 000 000 de gagner 1 000 000$ 
			- Perte certaine de 1€, gain incertain de 1€ en moyenne.
- ![[proba_percu_proba_relle.png]]
- *Sous-estimation des probabilités faibles*
- *Sur-estimation des probabilités fortes*


Conclusion : ce qu’on observe comportementalement, c’est le résultat de l’estimation des probabilités (qui n’est pas parfaite) combiné à un processus de décision (qui n’est pas parfait
- La « prospect theory » de Tversky & Kahneman est bien une théorie de la prise de décision, mais on perçoit mal les probabilités et les utilités 
Mais : Attention, on ne retrouve pas la mauvaise représentation des probabilités dans les tâches sensorimotrices 
- Hypothèse 1 : 
	- Cognition consciente : sériel, lent, inférence bayésienne approximée 
	- Cognition périphérique : rapide, parallèle, inférence bayésienne exacte (ou moins approximée) 
- Hypothèse 2 : internalisation des données 
	- Transfert verbal à format interne peut-être en défaut


### Expé 5
Les sujets doivent viser le cercle vert, ils gagnent de l'argent en visant dans le cercle vert (et ignorer le cercle rouge dans une des conditions). Dans la seconde condition, le cercle rouge fait perdre de l'argent.
On remarque que les sujets sont très bons pour estimer leur biais et décaler de manière optimale leurs essais vers le rond vert, pour ne plus toucher le rond rouge.

![[cercle_vertRouge_gainPerte.png]]


### Expe 6

- Example tested on physicians 
	- The probability of breast cancer is 1 % for a woman at age forty who participates in routine screening. If a woman has breast cancer, the probability is 80% that she will get a positive mammography. If a woman does not have breast cancer, the probability is 9.6% that she will also get a positive mammography. A woman in this age group had a positive mammography in a routine screening. What is the probability that she actually has breast cancer? 
- Eddy (1982) reported that 95 out of 100 physicians estimated the posterior probability to be between 70% and 80%
- La vraie réponse par le calcul est 7.8%: ![[cancer_test_calcul.png]]
- Le prior (cancer à 1% de chance) a une grande influence sur la valeur finale!
- Explication possible de l'erreur comise par les médecins (physicians):
	- 95 out of 100 physicians estimated the posterior probability to be between 70% and 80% 
	- 0.8 / (0.8+0.096) = 0.89 
	- Their error “looks like” forgetting the prior probability 
	- Base rate neglect error (aka base rate fallacy)

**Variante**:
- Example tested on physicians 
	- The probability of breast cancer is 1 % for a woman at age forty who participates in routine screening. If a woman has breast cancer, the probability is 80% that she will get a positive mammography. If a woman does not have breast cancer, the probability is 9.6% that she will also get a positive mammography. A woman in this age group had a positive mammography in a routine screening. What is the probability that she actually has breast cancer? 
- Another formulation of the same problem 
	- Consider 1,000 women, 10 of whom have breast cancer. Of those 10, 8 would get a positive mammography. Of the 990 not afflicted, 95 would also get a positive mammography. A woman is screened, and her mammography turns out positive. What is the probability that she actually has breast cancer? 
- Answer
	- 8 / (8 + 95), which is certainly a small number! (= 7.8%)


## Modélisation de la perception

### Inversion et ambiguités

![[inverion_amigu.png]]
Avec $S_n$ les informations sensorielles, et V le stimulus. Dans l'inversion, on s'intéresse à la probabilité du stimuli, sachant les observations qui ont été faites.

#### Expe 1
![[expe_1_oeuf_dans_boite.png]]
A priori il y a 5 oeufs dans cette boite, mais si on retourne l'image la réponse donnée serait plutot 1 oeuf.
Le prior ici est que la lumière vient du dessus. Il y a beaucoup de prior similaires:
- Light comes from above 
- Light is stationary 
- Viewpoint is above the scene 
- Contours follow statistics of natural scene 
- Object perception favors 
	- regular geometrical shapes, convex geometrical shapes 
- Face perception favors convex faces 
- Movement perception favors 
	- Rigid objects, low translation and rotation speeds 
- Body movement perception favors 
	- Low rotation speeds, upright positions


#### Expe 2
![[oeuf_complexe.png]]
Dans la figure C, c'est simplement une réplication de l'expérience précédente, la réponse est donnée selon la direction de la provenance de la lumière. Dans les autres figure A,B et D, les scènes visuelles autour des différents points d'interets donnes des informations de la direction de la lumière de manière plus globale.


#### Expe 3
Une boule se déplace sur un échiquier, selon la position de son ombre, son déplacement est perçu quand dans un plan équidistant de l'observateur, ou en profondeur etc...
![[boule_en_3D.png]]
En réalité, la boule suit systématiquement la même trajectoire, le système visuel se base quasi-exclusivement sur les indices d'ombre.

#### Expe 4
Necker cube, plusieurs interpretation de la même image selon les prior.
![[necker_cube.png]]
Certains on une probabilité très faible (les formes géométriques 'régulières' sont favorisées: cube, triangle etc...)


### Body movement peception
Selon certaines situations de mouvements (rotation inégale entre la tete et les pieds), le prior d'axe vertical est modifié: les sujets ne sont plus capables d'indiquer l'axe vertical (dans le noir).


### Ambiguité et bistabilité
Selon l'attention, on peut voir l'une ou l'autre version stable d'une image:
![[bistable_B_13.png]]

- On ne peut pas voir à la fois le B et le 13.
- Les changements d'une interprétation à l'autre prennent quelques secondes.

### Combinaison
Apprendre à catégoriser à partir de données très "sparse".
Expérience:
- You come out of your spaceship on planet Ix, eager to explore. You meet three lively dudes. They tell you that they are three “Tufas”.![[planet_X_tufa.png]]
- They show you the way to a village. They tell you that Tufas live there, but not only. In the village square, eight other dudes hang out. Do you think some of them are Tufas? If yes, which ones are Tufas?: ![[tufasvillage.png]]

Comment modéliser ça mathématiquement?
- **Model assumptions**:
	- Hypothesis space: trees; samples are leaves, word labels are nodes 
	- Prior: favors nodes down the tree (smaller branch length has higher probability) 
	- Likelihood: 
	1. Assume no error in sample labels 
	2. Assume that samples are drawn randomly from the branch, favoring lower branches (highly suspicious that all samples would happen to be packed in a sub-tree)
- Posterior probability favors generalizing across the lowest branch that spans all the observed samples

![[arbre_categ_bayes.png]]
La taches de catégorisation revient à associer un nom à un noeud de l'arbre.

#### Apprentissage des structures
On part de principes abstraits à des structures générale, à finalement les données, aussi diverses qu'elles soient.



## Multi-cue and multi-model perception

### Modèle de pondération linéaire
Un stimuli donne lieu à plusieurs **estimations** selon différentes **fonctions de transfert**. Et l'estimation finale est obtenue par **somme pondérée** des différentes estimations:
![[pondération_linéaire.png]]

A partir de ce type de modèle, on peut modéliser des comportements d'adaptation (re-calibrage; donc de modification des fonctions de transferts) et des comportements de sélection (re-podération; donc de modification des poids attribués aux différentes estimations).

[[Ernst&Banks en détail]]
#### Modèle bayésien de fusion de capteurs
![[haptic_visu_naive_bayes.png]]
Dans la définition de ce modèle, le prior est uniforme (P(X) = U(X) peut prendre n'importe quelle valeur avec autant de chance: on a aucune information sur la taille de la barre à priori.
![[hapti_visio_bayes_compute.png]]
On en revient alors finalement à exprimer la taille prédite en fonction des deux capteurs comme un produit des deux distributions Gaussiennes (visuelle et haptique). Or un produit de gaussienne est aussi une gaussienne, dont la variance est forcément inférieure à celles de chacune des modalités.

> [!NOTE] Examen
> Démonstration potentiellement demandée à l'examen: 
> 

Démontrer : $\sigma_{VH}^2 <= \sigma_V$ et <= $\sigma_H$ 
Avec $\sigma_{VH}^{2}= \frac{\sigma_V^2\sigma_H^2}{\sigma_V^2+\sigma_H^2}$

Le papier est nommé 'Statistically optimal' car justement cette variance recombinée est inférieure à la variance de chaque capteur.


#### Comparaison du modèle aux données
![[comparaison_model_donnee_vis_hapt.png]]
On compare les PSE et les JND prédis avec ceux observés dans les données:
![[compa_effective_.png]]
Petite différence dans le cas à 200% de bruit. Autre représentation:
![[comparaison_pred_donne_2.png]]


### Aperture effect
![[aperture_effect.png]]
Dans le champ recepteur de la rétine, lors de vision par une petite ouverture, on est capable de donner la direction de mouvement, mais il y a une forte ambiguité sur la vitesse de déplacement de l'objet.
Pour un autre capteur qui voit un morceau différent de l'objet, il va avoir sa propre distribution de vitesse déduite.

Lors de l'intégration de plusieurs capteurs, la plus grande probabilité de vitesse de déplacement se trouve normalement bien placée. En cas de contraste moins marqué, la perception de la vitesse est biaisée.

### Inférence causale
Y a t il une source unique, ou deux sources distinctes? On utilise deux modèles différents, que l'on compare à la volée.
- un premier modèle qui mélange (ie qui part du principe qu'il n'y a qu'une source)
- un second modèle qui ségrégue (ie qui part du principe qu'il y a deux sources distinctes)

On parle de source visuelles et auditives, qui viennent de différentes positions derrière un écran:
![[expe_visu_audit_.png]]
En terme de courbes de réponses:
![[audit_visuel_reposne.png]]

On part de plusieurs modèles:
- C=2: modèle ségrégatoire totale
- C=1: modèle intégratoire totale
- C inconnue: modèle d'inférence causale, on tire sur C
- D'après les résultats de Körding KP, Beierholm U, Ma WJ, Quartz S, ... 2007, le modèle d'inférence causale est supérieur aux autres.

## Case study: BRAID model
**Bayesian word Recognition using Attention, Interference and Dynamics** 
- Classical, three-layer architecture 
	- Lexical knowledge submodel ≈ “word level” 
	- Letter perceptual submodel ≈ “letter level” 
	- Letter sensory submodel ≈ “feature level”
	- Additional fourth layer: Visual Attentional Submodel
	- ![[BRAID_representation.png]]
- Integrates acuity, interference and attention 
- Probabilistic, hierarchical and dynamical model 
- Simulates letter identification, word recognition and lexical decision 
- Accounts for benchmark effects
	- e.g., frequency, word superiority, neighborhood, priming effects 
- Accounts for effects related to visual processing dimensions •
	- e.g., optimal viewing position (OVP), word length effect in LD, crowding effects wrt interletter spacing

# Généralisation
![[generalisation_risk_2nd_courbe.png]]

Avec énormément de paramètres, il existe plusieurs solutions (et d'autant plus que de paramètres) et le plus grand nombre de paramètres permet alors une meilleure généralisation. Ce qui explique la seconde décroissance sur l'image ci-dessus.

## Cross validation
Séparation du jeu de données en deux, estimation des paramètres sur une première partie et test de généralisation sur la seconde partie. Puis on interverti les deux jeux de données et on refait le calcul d'erreur de généralisation. L'erreur globale est alors (E1-E2)/2, pour obtenir les paramètres globaux, le mieux est toujours de refaire l'entrainement sur l'ensemble des données (la séparation initiale permet simplement de tester la généralisation).

Il existe plusieurs autres manières de gérer les données d'entrée, training, validation, test. N-1; leave K out etc...

# Astuce math
![[astuce_math_log_produit.png]]


# Ods, posterior odds, evidence
[video explicative](https://www.youtube.com/watch?v=lG4VkPoG3ko)
Potentielle question au partiel, reécrire un problème en ods plutot qu'en probabilité.

![[odds_proba_.png]]