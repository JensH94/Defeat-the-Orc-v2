from database import disconnect, verbinden
from loader import load_all
from fight import Fight, test_fight

connection = verbinden()

every_data = load_all(connection)

for entity in every_data["classes"]:
    print(entity.name, entity.entity_skills, entity.entity_spells)

disconnect(connection)

player_data, enemy_data = test_fight(every_data["classes"], every_data["enemies"])

bleed = next(e for e in every_data["effects"] if e.name == "Bleed")
fire = next(e for e in every_data["effects"] if e.name == "Fire")
enemy_data[0].entity_effects.append(bleed)
enemy_data[1].entity_effects.append(fire)

fight_start = Fight(player_data, enemy_data)

fight_start.fight_loop()
""" print(Fight(player_data, enemy_data)) """
""" print(every_data) """
