---
prof: BERARD François
date: 2025-11-25
publish: true
---
Augmented cognition: A human-computer Interaction (HCI) viewpoint 

Déplacement de la souris, plutôt en boucle fermée, tpyiquement 50-200ms de perception, 25-170ms de cognition et 30-100ms d'action. Une boucle totale fait en moyenne 240ms (100ms dans les cas les plus rapides).
Pour atteindre une cible, le temps nécessaire est donc donné en fonction des *temps de boucles* (perception, cognition, action; temps fixe) et de la *distance initiale entre le pointeur et sa cible* (normalisée par rapport à sa taille: on considère que le pointeur atteint la cible quand la distance est inférieure à taille/2).

**Fitts' Law**:
Temps = a + 1/IP * ID
Avec:
- IP les performances en bit/s, liée au temps de boucle perception/cognition/action
- ID en bit, lié à la distance initiale pointeur/cible

On a donc une relation linéaire entre le temps de pointage et l'amplitude/la largeur de la cible. Cette équation permet de quantifier la quantité d'information transmise en un laps de temps donné en terme de translation de pointeur. Expérimentalement, il a été démontré que cette quantité est supérieure dans le mouvement de la souris sur une surface plane que dans le mouvement du bras (en VR par exemple).

**Fastest typing speed**: 1946 Stella PAjunas, 216 mots par minute sur la machine à écrire. On est loin des Gbits/s gérables par nos ordinateurs.

Un système avec une grille de curseur a permi de produire un système plus efficace que la souris: l'occulométrie a été couplée avec une souris classique. Le système reconnais le curseur le plus proche du point regardé, et la soucis actionne les clics.

Le système le plus efficace est le pointage avec l'index sur une surface, on passe de 5/6bits/s à la souris à quasiment 8bits/s en pointant. Se pose alors le fat finger problème: le doigt a tendance à cacher la surface et à appuyer sur une zone plus grosse que la cible effective. Pour avoir la précision de la souris avec la rapidité/efficacité du pointage, une solution serait de pointer du doigt, en ayant des doigts transparents. Typiquement en activant sa tablette par derrière, avec une projection des doigts avec une couche alpha<255.