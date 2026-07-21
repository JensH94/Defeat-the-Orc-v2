-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Erstellungszeit: 21. Jul 2026 um 18:59
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
CREATE TABLE IF NOT EXISTS `armor` (
  `armor_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `defense` int(11) DEFAULT NULL,
  PRIMARY KEY (`armor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
CREATE TABLE IF NOT EXISTS `classes` (
  `class_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `base_health` int(11) DEFAULT NULL,
  `base_mana` int(11) DEFAULT NULL,
  `base_initiative` int(11) DEFAULT NULL,
  PRIMARY KEY (`class_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `classes`
--

INSERT INTO `classes` (`class_id`, `name`, `base_health`, `base_mana`, `base_initiative`) VALUES
(1, 'Mage', 20, 40, 15),
(2, 'Barbarian', 30, 0, 13);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `effects`
--

DROP TABLE IF EXISTS `effects`;
CREATE TABLE IF NOT EXISTS `effects` (
  `effects_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `min_damage` int(11) DEFAULT NULL,
  `max_damage` int(11) DEFAULT NULL,
  PRIMARY KEY (`effects_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `effects`
--

INSERT INTO `effects` (`effects_id`, `name`, `min_damage`, `max_damage`) VALUES
(1, 'Fire', 2, 4),
(2, 'Bleed', 1, 5);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `enemies`
--

DROP TABLE IF EXISTS `enemies`;
CREATE TABLE IF NOT EXISTS `enemies` (
  `enemy_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `base_health` int(11) DEFAULT NULL,
  `base_mana` int(11) DEFAULT NULL,
  `base_initiative` int(11) DEFAULT NULL,
  PRIMARY KEY (`enemy_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
CREATE TABLE IF NOT EXISTS `items` (
  `item_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `min_damage` int(11) DEFAULT NULL,
  `max_damage` int(11) DEFAULT NULL,
  `min_heal` int(11) DEFAULT NULL,
  `max_heal` int(11) DEFAULT NULL,
  PRIMARY KEY (`item_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
CREATE TABLE IF NOT EXISTS `skills` (
  `skill_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `min_damage` int(11) DEFAULT NULL,
  `max_damage` int(11) DEFAULT NULL,
  PRIMARY KEY (`skill_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `skills`
--

INSERT INTO `skills` (`skill_id`, `name`, `min_damage`, `max_damage`) VALUES
(1, 'Wounding Strike', 2, 6);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `spells`
--

DROP TABLE IF EXISTS `spells`;
CREATE TABLE IF NOT EXISTS `spells` (
  `spell_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `min_damage` int(11) DEFAULT NULL,
  `max_damage` int(11) DEFAULT NULL,
  `mana_cost` int(11) DEFAULT NULL,
  PRIMARY KEY (`spell_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `spells`
--

INSERT INTO `spells` (`spell_id`, `name`, `min_damage`, `max_damage`, `mana_cost`) VALUES
(1, 'Fireball', 3, 9, 7);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `weapons`
--

DROP TABLE IF EXISTS `weapons`;
CREATE TABLE IF NOT EXISTS `weapons` (
  `weapon_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `min_damage` int(11) DEFAULT NULL,
  `max_damage` int(11) DEFAULT NULL,
  `crit_chance` int(11) DEFAULT NULL,
  `hit_chance` int(11) DEFAULT NULL,
  PRIMARY KEY (`weapon_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `weapons`
--

INSERT INTO `weapons` (`weapon_id`, `name`, `min_damage`, `max_damage`, `crit_chance`, `hit_chance`) VALUES
(1, 'Axe', 3, 10, 0, 0),
(2, 'Staff', 1, 6, 0, 0);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
