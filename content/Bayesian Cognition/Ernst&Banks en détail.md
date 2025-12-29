---
publish: true
---
> [!NOTE] Examen
> Ernst et Bankd 2022, souvent des idées demandées au partiel!

"Humans integrate visual and haptic information in a statistically optimal fashion", 2002

#### Principe général
On s'intéresse aux mécanisme d'intégration visuo-haptique pour l'estimation de la taille d'un objet (qui est donc vu et manipulé manuellement).
Chaque modalité d'intégration est représenté par une gaussienne, on s'interesse à la manière dont les deux sont intégrées ensemble:
![[haptic_visual_integ_principe.png]]
Dans la manipulation, les auteurs font varier la qualité (étalement de la gaussienne) de chaque capteur (visuel et haptique) et voient comment le système doit s'adapter pour obtenir malgré tout le meilleur résultat possible (on veut pondérer plus fort le capteur de meilleur qualité, par rapport à l'autre).

Sur la figure ci-dessus, à gauche, l'axe des abscisses donne le niveau de bruit visuel présenté, on voit la répartition d'utilisation des capteurs visuel ou haptique sur l'axe des ordonnées. On prédit qu'en cas de bruit visuel fort, le capteur haptique va être davantage utilisé par rapport au capteur visuel.


#### Protocole expérimental

![[hapti_vis_protocole.png]]
Comme il est impossible d'avoir un objet qui ait une taille différente visuellement que sa taille au touché, on présente aux sujets des objets 'virtuels' grâce au dispositif présenté dans l'image ci-dessus.
L'objet cible est présenté via un robot 'phantom', selon la position du robot, il est possible d'appliquer des forces dans certaines directions (pour faciliter/rendre plus difficile les mouvements). En réalité, il n'y a pas d'objet mais des coordonnées dans l'espace qui provoque des forces résistantes (programmation du robot). La manipulation se fait à deux doigts, qui ne peuvent pas s'approcher selon les règles définies par le robot.

En terme de stimulation visuelle:
![[stimuli_visuel_haptic_visu.png]]
Elle est basé sur des lunettes stéréo, on présente au sujet un stéréogramme qui lui permet d'estimer visuellement une barre parmi des points qui sont à différente profondeur (3cm normalement, et 3cm-barre sous la barre).

Le niveau de bruit visuel est obtenu en faisant bouger les points en profondeur de manière aléatoire (avec une amplitude définie telle que 100% de bruit corresponde à 3cm de profondeur de variation aléatoire).

**Stimuli et tâche**:
- 4 niveaux de bruit visuel (0, 67, 133, 200)
- 1 niveau haptique
- 1s de présentation
- Tâche de choix forcé, la quelle de ces deux barres est la plus grande?
	- **Cas mono-modal**
		- Permet de calibrer le modèle.
		- 2 barres en séquence
			- l'une à 55mm (stimulus standard)
			- l'autre à 47-63mm, taille variable (stimulus de comparaison)
		- ![[mono_modal_result.png]]
		- En ordonnée ci-dessus, on représente la proportion de fois où la barre variable a été annoncé comme "plus grande". 
			- On considère le point de discrimination (JND) comme étant à 85% (environ 5mm ici).
			- On considère le Point of Subjective Equality (PSE) comme étant celui où les barres sont confondues le plus souvent (50%, qui arrive bien quand les deux barres font la même taille ici).
			- On remarque que moins il y a de bruit, plus on se rapproche de la courbe idéale (créneaux), à partir de 133% de bruit (67% de bruit ne semble pas avoir d'influence sur l'indice de discrimination).
			- Par hasard, la courbe haptique se superpose exactement avec le niveau de bruit 133%.
	- **Cas multi-modal**:
		- ![[multi_modal_pres.png]]
		- Une barre est présentée visuellement, et une barre est présentée haptiquement. On a à nouveau un stimulus standard et un stimulus de comparaison.
			- Pour la *barre standard*: la différence de taille des barres visuelles et haptiques présentée est de 0, 3 ou 6 mm. Par manipulation et renormalisation des données, on peut se retrouver dans un cas où la différence entre haptique et visuelle est (en équivalence) toujours telle que la taille haptique soit plus faible que la taille visuelle (pour faciliter la représentation graphique).
			- Pour la *barre de comparaison*, il n'y a jamais de discongruence entre sa présentation haptique et visuelle, elle varie simplement de 47 à 63mm.
		- ![[multi_modal_result.png]]
			- A 67% de bruit, pas de différence comme prévu dans le monomodal
			- A 133% on avait vu que le systeme haptique était équivalent au systeme visuel, ici, on remarque que la courbe se décale vers la gauche pour s'équilibrer avec un PSE (correctement) à 55mm.
			- Au dela, le système haptique "prend le pas" sur le système visuel, la courbe se décale encore.