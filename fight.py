import random
from classes import Entity


class Fight:
    def __init__(self, player_group, enemy_group):
        self.player_group: list = player_group
        self.enemy_group: list = enemy_group
        self.turn_order: list[Entity] = []
        self.rounds: int = 1

    def __repr__(self) -> str:
        return f"Player Group : {self.player_group} | Enemy Group : {self.enemy_group} | Initiative : {self.initiative} | Rounds : {self.rounds}"

    def initiative_list(self):
        init_list = self.player_group + self.enemy_group
        init_list["self.base_initiative"].sort(reverse=True)
        return init_list


def test_fight(character_classes, enemies):

    player_group = []
    enemy_group = []

    player_group.append(character_classes[0])

    enemy_group.append(enemies[0])

    return player_group, enemy_group
