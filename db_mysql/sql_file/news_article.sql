CREATE TABLE `tb_news_article` (
  `article_id` int(11) NOT NULL AUTO_INCREMENT,
  `web_id` int(11) NOT NULL,
  `article_title` varchar(200) DEFAULT NULL,
  `article_author` varchar(100) DEFAULT NULL,
  `article_videos` varchar(500) DEFAULT NULL,
  `article_top_image_url` varchar(200) DEFAULT NULL,
  `article_image_list` varchar(2000) DEFAULT NULL,
  `article_text` text,
  `article_summary` varchar(1000) DEFAULT NULL,
  `article_keywords` varchar(500) DEFAULT NULL,
  `article_url` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`article_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
