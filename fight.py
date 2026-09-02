import random
from classes import Entity
from print_style import slow_print, slow_input

RAGE_HIT_FACTOR = 0.2
RAGE_TICK_FACTOR = 0.1


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

    def health_check(self, entity_group):
        return any(entity.is_alive() for entity in entity_group)

    def announce_death(self, entity):
        slow_print(f"{entity.name} died")

    def choose_action(self, entity) -> str:

        choices = []
        choices.append("Attack")

        if entity.entity_skills:
            choices.append("Skills")
        if entity.entity_spells:
            choices.append("Spells")

        while True:
            for index, action in enumerate(choices, start=1):
                slow_print(f"{index} - {action}")

            try:
                choice = int(slow_input("\nChoose an action\n"))
            except ValueError:
                slow_print(f"Not a number, choose from {len(choices)}")
                continue

            if 1 <= choice <= len(choices):
                return choices[choice - 1]
            else:
                slow_print(f"Wrong number, pick a number from {len(choices)}")

    def player_choice(self, entity_group) -> Entity:

        target_group = []
        for entity in entity_group:
            if entity.is_alive():
                target_group.append(entity)

        while True:
            slow_print("-- Available Targets--")
            for index, entity in enumerate(target_group, start=1):
                slow_print(f"{index} - {entity.name}")

            try:
                target_number = int(slow_input("Choose a Target\n"))
            except ValueError:
                slow_print(
                    f"Not a number, please choose a number between 1 and {len(target_group)}"
                )
                continue

            if target_number >= 1 and target_number <= len(target_group):
                target = target_group[target_number - 1]
                return target
            else:
                slow_print(
                    f"Wrong number, please choose a number between 1 and {len(target_group)}"
                )

    def choose_ability(self, ability_list, entity):
        while True:
            slow_print(f" Choose an ability\n")
            for index, ability in enumerate(ability_list, start=1):

                slow_print(f" {index} - {ability.name}")

            slow_print("0 - Back")

            try:
                number = int(slow_input("Choose\n"))
            except ValueError:
                slow_print("Not a number")
                continue

            if number == 0:
                return None
            elif 1 <= number <= len(ability_list):
                selected = ability_list[number - 1]
                if entity.resource_spending(selected.resource_cost):
                    return selected
                else:
                    slow_print("Not enough resource")
                    continue
            else:
                slow_print("Wrong number")

    def enemy_choice(self, entity_group) -> Entity:

        target_group = []
        for entity in entity_group:
            if entity.is_alive():
                target_group.append(entity)
        attack_target = random.choice(target_group)
        return attack_target

    def dmg_calculation(self, min_damage, max_damage) -> int:
        return random.randint(min_damage, max_damage)

    def roll_chance(self, chance) -> bool:
        return random.randint(1, 100) <= chance

    def announce_fight(self):
        palyer_names = ",".join(entity.name for entity in self.player_group)
        enemy_names = ",".join(entity.name for entity in self.enemy_group)
        slow_print(f"Fight between {palyer_names} and {enemy_names} !")

    def tick_phase(self):
        for entity in self.turn_order:
            if entity.is_alive():
                for effects_name, tick_damage in entity.tick_effects():
                    slow_print(
                        f"\n{entity.name} takes {tick_damage} from {effects_name}"
                    )
                entity.resource_generation(int(entity.max_resource * RAGE_TICK_FACTOR))
            if not entity.is_alive() and not entity.death_reported:
                self.announce_death(entity)
                entity.death_reported = True

    def announce_health(self):
        slow_print("Current Health:")

        for entity in self.turn_order:
            slow_print(
                f"Name:{entity.name} HP:{entity.current_health} {entity.resource_type}:{entity.current_resource}"
            )

    def fight_loop(self) -> None:

        self.announce_fight()

        while self.health_check(self.player_group) and self.health_check(
            self.enemy_group
        ):

            slow_print(f"\n------ Round: {self.rounds} ------")

            for entity in self.turn_order:
                if not entity.is_alive():
                    continue
                slow_print(f"{entity.name}s turn: ")
                action = None
                if entity in self.player_group:
                    while True:
                        action = self.choose_action(entity)
                        if action == "Attack":
                            damage = self.dmg_calculation(
                                entity.unarmed_min_damage, entity.unarmed_max_damage
                            )
                        else:
                            if action == "Skills":
                                ability_list = entity.entity_skills
                            elif action == "Spells":
                                ability_list = entity.entity_spells
                            ability = self.choose_ability(ability_list, entity)
                            if ability is None:
                                continue
                            else:
                                damage = self.dmg_calculation(
                                    ability.min_damage, ability.max_damage
                                )
                        target_group = self.enemy_group
                        target = self.player_choice(target_group)
                        break
                else:
                    target_group = self.player_group
                    target = self.enemy_choice(target_group)
                    damage = self.dmg_calculation(
                        entity.unarmed_min_damage, entity.unarmed_max_damage
                    )

                entity.resource_generation(int(entity.max_resource * RAGE_HIT_FACTOR))
                target.current_health = max(0, target.current_health - damage)
                slow_print(f"{entity.name} attacks {target.name} for {damage} !")
                if action == "Skills":
                    effect_list = ability.skill_effects
                elif action == "Spells":
                    effect_list = ability.spell_effects

                if action == "Skills" or action == "Spells":
                    for effect in effect_list:
                        if self.roll_chance(effect.effect_chance):
                            target.entity_effects.append(effect)

                if not target.is_alive() and not target.death_reported:
                    self.announce_death(target)
                    target.death_reported = True

                if not (
                    self.health_check(self.player_group)
                    and self.health_check(self.enemy_group)
                ):
                    break

            self.tick_phase()

            self.announce_health()

            self.rounds += 1


def test_fight(character_classes, enemies):

    player_group = []
    enemy_group = []

    player_group.append(character_classes[0])
    player_group.append(character_classes[1])

    enemy_group.append(enemies[0])
    enemy_group.append(enemies[1])

    return player_group, enemy_group
