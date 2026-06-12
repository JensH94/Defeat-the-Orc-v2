class Entity:

    def __init__(self, daten: dict):
        self.name: str = daten.get("name", "Unbekannt")
        self.base_health: int = daten.get("base_health", 0)
        self.base_mana: int = daten.get("base_mana", 0)
        self.base_initiative: int = daten.get("base_initiative", 0)

    def __repr__(self) -> str:
        return f"Entity ({self.name} | HP: {self.base_health} | Mana: {self.base_mana} | Initiative: {self.base_initiative})"
