class Graph:
    def __init__(self, n, edges):  # n is number of vertices, edges is list of edges
        self._adj = [[] for _ in range(n)]  # adjacency list
        self._n = n  # number of vertices
        self._m = 0  # number of edges

        # adding edges
        for e in edges:
            try:
                u, v = e
                self.add_edge(u, v)
            except TypeError:
                pass

        # sorting the edges for faster access
        self.sort_edges()

    def n(self):  # return number of vertices
        return self._n

    def m(self):  # return number of edges
        return self._m

    # add edge between u and v vertex
    def add_edge(self, u, v):
        self._adj[u].append(v)
        self._adj[v].append(u)
        self._m += 1

    # remove edge between u and v vertex
    def remove_edge(self, u, v):
        try:
            self._adj[u].remove(v)
            self._adj[v].remove(u)
            self._m -= 1
        except ValueError:
            pass

    # sort the edges
    def sort_edges(self):
        for vertex in range(self._n):
            self._adj[vertex] = sorted(self._adj[vertex])

    # return the neighbors of u
    def neighbors(self, u):
        return self._adj[u]

    def degree(self, u):
        return len(self._adj[u])  # return the number of neighbors

    def adjacent(self, u, v):
        return 1 if v in self._adj[u] else 0  # return check if both vertices are adjacent

    def __str__(self):
        return str(self._adj)

    def __repr__(self):
        return str(self._adj)
