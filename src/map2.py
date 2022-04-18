import os
from src.buildings import Cannon, Hut, Wall, TownHall, Wizard_Tower
from src.units import Barbarian, King, Archer, Balloon, Queen
import numpy
from click import getchar
from datetime import datetime

grass_id = "\033[38;2;255;218;0;48;2;0;209;0m   \033[0m"
king_id = "\033[38;2;255;255;255;48;2;255;0;0m   \033[0m"
barb_high_id = "\033[38;2;255;218;0;48;2;0;0;0m   \033[0m"
barb_mid_id = "\033[38;2;255;218;0;48;2;100;100;100m   \033[0m"
barb_low_id = "\033[38;2;255;218;0;48;2;200;200;200m   \033[0m"
arch_high_id = "\033[38;2;255;218;0;48;2;255;0;255m   \033[0m"
arch_mid_id = "\033[38;2;255;218;0;48;2;255;100;255m   \033[0m"
arch_low_id = "\033[38;2;255;218;0;48;2;255;200;255m   \033[0m"
loon_high_id = "\033[38;2;255;218;0;48;2;0;0;255m   \033[0m"
loon_mid_id = "\033[38;2;255;218;0;48;2;100;50;255m   \033[0m"
loon_low_id = "\033[38;2;255;218;0;48;2;200;100;255m   \033[0m"
wall_high_id = "\033[38;2;255;218;0;48;2;207;93;0m   \033[0m"
wall_mid_id = "\033[38;2;255;218;0;48;2;128;64;0m   \033[0m"
wall_low_id = "\033[38;2;255;218;0;48;2;64;32;0m   \033[0m"
hut_high_id = "\033[38;2;255;218;0;48;2;128;128;248m   \033[0m"
hut_mid_id = "\033[38;2;255;218;0;48;2;64;64;124m   \033[0m"
hut_low_id = "\033[38;2;255;218;0;48;2;32;32;64m   \033[0m"
cannon_high_id = "\033[38;2;255;218;0;48;2;125;125;125m   \033[0m"
cannon_mid_id = "\033[38;2;255;218;0;48;2;60;60;60m   \033[0m"
cannon_low_id = "\033[38;2;255;218;0;48;2;0;0;0m   \033[0m"
wiz_high_id = "\033[38;2;255;218;0;48;2;153;0;255m   \033[0m"
wiz_mid_id = "\033[38;2;255;218;0;48;2;84;0;173m   \033[0m"
wiz_low_id = "\033[38;2;255;218;0;48;2;55;0;115m   \033[0m"
townhall_high_id = "\033[38;2;255;218;0;48;2;91;236;255m   \033[0m"
townhall_mid_id = "\033[38;2;255;218;0;48;2;45;118;140m   \033[0m"
townhall_low_id = "\033[38;2;255;218;0;48;2;20;60;80m   \033[0m"

