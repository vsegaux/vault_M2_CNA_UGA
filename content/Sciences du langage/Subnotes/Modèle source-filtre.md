---
publish: true
---
L'acoustique de la parole est souvent basée sur le modèle source-filtre suivant:

![[sourcefiltre.png]]

### Source
La source de la parole est le voisement, qui correspond à la mise en vibration de nos cordes vocales:
![[voiseement_cordevoc.png]]

La fréquence produite peut varier de 70 à 250Hz environ selon les personnes. La *fréquence de vibration* des *cordes vocales* est appelée *fréquence fondamentale* (F0).

Au niveau fréquentiel:
![[freq_H_F.png]]
La première 'barre' correspond à la fréquence fondamentale et les barres successives suivantes correspondent à ses multiples. Si la fréquence fondamentale est grave (pour un homme typiquement), les différentes barres seront plus rapprochées les unes des autres.

Afin de produire différents son, le conduit vocal va venir filtrer la production de la source:

![[source_filtre_out.png]]

On appelle **formants** les 'pics' sur la fonction de transfert du filtre, ils correspondent aux fréquences qui sont amplifiées par rapport au reste du signal (le trait plein sur la figure suivante correspond à l'*envolope spectrale*):
![[shoafreqspectr.png]]
Pour représenter l'évolution de l'amplitude des fréquences au cours du temps, on utilise un *spectrogramme*, sur lequel l'amplitude est représentée en niveau de gris (ou couleur selon les cas).