from database import disconnect, verbinden
from loader import load_all, choose_player_class
from environment import Environment, ExploreResult
from room_data import forest
from print_style import slow_print

connection = verbinden()

every_data = load_all(connection)


disconnect(connection)

player_group = choose_player_class(every_data["classes"])
environment = Environment(forest, player_group, every_data["enemies_data"])
result = environment.exploring_menu()
if result == ExploreResult.GAME_OVER:
    slow_print("Game Over")
else:
    slow_print("You leave the forest")