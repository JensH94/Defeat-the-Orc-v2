import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()


def verbinden():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=int(os.getenv("DB_PORT")),
            database=os.getenv("DB_NAME"),
        )

        if connection.is_connected():
            print("Verbindung hergestellt")
        return connection

    except Error as e:
        print(f"Fehler: {e}")
        return None


def fetch_all(connection, query, params=None):
    with connection.cursor(dictionary=True) as cursor:
        cursor.execute(query, params)
        return cursor.fetchall()


def get_data(connection, tabelle):
    query = f"SELECT * FROM {tabelle}"
    return fetch_all(connection, query)


def get_skills_for_classes(connection, class_id):
    query = """
            SELECT skills.*
            FROM class_skills
            JOIN skills ON class_skills.skill_id = skills.skill_id
            WHERE class_skills.class_id = %s
            """
    return fetch_all(connection, query, (class_id,))


def get_spells_for_classes(connection, class_id):
    query = """
            SELECT spells.*
            FROM class_spells
            JOIN spells ON class_spells.spell_id = spells.spell_id
            WHERE class_spells.class_id = %s
            """
    return fetch_all(connection, query, (class_id,))


def get_effects_for_skills(connection, skill_id):
    query = """
            SELECT effects.*, skill_effects.effect_chance
            FROM skill_effects
            JOIN effects ON skill_effects.effect_id = effects.effects_id
            WHERE skill_effects.skill_id = %s
            """
    return fetch_all(connection, query, (skill_id,))


def get_effects_for_spells(connection, spell_id):
    query = """
            SELECT effects.*, spell_effects.effect_chance
            FROM spell_effects
            JOIN effects ON spell_effects.effect_id = effects.effects_id
            WHERE spell_effects.spell_id = %s
            """
    return fetch_all(connection, query, (spell_id,))


def disconnect(connection):
    if connection.is_connected():
        connection.close()
        print("Verbindung getrennt")
