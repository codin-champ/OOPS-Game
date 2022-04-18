def heal(unit):
    unit.hp = min(unit.max_hp, unit.hp * 1.5)

def rage(unit):
    unit.damage = unit.damage * 2
    if unit.speed == 1:
        unit.speed = unit.speed * 2

# def unrage(unit):
#     if unit.speed == 2:
#         unit.speed = unit.speed / 2