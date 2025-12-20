---
prof: ROUSSET Stéphane
date:
publish: true
---

**Articles de référence**:
- Squire & Alvarez (95)
- Mc Clelland & Al. (95)
- Meeter& Murre (2004)
- Nadel & Moscowitch (97)


Deux dilemmes pour les systèmes de mémoire:
 - information générale VS spécifique
 - stabilité VS plasticité


Rappel sur les notions vues avec Minerva II:
- Autoassociation: à partir des valeurs en entrée (sur les capteurs), produire des valeurs identitques
- Hétéroassociation: A partir de différents capteurs (visuel, olfactif etc..), associer les valeurs d'entrée dans une modalité à des valeurs dans une autre modalité (odeur de rose => image de rose).

# Rappel sur la loi de Hebb (stricte)
Lorsque deux neurones sont simultanément activées alors le poids de la connexion qui les relie est modifié proportionnellement au produit de leur activation.

- Loi d apprentissage quand deux neurones sont activés par une entrée externe
	- Forme simple de la règle : 
		- Nouveau poids = ancien poids + ((1/nb connexions) X (ActivNeurEntrée x ActivNeurSortie))
		- En (a) : nouveau poids = 0 +( ½ x (-1x0.5) ) = -1/4
	- Quand un neurone n'est pas activé une entrée externe: Calcul de la somme des entrées pondérées par les poids de connexions
		- Activation = Somme des entrées pondérées par les poids de connexions
		- En (a) : activation = (-1x-1/4) + (1x1/4) = 0.5

![[exeple_appren_HEBB.png]]
Si on suppose que dans l'image ci-dessus, les neurones d'en bas sont des entrées visuelles et ceux d'en haut sont des entrées olfactives. Dans la première ligne, il apprend l'association odeur-vision pour une entrée spécifique; et puis avec cet apprentissage, il apprend en deuxième ligne une nouvelle association. Finalement, en revoyant l'entrée initiale, il est capable de refaire l'association initialement apprise.

A chaque apprentissage, on modifie l'ensemble des paramètres: on parle de **mémorisation distribuée**. Les mêmes *paramètres* sont modifiés pour tous les exemples à apprendre. On ne peut donc pas dire qu'on va réellement stocker les éléments à apprendre.

**Attention**, dans l'exemple ci-dessus, les deux entrées sont *orthogonales* entre elle donc les capacité d'apprentissage du modèle sont excellentes. (-1 1) et (1 1) (orthogonaux car -1x1 + 1x1 = 0). Cette capacité d'information spécifique est perdue dès lors que les entrées ne sont plus orthogonales. 
- Sans orthogonalité, on va finir par avoir de l'oubli catastrophique. Dans le monde réel, les entrées ne sont pas que orthogonales, c'est pour ça que les synapses sont initialisées à 0. 
- Si on suppose que toutes les entrées étaient systématiquement orthogonales, le système serait alors incapable de se représenter le monde, de faire le lien entre les différentes entrées; autrement dit, il serait incapable de généraliser.

Terminologie:
- On parle de "**distribution**" quand on parle de la manière dont est faite la mémorisation sur les paramètres variables du modèle. L'encodage d'un concept est réalisé (distribué) sur l'**ensemble** des paramètres.
- On parle de "**répartition**" quand on parle de localisation dans l'espace d'entrée. Un concept est "réparti" comme une activation spécifique des capteurs d'entrée.
- L'entrée est répartie, l'apprentissage est distribué.


Pour rendre compte du cerveau humain, qui peut apprendre et récupérer indépendamment de l'orthogonalité des éléments appris, il faudrait un système en plus du simple système neuronal décrit ci-dessus.



