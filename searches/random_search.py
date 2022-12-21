import sys
sys.path.append('/Users/mnguyen/Documents/CS 4300/environment-minhducnguyen26/self_driving_car/models')

import random
from agent_model import AgentModel

def random_search(actions: list[str]):
    action = random.choice(actions)
    amount = random.randint(1, 10)

    return action, amount   