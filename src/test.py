import random
from utils.clear import clear
from utils.test_search_speed import test_search_speed
from DataStructure.BSTree.BST import BST
from DataStructure.AVLTree.AVL import AVL


def generate_random_keys(total_data):
    """Generate random keys"""
    return random.sample(range(1, 100000), total_data)


def insert_keys(tree, keys):
    """Insert keys into tree"""
    for key in keys:
        tree.insert(key, "")


clear()

total_data = 10000
total_keys = 10

for _ in range(3):
    random_keys = generate_random_keys(total_data)
    keys_to_search = random.sample(random_keys, total_keys)

    bst = BST()
    avl = AVL()

    insert_keys(bst, random_keys)
    insert_keys(avl, random_keys)

    print(f"\nTotal data: {total_data}")
    print(f"Total keys: {total_keys}\n")

    bst_search_time = test_search_speed(bst, keys_to_search)
    print(f"Waktu pencarian BST: {bst_search_time}")

    avl_search_time = test_search_speed(avl, keys_to_search)
    print(f"Waktu pencarian AVL Tree: {avl_search_time}\n")

    print(
        "draw"
        if bst_search_time == avl_search_time
        else "AVL win" if bst_search_time > avl_search_time else "BST win"
    )