class Map():

    def __init__(self):

        self.map = numpy.zeros((40, 40), dtype="<U100")
        # initialise each character to blank
        for x in range (0,40):
            for y in range (0,40):
                self.map[x][y] = grass_id
        self.Walls = []
        self.Cannons = []
        self.Huts = []
        self.Barbarians = []
        self.Archers = []
        self.Balloons = []
        self.townHall = TownHall(18, 18, 21, 21)
        self.wizardTowers = []
        self.is_townhall = True

    def summonKing(self):
        self.King = King(38, 22)

    def summonQueen(self):
        self.King = Queen(38, 22)

    def newMap(self, char):

        for y in range (3,37):
            self.Walls.append(Wall(3,y,3,y))
            self.Walls.append(Wall(36,y,36,y))
        for x in range (4,36):
            self.Walls.append(Wall(x,3,x,3))
            self.Walls.append(Wall(x,36,x,36))
        self.Cannons.append(Cannon(6, 6, 8, 8))
        self.Cannons.append(Cannon(31,31,33,33))
        self.wizardTowers.append(Wizard_Tower(14, 23, 16, 25))
        self.wizardTowers.append(Wizard_Tower(23, 17, 25, 19))
        self.Huts.append(Hut(7, 20, 7, 20))
        self.Huts.append(Hut(32, 20, 32, 20))
        self.Huts.append(Hut(15, 32, 15, 32))
        self.Huts.append(Hut(20, 32, 20, 32))
        self.Huts.append(Hut(25, 32, 25, 32))

        if char == "2":
            self.Cannons.append(Cannon(31,6,33,8))
            self.wizardTowers.append(Wizard_Tower(23,23,25,25))
        elif char == "3":
            self.Cannons.append(Cannon(31,6,33,8))
            self.wizardTowers.append(Wizard_Tower(23,23,25,25))
            self.Cannons.append(Cannon(6,31,8,33))
            self.wizardTowers.append(Wizard_Tower(14,14,16,16))

    def summonTroop(self, char):

        if char == "c":
            self.Barbarians.append(Barbarian(38,8))
        elif char == "v":
            self.Barbarians.append(Barbarian(38,18))
        elif char == "b":
            self.Barbarians.append(Barbarian(38,31))
        elif char == "f":
            self.Archers.append(Archer(38,8))
        elif char == "g":
            self.Archers.append(Archer(38,18))
        elif char == "h":
            self.Archers.append(Archer(38,31))
        elif char == "t":
            self.Balloons.append(Balloon(38,8))
        elif char == "y":
            self.Balloons.append(Balloon(38,18))
        elif char == "u":
            self.Balloons.append(Balloon(38,31))

    def level2(self):

        self.Cannons.append(Cannon(31,6,33,8))
        self.wizardTowers.append(Wizard_Tower(23,23,25,25))

    def level3(self):

        self.Cannons.append(Cannon(31,6,33,8))
        self.wizardTowers.append(Wizard_Tower(23,23,25,25))
        self.Cannons.append(Cannon(6,31,8,33))
        self.wizardTowers.append(Wizard_Tower(14,14,16,16))

    def updateMap(self):
        for x in range (0,40):
            for y in range (0,40):
                self.map[x][y] = grass_id
        for wall in self.Walls:
            if wall.hp >= 0.66*(wall.max_hp):
                self.map[wall.x1][wall.y1] = wall_high_id
            elif wall.hp >= 0.33*(wall.max_hp):
                self.map[wall.x1][wall.y1] = wall_mid_id
            elif wall.hp > 0:
                self.map[wall.x1][wall.y1] = wall_low_id
            else:
                self.map[wall.x1][wall.y1] = grass_id
                self.Walls.remove(wall)
        for hut in self.Huts:
            if hut.hp >= 0.66*(hut.max_hp):
                self.map[hut.x1][hut.y1] = hut_high_id
            elif hut.hp >= 0.33*(hut.max_hp):
                self.map[hut.x1][hut.y1] = hut_mid_id
            elif hut.hp > 0:
                self.map[hut.x1][hut.y1] = hut_low_id
            else:
                self.map[hut.x1][hut.y1] = grass_id
                self.Huts.remove(hut)
        for cannon in self.Cannons:
            if cannon.hp >= 0.66*(cannon.max_hp):
                for x in range (cannon.x1, cannon.x2+1):
                    for y in range (cannon.y1, cannon.y2+1):
                        self.map[x][y] = cannon_high_id
            elif cannon.hp >= 0.33*(cannon.max_hp):
                for x in range (cannon.x1, cannon.x2+1):
                    for y in range (cannon.y1, cannon.y2+1):
                        self.map[x][y] = cannon_mid_id
            elif cannon.hp > 0:
                for x in range (cannon.x1, cannon.x2+1):
                    for y in range (cannon.y1, cannon.y2+1):
                        self.map[x][y] = cannon_low_id
            else:
                for x in range (cannon.x1, cannon.x2+1):
                    for y in range (cannon.y1, cannon.y2+1):
                        self.map[x][y] = grass_id
                self.Cannons.remove(cannon)
        for tower in self.wizardTowers:
            if tower.hp >= 0.66*(tower.max_hp):
                for x in range (tower.x1, tower.x2+1):
                    for y in range (tower.y1, tower.y2+1):
                        self.map[x][y] = wiz_high_id
            elif tower.hp >= 0.33*(tower.max_hp):
                for x in range (tower.x1, tower.x2+1):
                    for y in range (tower.y1, tower.y2+1):
                        self.map[x][y] = wiz_mid_id
            elif tower.hp > 0:
                for x in range (tower.x1, tower.x2+1):
                    for y in range (tower.y1, tower.y2+1):
                        self.map[x][y] = wiz_low_id
            else:
                for x in range (tower.x1, tower.x2+1):
                    for y in range (tower.y1, tower.y2+1):
                        self.map[x][y] = grass_id
                self.wizardTowers.remove(tower)
        if self.is_townhall:
            if self.townHall.hp >= 0.66*(self.townHall.max_hp):
                for x in range (self.townHall.x1, self.townHall.x2+1):
                    for y in range (self.townHall.y1, self.townHall.y2+1):
                        self.map[x][y] = townhall_high_id
            elif self.townHall.hp >= 0.33*(self.townHall.max_hp):
                for x in range (self.townHall.x1, self.townHall.x2+1):
                    for y in range (self.townHall.y1, self.townHall.y2+1):
                        self.map[x][y] = townhall_mid_id
            elif self.townHall.hp > 0:
                for x in range (self.townHall.x1, self.townHall.x2+1):
                    for y in range (self.townHall.y1, self.townHall.y2+1):
                        self.map[x][y] = townhall_low_id
            else:
                for x in range (self.townHall.x1, self.townHall.x2+1):
                    for y in range (self.townHall.y1, self.townHall.y2+1):
                        self.map[x][y] = grass_id
                self.townHall = None
                self.is_townhall = False
        for barb in self.Barbarians:
            if barb.hp >= 0.66*(barb.max_hp):
                self.map[barb.x][barb.y] = barb_high_id
            elif barb.hp >= 0.33*(barb.max_hp):
                self.map[barb.x][barb.y] = barb_mid_id
            elif barb.hp > 0:
                self.map[barb.x][barb.y] = barb_low_id
            else:
                self.map[barb.x][barb.y] = grass_id
                self.Barbarians.remove(barb)
        for arch in self.Archers:
            if arch.hp >= 0.66*(arch.max_hp):
                self.map[arch.x][arch.y] = arch_high_id
            elif arch.hp >= 0.33*(arch.max_hp):
                self.map[arch.x][arch.y] = arch_mid_id
            elif arch.hp > 0:
                self.map[arch.x][arch.y] = arch_low_id
            else:
                self.map[arch.x][arch.y] = grass_id
                self.Archers.remove(arch)
        for loon in self.Balloons:
            if loon.hp >= 0.66*(loon.max_hp):
                self.map[loon.x][loon.y] = loon_high_id
            elif loon.hp >= 0.33*(loon.max_hp):
                self.map[loon.x][loon.y] = loon_mid_id
            elif loon.hp > 0:
                self.map[loon.x][loon.y] = loon_low_id
            else:
                self.map[loon.x][loon.y] = grass_id
                self.Balloons.remove(loon)
        self.map[self.King.x][self.King.y] = king_id

    def printMap(self):
        # clear the current screen
        os.system('clear')
        # print the map
        for x in range (0,40):
            for y in range (0,40):
                print(self.map[x][y], end="")
            print("")
        # print a health bar for the king
        print("Hero's health: ", end="")
        health = (self.King.hp/self.King.max_hp)*20
        health = int(health)
        print("#"*health, end="\n")

# example_map = Map()
# example_map.newMap()
# example_map.updateMap()
# example_map.printMap()