---
publish: true
---
![[filtrage_eeg.png]]

*Attention*:
- au filtrage avant les autres traitements, si on se *limite* à certaines *gammes de fréquences* on perd potentiellement beaucoup du signal. 
- Le filtrage *déforme* les artéfacts (et le signal d'intérêt), qui seront potentiellement plus difficile à discriminer par la suite.
- Le filtrage 'sans risque' typique serait : 
	- Retirer $50 Hz$ avec un filtre fente
	- Appliquer un passe bande sur $[0.5; 100] Hz$.