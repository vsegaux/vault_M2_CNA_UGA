---
prof: CAMPAGNE Aurélie
date: 2025-10-11
publish: true
---
 > [!NOTE] Examen  
> Question de cours + application; question de méthodo

# Introduction

Cours de neuroimagerie, principes et bases des mesures de surface (EEG : électroencéphalographie ; MEG : magnétoencéphalographie).  
![[Cerveau et neurones]]

### **Conséquence pour EEG/MEG**

- EEG et MEG sont **particulièrement sensibles aux courants transmembranaires synchrones générés par les PPS** des populations de cellules (sommation spatiale et temporelle).
    
- Les potentiels d'action, étant très courts et localisés, contribuent peu au signal de surface mesurable.
    

**Remarque métabolique / hémodynamique** :  
L'activité neuronale s'accompagne d'une demande accrue en oxygène et en nutriments ; ceci entraîne des variations du débit sanguin local (réponses hémodynamiques, de l'ordre de la seconde) — c'est le principe exploité par l'IRMf (voir autres cours).
# Les techniques d’imagerie cérébrale
![[Résolutions des techniques d'imagerie cérébrale]]
# Nature, origine et topographie des signaux EEG et MEG

L’activité mesurée à la surface du scalp (EEG) ou à proximité du crâne (MEG) correspond à la **sommation** de l’activité électrique synchronisée de **milliers de neurones**, principalement les **cellules pyramidales corticales**.  
Ces signaux se traduisent souvent par des **oscillations** reflétant la dynamique temporelle de réseaux neuronaux.

| Technique | Objet mesuré           | Type de mesure | Résolution temporelle | Ordre de grandeur | Capteurs utilisés                    |
| --------- | ---------------------- | -------------- | --------------------- | ----------------- | ------------------------------------ |
| **EEG**   | Potentiels électriques | Relative       | ≈ 1 ms                | quelques µV       | Électrodes de surface                |
| **MEG**   | Champs magnétiques     | Absolue        | ≈ 1 ms                | ~10⁻¹³ Tesla      | Capteurs SQUID couplés à des bobines |

## Mesure EEG : principe et références

L’**EEG** mesure des **différences de potentiel électrique** entre une ou plusieurs électrodes.

Deux montages principaux :

- **Monopolaire** : chaque électrode est comparée à une électrode de référence fixe (méthode la plus utilisée en recherche).
    
- **Bipolaire** : mesure de la différence de potentiel entre deux électrodes actives (souvent utilisée en clinique).
    

### Choix de la référence en EEG monopolaire
![[Choix de la référence en EEG monopolaire]]
## Activités oscillatoires

![[rythmes.png]]

Les signaux EEG/MEG présentent des **rythmes oscillatoires** (alpha, bêta, gamma, etc.), reflétant la coordination temporelle des réseaux neuronaux.

### Origine des signaux oscillatoires
![[Origine des signaux oscillatoires]]
### Origine physique des signaux EEG/MEG
![[Origine physique des signaux EEGMEG]]

### Le macro-dipôle cortical
![[Le macro-dipôle cortical]]
## EEG et MEG : géométrie des dipôles
![[EEG et MEG  géométrie des dipôles]]
### Différences spatiales entre EEG et MEG

- En **EEG**, le signal électrique issu d’une source unique apparaît **étalé** sur le scalp à cause de la conductivité variable des tissus (os, peau, liquide céphalorachidien).
    
- En **MEG**, les champs magnétiques sont **moins déformés** par les milieux traversés → **meilleure résolution spatiale**.
    

Effets de la distance à la source :

- **Amplitude** du signal diminue avec la profondeur.
    
- **Dispersion spatiale** augmente avec la distance à la source.
    
### Sensibilité relative des deux techniques

|Type de source|MEG|EEG|Commentaire|
|---|---|---|---|
|**Radiale**|~1/10|2|L’EEG est plus sensible aux sources radiales (gyrus).|
|**Profonde**|~1/3|1/100|La MEG perd moins de signal en profondeur que l’EEG, mais reste surtout sensible aux sources superficielles.|
### Sources multiples

En pratique, les signaux mesurés résultent de la **sommation de plusieurs macro-dipôles** actifs simultanément.  
Ainsi, une activité observée sur une zone donnée du scalp ne signifie pas forcément que la région sous-jacente est activée.  
Exemple : une onde auditive peut apparaître sur le sommet du crâne alors que les sources réelles se trouvent dans les régions temporales.


## Résumé EEG vs MEG
![[Résumé EEG vs MEG]]

# Dispositifs et principes de mesure des signaux

## MEG — Magnétoencéphalographie
![[MEG — Magnétoencéphalographie]]

## EEG — Électroencéphalographie
![[EEG — Électroencéphalographie]]
# Protocoles d’étude et traitement des signaux EEG/MEG

## Structure d’une expérience EEG/MEG

Les signaux EEG/MEG sont toujours enregistrés **en contexte expérimental contrôlé**.  
L’objectif est de relier l’activité cérébrale mesurée à des **événements précis** (stimuli visuels, sons, actions, réponses, etc.).

### Organisation typique d’une étude

1. **Planification du protocole**
    
    - Choix des stimuli et du type de tâche (visuelle, auditive, motrice…).
        
    - Définition de la durée et du nombre d’essais (trials).
        
    - Contrebalancement des conditions expérimentales.
        
2. **Acquisition**
    
    - Enregistrement simultané du signal EEG ou MEG et des marqueurs d’événements.
        
    - Les marqueurs (ou _triggers_) sont envoyés par l’ordinateur de présentation de la tâche au système d’enregistrement pour aligner précisément le signal avec les stimuli.
        
3. **Prétraitement**
    
    - Nettoyage du signal, suppression du bruit et des artefacts.
        
    - Segmentation des données en **époques** autour des événements d’intérêt.
        
    - Alignement temporel des essais.
        
4. **Analyse**
    
    - Calcul d’**ERPs (potentiels évoqués)** ou **ERFs (champs évoqués)**.
        
    - Études fréquentielles (oscillations, synchronisation).
        
    - Analyses de source (modélisation de l’origine du signal dans le cerveau).
        
## Prétraitement du signal
![[Prétraitement du signal]]

## Analyses des signaux
![[Analyses des signaux]]

# Résumé

## 1. Différences EEG - MEG

| Caractéristique            | **EEG**                                                                                             | **MEG**                                                                |
| -------------------------- | --------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| **Signal mesuré**          | Différences de potentiel électrique à la surface du scalp                                           | Champs magnétiques induits par les courants neuronaux                  |
| **Unités**                 | Microvolts (µV)                                                                                     | Femtoteslas (fT)                                                       |
| **Capteurs**               | Électrodes en contact avec la peau                                                                  | Bobines SQUID refroidies (sans contact direct)                         |
| **Orientation sensible**   | Sensible aux **composantes radiales** du dipôle neuronal (perpendiculaires à la surface du crâne)   | Sensible aux **composantes tangentielles** (parallèles à la surface)   |
| **Influence des tissus**   | Le signal est atténué et déformé par les couches du scalp, du crâne et du liquide céphalo-rachidien | Le champ magnétique traverse les tissus sans déformation majeure       |
| **Résolution temporelle**  | Excellente (millisecondes)                                                                          | Excellente (millisecondes)                                             |
| **Résolution spatiale**    | Moyenne (1–3 cm)                                                                                    | Bonne (quelques mm à 1 cm)                                             |
| **Coût / logistique**      | Faible, portable, installation simple                                                               | Très coûteuse, nécessite une chambre blindée et du hélium liquide      |
| **Sensibilité anatomique** | Bon accès aux régions **corticales superficielles** et radiales                                     | Meilleure sensibilité aux **sources tangentielles** (dans les sillons) |
| **Usage clinique typique** | Épilepsie, sommeil, pathologies psychiatriques                                                      | Recherche cognitive, cartographie fonctionnelle préchirurgicale        |

## 2. Complémentarité EEG / MEG

Les signaux EEG et MEG proviennent de la même activité neuronale (courants postsynaptiques des cellules pyramidales), mais offrent **des perspectives différentes** :

- L’**EEG** capture mieux les sources orientées radialement, situées sur les _crêtes des gyrus_.
    
- La **MEG**, au contraire, est plus sensible aux sources tangentielles, situées dans les _sillons_.
    

Ainsi, leur **combinaison** permet une **meilleure couverture spatiale** du cortex et une estimation plus robuste des sources neuronales.
