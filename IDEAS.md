IDEAS.md — Defeat the Orc v2
Ideen-Backlog und grobe Roadmap. Übernommen aus dem v1-Meilensteinplan + Tagebuch.
Grundregel: Ein Meilenstein = eine Sache funktioniert vollständig.
Neue Ideen kommen hier rein und werden NICHT sofort umgesetzt.
Roadmap (Kurzfassung)

M0 Fundament — DB fertig, alle Models, Loader funktioniert
M1 Erster Kampf — Kampf komplett aus DB geladen und spielbar
M2 Erste Umgebung — Höhle begehbar, Räume, Umschauen, Gegner spawnen
M3 Erster Spiel-Loop — Hub + Höhle + Tod + Zeitsystem = spielbar
M4 Items & Inventar — Loot, Inventar, Ausrüsten, Händler, Schmied
M5 MVP — Orc, 4 Klassen, Skillbaum, Quests, durchspielbar
M6+ Post-MVP — Backlog, erst nach M5 anfassen

Ideen nach Meilenstein
M1 — Kampf

Kampflog (später im Interface-Teil)
Schild-als-Waffe-Mechanik (Balancing, Voraussetzung M4):

Schilde als Einhand-Waffen, können angreifen (Shieldbash)
Block-Wert + Verteidigung → Schadenswerte umrechnen (Formel TBD)
Offhand-Waffen ohne Klassen-Talent abgeschwächt (Standard-Dual-Wield)



M2 — Umgebung

i18n / Mehrsprachigkeit (vor M5 einplanen, Architektur muss früh stehen):

translations-Tabelle (name_key, language, text)
entities.name → name_key (technischer Identifier)
vorhandene Item-Namen und Beschreibungen migrieren
Helper get_text(key, language='de'), Code nutzt durchgehend get_text()



M3 — Loop

UI-System mit Tooltips:

Bibliothek wählen (pygame / textual / arcade)
Inventar-Fenster mit Hover-Tooltips
Stat-Tooltips mit Beschreibung + Kategorie
Maus-Auswahl statt Eingabe-Nummern (beides soll Funktionieren!)



M4 — Items & Inventar

Absteigendes Gewichtssystem
Klassenquests
Crafting-System (Alchemie, Schmied)
Trainingssystem (z. B. schwere Rüstung für Barbar)
Haltbarkeits-Formel: zufaellige_haltbarkeit(max, min_prozent, max_prozent)

frischer Drop aus Truhe: 0.7–1.0
Drop vom gegnerischen Träger: 0.3–0.7
in Höhle gefunden / vergessen: 0.1–0.4



M5 — MVP / Balancing

Boundary-Testing: immer Minimal- und Maximal-Konfiguration testen
(nackt vs. Cap-Ausrüstung), gilt für alle Werte mit Cap (Rüstung, Resistenzen, Crit)
Bestiarium als eigene Domäne:

Tabelle bestiarium_eintraege mit entity_id (FK)
Status entdeckt/nicht, Anzahl besiegt, Datum erster Sieg
aufgedeckte Schwächen (erst nach X Kämpfen sichtbar), Lore-Text
Fortschritt nach Art des Sieges (Tötung > Spezial-Kill > Flucht)



M6+ — Post-MVP Backlog

NPC-Begleiter (finden, mitkämpfen, in Hub schicken)
Hub-Angriff-Event
Gruppenbildung und Befreiungsquests
Unterklassen und erweiterter Skillbaum
Weitere Klassen: Druide, Mystiker, Nekromant
Weitere Gegnertypen: Untote, Tiere, Elementare, Mimic
Verkettete Zustands-Kombos (3+ Zustände)
Verzauberer-NPC im Hub
Vollständiges Wettersystem
Permadeath-Modus
Licht-System (Fackel, magische Items)
Grafik und Musik (itch.io, OpenGameArt.org)