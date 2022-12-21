from ursina import *
import random

from objects.smart_car import SmartCar
from objects.other_cars import OtherCars
from objects.trophy import Trophy
from objects.roads import AllRoads

app = Ursina()
window.title = 'Car.ai' 

camera.orthographic = True
camera.fov = 50

smart_car = SmartCar()

other_cars = OtherCars()


trophy = Trophy()

roads = AllRoads()

app.run()


