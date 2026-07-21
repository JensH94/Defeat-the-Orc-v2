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


def disconnect(connection):
    if connection.is_connected():
        connection.close()
        print("Verbindung getrennt")
