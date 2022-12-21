from ursina import *

class OtherCar(Entity):
    def __init__(self):
        super().__init__(
            model='cube',
            texture='assets/other_car',
            collider='box',
            scale=(6,3),
            x = self.get_random_x_position(),
            y = self.get_random_y_position(),
            color = color.random_color(),
            )

    def get_random_x_position(self):
        options = [-30, -20, -10, 0, 10, 20, 30, 40]
        return random.choice(options)

    def get_random_y_position(self):
        options = [-22,-17.5,-13,-8.5,-4,0.5, 5 ,9.5, 14, 18.5]
        return random.choice(options)

    def update(self):
        self.x += 0.5 * time.dt

class OtherCars(Entity):
    def __init__(self, amount_of_cars=5):
        super().__init__()
        self.other_cars_list = []
        self.add_other_cars(amount_of_cars)    

    def add_other_cars(self,amount_of_cars=5):
        for i in range(amount_of_cars):
            new_car = OtherCar()
            self.other_cars_list.append(new_car)

