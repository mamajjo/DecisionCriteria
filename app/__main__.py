import numpy as np
from app.configuration.config import configuration
INT_MAX = 999999
def calc_dist(GRAPH, source, destination, checked, parent):
    if source == destination:
        return 0
    checked[source] = True
    min_dist = INT_MAX
    for k in range(V):
        if checked[k] == False and GRAPH[source][k]:
            res = calc_dist(GRAPH, k, destination, checked, parent)
            if res != INT_MAX:
                if min_dist > GRAPH[source][k] + res:
                    min_dist = GRAPH[source][k] + res
                    parent[k] = source
    checked[source] = False
    return min_dist

def show_sol(parent, destination):
    if parent[destination] == -1:
        return
    show_sol(parent, int(parent[destination]))
    print(f"{int(parent[destination])} --> ", end='')

rawGraph = np.loadtxt(configuration.graphPath, dtype='i', delimiter=' ')
V = rawGraph.shape[0]
checked = np.zeros(V)
parent = np.zeros(V)
for i in range(V):
    checked[i] = False
    parent[i] = -1
print(f"Size of adjacency matrix is {V}")
try:
    if (len(rawGraph) < 0):
        raise AttributeError(f"At least one row of data is required")
    g = rawGraph
    print(f" Min Distance from 0 to {V-1} : {calc_dist(g, 0, V-1, checked, parent)}")
    print(f"Path: ", end='')
    show_sol(parent, V-1)
    print(V-1, end='')
except AttributeError as error:
    print('in configuration file: ' + repr(error))
except KeyError as keyError:
    print('in configuration file: ' + repr(keyError))