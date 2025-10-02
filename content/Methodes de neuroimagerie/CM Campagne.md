---
prof: CAMPAGNE Aurélie
date: 2025-09-29
publish: true
---
 
> [!NOTE] Examen
> Question de cours + application; question de méthodo
> ++ Typiquement une étude présentée et il faut être capable de dire, pour les aspects méthodo: pourquoi/à quoi ça sert/quels sont les limites,risques associés


# Introduction
Cours de neuroimagerie; mesures de surfaces EEG et MEG.

## Anatomie du cerveau
![[Anatomie du cerveau]]
## Organisation fonctionnelle
![[Organisation fonctionnelle]]
## Organisation cérébrale

Le cerveau est constitué du cortex (substance grise) au niveau de sa partie extérieure. Les différentes régions du cortex sont reliées par des fibres (matière blanche):
- Fibres d'association: entre différentes zones d'un même hémisphère
- Fibre commissurales: entre les deux hémisphères
- Fibres de projection: entre le cerveau et les structures sous-jacentes

![[couches_fibres.png]]

Le cortex lui-même est constitué de six couches différentes, numérotées de l'extérieur vers l'intérieur:
- Couches 2 et 4: beaucoup de cellules *étoilées*, dont le rôle est de traiter l'*information qui arrivent* depuis les autres zones du cerveau/système nerveux.
- Couches 3 et 5: beaucoup de cellules *pyramidales*, dont le rôle est l'*intégration et la transmission d'information des autres couches*.

### Structure et fonctionnement du neurone
![[Structure et fonctionnement du neurone]]
# Les techniques d'imagerie
![[Les techniques d'imagerie]]

# Nature, origine et topographie des signaux EEG de surface et MEG
![[Nature, origine et topographie des signaux EEG de surface et MEG]]

## Activités oscillatoires

![[rythmes.png]]

### Origine des signaux
![[Origine des signaux]]
### Dipoles en EEG et en MEG
![[Dipoles en EEG et en MEG]]

### Sensibilité
![[Sensibilité EEG - MEG]]
### Cas des sources multiples
Les observations réalisées en surface sont la résultante de la somme de plusieurs macro-dipôles. Exemple: dans le cas d'une onde auditive perçue, on a de fortes activation sur le dessus du crâne alors que ces zones ne sont pas impliquées dans son traitement.

## Résumé EEG-MEG
![[Résumé EEG-MEG]]

# Dispositifs et principe de mesure des signaux

## MEG
![[Dispositif MEG]]
## EEG
![[Electrodes et disposition]]
### Dispositif de mesure de la position du casque par rapport à la tête

Idéalement, il faudrait un IRM du cerveau du patient. Certaines références ont été créée à partir de moyenne sur 1000 cerveaux sinon. La position précise des électrodes est reconstruite numériquement par rapport aux points de référence (Nasion, Péri-auriculaire Droit et Gauche) et au contour de la peau.

# Protocoles d'étude et traitement des données

Selon les études et les chercheurs, les différentes méthodes de pré-traitement des données peuvent être réalisées dans des ordres variés. Certains points sont à considérer:
- Filtrage: risque de perte d'information du signal utile selon les bandes de fréquences filtrées
- Segmentation: peut être appliquée avant ou après le pré-traitement:
	- Avant: permet de ne pré-traiter que les portions utiles, attention dans ce cas à segmenter des morceaux plus longs que strictement les morceaux utiles afin d'éviter les effets de bords de filtrages
	- Après: Permet d'éviter les effets de bords, attention toujours à la cohérence temporelle des différents pistes/patients entre elles.
## Pré-traitement des données

![[Pré-traitement des données]]

## Traitement des données

![[Traitement des données]]