from classes import Entity, Item, Weapon, Armor, Effects, Skill, Spell
import random
from print_style import slow_print, slow_input
from database import (
    get_data,
    get_skills_for_classes,
    get_spells_for_classes,
    get_effects_for_skills,
    get_effects_for_spells,
)


def build_classes(classes_data, connection):
    character_classes = []
    for zeile in classes_data:
        entity = Entity(zeile)
        entity.entity_id = zeile["class_id"]
        skills_data = get_skills_for_classes(connection, entity.entity_id)
        spells_data = get_spells_for_classes(connection, entity.entity_id)
        entity.entity_skills = build_skills(skills_data, connection)
        entity.entity_spells = build_spells(spells_data, connection)
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


def build_skills(skills_data, connection):
    skills = []
    for zeile in skills_data:
        skill = Skill(zeile)
        effects_data = get_effects_for_skills(connection, skill.skill_id)
        skill.skill_effects = build_effects(effects_data)
        skills.append(skill)
    return skills


def build_spells(spells_data, connection):
    spells = []
    for zeile in spells_data:
        spell = Spell(zeile)
        effects_data = get_effects_for_spells(connection, spell.spell_id)
        spell.spell_effects = build_effects(effects_data)
        spells.append(spell)
    return spells


def random_enemy_count():
    return random.randint(1, 3)


def random_enemy_select(enemies_data):
    enemy_select_list = random.choices(enemies_data, k=random_enemy_count())
    return enemy_select_list

def choose_player_class(character_classes):
    while True:
        slow_print(f"Choose a Class:\n")
        for index, entity in enumerate(character_classes, start=1):
            slow_print(f"{index} - {entity.name}")
        try:
            class_number = int(slow_input(f"Which Class do you choose?"))
        except ValueError:
            slow_print(f"Wrong number, please choose a number between 1 and {len(character_classes)}")
            continue
        if 1 <= class_number <= len(character_classes):
            return [character_classes[class_number -1]]
        else:
            slow_print(f"Wrong number, please choose a number between 1 and {len(character_classes)}")


def load_all(connection):

    classes_data = get_data(connection, "classes")
    enemies_data = get_data(connection, "enemies")
    items_data = get_data(connection, "items")
    weapons_data = get_data(connection, "weapons")
    armor_data = get_data(connection, "armor")
    effects_data = get_data(connection, "effects")

    character_classes = build_classes(classes_data, connection)
    items = build_items(items_data)
    weapons = build_weapons(weapons_data)
    armor = build_armor(armor_data)
    effects = build_effects(effects_data)

    data_all = {
        "classes": character_classes,
        "items": items,
        "weapons": weapons,
        "armor": armor,
        "effects": effects,
        "enemies_data": enemies_data,
    }
    return data_all
