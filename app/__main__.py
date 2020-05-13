import numpy as np
from app.configuration.config import configuration
from collections import defaultdict


class Graph:
    def __init__(self, values=[]):
        self.V = values

    def shortestDist(self):
        graph = self.V
        global INF

        # dist[i] is going to store shortest
        # distance from node i to node N-1.
        dist = [0] * N

        dist[N - 1] = 0

        # Calculating shortest path
        # for rest of the nodes
        for i in range(N - 2, -1, -1):

            # Initialize distance from
            # i to destination (N-1)
            dist[i] = INF

            # Check all nodes of next stages
            # to find shortest distance from
            # i to N-1.
            for j in range(N):

                # Reject if no edge exists
                if graph[i][j] == INF:
                    continue

                # We apply recursive equation to
                # distance to target through j.
                # and compare with minimum
                # distance so far.
                dist[i] = min(dist[i],
                              graph[i][j] + dist[j])

        return dist[0]


N = 9
INF = 99

# rawGraph = [[INF, 1, 2, 5, INF, INF, INF, INF],
#             [INF, INF, INF, INF, 4, 11, INF, INF],
#             [INF, INF, INF, INF, 9, 5, 16, INF],
#             [INF, INF, INF, INF, INF, INF, 2, INF],
#             [INF, INF, INF, INF, INF, INF, INF, 18],
#             [INF, INF, INF, INF, INF, INF, INF, 13],
#             [INF, INF, INF, INF, INF, INF, INF, 2]]

rawGraph = np.loadtxt(configuration.graphPath, dtype='i', delimiter=' ')
try:
    if (len(rawGraph) < 0):
        raise AttributeError(f"At least one row of data is required")
    g = Graph(rawGraph)
    # indexing from 0
    print(g.shortestDist())
except AttributeError as error:
    print('in configuration file: ' + repr(error))
except KeyError as keyError:
    print('in configuration file: ' + repr(keyError))
