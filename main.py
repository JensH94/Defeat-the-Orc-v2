from database import disconnect, verbinden
from loader import load_all, random_enemy_select, build_enemies, choose_player_class
from fight import Fight
from environment import Environment
from room_data import forest

connection = verbinden()

every_data = load_all(connection)


disconnect(connection)

player_group = choose_player_class(every_data["classes"])
select_enemy = random_enemy_select(every_data["enemies_data"])
enemy_group = build_enemies(select_enemy)
environment = Environment(forest, player_group, every_data["enemies_data"])
environment.room_movement()


fight_start = Fight(player_group, enemy_group)

fight_start.fight_loop()
