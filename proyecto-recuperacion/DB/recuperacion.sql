/*
Navicat MySQL Data Transfer

Source Server         : concecion_local
Source Server Version : 50616
Source Host           : localhost:3306
Source Database       : recuperacion

Target Server Type    : MYSQL
Target Server Version : 50616
File Encoding         : 65001

Date: 2016-03-15 10:28:59
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for DOCUMENTO
-- ----------------------------
DROP TABLE IF EXISTS `DOCUMENTO`;
CREATE TABLE `DOCUMENTO` (
  `id_documento` int(255) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  KEY `id_documento` (`id_documento`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for TBDOCTER
-- ----------------------------
DROP TABLE IF EXISTS `TBDOCTER`;
CREATE TABLE `TBDOCTER` (
  `id_documento` int(255) DEFAULT NULL,
  `no_termino` varchar(1000) DEFAULT NULL,
  `nu_frecuencia` int(255) DEFAULT NULL,
  `nu_peso` decimal(65,10) DEFAULT NULL,
  `nu_pesnor` decimal(65,10) DEFAULT NULL,
  KEY `ddocumento` (`id_documento`),
  CONSTRAINT `ddocumento` FOREIGN KEY (`id_documento`) REFERENCES `DOCUMENTO` (`id_documento`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
