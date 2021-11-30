class FordFulkerson:

    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)

    def breadth_first_search(self, node, start, parent):

        visited = [False] * (self.ROW)
        queue = []

        queue.append(node)
        visited[node] = True

        while queue:
            element = queue.pop(0)

            for index, value in enumerate(self.graph[element]):
                if visited[index] == False and value > 0:
                    queue.append(index)
                    visited[index] = True
                    parent[index] = element
                    if index == start:
                        return True

        return False

    def ford_fulkerson(self, source, sink):
        parent = [-1] * (self.ROW)

        max_flow = 0

        while self.breadth_first_search(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while (s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            v = sink
            while (v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


graph = [[0, 16, 13, 0, 0, 0],
         [0, 0, 10, 12, 0, 0],
         [0, 4, 0, 0, 14, 0],
         [0, 0, 9, 0, 0, 20],
         [0, 0, 0, 7, 0, 4],
         [0, 0, 0, 0, 0, 0]]

g = FordFulkerson(graph)

source = 0
sink = 5

print("Max flow is %d " % g.ford_fulkerson(source, sink))
