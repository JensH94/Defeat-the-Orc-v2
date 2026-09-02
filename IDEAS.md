IDEAS.md — Defeat the Orc v2
Ideen-Backlog und grobe Roadmap.
Neue Ideen kommen hier rein und werden NICHT sofort umgesetzt.

Ideas:

- Kampflog (später im Interface-Teil)
- Schild-als-Waffe-Mechanik (Balancing, Voraussetzung M4):
- Schilde als Einhand-Waffen, können angreifen (Shieldbash)
- Block-Wert + Verteidigung → Schadenswerte umrechnen (Formel TBD)
- Offhand-Waffen ohne Klassen-Talent abgeschwächt (Standard-Dual-Wield)
- i18n / Mehrsprachigkeit (vor M5 einplanen, Architektur muss früh stehen):
- translations-Tabelle (name_key, language, text)
- entities.name → name_key (technischer Identifier)
- vorhandene Item-Namen und Beschreibungen migrieren
- Helper get_text(key, language='de'), Code nutzt durchgehend get_text()
- UI-System mit Tooltips
- Bibliothek wählen (pygame / textual / arcade)
- Inventar-Fenster mit Hover-Tooltips
- Stat-Tooltips mit Beschreibung + Kategorie
- Maus-Auswahl statt Eingabe-Nummern (beides soll Funktionieren!)
- Absteigendes Gewichtssystem
- Klassenquests
- Crafting-System (Alchemie, Schmied)
- Trainingssystem (z. B. schwere Rüstung für Barbar)
- Haltbarkeits-Formel: zufaellige_haltbarkeit(max, min_prozent, max_prozent)
- frischer Drop aus Truhe
- Drop vom gegnerischen Träger
- in Höhle gefunden
- Boundary-Testing: immer Minimal- und Maximal-Konfiguration testen
- Bestiarium:
    Status entdeckt/nicht, Anzahl besiegt, Datum erster Sieg
    aufgedeckte Schwächen (erst nach X Kämpfen sichtbar), Lore-Text
    Fortschritt nach Art des Sieges (Tötung > Spezial-Kill > Flucht)

- NPC-Begleiter (finden, mitkämpfen, in Hub schicken)
- Hub-Angriff-Event
- Gruppenbildung und Befreiungsquests
- Unterklassen und erweiterter Skillbaum
- Weitere Klassen: Druide, Mystiker, Nekromant
- Weitere Gegnertypen: Untote, Tiere, Elementare, Mimic
- Verkettete Zustands-Kombos (3+ Zustände)
- Verzauberer-NPC im Hub
- Vollständiges Wettersystem
- Permadeath-Modus
- Licht-System (Fackel, magische Items)
- Grafik und Musik (itch.io, OpenGameArt.org)
- Dynamische Menüführung durch Stack (append,pop)