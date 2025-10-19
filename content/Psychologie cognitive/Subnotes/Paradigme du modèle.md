---
publish: true
---
On considère que les entrées sensorielles du système constituent des capteurs dont les états sont chacun continu sur une dimension. L'ensemble des entrées sensorielles a donc N dimensions, et le système, dans notre *exemple simple*, doit renvoyer l'*identité* ($f(x)=x$).
Si l'on réduit, par simplification, l'ensemble des dimensions d'entrée sur un seul axe et que l'on représente le taux d'erreur de notre système en réponse à un stimuli donné, on a:
![[Apprentissage_sys.png]]

Si l'on suppose un cas d'apprentissage de A', proche de A, le système va faire des erreurs, il aura tendance à recréer (le but étant l'identité) des éléments correspondant au point appris le plus proche (A): $A < f(A') < A'$ (si l'on a $A'>A$).

Le vrai critère de la mémoire est la *vitesse d'adaptation*, on parle de fluence perceptive.