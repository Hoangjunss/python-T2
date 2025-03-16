from database.ConnectDB import Database
from models.Students import Student

@staticmethod
def save(student: Student):
    db = Database()
    sql = """
        INSERT INTO Student
        (id, fullname, gender, status, dateOfBirth, academicYear, address, ethnicity, religion, nationality, departmentID, class_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
    values = (
        student.fullname, student.gender, student.status, 
        student.dateOfBirth, student.academicYear, student.address, 
        student.ethnicity, student.religion, student.nationality, student.departmentId, student.class_id
    )
    db.exec_query(sql, values)
    db.close()


@staticmethod
def update(student: Student):
    db = Database()
    sql = """
        UPDATE Student
        SET fullname=%s, gender=%s, status=%s, dateOfBirth=%s, academicYear=%s, 
                address=%s, ethnicity=%s, religion=%s, nationality=%s, departmentID=%s, class_id=%s
            WHERE id=%s
        """
    values = (
        student.fullname, student.gender, student.status, 
        student.dateOfBirth, student.academicYear, student.address, 
        student.ethnicity, student.religion, student.nationality, 
        student.departmentId, student.class_id, student.id
    )
    db.exec_query(sql, values)
    db.close()

@staticmethod
def delete(student_id: int):
    db = Database()
    sql = "DELETE FROM Student WHERE id = %s"
    values = (student_id,)
    db.exec_query(sql, values)
    db.close()

@staticmethod
def get_all() -> list[Student]:
    db = Database()
    sql = "SELECT * FROM Student"
    result = db.fetch_all(sql)
    students = []
    for row in result:
        students.append(Student(*row))
    db.close()
    return students

@staticmethod
def get_by_id(student_id: int) -> Student:
    db = Database()
    sql = "SELECT * FROM Student WHERE id = %s"
    result = db.fetch_one(sql, (student_id,))
    db.close()
    if result:
        return Student(*result)
    return None

@staticmethod
def get_by_department_id(department_id: int) -> list[Student]:
    db = Database()
    sql = "SELECT * FROM Student WHERE departmentID = %s"
    result = db.fetch_all(sql, (department_id,))
    students = []
    for row in result:
        students.append(Student(*row))
    db.close()
    return students

@staticmethod
def get_by_class_id(class_id: int) -> list[Student]:
    db = Database()
    sql = "SELECT * FROM Student WHERE class_id = %s"
    result = db.fetch_all(sql, (class_id,))
    students = []
    for row in result:
        students.append(Student(*row))
    db.close()
    return students