-- Active: 1704807633484@@127.0.0.1@3306@student_information_management
DROP DATABASE student_information_management;

CREATE DATABASE student_information_management
    DEFAULT CHARACTER SET = 'utf8mb4';

USE student_information_management;

-- Bảng Student
CREATE TABLE `Student` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `fullname` VARCHAR(100) NOT NULL,
  `gender` VARCHAR(10),
  `status` VARCHAR(10),
  `dateOfBirth` DATE,
  `academicYear` VARCHAR(20),
  `address` VARCHAR(255),
  `ethnicity` VARCHAR(100),
  `religion` VARCHAR(100),
  `nationality` VARCHAR(100),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `FaceEndcoding`(
  `id` INT NOT NULL AUTO_INCREMENT,
  `student_id` INT NOT NULL,
  `face_encoding` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_student_id` (`student_id`)
)


-- Bảng Subject
CREATE TABLE `Subject` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NOT NULL,
  `numberOfLessons` INT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `TEACHER` (
       `id` INT NOT NULL AUTO_INCREMENT,
      `class_id` INT NOT NULL,
      `fullname` VARCHAR(100) NOT NULL,
      `gender` VARCHAR(10),
      `status` VARCHAR(10),
      `dateOfBirth` DATE,
      PRIMARY KEY (`id`)
)

DROP Table class

DROP TABLE Attendances

-- Bảng Class
CREATE TABLE `Class` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50) NOT NULL,
  `grade_level` INT,
  `teacher_id` INT,
  `academic_year` VARCHAR(20),
  `room` VARCHAR(10),
  `total_student` INT,
  `description` VARCHAR(255),
  PRIMARY KEY (`id`),
    CONSTRAINT `fk_class_teacher`
    FOREIGN KEY (`id`) REFERENCES `Teacher` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- Bảng Attendances
CREATE TABLE `Attendances` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `class_id` INT NOT NULL,
  `student_id` INT NOT NULL,
  `status` VARCHAR(20),
  `checkin_time` DATETIME,
  PRIMARY KEY (`id`),
  KEY `idx_class_id` (`class_id`),
  KEY `idx_student_id` (`student_id`),
  CONSTRAINT `fk_rollcall_class`
    FOREIGN KEY (`class_id`) REFERENCES `Class` (`id`),
  CONSTRAINT `fk_rollcall_student`
    FOREIGN KEY (`student_id`) REFERENCES `Student` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Bảng score
CREATE TABLE `score` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `student_id` INT NOT NULL,
  `subject_id` INT NOT NULL,
  `score` DECIMAL(5,2),
  PRIMARY KEY (`id`),
  KEY `idx_student_id` (`student_id`),
  KEY `idx_subject_id` (`subject_id`),
  CONSTRAINT `fk_score_student`
    FOREIGN KEY (`student_id`) REFERENCES `Student` (`id`),
  CONSTRAINT `fk_score_subject`
    FOREIGN KEY (`subject_id`) REFERENCES `Subject` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

