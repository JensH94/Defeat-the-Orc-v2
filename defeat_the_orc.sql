-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Erstellungszeit: 26. Aug 2026 um 15:00
-- Server-Version: 10.4.32-MariaDB
-- PHP-Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Datenbank: `defeat_the_orc`
--
CREATE DATABASE IF NOT EXISTS `defeat_the_orc` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `defeat_the_orc`;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `armor`
--

DROP TABLE IF EXISTS `armor`;
CREATE TABLE `armor` (
  `armor_id` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `defense` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `armor`
--

INSERT INTO `armor` (`armor_id`, `name`, `defense`) VALUES
(1, 'Mage Cloth', 10),
(2, 'Barbarian Leather', 17);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `classes`
--

DROP TABLE IF EXISTS `classes`;
CREATE TABLE `classes` (
  `class_id` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `base_health` int(11) DEFAULT NULL,
  `base_initiative` int(11) DEFAULT NULL,
  `base_resource` int(11) DEFAULT NULL,
  `resource_type` varchar(30) DEFAULT NULL,
  `max_resource` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `classes`
--

INSERT INTO `classes` (`class_id`, `name`, `base_health`, `base_initiative`, `base_resource`, `resource_type`, `max_resource`) VALUES
(1, 'Mage', 20, 15, 100, 'mana', 100),
(2, 'Barbarian', 30, 13, 0, 'rage', 100);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `class_skills`
--

DROP TABLE IF EXISTS `class_skills`;
CREATE TABLE `class_skills` (
  `class_id` int(11) NOT NULL,
  `skill_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `class_skills`
--

INSERT INTO `class_skills` (`class_id`, `skill_id`) VALUES
(2, 1);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `class_spells`
--

DROP TABLE IF EXISTS `class_spells`;
CREATE TABLE `class_spells` (
  `class_id` int(11) NOT NULL,
  `spell_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `class_spells`
--

INSERT INTO `class_spells` (`class_id`, `spell_id`) VALUES
(1, 1);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `effects`
--

DROP TABLE IF EXISTS `effects`;
CREATE TABLE `effects` (
  `effects_id` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `min_damage` int(11) DEFAULT NULL,
  `max_damage` int(11) DEFAULT NULL,
  `duration` int(11) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `effects`
--

INSERT INTO `effects` (`effects_id`, `name`, `min_damage`, `max_damage`, `duration`) VALUES
(1, 'Fire', 2, 4, 3),
(2, 'Bleed', 1, 5, 4);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `enemies`
--

DROP TABLE IF EXISTS `enemies`;
CREATE TABLE `enemies` (
  `enemy_id` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `base_health` int(11) DEFAULT NULL,
  `base_mana` int(11) DEFAULT NULL,
  `base_initiative` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `enemies`
--

INSERT INTO `enemies` (`enemy_id`, `name`, `base_health`, `base_mana`, `base_initiative`) VALUES
(1, 'Rat', 15, 0, 12),
(2, 'Slime', 15, 0, 10);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `items`
--

DROP TABLE IF EXISTS `items`;
CREATE TABLE `items` (
  `item_id` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `min_damage` int(11) DEFAULT NULL,
  `max_damage` int(11) DEFAULT NULL,
  `min_heal` int(11) DEFAULT NULL,
  `max_heal` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `items`
--

INSERT INTO `items` (`item_id`, `name`, `min_damage`, `max_damage`, `min_heal`, `max_heal`) VALUES
(1, 'Small Bomb', 2, 6, 0, 0),
(2, 'Small Health Potion', 0, 0, 2, 6);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `skills`
--

DROP TABLE IF EXISTS `skills`;
CREATE TABLE `skills` (
  `skill_id` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `min_damage` int(11) DEFAULT NULL,
  `max_damage` int(11) DEFAULT NULL,
  `resource_cost` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `skills`
--

INSERT INTO `skills` (`skill_id`, `name`, `min_damage`, `max_damage`, `resource_cost`) VALUES
(1, 'Wounding Strike', 2, 6, 10);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `spells`
--

DROP TABLE IF EXISTS `spells`;
CREATE TABLE `spells` (
  `spell_id` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `min_damage` int(11) DEFAULT NULL,
  `max_damage` int(11) DEFAULT NULL,
  `resource_cost` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `spells`
--

INSERT INTO `spells` (`spell_id`, `name`, `min_damage`, `max_damage`, `resource_cost`) VALUES
(1, 'Fireball', 3, 9, 12);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `weapons`
--

DROP TABLE IF EXISTS `weapons`;
CREATE TABLE `weapons` (
  `weapon_id` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `min_damage` int(11) DEFAULT NULL,
  `max_damage` int(11) DEFAULT NULL,
  `crit_chance` int(11) DEFAULT NULL,
  `hit_chance` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `weapons`
--

INSERT INTO `weapons` (`weapon_id`, `name`, `min_damage`, `max_damage`, `crit_chance`, `hit_chance`) VALUES
(1, 'Axe', 3, 10, 0, 0),
(2, 'Staff', 1, 6, 0, 0);

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `armor`
--
ALTER TABLE `armor`
  ADD PRIMARY KEY (`armor_id`);

--
-- Indizes für die Tabelle `classes`
--
ALTER TABLE `classes`
  ADD PRIMARY KEY (`class_id`);

--
-- Indizes für die Tabelle `class_skills`
--
ALTER TABLE `class_skills`
  ADD PRIMARY KEY (`class_id`,`skill_id`),
  ADD KEY `skill_id` (`skill_id`);

--
-- Indizes für die Tabelle `class_spells`
--
ALTER TABLE `class_spells`
  ADD PRIMARY KEY (`class_id`,`spell_id`),
  ADD KEY `spell_id` (`spell_id`);

--
-- Indizes für die Tabelle `effects`
--
ALTER TABLE `effects`
  ADD PRIMARY KEY (`effects_id`);

--
-- Indizes für die Tabelle `enemies`
--
ALTER TABLE `enemies`
  ADD PRIMARY KEY (`enemy_id`);

--
-- Indizes für die Tabelle `items`
--
ALTER TABLE `items`
  ADD PRIMARY KEY (`item_id`);

--
-- Indizes für die Tabelle `skills`
--
ALTER TABLE `skills`
  ADD PRIMARY KEY (`skill_id`);

--
-- Indizes für die Tabelle `spells`
--
ALTER TABLE `spells`
  ADD PRIMARY KEY (`spell_id`);

--
-- Indizes für die Tabelle `weapons`
--
ALTER TABLE `weapons`
  ADD PRIMARY KEY (`weapon_id`);

--
-- AUTO_INCREMENT für exportierte Tabellen
--

--
-- AUTO_INCREMENT für Tabelle `armor`
--
ALTER TABLE `armor`
  MODIFY `armor_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT für Tabelle `classes`
--
ALTER TABLE `classes`
  MODIFY `class_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT für Tabelle `effects`
--
ALTER TABLE `effects`
  MODIFY `effects_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT für Tabelle `enemies`
--
ALTER TABLE `enemies`
  MODIFY `enemy_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT für Tabelle `items`
--
ALTER TABLE `items`
  MODIFY `item_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT für Tabelle `skills`
--
ALTER TABLE `skills`
  MODIFY `skill_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT für Tabelle `spells`
--
ALTER TABLE `spells`
  MODIFY `spell_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT für Tabelle `weapons`
--
ALTER TABLE `weapons`
  MODIFY `weapon_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints der exportierten Tabellen
--

--
-- Constraints der Tabelle `class_skills`
--
ALTER TABLE `class_skills`
  ADD CONSTRAINT `class_skills_ibfk_1` FOREIGN KEY (`class_id`) REFERENCES `classes` (`class_id`),
  ADD CONSTRAINT `class_skills_ibfk_2` FOREIGN KEY (`skill_id`) REFERENCES `skills` (`skill_id`);

--
-- Constraints der Tabelle `class_spells`
--
ALTER TABLE `class_spells`
  ADD CONSTRAINT `class_spells_ibfk_1` FOREIGN KEY (`class_id`) REFERENCES `classes` (`class_id`),
  ADD CONSTRAINT `class_spells_ibfk_2` FOREIGN KEY (`spell_id`) REFERENCES `spells` (`spell_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
