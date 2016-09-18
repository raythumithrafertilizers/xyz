-- MySQL dump 10.13  Distrib 5.5.49, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: kranthiagro
-- ------------------------------------------------------
-- Server version	5.5.49-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Admin_advancedetails`
--

DROP TABLE IF EXISTS `Admin_advancedetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Admin_advancedetails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `amount` double NOT NULL,
  `paid_date` date NOT NULL,
  `interest_rate` double NOT NULL,
  `purchase_id` int(11) NOT NULL,
  `interest_money` double NOT NULL,
  `remarks` longtext NOT NULL,
  `isCleared` tinyint(1) NOT NULL,
  `cleared_date` date DEFAULT NULL,
  `paid_details_id` int(11) NOT NULL,
  `bill_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Admin_advancedetails`
--

LOCK TABLES `Admin_advancedetails` WRITE;
/*!40000 ALTER TABLE `Admin_advancedetails` DISABLE KEYS */;
INSERT INTO `Admin_advancedetails` VALUES (1,1000,'2016-09-14',0,1,0,'',0,NULL,0,0),(3,1000,'2016-09-10',0,3,0,'',0,NULL,0,0),(4,2000,'2016-09-07',0,4,0,'',0,NULL,0,0),(5,3000,'2016-09-21',0,5,0,'',0,NULL,0,0),(7,1000,'2016-11-11',0,0,0,'kranathi paid to farmer 1000',0,NULL,0,0),(8,-2000,'2016-02-28',0,0,0,'farmer paid to kranthi',0,NULL,0,0),(9,-900,'2016-02-28',0,0,0,'farmer paid to kranthi',0,NULL,0,0),(10,2000,'2016-02-11',0,0,0,'paid by kranthi to harvester',0,NULL,0,0),(11,-3000,'2016-02-11',0,0,0,'harvester paid to karnathi',0,NULL,0,0),(12,1,'2016-09-13',0,9,0,'',0,NULL,0,0),(13,-200,'2016-09-08',0,0,0,'',0,NULL,0,1),(14,200,'2016-11-11',0,0,0,'kranthi paid to customer',0,NULL,0,0),(15,-300,'2016-11-11',0,0,0,'customer paid to kranthi',0,NULL,0,0),(16,-43,'2016-09-17',0,0,0,'',0,NULL,0,2),(17,222,'2016-09-13',0,10,0,'',0,NULL,0,0);
/*!40000 ALTER TABLE `Admin_advancedetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Admin_appendstockdetails`
--

DROP TABLE IF EXISTS `Admin_appendstockdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Admin_appendstockdetails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_date` date DEFAULT NULL,
  `append_count` double NOT NULL,
  `remarks` longtext NOT NULL,
  `stock_id` int(11) NOT NULL,
  `total_stock` double NOT NULL,
  `sold_stock_id` int(11) NOT NULL,
  `manual_create_or_append_stock_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Admin_appendst_stock_id_61c4ceae1e642f9_fk_Admin_stockdetails_id` (`stock_id`),
  CONSTRAINT `Admin_appendst_stock_id_61c4ceae1e642f9_fk_Admin_stockdetails_id` FOREIGN KEY (`stock_id`) REFERENCES `Admin_stockdetails` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Admin_appendstockdetails`
--

LOCK TABLES `Admin_appendstockdetails` WRITE;
/*!40000 ALTER TABLE `Admin_appendstockdetails` DISABLE KEYS */;
INSERT INTO `Admin_appendstockdetails` VALUES (1,'2016-09-13',100,'adding 100 to sugar cane',1,0,0,1),(2,'2016-09-15',100,'appending 100 to sugar cane',1,0,0,1),(3,'2016-09-15',100,'appending 100 to sugar cane',3,0,0,3),(4,'2016-09-15',100,'appending 100 to bhajra 13kg',6,0,0,6),(5,'2016-09-13',345,'',1,512,10,0);
/*!40000 ALTER TABLE `Admin_appendstockdetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Admin_billing`
--

DROP TABLE IF EXISTS `Admin_billing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Admin_billing` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `total_price` double DEFAULT NULL,
  `total_paid` double DEFAULT NULL,
  `due` double DEFAULT NULL,
  `total_quantity` double DEFAULT NULL,
  `bill_date` date NOT NULL,
  `description` longtext NOT NULL,
  `month` varchar(100) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `vat_money` double NOT NULL,
  `vat_percentage` double NOT NULL,
  `contact_number` longtext NOT NULL,
  `remarks` longtext NOT NULL,
  `vehicle_number` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Admin_billing_customer_id_420e29b3e36e9f7e_fk_Admin_person_id` (`customer_id`),
  CONSTRAINT `Admin_billing_customer_id_420e29b3e36e9f7e_fk_Admin_person_id` FOREIGN KEY (`customer_id`) REFERENCES `Admin_person` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Admin_billing`
--

LOCK TABLES `Admin_billing` WRITE;
/*!40000 ALTER TABLE `Admin_billing` DISABLE KEYS */;
INSERT INTO `Admin_billing` VALUES (1,333,200,133,30,'2016-09-08','','September',7,0,0,'','',''),(2,1300,43,1257,68,'2016-09-17','','September',8,0,0,'','','');
/*!40000 ALTER TABLE `Admin_billing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Admin_billing_products_list`
--

DROP TABLE IF EXISTS `Admin_billing_products_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Admin_billing_products_list` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `billing_id` int(11) NOT NULL,
  `productslist_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `billing_id` (`billing_id`,`productslist_id`),
  KEY `Admin__productslist_id_5a788b3b752d5a2a_fk_Admin_productslist_id` (`productslist_id`),
  CONSTRAINT `Admin_billing_pr_billing_id_32ac7e3c8c985710_fk_Admin_billing_id` FOREIGN KEY (`billing_id`) REFERENCES `Admin_billing` (`id`),
  CONSTRAINT `Admin__productslist_id_5a788b3b752d5a2a_fk_Admin_productslist_id` FOREIGN KEY (`productslist_id`) REFERENCES `Admin_productslist` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Admin_billing_products_list`
--

LOCK TABLES `Admin_billing_products_list` WRITE;
/*!40000 ALTER TABLE `Admin_billing_products_list` DISABLE KEYS */;
INSERT INTO `Admin_billing_products_list` VALUES (1,1,1),(2,1,2),(3,2,3),(4,2,4);
/*!40000 ALTER TABLE `Admin_billing_products_list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Admin_expenditures`
--

DROP TABLE IF EXISTS `Admin_expenditures`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Admin_expenditures` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `amount` double NOT NULL,
  `create_date` date NOT NULL,
  `remarks` longtext NOT NULL,
  `type` longtext NOT NULL,
  `isActive` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Admin_expenditures`
--

LOCK TABLES `Admin_expenditures` WRITE;
/*!40000 ALTER TABLE `Admin_expenditures` DISABLE KEYS */;
INSERT INTO `Admin_expenditures` VALUES (1,200,'2016-09-22','erew','personal',1),(2,2000,'2016-09-22','erew','industrial',1),(3,20000,'2016-09-22','erew','industrial',1),(4,2000,'2016-09-22','erew','personal',1);
/*!40000 ALTER TABLE `Admin_expenditures` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Admin_person`
--

DROP TABLE IF EXISTS `Admin_person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Admin_person` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(400) NOT NULL,
  `created_date` datetime DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `person_type` varchar(200) NOT NULL,
  `isActive` tinyint(1) NOT NULL,
  `address` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Admin_person`
--

LOCK TABLES `Admin_person` WRITE;
/*!40000 ALTER TABLE `Admin_person` DISABLE KEYS */;
INSERT INTO `Admin_person` VALUES (1,'f1','2016-09-17 06:25:18','','farmer',1,''),(2,'f2','2016-09-17 06:25:32','','farmer',1,''),(3,'f3','2016-09-17 06:25:39','','farmer',1,''),(4,'h1','2016-09-17 06:25:53','','harvester',1,''),(5,'h2','2016-09-17 06:26:55','','harvester',1,''),(6,'h3','2016-09-17 06:27:02','','harvester',1,''),(7,'c1','2016-09-17 06:33:57','9877655447','customer',1,'ltr'),(8,'c2','2016-09-17 06:34:19','','customer',1,'ltr'),(9,'yashki lakshmi narayana','2016-09-17 06:35:00','8532456787','farmer',1,'tmd');
/*!40000 ALTER TABLE `Admin_person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Admin_person_advance_details`
--

DROP TABLE IF EXISTS `Admin_person_advance_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Admin_person_advance_details` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `person_id` int(11) NOT NULL,
  `advancedetails_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `person_id` (`person_id`,`advancedetails_id`),
  KEY `Adm_advancedetails_id_ff5f45419bb0355_fk_Admin_advancedetails_id` (`advancedetails_id`),
  CONSTRAINT `Admin_person_advanc_person_id_e0d4bd10475dbb8_fk_Admin_person_id` FOREIGN KEY (`person_id`) REFERENCES `Admin_person` (`id`),
  CONSTRAINT `Adm_advancedetails_id_ff5f45419bb0355_fk_Admin_advancedetails_id` FOREIGN KEY (`advancedetails_id`) REFERENCES `Admin_advancedetails` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Admin_person_advance_details`
--

LOCK TABLES `Admin_person_advance_details` WRITE;
/*!40000 ALTER TABLE `Admin_person_advance_details` DISABLE KEYS */;
INSERT INTO `Admin_person_advance_details` VALUES (1,1,1),(3,1,3),(4,1,4),(7,1,7),(8,1,8),(9,1,9),(12,1,12),(17,1,17),(5,2,5),(10,4,10),(11,4,11),(13,7,13),(14,7,14),(15,7,15),(16,8,16);
/*!40000 ALTER TABLE `Admin_person_advance_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Admin_piadadvancedetails`
--

DROP TABLE IF EXISTS `Admin_piadadvancedetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Admin_piadadvancedetails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `amount` double NOT NULL,
  `farmer_paid_date` date NOT NULL,
  `interest_rate` double NOT NULL,
  `interest_money` double NOT NULL,
  `farmer_paid_amount` double NOT NULL,
  `final_total_with_interest` double NOT NULL,
  `remarks` longtext NOT NULL,
  `paid_farmer_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Admin_piadadvancedetails`
--

LOCK TABLES `Admin_piadadvancedetails` WRITE;
/*!40000 ALTER TABLE `Admin_piadadvancedetails` DISABLE KEYS */;
/*!40000 ALTER TABLE `Admin_piadadvancedetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Admin_productslist`
--

DROP TABLE IF EXISTS `Admin_productslist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Admin_productslist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `quantity` double DEFAULT NULL,
  `price` double DEFAULT NULL,
  `isReturned` tinyint(1) NOT NULL,
  `product_id` int(11) NOT NULL,
  `per_kg_price` double NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Admin_productslist_9bea82de` (`product_id`),
  CONSTRAINT `Admin_produ_product_id_568969cfa0d5d54a_fk_Admin_stockdetails_id` FOREIGN KEY (`product_id`) REFERENCES `Admin_stockdetails` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Admin_productslist`
--

LOCK TABLES `Admin_productslist` WRITE;
/*!40000 ALTER TABLE `Admin_productslist` DISABLE KEYS */;
INSERT INTO `Admin_productslist` VALUES (1,10,111,0,1,11),(2,20,222,0,3,11),(3,23,700,0,1,232),(4,45,600,0,3,345);
/*!40000 ALTER TABLE `Admin_productslist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Admin_soldstockdetails`
--

DROP TABLE IF EXISTS `Admin_soldstockdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Admin_soldstockdetails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `quantity` double NOT NULL,
  `quality` double NOT NULL,
  `farmer_rate_per_ton` double NOT NULL,
  `farmer_payment` double NOT NULL,
  `harvester_payment` double NOT NULL,
  `harvester_rate_per_ton` double NOT NULL,
  `created_date` date NOT NULL,
  `farmer_id` int(11) NOT NULL,
  `harvester_id` int(11) NOT NULL,
  `miscellaneous_detections` double NOT NULL,
  `remarks` longtext NOT NULL,
  `stock_object_id` int(11) DEFAULT NULL,
  `quantity_in_numbers` double NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Admin_soldstockdetails_588af010` (`stock_object_id`),
  KEY `Admin_soldstockdet_farmer_id_311ad1acf8bdf22b_fk_Admin_person_id` (`farmer_id`),
  KEY `Admin_soldstock_harvester_id_5716e8ab854b7af5_fk_Admin_person_id` (`harvester_id`),
  CONSTRAINT `Admin_soldstockdet_farmer_id_311ad1acf8bdf22b_fk_Admin_person_id` FOREIGN KEY (`farmer_id`) REFERENCES `Admin_person` (`id`),
  CONSTRAINT `Admin_soldstock_harvester_id_5716e8ab854b7af5_fk_Admin_person_id` FOREIGN KEY (`harvester_id`) REFERENCES `Admin_person` (`id`),
  CONSTRAINT `Admin_sol_stock_object_id_ca254216dfa0196_fk_Admin_stocknames_id` FOREIGN KEY (`stock_object_id`) REFERENCES `Admin_stocknames` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Admin_soldstockdetails`
--

LOCK TABLES `Admin_soldstockdetails` WRITE;
/*!40000 ALTER TABLE `Admin_soldstockdetails` DISABLE KEYS */;
INSERT INTO `Admin_soldstockdetails` VALUES (1,2.1,0,3000,6300,840,400,'2016-09-14',1,4,300,'',1,0),(2,2.5,0,3000,7500,1000,400,'2016-09-05',1,4,200,'',1,0),(3,3,0,3000,8900,0,0,'2016-09-10',1,1,100,'',1,0),(4,1,0,3000,3000,400,400,'2016-09-07',1,5,200,'',1,0),(5,3,0,3000,8000,0,0,'2016-09-21',2,2,1000,'',1,0),(6,2,0,3000,5800,0,0,'2016-09-21',1,1,200,'',1,0),(7,15,0,30000,445000,0,0,'2016-09-21',9,9,5000,'',1,0),(9,11,1,1,11,11,1,'2016-09-13',1,1,0,'',NULL,0),(10,1.2,1,11,10.2,0,0,'2016-09-13',1,1,3,'',1,345);
/*!40000 ALTER TABLE `Admin_soldstockdetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Admin_stockdetails`
--

DROP TABLE IF EXISTS `Admin_stockdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Admin_stockdetails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `inital_stock` double DEFAULT NULL,
  `available_stock` double NOT NULL,
  `create_date` date DEFAULT NULL,
  `month` varchar(100) NOT NULL,
  `remarks` longtext NOT NULL,
  `isActive` tinyint(1) NOT NULL,
  `item_name_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Admin_stockdetails_fd61a834` (`item_name_id`),
  CONSTRAINT `Admin_stock_item_name_id_608b13e482c6e72c_fk_Admin_stocknames_id` FOREIGN KEY (`item_name_id`) REFERENCES `Admin_stocknames` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Admin_stockdetails`
--

LOCK TABLES `Admin_stockdetails` WRITE;
/*!40000 ALTER TABLE `Admin_stockdetails` DISABLE KEYS */;
INSERT INTO `Admin_stockdetails` VALUES (1,0,512,'2016-09-30','','',1,1),(3,0,35,'2016-09-29','','',1,2),(6,NULL,100,NULL,'September','',1,3),(8,NULL,0,NULL,'','',1,4),(9,NULL,0,NULL,'September','',1,6);
/*!40000 ALTER TABLE `Admin_stockdetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Admin_stocknames`
--

DROP TABLE IF EXISTS `Admin_stocknames`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Admin_stocknames` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(500) NOT NULL,
  `isActive` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Admin_stocknames`
--

LOCK TABLES `Admin_stocknames` WRITE;
/*!40000 ALTER TABLE `Admin_stocknames` DISABLE KEYS */;
INSERT INTO `Admin_stocknames` VALUES (1,'Sugar cane',1),(2,'Bhajra 10kg',1),(3,'Bhajra 13kg',1),(4,'Lal dim 10kg',1),(5,'test_stock_name',1),(6,'test_stock_name2',1);
/*!40000 ALTER TABLE `Admin_stocknames` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BaseApp_token`
--

DROP TABLE IF EXISTS `BaseApp_token`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BaseApp_token` (
  `token` varchar(200) NOT NULL,
  `created` datetime NOT NULL,
  `token_type` int(11) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `token` (`token`),
  KEY `BaseApp_token_user_id_2486c818dbbfdd00_fk_auth_user_id` (`user_id`),
  CONSTRAINT `BaseApp_token_user_id_2486c818dbbfdd00_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BaseApp_token`
--

LOCK TABLES `BaseApp_token` WRITE;
/*!40000 ALTER TABLE `BaseApp_token` DISABLE KEYS */;
/*!40000 ALTER TABLE `BaseApp_token` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BaseApp_userdetails`
--

DROP TABLE IF EXISTS `BaseApp_userdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BaseApp_userdetails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `phone` varchar(25) NOT NULL,
  `activationCode` varchar(50) NOT NULL,
  `role` varchar(15) NOT NULL,
  `userKey_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `BaseApp_userdetails_userKey_id_146ff78428fe3628_fk_auth_user_id` (`userKey_id`),
  CONSTRAINT `BaseApp_userdetails_userKey_id_146ff78428fe3628_fk_auth_user_id` FOREIGN KEY (`userKey_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BaseApp_userdetails`
--

LOCK TABLES `BaseApp_userdetails` WRITE;
/*!40000 ALTER TABLE `BaseApp_userdetails` DISABLE KEYS */;
INSERT INTO `BaseApp_userdetails` VALUES (1,'','','admin',1);
/*!40000 ALTER TABLE `BaseApp_userdetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permission_group_id_689710a9a73b7457_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  CONSTRAINT `auth__content_type_id_508cf46651277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add token',7,'add_token'),(20,'Can change token',7,'change_token'),(21,'Can delete token',7,'delete_token'),(22,'Can add user details',8,'add_userdetails'),(23,'Can change user details',8,'change_userdetails'),(24,'Can delete user details',8,'delete_userdetails'),(25,'Can add cors model',9,'add_corsmodel'),(26,'Can change cors model',9,'change_corsmodel'),(27,'Can delete cors model',9,'delete_corsmodel'),(28,'Can add Token',10,'add_token'),(29,'Can change Token',10,'change_token'),(30,'Can delete Token',10,'delete_token'),(31,'Can add advance details',11,'add_advancedetails'),(32,'Can change advance details',11,'change_advancedetails'),(33,'Can delete advance details',11,'delete_advancedetails'),(34,'Can add piad advance details',12,'add_piadadvancedetails'),(35,'Can change piad advance details',12,'change_piadadvancedetails'),(36,'Can delete piad advance details',12,'delete_piadadvancedetails'),(37,'Can add expenditures',13,'add_expenditures'),(38,'Can change expenditures',13,'change_expenditures'),(39,'Can delete expenditures',13,'delete_expenditures'),(40,'Can add person',14,'add_person'),(41,'Can change person',14,'change_person'),(42,'Can delete person',14,'delete_person'),(43,'Can add stock names',15,'add_stocknames'),(44,'Can change stock names',15,'change_stocknames'),(45,'Can delete stock names',15,'delete_stocknames'),(46,'Can add sold stock details',16,'add_soldstockdetails'),(47,'Can change sold stock details',16,'change_soldstockdetails'),(48,'Can delete sold stock details',16,'delete_soldstockdetails'),(49,'Can add stock details',17,'add_stockdetails'),(50,'Can change stock details',17,'change_stockdetails'),(51,'Can delete stock details',17,'delete_stockdetails'),(52,'Can add append stock details',18,'add_appendstockdetails'),(53,'Can change append stock details',18,'change_appendstockdetails'),(54,'Can delete append stock details',18,'delete_appendstockdetails'),(55,'Can add products list',19,'add_productslist'),(56,'Can change products list',19,'change_productslist'),(57,'Can delete products list',19,'delete_productslist'),(58,'Can add billing',20,'add_billing'),(59,'Can change billing',20,'change_billing'),(60,'Can delete billing',20,'delete_billing');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$20000$H0w5RQGtPBn5$qEdZNDlwsLH5vlsuzLKnmA3STZKoeWymPPnO+PyBJO0=',NULL,0,'kranthi@example.com','','','kranthi@example.com',0,1,'2016-09-17 06:22:41');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_permissi_user_id_7f0938558328534a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authtoken_token`
--

DROP TABLE IF EXISTS `authtoken_token`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `authtoken_token_user_id_1d10c57f535fb363_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authtoken_token`
--

LOCK TABLES `authtoken_token` WRITE;
/*!40000 ALTER TABLE `authtoken_token` DISABLE KEYS */;
/*!40000 ALTER TABLE `authtoken_token` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `corsheaders_corsmodel`
--

DROP TABLE IF EXISTS `corsheaders_corsmodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `corsheaders_corsmodel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cors` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `corsheaders_corsmodel`
--

LOCK TABLES `corsheaders_corsmodel` WRITE;
/*!40000 ALTER TABLE `corsheaders_corsmodel` DISABLE KEYS */;
/*!40000 ALTER TABLE `corsheaders_corsmodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `djang_content_type_id_697914295151027a_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `djang_content_type_id_697914295151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_45f3b1d93ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (11,'Admin','advancedetails'),(18,'Admin','appendstockdetails'),(20,'Admin','billing'),(13,'Admin','expenditures'),(14,'Admin','person'),(12,'Admin','piadadvancedetails'),(19,'Admin','productslist'),(16,'Admin','soldstockdetails'),(17,'Admin','stockdetails'),(15,'Admin','stocknames'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(10,'authtoken','token'),(7,'BaseApp','token'),(8,'BaseApp','userdetails'),(5,'contenttypes','contenttype'),(9,'corsheaders','corsmodel'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'Admin','0001_initial','2016-09-17 06:21:40'),(2,'Admin','0002_auto_20160629_1024','2016-09-17 06:21:40'),(3,'Admin','0003_auto_20160706_1300','2016-09-17 06:21:40'),(4,'Admin','0004_soldstockdetails_common_advance','2016-09-17 06:21:40'),(5,'Admin','0005_soldstockdetails_common_payment','2016-09-17 06:21:40'),(6,'Admin','0006_advancedetails_interest_rate','2016-09-17 06:21:40'),(7,'Admin','0007_advancedetails_purchase_id','2016-09-17 06:21:41'),(8,'Admin','0008_advancedetails_interest_money','2016-09-17 06:21:41'),(9,'Admin','0009_billing_vat_percentage','2016-09-17 06:21:41'),(10,'Admin','0010_auto_20160730_0937','2016-09-17 06:21:41'),(11,'Admin','0011_auto_20160730_1026','2016-09-17 06:21:41'),(12,'Admin','0012_billing_remarks','2016-09-17 06:21:41'),(13,'Admin','0013_soldstockdetails_remarks','2016-09-17 06:21:41'),(14,'Admin','0014_auto_20160730_1304','2016-09-17 06:21:41'),(15,'Admin','0015_auto_20160730_1417','2016-09-17 06:21:41'),(16,'Admin','0016_auto_20160730_1418','2016-09-17 06:21:41'),(17,'Admin','0017_auto_20160730_1519','2016-09-17 06:21:41'),(18,'Admin','0018_auto_20160730_1529','2016-09-17 06:21:41'),(19,'Admin','0019_auto_20160731_0948','2016-09-17 06:21:41'),(20,'Admin','0020_auto_20160806_1436','2016-09-17 06:21:41'),(21,'Admin','0021_advancedetails_iscleared','2016-09-17 06:21:41'),(22,'Admin','0022_advancedetails_cleared_date','2016-09-17 06:21:41'),(23,'Admin','0023_person_paid_advance_details','2016-09-17 06:21:41'),(24,'Admin','0024_auto_20160806_1641','2016-09-17 06:21:41'),(25,'Admin','0025_auto_20160806_1711','2016-09-17 06:21:41'),(26,'Admin','0026_auto_20160806_1718','2016-09-17 06:21:42'),(27,'Admin','0027_piadadvancedetails_paid_farmer_id','2016-09-17 06:21:42'),(28,'Admin','0028_auto_20160806_1918','2016-09-17 06:21:42'),(29,'Admin','0029_appendstockdetails','2016-09-17 06:21:42'),(30,'Admin','0030_productslist_per_kg_price','2016-09-17 06:21:42'),(31,'Admin','0031_auto_20160807_1308','2016-09-17 06:21:42'),(32,'Admin','0032_expenditures_isactive','2016-09-17 06:21:42'),(33,'Admin','0033_auto_20160814_1044','2016-09-17 06:21:42'),(34,'Admin','0034_auto_20160814_1050','2016-09-17 06:21:42'),(35,'Admin','0035_appendstockdetails_total_stock','2016-09-17 06:21:42'),(36,'Admin','0036_appendstockdetails_sold_stock_id','2016-09-17 06:21:42'),(37,'Admin','0037_auto_20160901_1512','2016-09-17 06:21:42'),(38,'Admin','0038_auto_20160904_1053','2016-09-17 06:21:42'),(39,'Admin','0039_auto_20160904_1053','2016-09-17 06:21:42'),(40,'Admin','0040_auto_20160904_1604','2016-09-17 06:21:43'),(41,'Admin','0041_auto_20160905_0744','2016-09-17 06:21:43'),(42,'Admin','0042_auto_20160905_0928','2016-09-17 06:21:43'),(43,'Admin','0043_auto_20160905_0929','2016-09-17 06:21:43'),(44,'Admin','0044_auto_20160905_1907','2016-09-17 06:21:43'),(45,'Admin','0045_auto_20160909_2306','2016-09-17 06:21:43'),(46,'Admin','0046_auto_20160910_0802','2016-09-17 06:21:43'),(47,'Admin','0047_auto_20160911_1833','2016-09-17 06:21:43'),(48,'Admin','0048_auto_20160911_2019','2016-09-17 06:21:43'),(49,'Admin','0049_auto_20160914_0806','2016-09-17 06:21:44'),(50,'Admin','0050_auto_20160917_1151','2016-09-17 06:21:44'),(51,'contenttypes','0001_initial','2016-09-17 06:21:44'),(52,'auth','0001_initial','2016-09-17 06:21:44'),(53,'BaseApp','0001_initial','2016-09-17 06:21:44'),(54,'admin','0001_initial','2016-09-17 06:21:44'),(55,'contenttypes','0002_remove_content_type_name','2016-09-17 06:21:44'),(56,'auth','0002_alter_permission_name_max_length','2016-09-17 06:21:44'),(57,'auth','0003_alter_user_email_max_length','2016-09-17 06:21:44'),(58,'auth','0004_alter_user_username_opts','2016-09-17 06:21:44'),(59,'auth','0005_alter_user_last_login_null','2016-09-17 06:21:44'),(60,'auth','0006_require_contenttypes_0002','2016-09-17 06:21:44'),(61,'authtoken','0001_initial','2016-09-17 06:21:44'),(62,'authtoken','0002_auto_20160226_1747','2016-09-17 06:21:44'),(63,'sessions','0001_initial','2016-09-17 06:21:44');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('8mxwce7b3zbfm09dt06z8b2fas88pe8m','ODNkNWNmM2Y5NmVjY2Y4ZTA2YzYzNTkxOWQ0MmFmMjQ4NDNkY2YzNjp7InVzZXJfaWQiOjEsInJvbGUiOiJhZG1pbiJ9','2016-10-01 13:38:46'),('id45q1hpbqvh4tv0nct8sqxmpiygv1uo','ODNkNWNmM2Y5NmVjY2Y4ZTA2YzYzNTkxOWQ0MmFmMjQ4NDNkY2YzNjp7InVzZXJfaWQiOjEsInJvbGUiOiJhZG1pbiJ9','2016-10-01 06:25:01'),('wb6ht48q0i5xzwppeva5fd2fgxz3xai1','ODNkNWNmM2Y5NmVjY2Y4ZTA2YzYzNTkxOWQ0MmFmMjQ4NDNkY2YzNjp7InVzZXJfaWQiOjEsInJvbGUiOiJhZG1pbiJ9','2016-10-01 06:26:40');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-09-18 11:45:20
