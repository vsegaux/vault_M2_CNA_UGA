---
publish: true
---

Niveaux de compréhension
"Marr "[[2024-2025-Rousset-Partie-1.pdf#page=6&selection=20,0,20,5|p.6]] : 3 niveaux de compréhension d'une machine

| Marr                      | Marr                             | Exemple Aspirateur  | Psychologie                             |
| ------------------------- | -------------------------------- | ------------------- | --------------------------------------- |
| **Niveau computationnel** | But de la machine                | Aspirer             | Traiter le monde/Intégrer l'information |
| **Niveau algorithmique**  | Par quels principes/outils       | Ventilateur         |                                         |
| **Niveau implémentation** | Bas niveau, composants 'de base' | Moteur, Electricité |                                         |

*Implémentation*: On prend les 'briques de bases' du fonctionnement humain et on les fait fonctionner sur d'autres supports (typiquement ordinateur, machine à ressort historiquement). Par exemple des réseaux de neurones. Au niveau de l'implémentation, les modèles proposés sont le plus simple possible (typiquement séquentiels). L'implémentation *décrit les règles des mécanismes* et peut *simuler leur fonctionnement*. L'implémentation ne peut en aucun cas valider le fonctionnement humain, on en a simplement *besoin pour faire des hypothèses*, des prédictions. Il sert de support, d'aide pour le niveau algorithmique.

Exemple:
On prend un stimulus de base (prototype, P), un nuage de point et on en créé des dérivations ($D_{1}, ..., D_n$) en faisant bouger certains points. Les participants ne voient que les dérivations.
On laisse passer un certain temps et on réalise un expérience de mémoire en présentant aux participants:
- certaines dérivations présentée initialement ($D_x$)
- certains nuages de points jamais vus (N)
- le prototype qui n'a jamais été vu (P)
Le participants doivent dire oui s'il ont déjà vu le stimulus présenté.

| Situation | Bonne réponse | Réponse observée |
| --------- | ------------- | ---------------- |
| $D_x$     | OUI           | OUI              |
| N         | NON           | NON              |
| P         | NON           | *OUI*            |
*Effet de supériorité du prototype jamais vu.* Lors de la phase d'apprentissage, les participants se sont formé une représentation de la structure globale des stimuli présentés, qui correspond finalement au prototype. Ils répondent de manière plus rapide et avec plus de certitudes lors de la présentation du prototype pendant la phase de test.
