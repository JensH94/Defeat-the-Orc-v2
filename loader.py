from classes import Entity, Item, Weapon, Armor, Effects, Skill, Spell
from database import get_data, get_skills_for_classes, get_spells_for_classes


def build_classes(classes_data, connection):
    character_classes = []
    for zeile in classes_data:
        entity = Entity(zeile)
        entity.entity_id = zeile["class_id"]
        skills_data = get_skills_for_classes(connection, entity.entity_id)
        spells_data = get_spells_for_classes(connection, entity.entity_id)
        entity.entity_skills = build_skills(skills_data)
        entity.entity_spells = build_spells(spells_data)
        character_classes.append(entity)
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
        effects.append(Effects(zeile))
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


def load_all(connection):

    classes_data = get_data(connection, "classes")
    enemies_data = get_data(connection, "enemies")
    items_data = get_data(connection, "items")
    weapons_data = get_data(connection, "weapons")
    armor_data = get_data(connection, "armor")
    effects_data = get_data(connection, "effects")

    character_classes = build_classes(classes_data, connection)
    enemies = build_enemies(enemies_data)
    items = build_items(items_data)
    weapons = build_weapons(weapons_data)
    armor = build_armor(armor_data)
    effects = build_effects(effects_data)

    data_all = {
        "classes": character_classes,
        "enemies": enemies,
        "items": items,
        "weapons": weapons,
        "armor": armor,
        "effects": effects,
    }
    return data_all
