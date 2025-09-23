---
publish: true
---

# Types d'effets
- *Effet principal*: c’est l’effet que produit une VI sur une VD, c’est-à-dire sans considération des autres potentiels facteurs (= VI).
- *Effet d'interaction*: c’est l’effet que produit une VI sur une VD dépendamment de l’état d’une seconde VI, en sachant que ça ne peut être le cas que lorsque ces VI ne sont pas additives : l’interaction est le produit d’une dépendance entre deux variables indépendantes produisant un effet sur une VD. Il ne s’agit pas d’une somme, le produit doit être différent de la somme des VI.
- *Effet simple*: c’est l’effet que produit une VI sur une VD, lorsqu’on ne considère qu’un seul niveau de l’autre VI. Autrement dit, c’est l’effet d’une VI sur une VD en supposant la constance d’une modalité de l’autre VI

# Taille d'effet
*d de Cohen* : Taille d'effet, ampleur de l'influence de notre VI sur notre VD normalisée par la variabilité dans l'échantillon; définie dans le cadre d'un test T de Student par : $d = \frac{M1 - M2}{S_p}$ avec $S_p$ l'erreur standard (écart-type..?).


et $$ t = \sqrt{n} * d = \frac{M1-M2}{\frac{S_p}{\sqrt{n}}} $$  
