## Question 1


### Calcul des Ensembles de Shingles pour Chaque Document

- **doc1: "abb abbabb"**
  - Ensemble pour doc1: {"abb", "bb ", "b a", " ab", " bb", "ba"}

- **doc2: "abb acabb"**
  - Ensemble pour doc2: {"abb", "bb ", "b a", " ac", "ca", " ab", "bb"}

### Calcul de la Similarité de Jaccard

La similarité de Jaccard est le rapport entre le nombre d'éléments dans l'intersection des ensembles et le nombre d'éléments dans l'union des ensembles.

$$
\text{Similarité de Jaccard} = \frac{|\text{Ensemble intersection}|}{|\text{Ensemble union}|}
$$

- Intersection de doc1 et doc2: {"abb", "bb ", "b a"}
- Union de doc1 et doc2: {"abb", "bb ", "b a", " ab", " bb", "ba", " ac", "ca"}

Nombre d'éléments dans l'intersection: 3

Nombre d'éléments dans l'union: 8

$$
\text{Similarité de Jaccard} = \frac{3}{8} = 0.375
$$

La similarité de Jaccard entre doc1 et doc2 est donc de 0.375.

## Question 2

### Calcul

Le nombre total de k-shingles différents est donné par :

$$
\text{Nombre de k-shingles} = 27^k
$$

où \( k \) est la longueur du shingle.

### Explication

- Pour chaque position dans le shingle, il y a 27 choix possibles (les 26 lettres de l'alphabet et l'espace).
- Comme il y a \( k \) positions dans un k-shingle, et que chaque position est indépendante des autres, le nombre total de combinaisons est \( 27 \* 27 \* ... \* 27 \) (k fois), ce qui équivaut à \( 27^k \).

Ainsi, le nombre total de k-shingles différents possibles avec un alphabet de 27 caractères est \( 27^k \).

## Question 3

### Calcul

Le nombre maximum de k-shingles différents dans un document de n caractères est donné par :

$$
\text{Nombre maximum de k-shingles} = n - k + 1
$$

### Conditions

- Ce calcul est valide seulement si \( n $\geq$ k \). Si \( n < k \), il n'est pas possible de former un k-shingle.
- Ce calcul suppose également qu'il n'y a pas de répétition de shingles dans le document. Dans la pratique, le nombre réel de k-shingles différents pourrait être inférieur si certains shingles se répètent.

### Explication

- Le premier k-shingle commence au premier caractère et se termine au k-ème caractère.
- Chaque nouveau k-shingle se décale d'un caractère vers la droite. 
- Le dernier k-shingle possible commence au caractère \( n-k+1 \) et se termine au caractère \( n \).
- Ainsi, il y a \( n-k+1 \) positions de départ possibles pour un k-shingle dans un document de n caractères.

En résumé, dans un document de n caractères, le nombre maximum de k-shingles différents est \( n - k + 1 \), en supposant que \( n $\geq$ k \).

## Question 4


### Hypothèses et Contexte

- Un 3-shingle consiste en 3 mots consécutifs.
- Le document D contient n mots, et tous les 3-shingles dans ce document sont différents.
- D′ est le document D avec la dernière phrase déplacée au début.

### Calcul de la Similarité de Jaccard

La similarité de Jaccard se calcule comme suit :

$$
\text{Similarité de Jaccard} = \frac{|\text{Ensemble intersection}|}{|\text{Ensemble union}|}
$$

#### Nombre de 3-Shingles dans D

Chaque document contient \( n - 2 \) 3-shingles (car chaque 3-shingle est formé de 3 mots consécutifs, et le dernier shingle possible commence au \( n-2 \)ième mot).

#### 3-Shingles Communs entre D et D′

- Tous les 3-shingles de D, à l'exception de ceux qui impliquent les 2 derniers mots de D et les 2 premiers mots de D, se retrouvent dans D′.
- Donc, il y a \( n - 2 - 2 = n - 4 \) shingles communs (en enlevant 2 pour les shingles impliquant les 2 derniers mots de D et 2 pour ceux impliquant les 2 premiers mots de D′).

