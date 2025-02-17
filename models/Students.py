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
                 nationality=None):
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

    def __str__(self):
        return (f"Student(id={self.id}, fullname='{self.fullname}', gender='{self.gender}', "
                f"status='{self.status}', dateOfBirth='{self.dateOfBirth}', academicYear='{self.academicYear}', "
                f"address='{self.address}', ethnicity='{self.ethnicity}', religion='{self.religion}', "
                f"nationality='{self.nationality}')")

    @staticmethod
    def save(student):
        """
        Thêm một student mới vào bảng `students`.
        """
        db = Database()
        query = f"""
            INSERT INTO student
            (fullname, gender, status, dateOfBirth, academicYear, address, ethnicity, religion, nationality)
            VALUES
            ('{student.fullname}',
             '{student.gender}',
             '{student.status}',
             '{student.dateOfBirth}',
             '{student.academicYear}',
             '{student.address}',
             '{student.ethnicity}',
             '{student.religion}',
             '{student.nationality}')
        """
        db.exec_query(query)
        db.close()

    @staticmethod
    def get_all():
        """
        Lấy danh sách tất cả student từ bảng `students`.
        """
        db = Database()
        if db:
            print("Connected to database")
        query = "SELECT * FROM student"
        result = db.fetch_all(query)
        students = []
        for row in result:
            # row sẽ chứa 11 cột (id, fullname, gender, status, dateOfBirth, academicYear, address, ethnicity, religion, nationality)
            # row[0] = id, row[1] = fullname, row[2] = gender, ...
            students.append(Student(*row))
        db.close()
        return students

    @staticmethod
    def get_by_id(student_id):
        """
        Lấy thông tin 1 student theo id.
        """
        db = Database()
        query = f"SELECT * FROM student WHERE id = {student_id}"
        result = db.fetch_one(query)
        if result:
            return Student(*result[0])
        db.close()
        return None

    @staticmethod
    def update(student):
        """
        Cập nhật thông tin student theo id.
        """
        db = Database()
        query = f"""
            UPDATE student
            SET
              fullname = '{student.fullname}',
              gender = '{student.gender}',
              status = '{student.status}',
              dateOfBirth = '{student.dateOfBirth}',
              academicYear = '{student.academicYear}',
              address = '{student.address}',
              ethnicity = '{student.ethnicity}',
              religion = '{student.religion}',
              nationality = '{student.nationality}'
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
        query = f"DELETE FROM student WHERE id = {student_id}"
        db.exec_query(query)
        db.close()
