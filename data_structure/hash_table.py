from typing import Any, Optional


class Data:
    def __init__(self, key: str, value: Any):
        self.key = key
        self.value = value


class Node:
    def __init__(self, data: Data, next_node: 'Node'=None):
        self.data = data
        self.next_node = next_node


class HashTable:

    def __init__(self, table_size):
        self.table_size = table_size
        self.hash_table = [None] * table_size
    
    def custom_hash(self, key: str) -> int:
        """Generate a hash value

        Args:
            key (str): string

        Returns:
            int: hash value
        """
        hash_value = 0
        for i in key:
            hash_value += ord(i)
            hash_value = (hash_value * ord(i)) % self.table_size
        return hash_value
    
    def add_key_value(self, key: str, value: Any):
        """Add keys and values to the hash table

        Args:
            key (str): key
            value (Any): value
        """
        hashed_key = self.custom_hash(key)
        if self.hash_table[hashed_key] is None:
            self.hash_table[hashed_key] = Node(Data(key, value), None)
        else:
            node = self.hash_table[hashed_key]
            while node.next_node:
                node = node.next_node
            
            node.next_node = Node(Data(key, value), None)
    
    def get_value(self, key: str) -> Any:
        """get a value by a key

        Args:
            key (str): key

        Returns:
            Any: value
        """
        hashed_key = self.custom_hash(key)
        if self.hash_table[hashed_key] is not None:
            node = self.hash_table[hashed_key]
            if node.next_node is None:
                return node.data.value
            while node.next_node:
                if key == node.data.key:
                    return node.data.value
                node = node.next_node
            
            if key == node.data.key:
                return node.data.value
        return None
    
    def print_talbe(self):
        """Output the contents of the hash table to standard output
        """
        print("{")
        for i, val in enumerate(self.hash_table):
            if val is not None:
                llist_string = ""
                node = val
                if node.next_node:
                    while node.next_node:
                        llist_string += (
                            str(node.data.key) + " : " + str(node.data.value) + " --> "
                        )
                        node = node.next_node
                    llist_string += (
                        str(node.data.key) + " : " + str(node.data.value) + " --> None"
                    )
                    print(f"   [{i}] {llist_string}")
                else:
                    print(f"   [{i}] {val.data.key} : {val.data.value}")
            else:
                print(f"   [{i}] {val}")
        print("}")
