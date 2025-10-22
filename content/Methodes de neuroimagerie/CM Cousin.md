---
prof: COUSIN Emilie
date: 2025-10-09
publish: true
---
> [!NOTE] Examen
> 
> - Très peu de questions sur la physique ou les principes de fonctionnement précis des machines.
>     
> - Il faut connaître les **principes généraux** mais pas les détails techniques.
>     
> - **Priorité :** savoir **interpréter et critiquer** les images obtenues.  
>     _Examen : manipulation à analyser et à commenter._
>     
# IRM : Objectifs et principes

## Objectifs cliniques

L’IRM n’est **jamais utilisée seule pour poser un diagnostic**. Elle **complète une démarche diagnostique** initiée par d’autres examens.

Applications principales :

- **Outil d’investigation pré-chirurgicale**
    
- **Épilepsie** : chez les patients résistants aux médicaments, la seule solution peut être la **déconnexion chirurgicale de la zone épileptogène** afin d’empêcher la propagation de l’activité anormale.
    

## Objectifs en recherche

L’IRM est utilisée pour :

- **Cartographier les fonctions cérébrales** à partir de l’interprétation des activations neuronales.
    
- Étudier les **corrélats neuronaux** de processus cognitifs, perceptifs ou émotionnels.
    

## Carte cytoarchitectonique de Brodmann

Les **aires de Brodmann** correspondent à une **classification des régions cérébrales selon leur architecture cellulaire** (type, densité et organisation des neurones).


# Tomodensitométrie et TEP

## Tomodensitométrie (Scanner / CT-scan)

**Méthode anatomique**, basée sur l’**absorption des rayons X**.

### Principe

- Un **rayon X fin (1 à 4 mm)** est généré par un tube tournant autour de la zone à étudier.
    
- Des **détecteurs** situés en face mesurent le rayonnement non absorbé.
    
- La rotation permet de **reconstruire les différentes couches** anatomiques.
    
- **Plus une zone est dense**, **plus elle apparaît blanche** sur l’image.
    

|Avantages|Inconvénients|
|---|---|
|Peu coûteuse|Mauvais rapport signal/bruit|
|Très disponible|Utilisation de rayons X (irradiation)|


## Tomographie par Émission de Positons (TEP)

**Méthode fonctionnelle**, permettant d’étudier **l’activité métabolique cérébrale**.

### Principe

- Basée sur la **réponse hémodynamique** : lors d’une activité neuronale, le **débit sanguin et l’oxygénation** augmentent localement.
    
- Cette variation est mesurée à l’aide d’un **traceur radioactif** (ex. : **Oxygène-15**, isotope de l’eau : _$^{15}$O-eau_).
    
- Le **$^{15}$O** se désintègre en émettant un **positon** ; celui-ci s’annihile avec un électron, produisant **deux photons opposés** (sur un même axe) détectés par les capteurs.
    

|Avantages|Inconvénients|
|---|---|
|Mesure directe du traceur → données absolues|Injections multiples nécessaires|
||Faible signal|
||Nécessite moyennage sur plusieurs sujets|
||Exposition à la radioactivité|

### Autres traceurs

- **Fluor-18 (18F)** : permet d’étudier la **synthèse de dopamine** (utilisé dans la recherche sur la **maladie de Parkinson**) et le **métabolisme du glucose** (notamment dans le cerveau, les muscles et les cellules cancéreuses).
    

# IRM : Bases physiques

## Principes généraux

- Technique **non invasive**
    
- Fournit une **image 3D du cerveau**
    
- Basée sur la **Résonance Magnétique Nucléaire (RMN)**
    

La RMN exploite les propriétés magnétiques de certains noyaux atomiques, en particulier **l’hydrogène**, présent en grande quantité dans les tissus biologiques.

### En absence de champ magnétique

Les **spins nucléaires** (moments magnétiques des protons) ont des directions aléatoires, produisant une **aimantation longitudinale moyenne nulle**.


