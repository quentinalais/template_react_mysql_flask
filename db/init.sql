CREATE database Tracker;

USE Tracker;

CREATE TABLE `Project` (
  `idProject` int(11) NOT NULL,
  `P_name` varchar(45) DEFAULT NULL,
  `P_owner` varchar(45) DEFAULT NULL,
  `P_creation_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`idProject`)
) 