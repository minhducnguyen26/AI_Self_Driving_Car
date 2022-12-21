import sys
sys.path.append('/Users/mnguyen/Documents/CS 4300/environment-minhducnguyen26/self_driving_car/games/objects')

# Objects in the environment
from smart_car import SmartCar
from other_cars import OtherCars
from trophy import Trophy
from roads import AllRoads

class Model():
    def __init__(self, amount_of_other_cars=5):
        self.smart_car = SmartCar()
        self.other_cars = OtherCars(amount_of_other_cars)
        self.trophy = Trophy()
        self.roads = AllRoads()

        self.time = 0
        self.done = False