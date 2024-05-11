from datetime import datetime


def test_search_speed(tree, keys_to_search):
    start_time = datetime.now()
    for key in keys_to_search:
        tree.search(key)
    end_time = datetime.now()

    delta = (end_time - start_time).total_seconds() * 1000

    return delta
