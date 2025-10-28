---
publish: true
---
1. **Normalité** : les résidus doivent suivre une loi normale.  
    → Vérifié via Q-Q plot (si points alignés = normalité respectée).  
    → Sinon : transformation (ex. log).
    
2. **Indépendance** : les observations ne doivent pas être corrélées entre elles.
    
3. **Homogénéité des variances** : variances égales entre groupes.  
    → Sinon : utiliser **test de Welch** ou **test U de Mann–Whitney** (non paramétrique, sans interaction possible).