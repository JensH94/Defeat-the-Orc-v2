import random


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
        self.base_crit_chance: int = daten.get("base_crit_chance", 1)
        self.current_crit_chance: int = self.base_crit_chance
        self.base_hit_chance: int = daten.get("base_hit_chance", 97)
        self.current_hit_chance: int = self.base_hit_chance
        self.entity_effects: list = []
        self.entity_spells: list = []
        self.entity_skills: list = []
        self.death_reported: bool = False
        self.base_stats: dict = {}

    def tick_effects(self):
        effect_events = []
        for effect in self.entity_effects:
            if effect.effect_type != "tick":
                continue
            tick_damage = effect.effects_apply(self)
            effect_events.append((effect.name, tick_damage))
            effect.effects_duration -= 1
        self.entity_effects = [e for e in self.entity_effects if e.effects_duration > 0]
        return effect_events

    def expire_modifiers(self):
        expired = []
        for effect in self.entity_effects:
            if effect.effect_type != "stat_modifier":
                continue
            effect.effects_duration -= 1
            if effect.effects_duration <= 0:
                expired.append(effect.name)
        self.entity_effects = [e for e in self.entity_effects if e.effects_duration > 0]
        return expired

    def resource_generation(self, resource_value):
        if self.resource_type == "rage":
            self.current_resource = min(
                self.max_resource, self.current_resource + resource_value
            )

    def mana_regeneration(self, resource_value):
        if self.resource_type == "mana":
            self.current_resource = min(
                self.max_resource, self.current_resource + resource_value
            )

    def enough_resource(self, resource_cost):
        return self.current_resource >= resource_cost

    def resource_spending(self, resource_cost):
        self.current_resource = self.current_resource - resource_cost

    def is_alive(self):
        return self.current_health > 0

    def resource_reset(self):
        if self.resource_type == "rage":
            self.current_resource = 0

    def find_effect(self, effect_id) -> Effects | None:
        for effect in self.entity_effects:
            if effect.effect_id == effect_id:
                return effect
        return None

    def stat_modifier_sum(self, stat):
        result = 0
        for effect in self.entity_effects:
            if effect.effect_type == "stat_modifier" and effect.stat == stat:
                result += effect.min_value
        return result

    def get_stat(self, stat):
        return self.base_stats.get(stat, 0)

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
        self.effect_id: int = daten.get("effect_id", 0)
        self.name: str = daten.get("name", "unbekannt")
        self.min_value: int = daten["min_value"]
        self.max_value: int = daten["max_value"]
        self.effects_duration: int = daten.get("duration", 0)
        self.effect_chance: int = daten.get("effect_chance", 0)
        self.effect_type: str = daten["effect_type"]
        self.stat: str = daten["stat"]

    def effects_apply(self, target):
        effects_dmg: int = random.randint(self.min_value, self.max_value)
        target.current_health = max(0, target.current_health - effects_dmg)
        return effects_dmg

    def __repr__(self):
        return f"Effect ({self.name} | min damage:{self.min_damage} | max damage:{self.max_damage} | effect chance:{self.effect_chance})"


class Skill:

    def __init__(self, daten: dict):
        self.skill_id: int = daten.get("skill_id", 0)
        self.name: str = daten.get("name", "unbekannt")
        self.min_damage: int = daten.get("min_damage", 0)
        self.max_damage: int = daten.get("max_damage", 0)
        self.resource_cost: int = daten.get("resource_cost", 0)
        self.effect_data: list[dict] = []
        self.target_type: str = daten["target_type"]

    def create_effects(self):
        effects = []
        for zeile in self.effect_data:
            effects.append(Effects(zeile))
        return effects

    def __repr__(self):
        return f"Skill ({self.name} | min damage:{self.min_damage} | max damage:{self.max_damage} | resource cost:{self.resource_cost})"


class Spell:

    def __init__(self, daten: dict):
        self.spell_id: int = daten.get("spell_id", 0)
        self.name: str = daten.get("name", "unbekannt")
        self.min_damage: int = daten.get("min_damage", 0)
        self.max_damage: int = daten.get("max_damage", 0)
        self.resource_cost: int = daten.get("resource_cost", 0)
        self.effect_data: list[dict] = []
        self.target_type: str = daten["target_type"]

    def create_effects(self):
        effects = []
        for zeile in self.effect_data:
            effects.append(Effects(zeile))
        return effects

    def __repr__(self):
        return f"Spell ({self.name} | min damage:{self.min_damage} | max damage:{self.max_damage} | resource cost:{self.resource_cost})"
