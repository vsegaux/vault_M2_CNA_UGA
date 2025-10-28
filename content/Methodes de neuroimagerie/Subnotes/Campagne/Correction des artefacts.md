---
publish: true
---
([Identification et correction des artéfacts]( https://www.youtube.com/watch?v=zH3fim2uIHs))
Les signaux EEG/MEG sont sensibles à de nombreuses sources de bruit non cérébral :

- **Mouvements oculaires** (clignements, saccades), 
    
- **Activité musculaire** (mâchoire, cou, front),
    
- **Bruits cardiaques**,
    
- **Micro-mouvements du capteur ou du participant**.
    

#### Méthodes de correction

- **Rejet manuel d’essais contaminés** : suppression des segments trop bruités.
    
- **Correction automatique** :
    
    - **ICA (Independent Component Analysis)** : séparation des composantes indépendantes du signal, permettant d’isoler et retirer celles correspondant à des artefacts (ex. composante “clignement”).
- **Recourt à l'EOG** (Electro-Oculographie):
	- Mesure bipolaire, au moins 4 éléctrodes pour séparer l'EOG verticale (clignement + mouvements oculaires verticaux) et horizontale (mouvement oculaires horizontaux). Idéalement, la composante horizontale ne mesure strictement QUE de l'horizontale et pareil pour la verticale; ce résultat est obtenu en plaçant parfaitement les 4 électrodes (le sens de variation dépend du montage, il n'y a pas de convention): ![[position_electrodes.png]]
-  **Recourt à l'ECG** (Electro-Cardiographie): 
	- Mesure bipolaire, rarement nécessaire car le signal émit par le cœur est de forme très typique (simplement fréquence variable). Deux électrodes (+ la masse) suffisent.
- **Recourt à l'EMG** (Electro-myographie):
	- Mesure bipolaire, attention, toute correction liée à l'activité musculaire est un potentiel biais pour la mesure initiale (car l'EMG va elle-même présenter des artéfacts). En cas de mesure à artéfacts, il est souvent préférable de simplement supprimer les mesures concernées.