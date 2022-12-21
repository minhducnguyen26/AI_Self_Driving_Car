from ursina import *

# Environment and Agent Models
from models.model import Model
from models.environment_model import EnvironmentModel
from models.agent_model import AgentModel

# Search Algorithms
from searches.random_search import random_search
from searches.breadth_first_search import breadth_first_search
from searches.depth_first_search import depth_first_search
from searches.depth_limited_search import depth_limited_search
from searches.iterative_deepening_search import iterative_deepening_search

def main(): 
    model = Model()   
    env = EnvironmentModel(model)
    agent = AgentModel(model)

    while not env.done():
        percepts_dict = env.get_observable_percepts()
        agent.update_from_percepts(percepts_dict)
        actions = agent.get_legal_actions()

        initial_state = agent.copy()
        result = env.action_result
        goal_test = agent.goal_test

        #* Random Search (Random Agent)
        action, amount = random_search(actions)

        #* Breadth First Search
        # action, amount = breadth_first_search(initial_state, actions, result, goal_test)

        #* Depth First Search
        # depth_first_search(init_state, actions, result, goal_test)

        #* Depth Limited Search
        # depth_limited_search(init_state, actions, result, goal_test, limit=10)

        #* Iterative Deepening Search
        # iterative_deepening_search(init_state, actions, result, goal_test)

        env.apply_actions(action, amount)
        env.update_time_step()

if __name__ == "__main__":
    # Set up the game environment
    app = Ursina()
    window.title = 'Car.ai' 
    camera.orthographic = True
    camera.fov = 50

    main()

    app.run()