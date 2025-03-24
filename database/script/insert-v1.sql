
USE student_information_management;

INSERT INTO Class (id, name, grade_level, teacher_id, academic_year, room, total_student, description)
VALUES
(1, 'Class 10A1', 10, 1, '2024-2025', 'A101', 40, 'Lớp học Toán nâng cao'),
(2, 'Class 10A2', 10, 2, '2024-2025', 'A102', 38, 'Lớp học Văn nâng cao'),
(3, 'Class 11B1', 11, 3, '2024-2025', 'B201', 35, 'Lớp học Khoa học tự nhiên');

INSERT INTO TEACHER (id, username, fullname, gender, status, address, email, phone, department_id)
VALUES
(1, 'GV001', 'Nguyễn Văn An', 'Nam', 'Active', 'Hà Nội', 'an.nguyen@example.com', '0987654321', 1),
(2, 'GV002', 'Trần Thị Bích', 'Nữ', 'Active', 'Hồ Chí Minh', 'bich.tran@example.com', '0976543210', 2),
(3, 'GV003', 'Lê Minh Tuấn', 'Nam', 'Active', 'Đà Nẵng', 'tuan.le@example.com', '0965432109', 3);

INSERT INTO Student (id, fullname, gender, status, dateOfBirth, academicYear, address, ethnicity, religion, nationality, departmentID, class_id)
VALUES
(1, 'Phạm Văn Quang', 'Nam', 'Active', '2008-05-10', '2024-2025', 'Hà Nội', 'Kinh', 'Không', 'Việt Nam', 1, 1),
(2, 'Lê Thị Hoa', 'Nữ', 'Active', '2008-07-15', '2024-2025', 'Hồ Chí Minh', 'Kinh', 'Phật giáo', 'Việt Nam', 2, 1),
(3, 'Ngô Văn Đức', 'Nam', 'Active', '2007-03-20', '2024-2025', 'Đà Nẵng', 'Kinh', 'Không', 'Việt Nam', 3, 2),
(4, 'Trần Ngọc Minh', 'Nữ', 'Active', '2007-09-05', '2024-2025', 'Cần Thơ', 'Hoa', 'Công giáo', 'Việt Nam', 1, 3);

INSERT INTO Department (id, name, dean_id)
VALUES
(1, N'Khoa Công Nghệ Thông Tin', 1),
(2, N'Khoa Kinh Tế', 2),
(3, N'Khoa Khoa Học Tự Nhiên', 3);

INSERT INTO Semester (id, name, startdate, enddate)
VALUES
(1, N'Học Kỳ 1 - 2024', '2024-08-01', '2024-12-31'),
(2, N'Học Kỳ 2 - 2025', '2025-01-15', '2025-05-31'),
(3, N'Học Kỳ Hè - 2025', '2025-06-01', '2025-07-31');

INSERT INTO Schedule (id, departmentID, semesterID, description)
VALUES
(1, 1, 1, N'Lịch học cho khoa Công Nghệ Thông Tin'),
(2, 2, 1, N'Lịch học cho khoa Kinh Tế'),
(3, 3, 2, N'Lịch học cho khoa Khoa Học Tự Nhiên');

INSERT INTO ScheduleDetail (id, scheduleID, dayOfWeek, startTime, endTime)
VALUES
(1, 1, 2, '07:00:00', '11:30:00'), 
(2, 1, 3, '13:00:00', '17:30:00'), 
(4, 1, 5, '09:00:00', '11:30:00'),
(5, 1, 6, '15:00:00', '17:30:00');

