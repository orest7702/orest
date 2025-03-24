-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1
-- Час створення: Бер 24 2025 р., 12:02
-- Версія сервера: 10.4.32-MariaDB
-- Версія PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База даних: `colleg_orest`
--

-- --------------------------------------------------------

--
-- Структура таблиці `specuality`
--

CREATE TABLE `specuality` (
  `faculty_name` varchar(255) DEFAULT NULL,
  `faculty_code` int(11) DEFAULT NULL,
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп даних таблиці `specuality`
--

INSERT INTO `specuality` (`faculty_name`, `faculty_code`, `id`) VALUES
('Компютерні Науки', 35, 15),
('Компютерна інженеріяfghn', 123, 16),
('fghnj', 23456, 18);

-- --------------------------------------------------------

--
-- Структура таблиці `student`
--

CREATE TABLE `student` (
  `id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `first_name` varchar(255) DEFAULT NULL,
  `person_number` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `reside_code` int(11) DEFAULT NULL,
  `name_settlement` varchar(255) DEFAULT NULL,
  `math_grade` int(11) DEFAULT NULL,
  `uk_language` int(11) DEFAULT NULL,
  `specuality_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Індекси збережених таблиць
--

--
-- Індекси таблиці `specuality`
--
ALTER TABLE `specuality`
  ADD PRIMARY KEY (`id`);

--
-- Індекси таблиці `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_specuality` (`specuality_id`);

--
-- AUTO_INCREMENT для збережених таблиць
--

--
-- AUTO_INCREMENT для таблиці `specuality`
--
ALTER TABLE `specuality`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT для таблиці `student`
--
ALTER TABLE `student`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- Обмеження зовнішнього ключа збережених таблиць
--

--
-- Обмеження зовнішнього ключа таблиці `student`
--
ALTER TABLE `student`
  ADD CONSTRAINT `fk_specuality` FOREIGN KEY (`specuality_id`) REFERENCES `specuality` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
