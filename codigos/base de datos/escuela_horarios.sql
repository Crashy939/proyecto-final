-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: escuela
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `horarios`
--

DROP TABLE IF EXISTS `horarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `horarios` (
  `id_horario` int NOT NULL AUTO_INCREMENT,
  `grupo_id` int DEFAULT NULL,
  `dia_semana` enum('Lunes','Martes','Miércoles','Jueves','Viernes') COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `hora_inicio` time DEFAULT NULL,
  `hora_fin` time DEFAULT NULL,
  `materia` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `duracion_en_horas` int DEFAULT NULL,
  PRIMARY KEY (`id_horario`),
  KEY `grupo_id` (`grupo_id`),
  CONSTRAINT `horarios_ibfk_1` FOREIGN KEY (`grupo_id`) REFERENCES `grupos` (`id_grupo`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `horarios`
--

LOCK TABLES `horarios` WRITE;
/*!40000 ALTER TABLE `horarios` DISABLE KEYS */;
INSERT INTO `horarios` VALUES (2,1,'Martes','10:00:00','12:00:00','Bases de Datos',2),(3,1,'Miércoles','08:00:00','10:00:00','Redes de Computadoras',2),(4,1,'Jueves','08:00:00','10:00:00','Sistemas Operativos',2),(5,1,'Viernes','10:00:00','12:00:00','Desarrollo Web',2),(6,1,'Lunes','08:00:00','10:00:00','Programación Avanzada',2),(7,1,'Lunes','10:00:00','12:00:00','Bases de Datos',2),(8,1,'Lunes','12:00:00','14:00:00','Redes de Computadoras',2),(9,1,'Martes','08:00:00','10:00:00','Programación Avanzada',2),(10,1,'Martes','10:00:00','11:00:00','Bases de Datos',1),(11,1,'Martes','11:00:00','13:00:00','Redes de Computadoras',2),(12,1,'Martes','13:00:00','14:00:00','Sistemas Operativos',1),(13,1,'Miércoles','08:00:00','10:00:00','Bases de Datos',2),(14,1,'Miércoles','10:00:00','11:00:00','Programación Avanzada',1),(15,1,'Miércoles','11:00:00','13:00:00','Desarrollo Web',2),(16,1,'Miércoles','13:00:00','14:00:00','Redes de Computadoras',1),(17,1,'Jueves','08:00:00','10:00:00','Redes de Computadoras',2),(18,1,'Jueves','10:00:00','11:00:00','Sistemas Operativos',1),(19,1,'Jueves','11:00:00','13:00:00','Programación Avanzada',2),(20,1,'Jueves','13:00:00','14:00:00','Bases de Datos',1),(21,1,'Viernes','08:00:00','10:00:00','Sistemas Operativos',2),(22,1,'Viernes','10:00:00','11:00:00','Desarrollo Web',1),(23,1,'Viernes','11:00:00','13:00:00','Programación Avanzada',2),(24,1,'Viernes','13:00:00','14:00:00','Redes de Computadoras',1);
/*!40000 ALTER TABLE `horarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-17 15:02:26
