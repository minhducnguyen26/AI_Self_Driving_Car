from ursina import *

class Trophy(Entity):
    def __init__(self):
        super().__init__(
            model='cube',
            texture='assets/trophy',
            collider='box',
            scale=(6,3),
            x = 37,
            y = self.get_random_y_position(),
            )

    def get_random_y_position(self):
        options = [-22,-17.5,-13,-8.5,-4,0.5, 5 ,9.5, 14, 18.5]
        return random.choice(options)