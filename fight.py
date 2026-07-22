import random
from classes import Entity
from print_style import slow_print, slow_input


def key_base_init(entity):
    return entity.base_initiative


class Fight:
    def __init__(self, player_group, enemy_group):
        self.player_group: list = player_group
        self.enemy_group: list = enemy_group
        self.turn_order: list[Entity] = []
        self.rounds: int = 1
        self.initiative_list()

    def __repr__(self) -> str:
        return f"\n| Player Group : {self.player_group} \n| Enemy Group : {self.enemy_group} \n| Turn Order : {self.turn_order} \n| Rounds : {self.rounds}"

    def initiative_list(self) -> None:
        init_list = self.player_group + self.enemy_group
        random.shuffle(init_list)
        self.turn_order = sorted(init_list, key=key_base_init, reverse=True)

    def health_check(self, entity_group) -> bool:
        return any(entity.current_health > 0 for entity in entity_group)

    def player_choice(self, entity_group) -> Entity:

        target_group = []
        for entity in entity_group:
            if entity.current_health > 0:
                target_group.append(entity)

        while True:
            slow_print("-- Available Targets--")
            for index, entity in enumerate(target_group, start=1):
                slow_print(f"{index} - {entity.name}")

            try:
                target_number = int(slow_input("Choose a Target\n"))
            except ValueError:
                slow_print(
                    f"Your input was not a number, please choose a number between 1 and {len(target_group)}"
                )
                continue

            if target_number >= 1 and target_number <= len(target_group):
                target = target_group[target_number - 1]
                return target
            else:
                slow_print(
                    f"Your input was a wrong number, please choose a number between 1 and {len(target_group)}"
                )

    def enemy_choice(self, entity_group) -> Entity:

        target_group = []
        for entity in entity_group:
            if entity.current_health > 0:
                target_group.append(entity)
        attack_target = random.choice(target_group)
        return attack_target

    def dmg_calculation(self, min_damage, max_damage) -> int:
        return random.randint(min_damage, max_damage)

    def fight_loop(self) -> None:

        player_names = ",".join(entity.name for entity in self.player_group)
        enemy_names = ",".join(entity.name for entity in self.enemy_group)
        slow_print(f"Fight between {player_names} and {enemy_names} !")

        while self.health_check(self.player_group) and self.health_check(
            self.enemy_group
        ):

            slow_print(f"\n------ Round: {self.rounds} ------")

            for entity in self.turn_order:
                if entity.current_health <= 0:
                    continue
                slow_print(f"{entity.name}s turn: ")
                if entity in self.player_group:
                    target_group = self.enemy_group
                    target = self.player_choice(target_group)
                else:
                    target_group = self.player_group
                    target = self.enemy_choice(target_group)

                damage = self.dmg_calculation(
                    entity.unarmed_min_damage, entity.unarmed_max_damage
                )
                target.current_health -= damage
                slow_print(f"{entity.name} attacks {target.name} for {damage} !")
                if target.current_health <= 0:
                    slow_print(f"{target.name} died")

                if not (
                    self.health_check(self.player_group)
                    and self.health_check(self.enemy_group)
                ):
                    break

            slow_print("Current Health:")

            for entity in self.turn_order:
                slow_print(f"\nName:{entity.name} HP:{entity.current_health}")

            self.rounds += 1


def test_fight(character_classes, enemies):

    player_group = []
    enemy_group = []

    player_group.append(character_classes[0])
    player_group.append(character_classes[1])

    enemy_group.append(enemies[0])
    enemy_group.append(enemies[1])
    """ enemy_group.append(enemies[1]) """

    return player_group, enemy_group
