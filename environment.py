from print_style import slow_print, slow_input
from fight import Fight, FightResult, roll_chance
from loader import random_enemy_select, build_enemies
from enum import Enum
from display import show_status

ENCOUNTER_CHANCE = 30
MENU_OPTIONS = ["Move on", "Look around", "Wait", "Status", "Rest"]
REST_HEALTH_FACTOR = 0.40
REST_MANA_FACTOR = 0.30


class ExploreResult(Enum):
    GAME_OVER = "game_over"
    LEFT = "left"


class Environment:
    def __init__(self, rooms, player_group, enemies_data):
        self.rooms: dict = rooms
        self.player_group: list = player_group
        self.enemies_data: list = enemies_data
        self.current_room: str = "room_1"
        self.encounter_rooms: set = set()
        self.roll_encounter_rooms()

    def room_description(self):
        room = self.rooms[self.current_room]
        slow_print(f"{room["description"]}")

    def room_directions(self):
        room = self.rooms[self.current_room]
        for index, direction in enumerate(room["exit"], start=1):
            slow_print(f"{index} - {direction}")
        slow_print("0 - Cancel")

    def room_movement(self):
        while True:
            room = self.rooms[self.current_room]
            self.room_directions()

            directions = list(room["exit"])

            try:
                number = int(slow_input("Choose\n"))
            except ValueError:
                slow_print("Not a number")
                continue

            if number == 0:
                return None
            if 1 <= number <= len(directions):
                room_choice = directions[number - 1]
                room_target = room["exit"][room_choice]

                if room_target == "exit_environment":
                    return ExploreResult.LEFT
                self.current_room = room_target
                return self.enter_room()

            else:
                slow_print("Wrong number")

    def waiting(self) -> FightResult | None:
        if roll_chance(ENCOUNTER_CHANCE):
            return self.start_encounter()
        slow_print("Some time has passed")
        return None

    def look(self):
        room = self.rooms[self.current_room]
        slow_print(f"You are investigating the {room['name']}")
        slow_print(room["details"])
        directions = ", ".join(room["exit"])
        slow_print(f"Paths lead: {directions}")

    def rest(self):
        for player in self.player_group:
            player.current_health = min(
                player.base_health,
                player.current_health + int(player.base_health * REST_HEALTH_FACTOR),
            )
            if player.resource_type == "mana":
                player.current_resource = min(
                    player.max_resource,
                    player.current_resource
                    + int(player.max_resource * REST_MANA_FACTOR),
                )
        slow_print("You find a spot to rest for a bit.\nYou feel rested.")

    def exploring_menu(self):
        self.room_description()
        while True:
            for index, option in enumerate(MENU_OPTIONS, start=1):
                slow_print(f"{index} - {option}")
            try:
                menu_option = int(slow_input("\nWhat do you want to do?\n"))
            except ValueError:
                slow_print(f"Choose an option between 1 and {len(MENU_OPTIONS)}\n")
                continue
            if menu_option == 1:
                result = self.room_movement()
                if result == ExploreResult.LEFT:
                    return ExploreResult.LEFT
                elif result == FightResult.DEFEAT:
                    return ExploreResult.GAME_OVER
                elif result == FightResult.RUN:
                    slow_print("You got away!")
            elif menu_option == 2:
                self.look()
            elif menu_option == 3:
                result = self.waiting()
                if result == FightResult.DEFEAT:
                    return ExploreResult.GAME_OVER
                if result == FightResult.RUN:
                    slow_print("You got away!")
            elif menu_option == 4:
                show_status(self.player_group, "Party")
            elif menu_option == 5:
                self.rest()
            else:
                slow_print("Wrong number")

    def start_encounter(self):
        select_enemy = random_enemy_select(self.enemies_data)
        enemy_group = build_enemies(select_enemy)
        fight_start = Fight(self.player_group, enemy_group)
        return fight_start.fight_loop()

    def roll_encounter_rooms(self):
        for room_key, room_data in self.rooms.items():
            chance = room_data.get("encounter_chance", 0)
            if roll_chance(chance):
                self.encounter_rooms.add(room_key)

    def enter_room(self) -> FightResult | None:
        self.room_description()
        if self.current_room in self.encounter_rooms:
            result = self.start_encounter()
            self.encounter_rooms.discard(self.current_room)
            return result
        return None
