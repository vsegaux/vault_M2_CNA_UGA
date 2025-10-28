---
publish: true
---
![[SR_Research.png]]

Technique la plus répandue aujourd’hui, notamment pour les tests ergonomiques, car elle **n’impose aucune contrainte physique** (tête libre).  
Une simple **calibration** relie la position du regard à des coordonnées sur l’écran.

**Principe :**

- Une **diode infrarouge** éclaire la pupille.
    
- La **cornée réfléchit** cette lumière, formant un point brillant.
    
- Le système calcule la **position du regard** à partir de la relation entre le **centre de la pupille** et le **reflet cornéen**.
    

L’échantillonnage se fait à haute fréquence, selon le capteur.  
Ensuite, un traitement des données brutes permet d’extraire les **saccades** et **fixations** : c’est le **on-line event parsing**.

### On-line event parsing

Le système parcourt les données brutes avec une **fenêtre temporelle glissante** (3 points).  
Il calcule **vitesse** et **accélération**, puis classe chaque point selon des **seuils** :

```
saccade_velocity_threshold = 30
saccade_acceleration_threshold = 8000
saccade_motion_threshold = 0.15
```

Si la pupille disparaît (clignement), les points correspondants sont marqués « sans données ».

![[donnee_brute_traitee.png]]

Dans cet exemple :

- `EFIX` indique la **fin d’une fixation**,
    
- suivi d’un `SSACC` (start saccade), qui dure ici **12 ms**.
    

Les données peuvent être représentées :

- en **fonction du temps** (déplacements X/Y),
    
- ou sous forme de **trajectoire du regard sur l’écran**:
    

![[representation_ecran.png]]


### Posner Task

**Principe expérimental :**

1. Le participant fixe un point central.
    
2. Un des deux carrés latéraux **clignote** pour attirer son attention (réponse automatique).
    
3. Après un délai variable (**SOA**, Stimulus Onset Asynchrony), une **étoile** apparaît dans l’un des carrés.
    
4. Le sujet indique le plus vite possible où apparaît l’étoile.
    

**Résultats :**

- Pour **SOA courts (< 200 ms)** : réponse plus rapide si le flash et l’étoile sont **du même côté** → _cueing attentionnel_.
    
- Pour **SOA longs (> 200 ms)** : réponse plus lente du même côté → _inhibition of return_ (l’attention ne revient pas immédiatement sur la zone stimulée).
    

### Eye Movements & Visual Attention

- Les **saccades** suivent généralement les **déplacements de l’attention** pour permettre une vision fine.
    
- On peut **regarder sans attention** (regard vide), ou **déplacer son attention sans bouger les yeux** (attention couverte).
    
- Mais il est **impossible de faire une saccade sans décaler son attention**.  



    → Lors de tâches naturelles, on suppose donc que **les saccades reflètent les déplacements attentionnels**.    

### Protocoles expérimentaux

**Variables mesurées :**

- **Latence** (en ms, pour essais corrects) en conditions PS et AS,
    
- **Erreurs** (%) en conditions NS et AS.
    

#### Pro-saccade (PS)

Regarder **du côté de l’indice périphérique**.  
→ Sert à vérifier les capacités normales de détection et de production de saccades.

#### Anti-saccade (AS)

Regarder **du côté opposé à l’indice périphérique**.  
→ Nécessite :

- **inhibition** du réflexe pro-saccadique,
    
- **programmation** d’une saccade en position miroir.
    

#### Non-saccade (NS)

Rester **fixé sur le point central** malgré l’apparition d’un stimulus périphérique.  
→ Nécessite une **inhibition complète** de la saccade réflexe.

![[overlap_saccade_.png]]

On observe une **variation nette de la latence moyenne** selon la présence ou non d’un délai (200 ms) entre l’extinction du point de fixation et l’apparition de la cible.  
→ Cela montre l’importance cruciale des **paramètres expérimentaux**.

#### Impact des consignes

![[impact_consignes.png]]

Les **consignes données au participant** influencent fortement la latence et la nature des saccades.  
Une simple variation dans la formulation des instructions peut modifier le comportement oculomoteur.