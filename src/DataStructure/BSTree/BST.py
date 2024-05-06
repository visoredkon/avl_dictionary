from DataStructure.BSTree.Node import Node


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        self.root = self.__insert(self.root, key, value)

    def __insert(self, root, key, value):
        if root is None:
            return Node(key, value)
        if key < root.key:
            root.left = self.__insert(root.left, key, value)
        else:
            root.right = self.__insert(root.right, key, value)
        return root

    def delete(self, key):
        self.root = self.__delete(self.root, key)

    def __delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self.__delete(root.left, key)
        elif key > root.key:
            root.right = self.__delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.__min_value_node(root.right)

            root.key = temp.key

            root.right = self.__delete(root.right, temp.key)

        return root

    def search(self, key):
        return self.__search(self.root, key)

    def __search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.__search(root.left, key)
        return self.__search(root.right, key)

    def __min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
