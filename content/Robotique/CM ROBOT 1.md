---
prof: QUINTON Jean-Charles
date: 2025-11-20
publish: true
---

> [!NOTE] Conseils Examen (Annale 2025)
> **Objectif :** Conception d'un système cobotique industriel sur table.
> **Attentes :** Ne pas se contenter de lister le cours. Il faut **justifier** chaque choix matériel ou logiciel par rapport aux contraintes (de l'énoncé!):
> * **Espace réduit :** Optimisation de la structure (bras série vs parallèle).
> * **Sécurité humaine :** Compliance (souplesse), évitement, redondance.
> * **Adaptabilité :** Apprentissage sur des pièces variables.
> * **Mots-clés à placer :** Couplage perception-action, Redondance, Compliance (passive/active), Subsomption, Exploration vs Exploitation, Généralisation.

Lien du cours : https://cours.univ-grenoble-alpes.fr/enrol/index.php?id=8209
Clef: M2R-ROB-S9

# Partie 1 : Aspects Matériels & Contrôle (J.C. Quinton)

## 1. Philosophie : Du Calculateur au Vivant

### Métaphore de l’ordinateur (Robotique Classique)
* **Couplage Faible (Séquentiel & Centralisé) :**
    * Le flux est linéaire : `Capteurs (Entrée) -> Processeur (Modèle/Planification) -> Actionneurs (Sortie)`.
    * **Inconvénients :** Lent (goulot d'étranglement du CPU), peu robuste (si le modèle du monde est faux, l'action échoue), manque de réactivité face aux imprévus.

### Métaphore de l'Être Vivant (Robotique Nouvelle/Cognitive)
* **Couplage Fort (Parallèle & Distribué) :**
    * Pas de distinction nette entre sentir et agir.
    * **Perception Active :** On bouge pour mieux percevoir (ex: bouger la tête pour avoir la profondeur, tâter un objet).
    * **Distribution :** L'intelligence n'est pas que dans le cerveau central.
        * *Exemple :* Les réflexes de la moelle épinière ou la mécanique des muscles (compliance) gèrent les perturbations rapides sans attendre le cerveau.
    * **Frontière floue :**
        * *Smart Sensors :* La caméra traite déjà l'image (flux optique) avant d'envoyer l'info.
        * *Smart Actuators :* Le moteur s'asservit lui-même en vitesse/position.

## 2. Capteurs (La Perception)

Pour l'examen, justifiez le choix par la **complémentarité** (combler les lacunes d'un capteur par un autre) et la **redondance** (sécurité).

### A. Classification
1.  **Proprioceptifs** (État interne du robot)
    * **Encodeurs (Coders) :** Indispensables. Mesurent l'angle des jointures ($\theta$). Sans eux, le robot ignore sa posture.
    * **IMU (Centrale Inertielle) :** Accéléromètres/Gyroscopes. Utile pour la stabilité (robot mobile) ou détecter des vibrations anormales (bras industriel).
    * **Courant moteur :** Mesure de l'effort ($I \propto Couple$). Permet de détecter une collision sans capteur de force dédié (mais peu précis à cause des frottements).

