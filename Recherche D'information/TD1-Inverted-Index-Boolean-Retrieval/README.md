## Exercice 1 : Index Inversé et Recherche Booléenne

### Collection de Documents
1. Please Please Me
2. A Day in the Life
3. A Hard Day’s Night
4. Long, Long, Long
5. The Long and Winding Road
6. Love Me Do
7. Love You To
8. Please Mr. Postman

### Termes Uniques Identifiés
- Please
- Me
- A
- Day
- In
- The
- Life
- Hard
- Night
- Long
- And
- Winding
- Road
- Love
- You
- To
- Mr
- Postman

### Index Inversé avec Listes de Postings
- Please: [1, 8]
- Me: [1, 6]
- A: [2, 3]
- Day: [2, 3]
- In: [2]
- The: [5]
- Life: [2]
- Hard: [3]
- Night: [3]
- Long: [4, 5]
- And: [5]
- Winding: [5]
- Road: [5]
- Love: [6, 7]
- You: [7]
- To: [7]
- Mr: [8]
- Postman: [8]

### Matrice d'Incidence

| Term    | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---------|---|---|---|---|---|---|---|---|
| Please  | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Me      | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| A       | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| Day     | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| In      | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| The     | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| Life    | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| Hard    | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| Night   | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| Long    | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 |
| And     | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| Winding | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| Road    | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| Love    | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 |
| You     | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| To      | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| Mr      | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Postman | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |


## Exercice 2 : Complexité des Requêtes

### Contexte
- Collection de 1 million de documents.
- Évaluation de la complexité des requêtes suivantes.

### Requêtes Évaluées
1. Brutus AND NOT Caesar
2. Brutus OR NOT Caesar

### Analyse de Complexité

#### Requête 1 : Brutus AND NOT Caesar
- **Description**: Cette requête récupère les documents qui contiennent "Brutus" mais pas "Caesar".
- **Complexité Théorique**: 
  - Supposons que `x` est la longueur de la liste de postings pour "Brutus" et `y` est celle pour "Caesar".
  - La complexité pour trouver les documents contenant "Brutus" est `O(x)`.
  - La complexité pour identifier ceux qui ne contiennent pas "Caesar" dépend de la méthode utilisée. Si nous avons une liste de documents qui ne contiennent pas "Caesar", la complexité serait `O(y)`. Sinon, elle pourrait être plus importante car il faudrait parcourir potentiellement toute la collection.
  - La complexité totale ne serait pas nécessairement `O(x + y)` car l'opération "NOT" peut requérir un traitement additionnel.

#### Requête 2 : Brutus OR NOT Caesar
- **Description**: Cette requête récupère les documents qui contiennent "Brutus", ceux qui ne contiennent pas "Caesar", ou les deux.
- **Complexité Théorique**: 
  - La complexité pour identifier les documents contenant "Brutus" est `O(x)`.
  - Comme pour la requête précédente, identifier les documents ne contenant pas "Caesar" peut être complexe, en particulier si nous n'avons pas de liste préparée.
  - L'opération "OR" entre les deux ensembles est généralement moins complexe que "AND NOT", mais la complexité totale dépend toujours de la méthode utilisée pour traiter "NOT Caesar".

### Conclusion
- Pour les deux requêtes, la complexité théorique peut excéder `O(x + y)` en raison de la complexité intrinsèque de l'opération "NOT" dans une grande collection de documents.
- Des optimisations spécifiques ou des structures de données avancées pourraient être nécessaires pour traiter efficacement ces requêtes, en particulier pour la gestion de l'opération "NOT".


## Exercice 3 : Optimisation de l'Ordre de Traitement des Requêtes Booléennes

### Contexte
- Index inversé sur une collection de 0.5 million de documents.
- Statistiques de fréquence des termes observées :

| Terme         | Fréquence Documentaire |
|---------------|-----------------------|
| eyes          | 213312                 |
| kaleidoscope  | 87009                  |
| marmalade     | 107913                 |
| skies         | 271658                 |
| tangerine     | 46653                  |
| trees         | 316812                 |

### Requêtes Évaluées

#### Requête 1
- **Formulation**: (tangerine OR trees) AND (marmalade OR skies) AND (kaleidoscope OR eyes)
- **Optimisation Proposée**:
  1. **Étape Initiale**: Commencer par les termes avec la plus faible fréquence documentaire pour minimiser la taille initiale des ensembles de résultats. Ici, "tangerine" (46653) et "kaleidoscope" (87009).
  2. **Étape Intermédiaire**: Ensuite, traiter "marmalade" (107913) ou "trees" (316812), en commençant par le terme avec la fréquence la plus faible.
  3. **Étape Finale**: Traiter les termes restants, ici "skies" (271658) et "eyes" (213312), en les combinant avec les résultats des étapes précédentes.

#### Requête 2
- **Formulation**: tangerine AND (NOT marmalade) AND (NOT trees)
- **Optimisation Proposée**:
  1. **Étape Initiale**: Commencer par "tangerine" (46653) car c'est le seul terme positif et a la plus faible fréquence.
  2. **Étapes Suivantes**: Appliquer les opérations "NOT" sur "marmalade" (107913) et "trees" (316812). Cela pourrait être complexe car "NOT" nécessite potentiellement de traiter tous les documents de la collection.
  3. **Traitement Combiné**: Combiner les résultats de "tangerine" avec les ensembles complémentaires de "marmalade" et "trees".

### Conclusion
- Pour les deux requêtes, l'ordre de traitement recommandé vise à minimiser la taille des ensembles intermédiaires, en commençant par les termes avec les plus faibles fréquences documentaires.
- L'opération "NOT" dans la Requête 2 présente des défis uniques en termes de complexité et devrait être gérée avec précaution.
