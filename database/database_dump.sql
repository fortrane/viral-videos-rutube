-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Sep 28, 2024 at 11:05 PM
-- Server version: 8.0.39-0ubuntu0.24.04.2
-- PHP Version: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `5_188_118_21`
--

-- --------------------------------------------------------

--
-- Table structure for table `rutube_videos`
--

CREATE TABLE `rutube_videos` (
  `id` int NOT NULL,
  `videoTitle` text CHARACTER SET utf16 COLLATE utf16_general_ci NOT NULL,
  `originalVideo` text NOT NULL,
  `video_json` mediumtext CHARACTER SET utf32 COLLATE utf32_general_ci,
  `metric_score` mediumtext CHARACTER SET utf32 COLLATE utf32_general_ci,
  `add_soap_video` text NOT NULL,
  `status` text NOT NULL,
  `created_at` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `rutube_videos`
--
ALTER TABLE `rutube_videos`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `rutube_videos`
--
ALTER TABLE `rutube_videos`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
