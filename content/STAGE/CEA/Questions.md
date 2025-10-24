- Prise en main des algos: python? pseudo-code? C++? ou déjà embarqué?
- Export des algos: automatique? OpenCL/CUDA etc.. généré seul?
- Partie floue: apprentissage incrémental/en ligne?
- *Focus portage ou focus développement de AIDGE?*
notes Licence


Doc. Aidge https://eclipse.dev/aidge/source/Tutorial

Arrivée des données/Apprentissage:
- **Incremental batch learning** : apprentissage sur lots fixes, revisités plusieurs fois.
- **Online continual learning** : apprentissage en une seule passe par lot, sans revoir les exemples.
- **Online streaming learning** : apprentissage échantillon par échantillon

Dream Net - Data free
- Interet pour l'embarqué parce qu'il ne stocke pas de donnée?
- *Mais basé sur de la reconnaissance d'image de base non?*

"The global architecture of the model composed of two fully connected hybrid networks: Learning Net and Memory Net which are structured as following: -
- An input layer that has the size of features extracted from images. 
- Several hidden layers with parameters depending on the considered database. For Fer-2013 we use one hidden layer with 1000 neurons. 
- An output layer, with sigmoid activation function, composed of several neurons corresponding to the input (Auto-associative or Auto-encoder part) and several neurons corresponding to the number of classes (Hetero-associative or part)"


Poursuite après le stage? Thèse?