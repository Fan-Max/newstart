CREATE TABLE `tb_news_web` (
  `web_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_id` INT(11) NOT NULL,
  `web_title` varchar(500) DEFAULT NULL,
  `web_url` varchar(500) DEFAULT NULL,
  `image_url` varchar(500) DEFAULT NULL,
  `web_source` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`web_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

