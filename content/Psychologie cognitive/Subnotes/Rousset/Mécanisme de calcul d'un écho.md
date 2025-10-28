---
publish: true
---
1. **Activation des traces**  
    Activation de la trace *i*, en fonction de sa similitude à la *sonde*: $A(i)=\sum_{j=1}^{n} \frac{M(j)*S(j)}{n}$, ce calcul est effectué en parallèle pour chaque trace *i*. 
    
2. **Calcul de l’écho**  
    Détermination de l'*écho* comme moyenne de toutes les traces pondérées par leurs activations, pour chaque composante *j*: $E(j) = \frac{\sum_{i=1}^{n} A(i)*M(i,j)}{\|\sum_{i=1}^{n} A(i)\|}$  (Note: l'activation $A(i)$ peut être élevée à une puissance 'Acc' (impaire, pour conserver le signe), qui est un méta paramètre du modèle). 
3. La sonde *devient une trace* dans la mémoire; l'*écho est retourné*.    

Le paramètre “_acc_” (puissance appliquée à A) module la précision du rappel :  
valeurs élevées → récupération **spécifique** (épisodique),  
valeurs faibles → récupération **générale** (sémantique).
`ex:`

| Trace/Activation   | A   | $A^3$ |
| ------------------ | --- | ----- |
| trace 1            | 2   | 8     |
| trace 2            | 4   | 64    |
| Ratio d'activation | *2* | *8*   |