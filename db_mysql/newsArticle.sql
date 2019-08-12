CREATE TABLE `news_content` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `news_platform` varchar(45) DEFAULT NULL,
  `news_title` varchar(200) DEFAULT NULL,
  `news_top_image_url` varchar(200) DEFAULT NULL,
  `news_author` varchar(100) DEFAULT NULL,
  `news_image_list` varchar(2000) DEFAULT NULL,
  `news_videos` varchar(500) DEFAULT NULL,
  `news_text` text,
  `news_summary` varchar(1000) DEFAULT NULL,
  `news_keywords` varchar(500) DEFAULT NULL,
  `news_url` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=60 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
