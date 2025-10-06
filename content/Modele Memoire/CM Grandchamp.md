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