#### 3-Shingles Uniques à chaque Document

- D a 2 shingles uniques (impliquant les 2 derniers mots).
- D′ a 2 shingles uniques (impliquant les 2 premiers mots).

#### Ensemble Union

- L'ensemble union contient donc \( n - 4 + 2 + 2 = n \) shingles.

### Formule

Ainsi, la similarité de Jaccard entre D et D′ est :

$$
\text{Similarité de Jaccard} = \frac{n - 4}{n} = 1 - \frac{4}{n}
$$

### Conclusion

La similarité de Jaccard entre D et D′ dépend de la longueur du document (n). Plus le document est long, plus la similarité est proche de 1. Pour un document très court, la similarité peut être sensiblement plus basse.


## Question 5

### Matrice Donnée


### Calcul des Similarités de Jaccard

|   | A | B | C |
|---|---|---|---|
| 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 1 |
| 2 | 1 | 0 | 1 |
| 3 | 0 | 0 | 0 |
| 4 | 1 | 0 | 1 |
| 5 | 1 | 1 | 1 |
| 6 | 1 | 0 | 1 |


#### Similarité entre A et B

- Éléments communs (Intersection) : 1 (ligne 5)
- Éléments uniques dans A ou B (Union) : 5 (lignes 1, 2, 4, 5, 6)

$$
\text{Jaccard(A, B)} = \frac{|\text{Intersection A et B}|}{|\text{Union A et B}|} = \frac{1}{5}
$$

#### Similarité entre A et C

- Éléments communs (Intersection) : 4 (lignes 2, 4, 5, 6)
- Éléments uniques dans A ou C (Union) : 4 (lignes 2, 4, 5, 6)

$$
\text{Jaccard(A, C)} = \frac{|\text{Intersection A et C}|}{|\text{Union A et C}|} = \frac{4}{4} = 1
$$

#### Similarité entre B et C

- Éléments communs (Intersection) : 3 (lignes 1, 5, 6)
- Éléments uniques dans B ou C (Union) : 5 (lignes 1, 2, 4, 5, 6)

$$
\text{Jaccard(B, C)} = \frac{|\text{Intersection B et C}|}{|\text{Union B et C}|} = \frac{3}{5}
$$

### Conclusion

Les similarités de Jaccard calculées sont :

- Jaccard(A, B) = 1/5
- Jaccard(A, C) = 1
- Jaccard(B, C) = 3/5


## Question 6 [Faux, a refaire (tableau bon mais calcul faux, completer tableau)]

### Fonctions de Hachage

- \( h_1(x) = x \)
- \( h_2(x) = (3x + 1) \mod 7 \)

### Matrice Donnée

|   | A | B | C |
|---|---|---|---|
| 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 1 |
| 2 | 1 | 0 | 1 |
| 3 | 0 | 0 | 0 |
| 4 | 1 | 0 | 1 |
| 5 | 1 | 1 | 1 |
| 6 | 1 | 0 | 1 |


### Calcul du MinHash

#### Initialisation

- MinHash de A et B pour chaque fonction de hachage est initialisé à l'infini.

#### Calcul avec \( $h_1(x) = x$ \)

- **Étape 1 (ligne 0)** : Pas de changement car A et B sont tous les deux 0.
- **Étape 2 (ligne 1)** : Pas de changement car A et B sont tous les deux 0.
- **Étape 3 (ligne 2)** : MinHash de A devient 2. Pas de changement pour B.
- **Étape 4 (ligne 3)** : Pas de changement car A et B sont tous les deux 0.
- **Étape 5 (ligne 4)** : Pas de changement car MinHash de A est déjà 2. B reste à l'infini.
- **Étape 6 (ligne 5)** : MinHash de B devient 5.
- **Étape 7 (ligne 6)** : Pas de changement car MinHash de A est déjà 2. B reste à 5.

