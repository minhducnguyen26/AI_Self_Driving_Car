from ursina import *
import random

app = Ursina()
window.title = 'Car.ai' 

camera.orthographic = True
camera.fov = 10

# Create Roads
road_1 = Entity(model='quad', texture='objects/assets/road', scale=20, z=1)
road_2 = duplicate(road_1, y=15)
roads_list = [road_1, road_2]

# Create Smart Car
smart_car = Entity(model='quad', texture='objects/assets/car', collider='box', scale=(2,1), rotation_z=-90, y = -3)

# Create Other Cars
other_cars_list = []
def create_other_cars():
  value = random.uniform(-2,2)
  new_random_car = duplicate(smart_car, texture='objects/assets/other_car', x = 2*value, y = 25, 
                            color=color.random_color(), rotation_z = 90 if value < 0 else -90)
  
  other_cars_list.append(new_random_car)
  invoke(create_other_cars, delay=0.5)
  
create_other_cars()

def update():
    # Move Smart Car left and right by pressing A and D
    smart_car.x -=held_keys['a']*5*time.dt
    smart_car.x +=held_keys['d']*5*time.dt

    # Move Smart Car up and down by pressing W and S
    smart_car.y +=held_keys['w']*5*time.dt
    smart_car.y -=held_keys['s']*5*time.dt

    for road in roads_list:
        road.y -= 6*time.dt
        
        # Reset road position
        if road.y < -15:
            road.y += 30
    
    for other_car in other_cars_list:
        if other_car.x < 0:
            other_car.y -= 10 * time.dt
        else:
            other_car.y -= 5 * time.dt
        
        if other_car.y < -10:
            other_cars_list.remove(other_car)
            destroy(other_car)
    
    if smart_car.intersects().hit:
        smart_car.shake()

app.run()