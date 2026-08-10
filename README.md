# Defeat-the-Orc-v2
Defeat the Orc ist ein Schüler- und Lernprojekt welches den Fokus hat von Grund auf ein Spiel zu entwickeln. Es dient zur Festigung erlernter Kenntnisse sowie dem Erlernen neuer Fähigkeiten durch das Hinzufügen neuer Features und Spielmechaniken.

## Status
Grundgerüst des Kampfes läuft. Als Nächstes das Kampfsystem erweitern und Räume und Umgebung hinzufügen.

## Tech-Stack
- Python 3.14.3
- MariaDB 10.4
- mysql-connector-python 9.7.0
- python-dotenv 1.2.2
- ruff 0.15.22

## Setup
1. Repo Klonen
2. venv anlegen und aktivieren
3. pip install -r requirements.txt
4. DB importieren (defeat_the_orc.sql) über phpMyAdmin oder über SQL-Befehl
5. env aus env.example anlegen
6. python main.py ausführen

## Projektstruktur
- main.py - Einstiegspunkt
- fight.py - Kampfsystem
- loader.py - lädt Entities aus der DB in Objekte
- classes.py - Datenmodelle(Fighter, Item,...)
- database.py - DB-Verbindung
- defeat_the_orc.sql - DB-Dump
- [MILESTONES](MILESTONES.md)/[IDEAS](IDEAS.md)/[TECH_DEBT](TECH_DEBT.md) - Planung, Ideen, Verbesserungen

## Architektur-Entscheidungen
- Datenbank statt json zur Übung im Umgang mit Datenbanken
- Manuelles Loader-Mapping statt ORM für besseres Verständnis
- TECH_DEBT statt direkter Fix um Fehler sowie Bugs zu sammeln für strukturiertes Abarbeiten zu gegebener Zeit


  Alle Rechte vorbehalten.