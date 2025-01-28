# Python Graphe course :

## to get started install the following :

# Create virtual environment and activate it On macOS/Linux
python -m venv venv && source venv/bin/activate




'''
pip install networkx
pip install matplotlib
pip install scipy
'''

### Introduction :
L'objectif du TP vas etre de savoir faire des graphiques en python.

Création d’un graphe non orienté :

'''
import networkx as nx
G = nx.Graph()
'''

por ajouter un sommets (ou neux) :

'''
G.add_node(1)
G.add_node([2,3,4])
'''



Ajout d’arêtes (edge) :
'''
G.add_edge(1, 2)
G.add_edges_from([(1, 3), (1, 4), (2, 3)])
G.add_edge(1, 5) # Même si le noeud n’existe pas encore
'''