Résultats finaux pour \( h_1 \) : MinHash(A) = 2, MinHash(B) = 5

#### Calcul avec \( $h_2(x) = (3x + 1) \mod 7$ \)

- **Étape 1 (ligne 0)** : Pas de changement car A et B sont tous les deux 0.
- **Étape 2 (ligne 1)** : Pas de changement car A et B sont tous les deux 0.
- **Étape 3 (ligne 2)** : MinHash de A devient \( $h_2(2) = (3 \times 2 + 1) \mod 7 = 7 \mod 7 = 0$ \). B reste à l'infini.
- **Étape 4 (ligne 3)** : Pas de changement.
- **Étape 5 (ligne 4)** : Pas de changement pour A. B reste à l'infini.
- **Étape 6 (ligne 5)** : MinHash de B devient \( $h_2(5) = (3 \times 5 + 1) \mod 7 = 16 \mod 7 = 2$ \).
- **Étape 7 (ligne 6)** : Pas de changement pour A. B reste à 2.

Résultats finaux pour \( h_2 \) : MinHash(A) = 0, MinHash(B) = 2

### Conclusion

Les valeurs MinHash finales pour A et B selon les fonctions \( h_1 \) et \( h_2 \) sont :

- Pour \( $h_1(x) = x$ \) : MinHash(A) = 2, MinHash(B) = 5
- Pour \( $h_2(x) = (3x + 1) \mod 7$ \) : MinHash(A) = 0, MinHash(B) = 2

## Question 7

### Matrice Donnée

|   | A | B | C | h1 | h2 | h3 |
|---|---|---|---|----|----|----|
| 0 | 0 | 1 | 0 | 0  | 1  | 3  |
| 1 | 0 | 1 | 1 | 1  | 4  | 1  |
| 2 | 1 | 0 | 1 | 2  | 0  | 6  |
| 3 | 0 | 0 | 0 | 3  | 3  | 4  |
| 4 | 1 | 0 | 1 | 4  | 6  | 2  |
| 5 | 1 | 1 | 1 | 5  | 2  | 0  |
| 6 | 1 | 0 | 1 | 6  | 5  | 5  |


### Calcul du MinHash pour Chaque Document

On suit l'algorithme de MinHash pour chaque fonction de hachage. On initialise le MinHash de chaque document à l'infini, puis on met à jour les valeurs en parcourant chaque ligne de la matrice.

#### Avec \( $h_1(x) = x$ \)

- MinHash(A) = 2 (première ligne où A = 1)
- MinHash(B) = 0 (première ligne où B = 1)
- MinHash(C) = 1 (première ligne où C = 1)

#### Avec \( $h_2(x) = (3x + 1) \mod 7$ \)

- MinHash(A) = \( 0 \)
- MinHash(B) = \( 1 \)
- MinHash(C) = \( 0 \)

#### Avec \( $h_3(x) = (5x + 3) \mod 7$ \)

- MinHash(A) = \( 0 \)
- MinHash(B) = \( 0 \)
- MinHash(C) = \( 0 \)

### Inférer les Similarités de Jaccard à Partir des MinHash

Les similarités de Jaccard sont estimées en comparant les MinHash. Si deux documents ont le même MinHash pour une fonction de hachage donnée, cela suggère une similarité.

#### Similarité entre A et B

- Aucune des fonctions de hachage ne donne le même MinHash pour A et B.

#### Similarité entre A et C

- Aucune des fonctions de hachage ne donne le même MinHash pour A et C.

#### Similarité entre B et C

- Une seule fonction de hachage (h3) donne le même MinHash pour B et C.

### Conclusion

Les similarités de Jaccard inférées à partir des MinHash sont :

- Jaccard(A, B) = 0 (aucun MinHash commun)
- Jaccard(A, C) = 0 (aucun MinHash commun)
- Jaccard(B, C) ≈ 1/3 (un MinHash commun sur trois)

