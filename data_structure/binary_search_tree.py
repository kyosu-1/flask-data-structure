from typing import Any, Dict, Optional


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BinnarySearchTree:
    def __init__(self):
        self.root = None

    def _insert_recursive(self, data: Dict[str, Any], node):
        """Insert data recursively

        Args:
            data (Dict[str, Any]): data
            node ([type]): node
        """
        if data["id"] < node.data["id"]:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(data, node.left)
        elif data["id"] > node.data["id"]:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(data, node.right)
        else:
            return
    
    def insert(self, data: Dict[str, Any]):
        """insert data

        Args:
            data (Dict[str, Any]): data
        """
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(data, self.root)
    
    def _search_recursive(self, blog_post_id: int, node: Node) -> Optional[Dict[str, Any]]:
        """Search recursively

        Args:
            blog_post_id (int): id
            node (Node): node

        Returns:
            Optional[Dict[str, Any]]: Returns data if the data corresponding to the id exists, or None if not.
        """
        if blog_post_id == node.data["id"]:
            return node.data

        if blog_post_id < node.data["id"] and node.left is not None:
            return self._search_recursive(blog_post_id, node.left)

        if blog_post_id > node.data["id"] and node.right is not None:
            return self._search_recursive(blog_post_id, node.right)

        return None

    def search(self, blog_post_id: int) -> Optional[Dict[str, Any]]:
        """search for data corresponding to id

        Args:
            blog_post_id (int): [description]

        Returns:
            Optional[Dict[str, Any]]: [description]
        """
        blog_post_id = int(blog_post_id)
        if self.root is None:
            return None

        return self._search_recursive(blog_post_id, self.root)
