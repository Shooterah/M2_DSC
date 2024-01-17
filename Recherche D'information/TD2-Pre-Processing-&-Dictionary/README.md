
## Exercice 1 : Stemmer de Porter

### Questions et Réponses

1. **Pourquoi la règle ss → ss apparaît-elle alors qu'elle semble n'avoir aucun effet ?**
   - La règle "ss → ss" est présente pour éviter de tronquer incorrectement les mots se terminant par "ss". Sans cette règle, des mots comme "caress" pourraient être incorrectement réduits à "cares". Le Stemmer de Porter s'arrête dès qu'une première règle applicable est trouvée, donc cette règle sert à protéger les terminaisons en "ss" de toute modification.

2. **Application des règles sur les mots : circus, canaries, ponies, boss.**
   - Résultats après stemming :
     - circus → circu
     - canaries → canari
     - ponies → poni
     - boss → boss

3. **Quelle règle devrait être ajoutée pour stemmer "pony" également ?**
   - La règle appropriée serait "y → i". Cependant, c'est plus complexe. La vraie règle est :
     - Étape 1c : (*v*) Y → I
       - happy → happi
       - sky → sky

4. **Le résultat du stemmer pour "ponies" semble étrange car il ne correspond pas à un mot usuel du dictionnaire. Est-ce nocif pour la recherche ?**
   - Non, ce n'est pas nocif pour la recherche. Les mots "ponies" seront stemmés de la même manière dans les requêtes que dans les documents, ce qui permet à "ponies" et "pony" de correspondre. Le stemmer vise à réduire les mots à leur racine ou forme de base, pas nécessairement à un mot existant dans le dictionnaire.

### Conclusion
- Le Stemmer de Porter est conçu pour réduire efficacement les mots à leur racine, facilitant ainsi la correspondance entre différentes formes du même mot. Les règles spécifiques, comme "ss → ss" ou "(*v*) Y → I", jouent un rôle crucial dans le traitement précis des différentes terminaisons de mots.


## Exercice 2 : Online Porter’s stemmer

Faut stemmer en ligne donc on s'en fou :D

## Exercice 3 : Pré-Traitement et Index Inversé

### Contexte
Considération de trois courts documents pour le traitement de texte et la création d'un index inversé.

#### Documents Originaux
- **Doc 1**: Glimpse is an indexing and query system that allows for search through a file system or document collection quickly. Glimpse is the default search engine in a larger information retrieval system. It has also been used as part of some web based search engines.
- **Doc 2**: The main processes in an retrieval system are document indexing, query processing, query evaluation and relevance feedback. Among these, efficient updating of the index is critical in large scale systems.
- **Doc 3**: Clusters are created from short snippets of documents retrieved by web search engines which are as good as clusters created from the full text of web documents.

### Étapes de Pré-Traitement

1. **Tokenisation, Suppression des Stop Words et Normalisation**
   - **Doc1**: glimpse indexing query system allows search file system document collection quickly glimpse default search engine larger information retrieval system web based search engines
   - **Doc2**: main processes retrieval system document indexing query processing query evaluation relevance feedback efficient updating index critical scale systems
   - **Doc3**: clusters created short snippets documents retrieved web search engines clusters created text web documents

2. **Application du Stemming de Porter**
   - **Doc1**: glimps index queri system allow search file system document collect quickli glimps default search engin larger inform retriev system web base search engin
   - **Doc2**: main process retriev system document index queri process queri evalu relev feedback effici updat index critic scale system
   - **Doc3**: cluster creat short snippets document retriev web search engin cluster creat text web document

### Création de l'Index Inversé

#### Dictionnaire et Listes de Postings

