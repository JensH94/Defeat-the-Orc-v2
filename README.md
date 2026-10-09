# Defeat-the-Orc-v2

Defeat the Orc ist ein Schüler- und Lernprojekt welches den Fokus hat von Grund auf ein Spiel zu entwickeln. Es dient zur Festigung erlernter Kenntnisse sowie dem Erlernen neuer Fähigkeiten durch das Hinzufügen neuer Features und Spielmechaniken.

## Status

Grundgerüst des Kampfes, erste Umgebung und Räume laufen. Als Nächstes das Kampfsystem erweitern.

## Tech-Stack

- Python 3.14.3
- SQLite (in python enrhalten)
- ruff 0.15.22

## Setup

1. Repo Klonen
2. venv anlegen und aktivieren
3. pip install -r requirements.txt
4. python init_db.py ausführen (erstellt Datenbank aus schema_sqlite.sql)
5. python main.py ausführen

## Projektstruktur

- main.py - Einstiegspunkt
- fight.py - Kampfsystem
- loader.py - lädt Entities aus der DB in Objekte
- classes.py - Datenmodelle(Fighter, Item,...)
- database.py - DB-Verbindung
- display.py - Status Anzeige
- print_style.py - Terminal textausgabe Stil
- environment.py - Erkundung, Räume, Menüführung
- room_data.py - Raumdaten (Wald)
- init_db.py - baut die Datenbank aus dem Schema
- schema_sqlite.sql - Datenbank-Schema (Struktur + Startdaten)
- [MILESTONES](MILESTONES.md)/[IDEAS](IDEAS.md)/[TECH_DEBT](TECH_DEBT.md) - Planung, Ideen, Verbesserungen

## Architektur-Entscheidungen

- Datenbank statt json zur Übung im Umgang mit Datenbanken
- Manuelles Loader-Mapping statt ORM für besseres Verständnis
- TECH_DEBT statt direkter Fix um Fehler sowie Bugs zu sammeln für strukturiertes Abarbeiten zu gegebener Zeit
- Migration von MariaDB zu SQLite:
  database.py auf sqlite3 umgestellt, schema_sqlite.sql als Schema-Quelle,
  init_db.py baut die DB daraus. Connector und dotenv entfernt, README angepasst.
  Grund: Single-Player-Spiel braucht keinen DB-Server; Datei-DB vereinfacht Packaging.

  Alle Rechte vorbehalten.
