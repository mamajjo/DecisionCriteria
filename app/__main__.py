from pandas import read_csv, DataFrame
from app.configuration.config import json_config
import numpy as np
from numpy import all, any, delete, transpose
import matplotlib.pyplot as pl
from pymprog import *

from collections import defaultdict 
  
class Graph: 
    def minDistance(self,dist,queue): 
        minimum = float("Inf") 
        min_index = -1

        for i in range(len(dist)): 
            if dist[i] < minimum and i in queue: 
                minimum = dist[i] 
                min_index = i 
        return min_index 

    def printPath(self, parent, j): 
          
        if parent[j] == -1 :  
            print (j)
            return
        self.printPath(parent , parent[j]) 
        print (j)
    def printSolution(self, dist, parent): 
        src = 0
        print("Vertex \t\tDistance from Source\tPath") 
        for i in range(1, len(dist)): 
            print("\n%d --> %d \t\t%d \t\t\t\t\t" % (src, i, dist[i])), 
            self.printPath(parent,i) 

    def dijkstra(self, graph, src): 
  
        row = len(graph) 
        col = len(graph[0]) 
  
        dist = [float("Inf")] * row 
  
        parent = [-1] * row 
  
        dist[src] = 0
      
        queue = [] 
        for i in range(row): 
            queue.append(i) 

        while queue: 
            u = self.minDistance(dist,queue)  
  
            queue.remove(u) 
            for i in range(col): 
                if graph[u][i] and i in queue: 
                    if dist[u] + graph[u][i] < dist[i]: 
                        dist[i] = dist[u] + graph[u][i] 
                        parent[i] = u 
  
        self.printSolution(dist,parent) 
  
dataset = read_csv(json_config.dataSourceUrl, header=None)
try:
    if(len(dataset.index) < 0):
        raise AttributeError(f"At least one row of data is required")
    g= Graph() 
    
    graph = [   
            [0, 4, 0, 0, 0, 0, 0, 8, 0], 
            [4, 0, 8, 0, 0, 0, 0, 11, 0], 
            [0, 8, 0, 7, 0, 4, 0, 0, 2], 
            [0, 0, 7, 0, 9, 14, 0, 0, 0], 
            [0, 0, 0, 9, 0, 10, 0, 0, 0], 
            [0, 0, 4, 14, 10, 0, 2, 0, 0], 
            [0, 0, 0, 0, 0, 2, 0, 1, 6], 
            [8, 11, 0, 0, 0, 0, 1, 0, 7], 
            [0, 0, 2, 0, 0, 0, 6, 7, 0] 
        ] 

    g.dijkstra(graph,0) 
except AttributeError as error:
    print('in configuration file: ' + repr(error))
except KeyError as keyError:
    print('in configuration file: ' + repr(keyError))
