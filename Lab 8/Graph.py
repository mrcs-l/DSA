# Implementation of breadth-first search (BSF) and
# depth-first search (DFS) algorithms with the
# adjacency-list graph representation.

from collections import deque

# Node class for the linked list.
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

# Linked list class to store the neighbors of a vertex.
class LinkedList:
    def __init__(self):
        self.head = None

    # Method to append a new node to the linked list.
    def append(self, key):
        # Create a new node.
        new_node = Node(key)
        # Check if the linked list is empty.
        if not self.head:
            # Set the new node as the head.
            self.head = new_node
            return
        # Traverse the linked list to find the last node.
        last_node = self.head
        # Iterate until the last node is found.
        while last_node.next:
            # Move to the next node.
            last_node = last_node.next
        # Set the new node as the next node of the last node.
        last_node.next = new_node

    # Method to iterate over the linked list.
    def __iter__(self):
        # Return the iterator object.
        current = self.head
        # Iterate as long as the current node is not None.
        while current:
            # Wait for the next call to return the current node key.
            yield current.key
            # Move to the next node.
            current = current.next

# Vertex class to represent vertices in the graph.
class Vertex:
    def __init__(self, key):
        self.key = key
        self.color = "WHITE"
        self.d = float("inf")
        self.parent = None
        self.neighbors = LinkedList()

# Graph class containing the vertices and edges.
class Graph:
    def __init__(self):
        # Represent the vertices as a dictionary.
        self.vertices = {}

    # Method to add a new vertex to the graph.
    def add_vertex(self, key):
        # Check if the vertex is not already in the graph.
        if key not in self.vertices:
            # Add the vertex to the graph.
            self.vertices[key] = Vertex(key)

    # Method to add a new edge to the graph.
    def add_edge(self, u, v):
        if u not in self.vertices:
            self.add_vertex(u)
        if v not in self.vertices:
            self.add_vertex(v)
        self.vertices[u].neighbors.append(v)
        
# Function to perform breadth-first search on a graph.
def BFS(G, s):
    # Iterate over all vertices in the graph.
    for u in G.vertices.values():
        # Check if the vertex is not the source vertex.
        if u.key != s.key:
            # Initialize the vertex attributes.
            u.color = "WHITE"
            u.d = float("inf")
            u.parent = None
    s.color = "GRAY"
    s.d = 0
    s.parent = None
    # Create a queue to store the vertices to visit.
    Q = deque()
    # Enqueue the souce vertex into the empty queue.
    Q.append(s)
    # Iterate as long as the queue is not empty.
    while Q:
        # Dequeue the vertex at the front of the queue.
        u = Q.popleft()
        # Search the neighbors of the dequeued vertex.
        for v_key in u.neighbors:
            # Retrieve the vertex object from the graph.
            v = G.vertices[v_key]
            # Check if the vertex is being visited for the first time.
            if v.color == "WHITE":
                # Update the vertex attributes.
                v.color = "GRAY"
                v.d = u.d + 1
                v.parent = u
                # The vertex is now on the frontier.
                Q.append(v)
        # "u" is now behind the frontier. 
        u.color = "BLACK"

# Function to perform depth-first search on a graph.
def DFS(G):
    # Iterate over all vertices in the graph.
    for u in G.vertices.values():
        # Initialize the vertex attributes.
        u.color = "WHITE"
        u.parent = None
    # Initialize the time variable as a list to pass by reference.
    time = [0]
    # Iterate over all vertices in the graph.
    for u in G.vertices.values():
        # Check if the vertex is not visited.
        if u.color == "WHITE":
            # Visit the vertex and its neighbors.
            DFS_visit(G, u, time)

# Function to visit a vertex and its neighbors in depth-first search.
def DFS_visit(G, u, time):
    # White vertex has just been discovered.
    time[0] += 1
    # Set the discovery time for the vertex.
    u.d = time[0]
    # The vertex is now being visited.
    u.color = "GRAY"
    # Explore the neighbors of the vertex.
    for v_key in u.neighbors:
        # Retrieve the vertex object from the graph.
        v = G.vertices[v_key]
        # Check if the vertex is not visited.
        if v.color == "WHITE":
            # Update the vertex attributes.
            v.parent = u
            # Recursively visit the vertex and its neighbors.
            DFS_visit(G, v, time)
    time[0] += 1
    # Update the finish time for the vertex.
    u.f = time[0]
    # The vertex is now visited.
    u.color = "BLACK"

# Undirected graph using the adjacency-list representation.
graph1 = {
    "r": ["s", "t", "w"],
    "s": ["r", "u", "v"],
    "t": ["r", "u"],
    "u": ["s", "t", "y"],
    "v": ["s", "w", "y"],
    "w": ["r", "v", "x", "z"],
    "x": ["w", "y", "z"],
    "y": ["u", "v", "x"],
    "z": ["w", "x"]
}

# Create a graph object and add the vertices and edges.
G1 = Graph()
for u in graph1:
    G1.add_vertex(u)
    for v in graph1[u]:
        G1.add_vertex(v)
        G1.add_edge(u, v)

# Perform BFS starting from vertex "s".
BFS(G1, G1.vertices["s"])

print("BFS for the following undirected graph:")
# Print out the order in which the vertices are discovered and
# the distance of each vertex to the source.
for u in G1.vertices.values():
    print(u.key, u.d)

# Directed graph using the adjacency-list representation.
graph2 = {
    "u": ["v", "x"],
    "v": ["y"],
    "w": ["y", "z"],
    "x": ["v"],
    "y": ["x"],
    "z": ["z"]
}

# Create a graph object and add the vertices and edges.
G2 = Graph()
for u in graph2:
    G2.add_vertex(u)
    for v in graph2[u]:
        G2.add_vertex(v)
        G2.add_edge(u, v)

# Perform DFS on the directed graph.
DFS(G2)

print("\nDFS for the following directed graph:")
# Print out the order in which the vertices are discovered and
# the finish time stamp for each vertex.
for u in G2.vertices.values():
    print(u.key, u.d, u.f)