2.  **Extéroceptifs** (État de l'environnement)
    * **Capteurs de Contact / Force (F/T sensors) :**
        * *Usage :* Interaction physique fine (insérer une pièce, poncer).
        * *Principe :* Jauges de contrainte qui se déforment.
    * **Télémètres (Mesure de distance) :**
        * *LIDAR (Laser) :* Très précis, longue portée, balayage plan ou 3D. *Défaut :* Aveuglé par fumée/surfaces transparentes ou très sombres.
        * *Ultrasons (Sonars) :* Cône de détection large, pas cher. *Défaut :* Réflexions spéculaires (l'onde rebondit ailleurs), faible précision.
        * *Infrarouge :* Courte portée, sensible à la lumière ambiante.
    * **Vision (Caméras) :**
        * *RGB :* Riche sémantiquement (reconnaître "une vis" vs "un écrou").
        * *RGB-D (Kinect, Realsense) :* Donne la profondeur. Crucial pour saisir un objet en 3D.
        * *Défaut :* Lourd en calcul, sensible aux variations de lumière, occlusions (main du robot cachant l'objet).
![[robotique_capteurs.png]]
### B. Application Cas d'étude (Cobot sur table)
* **Sécurité (Redondance) :** Peau artificielle (capacitive) sur le bras pour stopper avant contact + Caméra globale surveillant l'approche de l'humain.
* **Précision :** Caméra dans la main ("Eye-in-hand") pour l'approche fine + Capteur d'effort pour le "clic" d'insertion.

## 3. Actionneurs & Structure Mécanique

### A. Types de Moteurs
* **Moteurs Électriques (Le standard) :**
    * *DC / Brushless :* Bon rapport poids/puissance, dynamique élevée.
    * *Pas-à-pas :* Contrôle en boucle ouverte possible (pas cher), mais risque de "sauter" des pas si on force trop.
* **Actionneurs Artificiels / Souples :**
    * *Pneumatique (Air) :* Souplesse naturelle (l'air est compressible). Très sûr pour l'humain mais difficile à contrôler précisément (non-linéaire).
    * **SEA (Series Elastic Actuators) :** Un ressort est placé entre le moteur et la charge.
        * *Avantage 1 :* **Compliance passive** (absorbe les chocs instantanément).
        * *Avantage 2 :* Permet de mesurer la force via la compression du ressort.
        * *Idéal pour le cobot de l'examen.*

### B. Structures et Cinématique
* **Série (Bras articulé, ex: Kuka, Universal Robots) :**
    * Chaîne ouverte. Espace de travail vaste (forme de sphère).
    * *Défaut :* Moins rigide, erreurs cumulatives.
* **Parallèle (ex: Plateforme Stewart, Delta) :**
    * Chaîne fermée. Très rigide, très rapide, précis.
    * *Défaut :* Espace de travail très petit.
* **Redondance Cinématique :**
    * Avoir plus de Degrés de Liberté (DDL) que nécessaire (ex: 7 moteurs pour positionner un objet en 6D - x,y,z,r,p,y).
    * *Intérêt majeur :* **Évitement de singularités** et **Évitement d'obstacles**. Le robot peut garder la main fixe tout en bougeant le coude pour ne pas taper l'humain.

![[Liaisons.png]]
![[typologie_robots.png]]

## 4. Architectures de Contrôle
Comment organiser l'intelligence ?
![[couplage_sensor_actor.png]]
### A. Délibérative (SPA : Sense-Plan-Act)
Modèle hiérarchique classique.
1.  On capture tout l'état du monde.
2.  On planifie une trajectoire complète pour éviter les obstacles modélisés.
3.  On exécute.
* *Critique :* "Le monde est son meilleur modèle". Si le monde change pendant le calcul (l'humain bouge), le plan est faux. Trop lent.

### B. Réactive (Action-Perception directe)
Pas de mémoire, pas de modèle global.
* **Véhicules de Braitenberg :** Connexion directe capteur $\to$ moteur (ex: La lumière fait tourner la roue gauche $\to$ le robot va vers la lumière).
* *Avantage :* Réflexe immédiat.
* *Défaut :* Pas de planification à long terme, peut rester coincé dans des minimums locaux.

### C. Architecture de Subsomption (Rodney Brooks)
Structure en "couches" comportementales parallèles. Pas de processeur central unique.
* **Principe :** Les couches basses (réflexes) fonctionnent toujours. Les couches hautes (cognitives) modulent les basses.
* **Mécanismes de coordination :**
    1.  **Inhibition (Sortie) :** Une couche haute empêche une couche basse d'envoyer sa commande aux moteurs.
    2.  **Suppression (Entrée) :** Une couche haute remplace l'information reçue par la couche basse (lui "ment").
* **Exemple Cas d'étude :**
    * *Niveau 0 (Bas) :* "Stopper si force > seuil" (Sécurité hardware).
    * *Niveau 1 :* "Suivre la main de l'humain" (Collaboration).
    * *Niveau 2 (Haut) :* "Assembler la pièce".
    * *Logique :* Si l'humain pousse le robot (Niveau 1), cela inhibe temporairement l'assemblage (Niveau 2). Si choc violent (Niveau 0), tout s'arrête.

---

# Partie 2 : Apprentissage & Cognition (M. Lefort)

## 1. Apprentissage Supervisé
* **Principe :** Le système apprend une fonction d'approximation $y = f(x)$ en minimisant une erreur entre sa sortie et la vérité terrain (étiquette) fournie par un "professeur".
* **Modèles :** Réseaux de neurones (Deep Learning), SVM, Régression.
* **Cas d'utilisation (Cobot) :**
    * *Vision :* Détection de défauts sur les pièces. Entrée = Image, Sortie = OK/KO.
    * *Maintenance prédictive :* Entrée = Bruit moteur, Sortie = "Panne imminente".
* **Limites :**
    * Dépendance totale à la qualité/quantité des données annotées (biais).
    * Faible robustesse aux données "hors distribution" (ex: pièce vue sous un angle jamais appris).

## 2. Apprentissage Non-Supervisé
* **Principe :** Extraire des régularités statistiques sans étiquettes. Le système organise les données lui-même.
* **Approches :**
    * **Clustering (K-Means) :** Grouper des objets similaires. (Ex: Trier des vis vs boulons sans savoir leur nom).
    * **Réduction de dimension (PCA, Auto-encodeurs) :** Simplifier les données pour trouver les variables latentes importantes.
    * **Modèles Génératifs :** Apprendre la distribution $P(x)$ pour générer de nouvelles données plausibles ou détecter des anomalies (si $P(x_{nouveau})$ est très faible, c'est une anomalie).
* **Intérêt :** Autonomie, pas de coût d'étiquetage humain.

## 3. Apprentissage par Renforcement (RL)
* **Principe :** Apprentissage par essais-erreurs. Pas de professeur, mais un score (récompense/punition).
* **Boucle RL :** L'agent observe l'état $S_t$, choisit une action $A_t$, reçoit une récompense $R_{t+1}$ et arrive en $S_{t+1}$.
* **Défis :**
    * **Exploration vs Exploitation :** Faut-il tester une action inconnue (risque mais potentiel gain) ou faire ce qu'on sait faire (sûr mais sous-optimal) ?
    * **Credit Assignment Problem :** Si le robot gagne à la fin, quelle action précise a été décisive 10 secondes avant ?
    * **Q-Learning :** Apprendre une table ou fonction $Q(S, A)$ qui prédit la somme des récompenses futures.
* **Cas d'utilisation :** Apprendre à manipuler un objet déformable où la modélisation physique est trop dure.
* **Contrainte Cas d'étude :** Dangereux sur robot réel (casse). Solution : Apprendre en simulation (Sim-to-Real) ou utiliser des algos "Safe RL". -> Mais c'est très long, il faut que le robot tombe d'abord par hasard sur une solution qui augmente son "score".
* **Processus de décision Markovien**:
	* ![[markov.png]]
	* Le robot observe son **État** ($S$) (ex: "Je suis face à un mur").
	- Il choisit une **Action** ($A$) (ex: "Tourner à droite").
	- L'environnement réagit via la **Transition** ($T$) : le robot se retrouve dans un nouvel état.
	- Il reçoit une **Récompense** ($R$) (ex: +1 point pour ne pas avoir cogné le mur).
	- Et avec potentiellement en plus des **Observations** ($O$) qui sont imparfaites, et à partir des-quelles des probabilités sont calculés pour essayer d'obtenir une récompense.
	- Le but ultime est de trouver une "**Politique**" ($\pi$) : une stratégie qui dit au robot quelle action choisir dans chaque état pour gagner le maximum de récompenses
- **Q-Learning**
	- ![[q_learning.png]]
	- ![[qvalue_param.png]]
	- ![[qlearning_politic.png]]

## 4. Apprentissage par Démonstration (LfD - Imitation)
* **Principe :** Transférer une compétence de l'expert humain au robot sans programmation explicite.
* **Méthodes :**
    * **Kinéthétique :** On bouge physiquement le bras du robot (mode gravité zéro).
    * **Téléopération :** Via un joystick ou exosquelette.
    * **Observation visuelle :** Le robot regarde l'humain faire.
* **Problème de Correspondance :** Le corps de l'humain (5 doigts) $\neq$ Pince du robot (2 doigts). Comment mapper l'un sur l'autre ?
* ![[imitation.png]]
* Permet de grandement réduire les données nécessaires à l'entrainement.
* **Dynamic Movement Primitives**
	* On contrôle des primitives motrices plutot que directement chaque les mouvements du robots, cela permet de moduler ces primitives (basées sur des fonctions mathématiques) pour faire varier les possibilités de mouvements du robot. -> Décomposition des mouvements en primitives, chaque morceau est alors modulable.![[primitive_move.png]]

## 5. Apprentissage Développemental & Curiosité
* **Approche Bio-inspirée :** Le robot naît "immature" et apprend progressivement.
* **Schème de Drescher :** Unité de connaissance de base : `Contexte + Action -> Résultat`.
    * Le robot teste des actions au hasard (babillage moteur). Si une action change l'état perçu, il crée un schème.
    * ![[descher.png]]
    * ![[descher_schema.png]]
* **Curiosité Artificielle (Motivation Intrinsèque) :**
    * Le robot ne cherche pas une récompense externe, mais cherche à réduire sa **prédiction d'erreur**.
    * Il choisit les tâches qui ne sont *ni trop faciles* (rien à apprendre), *ni trop dures* (chaos, impossible à apprendre), mais qui offrent le **progrès maximal**.
    * *Application :* Permet au cobot de découvrir seul comment utiliser un nouvel outil laissé sur la table.
    * ![[curio_artif.png]]
## 5. Apprentissage génétique
![[algo_genetiq.png]]Mise en compétition de plusieurs agents, selection de celui qui fonctionne le mieux, tentatives successives par "mutations/reproduction/création" aléatoire.

Pas d'hypothèse sur le type d'apprentissage/de résolution cherchée, mais du coup potentiellement beaucoup plus long parce que bcp d'exploration.

Moins efficace que la rétro-propagation de gradient pour les paramètres d'un réseau de neurone.

Bénéfice de ces algo:
- diversité des comportements possibles pour résoudre une même tâche => Robustesse
- meilleur adaptation aussi en cas de dommage