| Terme      | Fréquence Totale | Fréquence Documentaire | Liste de Postings |
|------------|------------------|------------------------|-------------------|
| allow      | 1                | 1                      | 1                 |
| base       | 1                | 1                      | 1                 |
| cluster    | 2                | 1                      | 3                 |
| collect    | 1                | 1                      | 1                 |
| creat      | 2                | 1                      | 3                 |
| critic     | 1                | 1                      | 2                 |
| default    | 1                | 1                      | 1                 |
| document   | 4                | 3                      | 1→2→3             |
| effici     | 1                | 1                      | 2                 |
| engin      | 3                | 2                      | 1→3               |
| evalu      | 1                | 1                      | 2                 |
| feedback   | 1                | 1                      | 2                 |
| file       | 1                | 1                      | 1                 |
| glimps     | 2                | 1                      | 1                 |
| index      | 3                | 2                      | 1→2               |
| inform     | 1                | 1                      | 1                 |
| larger     | 1                | 1                      | 1                 |
| main       | 1                | 1                      | 2                 |
| process    | 2                | 1                      | 2                 |
| queri      | 3                | 2                      | 1→2               |
| quickli    | 1                | 1                      | 1                 |
| relev      | 1                | 1                      | 2                 |
| retriev    | 3                | 3                      | 1→2→3             |
| scale      | 1                | 1                      | 2                 |
| search     | 4                | 2                      | 1→3               |
| short      | 1                | 1                      | 3                 |
| snippets   | 1                | 1                      | 3                 |
| system     | 5                | 2                      | 1→2               |
| text       | 1                | 1                      | 3                 |
| updat      | 1                | 1                      | 2                 |
| web        | 3                | 2                      | 1→3               |


### 4) Requêtes de Recherche

#### Analyse des Résultats de Requêtes Booléennes
Utilisation de l'index inversé pour déterminer les résultats des requêtes suivantes :

1. **Requête : index AND query**
   - **Index**: 3 occurrences, présence dans doc1 et doc2 (1→2)
   - **Query**: 3 occurrences, présence dans doc1 et doc2 (1→2)
   - **Fusion**: doc1, doc2
   - **Résultat**: Les documents 1 et 2 sont retournés car ils contiennent tous les deux les termes "index" et "query".

2. **Requête : index OR query**
   - **Index**: 3 occurrences, présence dans doc1 et doc2 (1→2)
   - **Query**: 3 occurrences, présence dans doc1 et doc2 (1→2)
   - **Fusion**: doc1, doc2
   - **Résultat**: Les documents 1 et 2 sont retournés car ils contiennent au moins l'un des termes "index" ou "query".

3. **Requête : index AND (NOT query)**
   - **Index**: 3 occurrences, présence dans doc1 et doc2 (1→2)
   - **Query**: 3 occurrences, présence dans doc1 et doc2 (1→2)
   - **Fusion**: Aucun document
   - **Résultat**: Aucun document n'est retourné car aucun document ne contient "index" sans contenir "query".

4. **Requête : (search AND query) OR (search AND retrieve)**
   - **Search**: 4 occurrences, présence dans doc1 et doc3 (1→3)
   - **Query**: 3 occurrences, présence dans doc1 et doc2 (1→2)
   - **Retrieve**: 3 occurrences, présence dans doc1, doc2 et doc3 (1→2→3)
   - **1) Search and query**: doc1
   - **2) Search and retrieve**: doc1, doc3
   - **Total**: doc1, doc3
   - **Résultat**: Les documents 1 et 3 sont retournés car ils satisfont au moins l'une des conditions de la requête.

5. **Requête : (index OR cluster) AND (web OR system)**
   - **Index**: 3 occurrences, présence dans doc1 et doc2 (1→2)
   - **Cluster**: 2 occurrences, présence dans doc3 (3)
   - **Web**: 3 occurrences, présence dans doc1 et doc3 (1→3)
   - **System**: 5 occurrences, présence dans doc1 et doc2 (1→2)
   - **1) Index or cluster**: doc1, doc2, doc3
   - **2) Web or system**: doc1, doc2, doc3
   - **Total**: doc1, doc2, doc3
   - **Résultat**: Tous les trois documents sont retournés car ils satisfont les conditions de la requête.

### Conclusion
- L'utilisation de l'index inversé pour répondre à des requêtes booléennes démontre l'efficacité de cette structure pour filtrer rapidement et précisément les documents pertinents en fonction des termes de recherche spécifiés.