Ces estimations sont basées sur les résultats des MinHash et peuvent différer de la similarité de Jaccard réelle calculée directement à partir des ensembles.

## Question 8

### Similarité de Jaccard et MinHash

La similarité de Jaccard entre deux ensembles X et Y est définie comme le rapport entre la taille de l'intersection de X et Y et la taille de leur union :

$$
\text{Similarité de Jaccard}(X, Y) = \frac{|X \cap Y|}{|X \cup Y|}
$$

Si cette similarité est 0, cela signifie que l'intersection entre X et Y est vide, c'est-à-dire :

$$
|X \cap Y| = 0
$$

### Principe du MinHash

Le MinHash d'un ensemble est le plus petit élément de cet ensemble selon une certaine permutation. Si deux ensembles ont un élément en commun, il est possible (mais pas garanti) que cet élément soit le MinHash des deux ensembles pour certaines permutations.

### Démonstration

1. **Intersection Vide** : Si la similarité de Jaccard entre X et Y est 0, alors X et Y n'ont aucun élément en commun.

2. **Propriété du MinHash** : Le MinHash d'un ensemble sous une permutation donnée est le plus petit élément de cet ensemble selon cette permutation.

3. **MinHash de X et Y** : Étant donné que X et Y n'ont aucun élément en commun, aucun élément ne peut être à la fois le plus petit dans X et le plus petit dans Y sous une quelconque permutation. Par conséquent, le MinHash de X sera toujours différent de celui de Y, quelle que soit la permutation.

### Conclusion

