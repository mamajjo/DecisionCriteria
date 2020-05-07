import numpy as np
from app.configuration.config import configuration
from collections import defaultdict 

class Graph: 
    def __init__(self, values=[]):
        self.V = values

    def minDistance(self,dist,queue): 
        minim = float("Inf") 
        min_index = -1
        for i in range(len(dist)): 
            if dist[i] < minim and i in queue: 
                minim = dist[i] 
                min_index = i 
        return min_index 
    def find_shortest_paths(self, start): 
        row = len(self.V) 
        col = len(self.V[0]) 
        dist = [float("Inf")] * row 
        parent = [-1] * row 
        dist[start] = 0

        queue = [] 
        for i in range(row): 
            queue.append(i) 

        while queue: 
            u = self.minDistance(dist,queue)  
            queue.remove(u) 
            for i in range(col): 
                if self.V[u][i] and i in queue: 
                    if dist[u] + self.V[u][i] < dist[i]: 
                        dist[i] = dist[u] + self.V[u][i] 
                        parent[i] = u 

        self.print_paths(dist, parent, start)
    def print_path(self, parent, j): 
        if parent[j] == -1:  
            print (f"{j}", end='')
            return
        self.print_path(parent , parent[j]) 
        print (f" -> {j}", end='')
    def print_paths(self, dist, parent, start): 
        print("Vertice_num \t\tmin_distance \t path", end='') 
        for i in range(1, len(dist)): 
            print("\n%d --> %d \t\t%d \t\t" % (start, i, dist[i]), end='')
            self.print_path(parent,i) 

rawGraph = np.loadtxt(configuration.graphPath, dtype='i', delimiter=' ')
try:
    if(len(rawGraph) < 0):
        raise AttributeError(f"At least one row of data is required")
    g= Graph(rawGraph) 
    # indexing from 0
    g.find_shortest_paths(0) 
except AttributeError as error:
    print('in configuration file: ' + repr(error))
except KeyError as keyError:
    print('in configuration file: ' + repr(keyError))
