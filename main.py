from database import disconnect, verbinden
from loader import load_all, random_enemy_select, build_enemies
from fight import Fight, build_player_group

connection = verbinden()

every_data = load_all(connection)


disconnect(connection)

player_group = build_player_group(every_data["classes"])
select_enemy = random_enemy_select(every_data["enemies_data"])
enemy_group = build_enemies(select_enemy)

fight_start = Fight(player_group, enemy_group)

fight_start.fight_loop()
# print(Fight(player_data, enemy_data))
# print(every_data)
