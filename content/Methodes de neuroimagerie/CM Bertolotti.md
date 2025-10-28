---
prof: BERTOLOTTI Marcella
date: 2025-10-22
publish: true
---


> [!NOTE] **Examen**
> 
> - Comprendre **dans quel contexte** l’iEEG est utilisée.
>     
> - Savoir **interpréter les cartes et graphiques** pour adopter un regard critique sur les publications.
>     
> - Connaître les **limites de généralisation** de cette méthode.
>     
# iEEG

L’**électroencéphalographie intracrânienne (iEEG)** est une **méthode invasive** utilisée exclusivement dans un **contexte clinique**, principalement chez des **patients épileptiques pharmaco-résistants**.  
Elle intervient lors du **bilan pré-chirurgical**, pour localiser précisément le **foyer épileptogène** avant une éventuelle **chirurgie d’ablation** de la zone responsable des crises.

Cette approche s’est révélée très efficace chez les patients concernés. Les chercheurs profitent de ces enregistrements réalisés à des fins médicales pour étudier les signaux neuronaux, mais il faut souligner que **l’implantation des électrodes est toujours guidée uniquement par les besoins cliniques du patient**, et **jamais** par ceux de la recherche.

## Méthodes d’implantation

Deux principales techniques d’implantation existent :

- **ECoG (Electrocorticographie)** : les électrodes sont placées **directement sur la surface du cortex**, après une **craniotomie**.
    
- **SEEG (Stéréo-EEG)** : les électrodes sont **implantées en profondeur** dans le cerveau via de fines tiges pénétrant le crâne. Cette méthode permet d’enregistrer l’activité **des structures profondes**.
    

![[SEEG_recap.png]]


## Objectifs de l’iEEG
![[Objectifs de l’iEEG]]
## Cartographie fonctionnelle par stimulation directe (DES)
![[Cartographie fonctionnelle par stimulation directe (DES)]]
## Avantages de la SEEG

La SEEG offre une **excellente résolution spatiale**, en plus de la **résolution temporelle élevée** propre à l’EEG. Cela permet une observation très fine de l’activité neuronale à l’échelle milliseconde et millimétrique.


## Rappel : potentiel de champ local (LFP)

Le **potentiel de champ local (LFP)** correspond au **courant extracellulaire** résultant de la **sommation linéaire** des **potentiels post-synaptiques** d’un groupe de neurones proches.

L’activité mesurée reflète ainsi directement **l’activité neuronale locale**, particulièrement dans les **hautes fréquences (High Frequency Activity, HFA)** comprises entre **40 et 150 Hz**.  
Ces hautes fréquences représentent une activité **induite**, souvent **filtrée** par les moyennages utilisés dans l’EEG standard — d’où **l’intérêt majeur de l’iEEG** pour accéder à cette richesse d’information.

## Induced vs Evoked Gamma
![[Induced vs Evoked Gamma]]    

## Méthodes d’estimation des HFA

- **Analyse par ondelettes (Wavelet Analysis)** : représentation temps-fréquence (2–200 Hz).  
    Le signal est **convolué** avec plusieurs **filtres oscillatoires** représentant différentes bandes de fréquences → produit une **carte temps-fréquence**.
    
    > (Bruns, _Journal of Neuroscience Methods_, 2004)

![[Evoc_invoc.png]]
- **Transformée de Hilbert (Hilbert Transform)** : estimation de l’**enveloppe d’amplitude** d’un signal limité en bande (20–60 Hz).  
    Cette méthode décompose le signal en **composantes fréquentielles voisines** et calcule le **signal analytique** de chacune via la transformée de Hilbert.
    
    > (Bruns, _Journal of Neuroscience Methods_, 2004)
    

# Résultats liés aux HFA

## 1. Sensibilité fine au stimulus et à la tâche
![[HFA et sensibilité fine]]

## 2. Le timing révèle la fonction
![[Timing et fonction]]
## 3. HFA et désactivation dans le DMN

L’iEEG permet aussi d’observer les **désactivations cérébrales** dans le **Default Mode Network (DMN)**.  
Ces désactivations, souvent négligées, peuvent être **aussi informatives que les activations**, en témoignant de la **suppression d’activités non pertinentes** pendant une tâche.


## 4. Recherches sur la connectivité et la plasticité fonctionnelle
![[Connectivité et plasticité]]
## 5. HFA en temps réel

Dans une tâche de **“cherche et trouve”**, les patients doivent identifier des différences entre deux images.  
Les mouvements oculaires sont enregistrés pendant que l’activité de la **VWFA** est mesurée.

Une autre expérience a révélé une **région spécifique** s’activant uniquement lors de la **parole intérieure**, et ce, **proportionnellement à l’intensité perçue** de cette voix intérieure.

## Avantages et désavantages de la HFA
![[HFA Pros and cons]]
