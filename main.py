from database import get_data, disconnect, verbinden
from loader import (
    build_classes,
    build_enemies,
    build_items,
    build_weapons,
    build_armor,
    build_effects,
    build_skills,
    build_spells,
)

connection = verbinden()

classes_data = get_data(connection, "classes")
enemies_data = get_data(connection, "enemies")
items_data = get_data(connection, "items")
weapons_data = get_data(connection, "weapons")
armor_data = get_data(connection, "armor")
effects_data = get_data(connection, "effects")
skills_data = get_data(connection, "skills")
spells_data = get_data(connection, "spells")


disconnect(connection)

character_classes = build_classes(classes_data)
enemies = build_enemies(enemies_data)
items = build_items(items_data)
weapons = build_weapons(weapons_data)
armor = build_armor(armor_data)
effects = build_effects(effects_data)
skills = build_skills(skills_data)
spells = build_spells(spells_data)

print(character_classes)
print(enemies)
print(items)
print(weapons)
print(armor)
print(effects)
print(skills)
print(spells)
