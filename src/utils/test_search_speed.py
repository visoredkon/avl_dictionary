import time


def test_search_speed(tree, keys_to_search):
    start_time = time.time()
    for key in keys_to_search:
        tree.search(key)
    end_time = time.time()
    return end_time - start_time
