--
-- Database: `dummy_database`
--

-- --------------------------------------------------------

--
-- Table structure for table `content`
--

CREATE TABLE `content` (
  `id` int(11) NOT NULL,
  `filename` varchar(13) COLLATE utf8_polish_ci NOT NULL,
  `category` varchar(49) COLLATE utf8_polish_ci NOT NULL,
  `category_slug` varchar(49) COLLATE utf8_polish_ci NOT NULL,
  `title` varchar(200) COLLATE utf8_polish_ci NOT NULL,
  `publishedby` varchar(10) COLLATE utf8_polish_ci NOT NULL,
  `createdby` varchar(20) COLLATE utf8_polish_ci NOT NULL,
  `publishedon` datetime NOT NULL,
  `modifiedby` varchar(10) COLLATE utf8_polish_ci NOT NULL,
  `modifiedon` datetime NOT NULL,
  `modifiedurl` varchar(19) COLLATE utf8_polish_ci NOT NULL,
  `article` text COLLATE utf8_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `list`
--

CREATE TABLE `list` (
  `id` int(11) NOT NULL,
  `filename` varchar(8) COLLATE utf8_polish_ci NOT NULL,
  `url` varchar(13) COLLATE utf8_polish_ci NOT NULL,
  `url_text` varchar(200) COLLATE utf8_polish_ci NOT NULL,
  `modifiedon` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `id` int(11) NOT NULL,
  `operation` varchar(29) COLLATE utf8_polish_ci NOT NULL,
  `title` varchar(452) COLLATE utf8_polish_ci NOT NULL,
  `section` varchar(49) COLLATE utf8_polish_ci NOT NULL,
  `modifiedby` varchar(15) COLLATE utf8_polish_ci NOT NULL,
  `modifiedon` datetime NOT NULL,
  `url` varchar(40) COLLATE utf8_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Indexes for dumped tables
--

ALTER TABLE `content`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `list`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `register`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

ALTER TABLE `content`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `list`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `register`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

