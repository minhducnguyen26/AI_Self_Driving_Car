import sys
sys.path.append('/Users/mnguyen/Documents/CS 4300/environment-minhducnguyen26/self_driving_car/self_driving_car')

import random
from models.model import Model

class AgentModel():
    def __init__(self, model: Model):
        self.model = model

    def update_from_percepts(self, percepts_dict):
        self.model.smart_car = percepts_dict["smart_car"]
        self.model.other_cars = percepts_dict["other_cars"]
        self.model.trophy = percepts_dict["trophy"]
        self.model.roads = percepts_dict["roads"]
       
        self.model.time = percepts_dict["time"]
        self.model.done = percepts_dict["done"]

    def get_legal_actions(self):
        return ["go_forward", "go_backward", "go_left", "go_right"]

    def goal_test(self, state: Model) -> bool:
        smart_car = state.smart_car
        trophy = state.trophy

        if smart_car.x >= 31:
            if smart_car.y >= trophy.y - 2 and smart_car.y <= trophy.y + 2:
                print("Smart Car has reached the trophy!")
                return True
        
        if smart_car.x >= 31 and smart_car.y == trophy.y:
            print("Smart Car has reached the trophy!")
            return True
       
        elif smart_car.collisions > 100:
            print("Smart Car has collided too many times!")
            return True

        else:
            return False

    def copy(self):
        return self.model
        