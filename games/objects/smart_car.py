from ursina import *

class SmartCar(Entity):
    def __init__(self):
        super().__init__(
            model='cube',
            texture='assets/car',
            collider='box',
            scale=(6,3),
            x = -37,
            y = 0.5,
            )
        self.collisions = 0

    def update(self, go_forward=False, go_backward=False, go_left=False, go_right=False, amount=1):
        # Handle Driving
        if go_forward:
            self.go_forward(amount)
        if go_backward:
            self.go_backward(amount)
        if go_left:
            self.go_left(amount)
        if go_right:
            self.go_right(amount)

        # Handle Collisions
        self.handle_collisions()

        # Manual Driving (for testing)
        self.manual_driving()

    def go_forward(self, amount=1):
        if self.x + amount < 37:
            self.x += amount

    def go_backward(self, amount=1):
        if self.x - amount > -37:
            self.x -= amount

    def go_left(self, amount=1):
        if self.y + amount > 22:
            self.y += amount

    def go_right(self, amount=1):
        if self.y - amount < -22:
            self.y -= amount

    def handle_collisions(self):
        if self.intersects().hit:
            self.collisions += 1

    def manual_driving(self):
         # Move Smart Car forward or backward by pressing A and D
        self.x -=held_keys['a']*5*time.dt
        self.x +=held_keys['d']*5*time.dt

        # Move Smart Car left or right by pressing W and S
        self.y +=held_keys['w']*5*time.dt
        self.y -=held_keys['s']*5*time.dt