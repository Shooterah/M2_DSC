# Résumé pour le Partiel de IR

## IR Model & Boolean Retrieval

### 1.1 Information Retrieval (IR)
- **Définition**: La récupération d'information (IR) concerne la recherche de matériel (généralement des documents textuels) qui répond à un besoin d'information dans de grandes collections.
- **Applications**: Recherche sur le web, recherche d'emails, bases de connaissances d'entreprise, recherche d'informations juridiques.
- **Exemple**: Trouver des articles sur "le changement climatique" dans une bibliothèque numérique.

### 1.2 IR Model & IR System
- **Différence IR/DR**: IR traite des données non structurées (texte libre) avec des requêtes par mots-clés, alors que DR concerne les données structurées (tables) avec des requêtes sur des plages numériques ou des correspondances exactes.
- **Exemple IR**: Recherche de "recettes de gâteaux sans gluten" dans un forum de cuisine.
- **Exemple DR**: Recherche dans une base de données d'employés ceux avec un salaire > 50 000 €.

### 1.3 Indexation: Inverted Index
- **Inverted Index**: Structure de données où pour chaque terme, une liste de tous les documents le contenant est conservée.
- **Construction d'Inverted Index**: Inclut la tokenisation, le traitement linguistique, et l'organisation en un dictionnaire et des listes de postages.
- **Exemple**: Pour "économie", l'index inversé montre tous les documents contenant ce terme.

### 1.4 Querying: Boolean Retrieval
- **Boolean Retrieval**: Utilise des opérateurs logiques (AND, OR, NOT) pour combiner les termes de recherche.
- **Traitement des requêtes**: Localisation de chaque terme dans le dictionnaire, récupération et fusion de leurs postages.
- **Exemple**: La requête "économie AND politique" renvoie des documents contenant à la fois "économie" et "politique".

### 1.5 Exemples Supplémentaires
- **Utilisation de l'Inverted Index**: Supposons une base de données de documents contenant les mots "informatique", "programmation" et "algorithmes". L'index inversé pour "algorithmes" listerait tous les documents où ce terme apparaît.
- **Requête Booléenne Complexe**: Une requête comme "informatique NOT théorie" chercherait des documents contenant "informatique" mais exclurait ceux contenant également "théorie".


##  Pre-Processing & Dictionary

### 2.1 Indexing and Inverted Index
- **Inverted Index**: Structure essentielle en RI pour stocker, pour chaque terme, une liste de tous les documents le contenant.
- **Objectif**: Permettre une recherche rapide dans une grande collection de documents.

### 2.2 Terms: Tokenization
- **Tokenization**: Processus de découpage d'un texte en tokens (mots).
- **Exemple**: Le texte "Amis, Romains, citoyens" devient les tokens ["Amis", "Romains", "citoyens"].

### 2.3 Stop-Words Removal
- **Stop-Words**: Mots courants avec peu de contenu sémantique (ex: "le", "et").
- **Raison**: Éliminer les mots vides réduit la taille de l'index et améliore l'efficacité de la recherche.

### 2.4 Normalization
- **But**: Traiter les variantes d'un terme comme équivalentes (ex: "U.S.A." et "USA").
- **Méthodes**: Suppression des points, des traits d'union, etc.

### 2.5 Stemming
- **Stemming**: Réduction des mots à leur forme de base ou racine.
- **Algorithme de Porter**: Méthode populaire pour l'anglais.

### 2.6 Statistics: Heaps' Law and Zipf's Law
#### Heaps' Law
- **Formule**: \( M = kT^b \)
  - \( M \): Nombre de termes uniques.
  - \( T \): Nombre total de tokens.
  - \( k, b \): Constantes spécifiques à la collection.
- **Implication**: Plus la collection de documents est grande, plus le nombre de termes uniques est élevé.

#### Zipf's Law
- **Formule de base**: La fréquence du \( i \)-ème terme le plus fréquent est proportionnelle à \( \frac{1}{i} \).
- **Explication**: Dans une langue naturelle, quelques termes sont extrêmement fréquents (comme "le", "et"), alors que la majorité des termes sont rares.
- **Exemple**: Dans une collection de documents, le terme le plus fréquent pourrait apparaître des milliers de fois, le deuxième terme le plus fréquent à peu près la moitié de ce nombre, et ainsi de suite.
- **Implications pour l'indexation**: Les termes très fréquents et très rares sont généralement de mauvais candidats pour l'indexation, car ils n'aident pas à distinguer efficacement les documents les uns des autres.

