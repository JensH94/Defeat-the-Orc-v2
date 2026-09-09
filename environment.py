from print_style import slow_print, slow_input


class Environment:
    def __init__(self, rooms, player_group, enemies_data):
        self.rooms: dict = rooms
        self.player_group: list = player_group
        self.enemies_data: list = enemies_data
        self.current_room: str = "room_1"

    def room_show(self):
        room = self.rooms[self.current_room]
        slow_print(f"{room["description"]}")
        for index, direction in enumerate(room["exit"], start=1):
            slow_print(f"{index} - {direction}")

    def room_movement(self):
        while True:
            room = self.rooms[self.current_room]
            self.room_show()

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
                    break
                self.current_room = room_target

            else:
                slow_print("Wrong number")
