Weapons = [
    #medium
    [{"name": "Starter Sword", "damage": 15},
     {"name": "Wooden Sword", "damage": 25},
     {"name": "Iron Sword", "damage": 40}],
    #light
    [{"name": "Starter Dagger", "damage": 10},
     {"name": "Stone Dagger", "damage": 15},
     {"name": "Short Sword", "damage": 25}],
    #heavy
    [{"name": "Starter Club", "damage": 30},
     {"name": "Spiked Club", "damage": 40},
     {"name": "Iron Axe", "damage": 60}]
]

Armor = [
    {"name": "Leather Armor", "health": 10},
    {"name": "Chainmail Armor", "health": 10, "speed": 20},
    {"name": "Iron Armor", "health": 20, "speed": -20}
]

for type in Weapons:
    print(type)