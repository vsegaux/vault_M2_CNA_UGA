---
publish: true
---
L'activité mesurée en EEG/MEG de surface est la résultante de l'activité cumulée de tous les neurones à proximité de l'endroit où est positionnée l'électrode. On observe alors typiquement une activité oscillatoire, résultante de l'activité d'une population de neurones synchrones.


| Technique | Objet mesuré           | Mesure   | Résolution temporelle | Ordre de grandeur | Capteur                             |
| --------- | ---------------------- | -------- | --------------------- | ----------------- | ----------------------------------- |
| EEG       | Potentiels électriques | Relative | 1ms                   | quelques µV       | Electrodes de surface               |
| MEG       | Champs magnétiques     | Absolue  | 1ms                   | $10^{-13}$ tesla  | Capteurs SQUID couplé à des bobines |
En EEG, on mesure des différences de potentiels électriques, soit par mesure *monopolaire* (électrode VS référence, le plus souvent utilisé en recherche), soit par mesure *bipolaire* (électrode VS électrode, plutôt utilisé en médecine). Dans le cas monopolaire se pose le soucis de la référence, plusieurs méthodes sont possibles:
- Sur le nez, mais gênée par le mouvement des yeux
- Derrière l'oreille (sur les mastoïdes), souvent utilisé
- Sur les lobes d'oreilles (moyenne des deux côtés), potentiellement complexe selon la taille du lobe/la présence de piercings...
- Obtenue par moyenne (seulement possible sur un grand nombre d'électrode (>64)), l'avantage est que les différences obtenues avec cette référence sont bien dues à des activités d'"intérêt".