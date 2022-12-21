import queue
from searches.depth_limited_search import depth_limited_search

def iterative_deepening_search(init_state, actions: list[str], result, goal_test: bool, queue_size=1000000):
    for depth in range(queue_size):
        result = depth_limited_search(init_state, actions, result, goal_test, depth, queue_size)
        if result != False:
            return result
    return False