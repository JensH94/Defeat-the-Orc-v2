Tech-Debt:

## DB / Schema

- DB-Datei: connect legt still leere .db an → vor Verbinden prüfen + klare Meldung ("init_db.py ausführen")
- DB-Pfad relativ zum Arbeitsverzeichnis → Path(**file**).parent; DB-Name doppelt (database.py + init_db.py) → eine Stelle
- Verbindung nicht sauber geschlossen → try/finally oder contextlib.closing (main.py + init_db.py)
- get_data: Tabellenname per f-string → Whitelist oder bewusst kommentieren
- Schema härten: NOT NULL/CHECK für Pflichtspalten (jeweils mit dem Feature-Umbau der Tabelle)
- classes-Tabelle gemischt gehärtet: neue Stat-Spalten (strength/intelligence/armor/magic*resistance) haben NOT NULL + CHECK (>=0), alte Spalten (base_health etc.) nicht. Bewusst gestaffelt. Beim entities-Merge alle Spalten mithärten (zusammen mit base*-Rename).

## loader.py

- choose*player_class + random_enemy*\* raus aus Loader (SoC) → Menü-/Spawn-Modul
- build_list(cls, rows) generisch für build_items/weapons/armor (erst beim 3. Fall)
- items/weapons/armor geladen aber ungenutzt → ggf. bis M3 aufschieben
- get_skills/get_spells_for_classes (+ get_effects_for_skills/\_spells) fast identisch → erst beim 3. Fall zusammenlegen
- entity_id vom Loader gesetzt statt im Konstruktor
- build_enemies braucht entity_id = zeile["enemy_id"], sobald Enemies Fähigkeiten bekommen
- N+1-Queries im Loader → eher Architektur-Notiz ins README

## fight.py / environment.py

- fight_loop splitten: resolve_turn, apply_effects, end-of-round (kommt mit Buffs)
- initiative_list: nach current_initiative sortieren, key_base_init umbenennen
- ENCOUNTER_CHANCE dupliziert room_data.encounter_chance → eine Quelle
- room_movement gibt 2 Enum-Typen zurück → ein Typ pro Methode, an Grenze übersetzen
- palyer_names → player_names (announce_fight)
- resource_spending (classes.py) kein Schutz gegen negativ (aktuell sicher)
- enemy_choice/player_choice setzen nicht-leere Zielgruppe voraus (aktuell sicher)

## main.py

- if **name** == "**main**": Guard + main()-Funktion
- Ausgangs-else schluckt alles → bei 3+ Ausgängen explizit pro Enum-Wert

## Naming / Typen

- Naming-Konvention festlegen, dann Rename-Commit (verbinden/disconnect, tabelle, \_for_classes→_for_class, daten/zeile)
- Konstruktor-Attributnamen an DB-Spalten angleichen (im Tabellen-Härtungs-Commit)
- Pflichtfelder in Konstruktoren auf daten["key"] statt .get(...,0) (mit Härtung)
- Type Hints: Hit/Crit als int statt float (Entity.base_crit_chance, base_hit_chance, Weapon.crit_chance)
- Weapon.hit_chance: Attribut ohne DB-Spalte, Default 0.0 → entfernen oder kommentieren
- **repr** Dauerdebt (für Tests umgeschrieben)
- environment directions umbenennen
- .gitattributes fehlt (CRLF/LF-Warnung)
- try/int(input)/range-check → Helper-Funktion
- Prints "Verbindung hergestellt/getrennt" aus dem Spielerterminal
- base*health/base_initiative/base_resource tragen in der DB base*-Präfix, neue Stat-Spalten (strength/intelligence/armor/magic*res) nicht. DB kennt nur Grundwerte, base* ist dort überflüssig. Bei nächstem Schema-Rename angleichen (base\_ aus DB-Spalten raus).

## Schaden / Struktur:

- Schadensberechnung an 2 Orten: effects_apply (classes.py, Tick zieht selbst HP ab) und calculate_damage (fight.py, Angriff). Zu zentraler Pipeline in Fight zusammenlegen, sobald Ticks stat-skalieren oder durch Resistenz müssen.

## Effekte / Dauer:

- expire_modifiers zählt nur ==stat_modifier runter, tick_effects nur ==tick. Kommende Dauer-Typen (state/absorb/trigger) haben auch Dauer, fallen durch BEIDE Filter → beim Bau explizit einsortieren, sonst laufen sie nie ab.
