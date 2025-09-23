---
publish: true
---

On suppose :
- *Normalité*: les distributions des résidus (différences entre chaque individu et son groupe) doivent être normales. (visible graphiquement par Q-Q plot, graphique Quantile par Quantile, si les résidus sont réparties selon une loi normale, les échantillons apparaissent le long de la ligne sur le Q-Q plot.) (*Si non respect: transformer les données*, par exemple avec une fonction log pour restaurer la normalité)
- Indépendance: Euuuh plus dur à expliquer on skip.. 
- *Homogénéité*: les variances des différents groupes doivent être égales (afin que la seule différence entre les groupes soit bien leur moyenne (T-test)) -> Permet une interprétation correcte des résultats. (*Si non respect : Test de Welch*, peu apprécié plutôt que Student, sinon *U de Mann&Whitney*, Note : pas de test d'interaction pour ces tests non paramétriques.)