### 2.7 Practice
- **Application pratique**: Analyse de collections comme Reuters RCV1 et la collection Wikipedia d'INEX 2006 pour observer les lois de Heaps et Zipf en action.


## Ranked Retrieval

### 3.1 Scoring as the Basis of Ranked Retrieval
- **Définition**: Le classement des résultats est basé sur l'assignation d'un score à chaque paire requête-document, reflétant la pertinence du document par rapport à la requête.
- **Exemple**: Un document contenant plusieurs fois le terme de la requête aura un score plus élevé qu'un document où le terme apparaît moins fréquemment.

### 3.2 Term Frequency (tf)
- **Définition**: La fréquence d'un terme dans un document, utilisée pour mesurer son importance dans ce document.
- **Calcul**: `tf(t, d)` = (Nombre de fois que le terme `t` apparaît dans le document `d`) / (Nombre total de termes dans le document).
- **Exemple**: Si le terme "économie" apparaît 3 fois dans un document de 100 mots, `tf("économie", document)` = 3/100 = 0.03.

### 3.3 Document Frequency (df)
- **Définition**: La fréquence d'un terme dans l'ensemble de la collection de documents, indiquant sa rareté ou sa fréquence.
- **Calcul**: `df(t)` = Nombre de documents contenant le terme `t`.
- **Exemple**: Si "économie" apparaît dans 50 documents sur 1000, `df("économie")` = 50.

### 3.4 Vector Space Model
- **Principe**: Représentation des documents et des requêtes comme des vecteurs dans un espace multidimensionnel, où chaque dimension correspond à un terme distinct.
- **Utilité**: Permet de calculer la similarité entre documents et requêtes en utilisant des mesures comme la similarité cosinus.

### 3.5 tf.idf Variants
- **Définition**: Poids tf-idf d'un terme est le produit de sa fréquence dans un document (tf) et l'inverse de sa fréquence dans les documents (idf).
- **Formule**: `tf-idf(t, d)` = `tf(t, d)` x `idf(t)`, où `idf(t)` = log(N / `df(t)`).
- **Exemple**: Pour un terme apparaissant dans 3 documents sur 1000, son poids tf-idf sera plus élevé, montrant son importance relative dans le document.

### 3.6 Jaccard Coefficient
- **Définition**: Mesure de la similarité entre deux ensembles, souvent utilisée pour comparer la similitude entre un ensemble de termes dans une requête et un ensemble de termes dans un document.
- **Calcul**: `Jaccard(A, B)` = `|A ∩ B| / |A ∪ B|`, où `A` et `B` sont des ensembles de termes.
- **Exemple**: Si une requête contient les termes {a, b} et un document contient les termes {a, b, c, d}, alors `Jaccard(requête, document)` = `|{a, b} ∩ {a, b, c, d}| / |{a, b} ∪ {a, b, c, d}|` = `2 / 4` = 0.5.

### 3.7 Log-Frequency Weighting
- **Définition**: Une méthode de pondération qui utilise le logarithme de la fréquence d'un terme pour modérer l'impact des fréquences de termes élevées dans les calculs de pertinence.
- **Calcul**: `log-weight(t, d)` = 1 + log(`tf(t, d)`), si `tf(t, d)` > 0; sinon 0.
- **Exemple**: Si le terme "économie" apparaît 10 fois dans un document, `log-weight("économie", document)` = 1 + log(10) = 2.3 (en supposant un logarithme de base 10).

### 3.8 Relevance Status Value (RSV)
- **Définition**: Un score calculé pour un document par rapport à une requête, représentant la somme des poids des termes qui sont communs à la fois à la requête et au document.
- **Calcul**: `RSV(Q, D)` = Σ `weight(t, D)`, pour tous les termes `t` dans la requête `Q` et le document `D`.
- **Exemple**: Pour une requête contenant les termes {a, b} et un document où `weight(a, D)` = 0.8 et `weight(b, D)` = 0.5, `RSV(Q, D)` = 0.8 + 0.5 = 1.3.

