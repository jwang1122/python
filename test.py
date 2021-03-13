import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from statistics import mean 
from itertools import combinations
from collections import defaultdict
from pprint import pprint

def Average(lst): 
    return mean(lst) 

data = pd.read_csv('Airlines_graph.csv')
x = data.shape
y = data.dtypes
data['std'] = data.sched_dep_time.astype(str).str.replace('(\d{2}$)', '') + ':' + data.sched_dep_time.astype(str).str.extract('(\d{2}$)', expand=False) + ':00'
data['sta'] = data.sched_arr_time.astype(str).str.replace('(\d{2}$)', '') + ':' + data.sched_arr_time.astype(str).str.extract('(\d{2}$)', expand=False) + ':00'
data['atd'] = data.dep_time.fillna(0).astype(np.int64).astype(str).str.replace('(\d{2}$)', '') + ':' + data.dep_time.fillna(0).astype(np.int64).astype(str).str.extract('(\d{2}$)', expand=False) + ':00'
data['ata'] = data.arr_time.fillna(0).astype(np.int64).astype(str).str.replace('(\d{2}$)', '') + ':' + data.arr_time.fillna(0).astype(np.int64).astype(str).str.extract('(\d{2}$)', expand=False) + ':00'
#data['date'] = pd.to_datetime(data[['year', 'month', 'day']])
print(data.dtypes)
print(data.shape)
FG = nx.from_pandas_edgelist(data, source='origin', target='dest', edge_attr=True,)
FG.nodes()
FG.edges()
nx.draw_networkx(FG, with_labels = True)
nx.algorithms.degree_centrality(FG)
lst = list(nx.degree_centrality(FG).values())
average = Average(lst) 
print(average)
x = nx.average_shortest_path_length(FG)
print(f"average shortest path length: {x}")
x = nx.average_degree_connectivity(FG)
print(f"average degree connectivity: {x}")
# for path in nx.all_simple_paths(FG, source='JAX', target='DFW'):
#     print(path)
print("dijkstral path: ")
dijpath = nx.dijkstra_path(FG, source='JAX', target='DFW')
print(dijpath)
print("shortest path: ")
shortpath = nx.dijkstra_path(FG, source='JAX', target='DFW', weight='air_time')
print(shortpath)
simplePaths = [path for path in nx.shortest_simple_paths(FG, source='JAX', target='DFW', weight='air_time')]
l1 = sorted(simplePaths, key=len)
pprint(l1[:6])

# cliques = nx.find_cliques(FG)
# print(list(cliques))

# recommended = defaultdict(int)
# for n, d in FG.nodes(data=True):
#     for n1, n2 in combinations(FG.neighbors(n), 2):
#         if not FG.has_edge(n1, n2):
#             recommended[(n1, n2)] += 1
# all_counts = sorted(recommended.values())
# top10_pairs = [pair for pair, count in recommended.items() if count > all_counts[-10]]
# print("recommended pair: ")
# print(top10_pairs)