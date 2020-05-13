import numpy as np
from app.configuration.config import configuration
INT_MAX = 999999
def mindist(G, src, dst, visited, parent):
    #Base Conditions
    if src == dst:
        return 0
    visited[src] = True
    min_dist = INT_MAX
    for k in range(V):
        if visited[k] == False and G[src][k]:
            res = mindist(G, k, dst, visited, parent);
            if res != INT_MAX:
                if min_dist > G[src][k] + res:
                    min_dist = G[src][k] + res;
                    parent[k] = src;
    visited[src] = False
    return min_dist

def printpath(parent, dst):
    if parent[dst] == -1:
        return;
    printpath(parent, int(parent[dst]));
    print(f"{int(parent[dst])} --> ", end='')

rawGraph = np.loadtxt(configuration.graphPath, dtype='i', delimiter=' ')
V = rawGraph.shape[0]
visited = np.zeros(V)
parent = np.zeros(V)
for i in range(V):
    visited[i] = False
    parent[i] = -1
print(V)
try:
    if (len(rawGraph) < 0):
        raise AttributeError(f"At least one row of data is required")
    g = rawGraph
    print(f" Min Distance from 0 to {V-1} : {mindist(g, 0, V-1, visited, parent)}")
    print(f"Path: ", end='')
    printpath(parent, V-1)
    print(V-1, end='')
except AttributeError as error:
    print('in configuration file: ' + repr(error))
except KeyError as keyError:
    print('in configuration file: ' + repr(keyError))