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
        return f"Player Group : {self.player_group} | Enemy Group : {self.enemy_group} | Turn Order : {self.turn_order} | Rounds : {self.rounds}"

    def initiative_list(self):
        init_list = self.player_group + self.enemy_group
        random.shuffle(init_list)
        self.turn_order = sorted(init_list, key=key_base_init, reverse=True)


def test_fight(character_classes, enemies):

    player_group = []
    enemy_group = []

    player_group.append(character_classes[0])

    enemy_group.append(enemies[0])

    return player_group, enemy_group
