-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 08, 2024 at 01:03 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `prodganize`
--

-- --------------------------------------------------------

--
-- Table structure for table `accounts`
--

CREATE TABLE `accounts` (
  `Name` varchar(100) NOT NULL,
  `Age` int(4) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `accounts`
--

INSERT INTO `accounts` (`Name`, `Age`, `username`, `password`) VALUES
('janin anne', 19, 'jan123', '123');

-- --------------------------------------------------------

--
-- Table structure for table `patients`
--

CREATE TABLE `patients` (
  `pid` int(100) NOT NULL,
  `Last Name` varchar(100) NOT NULL,
  `First Name, MI` varchar(100) NOT NULL,
  `Age` int(4) NOT NULL,
  `Sex` varchar(10) NOT NULL,
  `Address` varchar(200) NOT NULL,
  `Ward #, Bed#` varchar(100) NOT NULL,
  `Health Record` varchar(3000) NOT NULL,
  `Status` varchar(20) NOT NULL DEFAULT 'Assisted',
  `Date Admitted` date DEFAULT NULL,
  `Date Discharged` date DEFAULT NULL,
  `Date Reffered` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `patients`
--

INSERT INTO `patients` (`pid`, `Last Name`, `First Name, MI`, `Age`, `Sex`, `Address`, `Ward #, Bed#`, `Health Record`, `Status`, `Date Admitted`, `Date Discharged`, `Date Reffered`) VALUES
(1, 'Silvias', 'Janin', 25, 'Female', 'Brgy.Sulanga', '', 'healthy,mild headache', 'Assisted', '2011-01-23', '2011-01-23', '2011-01-23'),
(56, 'Indencio', 'jun', 18, 'Female', 'Rizal St', '', 'check up', 'Assisted', '2011-01-23', '0000-00-00', '0000-00-00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accounts`
--
ALTER TABLE `accounts`
  ADD UNIQUE KEY `username` (`username`),
  ADD KEY `password_2` (`password`);

--
-- Indexes for table `patients`
--
ALTER TABLE `patients`
  ADD PRIMARY KEY (`pid`),
  ADD UNIQUE KEY `Patient's ID` (`pid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `patients`
--
ALTER TABLE `patients`
  MODIFY `pid` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
