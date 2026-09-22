from database import disconnect, verbinden
from loader import load_all, choose_player_class
from fight import Fight
from environment import Environment
from room_data import forest

connection = verbinden()

every_data = load_all(connection)


disconnect(connection)

player_group = choose_player_class(every_data["classes"])
environment = Environment(forest, player_group, every_data["enemies_data"])
environment.exploring_menu()
