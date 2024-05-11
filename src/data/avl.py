from data.kamus import kamus
from DataStructure.AVLTree.AVL import AVLTree

avl = AVLTree()

for key, value in kamus:
    avl.insert(key, value)
