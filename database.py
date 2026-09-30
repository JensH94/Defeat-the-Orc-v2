import sqlite3


def verbinden():
    connection = sqlite3.connect("defeat_the_orc.db")
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    print("Verbindung hergestellt")
    return connection

def fetch_all(connection, query, params=None):
    cursor = connection.cursor()
    cursor.execute(query, params or [])
    return [dict(row) for row in cursor.fetchall()]


def get_data(connection, tabelle):
    query = f"SELECT * FROM {tabelle}"
    return fetch_all(connection, query)


def get_skills_for_classes(connection, class_id):
    query = """
            SELECT skills.*
            FROM class_skills
            JOIN skills ON class_skills.skill_id = skills.skill_id
            WHERE class_skills.class_id = ?
            """
    return fetch_all(connection, query, (class_id,))


def get_spells_for_classes(connection, class_id):
    query = """
            SELECT spells.*
            FROM class_spells
            JOIN spells ON class_spells.spell_id = spells.spell_id
            WHERE class_spells.class_id = ?
            """
    return fetch_all(connection, query, (class_id,))


def get_effects_for_skills(connection, skill_id):
    query = """
            SELECT effects.*, skill_effects.effect_chance
            FROM skill_effects
            JOIN effects ON skill_effects.effect_id = effects.effects_id
            WHERE skill_effects.skill_id = ?
            """
    return fetch_all(connection, query, (skill_id,))


def get_effects_for_spells(connection, spell_id):
    query = """
            SELECT effects.*, spell_effects.effect_chance
            FROM spell_effects
            JOIN effects ON spell_effects.effect_id = effects.effects_id
            WHERE spell_effects.spell_id = ?
            """
    return fetch_all(connection, query, (spell_id,))


def disconnect(connection):
    connection.close()
    print("Verbindung getrennt")
