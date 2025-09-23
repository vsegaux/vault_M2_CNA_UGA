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

# Terminologie:
- *Big Data*: données massives (cas particulier de volumétrie), définies comme telles selon 3 critères (3V):
	- Volume (taille)
	- Vélocité: à quelle vitesse les données arrivent elle?
	- Variété: à quel point les données sont-elles hétérogènes (numériques, images, Json, ...)
- *Machine Learning*: technologie permettant d'apprendre sans programmation explicite à partir de données en entrée. 
- *Pattern recognition*: reconnaissance de caractéristiques structurelles spécifiques
- *Data Mining*: fouille/forage de données...terme plus ancien 
- *Deep Learning*: catégorie de ML utilisant des réseaux de neurones 
- *Agent*: une entité qui perçoit et agit 
- *Rational agent*: Un agent rationnel est un agent qui agit d'une manière lui permettant d'obtenir le plus de succès possible dans la réalisation des tâches qu'on lui a assignées
- Machine Learning : a target is called a label. 
- Statistics : a target is called a dependent variable. 
- A variable in statistics is called a feature in machine learning.
- A transformation in statistics is called feature creation in machine learning.

## Donnée - Information - Connaissance

Une *donnée* est l'enregistrement d'une observation destinée à être interprétée/traitée par l'humain (ex. température, temps de réaction, âge, ...)
Une *information* est le signifiant attaché à la donnée ou à un ensemble de données par association. L'information est définie selon un contexte (ex. temps chaud pour T=40°C; nourrisson pour âge=2mois, ...)
Une *connaissance* est une information nouvelle, apprise par association d'information de base, de règles, de raisonnement, d'expérience (ex. T=35°C et avec cette température, nous devons ajuster le système de refroidissement; âge=2mois alors il ne faut pas lui donner d'alcool, ...)

## IA et apprentissage

![[AI_ML_DL.png]]


| Type d'apprentissage | Supervisé                                                                 | Non Supervisé                                                            | Par renforcement                                                                                                                    |
| -------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| Description          | Les données d'entrée ont été labelisée (i.e. elles ont déjà été traitées) | Données non labelisées, l'algorithme doit trouver des structures cachées | On qualifie la sortie du système (note de performance, ex: qté d'argent, distance parcourue...) afin de l'entrainer par essai-errur |
| Exemple              | k-NN (NearestNeighbours); reconnaissance de chiffre manuscrits, ...       | Clustering, segmenter une clientèle selon leurs comportements, ...       | Alpha-Go, Checkers, apprentissage de la marche pour les robots, ...                                                                 |

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
Répétition du tableau...:
- *Reproduction du comportement* : L'IA est jugée uniquement sur sa capacité à imiter les actions humaines de manière efficace, sans tenir compte des processus qu'elle utilise pour arriver à ces actions. Ce qui compte, c'est le comportement observable. 
- *Modélisation du fonctionnement* : L'IA est jugée sur sa capacité à imiter les processus cognitifs humains, c'est-à-dire la manière dont elle pense ou raisonne, même si ses actions ne sont pas directement les mêmes que celles d’un humain.

## Thinking humanly
Pour comprendre comment pense l'Humain:
- Introspection, investigation expérimentale, nécessite des théories sur l'activité du cerveau
- Nécessite d'exprimer ces théories en tant que programmes informatiques
Pour valider ces théories:
- Prédiction et test du comportement humain (top-down)
- Identification directement depuis les données neurobiologiques (bottom-up)