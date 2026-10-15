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
- Grundprinzip: Klassen starten klein, keine playstyle-bestimmenden Mechaniken in den ersten Leveln
  - playstyle-definierende Dinge erst nach ein paar Leveln, Spieler wählt selbst
  - Umskillen/Respec für Ingame-Geld, bewusst günstig, encouraged
- Ritter — Oath/Growth Charges, drei mögliche Richtungen (vermutlich drei Skill-Pfade einer Klasse):
  - Charges für Fähigkeiten ausgeben (verbrauchend)
  - Charges halten als Zustand/Modus ("halte 3 Charges für X-Playstyle")
  - Charges in Auras verteilen (Diablo-Aura-Stil, jede Charge speist eine anhaltende Aura)
  - Abgrenzung: Oath = halten/zuteilen, NICHT Combo (flüchtig aufbauen/entladen)
- Schurke — Combo-Punkte, max 5, erweiterbar durch Skills/Items:
  - max-Verbrauch NICHT immer optimal (taktische Tiefe)
  - Aufbau per Auto-Attack oder Fähigkeiten, Fähigkeiten auf Combos ausgelegt
  - gestaffelte Boni nach verbrauchter Punktzahl: 1 = höhere Effekt-Chance (Gift/Crit), 2 = längere Debuff-Dauer, 3 = längere Buff-Dauer / Fähigkeit stärker, 4 = max Schaden, 5 = Extra-Effekt (mehrere Effekte pro Fähigkeit)
  - -2 Combo für 2 Runden = Extra-Angriff
- Wetter-Caster — Reaktions-Playstyle (siehe Kampf/Effekte: Zustands-Kombos)
  - Wetter macht nass -> Eis friert ein -> stumpfer Angriff zerbricht
  - nutzt geplante state- und trigger-Effekttypen
  - Vorsicht: N×N-Kombinatorik, Reaktionen erst wenn beide Zustände real existieren
- Barbar — Improvised Attack:
  - wirft Umgebungsobjekte, Größenklassen klein/mittel/groß je nach Gebiet
  - braucht Objekte aus look()/Umgebung (siehe Welt)

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
- Umsehen mit Konsequenz: look() nicht nur Text
  - Objekte sammeln (für Improvised Attack)
  - Bereiche durchsuchen
  - Secrets (Schreine, Opfergegenstände, Schrein-Quest über mehrere Gebiete)
- Handelsrouten: Eskorte/Sicherung -> große Stadt als Endpunkt
  - gestaffelte Händler-Verfügbarkeit (seltene Items normal erhältlich, bessere Versionen)
  - Angreifer = Boss-Fraktion, koppelt an System A

## UI / Technik

- UI-System mit Tooltips (pygame gesetzt): Inventar-Hover, Stat-Tooltips, Maus-Auswahl zusätzlich zu Nummern
- i18n/Mehrsprachigkeit (translations-Tabelle name_key/language/text, get_text(), Architektur früh vor M5)
- Dynamische Menüführung per Stack (append/pop)
- Bestiarium: entdeckt-Status, Anzahl besiegt, Datum, aufgedeckte Schwächen, Lore, Fortschritt nach Sieg-Art
- Grafik + Musik (itch.io, OpenGameArt)
- Permadeath-Modus
- Effekt-Summe als Status-Sicht (Modifier in Klammern/Hover), dieselbe compute-Methode wie Schadensrechnung

## Struktur-Kandidaten

- Unterklassen Player/Enemy(Entity) — erst bei 2+ divergierenden Fällen
- Boundary-Testing: Minimal- und Maximal-Konfig testen (bei Werten mit Cap)
- Angriffe als Ability-Typen vereinheitlichen (Weapon/Improvised/Unarmed), kommt mit abilities-Merge

## Boss-Design

- kleines Vorwort zu Motivation/Lore vor dem Boss
- klassen-einzigartige Boss-/Story-Interaktionen (Horror-Game-Stil, jeder Charakter eigene Interaktionen)
- skalierender Boss: feste handgebaute Versionen + ein paar variierte (Element/Kampfstil), skaliert mit Zeit/Level

## Zeitsystem

- System A — Welt-Timer (King's-Bounty-Stil):
  - langsamer Countdown löst Eskalation aus (Goblins sammeln -> Hub-Angriff -> Gebiet wird "Waldfeste" -> bei 0 Boss-Angriff)
  - kein Zwang, aber Konsequenzen
  - Gebiets-Wechsel billig als andere Gebietsdefinition laden, nicht Raum-Mutation
- System B — Tag/Nacht-Phasen:
  - morgens/mittags/abends/nacht, aktionsgetrieben (nicht kontinuierlich, sonst Zeitdruck)
  - versteckt angezeigt
  - zwei getrennte Zähler (dieselbe Aktion kann beide speisen, nie eine Uhr für beides)
