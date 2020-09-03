CREATE TABLE `car` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `carid` varchar(512) DEFAULT NULL,
  `userid` varchar(512) DEFAULT NULL,
  `license` varchar(512) DEFAULT NULL,
  `totalvalue` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

LOCK TABLES `car` WRITE;
/*!40000 ALTER TABLE `car` DISABLE KEYS */;
INSERT INTO `car` VALUES (1,'car001','user001','京 N880066',400000),(2,'car002','user001','辽 A99999',1000000),(3,'car003','user004','京 P77766',300000);
/*!40000 ALTER TABLE `car` ENABLE KEYS */;
UNLOCK TABLES;

CREATE TABLE `pet` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `petid` varchar(512) DEFAULT NULL,
  `userid` varchar(512) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

LOCK TABLES `pet` WRITE;
/*!40000 ALTER TABLE `pet` DISABLE KEYS */;
INSERT INTO `pet` VALUES (1,'pet001','user002'),(2,'pet002','user003'),(3,'pet003','user004');
/*!40000 ALTER TABLE `pet` ENABLE KEYS */;
UNLOCK TABLES;

CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userid` varchar(512) DEFAULT NULL,
  `name` varchar(512) DEFAULT NULL,
  `gender` varchar(512) DEFAULT NULL,
  `age` varchar(512) DEFAULT NULL,
  `phone` varchar(512) DEFAULT NULL,
  `weixin` varchar(512) DEFAULT NULL,
  `income` int(11) DEFAULT NULL,
  `marry` varchar(512) DEFAULT NULL,
  `character` varchar(512) DEFAULT NULL,
  `vip` varchar(512) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'user001',NULL,'男',NULL,NULL,NULL,800000,NULL,NULL,'是'),(2,'user002',NULL,'女',NULL,NULL,NULL,300000,NULL,NULL,'否'),(3,'user003',NULL,'男',NULL,NULL,NULL,50000,NULL,NULL,'否'),(4,'user004',NULL,'男',NULL,NULL,NULL,600000,NULL,NULL,'否'),(5,'user005',NULL,'女',NULL,NULL,NULL,120000,NULL,NULL,'否');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

-- 1、列出所有车主拥有的宠物数量，按宠物数量由小到大排类，sql结果：
-- license, pet_count
-- '京 N880066', '0'
-- '辽 A99999', '0'
-- '京 P77766', '1'

select distinct c.license,  (select count(1) from pet as p where p.userid=c.userid) as pet_count from car as c;

-- 2、统计收入小于100000、大于100000的男性，女性的个数：
-- gender, lt100000_count, gt100000_count
-- '女', '0', '2'
-- '男', '1', '2'

select gender, sum(if(income<100000,1,0)) as lt100000_count, sum(if(income>100000,1,0)) as gt100000_count
from user group by gender;

-- 3、重新定义vip标准，收入超过200000，汽车总价值超过300000，更新系统数据：
update user as a left join
(select c.userid, sum(c.totalvalue) as car_total from car as c group by c.userid) b
on a.userid=b.userid
set vip=if(b.car_total>300000 and a.income>200000, "是", "否");


