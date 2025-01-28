class HashTable:
    def __init__(self, size):
        self.size = size  # Hash table size
        self.table = [[] for _ in range(size)]  # Initializing table with empty lists 

    def hash_function(self, key):
        # Simple hash function: Add the ASCII values of characters in the key and mod by table size
        return sum(ord(c) for c in key) % self.size

    def insert(self, key, value):
        # Insert the key-value pair into the hash table
        index = self.hash_function(key)
        # Check if the key already exists in the chain
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                # Update the value if the key already exists
                self.table[index][i] = (key, value)
                return
        # If key does not exist, append the key-value pair to the chain
        self.table[index].append((key, value))

    def search(self, key):
        # Search for the value associated with the key
        index = self.hash_function(key)
        # Traverse the linked list at the index
        for k, v in self.table[index]:
            if k == key:
                return v  # Return the value if key is found
        return None  # Return None if the key doesn't exist

    def delete(self, key):
        # Delete the key-value pair from the hash table
        index = self.hash_function(key)
        # Traverse the linked list at the index and remove the key-value pair
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]  # Remove the pair
                return True
        return False  # Return False if the key wasn't found

    def display(self):
        # Display the hash table
        for index, bucket in enumerate(self.table):
            print(f"Index {index}: {bucket}")


# Example usage:
ht = HashTable(10)  # Create a hash table with 10 buckets

# Insert key-value pairs
ht.insert("book", 10)
ht.insert("shopping", 20)
ht.insert("food", 30)
ht.insert("house", 40)
ht.insert("apple", 50) # This will update the value for 'apple'
ht.insert("animal", 60)  
# Display the hash table
ht.display()

# Search for values
print("\nSearching for 'shopping':", ht.search("shopping"))  # Output: 20
print("Searching for 'food':", ht.search("food"))  # Output: 30
print("Searching for 'gold':", ht.search("gold"))  # Output: None (key not found)

# Delete a key
print("\nDeleting 'shopping':", ht.delete("shopping"))  # Output: True
ht.display()

# Try deleting a non-existing key
print("\nDeleting 'gold':", ht.delete("gold"))  # Output: False
