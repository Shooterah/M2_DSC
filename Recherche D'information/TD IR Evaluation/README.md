## Exercice 1 : Accuracy, Precision, Recall and F-measure

### Calculs

#### Données fournies
- Nombre de documents pertinents récupérés (True Positives, TP) : 16
- Nombre de documents non pertinents récupérés (False Positives, FP) : 4
- Nombre de documents pertinents non récupérés (False Negatives, FN) : 84
- Nombre de documents non pertinents non récupérés (True Negatives, TN) : 1,000,000,000

#### Exactitude (Accuracy)
L'exactitude est le pourcentage de prédictions correctes (pertinents et non pertinents) parmi l'ensemble des prédictions.

$\text{Accuracy} = \frac{TP + TN}{TP + FP + FN + TN}$

$\text{Accuracy} = \frac{16 + 1,000,000,000}{16 + 4 + 84 + 1,000,000,000} \approx \frac{1,000,000,016}{1,000,000,104} \approx 0.999999912$

#### Précision (Precision)
La précision est le pourcentage de documents pertinents parmi ceux qui ont été récupérés.

$\text{Precision} = \frac{TP}{TP + FP}$

$\text{Precision} = \frac{16}{16 + 4} = \frac{16}{20} = 0.8$

#### Rappel (Recall)
Le rappel est le pourcentage de documents pertinents récupérés par rapport à tous les documents pertinents.

$\text{Recall} = \frac{TP}{TP + FN}$

$\text{Recall} = \frac{16}{16 + 84} = \frac{16}{100} = 0.16$

#### Mesure F1 (F-Measure avec β=1)
La mesure F1 est la moyenne harmonique de la précision et du rappel.

$F1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$

$F1 = 2 \times \frac{0.8 \times 0.16}{0.8 + 0.16} = 2 \times \frac{0.128}{0.96} \approx 0.2667$

### Conclusion
- Exactitude : Environ 0.999999912
- Précision : 0.8
- Rappel : 0.16
- Mesure F1 : Environ 0.2667

## Exercice 2 : Recall and Precision

### Calcul de la précision moyenne pour les deux systèmes

#### Système 1: R N R N N N N N R R
- Documents pertinents trouvés : 4
- Points où un document pertinent est trouvé : 1, 3, 9, 10
- Calcul de la précision à ces points :
  - Après 1er document : Précision = 1/1
  - Après 3e document : Précision = 2/3
  - Après 9e document : Précision = 3/9
  - Après 10e document : Précision = 4/10
- Précision moyenne pour Système 1 :

  $\frac{1}{1} + \frac{2}{3} + \frac{3}{9} + \frac{4}{10} = 1 + \frac{2}{3} + \frac{1}{3} + \frac{2}{5}$
  $\frac{5}{3} + \frac{2}{5} = \frac{25 + 6}{15} = \frac{31}{15} \approx 2.067$

#### Système 2: N R N N R R R N N N
- Documents pertinents trouvés : 4
- Points où un document pertinent est trouvé : 2, 5, 6, 7
- Calcul de la précision à ces points :
  - Après 2e document : Précision = 1/2
  - Après 5e document : Précision = 2/5
  - Après 6e document : Précision = 3/6 = 1/2
  - Après 7e document : Précision = 4/7
- Précision moyenne pour Système 2 :

  $\frac{1}{2} + \frac{2}{5} + \frac{1}{2} + \frac{4}{7}$
  $\frac{5}{10} + \frac{4}{10} + \frac{5}{10} + \frac{8}{14} = \frac{14}{20} + \frac{8}{14}$
  $\frac{14}{20} + \frac{8}{14} = \frac{7}{10} + \frac{4}{7} = \frac{49 + 40}{70} = \frac{89}{70} \approx 1.271$

### 2.1) Précision moyenne des deux systèmes
- Système 1: Environ 2.067
- Système 2: Environ 1.271

### 2.2) Classement des systèmes et importance pour une bonne précision moyenne
- Avec ces résultats, Système 1 est classé devant Système 2 en termes de précision moyenne.
- Pour obtenir une bonne précision moyenne, il est important de récupérer non seulement un grand nombre de documents pertinents, mais aussi de les récupérer le plus tôt possible dans la liste des résultats.


