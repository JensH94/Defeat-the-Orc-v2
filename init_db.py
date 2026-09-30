import sqlite3
import os

if os.path.exists("defeat_the_orc.db"):
    os.remove("defeat_the_orc.db")

connection = sqlite3.connect("defeat_the_orc.db")
with open("schema_sqlite.sql", encoding="utf-8") as f:
    connection.executescript(f.read())
connection.close()
print("Datenbank neu erstellt")