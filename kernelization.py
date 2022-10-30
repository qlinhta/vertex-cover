'''
Written by: Quyen Linh TA
Date: 30/10/2022
'''


class Kernelization:
    def __init__(self, graph):
        self.graph = graph

    def kernelization(self, k):

        '''
        Step 1: If node is an isolated vertex, remove node
        Step 2: If exist node with k+1 neighbors, remove node and decrease k by 1
        Step 3: If the graph has more than k^2 edges, return NO
        '''

        eliminated_nodes = []
        param = 0
        processed = True
        while processed:
            processed = True
            # Step 1: If node is an isolated vertex, remove node
            for node in range(self.graph.n()):
                if self.graph.degree(node) == 0:
                    eliminated_nodes.append(node)
                    self.graph.remove_vertex(node)
                    processed = True
                    break

            # Step 2: If exist node with k+1 neighbors, remove node and decrease k by 1
            for node in range(self.graph.n()):
                if self.graph.degree(node) == k + 1:
                    eliminated_nodes.append(node)
                    self.graph.remove_vertex(node)
                    param -= 1  # decrease k by 1
                    processed = True
                    break

            k -= param  # update k

        # Step 3: If the graph has more than k^2 edges, return NO
        if self.graph.m() > k ** 2:
            return None

        return self.graph

    def recursive(self, k):
        '''
        Step 1: Get the vertex v with highest degree
        Step 2: If degree(v) == 1, then graph has only isolated vertices => trivial solution
        Step 3: If degree(v) != 1, execute the recursive function
        '''

        # Step 1: Get the vertex v with highest degree
        # Compute degree of each vertex
        degree = [0] * self.graph.n()
        for node in range(self.graph.n()):
            degree[node] = self.graph.degree(node)

        # Get the vertex v with highest degree
        v = degree.index(max(degree))

        # Step 2: If degree(v) == 1, then graph has only isolated vertices => trivial solution
        if degree[v] == 1:
            return None

        # Step 3: If degree(v) != 1, execute the recursive function
        neighbors = self.graph.neighbors(v)
        subset_without_v = [node for node in range(self.graph.n()) if node != v]
        subset_without_v_neighbors = [node for node in subset_without_v if node not in neighbors]

        first_subset, second_subset = self.recursive(self.graph.subgraph(subset_without_v), k - 1), self.recursive(
            self.graph.subgraph(subset_without_v_neighbors), k - len(neighbors))

        if first_subset is not None and (second_subset is None or first_subset.n() <= second_subset.n()):
            first_subset.append(v)
            return first_subset

        if second_subset is not None and (first_subset is None or second_subset.n() < first_subset.n()):
            second_subset += neighbors
            return second_subset
        else:
            return None


