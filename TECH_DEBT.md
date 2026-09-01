Tech-Debt:

- effects.effects_id → effect_id umbenennen (Konsistenz: Tabelle Plural, Schlüssel Singular). Betrifft classes.py + alle JOINs. Eigener Commit.
- Type Hints noch nicht vervollständigt
- .gitattributes fehlt noch (CRLF/LF-Warnung)
- build_enemies braucht entity_id = zeile ["enemy_id"], sobald Enemies Fähigkeiten bekommen
- get_skills/get_spells_for_classes fast identisch
- entity_id wird vom Loader gesetzt statt im Konstruktor, später als Parameter
- **repr** wird zu testzwecken immer mal umgeschrieben ("dauerdebt")
- try/int(input)/range-check -> helper-function
- with connection.cursor() -> Context Manager für sauberkeit
- load_all -> Standalone = Effects -> entfernen
- Magic Strings -> "Attack", "Skills", "Spells" -> Enum benutzen
- helper functions -> redundanz reduzieren und sauberer