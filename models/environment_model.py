import sys
sys.path.append('/Users/mnguyen/Documents/CS 4300/environment-minhducnguyen26/self_driving_car')

from models.model import Model

class EnvironmentModel():
    def __init__(self, model: Model, max_time_steps=100000):
        self.model = model
        self.max_time_steps = max_time_steps

    def get_observable_percepts(self):
        return {
            "smart_car": self.model.smart_car,
            "other_cars": self.model.other_cars,
            "trophy": self.model.trophy,
            "roads": self.model.roads,
            "time": self.model.time,
            "done": self.model.done
        }

    def update_time_step(self):
        self.model.time += 1

    def apply_actions(self, action: str, amount=1):
        if action == "go_forward":
            self.model.smart_car.update(go_forward=True, amount=amount)

        elif action == "go_backward":
            self.model.smart_car.update(go_backward=True, amount=amount)

        elif action == "go_left":
            self.model.smart_car.update(go_left=True, amount=amount)

        elif action == "go_right":
            self.model.smart_car.update(go_right=True, amount=amount)

    def action_result(self, current_state: Model, action: str, amount=1) -> Model:
        self.apply_actions(action, amount)
        return self.model

    def done(self) -> bool:
        smart_car = self.model.smart_car
        trophy = self.model.trophy

        if smart_car.x >= 31:
            if smart_car.y >= trophy.y - 2 and smart_car.y <= trophy.y + 2:
                print("Smart Car has reached the trophy!")
                return True
       
        elif smart_car.collisions > 100:
            print("Smart Car has collided too many times!")
            return True

        elif self.model.time > self.max_time_steps:
            print("Smart Car has reached the maximum time steps!")
            return True

        else:
            return False