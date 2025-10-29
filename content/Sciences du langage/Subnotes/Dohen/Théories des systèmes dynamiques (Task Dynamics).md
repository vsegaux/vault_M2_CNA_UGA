---
publish: true
---
Ici, la production de parole résulte non d’une succession d’étapes, mais d’une **coordination dynamique de structures** poursuivant des _tâches articulatoires précises_.

#### Les gestes articulatoires

Les unités fondamentales ne sont plus statiques, mais **dynamiques** :

> Des _actions coordonnées_ impliquant plusieurs articulateurs pour réaliser une tâche donnée.

- Ces **gestes** sont des _structures synergiques_ qui réduisent la complexité du contrôle moteur.
    
- Exemple : _fermeture labiale_ impliquant orbicularis oris + muscles de la mandibule.
    

> ⚠️ À ne pas confondre : **geste planifié** (intention) ≠ **mouvement effectif** (exécution).

#### Modélisation dynamique

Chaque mouvement d’une variable du conduit vocal est modélisé par :

$$mx'' + bx' + k(x - u) = 0$$

![[dynamic_speech_prod_theoryç.png]]

Les paramètres de contrôle sont :

- **u** : position d’équilibre (cible articulatoire),
    
- **k** : raideur,
    
- **b** : amortissement.  
    → Ces paramètres définissent la _vitesse_ et la _précision_ du mouvement.
    

#### Deux niveaux de coordination

1. **Inter-articulateur**
    
    - Les tâches de constriction du conduit vocal sont décrites par des _variables du conduit_ (position, degré).
        
    - Ces variables sont reliées à un sous-ensemble de _variables articulatoires_ (ex. lèvres, mâchoire).
        
    - Exemple : production d’une labiale (b, p, m)
        
        - **LP (Lip Protrusion)** → lèvres sup./inf.
            
        - **LA (Lip Aperture)** → lèvres + mâchoire.
            
    - Les relations entre niveaux sont assurées par une **transformation cinématique**.
        
2. **Inter-gestuel**
    
    - Coordonne les différents gestes entre eux (ex. consonnes et voyelles successives).
        
    - Les gestes peuvent **se chevaucher temporellement** (coarticulation).
        
    - Règles générales :
        
        1. Tout geste vocalique est synchronisé avec le premier geste consonantique.
            
        2. Les gestes consonantiques sont synchronisés avec le début ou la fin de la voyelle selon leur position dans la syllabe.
            


#### Variables d’activation

- Définissent **l’influence temporelle** d’un geste sur les mouvements des articulateurs.
    
- Chaque geste possède sa propre _courbe d’activation_ qui module la dynamique motrice.
    
- On parle de **partition gestuelle**:
    

![[partition_gestuelle.png]]