from database import disconnect, verbinden
from loader import load_all
from fight import Fight, test_fight

connection = verbinden()

every_data = load_all(connection)


disconnect(connection)

player_data, enemy_data = test_fight(every_data["classes"], every_data["enemies"])


fight_start = Fight(player_data, enemy_data)


fight_start.fight_loop()
# print(Fight(player_data, enemy_data))
# print(every_data)
