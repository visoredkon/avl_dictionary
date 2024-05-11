from data.kamus import kamus
from DataStructure.AVLTree.AVL import AVL

avl = AVL()

for key, value in kamus:
    avl.insert(key, value)
