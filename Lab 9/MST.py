# Implementation of Kruskal's and Prim's algorithms for
# finding the minimum spanning tree (MST) of a graph
# using an adjacency-list graph representation.

import heapq

# Vertex class to represent vertices in a graph
class Vertex:
    def __init__(self, key):
        self.key = key # Each vertex can be identified by a key
        self.d = float("inf")  # Distance from the source vertex
        self.parent = None # Parent vertex in the shortest path
        self.neighbors = {}  # Dictionary to store neighbors and their weights

    # Method to add a neighbor to the vertex
    def add_neighbor(self, key, weight=0):
        # Add the neighbor and its weight to the dictionary
        self.neighbors[key] = weight

    # Method that returns the neighbors of the vertex
    def get_neighbors(self):
        return self.neighbors.keys() 

    # Method that returns the weight of the edge between the vertex and a neighbor
    def get_weight(self, key):
        # The weight is stored in the dictionary
        return self.neighbors[key]
    
    # Method to compare vertices based on their keys
    def __repr__(self):
        return str(self.key)

# Graph class to represent a graph using an adjacency list
class Graph:
    def __init__(self):
        # Store the vertices of the graph in a dictionary
        self.vertices = {}

    # Method to add a vertex to the graph
    def add_vertex(self, key):
        # Check if the vertex is already in the graph
        if key not in self.vertices:
            # Create a new vertex and add it to the dictionary
            self.vertices[key] = Vertex(key)

    # Method to add an edge to the graph
    def add_edge(self, u, v, weight=0):
        # Check if the start and end vertices are not already in the graph
        if u not in self.vertices:
            # Add the start vertex to the graph
            self.add_vertex(u) 
        if v not in self.vertices:
            # Add the end vertex to the graph
            self.add_vertex(v)
        # Add the edge by connecting the start vertex to the end vertex with the given weight
        self.vertices[u].add_neighbor(v, weight)
        # Add the end vertex to the start vertex if the graph is undirected
        self.vertices[v].add_neighbor(u, weight) 

    # Method that returns the vertices of the graph
    def get_vertices(self):
        return self.vertices.keys()
    
# Disjoint set class to create a forest of single-vertex trees
class Disjoint_Set:
    def __init__(self):
        # Initialize dictionaires to store the 
        # parent and rank of each vertex
        self.parent = {}
        self.rank = {}

    # Method to create a set with a single vertex
    def make_set(self, vertex):
        # Set the parent of the vertex to itself
        self.parent[vertex] = vertex
        # Initialize the vertex's rank
        self.rank[vertex] = 0

    # Method to find the set that contains a vertex
    def find_set(self, vertex):
        # Check if the vertex is the parent of itself
        if self.parent[vertex] != vertex:
            # Recursively find the parent of the vertex
            self.parent[vertex] = self.find_set(self.parent[vertex])
        return self.parent[vertex]

    # Method to merge two sets
    def union(self, u, v):
        # Find the parents of the vertices
        u_parent = self.find_set(u)
        v_parent = self.find_set(v)
        # Check if the parents are the same
        if u_parent == v_parent:
            return # The vertices are already in the same set
        # Merge the sets based on the ranks of the parents
        if self.rank[u_parent] > self.rank[v_parent]:
            # Set the parent of the vertex with the lower rank to the parent with the higher rank
            self.parent[v_parent] = u_parent
        # Perform the same operation if the ranks are reversed
        elif self.rank[u_parent] < self.rank[v_parent]:
            self.parent[u_parent] = v_parent
        # Ranks of both parents are equal
        else:
            # Set the parent of one vertex to the other parent
            self.parent[u_parent] = v_parent
            # Increment the rank of the parent to maintain the upper bound of the tree's height
            self.rank[v_parent] += 1 

# Function to find the minimum spanning tree of a graph using Kruskal's algorithm
def MST_KRUSKAL(G):
    A = set()  # Minimum Spanning Tree
    disjoint_set = Disjoint_Set()

    # Create a forest with single-vertex trees 
    for v in G.get_vertices():
        disjoint_set.make_set(v)

    # Create a single list of the edges in the graph with their weights
    edges = []
    for u in G.get_vertices():
        for v in G.vertices[u].get_neighbors():
            edges.append((u, v, G.vertices[u].get_weight(v)))

    # Sort the list of edges by weight
    edges.sort(key=lambda x: x[2])

    # Iterate through sorted edges
    for u, v, weight in edges:
        # Check if adding the edge (u, v) creates a cycle
        if disjoint_set.find_set(u) != disjoint_set.find_set(v):
            # Add the edge to the MST
            A.add((u, v))
            # Union the sets of u and v
            disjoint_set.union(u, v)
    return A

# Function to find the minimum spanning tree of a graph using Prim's algorithm
def MST_PRIM(G, r):
    for u in G.get_vertices():  # Initialize vertices
        G.vertices[u].d = float("inf")
        G.vertices[u].parent = None
    r.d = 0
    Q = [(G.vertices[u].d, u) for u in G.get_vertices()]  # Priority queue
    heapq.heapify(Q)
    A = set()  # Minimum Spanning Tree
    visited = set()  # Set to track visited vertices

    while Q:
        _, u_key = heapq.heappop(Q)
        u = G.vertices[u_key]
        visited.add(u_key)
        for v_key in u.get_neighbors():
            v = G.vertices[v_key]
            weight = u.get_weight(v_key)
            if v_key not in visited and v.d > weight:
                v.parent = u
                v.d = weight
                # Update priority queue
                heapq.heappush(Q, (v.d, v.key))
        
        # Add edge (u.parent, u) to the MST
        if u.parent:
            A.add((u.parent.key, u.key))
    return A

# Test case
G = Graph()
G.add_edge("a", "b", 4)
G.add_edge("a", "h", 8)
G.add_edge("b", "c", 8)
G.add_edge("b", "h", 11)
G.add_edge("c", "d", 7)
G.add_edge("c", "f", 4)
G.add_edge("c", "i", 2)
G.add_edge("d", "e", 9)
G.add_edge("d", "f", 14)
G.add_edge("e", "f", 10)
G.add_edge("f", "g", 2)
G.add_edge("g", "h", 1)
G.add_edge("g", "i", 6)
G.add_edge("h", "i", 7)

print("Minimum Spanning Tree (Kruskal's algorithm):", MST_KRUSKAL(G))
# Print the weight of the minimum spanning tree
total_weight = sum(G.vertices[u].get_weight(v) for u, v in MST_KRUSKAL(G))
print("Total weight:", total_weight)

print("Minimum Spanning Tree (Prim's algorithm):", MST_PRIM(G, G.vertices["a"]))
# Print the weight of the minimum spanning tree
total_weight = sum(G.vertices[u].get_weight(v) for u, v in MST_PRIM(G, G.vertices["a"]))
print("Total weight:", total_weight)
