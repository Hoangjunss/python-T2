DROP DATABASE student_information_management;

CREATE DATABASE student_information_management
    DEFAULT CHARACTER SET = 'utf8mb4';

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
  PRIMARY KEY (`id`)
);

CREATE TABLE `FaceEndcoding`(
  `id` INT NOT NULL,
  `student_id` INT NOT NULL,
  `face_encoding` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`)
)

ALTER TABLE FaceEndcoding ADD CONSTRAINT FK_FaceEndcoding_Student FOREIGN KEY (student_id) REFERENCES student(id);

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
      `class_id` INT NOT NULL,
      `fullname` VARCHAR(100) NOT NULL,
      `gender` VARCHAR(10),
      `status` VARCHAR(10),
      `dateOfBirth` DATE,
      PRIMARY KEY (`id`)
)

ALTER TABLE class ADD CONSTRAINT FK_Class_Teacher FOREIGN KEY (teacher_id) REFERENCES TEACHER(id);

CREATE TABLE `Attendances` (
  `id` INT NOT NULL,
  `class_id` INT NOT NULL,
  `student_id` INT NOT NULL,
  `status` VARCHAR(20),
  `checkin_time` DATETIME,
   PRIMARY KEY (`id`)
);

ALTER TABLE Attendances ADD CONSTRAINT FK_Attendances_Student FOREIGN KEY (student_id) REFERENCES student(id);
ALTER TABLE Attendances ADD CONSTRAINT FK_Attendances_Class FOREIGN KEY (class_id) REFERENCES class(id);


CREATE TABLE Department (
    id INT PRIMARY KEY,
    name NVARCHAR(100) NOT NULL
);

ALTER TABLE student ADD CONSTRAINT FK_Student_Department FOREIGN KEY (departmentID) REFERENCES Department (id);

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
