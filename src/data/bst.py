from data.kamus import kamus
from DataStructure.BSTree.BST import BST

bst = BST()

for key, value in kamus:
    bst.insert(key, value)
