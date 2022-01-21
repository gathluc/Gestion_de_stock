/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 8.0.21 : Database - gestion_stock
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`gestion_stock` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `gestion_stock`;

/*Table structure for table `achat` */

DROP TABLE IF EXISTS `achat`;

CREATE TABLE `achat` (
  `Ref_His_Achat` int NOT NULL AUTO_INCREMENT,
  `Date_Achat` date NOT NULL,
  `Quant_Achat` int NOT NULL,
  `Ref_Client` int NOT NULL,
  `Ref_Mar` varchar(50) NOT NULL,
  PRIMARY KEY (`Ref_His_Achat`),
  KEY `ref_client_fk` (`Ref_Client`),
  KEY `Ref_Mar` (`Ref_Mar`),
  CONSTRAINT `achat_ibfk_1` FOREIGN KEY (`Ref_Mar`) REFERENCES `stock` (`Ref_Mar`),
  CONSTRAINT `ref_client_fk` FOREIGN KEY (`Ref_Client`) REFERENCES `client` (`Ref_Client`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

/*Data for the table `achat` */

insert  into `achat`(`Ref_His_Achat`,`Date_Achat`,`Quant_Achat`,`Ref_Client`,`Ref_Mar`) values (1,'2022-01-18',-50,1,'MO'),(2,'2022-01-20',-100,1,'JU'),(3,'2022-01-18',-100,1,'JU');

/*Table structure for table `admin` */

DROP TABLE IF EXISTS `admin`;

CREATE TABLE `admin` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `adminName` varchar(25) NOT NULL,
  `adminPassword` varchar(25) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

/*Data for the table `admin` */

insert  into `admin`(`ID`,`adminName`,`adminPassword`) values (1,'Tolotra','1234');

/*Table structure for table `approvi` */

DROP TABLE IF EXISTS `approvi`;

CREATE TABLE `approvi` (
  `Ref_His_Fourni` int NOT NULL AUTO_INCREMENT,
  `Date_Fourni` date NOT NULL,
  `Quant_Fourni` int NOT NULL,
  `Ref_Four` int NOT NULL,
  `Ref_Mar` varchar(10) NOT NULL,
  PRIMARY KEY (`Ref_His_Fourni`),
  KEY `Approvi_Stock0_FK` (`Ref_Mar`),
  KEY `Ref_Four` (`Ref_Four`),
  CONSTRAINT `approvi_ibfk_1` FOREIGN KEY (`Ref_Four`) REFERENCES `fournisseur` (`Ref_Four`),
  CONSTRAINT `Approvi_Stock0_FK` FOREIGN KEY (`Ref_Mar`) REFERENCES `stock` (`Ref_Mar`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

/*Data for the table `approvi` */

insert  into `approvi`(`Ref_His_Fourni`,`Date_Fourni`,`Quant_Fourni`,`Ref_Four`,`Ref_Mar`) values (4,'2021-11-04',20,1,'MA'),(5,'2021-11-07',75,2,'MO'),(6,'2021-11-03',100,2,'JU'),(7,'2022-01-01',125,1,'SD'),(8,'2021-12-27',10,1,'MJ'),(9,'2021-11-30',50,4,'MA'),(10,'2022-01-09',125,4,'MO'),(11,'2022-01-20',100,1,'JU'),(12,'2022-01-20',50,1,'JU'),(13,'2022-01-20',100,2,'CH');

/*Table structure for table `client` */

DROP TABLE IF EXISTS `client`;

CREATE TABLE `client` (
  `Ref_Client` int NOT NULL AUTO_INCREMENT,
  `Nom_Client` varchar(50) NOT NULL,
  `Address_Client` varchar(50) NOT NULL,
  `Tel_Client` int NOT NULL,
  `Email_Client` varchar(50) NOT NULL,
  PRIMARY KEY (`Ref_Client`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

/*Data for the table `client` */

insert  into `client`(`Ref_Client`,`Nom_Client`,`Address_Client`,`Tel_Client`,`Email_Client`) values (1,'rochel','12 bis Analakely',3333,'r@gmail.com');

/*Table structure for table `fournisseur` */

DROP TABLE IF EXISTS `fournisseur`;

CREATE TABLE `fournisseur` (
  `Ref_Four` int NOT NULL AUTO_INCREMENT,
  `Nom_Four` varchar(50) NOT NULL,
  `Adress_Four` varchar(50) NOT NULL,
  `Tel_Four` int NOT NULL,
  `Email` varchar(50) NOT NULL,
  PRIMARY KEY (`Ref_Four`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

/*Data for the table `fournisseur` */

insert  into `fournisseur`(`Ref_Four`,`Nom_Four`,`Adress_Four`,`Tel_Four`,`Email`) values (1,'tolotra','92 Bis FM',0,'t@gmail.com'),(2,'nisaina','95 ter fm',1111,'n@gmail.com'),(3,'syvio','427 Ankadifotsy',2222,'s@gmail.com'),(4,'babakoto','Ambohimanarina',316541244,'koto@gmail.com');

/*Table structure for table `stock` */

DROP TABLE IF EXISTS `stock`;

CREATE TABLE `stock` (
  `Ref_Mar` varchar(10) NOT NULL,
  `Marchandise` varchar(50) NOT NULL,
  `Quantite` int NOT NULL,
  PRIMARY KEY (`Ref_Mar`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `stock` */

insert  into `stock`(`Ref_Mar`,`Marchandise`,`Quantite`) values ('CH','Chaussette',100),('JU','Jus Naturel',175),('MA','Mouchoir',100),('MJ','Mouchoir',20),('MO','Montre',150),('SD','Sac à dos',15);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
