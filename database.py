import mysql.connector
from mysql.connector import Error


def verbinden():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            port=3306,
            password="",
            database="defeat_the_orc",
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


connection = verbinden()
classes_data = get_data(connection, "classes")
print(classes_data)
disconnect(connection)