## Étapes principales de la RMN

1. ### **Magnétisation**
    
    - Un **champ magnétique intense** ($B_0$, typiquement 3 Tesla, soit 60 000 fois le champ terrestre) aligne les spins des protons.
        
    - L’aimantation résultante ($M_0$) devient **non nulle** et orientée dans le sens de $B_0$.
        
    - Les spins *précessent* (tournent) autour de cet axe à une fréquence spécifique : la **fréquence de Larmor**.
        
2. ### **Résonance**
    
    - Application d’un **champ radiofréquence** ($B_1$), perpendiculaire à $B_0$.
        
    - Ce champ est **à la fréquence de Larmor**, ce qui provoque la **bascule de $M_0$** dans le **plan transversal**, permettant sa mesure.
        
3. ### **Relaxation**
    
    - Après l’arrêt de $B_1$, les spins retournent à l’équilibre :
        
        - **Relaxation longitudinale (T1)** : réalignement de $M_0$ avec $B_0$.
            
        - **Relaxation transversale (T2)** : déphasage des spins et perte du signal dans le plan transversal.
            
        - Lorsque des **inhomogénéités de champ** ($B_0$) ou des **agents paramagnétiques** (comme la désoxyhémoglobine) sont présents, la relaxation est encore plus rapide : on note **T2 *
            

> Note : T2 < T1


## Contrastes d’image

### Contraste T1 (anatomique)

- **Substance blanche** : hypersignal (blanche) → T1 court
    
- **Substance grise** : isosignal (gris)
    
- **Lésions / LCR** : hyposignal (noir) → T1 long
    

### Contraste T2 (fonctionnel)

- Contraste **inverse du T1** :
    
    - **Substance blanche** : gris foncé
        
    - **Substance grise** : gris clair
        
    - **LCR / lésions** : blanc  
        → Utile pour **mettre en évidence les lésions**.
        

# IRMf et Effet BOLD

L’**IRM fonctionnelle (IRMf)** étudie l’**activité cérébrale** via les variations de l’oxygénation sanguine (**effet BOLD** : _Blood Oxygen Level Dependent_).

## Comparaison TEP vs IRMf

| TEP                                            | IRMf                                                   |
| ---------------------------------------------- | ------------------------------------------------------ |
| Mesure directe du débit sanguin (via $^{15}$O) | Mesure indirecte via variations d’oxygénation          |
| Injection radioactive nécessaire               | Aucune injection, traceur endogène (désoxyhémoglobine) |
| Données absolues                               | Données relatives (contrastes, analyses statistiques)  |


## Effet BOLD

- **Oxyhémoglobine** : diamagnétique → ne perturbe pas le champ magnétique
    
- **Désoxyhémoglobine** : paramagnétique → perturbe le champ magnétique
    

Lorsqu’une région devient active :

- L’apport d’**oxygène** augmente beaucoup plus que la consommation neuronale.
    
- Il en résulte une **diminution locale de la désoxyhémoglobine** (1 à 5%), donc **une augmentation du signal (du temps de relaxation transversal) T2*
    

### Réponse hémodynamique typique

1. **Début d’activité neuronale** → consommation rapide d’O₂ → augmentation de la désoxyhémoglobine.
    
2. **Quelques secondes plus tard** → forte augmentation du débit sanguin.
    
3. **Surcompensation** → baisse de la désoxyhémoglobine (pic à 5–9 s).
    
4. **Retour à l’équilibre** après 15–30 s.
    

# IRM : Contre-indications et effets biologiques

## Contre-indications absolues

Liées au champ magnétique :

- Pacemaker, défibrillateur implantable
    
- Neurostimulateur
    
- Stimulateur de croissance
    
- Pompe implantée
    
- Implants cochléaires
    
- Prothèses ossiculaires métalliques
    
- Corps étranger métallique mobile
    

## Contre-indications relatives

Liées au patient :

