from print_style import slow_print, slow_input
from fight import Fight, roll_chance
from loader import random_enemy_select, build_enemies

ENCOUNTER_CHANCE = 30
MENU_OPTIONS = ["Move on", "Look around", "Wait"]


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

    def waiting(self):
        if roll_chance(ENCOUNTER_CHANCE):
            select_enemy = random_enemy_select(self.enemies_data)
            enemy_group = build_enemies(select_enemy)
            fight_start = Fight(self.player_group, enemy_group)
            fight_start.fight_loop()
        else:
            slow_print("Some time has passed")

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
                    break
            elif menu_option == 2:
                self.look()
            elif menu_option == 3:
                self.waiting()
            else:
                slow_print(f"Choose a number between 1 and {len(MENU_OPTIONS)}")
