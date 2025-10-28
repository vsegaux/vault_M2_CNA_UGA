---
publish: true
---
Les signaux EEG/MEG contiennent des composantes de fréquence variées (0 à plusieurs centaines de Hz).  
Un **filtrage** est nécessaire pour :

- supprimer les **bruits très lents** (mouvements, dérives de l’amplificateur),
    
- éliminer les **hautes fréquences parasites** (musculaires, électriques).
    

Types de filtres courants :

- **Filtre passe-bas** (low-pass) → supprime les hautes fréquences (ex. > 30 Hz).
    
- **Filtre passe-haut** (high-pass) → supprime les très basses fréquences (ex. < 0.1 Hz).
    
- **Filtre notch (anti-parasite)** → retire une fréquence spécifique (ex. 50 Hz ou 60 Hz du courant électrique).
    

> [!NOTE]  
> Un filtrage mal paramétré peut **détruire l’information** temporelle ou créer de **faux décalages de phase**.  
> Il est donc crucial de vérifier la stabilité des résultats avec différents paramètres.