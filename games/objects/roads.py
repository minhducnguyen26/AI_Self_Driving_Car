from ursina import *

class RoadsTopRow(Entity):
    def __init__(self):
        super().__init__()

        self.road_1 = Entity(model='quad', texture='assets/road',rotation_z=-90, scale=30, x=-25, y=17)
        self.road_2 = duplicate(entity=self.road_1, x=-5)
        self.road_2 = duplicate(entity=self.road_1, x=25)  

class RoadsMiddleRow(Entity):
    def __init__(self):
        super().__init__()

        self.road_1 = Entity(model='quad', texture='assets/road',rotation_z=-90, scale=30, x=-25, y=-1)
        self.road_2 = Entity(model='quad', texture='assets/road',rotation_z=-90, scale=30, x=-5, y=-1)
        self.road_3 = Entity(model='quad', texture='assets/road',rotation_z=-90, scale=30, x=25, y=-1)

class RoadsBottomRow(Entity):
    def __init__(self):
        super().__init__()  

        self.road_1 = Entity(model='quad', texture='assets/road',rotation_z=-90, scale=30, x=-25, y=-19)
        self.road_2 = duplicate(self.road_1, x=5)
        self.road_3 = duplicate(self.road_1, x=25)


class AllRoads(Entity):
    def __init__(self):
        super().__init__()

        self.roads_top_row = RoadsTopRow()
        self.roads_middle_row = RoadsMiddleRow()
        self.roads_bottom_row = RoadsBottomRow()


