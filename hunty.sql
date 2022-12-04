-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Dec 03, 2022 at 07:25 PM
-- Server version: 10.3.22-MariaDB-0+deb10u1
-- PHP Version: 7.3.14-1~deb10u1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hunty`
--

-- --------------------------------------------------------

--
-- Table structure for table `empresa`
--

CREATE TABLE `empresa` (
  `Id` int(11) NOT NULL,
  `Name` text NOT NULL,
  `City` text NOT NULL,
  `InternalCode` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `empresa`
--

INSERT INTO `empresa` (`Id`, `Name`, `City`, `InternalCode`) VALUES
(2, 'pandy systems', 'string', 5345643);

-- --------------------------------------------------------

--
-- Table structure for table `usuario`
--

CREATE TABLE `usuario` (
  `Id` int(11) NOT NULL,
  `UserId` int(11) NOT NULL,
  `FirstName` text NOT NULL,
  `LastName` text NOT NULL,
  `Email` text NOT NULL,
  `YearsPreviousExperience` int(11) NOT NULL,
  `Skills` text NOT NULL,
  `InternalCode` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `usuario`
--

INSERT INTO `usuario` (`Id`, `UserId`, `FirstName`, `LastName`, `Email`, `YearsPreviousExperience`, `Skills`, `InternalCode`) VALUES
(2, 0, 'string', 'string', 'string', 0, 'string', 0);

-- --------------------------------------------------------

--
-- Table structure for table `vacante`
--

CREATE TABLE `vacante` (
  `Id` int(11) NOT NULL,
  `PositionName` text NOT NULL,
  `CompanyName` text NOT NULL,
  `Salary` int(11) NOT NULL,
  `Currency` text NOT NULL,
  `VacancyId` int(11) NOT NULL,
  `VacancyLink` text NOT NULL,
  `RequiredSkills` text NOT NULL,
  `YearsPreviousExperience` int(11) NOT NULL,
  `InternalCode` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vacante`
--

INSERT INTO `vacante` (`Id`, `PositionName`, `CompanyName`, `Salary`, `Currency`, `VacancyId`, `VacancyLink`, `RequiredSkills`, `YearsPreviousExperience`, `InternalCode`) VALUES
(5, 'lucas andres', '777410', 1, '1', 1, '1', '1', 0, 143),
(7, 'carpintero', 'tata tcs', 416, '1', 1, '1', '1', 0, 1634),
(8, 'string', 'string', 0, 'string', 0, 'string', 'string', 0, 85),
(21, 'string', 'string', 0, 'string', 0, 'string', 'string', 0, 8),
(22, 'joven despierto', 'string', 0, 'string', 0, 'string', 'string', 0, 416),
(23, 'jairin', 'pcc', 0, 'string', 0, 'string', 'string', 0, 410),
(24, 'string', 'string', 0, 'string', 0, 'string', 'string', 0, 64),
(26, 'el mejor empleo', 'string', 0, 'string', 0, 'string', 'string', 0, 424333),
(27, 'el mejor de todos', 'string', 0, 'string', 0, 'string', 'moki', 34, 424333),
(28, 'string', 'string', 0, 'string', 0, 'string', 'string', 0, 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `empresa`
--
ALTER TABLE `empresa`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `vacante`
--
ALTER TABLE `vacante`
  ADD PRIMARY KEY (`Id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `empresa`
--
ALTER TABLE `empresa`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `usuario`
--
ALTER TABLE `usuario`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `vacante`
--
ALTER TABLE `vacante`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
