-- MySQL dump 10.13  Distrib 9.0.1, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: student_information_management
-- ------------------------------------------------------
-- Server version	9.0.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `attendances`
--

DROP TABLE IF EXISTS `attendances`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `attendances` (
  `id` int NOT NULL,
  `class_id` int NOT NULL,
  `student_id` int NOT NULL,
  `status` varchar(20) DEFAULT NULL,
  `checkin_time` datetime DEFAULT NULL,
  `scheduledetail_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_Attendances_Student` (`student_id`),
  KEY `FK_Attendances_Class` (`class_id`),
  KEY `FK_Attendances_ScheduleDetail` (`scheduledetail_id`),
  CONSTRAINT `FK_Attendances_Class` FOREIGN KEY (`class_id`) REFERENCES `class` (`id`),
  CONSTRAINT `FK_Attendances_ScheduleDetail` FOREIGN KEY (`scheduledetail_id`) REFERENCES `scheduledetail` (`id`),
  CONSTRAINT `FK_Attendances_Student` FOREIGN KEY (`student_id`) REFERENCES `student` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attendances`
--

/*!40000 ALTER TABLE `attendances` DISABLE KEYS */;
INSERT INTO `attendances` VALUES (1,1,2,'1','2025-03-27 23:18:11',1),(2,1,3,'1','2025-04-27 21:18:11',1),(3,1,2,'1','2025-04-27 23:30:11',1),(7484892,1,1,'1','2025-04-27 23:18:11',1),(135939576,1,2,'1','2025-04-27 23:33:27',1),(191484204,1,1,'1','2025-04-27 23:36:59',1),(224673922,1,1,'1','2025-04-27 23:33:38',1),(280301265,1,1,'1','2025-04-27 23:46:32',1),(419535750,1,1,'1','2025-04-27 23:37:17',1),(441023432,1,2,'1','2025-04-27 23:46:31',1);
/*!40000 ALTER TABLE `attendances` ENABLE KEYS */;

--
-- Table structure for table `class`
--

DROP TABLE IF EXISTS `class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `class` (
  `id` int NOT NULL,
  `name` varchar(50) NOT NULL,
  `grade_level` int DEFAULT NULL,
  `teacher_id` int DEFAULT NULL,
  `academic_year` varchar(20) DEFAULT NULL,
  `room` varchar(10) DEFAULT NULL,
  `total_student` int DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_Class_Teacher` (`teacher_id`),
  CONSTRAINT `FK_Class_Teacher` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `class`
--

/*!40000 ALTER TABLE `class` DISABLE KEYS */;
INSERT INTO `class` VALUES (1,'Class 10A1',10,1,'2024-2025','A101',40,'Lớp học Toán nâng cao'),(2,'Class 10A2',10,2,'2024-2025','A102',38,'Lớp học Văn nâng cao'),(3,'Class 11B1',11,3,'2024-2025','B201',35,'Lớp học Khoa học tự nhiên');
/*!40000 ALTER TABLE `class` ENABLE KEYS */;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `department` (
  `id` int NOT NULL,
  `name` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `dean_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_Department_Dean` (`dean_id`),
  CONSTRAINT `FK_Department_Dean` FOREIGN KEY (`dean_id`) REFERENCES `teacher` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

/*!40000 ALTER TABLE `department` DISABLE KEYS */;
INSERT INTO `department` VALUES (1,'Khoa Công Nghệ Thông Tin',1),(2,'Khoa Kinh Tế',2),(3,'Khoa Khoa Học Tự Nhiên',3),(999,'Test Department',1),(255956908,'!@#',NULL),(332875328,'KHOA KHTC',NULL),(437319290,'Khoa Toán',NULL),(495486334,'Khoa Bảo mật',NULL),(508509935,'Khoa Anh Văn',NULL),(530963326,'Khoanghệ thuật',NULL);
/*!40000 ALTER TABLE `department` ENABLE KEYS */;

--
-- Table structure for table `faceendcoding`
--

DROP TABLE IF EXISTS `faceendcoding`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `faceendcoding` (
  `id` int NOT NULL,
  `student_id` int NOT NULL,
  `face_encoding` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_FaceEndcoding_Student` (`student_id`),
  CONSTRAINT `FK_FaceEndcoding_Student` FOREIGN KEY (`student_id`) REFERENCES `student` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `faceendcoding`
--

/*!40000 ALTER TABLE `faceendcoding` DISABLE KEYS */;
/*!40000 ALTER TABLE `faceendcoding` ENABLE KEYS */;

--
-- Table structure for table `schedule`
--

DROP TABLE IF EXISTS `schedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `schedule` (
  `id` int NOT NULL,
  `departmentID` int NOT NULL,
  `semesterID` int NOT NULL,
  `description` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_Schedule_Department` (`departmentID`),
  KEY `FK_Schedule_Semester` (`semesterID`),
  CONSTRAINT `FK_Schedule_Department` FOREIGN KEY (`departmentID`) REFERENCES `department` (`id`),
  CONSTRAINT `FK_Schedule_Semester` FOREIGN KEY (`semesterID`) REFERENCES `semester` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schedule`
--

/*!40000 ALTER TABLE `schedule` DISABLE KEYS */;
INSERT INTO `schedule` VALUES (1,1,1,'Lịch học cho khoa Công Nghệ Thông Tin'),(2,2,1,'Lịch học cho khoa Kinh Tế'),(3,3,2,'Lịch học cho khoa Khoa Học Tự Nhiên'),(4,1,2,'Lịch học cho khoa Công Nghệ Thông Tin');
/*!40000 ALTER TABLE `schedule` ENABLE KEYS */;

--
-- Table structure for table `scheduledetail`
--

DROP TABLE IF EXISTS `scheduledetail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `scheduledetail` (
  `id` int NOT NULL,
  `scheduleID` int NOT NULL,
  `dayOfWeek` int NOT NULL,
  `startTime` time NOT NULL,
  `endTime` time NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_ScheduleDetail_Schedule` (`scheduleID`),
  CONSTRAINT `FK_ScheduleDetail_Schedule` FOREIGN KEY (`scheduleID`) REFERENCES `schedule` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scheduledetail`
--

/*!40000 ALTER TABLE `scheduledetail` DISABLE KEYS */;
INSERT INTO `scheduledetail` VALUES (1,1,2,'07:00:00','11:30:00'),(2,1,3,'13:00:00','17:30:00'),(4,1,5,'09:00:00','11:30:00'),(5,1,6,'15:00:00','17:30:00');
/*!40000 ALTER TABLE `scheduledetail` ENABLE KEYS */;

--
-- Table structure for table `semester`
--

DROP TABLE IF EXISTS `semester`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `semester` (
  `id` int NOT NULL,
  `name` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `startdate` date NOT NULL,
  `enddate` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `semester`
--

/*!40000 ALTER TABLE `semester` DISABLE KEYS */;
INSERT INTO `semester` VALUES (1,'Học Kỳ 1 - 2024','2024-08-01','2024-12-31'),(2,'Học Kỳ 2 - 2025','2025-01-15','2025-05-31'),(3,'Học Kỳ Hè - 2025','2025-06-01','2025-07-31');
/*!40000 ALTER TABLE `semester` ENABLE KEYS */;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `id` int NOT NULL,
  `fullname` varchar(100) NOT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `status` varchar(10) DEFAULT NULL,
  `dateOfBirth` date DEFAULT NULL,
  `academicYear` varchar(20) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `ethnicity` varchar(100) DEFAULT NULL,
  `religion` varchar(100) DEFAULT NULL,
  `nationality` varchar(100) DEFAULT NULL,
  `departmentID` int DEFAULT NULL,
  `class_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_Student_Department` (`departmentID`),
  KEY `fk_student_class` (`class_id`),
  CONSTRAINT `fk_student_class` FOREIGN KEY (`class_id`) REFERENCES `class` (`id`),
  CONSTRAINT `FK_Student_Department` FOREIGN KEY (`departmentID`) REFERENCES `department` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (1,'Phạm Văn Quang','Nam','Active','2008-05-10','2024-2025','Hà Nội','Kinh','Không','Việt Nam',1,1),(2,'Lê Thị Hoa','Nữ','Active','2008-07-15','2024-2025','Hồ Chí Minh','Kinh','Phật giáo','Việt Nam',2,1),(3,'Ngô Văn Đức','Nam','Active','2007-03-20','2024-2025','Đà Nẵng','Kinh','Không','Việt Nam',3,2),(4,'Trần Ngọc Minh','Nữ','Active','2007-09-05','2024-2025','Cần Thơ','Hoa','Công giáo','Việt Nam',1,3),(18560827,'1','Nữ',NULL,NULL,NULL,'1',NULL,NULL,NULL,1,1),(54907018,'1','Nam',NULL,NULL,NULL,'1',NULL,NULL,NULL,1,1),(134896600,'1','Nữ',NULL,NULL,NULL,'1',NULL,NULL,NULL,1,1),(202587046,'ghgh','Nam',NULL,NULL,'bnbn','ghghgh\n','bbnbn','jjhhj',NULL,1,1),(232230050,'ghgh','Nam',NULL,NULL,'bnbn','ghghgh','bbnbn','jjhhj',NULL,1,1),(505395069,'1','Nam',NULL,NULL,'1','1','1','1',NULL,1,1);
/*!40000 ALTER TABLE `student` ENABLE KEYS */;

--
-- Table structure for table `teacher`
--

DROP TABLE IF EXISTS `teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teacher` (
  `id` int NOT NULL,
  `fullname` varchar(100) NOT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `status` varchar(10) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone` varchar(10) DEFAULT NULL,
  `department_id` int DEFAULT NULL,
  `username` varchar(20) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher`
--

/*!40000 ALTER TABLE `teacher` DISABLE KEYS */;
INSERT INTO `teacher` VALUES (1,'Nguyễn Văn An','Nam','Active','Hà Nội','an.nguyen@example.com','0987654321',1,'GV001','1'),(2,'Trần Thị Bích','Nữ','Active','Hồ Chí Minh','bich.tran@example.com','0976543210',2,'GV002','1'),(3,'Lê Minh Tuấn','Nam','Active','Đà Nẵng','tuan.le@example.com','0965432109',3,'GV003','1');
/*!40000 ALTER TABLE `teacher` ENABLE KEYS */;

--
-- Dumping routines for database 'student_information_management'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-03 11:10:58
