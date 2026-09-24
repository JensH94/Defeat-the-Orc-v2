from print_style import slow_print, slow_input
from fight import Fight, FightResult, roll_chance
from loader import random_enemy_select, build_enemies
from enum import Enum
from display import show_status

ENCOUNTER_CHANCE = 30
MENU_OPTIONS = ["Move on", "Look around", "Wait", "Status"]

class ExploreResult(Enum):
    GAME_OVER = "game_over"
    LEFT = "left"


class Environment:
    def __init__(self, rooms, player_group, enemies_data):
        self.rooms: dict = rooms
        self.player_group: list = player_group
        self.enemies_data: list = enemies_data
        self.current_room: str = "room_1"

    def room_description(self):
        room = self.rooms[self.current_room]
        slow_print(f"{room["description"]}")

    def room_directions(self):
        room = self.rooms[self.current_room]
        for index, direction in enumerate(room["exit"], start=1):
            slow_print(f"{index} - {direction}")

    def room_movement(self):
        while True:
            room = self.rooms[self.current_room]
            self.room_directions()

            directions = list(room["exit"])

            try:
                number = int(slow_input("Choose\n"))
            except ValueError:
                slow_print("Not number")
                continue

            if 1 <= number <= len(directions):
                room_choice = directions[number - 1]
                room_target = room["exit"][room_choice]

                if room_target == "exit_environment":
                    return True
                self.current_room = room_target
                self.room_description()
                return

            else:
                slow_print("Wrong number")

    def waiting(self) -> FightResult | None:
        if roll_chance(ENCOUNTER_CHANCE):
            select_enemy = random_enemy_select(self.enemies_data)
            enemy_group = build_enemies(select_enemy)
            fight_start = Fight(self.player_group, enemy_group)
            return fight_start.fight_loop()
        slow_print("Some time has passed")
        return None

    def look(self):
        room = self.rooms[self.current_room]
        slow_print(f"You are investigating the {room['name']}")
        slow_print(room["details"])
        directions = ", ".join(room["exit"])
        slow_print(f"Paths lead: {directions}")

    def exploring_menu(self):
        self.room_description()
        while True:
            for index, option in enumerate(MENU_OPTIONS, start=1):
                slow_print(f"{index} - {option}")
            try:
                menu_option = int(slow_input("\nWhat do you want to do?\n"))
            except ValueError:
                slow_print(f"Choose an option between 1 and {len(MENU_OPTIONS)}")
                continue
            if menu_option == 1:
                if self.room_movement():
                    return ExploreResult.LEFT
            elif menu_option == 2:
                self.look()
            elif menu_option == 3:
                if self.waiting() == FightResult.DEFEAT:
                    return ExploreResult.GAME_OVER
            elif menu_option == 4:
                show_status(self.player_group, "Party")
            else:
                slow_print("Wrong number")
