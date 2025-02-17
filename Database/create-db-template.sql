CREATE DATABASE student_information_management
    DEFAULT CHARACTER SET = 'utf8mb4';

USE student_information_management;

-- Bảng sinh viên
CREATE TABLE Students (
    student_id VARCHAR(20) PRIMARY KEY,
    full_name NVARCHAR(100) NOT NULL,
    date_of_birth DATE,
    gender VARCHAR(10) CHECK (gender IN ('MALE', 'FEMALE')),
    email VARCHAR(100) UNIQUE,
    phone_number VARCHAR(15),
    class_id VARCHAR(10) NOT NULL,
    department_id INT NOT NULL,
    created_at DATETIME DEFAULT NOW(),
    FOREIGN KEY (class_id) REFERENCES Classes(class_id),
    FOREIGN KEY (department_id) REFERENCES Departments(department_id)
);

-- Bảng môn học
CREATE TABLE Courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT PRIMARY KEY, 
    course_code VARCHAR(10) UNIQUE NOT NULL,
    course_name NVARCHAR(100) NOT NULL,
    credits INT CHECK (credits > 0),
    department_id INT NOT NULL,
    FOREIGN KEY (department_id) REFERENCES Departments(department_id)
);

-- Bảng lớp học phần (Course Section)
CREATE TABLE CourseSections (
    section_id INT PRIMARY KEY AUTO_INCREMENT PRIMARY KEY, 
    course_id INT NOT NULL,
    lecturer_id INT NOT NULL,
    room_number VARCHAR(20),
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (course_id) REFERENCES Courses(course_id),
    FOREIGN KEY (lecturer_id) REFERENCES Lecturers(lecturer_id)
);

-- Bảng buổi học
CREATE TABLE Sessions (
    session_id INT PRIMARY KEY AUTO_INCREMENT PRIMARY KEY, 
    section_id INT NOT NULL,
    session_date DATETIME NOT NULL,
    topic NVARCHAR(255),
    is_cancelled BIT DEFAULT 0,
    FOREIGN KEY (section_id) REFERENCES CourseSections(section_id)
);

-- Bảng điểm danh
CREATE TABLE Attendances (
    attendance_id BIGINT PRIMARY KEY AUTO_INCREMENT PRIMARY KEY, 
    student_id VARCHAR(20) NOT NULL,
    session_id INT NOT NULL,
    status CHAR(1) CHECK (status IN ('P', 'A', 'E')), -- P: Present, A: Absent, E: Excused
    recorded_at DATETIME DEFAULT NOW(),
    image_recorded VARCHAR(255),
    UNIQUE (student_id, session_id),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (session_id) REFERENCES Sessions(session_id)
);

-- Bảng khoa
CREATE TABLE Departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY, 
    department_code VARCHAR(10) UNIQUE NOT NULL,
    department_name NVARCHAR(100) NOT NULL
);

-- Bảng lớp (lớp hành chính)
CREATE TABLE Classes (
    class_id VARCHAR(10) PRIMARY KEY,
    class_name NVARCHAR(100) NOT NULL,
    academic_year VARCHAR(10) NOT NULL,
    lecturer_id INT NOT NULL,
    FOREIGN KEY (lecturer_id) REFERENCES Lecturers(lecturer_id)
);

-- Bảng giảng viên
CREATE TABLE Lecturers (
    lecturer_id INT AUTO_INCREMENT PRIMARY KEY, 
    full_name NVARCHAR(100) NOT NULL,
    gender VARCHAR(10) CHECK (gender IN ('MALE', 'FEMALE')),
    email VARCHAR(100) UNIQUE,
    phone_number VARCHAR(15),
    department_id INT NOT NULL,
    FOREIGN KEY (department_id) REFERENCES Departments(department_id)
);