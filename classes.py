import random
from print_style import slow_print


class Entity:

    def __init__(self, daten: dict):
        self.entity_id: int = 0
        self.name: str = daten.get("name", "Unbekannt")
        self.base_health: int = daten.get("base_health", 0)
        self.current_health: int = self.base_health
        self.base_resource: int = daten.get("base_resource", 0)
        self.max_resource: int = daten.get("max_resource", 0)
        self.current_resource: int = self.base_resource
        self.resource_type: str = daten.get("resource_type", "none")
        self.base_initiative: int = daten.get("base_initiative", 0)
        self.current_initiative: int = self.base_initiative
        self.unarmed_min_damage: int = daten.get("unarmed_min_damage", 1)
        self.unarmed_max_damage: int = daten.get("unarmed_max_damage", 3)
        self.base_crit_chance: float = daten.get("base_crit_chance", 0.01)
        self.current_crit_chance: float = self.base_crit_chance
        self.base_hit_chance: float = daten.get("base_hit_chance", 0.97)
        self.current_hit_chance: float = self.base_hit_chance
        self.entity_effects: list = []
        self.entity_spells: list = []
        self.entity_skills: list = []
        self.death_reported: bool = False

    def tick_effects(self):
        effects_events = []
        for effects in self.entity_effects:
            tick_damage = effects.effects_apply(self)
            effects_events.append((effects.name, tick_damage))
            effects.effects_duration -= 1
        self.entity_effects = [e for e in self.entity_effects if e.effects_duration > 0]
        return effects_events

    def resource_generation(self, resource_value):
        if self.resource_type == "rage":
            self.current_resource = min(
                self.max_resource, self.current_resource + resource_value
            )

    def resource_spending(self, resource_cost):
        if self.current_resource >= resource_cost:
            self.current_resource = self.current_resource - resource_cost
            return True
        else:
            return False

    def is_alive(self):
        return self.current_health > 0

    def __repr__(self) -> str:
        return f"Entity ({self.name} | HP: {self.base_health} | Mana: {self.base_resource} | Initiative: {self.base_initiative})"


class Item:

    def __init__(self, daten: dict):
        self.item_id: int = daten.get("item_id", 0)
        self.name: str = daten.get("name", "unbekannt")
        self.min_damage: int = daten.get("min_damage", 0)
        self.max_damage: int = daten.get("max_damage", 0)
        self.min_heal: int = daten.get("min_heal", 0)
        self.max_heal: int = daten.get("max_heal", 0)

    def __repr__(self):
        return f"Item ({self.name} | min damage: {self.min_damage} | max damage:{self.max_damage} | min heal:{self.min_heal} | max heal:{self.max_heal})"


class Weapon:

    def __init__(self, daten: dict):
        self.weapon_id: int = daten.get("weapon_id", 0)
        self.name: str = daten.get("name", "unbekannt")
        self.min_damage: int = daten.get("min_damage", 0)
        self.max_damage: int = daten.get("max_damage", 0)
        self.crit_chance: float = daten.get("crit_chance", 0.0)
        self.hit_chance: float = daten.get("hit_chance", 0.0)

    def __repr__(self):
        return f"Weapon ({self.name} | min damage:{self.min_damage} | max damage:{self.max_damage} | crit chance:{self.crit_chance} | hit chance:{self.hit_chance})"


class Armor:

    def __init__(self, daten: dict):
        self.armor_id: int = daten.get("armor_id", 0)
        self.name: str = daten.get("name", "unbekannt")
        self.defense: int = daten.get("defense", 0)

    def __repr__(self):
        return f"Armor ({self.name} | Defense:{self.defense})"


class Effects:

    def __init__(self, daten: dict):
        self.effects_id: int = daten.get("effects_id", 0)
        self.name: str = daten.get("name", "unbekannt")
        self.min_damage: int = daten.get("min_damage", 0)
        self.max_damage: int = daten.get("max_damage", 0)
        self.effects_target = "current_health"
        self.effects_duration: int = daten.get("duration", 0)

    def effects_apply(self, target):
        effects_dmg: int = random.randint(self.min_damage, self.max_damage)
        target.current_health = max(0, target.current_health - effects_dmg)
        return effects_dmg

    def __repr__(self):
        return f"Effect ({self.name} | min damage:{self.min_damage} | max damage:{self.max_damage})"


class Skill:

    def __init__(self, daten: dict):
        self.skill_id: int = daten.get("skill_id", 0)
        self.name: str = daten.get("name", "unbekannt")
        self.min_damage: int = daten.get("min_damage", 0)
        self.max_damage: int = daten.get("max_damage", 0)
        self.resource_cost: int = daten.get("resource_cost", 0)

    def __repr__(self):
        return f"Skill ({self.name} | min damage:{self.min_damage} | max damage:{self.max_damage} | resource cost:{self.resource_cost})"


class Spell:

    def __init__(self, daten: dict):
        self.spell_id: int = daten.get("spell_id", 0)
        self.name: str = daten.get("name", "unbekannt")
        self.min_damage: int = daten.get("min_damage", 0)
        self.max_damage: int = daten.get("max_damage", 0)
        self.resource_cost: int = daten.get("resource_cost", 0)

    def __repr__(self):
        return f"Spell ({self.name} | min damage:{self.min_damage} | max damage:{self.max_damage} | resource cost:{self.resource_cost})"
