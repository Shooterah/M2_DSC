import networkx as nx
import random
import matplotlib.pyplot as plt
import time
from collections import Counter

###########################################################
#### 3 Creating a graph
###########################################################

G = nx.Graph()

def random_graph(n,p):
    for i in range(n):
        for j in range(i+1,n):
            if random.random() < p:
                G.add_edge(i,j)
    return G

G = random_graph(50,0.1)

largest_cc = max(nx.connected_components(G), key=len)

print(largest_cc)

# Si np = 1  alors les noeuds sont tous connecté entre eux

def plot_largest_cc(n,p):
    largest_cc = []
    for i in range(1,n):
        G = random_graph(i,p)
        largest_cc.append(len(max(nx.connected_components(G), key=len)))
    plt.plot(largest_cc)
    plt.show()

plot_largest_cc(100,0.1)

def multiple_random_graph(n, p):
    start_time = time.time()
    for i in range(1, n):
        G = random_graph(i, p)
    end_time = time.time()
    print(f"Execution time of plot_largest_cc: {end_time - start_time} seconds")

def multiple_erdos_renyi(n, p):
    start_time = time.time()
    for i in range(1, n):
        G = nx.erdos_renyi_graph(i, p)
    end_time = time.time()
    print(f"Execution time of erdos_renyi: {end_time - start_time} seconds")

multiple_random_graph(100, 0.5)
multiple_erdos_renyi(100, 0.5)

###########################################################
#### 4 Loading a graph
###########################################################

G = nx.read_edgelist("./graph0.txt")

G.add_node("10")
G.add_edge("5", "10")

nx.draw(G, with_labels=True)
plt.show()

###########################################################
#### 5 Drawing a graph
###########################################################

G = nx.karate_club_graph()

nx.draw(G, with_labels=True)
plt.show()

###########################################################
#### 6 Degree distribution
###########################################################

def plot_degree_distribution(G, title):
    degrees = [G.degree(n) for n in G.nodes()]
    degree_counts = Counter(degrees)
    x, y = zip(*degree_counts.items())
    
    plt.scatter(x, y, color='b')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Degree')
    plt.ylabel('Frequency')
    plt.title(title)
    plt.show()

# Karate Club graph
G = nx.karate_club_graph()
plot_degree_distribution(G, 'Karate Club Graph')

# Random graph
G = random_graph(100, 0.5)
plot_degree_distribution(G, 'Random Graph')

# Watts-Strogatz graph
G = nx.watts_strogatz_graph(100, 6, 0.2)
plot_degree_distribution(G, 'Watts-Strogatz Graph')

# Barabasi-Albert graph
G = nx.barabasi_albert_graph(100, 5)
plot_degree_distribution(G, 'Barabasi-Albert Graph')

# LFR benchmark graph
G = nx.LFR_benchmark_graph(250, 3, 1.5, 0.1, average_degree=5, min_community=20, seed=10)
plot_degree_distribution(G, 'LFR Benchmark Graph')

###########################################################
#### 7 Degree distribution
###########################################################