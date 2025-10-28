---
publish: true
---
Une fois le signal nettoyé, on le découpe en **époques temporelles** centrées sur chaque événement d’intérêt (par ex. de -200 à +800 ms autour du stimulus).  
Les époques sont ensuite **moyennées** pour augmenter le rapport signal/bruit :  
les réponses aléatoires s’annulent, tandis que les réponses stables (évoquées par le stimulus) se renforcent.

Ce moyennage donne les **potentiels évoqués (ERP - Event Related Potentiel)** en EEG, ou les **champs évoqués (ERF - Event Related Field)** en MEG.

![[PE_CE.png]]

> [!NOTE]  
> Ce traitement suppose que la réponse cérébrale est **temporellement stable et phasée** par rapport à l’événement.  
> Pour des phénomènes plus variables dans le temps (ex. oscillations), on utilisera plutôt des **analyses fréquentielles**.