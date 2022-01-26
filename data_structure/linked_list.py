from lib2to3.pgen2.token import OP
from typing import List, Any, Dict, Optional


class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def to_list(self) -> List[Any]:
        """Convert a linear list to a standard list and return it.

        Returns:
            List[Any]: list
        """
        l = []
        if self.head is None:
            return L
        
        node = self.head
        while node:
            l.append(node.data)
            node = node.next_node
        return l

    def print_ll(self):
        """Output a linear list as a string to the standard output
        """
        ll_string = ""
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f"{str(node.data)} ->"
            node = node.next_node

        ll_string += " None"
        print(ll_string)

    def insert_beginning(self, data: Dict[str, Any]):
        """Insert at the top

        Args:
            data (Dict[str, Any]): data
        """
        if self.head is None:
            self.head = Node(data, None)
            self.last_node = self.head
            return

        new_node = Node(data, self.head)
        self.head = new_node
    
    def insert_at_end(self, data: Dict[str, Any]):
        """Insert at the end

        Args:
            data (Dict[str, Any]): data
        """
        if self.head is None:
            self.insert_beginning(data)
            return
            
        self.last_node.next_node = Node(data, None)
        self.last_node = self.last_node.next_node
    
    def get_user_by_id(self, user_id: int) -> Optional[Dict[str, Any]]:
        """get user data by user_id

        Args:
            user_id (int): user_id

        Returns:
            Optional[Dict[str, Any]]: user data
        """
        node = self.head
        while node:
            if node.data["id"] == user_id:
                return node.data
            node = node.next_node
        return None
