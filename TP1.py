import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

def graphe():
    # Fix: use add_nodes_from instead of add_node for list of nodes
    G.add_nodes_from([1, 2, 3, 4, 5, 6])
    G.add_edges_from([(1,2),(1,4),(1,5),(2,3),(2,4),(2,5),(3,6),(3,5),(3,4),(6,4),(4,5),(6,2)])



def matrice_adjacente():
    matrice = [[0, 1, 0, 1, 1, 0],
               [1, 0, 1, 1, 1, 1],
               [0, 1, 0, 1, 1, 1],
               [1, 1, 1, 0, 1, 0],
               [1, 1, 1, 1, 0, 0],
               [0, 1, 1, 0, 0, 0]]
    return matrice




















def main():
    graphe()
    matrice = matrice_adjacente()
    # Add proper drawing configuration
    plt.figure(figsize=(8, 6))
    nx.draw(G, 
           node_color='lightblue',
           node_size=500,
           with_labels=True,
           font_size=16,
           font_weight='bold')
    plt.show()

if __name__ == "__main__":
    main()