from __future__ import annotations
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


def disconnect(connection):
    connection.close()
    print("Verbindung getrennt")
