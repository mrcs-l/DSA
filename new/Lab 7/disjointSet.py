# Implementation for disjoint-set data structure using a tree representation
# with the union by rank and path compression heuristics.

# Node class to represent each element in the set
class Node:
    def __init__(self, data):
        # Value of the node
        self.data = data
        # Pointer to the parent node
        self.parent = self
        # Initial rank of the node
        self.rank = 0

# Function to create a new tree with a single node
def makeSet(x):
    # The single node is its own parent
    x.parent = x
    # Initialize the rank of the node to 0
    x.rank = 0

# Function to combine two trees into one
def Union(x, y):
    # Link the two following the union by rank heuristic
    Link(findSet(x), findSet(y))

# Function to make the root of tree with smaller rank
# point to the root of tree with larger rank
def Link(x, y):
    # Case 1: rank of tree is unchanged
    # Check whether the rank of x is greater than the rank of y
    if x.rank > y.rank:
        # x represents the larger tree, so y is made a child of x
        y.parent = x
    # Case 2: rank of tree increases by 1
    # Otherwise, the rank of y is greater than or equal to the rank of x
    else:
        # x becomes a child of y
        x.parent = y
        # Check whether the ranks of x and y are equal
        if x.rank == y.rank:
            y.rank = y.rank + 1 # Increment

# Function to find the root of the tree containing x
def findSet(x):
    # Check whether x is not the root
    if x != x.parent: 
        # Path compression: update the parent of x along the path to the root
        x.parent = findSet(x.parent)
    # Return the root 
    return x.parent

# Initialize an empty dictionary to store the nodes of the disjoint-set
nodes = {}
# Iterate through the characters "a" to "h"
for char in "abcdefgh":
    # Create a new node object with the character as its data
    # and add it to the dictionary with the character as the key
    nodes[char] = Node(char)
    # Create a set for each node
    makeSet(nodes[char])

# Perform a sequence of operations 
Union(nodes["b"], nodes["a"])
Union(nodes["d"], nodes["c"])
Union(nodes["f"], nodes["e"])
Union(nodes["f"], nodes["g"])
Union(nodes["c"], nodes["b"])
Union(nodes["g"], nodes["h"])
Union(nodes["d"], nodes["g"])
findSet(nodes["f"])

print("Results of parent element for each node:")
for char, node in nodes.items():
    print(f"{char}.p = {node.parent.data}")

print("\nResults of rank for each node:")
for char, node in nodes.items():
    print(f"{char}.rank = {node.rank}")