## Exercice 3 : Recall-Precision curves

### Calcul de la Précision et du Rappel pour Système 1
Représentation des jugements de pertinence : N R R N N R N R R R N N R N R R N R R R

#### Calculs pour chaque document

| Rang | Jugement | Documents Pertinents Trouvés (TP) | Total Récupérés (TP+FP) | Précision (TP / (TP + FP)) | Rappel (TP / 33)   |
|------|----------|----------------------------------|-------------------------|----------------------------|--------------------|
| 1    | N        | 0                                | 1                       | 0/1 = 0                    | 0/33 ≈ 0.00        |
| 2    | R        | 1                                | 2                       | 1/2 = 0.5                  | 1/33 ≈ 0.03        |
| 3    | R        | 2                                | 3                       | 2/3 ≈ 0.67                 | 2/33 ≈ 0.06        |
| 4    | N        | 2                                | 4                       | 2/4 = 0.5                  | 2/33 ≈ 0.06        |
| 5    | N        | 2                                | 5                       | 2/5 = 0.4                  | 2/33 ≈ 0.06        |
| 6    | R        | 3                                | 6                       | 3/6 = 0.5                  | 3/33 ≈ 0.09        |
| 7    | N        | 3                                | 7                       | 3/7 ≈ 0.43                 | 3/33 ≈ 0.09        |
| 8    | R        | 4                                | 8                       | 4/8 = 0.5                  | 4/33 ≈ 0.12        |
| 9    | R        | 5                                | 9                       | 5/9 ≈ 0.56                 | 5/33 ≈ 0.15        |
| 10   | R        | 6                                | 10                      | 6/10 = 0.6                 | 6/33 ≈ 0.18        |
| 11   | N        | 6                                | 11                      | 6/11 ≈ 0.55                | 6/33 ≈ 0.18        |
| 12   | N        | 6                                | 12                      | 6/12 = 0.5                 | 6/33 ≈ 0.18        |
| 13   | R        | 7                                | 13                      | 7/13 ≈ 0.54                | 7/33 ≈ 0.21        |
| 14   | N        | 7                                | 14                      | 7/14 = 0.5                 | 7/33 ≈ 0.21        |
| 15   | R        | 8                                | 15                      | 8/15 ≈ 0.53                | 8/33 ≈ 0.24        |
| 16   | R        | 9                                | 16                      | 9/16 = 0.56                | 9/33 ≈ 0.27        |
| 17   | N        | 9                                | 17                      | 9/17 ≈ 0.53                | 9/33 ≈ 0.27        |
| 18   | R        | 10                               | 18                      | 10/18 ≈ 0.56               | 10/33 ≈ 0.30       |
| 19   | R        | 11                               | 19                      | 11/19 ≈ 0.58               | 11/33 ≈ 0.33       |
| 20   | R        | 12                               | 20                      | 12/20 = 0.6                | 12/33 ≈ 0.36       |


### 3.1) Graphique de la Précision
- L'axe des ordonnées représente la précision.
- L'axe des abscisses représente le nombre de documents retournés.
- Chaque point du graphique représente la précision à un certain rang (par exemple, précision = 0.5 au rang 2).

### 3.2) Graphique du Rappel
- L'axe des ordonnées représente le rappel.
- L'axe des abscisses représente le nombre de documents retournés.
- Chaque point du graphique représente le rappel à un certain rang (par exemple, rappel = 1/33 au rang 2).

### 3.3) Graphique de la Mesure F1
- Utiliser la formule F1 = 2 * (Précision * Rappel) / (Précision + Rappel) pour chaque rang.
- Tracer la mesure F1 en fonction du nombre de documents retournés.

### 3.4) Courbe Rappel/Précision
- Tracer la précision en fonction du rappel pour les 20 premiers documents.

### 3.5) Courbe Rappel/Précision Interpolée
- Pour chaque point de rappel, utiliser la plus grande précision trouvée pour ce rappel ou pour un rappel supérieur.
- Tracer ces valeurs interpolées pour créer la courbe.

