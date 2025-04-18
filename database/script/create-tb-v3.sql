-- Active: 1704807633484@@127.0.0.1@3306@student_information_management
-- Active: 1742819810405@@127.0.0.1@1521@SYSTEM

DROP DATABASE IF EXISTS student_information_management;

CREATE DATABASE student_information_management;

USE student_information_management;

CREATE TABLE `Student` (
  `id` INT NOT NULL,
  `fullname` VARCHAR(100) NOT NULL,
  `gender` VARCHAR(10),
  `status` VARCHAR(10),
  `dateOfBirth` DATE,
  `academicYear` VARCHAR(20),
  `address` VARCHAR(255),
  `ethnicity` VARCHAR(100),
  `religion` VARCHAR(100),
  `nationality` VARCHAR(100),
    `departmentID` INT,
    `class_id` INT,
  PRIMARY KEY (`id`)
);



CREATE TABLE `FaceEndcoding`(
  `id` INT NOT NULL,
  `student_id` INT NOT NULL,
  `face_encoding` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`)
)


-- Bảng Class
CREATE TABLE `Class` (
  `id` INT NOT NULL,
  `name` VARCHAR(50) NOT NULL,
  `grade_level` INT,
  `teacher_id` INT,
  `academic_year` VARCHAR(20),
  `room` VARCHAR(10),
  `total_student` INT,
  `description` VARCHAR(255),
  PRIMARY KEY (`id`)
);


CREATE TABLE `TEACHER` (
       `id` INT NOT NULL,
      `fullname` VARCHAR(100) NOT NULL,
      `gender` VARCHAR(10),
      `status` VARCHAR(10),
      `address` VARCHAR(255),
      `email` VARCHAR(100),
      `phone` VARCHAR(10),
      `department_id` INT,
      `username` VARCHAR(20),
      `password` VARCHAR(20),
      PRIMARY KEY (`id`)
)


CREATE TABLE `Attendances` (
  `id` INT NOT NULL,
  `class_id` INT NOT NULL,
  `student_id` INT NOT NULL,
  `status` VARCHAR(20),
  `checkin_time` DATETIME,
  `scheduledetail_id` INT,
   PRIMARY KEY (`id`)
);




CREATE TABLE Department (
    id INT PRIMARY KEY,
    name NVARCHAR(100) NOT NULL,
    dean_id INT
);



CREATE TABLE Semester (
    id INT PRIMARY KEY,
    name NVARCHAR(50) NOT NULL, 
    startdate DATE NOT NULL,
    enddate DATE NOT NULL
);

CREATE TABLE Schedule (
    id INT PRIMARY KEY,
    departmentID INT NOT NULL,
    semesterID INT NOT NULL,
    description NVARCHAR(255) NULL, 
    CONSTRAINT FK_Schedule_Department FOREIGN KEY (departmentID) REFERENCES Department(id),
    CONSTRAINT FK_Schedule_Semester FOREIGN KEY (semesterID) REFERENCES Semester(id)
);

CREATE TABLE ScheduleDetail (
    id INT PRIMARY KEY,
    scheduleID INT NOT NULL,
    dayOfWeek INT NOT NULL,            
    startTime TIME NOT NULL,
    endTime TIME NOT NULL,
    CONSTRAINT FK_ScheduleDetail_Schedule FOREIGN KEY (scheduleID) REFERENCES Schedule(id)
);

ALTER TABLE Student ADD CONSTRAINT fk_student_class FOREIGN KEY (class_id) REFERENCES class(id);

ALTER TABLE FaceEndcoding ADD CONSTRAINT FK_FaceEndcoding_Student FOREIGN KEY (student_id) REFERENCES student(id);

ALTER TABLE class ADD CONSTRAINT FK_Class_Teacher FOREIGN KEY (teacher_id) REFERENCES TEACHER(id);

ALTER TABLE attendances ADD CONSTRAINT FK_Attendances_ScheduleDetail FOREIGN KEY (scheduledetail_id) REFERENCES ScheduleDetail(id);

ALTER TABLE Attendances ADD CONSTRAINT FK_Attendances_Student FOREIGN KEY (student_id) REFERENCES student(id);

ALTER TABLE Attendances ADD CONSTRAINT FK_Attendances_Class FOREIGN KEY (class_id) REFERENCES class(id);

ALTER TABLE student ADD CONSTRAINT FK_Student_Department FOREIGN KEY (departmentID) REFERENCES Department (id);

ALTER TABLE department ADD constraint FK_Department_Dean FOREIGN KEY (dean_id) REFERENCES teacher(id);
