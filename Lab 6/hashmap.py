# Implementation for open addressing with double hashing and collision resolution

# Function representing the first hash function
def h1(k, m):
    return k % m 

# Function representing the second hash function for the first test case
def h2_case1(k, m):
    # Logic for first test case
    return 1 + (k % (m - 2))

# Function representing the second hash function for the second test case
def h2_case2(k, m):
    # Logic for second test case
    return (m - 2) - (k % (m - 2))

# Function for inserting a key into the hash table
# Takes in the hash table T, key k, table size m, and hash functions h1 and h2
def hashInsert(T, k, m, h1, h2): 
  i = 0 
  # Loop until an empty slot is found
  while i < m: 
    # Hash function h(k, i) = (h1(k) + i * h2(k)) % m 
    q = (h1(k, m) + i * h2(k, m)) % m 
    # Check where to insert the key
    if T[q] is None or T[q] == "DELETED":
      # Key can be inserted at index q
      T[q] = k
      return q
    # Key already exists in the hash table
    else:
      # Move to the next slot
      i += 1 
  # Error for when the hash table is full
  print("Hash table overflow")
  return None

# Function for searching a key in the hash table
# Takes in the hash table T, key k, table size m, and hash functions h1 and h2
def hashSearch(T, k, m, h1, h2):
  i = 0 
  # Loop until an empty slot is found
  while i < m:
    # Hash function h(k, i) = (h1(k) + i * h2(k)) % m
    q = (h1(k, m) + i * h2(k, m)) % m 
    # Check where to search for the key
    if T[q] == k:
      # Key is found at index q
      return q
    # Check when the key is not found
    elif T[q] is None:
      return None
    # Key has been deleted
    else:
      # Move to the next slot
      i += 1
  return None

# Function for printing the hash table as an array
def printHashTable(T):
  # Loop through the size of the hash table
  for i in range(len(T)):
    # Check if the element is None, DELETED, or a key and print accordingly
    if T[i] is None:
      print("NIL", end=" ")
    elif T[i] == "DELETED":
      print("DELETED", end=" ")
    else:
      print(T[i], end=" ")
  print("\n")

# Test case 1
print("Test case 1:")
# Initialize the hash table with size m = 13
T1 =  [None] * 13

# Insert keys into the hash table in expected order
hashInsert(T1, 79, 13, h1, h2_case1)
hashInsert(T1, 69, 13, h1, h2_case1)
hashInsert(T1, 72, 13, h1, h2_case1)
hashInsert(T1, 50, 13, h1, h2_case1)
hashInsert(T1, 98, 13, h1, h2_case1)
hashInsert(T1, 14, 13, h1, h2_case1)

# Display the contents of the hash table
printHashTable(T1)

# Search for keys in the hash table
search_keys_in_T1 = [14, 66]
for key in search_keys_in_T1:
  result = hashSearch(T1, key, 13, h1, h2_case1)
  # Check if the key exists in the hash table
  if result is not None:
    # Print the index where the key is found
    print(f"Key {key} found at index {result}")
  # Otherwise, the key does not exist
  else:
    print(f"Key {key} not found\n")

# Test case 2
print("Test case 2:")
# Initialize the hash table with size m = 7
T2 =  [None] * 7

# Insert keys into the hash table in expected order
hashInsert(T2, 10, 7, h1, h2_case2)
hashInsert(T2, 82, 7, h1, h2_case2)
hashInsert(T2, 40, 7, h1, h2_case2)
hashInsert(T2, 35, 7, h1, h2_case2)
hashInsert(T2, 15, 7, h1, h2_case2)
hashInsert(T2, 21, 7, h1, h2_case2)
hashInsert(T2, 52, 7, h1, h2_case2)

# Display the contents of the hash table
printHashTable(T2)

# Search for keys in the hash table
search_keys_in_T2 = [52, 11]
for key in search_keys_in_T2:
  result = hashSearch(T2, key, 7, h1, h2_case2)
    # Check if the key exists in the hash table
  if result is not None:
    # Print the index where the key is found
    print(f"Key {key} found at index {result}")
  # Otherwise, the key does not exist
  else:
    print(f"Key {key} not found")