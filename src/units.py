import src.misc as misc
import src.map2 as map2

config = misc.get_config()
# townHall = main.townHall
# huts = main.huts
# cannons = main.cannons
# walls = main.walls

class Unit:

    def __init__(self, x, y, max_hp, damage, speed):
        self.x = x
        self.y = y
        self.hp = max_hp
        self.max_hp = max_hp
        self.damage = damage
        self.speed = speed

    def attack(self, nearest_target):
        if nearest_target.hp > 0:
            nearest_target.hp -= self.damage

    def find_nearest_target(self, game_map, townHall, huts, cannons, walls, wizard_towers, is_townhall):
        nearest_target = None
        nearest_target_distance = 99999
        for hut in huts:
            if hut.hp > 0:
                distance = misc.distance(self.x, self.y, hut.x1, hut.y1)
                if distance < nearest_target_distance:
                    nearest_target = hut
                    nearest_target_distance = distance
        for cannon in cannons:
            if cannon.hp > 0:
                distance = misc.distance(self.x, self.y, (cannon.x1 + cannon.x2)/2, (cannon.y1 + cannon.y2)/2)
                if distance < nearest_target_distance:
                    nearest_target = cannon
                    nearest_target_distance = distance
        for wizard_tower in wizard_towers:
            if wizard_tower.hp > 0:
                distance = misc.distance(self.x, self.y, wizard_tower.x1, wizard_tower.y1)
                if distance < nearest_target_distance:
                    nearest_target = wizard_tower
                    nearest_target_distance = distance
        if is_townhall:
            townHallDistance = misc.distance(self.x, self.y, (townHall.x1 + townHall.x2)/2, (townHall.y1 + townHall.y2)/2)
            if townHallDistance < nearest_target_distance:
                nearest_target = townHall
                nearest_target_distance = townHallDistance
        return nearest_target

    def find_nearest_defense(self, game_map, townHall, huts, cannons, walls, wizard_towers, is_townhall):
        nearest_defense = None
        nearest_defense_distance = 99999
        for cannon in cannons:
            if cannon.hp > 0:
                distance = misc.distance(self.x, self.y, (cannon.x1 + cannon.x2)/2, (cannon.y1 + cannon.y2)/2)
                if distance < nearest_defense_distance:
                    nearest_defense = cannon
                    nearest_defense_distance = distance
        for wizard_tower in wizard_towers:
            if wizard_tower.hp > 0:
                distance = misc.distance(self.x, self.y, wizard_tower.x1, wizard_tower.y1)
                if distance < nearest_defense_distance:
                    nearest_defense = wizard_tower
                    nearest_defense_distance = distance
        if nearest_defense == None:
            for hut in huts:
                if hut.hp > 0:
                    distance = misc.distance(self.x, self.y, hut.x1, hut.y1)
                    if distance < nearest_defense_distance:
                        nearest_defense = hut
                        nearest_defense_distance = distance
            if is_townhall:
                townHallDistance = misc.distance(self.x, self.y, (townHall.x1 + townHall.x2)/2, (townHall.y1 + townHall.y2)/2)
                if townHallDistance < nearest_defense_distance:
                    nearest_defense = townHall
                    nearest_defense_distance = townHallDistance
        return nearest_defense

    def to_travel_x(self, game_map, nearest_target, walls):
        travel_distance = 9999
        # if nearest target is not none
        if nearest_target != None:
            for x in range(nearest_target.x1-1, nearest_target.x2+1):
                for y in range(nearest_target.y1-1, nearest_target.y2+1):
                    if misc.distance(self.x, self.y, x, y) < travel_distance:
                        travel_distance = misc.distance(self.x, self.y, x, y)
                        req_x = x
                        req_y = y
            return req_x

    def to_travel_y(self, game_map, nearest_target, walls):
        travel_distance = 9999
        if nearest_target != None:
            for x in range(nearest_target.x1-1, nearest_target.x2+1):
                for y in range(nearest_target.y1-1, nearest_target.y2+1):
                    if misc.distance(self.x, self.y, x, y) < travel_distance:
                        travel_distance = misc.distance(self.x, self.y, x, y)
                        req_x = x
                        req_y = y
            return req_y

    def move(self, x,y, walls):              
        # if x and y are not none
        if x != None and y != None:
            if self.x != x:
                if self.x < x:                
                    # check if there is a wall in the way
                    is_wall = False
                    for wall in walls:
                        if self.x+1 == wall.x1 and self.y == wall.y1:
                            is_wall = True
                            self.attack(wall)
                            # # exit the loop after hitting the wall once
                            # break
                    if is_wall == False:
                        self.x += 1
                elif self.x > x:
                    is_wall = False
                    for wall in walls:
                        if self.x-1 == wall.x2 and self.y == wall.y2:
                            is_wall = True
                            self.attack(wall)
                            # # exit the loop after hitting the wall once
                            # break
                    if is_wall == False:
                        self.x -= 1
            # if self.y is not y, move one step closer to y
            if self.y != y:
                if self.y < y:
                    is_wall = False
                    for wall in walls:
                        if self.y+1 == wall.y1 and self.x == wall.x1:
                            is_wall = True
                            self.attack(wall)
                            # # exit the loop after hitting the wall once
                            # break
                    if is_wall == False:
                        self.y += 1
                elif self.y > y:
                    is_wall = False
                    for wall in walls:
                        if self.y-1 == wall.y2 and self.x == wall.x2:
                            is_wall = True
                            self.attack(wall)
                            # # exit the loop after hitting the wall once
                            # break
                    if is_wall == False:
                        self.y -= 1 

    def hero_move(self, input, game_map):
        if input == "w":
            self.attack_direction = "up"
            if self.x >= self.speed:
                if game_map.map[self.x - self.speed][self.y] == map2.grass_id and game_map.map[self.x - 1][self.y] == map2.grass_id:
                    self.x -= self.speed
                elif game_map.map[self.x - 1][self.y] == map2.grass_id:
                    self.x -= 1
        elif input == "s":
            self.attack_direction = "down"
            if self.x <= 39 - self.speed:
                if game_map.map[self.x + self.speed][self.y] == map2.grass_id and game_map.map[self.x + 1][self.y] == map2.grass_id:
                    self.x += self.speed
                elif game_map.map[self.x + 1][self.y] == map2.grass_id:
                    self.x += 1
        elif input == "a":
            self.attack_direction = "left"
            if self.y >= self.speed:
                if game_map.map[self.x][self.y - self.speed] == map2.grass_id and game_map.map[self.x][self.y - 1] == map2.grass_id:
                    self.y -= self.speed
                elif game_map.map[self.x][self.y - 1] == map2.grass_id:
                    self.y -= 1
        elif input == "d":
            self.attack_direction = "right"
            if self.y <= 39 - self.speed:
                if game_map.map[self.x][self.y + self.speed] == map2.grass_id and game_map.map[self.x][self.y + 1] == map2.grass_id:
                    self.y += self.speed
                elif game_map.map[self.x][self.y + 1] == map2.grass_id:
                    self.y += 1

