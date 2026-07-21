import random
from classes import Entity
from print_style import slow_print, slow_input


def key_base_init(e):
    return e.base_initiative


class Fight:
    def __init__(self, player_group, enemy_group):
        self.player_group: list = player_group
        self.enemy_group: list = enemy_group
        self.turn_order: list[Entity] = []
        self.rounds: int = 1
        self.initiative_list()

    def __repr__(self) -> str:
        return f"\n| Player Group : {self.player_group} \n| Enemy Group : {self.enemy_group} \n| Turn Order : {self.turn_order} \n| Rounds : {self.rounds}"

    def initiative_list(self) -> dict:
        init_list = self.player_group + self.enemy_group
        random.shuffle(init_list)
        self.turn_order = sorted(init_list, key=key_base_init, reverse=True)

    def health_check(self, entity_group) -> bool:
        return any(entity.current_health > 0 for entity in entity_group)

    def target_choice(self, entity_group) -> Entity:

        target_group = []
        for e in entity_group:
            if e.current_health > 0:
                target_group.append(e)
        for i, e in enumerate(target_group, start=1):
            slow_print(f"-- Available Targets--\n{i} - {e.name}")

        target_number = int(slow_input("Choose a Target\n"))
        target = target_group[target_number - 1]
        return target

    def dmg_calculation(self, min_damage, max_damage) -> int:
        return random.randint(min_damage, max_damage)

    def fight_loop(self):

        player_names = ",".join(e.name for e in self.player_group)
        enemy_names = ",".join(e.name for e in self.enemy_group)
        slow_print(f"Fight between {player_names} and {enemy_names} !")

        while self.health_check(self.player_group) and self.health_check(
            self.enemy_group
        ):

            slow_print(f"\n------ Runde: {self.rounds} ------")

            for entity in self.turn_order:
                if entity.current_health <= 0:
                    continue
                if entity in self.player_group:
                    target_group = self.enemy_group
                else:
                    target_group = self.player_group

                slow_print(f"{entity.name}s turn: ")

                target = self.target_choice(target_group)
                damage = self.dmg_calculation(
                    entity.unarmed_min_damage, entity.unarmed_max_damage
                )
                target.current_health -= damage

                slow_print(f"{entity.name} attacks {target.name} for {damage} !")

            slow_print("Current Health:")

            for e in self.turn_order:
                slow_print(f"\nName:{e.name} HP:{e.current_health}")

            self.rounds += 1


def test_fight(character_classes, enemies):

    player_group = []
    enemy_group = []

    player_group.append(character_classes[0])

    enemy_group.append(enemies[0])

    return player_group, enemy_group
