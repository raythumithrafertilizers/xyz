-- MySQL dump 10.13  Distrib 5.5.47, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: raythumithra
-- ------------------------------------------------------
-- Server version	5.5.47-0ubuntu0.14.04.1

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
  `bill_date` datetime NOT NULL,
  `description` longtext NOT NULL,
  `customer_id` int(11) NOT NULL,
  `month` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Admin_billing_cb24373b` (`customer_id`),
  CONSTRAINT `Admin_billing_customer_id_420e29b3e36e9f7e_fk_Admin_customers_id` FOREIGN KEY (`customer_id`) REFERENCES `Admin_customers` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Admin_billing`
--

LOCK TABLES `Admin_billing` WRITE;
/*!40000 ALTER TABLE `Admin_billing` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Admin_billing_products_list`
--

LOCK TABLES `Admin_billing_products_list` WRITE;
/*!40000 ALTER TABLE `Admin_billing_products_list` DISABLE KEYS */;
/*!40000 ALTER TABLE `Admin_billing_products_list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Admin_companybills`
--

DROP TABLE IF EXISTS `Admin_companybills`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Admin_companybills` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `company_name` varchar(300) NOT NULL,
  `company_invoice_number` varchar(300) NOT NULL,
  `bill_image` varchar(100) NOT NULL,
  `uploaded_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Admin_companybills`
--

LOCK TABLES `Admin_companybills` WRITE;
/*!40000 ALTER TABLE `Admin_companybills` DISABLE KEYS */;
/*!40000 ALTER TABLE `Admin_companybills` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Admin_customers`
--

DROP TABLE IF EXISTS `Admin_customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Admin_customers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(500) NOT NULL,
  `last_name` varchar(500) NOT NULL,
  `phone` varchar(30) NOT NULL,
  `address` longtext NOT NULL,
  `create_date` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Admin_customers`
--

LOCK TABLES `Admin_customers` WRITE;
/*!40000 ALTER TABLE `Admin_customers` DISABLE KEYS */;
/*!40000 ALTER TABLE `Admin_customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Admin_galleryimages`
--

DROP TABLE IF EXISTS `Admin_galleryimages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Admin_galleryimages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `gallery_image` varchar(100) NOT NULL,
  `uploaded_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Admin_galleryimages`
--

LOCK TABLES `Admin_galleryimages` WRITE;
/*!40000 ALTER TABLE `Admin_galleryimages` DISABLE KEYS */;
/*!40000 ALTER TABLE `Admin_galleryimages` ENABLE KEYS */;
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
  `product_id` int(11) NOT NULL,
  `isReturned` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Admin_productslist_9bea82de` (`product_id`),
  CONSTRAINT `Admin_produ_product_id_568969cfa0d5d54a_fk_Admin_stockdetails_id` FOREIGN KEY (`product_id`) REFERENCES `Admin_stockdetails` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Admin_productslist`
--