class King(Unit):
    
    def __init__(self, x, y):
        super().__init__(x, y, config["king_hp"], config["king_damage"], config["king_speed"])
        self.aoe = config["king_aoe"]
        self.attack_direction = "up"

    def sword_attack(self, townHall, huts, cannons, walls, wizard_towers, is_townhall):
        if self.attack_direction == "up":
            for building in walls + huts:
                if self.x == building.x1+1 and self.y == building.y1:
                    if building.hp > 0:
                        building.hp -= self.damage
            for building in cannons + wizard_towers:
                if self.x == building.x2+1 and self.y >= building.y1 and self.y <= building.y2:
                    if building.hp > 0:
                        building.hp -= self.damage
            if is_townhall:
                if self.x == townHall.x2+1 and self.y >= townHall.y1 and self.y <= townHall.y2:
                    if townHall.hp > 0:
                        townHall.hp -= self.damage
        elif self.attack_direction == "down":
            for building in walls + huts:
                if self.x == building.x2-1 and self.y == building.y1:
                    if building.hp > 0:
                        building.hp -= self.damage
            for building in cannons + wizard_towers:
                if self.x == building.x1-1 and self.y >= building.y1 and self.y <= building.y2:
                    if building.hp > 0:
                        building.hp -= self.damage
            if is_townhall:
                if self.x == townHall.x2-1 and self.y >= townHall.y1 and self.y <= townHall.y2:
                    if townHall.hp > 0:
                        townHall.hp -= self.damage
        elif self.attack_direction == "left":
            for building in walls + huts:
                if self.x == building.x1 and self.y == building.y2+1:
                    if building.hp > 0:
                        building.hp -= self.damage
            for building in cannons + wizard_towers:
                if self.x >= building.x1 and self.x <= building.x2 and self.y == building.y2+1:
                    if building.hp > 0:
                        building.hp -= self.damage
            if is_townhall:
                if self.x >= townHall.x1 and self.x <= townHall.x2 and self.y == townHall.y2+1:
                    if townHall.hp > 0:
                        townHall.hp -= self.damage
        elif self.attack_direction == "right":
            for building in walls + huts:
                if self.x == building.x1 and self.y == building.y1-1:
                    if building.hp > 0:
                        building.hp -= self.damage
            for building in cannons + wizard_towers:
                if self.x >= building.x1 and self.x <= building.x2 and self.y == building.y1-1:
                    if building.hp > 0:
                        building.hp -= self.damage
            if is_townhall:
                if self.x >= townHall.x1 and self.x <= townHall.x2 and self.y == townHall.y1-1:
                    if townHall.hp > 0:
                        townHall.hp -= self.damage

    def axe_attack(self, townHall, huts, cannons, walls, wizard_towers, is_townhall):

        for building in huts + walls:
            if misc.distance(self.x, self.y, building.x1, building.y1) <= self.aoe:
                if building.hp > 0:
                    building.hp -= self.damage

        for building in cannons + wizard_towers:
            building_in_range = 0
            for x in range(building.x1, building.x2):
                for y in range(building.y1, building.y2):
                    if misc.distance(self.x, self.y, x, y) <= self.aoe:
                        building_in_range = 1
            if building_in_range == 1:
                building.hp -= self.damage
        
        if is_townhall == 1:
            town_hall_in_range = 0
            for x in range(townHall.x1, townHall.x2):
                for y in range(townHall.y1, townHall.y2):
                    if misc.distance(self.x, self.y, x, y) <= self.aoe:
                        town_hall_in_range = 1
            if town_hall_in_range == 1:
                townHall.hp -= self.damage

