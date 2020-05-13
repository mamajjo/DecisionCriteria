import numpy as np
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

V = 8
G = [[ 0, 1, 2, 5, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 4, 11, 0, 0 ],
    [ 0, 0, 0, 0, 9, 5, 16, 0 ],
    [ 0, 0, 0, 0, 0, 0, 2, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 18 ],
    [ 0, 0, 0, 0, 0, 0, 0, 13 ],
    [ 0, 0, 0, 0, 0, 0, 0, 2 ],
    [0, 0, 0, 0, 0, 0, 0, 0 ]]
                  
visited = np.zeros(V)
parent = np.zeros(V)

    
for i in range(V):
    visited[i] = False
    parent[i] = -1
    
print(f" Min Distance from 0 to {V-1} : {mindist(G, 0, V-1, visited, parent)}")
print(f"Path: ", end='')
printpath(parent, 7)
print(V-1, end='')