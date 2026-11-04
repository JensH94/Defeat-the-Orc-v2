from classes import Entity, Item, Weapon, Armor, Skill, Spell
import random
from print_style import slow_print, slow_input
from database import (
    get_data,
    get_skills_for_classes,
    get_spells_for_classes,
    get_effects_for_skills,
    get_effects_for_spells,
    get_weapon,
    get_skills_for_enemies,
)


def build_lookup(rows, key):
    return {row[key]: row for row in rows}


def build_mapping(rows, key_col):
    mapping = {}
    for row in rows:
        mapping.setdefault(row[key_col], []).append(row)
    return mapping


def build_classes(classes_data, connection):
    character_classes = []
    for zeile in classes_data:
        entity = Entity(zeile)
        entity.base_stats = {
            "strength": zeile["strength"],
            "intelligence": zeile["intelligence"],
            "armor": zeile["armor"],
            "magic_resistance": zeile["magic_resistance"],
        }
        entity.entity_id = zeile["class_id"]
        weapon_id = zeile["default_weapon_id"]
        weapon_data = get_weapon(connection, weapon_id)[0]
        entity.weapon = Weapon(weapon_data)
        skills_data = get_skills_for_classes(connection, entity.entity_id)
        spells_data = get_spells_for_classes(connection, entity.entity_id)
        entity.entity_skills = build_skills(skills_data, connection)
        entity.entity_spells = build_spells(spells_data, connection)
        character_classes.append(entity)
    return character_classes


def build_enemies(enemies_data, connection):
    enemies = []
    for zeile in enemies_data:
        entity = Entity(zeile)
        entity.entity_id = zeile["enemy_id"]
        skills_data = get_skills_for_enemies(connection, entity.entity_id)
        entity.entity_skills = build_skills(skills_data, connection)
        entity.base_stats = {
            "armor": zeile["armor"],
            "magic_resistance": zeile["magic_resistance"],
        }
        enemies.append(entity)
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


def build_skills(skills_data, connection):
    skills = []
    for zeile in skills_data:
        skill = Skill(zeile)
        effects_data = get_effects_for_skills(connection, skill.skill_id)
        skill.effect_data = effects_data
        skills.append(skill)
    return skills


def build_spells(spells_data, connection):
    spells = []
    for zeile in spells_data:
        spell = Spell(zeile)
        effects_data = get_effects_for_spells(connection, spell.spell_id)
        spell.effect_data = effects_data
        spells.append(spell)
    return spells


def random_enemy_count():
    return random.randint(1, 3)


def random_enemy_select(enemies_data):
    enemy_select_list = random.choices(enemies_data, k=random_enemy_count())
    return enemy_select_list


def choose_player_class(character_classes):
    while True:
        slow_print(f"\nChoose a Class:\n")
        for index, entity in enumerate(character_classes, start=1):
            slow_print(f"{index} - {entity.name}")
        try:
            class_number = int(slow_input(f"\nWhich Class do you choose?\n"))
        except ValueError:
            slow_print(
                f"Wrong number, please choose a number between 1 and {len(character_classes)}\n"
            )
            continue
        if 1 <= class_number <= len(character_classes):
            return [character_classes[class_number - 1]]
        else:
            slow_print(
                f"Wrong number, please choose a number between 1 and {len(character_classes)}\n"
            )


def load_all(connection):

    classes_data = get_data(connection, "classes")
    enemies_data = get_data(connection, "enemies")
    items_data = get_data(connection, "items")
    weapons_data = get_data(connection, "weapons")
    armor_data = get_data(connection, "armor")

    character_classes = build_classes(classes_data, connection)
    items = build_items(items_data)
    weapons = build_weapons(weapons_data)
    armor = build_armor(armor_data)

    skills_by_id = build_lookup(get_data(connection, "skills"), "skill_id")
    spells_by_id = build_lookup(get_data(connection, "spells"), "spell_id")
    effects_by_id = build_lookup(get_data(connection, "effects"), "effect_id")
    weapons_by_id = build_lookup(get_data(connection, "weapons"), "weapon_id")

    enemy_skills_map = build_mapping(get_data(connection, "enemy_skills"), "enemy_id")
    class_skills_map = build_mapping(get_data(connection, "class_skills"), "class_id")
    class_spells_map = build_mapping(get_data(connection, "class_spells"), "class_id")
    skill_effects_map = build_mapping(get_data(connection, "skill_effects"), "skill_id")
    spell_effects_map = build_mapping(get_data(connection, "spell_effects"), "spell_id")

    registry = {
        "skills_by_id": skills_by_id,
        "spells_by_id": spells_by_id,
        "effects_by_id": effects_by_id,
        "weapons_by_id": weapons_by_id,
        "enemy_skills_map": enemy_skills_map,
        "class_skills_map": class_skills_map,
        "class_spells_map": class_spells_map,
        "skill_effects_map": skill_effects_map,
        "spell_effects_map": spell_effects_map,
    }

    data_all = {
        "classes": character_classes,
        "items": items,
        "weapons": weapons,
        "armor": armor,
        "enemies_data": enemies_data,
        "registry": registry,
    }

    print(skill_effects_map)

    return data_all, registry
