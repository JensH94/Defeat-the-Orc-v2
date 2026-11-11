from __future__ import annotations
from classes import Entity, Weapon, Skill, Spell
import random
from print_style import slow_print, slow_input
from database import (
    get_data,
    get_skills_for_classes,
    get_spells_for_classes,
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


def build_skills(skills_data, registry):
    effects_by_id = registry["effects_by_id"]
    skill_effects_map = registry["skill_effects_map"]
    skills = []
    for zeile in skills_data:
        skill = Skill(zeile)
        junction_rows = skill_effects_map.get(skill.skill_id, [])
        skill.effect_data = [
            {**effects_by_id[row["effect_id"]], "effect_chance": row["effect_chance"]}
            for row in junction_rows
        ]
        skills.append(skill)
    return skills


def build_spells(spells_data, registry):
    effects_by_id = registry["effects_by_id"]
    spell_effects_map = registry["spell_effects_map"]
    spells = []
    for zeile in spells_data:
        spell = Spell(zeile)
        junction_rows = spell_effects_map.get(spell.spell_id, [])
        spell.effect_data = [
            {**effects_by_id[row["effect_id"]], "effect_chance": row["effect_chance"]}
            for row in junction_rows
        ]
        spells.append(spell)
    return spells


def random_enemy_count():
    return random.randint(1, 3)


def random_enemy_select(enemies_data):
    enemy_select_list = random.choices(enemies_data, k=random_enemy_count())
    return enemy_select_list


def choose_player_class(character_classes):
    while True:
        slow_print("\nChoose a Class:\n")
        for index, entity in enumerate(character_classes, start=1):
            slow_print(f"{index} - {entity.name}")
        try:
            class_number = int(slow_input("\nWhich Class do you choose?\n"))
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

    character_classes = build_classes(classes_data, connection)

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
        "enemies_data": enemies_data,
        "registry": registry,
    }

    return data_all
