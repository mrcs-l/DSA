# Implementation of Bellman-Ford and Dijkstra's algorithms for
# single-source shortest path problems on directed weighted graphs.

import heapq

# Vertex class to represent vertices in a graph
class Vertex:
    def __init__(self, key):
        self.key = key # Each vertex can be identified by a key
        self.d = float("inf") # Distance from the source vertex
        self.parent = None # Parent vertex in the shortest path
        self.neighbors = {} # Dictionary to store neighbors and their weights

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

    # Method that returns the vertices of the graph
    def get_vertices(self):
        return self.vertices.keys()
    
    # Method that returns a vertex with a given key
    def get_vertex(self, key):
        return self.vertices[key]
    
    # Method to compare graphs based on their vertices
    def __repr__(self):
        return str(self.vertices)

# Function to initialize attributes of vertices
def initializeSingleSource(G, s):
    # Iterate over each vertex in the graph
    for v in G.vertices.values():
        # Set the distance to originally be infinity
        v.d = float("inf")
        # Set the parent to be None
        v.parent = None
    # The source vertex has a distance of 0
    s.d = 0

# Function to print the shortest path from the source to a vertex
def printPath(G, s, v):
    # Check if the source and vertex are the same
    if v == s:
        # The path is the source vertex
        print(s)
    # Check if the vertex has no parent
    elif v.parent == None:
        # There is no path from the source to the vertex
        print("No path from", s, "to", v.key, "exists")
    else: # Otherwise, recursively print the path from the source to the parent of the vertex
        printPath(G, s, v.parent)
        print(v.key)

# Function to relax an edge between two vertices
def relax(u, v, w):
    # Check if the distance of the end vertex is greater than 
    # the sum of the distances of the start vertex and the weight
    if v.d > u.d + w:
        # Update the distance of the end vertex
        v.d = u.d + w
        # Update the parent of the end vertex
        v.parent = u

# Function for solving the SSSP problem using the Bellman-Ford algorithm
def bellmanFord(G, s):
    # Initialize the attributes of the vertices
    initializeSingleSource(G, s)
    # Iterate over the number of vertices - 1 times
    for i in range(len(G.vertices) - 1):
        # Iterate over each vertex in the graph
        for u in G.vertices.values():
            # Iterate over the neighbors of the vertex
            for v_key in u.get_neighbors():
                # Get the neighbor vertex
                v = G.vertices[v_key]
                # Relax the edge between the vertex and its neighbor
                relax(u, v, u.get_weight(v_key))
    # Iterate over each vertex in the graph
    for u in G.vertices.values():
        # Iterate over the neighbors of the vertex
        for v_key in u.get_neighbors():
            # Get the neighbor vertex
            v = G.vertices[v_key]
            # Check if the vertex should be relaxed
            if v.d > u.d + u.get_weight(v_key):
                # If relexation can still improve any shortest-path weight, 
                # then the graph contains a negative-weight cycle
                return False
    # The graph does not contain a negative-weight cycle
    return True

# Function for solving the SSSP problem using Dijkstra's algorithm
def dijkstra(G, s):
    # Initialize the attributes of the vertices
    initializeSingleSource(G, s)
    S = set() # Set to store visited vertices
    Q = [(v.d, v.key) for v in G.vertices.values()]  # Push tuples of (distance, vertex key)
    # Convert the list into a heap maintaining the smallest distance at the top
    heapq.heapify(Q) 
    while Q: 
        _, u_key = heapq.heappop(Q)  # Pop the vertex key with the smallest distance
        u = G.vertices[u_key]  # Get the corresponding vertex object
        S.add(u) # Add the vertex to the set of visited vertices
        # Iterate over the neighbors of the vertex
        for v_key in u.get_neighbors():
            # Get the neighbor vertex
            v = G.vertices[v_key]
            # Relax the edge between the vertex and its neighbor
            relax(u, v, u.get_weight(v_key))
        # Update the queue with non-visited vertices
        Q = [(v.d, v.key) for v_key, v in G.vertices.items() if v not in S]
        # Convert the list into a heap maintaining the smallest distance at the top
        heapq.heapify(Q)

# Graph for Bellman-Ford algorithm
G1 = Graph() 
G1.add_edge("s", "t", 6)
G1.add_edge("s", "y", 7)
G1.add_edge("t", "x", 5)
G1.add_edge("t", "y", 8)
G1.add_edge("t", "z", -4)
G1.add_edge("x", "t", -2)
G1.add_edge("y", "x", -3)
G1.add_edge("y", "z", 9)
G1.add_edge("z", "s", 2)
G1.add_edge("z", "x", 7)

# Graph for Dijkstra algorithm
G2 = Graph()
G2.add_edge("s", "t", 10)
G2.add_edge("s", "y", 5)
G2.add_edge("t", "x", 1)
G2.add_edge("t", "y", 2)
G2.add_edge("x", "z", 4)
G2.add_edge("y", "t", 3)
G2.add_edge("y", "x", 9)
G2.add_edge("y", "z", 2)
G2.add_edge("z", "s", 7)
G2.add_edge("z", "x", 6)

# Initialize source vertices
s1 = G1.get_vertex("s")
s2 = G2.get_vertex("s")

# Output for Bellman-Ford algorithm
print("Bellman-Ford Algorithm:\n")
bellmanFord(G1, s1)
# Iterate through each vertex in the graph
for v in G1.vertices.values():
    # Display the weight of the shortest path from the source to the vertex
    print("Shortest path from", s1.key, "to", v.key, ":", v.d)
    # Display the sequence of vertices that make up the shortest path
    printPath(G1, s1, v)

# Output for Dijkstra's algorithm
print("\nDijkstra's Algorithm:\n")
dijkstra(G2, s2)
# Iterate through each vertex in the graph
for v in G2.vertices.values():
    # Display the weight of the shortest path from the source to the vertex
    print("Shortest path from", s2.key, "to", v.key, ":", v.d)
    # Display the sequence of vertices that make up the shortest path
    printPath(G2, s2, v)