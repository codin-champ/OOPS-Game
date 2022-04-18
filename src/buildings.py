import src.misc as misc

config = misc.get_config()
# king = main.king

# note: can use something like main.map[self.x][self.y] for the colours

class Building:

    def __init__(self, x1, y1, x2, y2, max_hp):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.max_hp = max_hp
        self.hp = max_hp

class Cannon(Building):
    
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2, config["cannon_hp"])
        self.damage = config["cannon_damage"]
        self.range = config["cannon_range"]

    def nearest_troop(self, king, barbarians, archers):
        nearest_troop = None
        nearest_troop_distance = 99999
        for barbarian in barbarians:
            distance = misc.distance((self.x1 + self.x2)/2, (self.y1 + self.y2)/2, barbarian.x, barbarian.y)
            if distance < nearest_troop_distance:
                nearest_troop = barbarian
                nearest_troop_distance = distance
        for archer in archers:
            distance = misc.distance((self.x1 + self.x2)/2, (self.y1 + self.y2)/2, archer.x, archer.y)
            if distance < nearest_troop_distance:
                nearest_troop = archer
                nearest_troop_distance = distance
        king_distance = misc.distance((self.x1 + self.x2)/2, (self.y1 + self.y2)/2, king.x, king.y)
        if king_distance < nearest_troop_distance:
            nearest_troop = king
            nearest_troop_distance = king_distance
        if self.range >= nearest_troop_distance:
            return nearest_troop
        else:
            return None

    def shoot(self, nearest_troop):
        if nearest_troop != None:
            if nearest_troop.hp > 0:
                nearest_troop.hp -= self.damage

class Wall(Building):
    
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2, config["wall_hp"])

class Hut(Building):
    
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2, config["hut_hp"])

class TownHall(Building):
    
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2, config["th_hp"])

class Wizard_Tower(Building): # identical to cannon

    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2, config["cannon_hp"])
        self.damage = config["cannon_damage"]
        self.range = config["cannon_range"]

    def nearest_troop(self, king, barbarians, archers, balloons):

        nearest_troop = None
        nearest_troop_distance = 99999
        for barbarian in barbarians:
            distance = misc.distance((self.x1 + self.x2)/2, (self.y1 + self.y2)/2, barbarian.x, barbarian.y)
            if distance < nearest_troop_distance:
                nearest_troop = barbarian
                nearest_troop_distance = distance
        for archer in archers:
            distance = misc.distance((self.x1 + self.x2)/2, (self.y1 + self.y2)/2, archer.x, archer.y)
            if distance < nearest_troop_distance:
                nearest_troop = archer
                nearest_troop_distance = distance
        king_distance = misc.distance((self.x1 + self.x2)/2, (self.y1 + self.y2)/2, king.x, king.y)
        if king_distance < nearest_troop_distance:
            nearest_troop = king
            nearest_troop_distance = king_distance
        for balloon in balloons:
            distance = misc.distance((self.x1 + self.x2)/2, (self.y1 + self.y2)/2, balloon.x, balloon.y)
            if distance < nearest_troop_distance:
                nearest_troop = balloon
                nearest_troop_distance = distance
        if self.range >= nearest_troop_distance:
            return nearest_troop
        else:
            return None

    def shoot(self, nearest_troop, barbarians, archers, balloons, king):
        if nearest_troop != None:
            if nearest_troop.hp > 0:
                for unit in barbarians + archers + balloons:
                    distance = misc.distance(unit.x, unit.y, nearest_troop.x, nearest_troop.y)
                    if distance <= 3:
                        unit.hp -= self.damage
                if misc.distance(king.x, king.y, nearest_troop.x, nearest_troop.y) <= 3:
                    king.hp -= self.damage