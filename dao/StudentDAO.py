from database.ConnectDB import Database
from models.Students import Student

class StudentDAO:
    def __init__(self):
        print("hello")

@staticmethod
def save(student: Student):
    db = Database()
    sql = """
        INSERT INTO Student
        (id, fullname, gender, status, dateOfBirth, academicYear, address, ethnicity, religion, nationality, departmentID, class_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
    values = (
        student.id, student.fullname, student.gender, student.status, 
        student.dateOfBirth, student.academicYear, student.address, 
        student.ethnicity, student.religion, student.nationality, student.departmentId, student.class_id
    )
    db.exec_query(sql, values)
    db.close()

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
def delete(student_id: int):
    db = Database()
    sql = "DELETE FROM Student WHERE id = %s"
    values = (student_id,)
    db.exec_query(sql, values)
    db.close()
def get_all() -> list[Student]:
    db = Database()
    sql = "SELECT id, fullname, gender, status, dateOfBirth, academicYear, address, ethnicity, religion, nationality, departmentID, class_id FROM Student"
    result = db.fetch_all(sql)
    students = []
    for row in result:
        students.append(Student(
            id=row['id'],
            fullname=row['fullname'],
            gender=row['gender'],
            status=row['status'],
            dateOfBirth=row['dateOfBirth'],
            academicYear=row['academicYear'],
            address=row['address'],
            ethnicity=row['ethnicity'],
            religion=row['religion'],
            nationality=row['nationality'],
            departmentId=row['departmentID'],
            class_id=row['class_id']
        ))
    db.close()
    return students
def get_by_id(student_id: int) -> Student:
    db = Database()
    sql = "SELECT id, fullname, gender, status, dateOfBirth, academicYear, address, ethnicity, religion, nationality, departmentID, class_id FROM Student WHERE id = %s"
    result = db.fetch_one(sql, (student_id,))
    db.close()
    if result:
        return Student(
            id=result['id'],
            fullname=result['fullname'],
            gender=result['gender'],
            status=result['status'],
            dateOfBirth=result['dateOfBirth'],
            academicYear=result['academicYear'],
            address=result['address'],
            ethnicity=result['ethnicity'],
            religion=result['religion'],
            nationality=result['nationality'],
            departmentId=result['departmentID'],
            class_id=result['class_id']
        )
    return None
def get_by_department_id(department_id: int) -> list[Student]:
    db = Database()
    sql = "SELECT id, fullname, gender, status, dateOfBirth, academicYear, address, ethnicity, religion, nationality, departmentID, class_id FROM Student WHERE departmentID = %s"
    result = db.fetch_all(sql, (department_id,))
    students = []
    for row in result:
        students.append(Student(
            id=row['id'],
            fullname=row['fullname'],
            gender=row['gender'],
            status=row['status'],
            dateOfBirth=row['dateOfBirth'],
            academicYear=row['academicYear'],
            address=row['address'],
            ethnicity=row['ethnicity'],
            religion=row['religion'],
            nationality=row['nationality'],
            departmentId=row['departmentID'],
            class_id=row['class_id']
        ))
    db.close()
    return students
def get_by_class_id(class_id: int) -> list[Student]:
    db = Database()
    sql = "SELECT id, fullname, gender, status, dateOfBirth, academicYear, address, ethnicity, religion, nationality, departmentID, class_id FROM Student WHERE class_id = %s"
    result = db.fetch_all(sql, (class_id,))
    students = []
    for row in result:
        students.append(Student(
            id=row['id'],
            fullname=row['fullname'],
            gender=row['gender'],
            status=row['status'],
            dateOfBirth=row['dateOfBirth'],
            academicYear=row['academicYear'],
            address=row['address'],
            ethnicity=row['ethnicity'],
            religion=row['religion'],
            nationality=row['nationality'],
            departmentId=row['departmentID'],
            class_id=row['class_id']
        ))
    db.close()
    return students