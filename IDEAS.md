IDEAS.md — Defeat the Orc v2

## Kampf / Effekte
- Status-Effekt-Typen (effects.effect_type): tick (DoT/HoT), stat_modifier (im Bau), state/CC (kein Betrag), absorb, trigger — je neuer Typ = CHECK-Wert + Code-Stelle
- Raging Regeneration (Barbar): HoT + Enraged an einem Skill, Wut-verbrauch, später Talent-skaliert
- Magic Armor + Skillung: Reflect (trigger) / Element / Statusauslösung
- Battlemage: Nahkampfwaffen mit Int-Skalierung
- Verkettete Zustands-Kombos (3+ Zustände)
- Kampflog (später im Interface)

## Klassen / Progression
- Weitere Klassen: Druide, Mystiker, Nekromant
- Unterklassen + erweiterter Skillbaum
- Klassenquests
- Trainingssystem (z.B. schwere Rüstung für Barbar)

## Items / Ausrüstung
- Schild-als-Waffe (Shieldbash, Block+Verteidigung→Schaden, Offhand abgeschwächt) — M4
- Absteigendes Gewichtssystem
- Haltbarkeits-Formel zufaellige_haltbarkeit(max,min%,max%): Truhe 70-100, Träger 30-70, Höhle 10-40
- items: min/max_value + item_type statt 4 Wertspalten (mit Anker-Umbau, M3)

## Crafting (M3+, nach Item-/Affix-System)
- Generische Engine: Schmied/Alchemie/Koch/Verzauberer, eine Engine + Rezeptdaten in DB, nur Verzauberer eigener Pfad (Affix auf bestehendes Item)
- Materialfluss als verkettete Rezepte (Monsterteile → Staub/Pulver → Alchemie/Verzauberung)
- Recipe Discovery: Output ??? bis einmal hergestellt; entdeckt = Speicherstand-Zustand, ??? = abgeleitete Sicht; Quellen: herstellen/Buch/NPC/Gegner; Werkzeug-Gate per Einstiegsquest
- Wunschbrunnen (Event): Gamble Geld/Items → Ausrüstung+Verzauberung; teilt Unterbau mit Crafting

## Welt / NPCs
- NPC-Begleiter (finden, mitkämpfen, in Hub schicken)
- Hub-Angriff-Event
- Gruppenbildung + Befreiungsquests
- Verzauberer-NPC im Hub
- Weitere Gegnertypen: Untote, Tiere, Elementare, Mimic
- Nacht-/Rast-Encounter (rest ohne Risiko → nachts Gefahr), Zeitsystem M4
- Vollständiges Wettersystem
- Licht-System (Fackel, magische Items)

## UI / Technik
- UI-System mit Tooltips (pygame gesetzt): Inventar-Hover, Stat-Tooltips, Maus-Auswahl zusätzlich zu Nummern
- i18n/Mehrsprachigkeit (translations-Tabelle name_key/language/text, get_text(), Architektur früh vor M5)
- Dynamische Menüführung per Stack (append/pop)
- Bestiarium: entdeckt-Status, Anzahl besiegt, Datum, aufgedeckte Schwächen, Lore, Fortschritt nach Sieg-Art
- Grafik + Musik (itch.io, OpenGameArt)
- Permadeath-Modus

## Struktur-Kandidaten
- Unterklassen Player/Enemy(Entity) — erst bei 2+ divergierenden Fällen
- Boundary-Testing: Minimal- und Maximal-Konfig testen (bei Werten mit Cap)
