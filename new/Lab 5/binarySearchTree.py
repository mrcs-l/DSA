# Implementation for binary search tree (BST) data structure

# Binary Search Tree class that represents an empty BST.
class BinarySearchTree:
    def __init__(self):
        self.root = None

# Node class that represents a node in a BST.
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.p = None

# Function that inserts a new node into the BST by tracing down from the root.
def Tree_Insert(T, z):
    x = T.root # node being compared with z
    y = None # y will be a parent of x
    while x != None: # descend until reaching a leaf
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y # found location - insert z with parent y
    if y == None:
        T.root = z # tree T was empty
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z

# Function that recursively prints out all the elements of a BST in sorted order.
def Inorder_Tree_Walk(x):
    if x != None:
        Inorder_Tree_Walk(x.left)
        print(x.key)
        Inorder_Tree_Walk(x.right)

# Function that searches for a key in a BST.
def Tree_Search(x, k):
    if x == None or k == x.key:
        return x 
    if k < x.key:
        return Tree_Search(x.left, k)
    else:
        return Tree_Search(x.right, k)
    
# Function that returns the minimum element in a BST.
def Tree_Minimum(x):
    while x.left != None: 
        x = x.left # reach the leftmost node
    return x

# Function that returns the maximum element in a BST.
def Tree_Maximum(x):
    while x.right != None: 
        x = x.right # reach the rightmost node
    return x 

# Function that returns the successor of a node in a BST.
def Tree_Successor(x):
    if x.right != None:
        return Tree_Minimum(x.right) # leftmost node in right subtree
    else: # find the lowest ancestor of x whose left child is an ancestor of x
        y = x.p
        while y != None and x == y.right:
            x = y
            y = y.p
        return y 
    
# Function that returns the predecessor of a node in a BST.
def Tree_Predecessor(x):
    if x.left != None:
        return Tree_Maximum(x.right) # rightmost node in left subtree
    else: # find the lowest ancestor of x whose right child is an ancestor of x
        y = x.p
        while y != None and x == y.left:
            x = y
            y = y.p
        return y
    
# Test case 1
Tree1 = BinarySearchTree() # Start with an empty tree
Tree_Insert(Tree1, Node(15))
Tree_Insert(Tree1, Node(6))
Tree_Insert(Tree1, Node(18))
Tree_Insert(Tree1, Node(3))
Tree_Insert(Tree1, Node(7))
Tree_Insert(Tree1, Node(17))
Tree_Insert(Tree1, Node(20))
Tree_Insert(Tree1, Node(2))
Tree_Insert(Tree1, Node(4))
Tree_Insert(Tree1, Node(13))
Tree_Insert(Tree1, Node(9))

Inorder_Tree_Walk(Tree1.root) # Tree traversal
print("Tree Minimum: ", Tree_Minimum(Tree1.root).key)
print("Tree Maximum: ", Tree_Maximum(Tree1.root).key)
print("Tree Search: ", Tree_Search(Tree1.root, 13).key)
print("Tree Successor: ", Tree_Successor(Tree_Search(Tree1.root, 13)).key, "\n")

# Test case 2
Tree2 = BinarySearchTree() # Start with an empty tree
Tree_Insert(Tree2, Node(37))
Tree_Insert(Tree2, Node(24))
Tree_Insert(Tree2, Node(51))
Tree_Insert(Tree2, Node(7))
Tree_Insert(Tree2, Node(32))
Tree_Insert(Tree2, Node(41))
Tree_Insert(Tree2, Node(85))
Tree_Insert(Tree2, Node(2))
Tree_Insert(Tree2, Node(40))
Tree_Insert(Tree2, Node(120))

Inorder_Tree_Walk(Tree2.root) # Tree traversal
print("Tree Minimum: ", Tree_Minimum(Tree2.root).key)
print("Tree Maximum: ", Tree_Maximum(Tree2.root).key)
print("Tree Search: ", Tree_Search(Tree2.root, 40).key)
print("Tree Predecessor: ", Tree_Predecessor(Tree_Search(Tree2.root, 40)).key)