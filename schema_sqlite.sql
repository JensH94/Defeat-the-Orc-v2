-- SQLite-Schema für Defeat-the-Orc-v2
-- Aus dem MariaDB-Dump (defeat_the_orc.sql) neu geschrieben.
-- Reihenfolge: erst Tabellen ohne FK, dann die referenzierenden.

PRAGMA foreign_keys = ON;

-- ---------- Stammtabellen (keine FKs) ----------

CREATE TABLE armor (
    armor_id INTEGER PRIMARY KEY,
    name     TEXT,
    defense  INTEGER
);

CREATE TABLE classes (
    class_id        INTEGER PRIMARY KEY,
    name            TEXT,
    base_health     INTEGER,
    base_initiative INTEGER,
    base_resource   INTEGER,
    resource_type   TEXT,
    max_resource    INTEGER
);

CREATE TABLE effects (
    effects_id INTEGER PRIMARY KEY,
    name       TEXT,
    min_damage INTEGER,
    max_damage INTEGER,
    duration   INTEGER DEFAULT 0
);

CREATE TABLE enemies (
    enemy_id        INTEGER PRIMARY KEY,
    name            TEXT,
    base_health     INTEGER,
    base_mana       INTEGER,
    base_initiative INTEGER
);

CREATE TABLE items (
    item_id    INTEGER PRIMARY KEY,
    name       TEXT,
    min_damage INTEGER,
    max_damage INTEGER,
    min_heal   INTEGER,
    max_heal   INTEGER
);

CREATE TABLE skills (
    skill_id      INTEGER PRIMARY KEY,
    name          TEXT,
    min_damage    INTEGER,
    max_damage    INTEGER,
    resource_cost INTEGER
);

CREATE TABLE spells (
    spell_id      INTEGER PRIMARY KEY,
    name          TEXT,
    min_damage    INTEGER,
    max_damage    INTEGER,
    resource_cost INTEGER
);

CREATE TABLE weapons (
    weapon_id  INTEGER PRIMARY KEY,
    name       TEXT,
    min_damage INTEGER,
    max_damage INTEGER,
    crit_chance INTEGER
);

-- ---------- Verknüpfungstabellen (mit FKs) ----------

CREATE TABLE class_skills (
    class_id INTEGER,
    skill_id INTEGER,
    PRIMARY KEY (class_id, skill_id),
    FOREIGN KEY (class_id) REFERENCES classes(class_id),
    FOREIGN KEY (skill_id) REFERENCES skills(skill_id)
);

CREATE TABLE class_spells (
    class_id INTEGER,
    spell_id INTEGER,
    PRIMARY KEY (class_id, spell_id),
    FOREIGN KEY (class_id) REFERENCES classes(class_id),
    FOREIGN KEY (spell_id) REFERENCES spells(spell_id)
);

CREATE TABLE skill_effects (
    skill_id      INTEGER,
    effect_id     INTEGER,
    effect_chance INTEGER,
    PRIMARY KEY (skill_id, effect_id),
    FOREIGN KEY (skill_id) REFERENCES skills(skill_id),
    FOREIGN KEY (effect_id) REFERENCES effects(effects_id)
);

CREATE TABLE spell_effects (
    spell_id      INTEGER,
    effect_id     INTEGER,
    effect_chance INTEGER,
    PRIMARY KEY (spell_id, effect_id),
    FOREIGN KEY (spell_id) REFERENCES spells(spell_id),
    FOREIGN KEY (effect_id) REFERENCES effects(effects_id)
);

-- ---------- Daten ----------

INSERT INTO armor (armor_id, name, defense) VALUES
(1, 'Mage Cloth', 10),
(2, 'Barbarian Leather', 17);

INSERT INTO classes (class_id, name, base_health, base_initiative, base_resource, resource_type, max_resource) VALUES
(1, 'Mage', 20, 15, 100, 'mana', 100),
(2, 'Barbarian', 30, 13, 0, 'rage', 100);

INSERT INTO effects (effects_id, name, min_damage, max_damage, duration) VALUES
(1, 'Fire', 2, 4, 3),
(2, 'Bleed', 1, 5, 4);

INSERT INTO enemies (enemy_id, name, base_health, base_mana, base_initiative) VALUES
(1, 'Rat', 15, 0, 12),
(2, 'Slime', 15, 0, 10);

INSERT INTO items (item_id, name, min_damage, max_damage, min_heal, max_heal) VALUES
(1, 'Small Bomb', 2, 6, 0, 0),
(2, 'Small Health Potion', 0, 0, 2, 6);

INSERT INTO skills (skill_id, name, min_damage, max_damage, resource_cost) VALUES
(1, 'Wounding Strike', 2, 6, 10);

INSERT INTO spells (spell_id, name, min_damage, max_damage, resource_cost) VALUES
(1, 'Fireball', 3, 9, 12);

INSERT INTO weapons (weapon_id, name, min_damage, max_damage, crit_chance) VALUES
(1, 'Axe', 3, 10, 0),
(2, 'Staff', 1, 6, 0);

INSERT INTO class_skills (class_id, skill_id) VALUES
(2, 1);

INSERT INTO class_spells (class_id, spell_id) VALUES
(1, 1);

INSERT INTO skill_effects (skill_id, effect_id, effect_chance) VALUES
(1, 2, 100);

INSERT INTO spell_effects (spell_id, effect_id, effect_chance) VALUES
(1, 1, 30);
