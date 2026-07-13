class Entity:

    def __init__(self, daten: dict):
        self.entity_id: int = daten.get("entity_id", 0)
        self.name: str = daten.get("name", "Unbekannt")
        self.base_health: int = daten.get("base_health", 0)
        self.current_health: int = self.base_health
        self.base_mana: int = daten.get("base_mana", 0)
        self.current_mana: int = self.base_mana
        self.base_initiative: int = daten.get("base_initiative", 0)
        self.current_initiative: int = self.base_initiative

    def __repr__(self) -> str:
        return f"Entity ({self.name} | HP: {self.base_health} | Mana: {self.base_mana} | Initiative: {self.base_initiative})"


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
        self.crit_chance: int = daten.get("crit_chance", 0)
        self.hit_chance: int = daten.get("hit_chance", 0)

    def __repr__(self):
        return f"Weapon ({self.name} | min damage:{self.min_damage} | max damage:{self.max_damage} | crit chance:{self.crit_chance} | hit chance:{self.hit_chance})"


class Armor:

    def __init__(self, daten: dict):
        self.armor_id: int = daten.get("armor_id", 0)
        self.name: str = daten.get("name", "unbekannt")
        self.defense: int = daten.get("defense", 0)

    def __repr__(self):
        return f"Armor ({self.name} | Defense:{self.defense})"


class Effect:

    def __init__(self, daten: dict):
        self.effect_id: int = daten.get("effect_id", 0)
        self.name: str = daten.get("name", "unbekannt")
        self.min_damage: int = daten.get("min_damage", 0)
        self.max_damage: int = daten.get("max_damage", 0)

    def __repr__(self):
        return f"Effect ({self.name} | min damage:{self.min_damage} | max damage:{self.max_damage})"


class Skill:

    def __init__(self, daten: dict):
        self.skill_id: int = daten.get("skill_id", 0)
        self.name: str = daten.get("name", "unbekannt")
        self.min_damage: int = daten.get("min_damage", 0)
        self.max_damage: int = daten.get("max_damage", 0)

    def __repr__(self):
        return f"Skill ({self.name} | min damage:{self.min_damage} | max damage:{self.max_damage})"


class Spell:

    def __init__(self, daten: dict):
        self.spell_id: int = daten.get("spell_id", 0)
        self.name: str = daten.get("name", "unbekannt")
        self.min_damage: int = daten.get("min_damage", 0)
        self.max_damage: int = daten.get("max_damage", 0)
        self.mana_cost: int = daten.get("mana_cost", 0)

    def __repr__(self):
        return f"Spell ({self.name} | min damage:{self.min_damage} | max damage:{self.max_damage} | mana cost:{self.mana_cost})"
