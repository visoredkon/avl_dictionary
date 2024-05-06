from DataStructure.AVLTree.Node import Node


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        self.root = self.__insert(self.root, key, value)

    def __insert(self, root, key, value):
        if not root:
            return Node(key, value)
        if key < root.key:
            root.left = self.__insert(root.left, key, value)
        else:
            root.right = self.__insert(root.right, key, value)

        root.height = 1 + max(
            self.__get_height(root.left), self.__get_height(root.right)
        )

        balance = self.__get_balance(root)

        if balance > 1 and key < root.left.key:
            return self.__rotate_right(root)

        if balance < -1 and key > root.right.key:
            return self.__rotate_left(root)

        if balance > 1 and key > root.left.key:
            root.left = self.__rotate_left(root.left)
            return self.__rotate_right(root)

        if balance < -1 and key < root.right.key:
            root.right = self.__rotate_right(root.right)
            return self.__rotate_left(root)

        return root

    def delete(self, key):
        self.root = self.__delete(self.root, key)

    def __delete(self, root, key):
        if not root:
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

        if root is None:
            return root

        root.height = 1 + max(
            self.__get_height(root.left), self.__get_height(root.right)
        )

        balance = self.__get_balance(root)

        if balance > 1 and self.__get_balance(root.left) >= 0:
            return self.__rotate_right(root)

        if balance > 1 and self.__get_balance(root.left) < 0:
            root.left = self.__rotate_left(root.left)
            return self.__rotate_right(root)

        if balance < -1 and self.__get_balance(root.right) <= 0:
            return self.__rotate_left(root)

        if balance < -1 and self.__get_balance(root.right) > 0:
            root.right = self.__rotate_right(root.right)
            return self.__rotate_left(root)

        return root

    def search(self, key):
        return self.__search(self.root, key)

    def __search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.__search(root.left, key)
        return self.__search(root.right, key)

    def __min_value_node(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    def __get_height(self, root):
        if not root:
            return 0
        return root.height

    def __get_balance(self, root):
        if not root:
            return 0
        return self.__get_height(root.left) - self.__get_height(root.right)

    def __rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.__get_height(z.left), self.__get_height(z.right))
        y.height = 1 + max(self.__get_height(y.left), self.__get_height(y.right))

        return y

    def __rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.__get_height(z.left), self.__get_height(z.right))
        y.height = 1 + max(self.__get_height(y.left), self.__get_height(y.right))

        return y
