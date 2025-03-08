from database.ConnectDB import Database

class Student:
    def __init__(self, 
                 id=None, 
                 fullname=None, 
                 gender=None, 
                 status=None, 
                 dateOfBirth=None, 
                 academicYear=None, 
                 address=None, 
                 ethnicity=None, 
                 religion=None, 
                 nationality=None,
                 departmentId=None):
        self.id = id
        self.fullname = fullname
        self.gender = gender
        self.status = status
        self.dateOfBirth = dateOfBirth
        self.academicYear = academicYear
        self.address = address
        self.ethnicity = ethnicity
        self.religion = religion
        self.nationality = nationality
        self.departmentId = departmentId

    def __str__(self):
        return (f"Student(id={self.id}, fullname='{self.fullname}', gender='{self.gender}', "
                f"status='{self.status}', dateOfBirth='{self.dateOfBirth}', academicYear='{self.academicYear}', "
                f"address='{self.address}', ethnicity='{self.ethnicity}', religion='{self.religion}', "
                f"nationality='{self.nationality}', departmentId='{self.departmentId}')")

    @staticmethod
    def save(student):
        """
        Thêm một student mới vào bảng `Student`.
        Lưu ý: Nếu cột id được thiết lập tự động tăng (AUTO_INCREMENT), 
        thì không cần truyền giá trị cho id.
        """
        db = Database()
        query = f"""
            INSERT INTO Student
            (fullname, gender, status, dateOfBirth, academicYear, address, ethnicity, religion, nationality, departmentID)
            VALUES
            ('{student.fullname}',
             '{student.gender}',
             '{student.status}',
             '{student.dateOfBirth}',
             '{student.academicYear}',
             '{student.address}',
             '{student.ethnicity}',
             '{student.religion}',
             '{student.nationality}',
             '{student.departmentId}')
        """
        db.exec_query(query)
        db.close()

    @staticmethod
    def get_all():
        """
        Lấy danh sách tất cả student từ bảng `Student`.
        """
        db = Database()
        print("Connected to database")
        query = "SELECT * FROM Student"
        result = db.fetch_all(query)
        students = []
        for row in result:
            # Giả định thứ tự các cột là:
            # id, fullname, gender, status, dateOfBirth, academicYear, address, ethnicity, religion, nationality, departmentID
            students.append(Student(*row))
        db.close()
        return students

    @staticmethod
    def get_by_id(student_id):
        """
        Lấy thông tin 1 student theo id.
        """
        db = Database()
        query = f"SELECT * FROM Student WHERE id = {student_id}"
        result = db.fetch_one(query)
        if result:
            db.close()
            return Student(*result)
        db.close()
        return None

    @staticmethod
    def update(student):
        """
        Cập nhật thông tin student theo id.
        """
        db = Database()
        query = f"""
            UPDATE Student
            SET
              fullname = '{student.fullname}',
              gender = '{student.gender}',
              status = '{student.status}',
              dateOfBirth = '{student.dateOfBirth}',
              academicYear = '{student.academicYear}',
              address = '{student.address}',
              ethnicity = '{student.ethnicity}',
              religion = '{student.religion}',
              nationality = '{student.nationality}',
              departmentID = '{student.departmentId}'
            WHERE id = {student.id}
        """
        db.exec_query(query)
        db.close()

    @staticmethod
    def delete(student_id):
        """
        Xóa 1 student theo id.
        """
        db = Database()
        query = f"DELETE FROM Student WHERE id = {student_id}"
        db.exec_query(query)
        db.close()
