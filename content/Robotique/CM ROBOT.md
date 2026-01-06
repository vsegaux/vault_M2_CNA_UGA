---
prof: QUINTON Jean-Charles
date: 2025-11-20
publish: true
---
 
> [!NOTE] Examen
> Documents autorisés!
> Connaitre les modules/structure/contraintes et savoir les agencer entre elles+expliquer les potentielles limites
> Typiquement: "Imaginer quel serait le robot idéal pour remplir les contraintes XYZ.", En décrivant ce qui est faisable ou pas, prendre en compte les potentielles interactions avec les humains.



Lien du cours : https://cours.univ-grenoble-alpes.fr/enrol/index.php?id=8209
Clef: M2R-ROB-S9

# Aspect matériels

*Métaphore de l’ordinateur* (Couplage faible (séquentiel-centralisé))
- Entrées : clavier, souris (évènements) 
- Unité centrale : processeur(s), mémoire 
- Sorties : écran, imprim. (conséquences)
- 
*Être vivant* (Couplage fort (parallèle-distribué))
- Sensations : prétraitements, dynamique 
- « Traitement » : distribué, non linéaire 
- Actions : primitives, muscles → rétroact. (exemple du toucher ou de la vision active)  
*Robot*
- Capteurs : prétraitements, dynamique 
- Calculateur : électronique, ordinateur(s) 
- Actionneurs : moteurs

## Intégration - Distribution

*Frontière floue entre capteur-traitement-actionneur*
- Calculs dans le capteur (e.g., features visuelles) 
- Calculs dans l’actuateur (e.g., asservissement en position) 
- Décision décentralisée (e.g., couplage de primitives) actionneurs capteurs traitement e.g., servomoteur 
	- *Primitive motrice*: Sous ensemble de règle motrices qui permettent de décharger le contrôleur central. Par exemple, pour tenir un objet en main, on pense à serrer la main, et "ça se fait tout seul"; plutôt que de penser à contrôler chaque doigt, et à lui ordonner de serrer/de se plier de tant et tant de degrés.
*Difficulté de la tâche côté traitement (IA) qui dépend *
- Des propriétés des actuateurs utilisés + prétraitement des commandes 
- De la qualité / complexité / pertinence des informations issues des capteurs 
- Des capacités et ressources disponibles pour le traitement de l’information 
*Approches de conception matérielle et logicielle*
- Modulaires : réutilisabilité, remplacement ou mise-à-jour (e.g., outil) 
- Intégrées : apprentissage développemental, incarnation (e.g., deep embodiment
*Séparation de la plateforme (robot) et du logiciel (IA)*
- Robots industriels 
	- Design optimal en termes d’espace opérationnel – précision – vitesse) 
	- Application à n’importe quel mouvement (e.g., Kuka KR Agilus) 
- Robots sociaux 
	- Développement d’une plateforme robuste pour interactions ( force, équilibre) 
	- Programmation ultérieure d’applications (e.g., Choregraphe d’Aldebaran) KR Agilus (Kuka)
*Co-design matériel – logiciel* (processus souvent itératif) 
- Design organique de Boston Dynamics (« data-driven hardware design ») 
- Bio-mimétisme pour exploiter l’évolution, et compliance (e.g., ECCE Robot) 
- Matériel comme « facilitateur » du logiciel (e.g., iCub et approche développementale)

## Capteurs

- Exploitant divers phénomènes physiques 
	- Ondes électromagnétiques vs. sonore 
- Actifs ou passifs 
	- Gyromètres (rotation / vibration) 
	- Kinect ou LIDAR (projection) 
- Différents selon le domaine 
	- Pas de sonar dans l’air 
	- Pas de laser dans le brouillard
*Capteurs à combiner*
- Choix de capteurs complémentaires 
	- Selon leur précision spatiale et temporelle 
	- Précision qui dépend des conditions 
- Synchronisation 
	- Pas les mêmes délais ni fréquences ⚫
	- Pas le même référentiel (position / orientation)

![[robotique_capteurs.png]]

