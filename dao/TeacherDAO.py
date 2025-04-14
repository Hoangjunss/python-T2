from database.ConnectDB import Database
from models.Teacher import Teacher

@staticmethod
def save(teacher: Teacher):
    db = Database()
    query = "INSERT INTO teacher (id, fullname, gender, status, address, email, phone, department_id,username) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s)"
    values = (teacher.id, teacher.fullname, teacher.gender, teacher.status, teacher.address, teacher.email, teacher.phone, teacher.department_id,teacher.username)
    db.exec_query(query, values)
    db.close()

@staticmethod
def update(teacher: Teacher):
    db = Database()
    query = "UPDATE teacher SET fullname=%s, gender=%s, status=%s, address=%s, email=%s, phone=%s, department_id=%s ,username=%s WHERE id=%s"
    values = (teacher.fullname, teacher.gender, teacher.status, teacher.address, teacher.email, teacher.phone, teacher.department_id,teacher.username, teacher.id)
    db.exec_query(query, values)
    db.close()

@staticmethod
def delete(teacher_id: int):
    db = Database()
    query = "DELETE FROM teacher WHERE id=%s"
    values = (teacher_id,)
    db.exec_query(query, values)
    db.close()

@staticmethod
def get_by_id(teacher_id: int) -> Teacher:
    db = Database()
    query = "SELECT * FROM teacher WHERE id=%s"
    values = (teacher_id,)
    result = db.fetch_one(query, values)
    db.close()
    if result:
        return Teacher(*result)
    return None

@staticmethod
def get_all() -> list[Teacher]:
    db = Database()
    query = "SELECT * FROM teacher"
    result = db.fetch_all(query)
    teachers = []
    for row in result:
        teachers.append(Teacher(*row))
    db.close()
    return teachers
