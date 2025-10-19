---
publish: true
---
On considère la mémoire comme une matrice à j colonne, j correspondant au nombre de capteurs sensoriels. Les lignes correspondent au temps qui s'écoule, chaque case est donc l'état d'un capteur sensoriel à un instant donné. La mémoire enregistrerait donc des traces depuis la naissance, à une fréquence d'échantillonnage donnée. Dans notre modèle, tous les coefficients sont normalisés dans $[-1, 1]$.

![[MinervaII_matrice.png]]

Dans ce cadre:
- On appellera une "*sonde*" un ensemble de modalité des capteurs sensoriels avant d'être stocké dans la mémoire. 
- On appellera "*écho*" la sortie, calculée en fonction des différents éléments de la matrice.
- *L'idée d'accéder à une trace (ligne) particulière n'a pas de sens* (de par leur immense nombre, et similarité), *s'il y a un calcul, il devra impliquer toutes les traces*, de manière parallèle.

Le calcul se fait en deux étapes:
1. Activation de la trace *i*, en fonction de sa similitude à la *sonde*: $A(i)=\sum_{j=1}^{n} \frac{M(j)*S(j)}{n}$, ce calcul est effectué en parallèle pour chaque trace *i*. 
2. Détermination de l'*écho* comme moyenne de toutes les traces pondérées par leurs activations, pour chaque composante *j*: $E(j) = \frac{\sum_{i=1}^{n} A(i)*M(i,j)}{\|\sum_{i=1}^{n} A(i)\|}$  (Note: l'activation $A(i)$ peut être élevée à une puissance 'Acc' (impaire, pour conserver le signe), qui est un méta paramètre du modèle).


Dans l'ensemble, le processus complet pour chaque nouvelle stimulation est:
1. Stimulation (arrivée d'une *sonde*)
2. Calcul en deux étapes
3. La sonde *devient une trace* dans la mémoire; l'*écho est retourné*.

Finalement, on se retrouve avec *un système qui aura stocké une sémantique, sans jamais avoir stocké de représentation du monde*.