- Claustrophobie, anxiété, agitation
    
- Incapacité à rester allongé (décubitus dorsal)
    
- Enfant de moins de 6 ans
    
- Patient intubé ou ventilé (sans matériel compatible)
    

## Effets biologiques possibles

- Légers **échauffements tissulaires** dus à l’absorption des ondes radio
    
- Sensations : vertiges, goût métallique
    
- Effets cardiovasculaires
    
- **IRM déconseillée chez la femme enceinte**
    

# Considérations psychologiques et inférence inverse

Attention à la **tentation d’interpréter une activation cérébrale comme spécifique d’un processus mental** (ex. : « zone de la douleur »).  
Cette erreur est appelée **inférence inverse** :  
on suppose qu’une zone activée implique nécessairement un état psychologique donné, alors que cette zone peut être **recrutée par de nombreux processus différents**.

Exemple :  
_Kross et al., 2011_ — le rejet amoureux active des régions similaires à celles de la douleur.  
→ Cela ne signifie pas que le rejet amoureux _est_ de la douleur physique.

### Approche correcte : l’inférence directe

On part d’un **état psychologique induit** (ex. : réaliser une tâche) et on observe les activations correspondantes.  
On cherche ensuite à savoir **quelles théories cognitives** sont confirmées ou remises en question.

> _Une activation cérébrale ne prouve rien seule : elle doit contraindre ou informer une théorie._

#### Sensibilité vs spécificité

- **Sensible mais non spécifique** : zone cérébrale souvent active, mais pour de nombreuses raisons.
    
- **Spécifique mais peu sensible** : active uniquement dans des cas rares, même si la condition est présente.
    

### Types d’inférences

- **Inférence directe** : état → activité cérébrale observée
    
- **Inférence inverse** : activité cérébrale → déduction d’un état psychologique (⚠️ risqué)
    

### À retenir

- L’inférence inverse suppose une **valeur prédictive positive (VPP)** élevée, difficile à estimer sans comparer de nombreuses tâches.
    
- Pour qu’une activation ait une VPP élevée :
    
    1. Elle doit être **spécifique** à un état cognitif donné.
        
    2. Elle doit **reproduire** ce résultat dans différentes études.
        

# Théories testables par la neuroimagerie

1. **Théories de localisation fonctionnelle** (_« Où ? »_)
    
    - Cartes d’activation, contrastes tâche/contrôle.
        
2. **Théories de connectivité / architecture fonctionnelle** (_« Avec qui ? »_)
    
    - Analyses de connectivité, graph theory, ICA (Analyse en Composantes Indépendantes.
        
3. **Théories mécanistes ou computationnelles** (_« Comment ? »_)
    
    - Relient modèles cognitifs/neuronaux aux données IRMf (RSA, MVPA, modélisation computationnelle).
        

# Réalisation pratique d’un examen IRMf

1. **Scan de repérage**
    
2. **Scan fonctionnel** : acquisition des volumes (tâche/contrôle)
    
3. **Scan anatomique** : image de référence structurelle
    

Chaque **séquence d’acquisition** correspond à un ensemble de coupes obtenues avec les mêmes paramètres.


# Étude : perception olfactive et motricité

## Objectif

Comparer les réseaux cérébraux impliqués dans :

- L’olfaction réelle vs imaginaire
    
- La motricité réelle vs imaginaire
    

## Imagerie olfactive et motrice

- L’**imagerie mentale** correspond à la représentation d’une sensation sans stimulation externe.
    
- L’**imagerie motrice** est généralement plus vivace que l’olfactive.
    
- Le **QQME** (questionnaire) est utilisé pour évaluer l’**aphantasie** dans différents domaines sensoriels.
    

## Matériel et méthode

Quatre tâches cognitives :

1. Mouvement réel
    
2. Odorat réel
    
3. Imagerie motrice
    
4. Imagerie olfactive
    
Un peu la flemme de finir proprement la prise de note j'avoue...