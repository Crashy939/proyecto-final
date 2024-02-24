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
-- Table structure for table `asistencia`
--

DROP TABLE IF EXISTS `asistencia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `asistencia` (
  `id_asistencia` int NOT NULL AUTO_INCREMENT,
  `clase_id` int DEFAULT NULL,
  `grupo_id` int DEFAULT NULL,
  `alumno_id` int DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `hora` time DEFAULT NULL,
  `asistio` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id_asistencia`),
  KEY `clase_id` (`clase_id`),
  KEY `grupo_id` (`grupo_id`),
  KEY `alumno_id` (`alumno_id`),
  CONSTRAINT `asistencia_ibfk_1` FOREIGN KEY (`clase_id`) REFERENCES `horarios` (`id_horario`),
  CONSTRAINT `asistencia_ibfk_2` FOREIGN KEY (`grupo_id`) REFERENCES `grupos` (`id_grupo`),
  CONSTRAINT `asistencia_ibfk_3` FOREIGN KEY (`alumno_id`) REFERENCES `alumnos` (`id_alumno`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `asistencia`
--

LOCK TABLES `asistencia` WRITE;
/*!40000 ALTER TABLE `asistencia` DISABLE KEYS */;
INSERT INTO `asistencia` VALUES (7,2,1,1,'2024-02-05','08:00:00',1),(8,3,1,1,'2024-02-05','10:00:00',1),(9,4,1,1,'2024-02-05','12:00:00',0),(10,2,1,2,'2024-02-05','08:00:00',1),(11,3,1,2,'2024-02-05','10:00:00',1),(12,4,1,2,'2024-02-05','12:00:00',1),(13,2,1,3,'2024-02-05','08:00:00',1),(14,3,1,3,'2024-02-05','10:00:00',0),(15,4,1,3,'2024-02-05','12:00:00',1);
/*!40000 ALTER TABLE `asistencia` ENABLE KEYS */;
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