LOCK TABLES `Admin_productslist` WRITE;
/*!40000 ALTER TABLE `Admin_productslist` DISABLE KEYS */;
/*!40000 ALTER TABLE `Admin_productslist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Admin_quantity`
--

DROP TABLE IF EXISTS `Admin_quantity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Admin_quantity` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `quantity_name` varchar(500) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Admin_quantity`
--

LOCK TABLES `Admin_quantity` WRITE;
/*!40000 ALTER TABLE `Admin_quantity` DISABLE KEYS */;
/*!40000 ALTER TABLE `Admin_quantity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Admin_ratepertype`
--

DROP TABLE IF EXISTS `Admin_ratepertype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Admin_ratepertype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rate_per_type_name` varchar(500) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Admin_ratepertype`
--

LOCK TABLES `Admin_ratepertype` WRITE;
/*!40000 ALTER TABLE `Admin_ratepertype` DISABLE KEYS */;
/*!40000 ALTER TABLE `Admin_ratepertype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Admin_stockdetails`
--

DROP TABLE IF EXISTS `Admin_stockdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Admin_stockdetails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `item_name` varchar(500) NOT NULL,
  `item_type` varchar(100) NOT NULL,
  `item_batch_number` varchar(500) NOT NULL,
  `item_lot_number` varchar(500) NOT NULL,
  `expire_date` date NOT NULL,
  `mfg_date` date DEFAULT NULL,
  `purchase_form` longtext NOT NULL,
  `quantity_type` varchar(100) NOT NULL,
  `rate_per_type` varchar(100) NOT NULL,
  `item_cost` double DEFAULT NULL,
  `quantity_weight` double DEFAULT NULL,
  `available_stock` double NOT NULL,
  `create_date` datetime NOT NULL,
  `isLegal` varchar(100) NOT NULL,
  `month` varchar(100) NOT NULL,
  `seen` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Admin_stockdetails`
--

LOCK TABLES `Admin_stockdetails` WRITE;
/*!40000 ALTER TABLE `Admin_stockdetails` DISABLE KEYS */;
/*!40000 ALTER TABLE `Admin_stockdetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Admin_stocktype`
--

DROP TABLE IF EXISTS `Admin_stocktype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Admin_stocktype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type_name` varchar(500) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Admin_stocktype`
--

LOCK TABLES `Admin_stocktype` WRITE;
/*!40000 ALTER TABLE `Admin_stocktype` DISABLE KEYS */;
/*!40000 ALTER TABLE `Admin_stocktype` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BaseApp_token`
--

LOCK TABLES `BaseApp_token` WRITE;
/*!40000 ALTER TABLE `BaseApp_token` DISABLE KEYS */;
INSERT INTO `BaseApp_token` VALUES ('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE0NjE0OTA2NzgsInN1YiI6IjEiLCJleHAiOjE0NjMyMTg2Nzh9.ohS_q38qQU-HOP75EXKBUCLKo_Hkd58RHmoyvaNsF40','2016-04-24 04:07:58',1,1,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BaseApp_userdetails`
--

LOCK TABLES `BaseApp_userdetails` WRITE;
/*!40000 ALTER TABLE `BaseApp_userdetails` DISABLE KEYS */;
INSERT INTO `BaseApp_userdetails` VALUES (1,'353453453453','QWIUrzCiLAnpAtsQ','admin',1),(2,'44444444343','elPTWoKkuLhoKrNk','admin',2);
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
INSERT INTO `auth_permission` VALUES (4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add token',7,'add_token'),(20,'Can change token',7,'change_token'),(21,'Can delete token',7,'delete_token'),(22,'Can add user details',8,'add_userdetails'),(23,'Can change user details',8,'change_userdetails'),(24,'Can delete user details',8,'delete_userdetails'),(25,'Can add cors model',9,'add_corsmodel'),(26,'Can change cors model',9,'change_corsmodel'),(27,'Can delete cors model',9,'delete_corsmodel'),(28,'Can add token',10,'add_token'),(29,'Can change token',10,'change_token'),(30,'Can delete token',10,'delete_token'),(31,'Can add stock type',11,'add_stocktype'),(32,'Can change stock type',11,'change_stocktype'),(33,'Can delete stock type',11,'delete_stocktype'),(34,'Can add quantity',12,'add_quantity'),(35,'Can change quantity',12,'change_quantity'),(36,'Can delete quantity',12,'delete_quantity'),(37,'Can add rate per type',13,'add_ratepertype'),(38,'Can change rate per type',13,'change_ratepertype'),(39,'Can delete rate per type',13,'delete_ratepertype'),(40,'Can add stock details',14,'add_stockdetails'),(41,'Can change stock details',14,'change_stockdetails'),(42,'Can delete stock details',14,'delete_stockdetails'),(43,'Can add customers',15,'add_customers'),(44,'Can change customers',15,'change_customers'),(45,'Can delete customers',15,'delete_customers'),(46,'Can add products list',16,'add_productslist'),(47,'Can change products list',16,'change_productslist'),(48,'Can delete products list',16,'delete_productslist'),(49,'Can add billing',17,'add_billing'),(50,'Can change billing',17,'change_billing'),(51,'Can delete billing',17,'delete_billing'),(52,'Can add company bills',18,'add_companybills'),(53,'Can change company bills',18,'change_companybills'),(54,'Can delete company bills',18,'delete_companybills'),(55,'Can add gallery images',19,'add_galleryimages'),(56,'Can change gallery images',19,'change_galleryimages'),(57,'Can delete gallery images',19,'delete_galleryimages'),(58,'Can add cron job log',20,'add_cronjoblog'),(59,'Can change cron job log',20,'change_cronjoblog'),(60,'Can delete cron job log',20,'delete_cronjoblog');
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$20000$JYG95eWxqL02$P35mC3tjkh6H4h2avlbcKgvs+EBFWO2LgWzohJIfal0=',NULL,0,'satya@example.com','satya','satya','satya@example.com',0,1,'2016-04-24 04:03:58'),(2,'pbkdf2_sha256$20000$JGMnKlMd8idr$awwzCINpTFpshs4sqckIPYjWZa7j29cWYXHUlle7zfI=',NULL,0,'satya1@example.com','sfsd','fsf','satya1@example.com',0,1,'2016-04-24 04:07:28');
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
INSERT INTO `django_content_type` VALUES (17,'Admin','billing'),(18,'Admin','companybills'),(15,'Admin','customers'),(19,'Admin','galleryimages'),(16,'Admin','productslist'),(12,'Admin','quantity'),(13,'Admin','ratepertype'),(14,'Admin','stockdetails'),(11,'Admin','stocktype'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(10,'authtoken','token'),(7,'BaseApp','token'),(8,'BaseApp','userdetails'),(5,'contenttypes','contenttype'),(9,'corsheaders','corsmodel'),(20,'django_cron','cronjoblog'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_cron_cronjoblog`
--

DROP TABLE IF EXISTS `django_cron_cronjoblog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_cron_cronjoblog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(64) NOT NULL,
  `start_time` datetime NOT NULL,
  `end_time` datetime NOT NULL,
  `is_success` tinyint(1) NOT NULL,
  `message` longtext NOT NULL,
  `ran_at_time` time DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `django_cron_cronjoblog_code_754ef82e28dbbaf4_idx` (`code`,`is_success`,`ran_at_time`),
  KEY `django_cron_cronjoblog_code_633b08e9abde5764_idx` (`code`,`start_time`,`ran_at_time`),
  KEY `django_cron_cronjoblog_code_4e16f5a60e31a319_idx` (`code`,`start_time`),
  KEY `django_cron_cronjoblog_c1336794` (`code`),
  KEY `django_cron_cronjoblog_c4d98dbd` (`start_time`),
  KEY `django_cron_cronjoblog_305d2889` (`end_time`),
  KEY `django_cron_cronjoblog_a05e4b70` (`ran_at_time`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_cron_cronjoblog`
--

LOCK TABLES `django_cron_cronjoblog` WRITE;
/*!40000 ALTER TABLE `django_cron_cronjoblog` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_cron_cronjoblog` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2016-04-24 04:00:06'),(2,'auth','0001_initial','2016-04-24 04:00:09'),(3,'Admin','0001_initial','2016-04-24 04:00:17'),(4,'Admin','0002_auto_20160222_1726','2016-04-24 04:00:17'),(5,'Admin','0003_auto_20160222_1732','2016-04-24 04:00:18'),(6,'Admin','0004_auto_20160222_1735','2016-04-24 04:00:19'),(7,'Admin','0005_store_wise_stamp_offers_store_id','2016-04-24 04:00:20'),(8,'Admin','0006_auto_20160229_1741','2016-04-24 04:00:21'),(9,'Admin','0007_auto_20160320_1202','2016-04-24 04:00:33'),(10,'Admin','0008_auto_20160320_1230','2016-04-24 04:00:36'),(11,'Admin','0009_auto_20160320_1253','2016-04-24 04:00:40'),(12,'Admin','0010_auto_20160320_1453','2016-04-24 04:00:41'),(13,'Admin','0011_auto_20160320_1605','2016-04-24 04:00:42'),(14,'Admin','0012_auto_20160320_1606','2016-04-24 04:00:42'),(15,'Admin','0013_stockdetails_quantity_weight','2016-04-24 04:00:43'),(16,'Admin','0014_stockdetails_available_stock','2016-04-24 04:00:43'),(17,'Admin','0015_customers','2016-04-24 04:00:43'),(18,'Admin','0016_auto_20160323_1004','2016-04-24 04:00:46'),(19,'Admin','0017_billing_bill_date','2016-04-24 04:00:46'),(20,'Admin','0018_auto_20160323_1532','2016-04-24 04:00:47'),(21,'Admin','0019_auto_20160323_1533','2016-04-24 04:00:49'),(22,'Admin','0020_auto_20160323_1535','2016-04-24 04:00:50'),(23,'Admin','0021_auto_20160323_1720','2016-04-24 04:00:52'),(24,'Admin','0022_auto_20160323_1720','2016-04-24 04:00:58'),(25,'Admin','0023_auto_20160323_1720','2016-04-24 04:00:58'),(26,'Admin','0024_auto_20160326_2014','2016-04-24 04:00:59'),(27,'Admin','0025_auto_20160402_1638','2016-04-24 04:01:00'),(28,'Admin','0026_auto_20160404_1159','2016-04-24 04:01:01'),(29,'Admin','0027_auto_20160404_1352','2016-04-24 04:01:01'),(30,'Admin','0028_auto_20160404_1503','2016-04-24 04:01:02'),(31,'Admin','0029_auto_20160406_1635','2016-04-24 04:01:03'),(32,'Admin','0030_auto_20160407_1201','2016-04-24 04:01:04'),(33,'Admin','0031_auto_20160407_1202','2016-04-24 04:01:04'),(34,'Admin','0032_auto_20160407_1337','2016-04-24 04:01:05'),(35,'Admin','0033_auto_20160424_0930','2016-04-24 04:01:05'),(36,'BaseApp','0001_initial','2016-04-24 04:01:06'),(37,'BaseApp','0002_auto_20160320_1202','2016-04-24 04:01:07'),(38,'admin','0001_initial','2016-04-24 04:01:07'),(39,'contenttypes','0002_remove_content_type_name','2016-04-24 04:01:08'),(40,'auth','0002_alter_permission_name_max_length','2016-04-24 04:01:08'),(41,'auth','0003_alter_user_email_max_length','2016-04-24 04:01:09'),(42,'auth','0004_alter_user_username_opts','2016-04-24 04:01:09'),(43,'auth','0005_alter_user_last_login_null','2016-04-24 04:01:09'),(44,'auth','0006_require_contenttypes_0002','2016-04-24 04:01:09'),(45,'authtoken','0001_initial','2016-04-24 04:01:09'),(46,'django_cron','0001_initial','2016-04-24 04:01:11'),(47,'django_cron','0002_remove_max_length_from_CronJobLog_message','2016-04-24 04:01:11'),(48,'sessions','0001_initial','2016-04-24 04:01:11');
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

-- Dump completed on 2016-04-24 13:39:08
