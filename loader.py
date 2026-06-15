from classes import Entity, Item, Weapon, Armor, Effect, Skill, Spell


def build_classes(classes_data):
    character_classes = []
    for zeile in classes_data:
        character_classes.append(Entity(zeile))
    return character_classes


def build_enemies(enemies_data):
    enemies = []
    for zeile in enemies_data:
        enemies.append(Entity(zeile))
    return enemies


def build_items(items_data):
    items = []
    for zeile in items_data:
        items.append(Item(zeile))
    return items


def build_weapons(weapons_data):
    weapons = []
    for zeile in weapons_data:
        weapons.append(Weapon(zeile))
    return weapons


def build_armor(armor_data):
    armor = []
    for zeile in armor_data:
        armor.append(Armor(zeile))
    return armor


def build_effects(effects_data):
    effects = []
    for zeile in effects_data:
        effects.append(Effect(zeile))
    return effects


def build_skills(skills_data):
    skills = []
    for zeile in skills_data:
        skills.append(Skill(zeile))
    return skills


def build_spells(spells_data):
    spells = []
    for zeile in spells_data:
        spells.append(Spell(zeile))
    return spells
