import mysql.connector
from mysql.connector import Error


def verbinden():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            port=3306,
            passwort="",
            database="defeat_the_orc",
        )

        if connection.is_connected():
            print("Verbindung hergestellt")
        return connection

    except Error as e:
        print(f"Fehler: {e}")
        return None
