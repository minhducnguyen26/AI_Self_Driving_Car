import queue

def depth_first_search(init_state, actions: list[str], result, goal_test: bool, queue_size=1000000):
    # LIFO queue
    frontier = queue.LifoQueue(maxsize=queue_size)
    frontier.put(("none", init_state))

    while not frontier.empty():
        current_action, current_state = frontier.get()

        if goal_test(current_state):
            return current_action

        for action in actions:
            next_state = result(current_state, action)
            frontier.put((action, next_state))

    return False