## Diversité d'actionneurs
*Actionneurs* : comme pour les capteurs, tout dépend de la tâche à réaliser 
- Force / précision requise 
- Type de mouvement à réaliser (rotation vs. translation) 
- Contrôle en position, vitesse, force ou couple 
*Moteurs électriques (ou thermiques)* 
- Moteurs (électriques) rotatifs 
	- Courant continu = conversion tension en vitesse de rotation (souvent rapide) 
	- Pas à pas = conversion impulsion en changement d’angle fixe (souvent puissant) 
	- Servomoteur (encodeur + contrôleur + moteur) = angle contrôlé (limité ou pas) 
- Moteurs linéaires = force en translation, plutôt que couple en rotation 
*Autres* 
- Vérin (hydrauliques ou pneumatiques) 
- Câbles (couplés avec moteur ou piston) 
- Muscles artificiels (e.g., Suzomori Endo Lab)

## Degrés de liberté

**Degrés de liberté** = *Paramètres indépendants à définir pour positionner un objet*
- Généralement abrégé en ddl ou DoF (degrees of freedom) 
- Indépendants = on considère le nombre minimal requis 
- Positionner = translation et/ou rotation 
- Objet = élément d’un robot ou outil 1D 2D 3D ! 

**Exemple 1** : brosse sur un tableau 
- Collée au tableau + orientation = 3 ddl 
- Décollée du tableau (pos. + orient. 3D) = 3+3 ddl 
- Coordonnées dépendantes du repère (cartésien vs. polaire) 
- Nombre de degrés de liberté  nombre de muscles pour manipuler
**Exemple 2** : avion au sol ou en vol 
- Aligné sur piste (sens unique) = 1 ddl (même si elle n’est pas rectiligne) 
- Contraint à rester au sol = 2+2 ddl 
- Dans un couloir de vol = 1 ddl 
- Nombre de degrés de liberté  dimension de l’espace

## Liaisons mécaniques
**Degrés de liaison** = *ce qui est contraint* (6 - ddl), le degré de liaison décrit la classe d'une liaison

11 liaisons méca. + ressort / chaîne / engrenage 
- Classes 1 (ponctuelle) à 6 (encastrement) 
- Réduction à 3 liaisons seulement (en robotique)
	- Encastrement (classe d’équivalence) = segment / base 
	- Glissière (translation 1D) = articulation **prismatique (P) **
	- Pivot (rotation 1D) = articulation **rotoïde (R)**

![[Liaisons.png]]
## Typologie et espaces

