import queue

def depth_limited_search(init_state, actions: list[str], result, goal_test: bool, limit=10, queue_size=1000000):
    # LIFO queue
    frontier = queue.LifoQueue(maxsize=queue_size)
    frontier.put(("none", init_state))

    while not frontier.empty():
        current_action, current_state = frontier.get()

        if goal_test(current_state):
            return current_action

        if current_state.depth < limit:
            for action in actions:
                next_state = result(current_state, action)
                frontier.put((action, next_state))

    return False