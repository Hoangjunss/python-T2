
DROP DATABASE IF EXISTS student_information_management;

CREATE DATABASE student_information_management;

USE student_information_management;

DROP TABLE IF EXISTS `attendances`;

CREATE TABLE `attendances` (
  `id` int NOT NULL,
  `student_id` int NOT NULL,
  `status` varchar(20) DEFAULT NULL,
  `checkin_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `department` (
  `id` int NOT NULL,
  `name` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `dean_id` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `faceendcoding` (
  `id` int NOT NULL,
  `student_id` int NOT NULL,
  `face_encoding` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

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

INSERT INTO `department` (id, name) VALUES (1,'Khoa Công Nghệ Thông Tin'),(2,'Khoa Kinh Tế'),(3,'Khoa Khoa Học Tự Nhiên');

INSERT INTO `teacher` VALUES (1,'Nguyễn Văn An','Nam','Active','Ba Vì, Hà Nội','an.nguyen@example.com','0987654321',1,'GV001','1'),
(2,'Trần Thị Bích','Nữ','Active','Hồ Chí Minh','bich.tran@example.com','0976543210',2,'GV002','1'),
(3,'Lê Minh Tuấn','Nam','Active','Đà Nẵng','tuan.le@example.com','0965432109',3,'GV003','1');

INSERT INTO `student` VALUES (1,'Phạm Văn Quang','Nam','Active','2008-05-10','2024-2025','Hà Nội','Kinh','Không','Việt Nam',1),
(2,'Lê Thị Hoa','Nữ','Active','2008-07-15','2024-2025','Hồ Chí Minh','Kinh1','Phật giáo','Việt Nam',2),
(3,'Ngô Văn Đức','Nam','Active','2007-03-20','2024-2025','Đà Nẵng','Kinh','Không','Việt Nam',3),
(4,'Trần Ngọc Minh','Nữ','Active','2007-09-05','2024-2025','Cần Thơ','Hoa','Công giáo','Việt Nam',1),
(10,'Nguyễn Quốc Khánh','Nam','Active','2004-08-09','2024-2025','An Giang','Kinh','Phật','Việt Nam',1),
(11,'Vũ Hoang Chung','Nam','Active','2004-08-09','2024-2025','TpHCM','Kinh','Không','Việt Nam',1);

---------------------------------------------------------------------------------

ALTER TABLE attendances 
 ADD CONSTRAINT `FK_Attendances_Student` FOREIGN KEY (`student_id`) REFERENCES `student` (`id`);

  ALTER TABLE faceendcoding 
 ADD CONSTRAINT `FK_FaceEndcoding_Student` FOREIGN KEY (`student_id`) REFERENCES `student` (`id`);
  ALTER TABLE student  
 ADD CONSTRAINT `FK_Student_Department` FOREIGN KEY (`departmentID`) REFERENCES `department` (`id`);

ALTER TABLE department
ADD CONSTRAINT `FK_Department_Dean` FOREIGN KEY (dean_id) REFERENCES teacher(id);