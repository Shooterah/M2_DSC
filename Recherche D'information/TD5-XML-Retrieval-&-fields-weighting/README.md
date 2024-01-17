## Exercice 5 : Extension Simple de BM25 pour Plusieurs Champs Pondérés [Robertson2004]

### Questions et Réponses

1. **Qu’est-ce que C ?**
   - C représente une collection de documents non structurés. Un document non structuré `d¯` appartenant à C peut être vu comme un vecteur `d¯= (d1 ... dV )`, où `dj` indique la fréquence du terme j dans `d¯` et V est le nombre total de termes dans le vocabulaire.

2. **Qu’est-ce que V ?**
   - V est le nombre total de termes dans le vocabulaire d'un document non structuré dans la collection C.

3. **Qu’est-ce que d¯ ?**
   - `d¯` représente un document non structuré dans la collection C, considéré comme un vecteur de fréquences de termes.

4. **Qu’est-ce que dj ?**
   - `dj` est la fréquence du terme j dans le document `d¯`.

5. **Qu’est-ce que dfj ?**
   - `dfj` est la fréquence documentaire du terme j, c'est-à-dire le nombre de documents dans lesquels le terme j apparaît.

6. **Qu’est-ce que wj(d¯,C) ?**
   - `wj(d¯,C)` est une fonction de pondération de terme dans le contexte d'un document `d¯` et de la collection C. Elle exploite la fréquence du terme ainsi que d'autres facteurs tels que la longueur du document et les statistiques de la collection.

7. **Qu’est-ce que qj ?**
   - `qj` est la pondération d'un terme dans la requête.

8. **Qu’est-ce que W(d¯, q, C) ?**
   - `W(d¯, q, C)` est une fonction de classement standard qui étend à une nouvelle fonction `W(d, q, C, v)`, en tenant compte des poids des différents champs d'un document structuré.

9. **Qu’est-ce que K ?**
   - K représente le nombre de types de champs dans une collection de documents structurés. Par exemple, un champ pourrait être le titre, un autre le résumé, etc.

10. **Qu’est-ce que d[2]¯ ?**
    - `d[2]¯` représenterait le deuxième champ (par exemple, l'abstract) d'un document structuré.

11. **Qu’est-ce que d ?**
    - d est un document structuré représenté comme une matrice ou un vecteur de vecteurs, où chaque vecteur représente un champ différent dans le document.

12. **Qu’est-ce que v ?**
    - v est le vecteur de poids des champs dans un document structuré. Il sert à pondérer différemment les champs lors du classement d'un document.

13. **Qu’est-ce que W(d, q, C, v) ?**
    - `W(d, q, C, v)` est une fonction de classement qui étend une fonction de classement standard pour les documents structurés en tenant compte des poids des champs.

14. **Qu’est-ce que W1(d, q, C, v) ?**
    - `W1(d, q, C, v)` est une combinaison linéaire des scores obtenus pour chaque type de champ d'un document structuré, en utilisant les poids des champs.

15. **Liste des problèmes posés par W1(d, q, C, v) ?**
    - Les problèmes posés par `W1(d, q, C, v)` incluent la perte de la non-linéarité de la fréquence des termes et des difficultés d'interprétation et de gestion de la longueur des documents et des statistiques de la collection.

16. **Qu’est-ce que d’ ?**
    - d’ représenterait une variante ou une modification du document d, probablement dans le contexte de l'application d'une méthode de classement ou de pondération différente.

17. **Qu’est-ce que C’ ?**
    - C’ représenterait une collection modifiée ou alternative de documents, par exemple après l'application d'une méthode de classement différente.

18. **Qu’est-ce que W2(d, q, C, v) ?**
    - `W2(d, q, C, v)` est une méthode proposée pour combiner les fréquences des termes des différents champs d'un document structuré, en formant une combinaison linéaire pondérée par les poids des champs.

19. **Avantages de W2(d, q, C, v) ?**
    - Les avantages de `W2(d, q, C, v)` incluent la préservation de la non-linéarité des fréquences des termes et une interprétation plus simple des statistiques de la collection et de la longueur des documents.

20. **Comment fixer k1 et b dans W2 ?**
    - Les auteurs suggèrent de fixer k1 et b en se basant sur la fréquence moyenne des termes, en ajustant k1 proportionnellement au poids des champs.

21. **Limites de W2(d, q, C, v) ?**
    - Les limites de `W2(d, q, C, v)` ne sont pas explicitement mentionnées dans les extraits disponibles, mais pourraient inclure des complexités liées à l'ajustement des paramètres et à la gestion des différents types de champs dans des collections complexes.

22. **Optimisation des paramètres de W1 et W2 ?**
    - L'optimisation des paramètres de W1 et W2 n'est pas détaillée dans les extraits disponibles.

23. **Risque de sur-apprentissage ?**
    - Les auteurs soulèvent le risque de sur-apprentissage lié à l'optimisation des paramètres de classement, en particulier lors de l'utilisation de méthodes complexes ou de collections de données limitées.

24. **Confirmation des avantages par expérimentation ?**
    - Les expérimentations semblent confirmer les avantages de la méthode proposée, notamment en termes d'amélioration de la précision et de la gestion des dépendances entre les termes dans différents champs.
