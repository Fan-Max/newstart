CREATE TABLE `tb_new_category`(
    `category_id` INT(11) NOT NULL AUTO_INCREMENT,
    `category_name` VARCHAR(20) DEFAULT NULL,
    `category_url` VARCHAR(500) DEFAULT NULL,
    PRIMARY KEY(`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