class Queen(Unit):
    
    def __init__(self, x, y):
        super().__init__(x, y, config["queen_hp"], config["queen_damage"], config["queen_speed"])
        self.aoe = config["queen_aoe"]
        self.range = config["queen_range"]
        self.attack_direction = "up"
        self.eagle_range = config["eagle_range"]
        self.eagle_aoe = config["eagle_aoe"]

    def sword_attack(self, townHall, huts, cannons, walls, wizard_towers, is_townhall):
        if self.attack_direction == "up":
            self.target_x = max(0,self.x - self.range)
            self.target_y = self.y
        elif self.attack_direction == "down":
            self.target_x = min(0,self.x + self.range)
            self.target_y = self.y
        elif self.attack_direction == "left":
            self.target_x = self.x
            self.target_y = max(0,self.y - self.range)
        elif self.attack_direction == "right":
            self.target_x = self.x
            self.target_y = min(0,self.y + self.range)
        for building in walls + huts:
            in_range = 0
            if misc.distance(self.target_x, self.target_y, building.x1, building.y1) <= self.aoe:
                in_range = 1
            if in_range == 1:
                if building.hp > 0:
                    building.hp -= self.damage
        for building in cannons + wizard_towers:
            in_range = 0
            for x in range(townHall.x1, townHall.x2):
                for y in range(townHall.y1, townHall.y2):
                    if misc.distance(self.target_x, self.target_y, x, y) <= self.aoe:
                        in_range = 1
            if in_range == 1:
                if building.hp > 0:
                    building.hp -= self.damage
        if is_townhall == 1:
            in_range = 0
            for x in range(townHall.x1, townHall.x2):
                for y in range(townHall.y1, townHall.y2):
                    if misc.distance(self.target_x, self.target_y, x, y) <= self.aoe:
                        in_range = 1
            if in_range == 1:
                if townHall.hp > 0:
                    townHall.hp -= self.damage
                            
    def axe_attack(self, townHall, huts, cannons, walls, wizard_towers, is_townhall):
        if self.attack_direction == "up":
            self.target_x = max(0,self.x - self.eagle_range)
            self.target_y = self.y
        elif self.attack_direction == "down":
            self.target_x = min(0,self.x + self.eagle_range)
            self.target_y = self.y
        elif self.attack_direction == "left":
            self.target_x = self.x
            self.target_y = max(0,self.y - self.eagle_range)
        elif self.attack_direction == "right":
            self.target_x = self.x
            self.target_y = min(0,self.y + self.eagle_range)
        for building in walls + huts:
            in_range = 0
            if misc.distance(self.target_x, self.target_y, building.x1, building.y1) <= self.eagle_aoe:
                in_range = 1
            if in_range == 1:
                if building.hp > 0:
                    building.hp -= self.damage
        for building in cannons + wizard_towers:
            in_range = 0
            for x in range(townHall.x1, townHall.x2):
                for y in range(townHall.y1, townHall.y2):
                    if misc.distance(self.target_x, self.target_y, x, y) <= self.eagle_aoe:
                        in_range = 1
            if in_range == 1:
                if building.hp > 0:
                    building.hp -= self.damage
        if is_townhall == 1:
            in_range = 0
            for x in range(townHall.x1, townHall.x2):
                for y in range(townHall.y1, townHall.y2):
                    if misc.distance(self.target_x, self.target_y, x, y) <= self.eagle_aoe:
                        in_range = 1
            if in_range == 1:
                if townHall.hp > 0:
                    townHall.hp -= self.damage
                    