Si on veut une *mémoire spécifique*, il faut un *encodage orthogonal*. Cela est rendu possible pas un encodage de type 'sparse' (une entrée est codée non pas comme une activation partielle d'un ensemble spécifique de neurone, mais plutôt comme une activation spécifique de certains neurones, et pas du tout de tous les autres), de cette manière, les chances que les éléments d'entrée répartis sur les neurones d'entrée soient orthogonaux entre eux sont très grande.
- Ainsi, pour savoir si une nouvelle entrée est orthogonale, il faut la comparer à toutes les autres entrées déjà présentes: pour être sur qu'elle soit bien orthogonale à chacune d'entre elle. On ne stockerait finalement (dans l'**hyppocampe**) que les entrées complètement nouvelles (celles qui ont des similitudes avec d'autres ne 'valent pas la peine' d'être apprises).

Dans le reste du **cortex**:
- c'est cette partie qui doit trouver les points communs, la sémantique entre les différents éléments.
- C'est lui qui est responsable de la partie '*mémoire générale*'.

On en revient à un système similaire à celui proposé par Nadel & Moscowitch (1977).
![[nadel_mosco_rappe.png]]
Finalement, on aurait:
- l'*hyppocampe* qui est responsable du stockage spécifique de la mémoire, qui stocke des éléments orthogonaux entre eux.
- le *cortex* qui est responsable du stockage général de la mémoire, qui stocke le monde tel qu'il est réellement.
- Par rappel/renforcement aléatoire, les éléments sont maintenus à long terme (CF Nadel & Moscowitch dans le premier cours)

# Tracelink model
(Martijn Meeter & Jaap M.J. Murre)

![[tracelink_general.png]]
Ici:
- trace system représente le cortex
	- 200 Cellules (neurones), toutes connectées entre elles
	- Activation d'un neurone = représentation d'un concept (**représentation forte**, neurone 'bière', neurone 'Jennifer Aniston' etc...)
	- système Hebbien dynamique
	- Toutes les cellules calculent (en 5-6 étapes de calcul, d'abord par influence seule des entrée, puis par les autres retours d'activation) leur activation en fonction des entrées ET de leurs connections avec les autres cellules (du meme systeme et du système link).
- le link system représente l'hyppocampe.
	- 42 Cellules, toutes connectées entre elles
- Les cellules des deux systèmes sont toutes connectées entre elles
- Le link system est connecté à un système de modulation.

![[trace_link_foncitonnement.png]]
L'objectif est d'avoir un codage 'sparse' (certaines cellules activées, d'autre non), il nous faut donc un système/paramètre qui permette d'inhiber certaines cellules (aussi pour ne pas finir après quelques étapes de calcul sur un système complètement activé).

- Un *évènement* est décomposé en *10 composants sémantiques* (choix d'implémentation du modèle) (K=10) dans le trace system.
- Dans le link system, K=7, fixé ainsi par les auteurs parce que ça marchait bien pour leurs hypothèses et modélisations... ok...


- Pour l'apprentissage:
	- Pas d'apprentissage dans le link system.
	- Lors de l'arrivée d'un nouvel évènement, le système complet 'tourne' pendant un certains nombres d'itération (150), pour finalement ne donner que 10 neurones activés dans le trace system et 7 dans le link system.
	- Aléatoirement, à partir de bruit, des activations sont générées dans le trace system et permettent donc de consolider des liens ($\mu$ = 0.0025). On parle de *mode interne*.
	- En mode externe, c'est le cas de l'arrivée d'un nouvel évènement, elle ne résulte pas en la création de nouvelles traces. ça ressemble beaucoup à l'apprentissage décrit ci-dessus, mais sans création de nouvelle trace, simplement renforcement de celles activés après les 150 itérations. Ce mode ne sera jamais plus discuté dans ce cours; on ne s'intéresse qu'aux nouveaux apprentissages.


### Déroulement d'un apprentissage
La mémoire humaine est capable d'apprendre séquentiellement: on peut apprendre de nouvelles choses sans oublier celles qui ont été apprises dans le passé.

**Probabilité de consolidation en fonction de l'ordre d'apprentissage**:

![[proba_consolidation_ordre.png]]


Malgré la consolidation plus courante du premier élément appris, celui-ci fini quand même pas être "le plus oublié" au final, après un long moment.


Cas des lésions hypocampiques:
- ![[lesion_hypo.png]]
- Sur la courbe d'oubli, en abscisse on a l'ancienneté du souvenir, la courbe d'oubli controle indique que le patient se rappelle de moins en moins selon que les souvenirs soient anciens. Pour le patient lésionné, la courbe est croissante car les souvenirs ne se font que sur la base de la consolidation (lésion du link system; pas du trace system): ![[oubli_lesion_control.png]]


*Ictus amnésique*:
- Les patients atteints sont amnésique antérograde (incapacité de former de nouveaux souvenirs) pendant quelques heures. La récupération ensuite est progressive, mais l'évènement est oublié.
- Dans le modèle, ces cas sont simulés par un K=0 dans l'hypocampe (link system): ![[ictus_simulation_result.png]]
- Sur les graphes ci-dessus, la période d'amnésie est représentée en blanc (K=0). Le test de la mémoire est réalisé avec différentes valeurs de K. On reconnait la courbe de lésion dans le cas K=0. Dans la courbe en bas à droite, le patient a complètement récupéré au moment du test, le seul souvenir oublié est celui correspondant à l'apprentissage pendant l'ictus.

# Réseau de neurones
## Principe de fonctionnement
On se concentrera sur les réseaux de neurones fonctionnant avec des hyperplans séparateurs.

- Cellules d'entrée
- Cellules cachées
- Cellules de sortie
- Chaque cellule a une fonction de seuil, qui s'applique sur la somme pondérée des activations de toutes ses entrées $S = f(\sum_{j}E_j*W_j)$ Avec W le poids associé à l'entrée.

Si on prend le cas le plus simple, avec une entrée pour une sortie, le réseau défini un point limite de séparation entre S=0 et S=1 sur l'espace d'entrée E.
Dans le cas de 2 entrées pour une sortie, le réseau défini une droite séparatrice, à partir des sommes E1W1 et E2W2:
![[separation_E_S.png]]
Avec 3 entrées on défini un plan séparateur, et au delà, on défini un hyperplan séparateur.

Le soucis est finalement d'adapter l'hyperplan pour séparer nos entrées tel que souhaité:
- **Paramètres** du problème **fixes** :
	- L’architecture (cellules, connectivité) 
	- La fonction de seuil 
	- Les exemples à apprendre 
 - **Paramètres libres**:
	- Les poids de connexions 'W'.
	- En modifiant les poids, on *modifie la projection* de l'*espace d'entrée* sur la première couche du réseau. Tout l'espace d'entrée est projeté.
	- L'apprentissage se fait de manière séquentiel, on apprend en regardant l'erreur sur un exemple, on modifie les poids, puis on présente l'exemple suivant. L'objectif est de minimiser l'erreur pour tous les exemples.
	- En réalité, il y a des hyperparamètres pour ajuster l'apprentissage, les nouveaux poids sont calculés selon un paramètre d'inertie et un paramètre de 'rapidité' (à quel point les gros changements de poids sont autorisés ou pas).

**Le point fondamentalement différent de l'apprentissage humain est que dans un réseau de neurone, il n'y a aucun stockage des exemples d'apprentissage. Ceux-ci ont simplement été des contraintes permettant de positionner l'hyperplan séparateur, ils ne sont pas gardés en mémoire.**

Mais une seule couche (E->S) ne permet pas de résoudre des problèmes qui ne soient pas linéaires:
![[hyperplan_soucis_couche.png]]
La dernière couche (C1,C2->S1) n'est capable que de problèmes linéairement séparables, et la couche d'en dessous va projeter l'espace d'entrée dans une forme qui sera linéairement séparable. Cette projection **n'est pas linéaire**, elle transforme les relations de similitudes de l'espace d'entrée.

Les couches cachées ont donc plusieurs rôles:
- Augmentation du nombre de poids, donc de paramètres
- Augmentation de la dimensionnalité (passer de 2 à 3 par exemple)
- *Possibilité de projeter les entrées dans un nouvel espace façonné en fonction des contraintes d'apprentissage. C'est cette possibilité qui est essentielle, elle permet des transformations non-linéaires.*
- Les illustrations suivantes rendent compte de cette projection:
![[avant_appr_1.png]] ![[apres_appr1.png]]

![[apres_appr2.png]]


Quelle fonction d'activation pour les cellules cachées?
- Linéaire? bof parce que les fonctions d'activation linéaire ne permettent pas de projeter l'espace d'entrée de manière non linéaire.
- Créneaux? bof parce que pas continu
- **Sigmoïde** plutôt en réalité.

Lien avec la perception catégorielle:
- Pour des paires de points séparés par une même distance
- Deux points appartenant à une même catégorie seront moins bien discriminés que deux points appartenant à des catégories différentes 
- (pas le cas chez les bébé, car ils n'ont pas encore formé de catégories)


Et pour la généralisation?
- dans la réalité, généralisé revient à comprendre le monde, savoir qu'un animal est un animal implique qu'il a tout un tas de propriété spécifiques aux animaux.
	- Dire qu'un "torti" est un oiseaux implique qu'il peut voler, qu'il a des ailes, qu'il pond des oeufs etc...


Exemple pédagogique McClelland et col, 97):
	- Le but est d'étudier comment un réseau peut capturer une structure simplement au travers de succession d'exemples élémentaires, et ceci *sans fonctionner en suivant la structure hiérarchique globale* (sans parcourir l'arbre total des catégories possibles).
- ![[mcclelland_97.png]]
- Il n'y a pas de ressemblance physique entre les éléments appris, mais une structure commune entre tous les exemples appris. Ils partagent systématiquement les mêmes caractéristique 'logiques'. 
- L'espace d'entrée d'éléments qui ne se ressemblent pas du tout entre eux est déformé dans la première couche cachée. Sur la figure suivante, les activations de la couche cachée (8 neurones) sont données pour divers exemples d'entrée (au fil de 25, 200 et 500 époques d'apprentissage).
- ![[projection_couche_cachee.png]]
- On observe qu'au fil des époques, les activations de la couche intermédiaire se spécialisent et laissent apparaitre des catégories (les animaux donnent des activations similaires entre elles; et celles-ci sont très différentes des activations provoquées par les entrée étant des végétaux;; de la même manière que les activations des poissons sont très similaires entre elle, et plus proche de celle des oiseaux que les activation des végétaux).
- L'espace d'entrée à donc été déformé de telle sorte que les oiseaux et les végétaux soit 'déplacés' dans deux 'zones' différentes.
- On comprends donc que si par la suite, on lui apprend qu'un "torti" est un oiseaux, il va le projeter du même coté de l'espace que les oiseaux. **Non pas parce qu'il ressemble à un oiseau**, mais parce que le réseau a "l'habitude" de faire cette association entre les entrées 'oiseaux' et les sorties. **C'est la répétition de relation entre entrée et sortie qui défini le comportement du réseau**, pas la ressemblance des entrées entre elles.
- Paraphrase d'au dessus: **La couche cachée n'est pas un encodage des entrées, mais une projection de celle-ci; projection correspondant à celle qui a été utile pour résoudre la tâche (après apprentissage).** Autrement dit, la projection est influencée par le comportement attendu de toutes les couches entre elles (donc sur l'apprentissage des liens entre entrée et sorties).


> [!NOTE] Exam?
> Il a posé la question plusieurs fois/mentionner plusieurs fois le fait de savoir le définir:

*Pourquoi cette généralisation n'est pas comme la généralisation "habituelle/basique" (celle basée sur la ressemblance/l'arbre de ressemblance)?*
La généralisation est faite par une adaptation de fonction et non pas par un catégorisation dans l'espace des entrées. On a ici une généralisation sans avoir de représentation au sens fort (les neurones (de la couche cachée) ne sont pas là pour représenter/séparer les végétaux et les animaux; ni les oiseaux et les poissons)!


Cas des auto-encodeur:
- ici, la fonction à apprendre est la fonction identité, donc la sortie doit etre strictement égale à l'entrée.
- L'encodage sur la couche interne va donc dépendre strictement de l'image d'entrée, des entrée (et pas vraiment de la tâche, comme ça devrait être le cas normalement).
	- Pour chaque exemple d'entrée, il suffit d'en garder la position dans la couche intermédiaire pour pouvoir le ressortir à l'identique.



**Points clé du cours**
- forme de généralisation basique: on réfléchit sur les éléments du monde exterieur directement -> **interpolation**.
- il existe des interpolations/généralisations basées sur des règles extraites/des connaissances construites, des représentation en mémoire.
	- un réseau de neurone utilise la non-linéarité pour réussir à compléter la tâche qui lui est donné
	- dans l'exemple pédagogique, les éléments du monde exterieur ne se ressemblent pas du tout.
		- Mais ces éléments étaient liés dans le réseau par une régularité entre eux et la sortie du réseaux
		- Dans la couche cachée, la déformation de l'espace d'entrée permet de répondre à la tâche, sans être pour autant une représentation ou un encodage spécifique des éléments d'entrée. -> pas de représentation forte.

# L'oubli catastrophique
**Définition** : Oubli dramatique des exemples antérieurement appris lors de l’apprentissage de nouveaux exemples.
- *Cause* : les anciens exemples ne contraignent plus la fonction de re-création. 
- *Conséquence* : Il faut continuer à présenter les anciennes connaissance pour contraindre la fonction -> Rafraîchissement
## Solution 1: McClelland et al. (1995)
- **Sans rafraîchissement**
- Conserver les exemples récents (Mémoire Tampon = Hippocampe ?) 
- Limiter l’oubli en ne les faisant que très peu apprendre par la mémoire principale (Cortex ?)
	- Solution très partielle, non viable à long terme
## Auto-rafraîchissement par pseudo-exemples
- Porblème: on ne dispose en général pas des exemples passés
- Solution: **à partir de bruit aléatoire**, **créer des pseudo-exemples (PE)** qui seront des exemples de la fonction de recréation.

Principe proposé par Robins, 1995:
- Calculer la sortie à partir d’un bruit aléatoire en entrée 
- Cette sortie **sera le résultat du traitement par la fonction de re-création**
	- *L’association entrée - sortie (PE) sera un reflet de la fonction*
	- ![[auto_rafraichisseemnet.png]]
	- Par exemple:![[creationde_PE_auto_rafraich.png]]

Méthode (Robins, 1995):
- Avant tout nouvel apprentissage, création d’un ensemble de PE 
- Stockage de ces PE dans une mémoire tampon 
- Apprentissage conjoint des nouveaux exemples et de ces PE 
	- **Les connaissances passées continuent à contraindre la fonction**

Deux limites:
- Une des structures (mémoire tampon) n’est pas neuromimétique 
- L’oubli-catastrophique n’est que partiellement résolu

Afin de palier à ces limites:
### Proposition 1: Deux structures connectionistes
Principe; Faire apprendre les pseudo-exemples à un second réseau.

![[prop_1_deux_structures.png]]
Le réseau principal est en contact direct avec l'environnement, le second réseau apprend uniquement sur des pseudo-exemples (PE) à partir du réseau principal (typiquement pendant la nuit). Ensuite, le réseau principal apprends les nouveaux exemples (réel, du monde extérieur) conjointement avec les pseudos exemples qui lui sont rappelés depuis le réseau secondaire (et donc de ses propres connaissances antérieures). 

Chaque réseau est à la fois un auto- et un hétéro- associateur, l'autoassociation est réalisée quelques fois avant de finalement donner la sortie (le PE) correspondant à la sortie de l'auto- et de l'hétéro-associateur.


Les deux réseaux sont typiquement les mêmes (différent système de celui de Nadel & Moscowitch car dans ce cas là, l'hypocampe garde les infos spécifiques, le cortex les infos générales. Ici, les deux réseaux ont des fonctions très proches/égales).


### Proposition 2: auto-association & reinjection

- *Objectif* : capture optimale de la structure de la fonction de re-création 
- *Principe* : contribution maximale de la structure dans les Pseudo-Exemples 
- *Méthode* : réinjection des sorties auto-associatives (**Réverbération**)
	- A partir d’un bruit aléatoire, la première sortie est le reflet des caractéristiques du bruit et de la structure 
	- La sortie auto-associative devient une nouvelle entrée 
	- La part de la structure est plus importante dans les sorties (auto et hétéro associatives ) résultant de cette réinjection
	- Enchaînement de plusieurs réinjections successives : **réverbération**

Chaque Pseudo-Exemple sera donc le résultat de plusieurs réinjections successives des Auto-Associations.


Autrement dit:
A partir des bruits aléatoires, en rebouclant sur le système, la sortie va tendre vers les exemples appris (dans le cas idéal): ![[Apprentissage_sys.png]]
En réalité, la courbe n'est pas nette comme ça, et à moins d'être très proche des exemples réels appris (A sur la figure ci-dessus), la convergence du système ne se fera pas forcément sur un souvenir réel. Mais plutôt sur des minimums locaux (point attracteurs), qui constitue d'excellent pseudo-exemples malgré qu'ils n'aient  pas été appris.


Dans toute cette partie, les connaissances/souvenirs... ne sont pas stockés en mémoire, mais sont retrouvé dans la "fonction" du réseau, à partir de pseudo-exemple (sans avoir besoin de retenir tous les anciens exemples dont le nombre tend vers l'infini au fil du temps). L'ensemble des exemples connus est retenu sous forme de réseau et non pas comme une ensemble d'éléments en mémoire.

*Finalement, l'ordre des choses apprise a une importance: lors de l'apprentissage de nouveaux exemples, ce n'est pas simplement l'exemple en soit qui est important, mais l'ensemble des connaissances préalables à cet exemple.*


## Résultats - Suppression de l'oubli catastrophique
**Cas d'école** (MacCloskey, 1989):
![[oubli_cata_fini.png]]
- Sans auto-raffraichissement: oubli catastrophique
- Avec auto-raffraichissement:
	- Sans réverbération: oubli partiel de l'ancienne base 
	- Avec réverbération: très peu d'oubli de l'ancienne base

# Et une fois que l'oubli catastrophique est réglé?
**Objectif**: Etudier l’apprentissage séquentiel de deux ensembles structurés ( transfert ?)

![[sans_oubli_cata_transfert.png]]
Encodage:
![[codage_no_oubli_.png]]

Résultats:
![[perf_max_add_octal_VS_decim.png]]
A droite, sans rafraichissement, il y a oubli catastrophique de la fonction max lors de l'apprentissage de la fonction oct-add.
A gauche, l'oubli catastrophique est bien moindre, parce qu'il y a des choses communes dans l'addition octale et dans l'addition décimale, ce qui n'est pas le cas entre les fonctions max-dec et oct-add.


### Généralisation
Dans le cas de généralisation, on apprend sur la base de 229 items de la base octale, et on test sur la généralisation aux 687 autres éléments de cette base.
![[generalisation_add_dec_oct.png]]
L'étoile correspond au cas où le pourcentage de réponse correcte est de 99% (arbitraire). On remarque qu'on observe pas de baisse de généralisation malgré un surapprentissage (parce que le signal d'entrée n'est absolument pas bruité).

 Sur la courbe verte, on a déjà appris add-dec; on remarque que la généralisation à add-oct est possible dès le premier cycle d'apprentissage. On considère (une interprétation possible est) que la règle de calcul est apprise (la structure du problème), et que sa transmission/son adaptation sur une nouvelle base est plus rapide. En réalité, le réseau de neurone n'as pas extrait la règle de calcul, pourtant, les résultats sont similaire à "si il l'avait fait".


### Résistance aux lésions
![[resist_lesion_.png]]


### Transfert d'information avec des pseudo-exemples
Articles de référence: Musca, Rousset & Ans, 2004

![[transfert_pseudo_ex.png]]
On test si le 2nd réseau a appris les mêmes choses (les vrais exemples) que le 1er réseau, alors qu'il n'a vu que les pseudo-exemples.
Pour tester cela sur les humains, on ne peux considérer que l'autoassociateur (pas de tâche possible pour mettre en évidence hétéro-association). On génère des PE simplement en présentant du bruit aléatoire/des éléments inconnus.
#### Choix des stimulis
- Ils doivent le moins possible reposer sur des apprentissages passés
- Génération de formes aléatoirement: ![[forme_PE_humain.png]]
- Les éléments sont ensuite testés afin d'être sûr qu'ils n'évoquent rien aux participants (pour ne pas se reposer sur des connaissances lors de l'apprentissage)
- Les différents items retenus sont séparés dans deux listes, une première servira à l'apprentissage d'un réseau de neurones (net1 dans l'image ci-dessus) (source), la seconde servira de jeu de test (contrôle).

- En plus de cela, on créer des pseudo-exemples, qui sont les seuls présentés à l'humain (et à net2); mais on les filtres pour ne garder que les items qui ressemble plus aux items control qu'au items source (donc plus proches de ceux qui n'ont jamais été observés).

#### Procédure
- Le net1 apprends sur les items source (de la liste 1)
- Puis on lui fait générer des pseudos-exemples.
- Parmis ces exemples on ne garde que ceux qui ressemblent visuellement aux items de controle.
- On entraine ensuite le Net 2/l'humain sur ces pseudos-exemples

#### Résultats attendus
- Si le système de mémoire humaine est basé sur des exemplaires/des prototypes, on devrait avoir de meilleures performances sur les éléments de contrôles (parce qu'on ne présente que des pseudo-exemples qui y ressemblent).

- Si en revanche la mémoire apprends plutôt la fonction du réseau et non pas les exemples/prototype, les performances devraient être meilleure sur les éléments de source (Liste 1), malgré la présentation d'éléments contrôle. (*pourquoi?? pas clair!*)

#### Résultats pour le net 2

![[resultats_l1_l2.png]]

On observe de meilleures performances sur les items sources que les items contrôles. Ce qui va plutôt dans le sens du fait que le système ait appris la fonction plutôt que le prototype.

#### Tâche et résultats chez l'humain
On présente un pseudo-exemple chaque 250ms pendant une phase d'apprentissage. Parfois, en plus d'un PE, une crois est présentée et le sujet doit appuyer sur un bouton (pour contrôler que le participant soit bien attentif à l'écran et qu'il s'adapte aux changements d'image).

On présente alors une ature tache aux sujets: 
- on présente un stimuli pendant une certaine durée (exemple long et court donné pour référence)
- le sujet doit répondre si la présentation est longue ou pas
- mais tous les stimulis sont en réalité presenté pendant la meme durée.

S'il les sujets ont une mémoire de l'item, ils auront tendance à avoir l'impression que le stimulus reste plus longtemps à l'écran car il le voit mieux/s'y adaptent plus vite.

![[resultat_humain.png]]
Les items sources sont bien indiqués comme apparaissant plus longtemps, donc sont mieux reconnu que les items contrôles.

#### Tâche alternative
j'ai pas écouté le protocole mais c'est des résultats similaires... 
- Plus d'occurrences sur les sources reconnues que sur les items contrôle.


#### Conclusion
Dans la mémoire humaine, il y a qqchose qui fontionne plutot comme un apprentissage d'hyperplan séparateur, plutôt que comme un apprentissage de prototype.