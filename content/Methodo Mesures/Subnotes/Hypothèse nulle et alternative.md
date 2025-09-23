---
publish: true
---

L'hypothèse nulle ($H_0$) correspond à l'hypothèse d'absence d'effet de notre VI sur notre VD ($\mu_{1}= \mu_2$), on est alors dans le cas par défaut, et la variabilité observée pour la VD est celle du hasard, dont la distribution suit une loi normale:

```functionplot
---
title: 
xLabel: 
yLabel: 
bounds: [-3,3,0,1]
disableZoom: true
grid: true
---
f(x)=exp(-x^2)

```

L'hypothèse alternative ($H_1$) correspond à celle où la VI a une influence sur la VD (ex: $\mu_{1}\neq \mu_2$).

*On suppose alors que les deux hypothèses sont complémentaires l'une de l'autre donc rejeter l'une revient à accepter l'autre: on va chercher à rejeter $H_0$.