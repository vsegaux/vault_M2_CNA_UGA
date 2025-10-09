---
publish: true
---
([vidéo youtoube]( https://www.youtube.com/watch?v=zH3fim2uIHs)). 
Les principales causes d'artéfacts *physiologiques* sont:
- Mouvement oculaires
- Activité cardiaque
- Activité musculaire
- Activité liée à un état de fatigue (onde Alpha)

Sources *extra-physiologiques*:
- Mouvement transitoires du sujet, mouvement de tête
- Bruits électroniques (50Hz, déplacement de câbles, ...)

L'*Analyse en Composantes Principale* (*PCA*) permet aussi de filtrer les artéfacts (typiquement cardiaque), en particulier si ceux-ci sont très différents (orthogonaux) du signal d'intérêt.


- *Recourt à l'EOG* (Electro-Oculographie):
	- Mesure bipolaire, au moins 4 éléctrodes pour séparer l'EOG verticale (clignement + mouvements oculaires verticaux) et horizontale (mouvement oculaires horizontaux). Idéalement, la composante horizontale ne mesure strictement QUE de l'horizontale et pareil pour la verticale; ce résultat est obtenu en plaçant parfaitement les 4 électrodes (le sens de variation dépend du montage, il n'y a pas de convention): ![[position_electrodes.png]]
- *Recourt à l'ECG* (Electro-Cardiographie): 
	- Mesure bipolaire
	- Rarement nécessaire car le signal émit par le cœur est de forme très typique (simplement fréquence variable). Deux électrodes (+ la masse) suffisent.
- *Recourt à l'EMG* (Electro-myographie):
	- Mesure bipolaire
	- Attention, toute correction liée à l'activité musculaire est un potentiel biais pour la mesure initiale (car l'EMG va elle-même présenter des artéfacts). En cas de mesure à artéfacts, il est souvent préférable de simplement supprimer les mesures concernées.