class Barbarian(Unit):
    
    def __init__(self, x, y):
        super().__init__(x, y, config["barb_hp"], config["barb_damage"], config["barb_speed"])

# For archer, check if she's in firing range, if yes, attack. Else, use same alg as barb to find a spot to fire from

class Archer(Unit):

    def __init__(self, x, y):

        super().__init__(x, y, config["barb_hp"]/2, config["barb_damage"]/2, config["barb_speed"])
        self.range = config["arch_range"]

    def to_travel_x(self, game_map, nearest_target, walls):

        travel_distance = 9999
        # if nearest target is not none
        if nearest_target != None:
            # find coordinates to hit, then find a point within arch_range of those coordinates to go to (nearest to archer)
            for x in range(nearest_target.x1-1, nearest_target.x2+1):
                for y in range(nearest_target.y1-1, nearest_target.y2+1):
                    if misc.distance(self.x, self.y, x, y) < travel_distance:
                        travel_distance = misc.distance(self.x, self.y, x, y)
                        to_hit_x = x
                        to_hit_y = y
            travel_distance = 9999
            for x in range(39):
                for y in range(39):
                    if misc.distance(to_hit_x, to_hit_y, x, y) <= self.range:
                        if misc.distance(self.x, self.y, x, y) < travel_distance:
                            travel_distance = misc.distance(self.x, self.y, x, y)
                            req_x = x
                            req_y = y
            return req_x

    def to_travel_y(self, game_map, nearest_target, walls):

        travel_distance = 9999
        if nearest_target != None:
            for x in range(nearest_target.x1-1, nearest_target.x2+1):
                for y in range(nearest_target.y1-1, nearest_target.y2+1):
                    if misc.distance(self.x, self.y, x, y) < travel_distance:
                        travel_distance = misc.distance(self.x, self.y, x, y)
                        to_hit_x = x
                        to_hit_y = y
            travel_distance = 9999
            for x in range(39):
                for y in range(39):
                    if misc.distance(to_hit_x, to_hit_y, x, y) <= self.range:
                        if misc.distance(self.x, self.y, x, y) < travel_distance:
                            travel_distance = misc.distance(self.x, self.y, x, y)
                            req_x = x
                            req_y = y
            return req_y

class Balloon(Unit):

    def __init__(self, x, y):

        super().__init__(x, y, config["barb_hp"], config["barb_damage"]*2, config["barb_speed"]*2)

    def move(self, x, y, walls):
            
        if x != None and y != None:
            if self.x != x:
                if self.x < x:
                    if self.x < x-1:
                        self.x += self.speed
                    else:
                        self.x += 1
                elif self.x > x:
                    if self.x > x+1:
                        self.x -= self.speed
                    else:
                        self.x -= 1
            if self.y != y:
                if self.y < y:
                    if self.y < y-1:
                        self.y += self.speed
                    else:
                        self.y += 1
                elif self.y > y:
                    if self.y > y+1:
                        self.y -= self.speed
                    else:
                        self.y -= 1