- Cartésien PPP
- Cylindrique RPP
- Sphérique RRP
- SCARA (e.g., Adept Cobra) RRP [exemple vidéo](https://www.youtube.com/watch?v=vKD20BTkXhk)
	- Typiquement capable d'aller plus vite que pour la même tâche avec des translations
- Anthropo. (e.g., Kuka KR30) 3R à 6R
- Parallèle (e.g., plateforme Gough) RP-RP-... ([Exemple video](https://www.youtube.com/watch?v=KaaIGfJgcjA))
![[typologie_robots.png]]


> [!NOTE] Examen
> ça n'a pas été demandé depuis longtemps, mais c'est bien de connaitre/savoir représenter ce genre de liaisons (glissière+pivot), typiquement au cas où on nous demande de faire un schéma sur la copie.

**Espaces associés**:
- Espace **articulaire** défini par l’ensemble des paramètres des articulations (**configuration**) (description ci-dessus)
- Espace **opérationnel** dans lequel l’**organe terminal** (end effector) se déplace

Caractéristiques différenciées 
- Cartésien 
	- relativement lent (vs. anthropo) 
	- facile à contrôler (position) 
- Parallèle 
	- faible espace opérationnel 
	- très précis et rapide


## Complications
- *Articulations actives* (ou pas) 
	- Exemple du pendule inversé multi-segments ([ACIN, TU Wien](https://www.youtube.com/watch?v=cyN-CRNrb3E))
- *Mécanique sous ou sur-contraint* 
	- Hypostatisme (pendule inversé) -> Pas assez de liaison pour contrôler 
	- Isostatisme (Σ liaisons élémentaires = totale) -> Pile le bon nombre de liaisons élémentaires
	- Hyperstatisme (e.g., chaise à 4 pieds) -> Trop de liaison
- *Redondance* (comme dans le vivant) 
	- Nombre de ddl de l’organe terminal < ddl des articulations actives (pleins de possibilités pour le positionnement d'un bras articuler pour attraper un même objet à une position fixe) [vidéo exemple](https://www.youtube.com/watch?v=sZYBC8Lrmdo)
	- Si plus de 3 prismatiques, robots parallèles, ou anthropomorphiques 
- *A-coup* (jerk / jolt) = dérivée de l’accélération 
	- Par exemple selon courbure de la trajectoire (penser conduite auto) 
- *Instabilité / déformation* (e.g., difficulté à maintenir configuration) 
	- Par exemple selon la rigidité attendue (e.g., [Kuka KR16](https://www.youtube.com/watch?v=bA4CtdYa36s)) 
- *Singularités* (en général à éviter) 
	- Nombre de ddl de l’organe terminal < dimension de l’espace opérationnel
		- 
	- Type 1 = perte de contrôle sur/autour d’une direction (e.g., sur robot 6R) + limites d’espace 
		- Typiquement, pour une petit mouvement, le robot doit se déplacer/changer beaucoup sa configuration. 
	- Type 2 = mouvements incontrôlés du robot en absence de commande (e.g. DexTAR)[exemple vidéo](https://www.youtube.com/watch?v=R9Ha4XRMaWo)
		- Pour les éviter, on essaye de réduire l'espace opérationnel pour ne pas avoir à passer par les positions qui causent la perte de contrôle.

## Bilan
Robot au niveau matériel / physique 
- Ensemble de capteurs et actionneurs (avec délais et partiellement dépendants) 
- Liés ensemble par une structure mécanique (configuration si dynamique) 
Robot au niveau logiciel / contrôle 
- Traitements et/ou architecture permettant de coupler capteurs et actionneurs 
- Difficultés pour coordonner les actions entre elles, mais aussi aux sensations

Deux approches possibles pour le contrôle:
- Par apprentissage (DL etc...)
	- Risque de singularité élevé (ex. Tesla voiture autonomes)
- Par calcul et équations
	- Contrôle total, garanti sans singularité
	- Compliquer/impossible si trop de degrés de liberté
# Architecture de contrôle

## Couplage capteur-actionneurs
![[couplage_sensor_actor.png]]

# Apprentissage


> [!NOTE] à retenir
> -- Cout de l'apprentissage important, si on peut faire autrement c'est cool
> -- Apprentissage pour améliorer perception/décision/robustesse..; nécessite base de données, attention à la pertinence des données + souvent difficile d'avoir des données en robotiques.
> -- 


## Objectifs
- **mémorisation** : retrouver la réponse a une entrée déjà vue
- **généralisation** : trouver la réponse a une entrée inconnue (6= sur-apprentissage) 
- **hypothèses** : fonction localement continue, rasoir d’Occam 
- **techniques** : ensemble apprentissage/validation/test, régularisation, ...

## Types d'apprentissage
###  **supervisé** y = f(x)
#### Régression
(y, possibilités continues) ![[panorama_regression.png]]

#### Classification
(y, possibilités discètes)
##### Resnets
Typiquement pour la classification d'images:
![[classif_image.png]]

Exemple resnet50
Connexions résiduelles:
Layer:
![[resnet50_layer.png]]
Répété 50 fois ici:
![[resnet50__.png]]
##### R-CNN
![[rcnn.png]]
##### YOLO (You Only Look Once)
Extractions de boites englobantes de l'image
![[yolo.png]]

##### Mask R-CNN
Les boites englobantes sont réduites à des pixels:
![[rcnn_pixel.png]]

-> Application aux voitures autonomes

#### Fusion de données
![[data_fusion_1.png]]
![[fusion_donnee_2.png]]
A partir de combinaisons de deux entrées sur les 3, on peut prédire la 3eme.

Par exemple: fusion de images à produire et de commandes motrices pour écrire des nombres. => Action motrice pour prédire le nombre ou inversement.

### Par **renforcement**
- récompense si la tâche est bien réalisée
- généralement, la récompense c'est reçue que de manière éparse dans le temps
#### Modélisation du monde
Processus de décision markovien:
![[markov.png]]
- Le robot observe son **État** ($S$) (ex: "Je suis face à un mur").
- Il choisit une **Action** ($A$) (ex: "Tourner à droite").
- L'environnement réagit via la **Transition** ($T$) : le robot se retrouve dans un nouvel état.
- Il reçoit une **Récompense** ($R$) (ex: +1 point pour ne pas avoir cogné le mur).
- Et avec potentiellement en plus des **Observations** ($O$) qui sont imparfaites, et à partir des-quelles des probabilités sont calculés pour essayer d'obtenir une récompense.
- Le but ultime est de trouver une "**Politique**" ($\pi$) : une stratégie qui dit au robot quelle action choisir dans chaque état pour gagner le maximum de récompenses
##### Q-learning
![[q_learning.png]]
![[qvalue_param.png]]
![[qlearning_politic.png]]

Limites de l'apprentissage par renforcement: 
- c'est long, il faut arriver par hasard a faire le bon truc, puis apprendre à le faire bien.
Mais c'est sympa parce qu'on peut apprendre globalement n'importe quoi.


Et pour passer des simulations au monde réel? Plusieurs millions de simulations avec des variations de paramètres (toutes fausses, mais de manière différentes).

### Par **démonstration**
 Accelère l'apprentissage par rapport au renforcement, on lui montre directement une partie de la solution. (on apprends pas sur le robot de base pour éviter de potentiellement le casser en cas de mauvais réglage)
#### Dynamic movement primitives
On conrtôle des primitives motrices plutot que directement chaque les mouvements du robots, cela permet de moduler ces primitives (basées sur des fonctions mathématiques) pour faire varier les possibilités de mouvements du robot. -> Décomposition des mouvements en primitives, chaque morceau est alors modulable.![[primitive_move.png]]


On peut aussi faire de la démonstration ET du renforcement, qui bénéficie alors de la base d'apprentissage de la démonstration.

### Algorithme génétiques
![[algo_genetiq.png]]
Mise en compétition de plusieurs agents, selection de celui qui fonctionne le mieux, tentatives successives par "mutations/reproduction/création" aléatoire.

Pas d'hypothèse sur le type d'apprentissage/de résolution cherchée, mais du coup potentiellement beaucoup plus long parce que bcp d'exploration.

Moins efficace que la rétro-propagation de gradient pour les paramètres d'un réseau de neurone.

Bénéfice de ces algo:
- diversité des comportements possibles pour résoudre une même tâche => Robustesse
- meilleur adaptation aussi en cas de dommage

CPG: Central Pattern Generators => activité typiquement de la colonne vertébrale, qui gère à elle seule une bonne partie de la locomotion.

**Schème de Drescher**
![[descher.png]]
![[descher_schema.png]]
### **non-supervisé** (f(x))
	- clustering: regroupement des entrées par groupes
	- génératif: apprentissage de la distribution (p(x))
	- auto-supervisé: définition d'un signal de supervision à partir des données
		- Exemple dans un texte: on récupère le texte (données), on enlève des mots, le système doit le retrouver. 
### **par imitation/démonstration**
- on montre des solutions (suites d'actions) pour "initialiser" l'apprentissage
![[imitation.png]]
### **développemental/continu/incrémental**
	- apprentissage progressif de tâche, en construisant sur l'existant sans l'oublier

## Curiosité artificielle
![[curio_artif.png]]



> [!NOTE] Examen
> Par rapport aux apprentissages: savoir lequel utiliser pour quelle situation particulière etc... 



