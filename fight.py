import random
from classes import Entity


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

    def fight_loop(self):
        while self.health_check(self.player_group) and self.health_check(
            self.enemy_group
        ):
            for entity in self.turn_order:
                if entity.current_health <= 0:
                    continue
                if entity in self.player_group:
                    target_group = self.enemy_group
                else:
                    target_group = self.player_group
                print(target_group)
            self.rounds += 1


def test_fight(character_classes, enemies):

    player_group = []
    enemy_group = []

    player_group.append(character_classes[0])

    enemy_group.append(enemies[0])

    return player_group, enemy_group
