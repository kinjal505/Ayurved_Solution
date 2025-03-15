-- phpMyAdmin SQL Dump
-- version 5.3.0-dev+20221125.2e001c186a
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 03, 2022 at 07:35 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ayurveda`
--

-- --------------------------------------------------------

--
-- Table structure for table `medicine`
--

CREATE TABLE `medicine` (
  `id` int(11) NOT NULL,
  `category` varchar(80) DEFAULT NULL,
  `problem` text DEFAULT NULL,
  `details` text DEFAULT NULL,
  `image` varchar(200) DEFAULT NULL,
  `link` varchar(300) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `medicine`
--

INSERT INTO `medicine` (`id`, `category`, `problem`, `details`, `image`, `link`) VALUES
(1, 'skin', 'pimples', 'Turmeric Turmeric has anti-inflammatory, antimicrobial, and antioxidant properties. The active component of turmeric is curcumin that may help treat many skin conditions (1). Applying turmeric to skin may help treat acne, acne scars, hyperpigmentation, and dull skin.  Note: If you have lighter skin, turmeric will stain it yellow.', 'turmeric1.jpg', 'https://www.youtube.com/watch?v=6_M2Pj7uYL4'),
(2, 'hair', 'hairfall', 'Method 1:  Cut off a fresh leaf from aloe vera plant. Wash the aloe vera leaf thoroughly Slit it to draw out the gel inside Apply this gel directly to your scalp. Leave it for an hour before rinsing your hair with a mild shampoo. Redo the process two to three times per week to have the best results', 'alovera1.jpg', 'https://www.youtube.com/watch?v=LrTfLphOfCA'),
(3, 'skin', 'oily skin', 'Aloe Vera Treatment. One of the best ayurvedic tips for oily skin is using Aloe Vera. Step 1: Extract the pulp from...', 'alovera.jpg', 'https://www.youtube.com/watch?v=w8WAXvVSxj8'),
(4, 'skin', 'dry skin', 'Neem Leaves: Neem is regarded as a sacred plant in India. It has multiple skin benefits. Neem fights the bacteria on your skin and keeps them pimple free. It also penetrates deep into the layers of your skin and cleanses the skin off any impurities that may have settled within. Neem also treats dry skin problems. Just take some neem leaves and grind them into a paste. Apply this on your face and let it rest until the paste dries. Wash it with clean water for a flawlessly glowing and soft skin.', 'neem.jpg', 'https://www.youtube.com/watch?v=H-dweqlx2hY'),
(5, 'hair', 'frizzy hair', 'bananaMash the banana until there are no lumps and to it add the honey and oil to form a smooth paste. Apply the mixture all over your scalp and hair, and leave it on for 20-25 minutes. Rinse thoroughly with shampoo and conditioner.', 'banana1.jpg', 'https://www.youtube.com/watch?v=HX5WbnmzWjc'),
(6, 'hair', 'dandruf', 'One of the greatest sources of vitamin C, amla can be used in the treatment of dandruff. If you’ve tried pretty much everything to cure dandruff, but it doesn’t seem to go away, try this ayurvedic treatment for dandruff to get rid of it. Here’s how to use amla for the treatment of dandruff.  How to use: In a bowl mix amla powder and ground tulsi leaves. To this, add some water to form a thick paste. Apply the mixture on your scalp and let it stay for 30 minutes. Wash with shampoo and lukewarm water.', 'amla.jpg', 'https://www.youtube.com/watch?v=PAvNi0kT0lk'),
(7, 'hai', 'hair growth', 'Try Reetha for healthy and shining hair. Sapindus Mukorossi is an important Ayurvedic medicinal herb that is used for strengthening hair and fair complexion. Reetha or Sapindus Mukorossi is found from temperate to tropical regions. Its dried fruit is used as shampoo and detergent.', 'ritha.jpg', 'https://www.youtube.com/watch?v=qs51klBSLPI'),
(8, 'skin', 'blackheads', 'Use Tomato Paste: The easiest option is applying tomatoes on the affected area. They have antiseptic ingredients ', 'tomato.jpg', 'https://www.youtube.com/watch?v=qOVfY5Zs_Xc'),
(9, 'skin', 'skin tan', 'Mix 1 tbsp of sandalwood powder with 1 tsp of sour curd and 1/2 tsp of honey. Blend it well and apply on face, hands and other tanned areas of the body. Leave it on for 1 hour and wash off with water. It not only adds a natural glow to the skin but also removes skin tan. Sandalwood Remedy for Anti-aging', 'sandle.jpg', 'https://www.youtube.com/watch?v=tHSIJzpDGzA'),
(10, 'hair', 'hair growth', 'a. Brahmi Bringaraj Taila – This oil is made of herbs and is one of the most effective Ayurvedic remedies for hair growth. It nourishes the root of the hair and reduces hair fall by preventing a dry scalp. It helps destress you and, also, helps prevents premature greying.', 'bringraj.jpg', 'https://www.youtube.com/watch?v=BZMzEHfJkmM');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `medicine`
--
ALTER TABLE `medicine`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
