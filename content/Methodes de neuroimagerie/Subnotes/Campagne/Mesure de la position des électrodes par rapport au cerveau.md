---
publish: true
---
Pour une interprétation fiable des signaux EEG, il faut connaître précisément la position des électrodes par rapport au cerveau.  
Idéalement, on dispose d’une **IRM individuelle** du participant, permettant une **reconstruction anatomique personnalisée**.  
Si cette IRM n’est pas disponible, on utilise un **modèle de tête standardisé** construit à partir de la moyenne de plusieurs centaines ou milliers d’IRM.

La position exacte des électrodes est alors reconstruite numériquement à partir de :

- leurs coordonnées 3D,
    
- les points de référence anatomiques (nasion et préauriculaires),
    
- et la forme du contour crânien du participant.
    

Ces informations permettent de **co-localiser** les mesures EEG/MEG avec l’anatomie cérébrale pour l’analyse de sources.