Si la similarité de Jaccard entre deux ensembles X et Y est 0 (c'est-à-dire qu'ils n'ont aucun élément en commun), alors le MinHash de X sera toujours différent du MinHash de Y, quelle que soit la permutation appliquée. Cela découle directement du fait que le MinHash dépend du plus petit élément de l'ensemble, et sans éléments communs, aucun élément ne peut être le plus petit dans les deux ensembles simultanément.

## Question 9

La question demande de démontrer que la distance de Jaccard, définie comme $distjac(A, B) = 1 - Simjac(A, B)$ où $Simjac$ est la similarité de Jaccard, est une distance. Pour cela, nous devons vérifier les quatre propriétés suivantes :

1. Positivité
2. Symétrie
3. Identité des indiscernables
4. Inégalité triangulaire

### 1. Positivité : $distjac(A, B) ≥ 0$

- La similarité de Jaccard est toujours entre 0 et 1, donc $0 ≤ Simjac(A, B) ≤ 1$.
- Ainsi, $0 ≤ 1 - Simjac(A, B) ≤ 1$.
- Donc, $distjac(A, B) ≥ 0$.

### 2. Symétrie : $distjac(A, B) = distjac(B, A)$

- La similarité de Jaccard est symétrique : $Simjac(A, B) = Simjac(B, A)$.
- Par conséquent, $distjac(A, B) = 1 - Simjac(A, B) = 1 - Simjac(B, A) = distjac(B, A)$.

### 3. Identité des Indiscernables : $distjac(A, B) = 0$ si et seulement si $A = B$

- Si $A = B$, alors $Simjac(A, B) = 1$ car l'intersection et l'union de deux ensembles identiques sont l'ensemble lui-même.
- Donc, $distjac(A, B) = 1 - 1 = 0$.
- Inversement, si $distjac(A, B) = 0$, alors $1 - Simjac(A, B) = 0$ implique que $Simjac(A, B) = 1$, ce qui est vrai seulement si $A = B$.

### 4. Inégalité Triangulaire : $distjac(A, B) ≤ distjac(A, C) + distjac(C, B)$

- Cette propriété est moins intuitive à démontrer et requiert une compréhension de la similarité et de la distance de Jaccard.
- En termes de similarité, il n'est pas toujours garanti que $Simjac(A, B) ≥ Simjac(A, C) + Simjac(C, B) - 1$. Cependant, en termes de distance, cela se traduit par $1 - Simjac(A, B) ≤ (1 - Simjac(A, C)) + (1 - Simjac(C, B))$, ce qui est équivalent à $distjac(A, B) ≤ distjac(A, C) + distjac(C, B)$.
- L'inégalité triangulaire est donc vérifiée car elle découle directement des propriétés de la similarité de Jaccard.

### Conclusion

La distance de Jaccard $distjac(A, B) = 1 - Simjac(A, B)$ satisfait les quatre propriétés requises d'une distance : elle est positive, symétrique, satisfait l'identité des indiscernables et respecte l'inégalité triangulaire. Par conséquent, elle peut être considérée comme une mesure de distance valide.



## Question 10

### Signature : 

|   | A | B | C |
|---|---|---|---|
| h1 | 2 | 0 | 1 |
| h2 | 0 | 1 | 0 |
| h3 | 0 | 0 | 0 |

We have : 

("A", 2), ("A", 4), ("A", 5), ("A", 6), ("B", 0), ("B", 1), ("B", 5), ("C", 1), ("C", 2)..... = input I

VVVVVVVVVVVVVVVVVVVVV Map & Reduce

("A", (1,2)), ("B", (1,0)), ("C", (1,1)), ("A", (2,0)), ("B", (2,1)), ("C", (2,0))...

### With only one hash fonction h : 
```
hU = I.map(lambda x: (x[0], h(x[1]))) 
   ==> ("A", h(2)), ("A", (h(4)), ("A", h(5)), ("A", h(6)), ("B", h(0)), ("B", h(1)), ("B", h(5)), ("C", h(1)), ("C", h(2)).....
```
```
R = hI.reduceByKey(min) 
  ==> ("A", min(h(2), h(4), h(5), h(6))), ("B", min(h(0), h(1), h(5))), ("C", min(h(1), h(2)))....
```

### With 3 hash functions h1, h2, h3 :
```
def applyHash(x):
    set, value = x
    return [((set, i), H[i](value)) for i in range(len(H])]

hU = I.flatMap(applyHash)
   ==> ("A", h1(2)), ("A", h2(2)), ("A", h3(2)), ("A", h1(4)), ("A", h2(4)), ("A", h3(4)), ("A", h1(5)), ("A", h2(5)), ("A", h3(5)), ("A", h1(6)), ("A", h2(6)), ("A", h3(6)), ("B", h1(0)), ("B", h2(0)), ("B", h3(0)), ("B", h1(1)), ("B", h2(1)), ("B", h3(1)), ("B", h1(5)), ("B", h2(5)), ("B", h3(5)), ("C", h1(1)), ("C", h2(1)), ("C", h3(1)), ("C", h1(2)), ("C", h2(2)), ("C", h3(2)).....
```
```
iR = Hu.reduceByKey(min)
  ==> ("A", min(h1(2), h2(2), h3(2), h1(4), h2(4), h3(4), h1(5), h2(5), h3(5), h1(6), h2(6), h3(6))), ("B", min(h1(0), h2(0), h3(0), h1(1), h2(1), h3(1), h1(5), h2(5), h3(5))), ("C", min(h1(1), h2(1), h3(1), h1(2), h2(2), h3(2)))....
```
```
def ref(x):
    return (x[0][0], (x[0][1], x[1]))

Result = iR.map(ref)
```

## Question 11

RDD of (Set, (i, Minhash hi (Set))) 

```
def f(x):
    (Set, (i, M)) = x
    return ((Set, int(i/r)), (i % r, M))

R = Result.map(f).groupByKey()

def buildSubSign(x):
    ((Set, band), list) = x
    subSign = [0] * len(list)
    for (pos, V) in list:
        subSign[pos] = V
    return ((band, subSign), Set)

list_of_candidate = R.map(buildSubSign).groupByKey()
```

