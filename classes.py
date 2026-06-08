class Entity:

    def __init__(self, name, base_health, base_mana, base_initiative):
        self.name: str = name
        self.base_health: int = base_health
        self.base_mana: int = base_mana
        self.base_initiative: int = base_initiative
