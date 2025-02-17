from ConnectDB import Database

class Student:
    def __init__(self, student_id, full_name, date_of_birth, gender, email, phone_number, class_id, department_id):
        self.student_id = student_id
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.email = email
        self.phone_number = phone_number
        self.class_id = class_id
        self.department_id = department_id

    def __str__(self):
        return f"Student(student_id='{self.student_id}', full_name='{self.full_name}', date_of_birth='{self.date_of_birth}', gender='{self.gender}', email='{self.email}', phone_number='{self.phone_number}', class_id='{self.class_id}', department_id='{self.department_id}')"

    @staticmethod
    def save(self):
        db = Database()
        query = f"""
            INSERT INTO students (student_id, full_name, date_of_birth, gender, email, phone_number, class_id, department_id)
            VALUES ('{self.student_id}', '{self.full_name}', '{self.date_of_birth}', '{self.gender}', '{self.email}', '{self.phone_number}', '{self.class_id}', '{self.department_id}')
        """
        db.exec_query(query)
        db.close()

    @staticmethod
    def get_all():
        db = Database()
        query = "SELECT * FROM students"
        result = db.exec_query(query)
        students = []
        for row in result:
            students.append(Student(*row))
        db.close()
        return students
    
    @staticmethod
    def get_by_id(student_id):
        db = Database()
        query = f"SELECT * FROM students WHERE student_id = '{student_id}'"
        result = db.exec_query(query)
        if result:
            return Student(*result[0])
        db.close()
        return None
    
    @staticmethod
    def update(self):
        db = Database()
        query = f"""
            UPDATE students
            SET full_name='{self.full_name}', date_of_birth='{self.date_of_birth}', gender='{self.gender}', email='{self.email}', phone_number='{self.phone_number}', class_id='{self.class_id}', department_id='{self.department_id}'
            WHERE student_id='{self.student_id}'
        """
        db.exec_query(query)
        db.close()

    @staticmethod
    def delete(student_id):
        db = Database
        query = f"DELETE FROM students WHERE student_id='{student_id}'"
        db.exec_query(query)
        db.close()