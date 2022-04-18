import os
from src.map2 import Map
import regex
from src.spells import heal, rage
from click import getchar
import time
from datetime import datetime
from src.units import Barbarian, King

map = Map()
os.system('clear')
print("Do you want to play level 1, 2 or 3?")
level = getchar()
map.newMap(level)

list_of_inputs = []
endgame = 1
barbcount = 0
archcount = 0
looncount = 0
is_raged = 0

print("Do you want to play with King(k), Queen(q) or neither(n)?")
hero = getchar()

if hero == "k":
    map.summonKing()
elif hero == "q":
    map.summonQueen()

with open("replays/replay.txt", "r") as f:
    file_to_read = f.read()
# remove \n's from file_to_read
file_to_read = regex.sub(r'\n', '', file_to_read)
with open ("replays/" + file_to_read, "r") as f:
    while endgame:
        c = f.read(1)
        if c != None:
            list_of_inputs.append(c)
        for cannon in map.Cannons:
            cannon.shoot(cannon.nearest_troop(map.King, map.Barbarians, map.Archers))
        for tower in map.wizardTowers:
            target = tower.nearest_troop(map.King, map.Barbarians, map.Archers, map.Balloons)
            tower.shoot(target, map.Barbarians, map.Archers, map.Balloons, map.King)
        for barbarian in map.Barbarians:
            nearest_target = barbarian.find_nearest_target(map, map.townHall, map.Huts, map.Cannons, map.Walls, map.wizardTowers, map.is_townhall)
            to_travel_x = barbarian.to_travel_x(map, nearest_target, map.Walls)
            to_travel_y = barbarian.to_travel_y(map, nearest_target, map.Walls)
            if barbarian.x == to_travel_x and barbarian.y == to_travel_y:
                barbarian.attack(nearest_target)
            else:
                barbarian.move(to_travel_x, to_travel_y, map.Walls)
        for archer in map.Archers:
            nearest_target = archer.find_nearest_target(map, map.townHall, map.Huts, map.Cannons, map.Walls, map.wizardTowers, map.is_townhall)
            to_travel_x = archer.to_travel_x(map, nearest_target, map.Walls)
            to_travel_y = archer.to_travel_y(map, nearest_target, map.Walls)
            if archer.x == to_travel_x and archer.y == to_travel_y:
                archer.attack(nearest_target)
            else:
                archer.move(to_travel_x, to_travel_y, map.Walls)
        for balloon in map.Balloons:
            nearest_target = balloon.find_nearest_defense(map, map.townHall, map.Huts, map.Cannons, map.Walls, map.wizardTowers, map.is_townhall)
            to_travel_x = balloon.to_travel_x(map, nearest_target, map.Walls)
            to_travel_y = balloon.to_travel_y(map, nearest_target, map.Walls)
            if balloon.x == to_travel_x and balloon.y == to_travel_y:
                balloon.attack(nearest_target)
            else:
                balloon.move(to_travel_x, to_travel_y, map.Walls)
        if c == "w" or c == "a" or c == "s" or c == "d":
            map.King.hero_move(c, map)
        if c == "e":
            heal(map.King)
            for troop in map.Barbarians + map.Archers + map.Balloons:
                heal(troop)
        if c == "r":
            if is_raged == 0:
                is_raged = 1
                rage(map.King)
                for troop in map.Barbarians + map.Archers + map.Balloons:
                    rage(troop)
        if c == " ":
            map.King.sword_attack(map.townHall, map.Huts, map.Cannons, map.Walls, map.wizardTowers, map.is_townhall)
        if c =="x":
            if hero == "q":
                time.sleep(1)
            map.King.axe_attack(map.townHall, map.Huts, map.Cannons, map.Walls, map.wizardTowers, map.is_townhall)
        if c == "c" or c == "v" or c == "b":
            if barbcount < 6: 
                map.summonTroop(c)
                barbcount += 1
        if c == "f" or c == "g" or c == "h":
            if archcount < 6:
                map.summonTroop(c)
                archcount += 1
        if c == "t" or c == "y" or c == "u":
            if looncount < 3:
                map.summonTroop(c)
                looncount += 1
        if map.King.hp <= 0:
            endgame = 0
            won = 0
        # if is_townhall is false and huts, cannons, wizardtowers are empty, endgame = 1, won = 1
        if map.is_townhall == False and len(map.Huts) == 0 and len(map.Cannons) == 0 and len(map.wizardTowers) == 0:
            endgame = 1
            won = 1
        if c == "q":
            endgame = 0
            won = 0
        map.updateMap()
        if endgame == 1:
            map.printMap()
        else:
            os.system('clear')
            if won == 1:
                print("You won!")
            else:
                print("You lost!")