### 3.9 Cosine Similarity between Query and Document
- **Définition**: La similarité cosinus est une mesure qui calcule l'angle cosinus entre deux vecteurs non nuls dans un espace multidimensionnel, souvent utilisée pour mesurer la similarité entre un document et une requête dans le modèle d'espace vectoriel.
- **Calcul**: `cosine_similarity(Q, D)` = (Σ `tf-idf(t, Q)` x `tf-idf(t, D)`) / (||Q|| x ||D||), où `Q` est le vecteur de la requête, `D` est le vecteur du document, et `||X||` est la norme du vecteur `X`.
- **Norme d'un vecteur**: Calculée comme la racine carrée de la somme des carrés de ses composants. Pour un vecteur `X`, `||X||` = √(Σ `X[i]²`).
- **Exemple**:
  - Soit une requête `Q` avec des poids tf-idf: {a: 0.8, b: 0.5} et un document `D` avec des poids tf-idf: {a: 0.5, b: 0.3, c: 0.6}.
  - Le produit scalaire de `Q` et `D` est (0.8 x 0.5) + (0.5 x 0.3) = 0.4 + 0.15 = 0.55.
  - La norme de `Q` est √(0.8² + 0.5²) = √(0.64 + 0.25) = √0.89 ≈ 0.94.
  - La norme de `D` est √(0.5² + 0.3² + 0.6²) = √(0.25 + 0.09 + 0.36) = √0.7 ≈ 0.84.
  - La similarité cosinus entre `Q` et `D` est donc 0.55 / (0.94 x 0.84) ≈ 0.55 / 0.79 ≈ 0.70.

### 3.10 SMART 'ltc' Model
- **Définition**: Le modèle SMART 'ltc' est une méthode de pondération dans le modèle d'espace vectoriel. 'l' représente la fréquence logarithmique du terme, 't' l'inverse de la fréquence documentaire, et 'c' la normalisation cosinus.
- **Calcul**:
  - **Fréquence logarithmique du terme (l)**: `log-tf(t, d)` = 1 + log(`tf(t, d)`) si `tf(t, d)` > 0, sinon 0.
  - **Inverse de la fréquence documentaire (t)**: `idf(t)` = log(N / `df(t)`).
  - **Normalisation Cosinus (c)**: Diviser chaque composant du vecteur document par la norme du vecteur.
- **Formule complète**: `ltc(t, d)` = `log-tf(t, d)` x `idf(t)` / ||D||, où ||D|| est la norme du vecteur document.
- **Exemple**:
  - Supposons un document `D` contenant les termes {"machine": 3, "apprentissage": 2} dans une collection de N=1000 documents, où "machine" apparaît dans 100 documents et "apprentissage" dans 50.
  - `log-tf("machine", D)` = 1 + log(3) ≈ 1.48, `idf("machine")` = log(1000/100) = 2.
  - `log-tf("apprentissage", D)` = 1 + log(2) ≈ 1.30, `idf("apprentissage")` = log(1000/50) ≈ 2.30.
  - Le vecteur non normalisé de `D` serait alors {"machine": 2.96, "apprentissage": 2.99}.
  - La norme de ce vecteur est √(2.96² + 2.99²) ≈ 4.21.
  - Le vecteur normalisé (ltc) de `D` serait alors {"machine": 2.96/4.21 ≈ 0.70, "apprentissage": 2.99/4.21 ≈ 0.71}.

### 3.11 BM25 (Short Version)
- **Définition**: BM25 est un modèle de pondération utilisé dans les systèmes de récupération d'information basé sur le principe de la fréquence des termes, mais avec des améliorations pour éviter les problèmes de sur-pondération des termes fréquents.
- **Formule**: `BM25 = Σ ( (idf(t) * f(t, d) * (k1 + 1)) / (f(t, d) + k1 * (1 - b + b * |D| / avgdl)) )`, où `t` est un terme, `d` un document, `f(t, d)` la fréquence du terme `t` dans `d`, `|D|` la longueur du document, `avgdl` la longueur moyenne des documents dans la collection, `k1` et `b` des constantes.
- **Exemple**:
  - Supposons un document `D` contenant 100 mots avec le terme "machine" apparaissant 3 fois. La longueur moyenne des documents (`avgdl`) est de 150 mots. Utilisons `k1 = 1.5` et `b = 0.75`.
  - Disons que "machine" apparaît dans 100 documents sur 1000 (`N`), alors `idf(machine)` = log((1000 - 100 + 0.5) / (100 + 0.5)).
  - La partie BM25 pour "machine" serait alors : `(idf(machine) * 3 * (1.5 + 1)) / (3 + 1.5 * (1 - 0.75 + 0.75 * 100 / 150))`.
  - En calculant, cela donne un score BM25 pour "machine" dans `D`.


