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


def get_data(connection, tabelle):
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM {tabelle}")
    rows = cursor.fetchall()
    return rows


def get_skills_for_classes(connection, class_id):
    cursor = connection.cursor(dictionary=True)
    query = """
        SELECT skills.*
        FROM class_skills
        JOIN skills ON class_skills.skill_id = skills.skill_id
        WHERE class_skills.class_id = %s
        """
    cursor.execute(query, (class_id,))
    return cursor.fetchall()


def get_spells_for_classes(connection, class_id):
    cursor = connection.cursor(dictionary=True)
    query = """
        SELECT spells.*
        FROM class_spells
        JOIN spells ON class_spells.spell_id = spells.spell_id
        WHERE class_spells.class_id = %s
        """
    cursor.execute(query, (class_id,))
    return cursor.fetchall()


def get_effects_for_skills(connection,skill_id):
    cursor = connection.cursor(dictionary=True)
    query = """
        SELECT effects.*, skill_effects.effect_chance
        FROM skill_effects
        JOIN effects ON skill_effects.effect_id = effects.effects_id
        WHERE skill_effects.skill_id = %s
        """
    cursor.execute(query, (skill_id,))
    return cursor.fetchall()

def get_effects_for_spells(connection, spell_id):
    cursor = connection.cursor(dictionary=True)
    query= """
        SELECT effects.*, spell_effects.effect_chance
        FROM spell_effects
        JOIN effects ON spell_effects.effect_id = effects.effects_id
        WHERE spell_effects.spell_id = %s
        """
    cursor.execute(query, (spell_id,))
    return cursor.fetchall()


def disconnect(connection):
    if connection.is_connected():
        connection.close()
        print("Verbindung getrennt")
