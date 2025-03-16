from database.ConnectDB import Database
from models.Teacher import Teacher

@staticmethod
def save(teacher: Teacher):
    db = Database()
    query = "INSERT INTO teachers (id, fullname, gender, status, address, email, phone, department_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (teacher.id, teacher.fullname, teacher.gender, teacher.status, teacher.address, teacher.email, teacher.phone, teacher.department_id)
    db.exec_query(query, values)
    db.close()

@staticmethod
def update(teacher: Teacher):
    db = Database()
    query = "UPDATE teachers SET fullname=%s, gender=%s, status=%s, address=%s, email=%s, phone=%s, department_id=%s WHERE id=%s"
    values = (teacher.fullname, teacher.gender, teacher.status, teacher.address, teacher.email, teacher.phone, teacher.department_id, teacher.id)
    db.exec_query(query, values)
    db.close()

@staticmethod
def delete(teacher_id: int):
    db = Database()
    query = "DELETE FROM teachers WHERE id=%s"
    values = (teacher_id,)
    db.exec_query(query, values)
    db.close()

@staticmethod
def get_by_id(teacher_id: int) -> Teacher:
    db = Database()
    query = "SELECT * FROM teachers WHERE id=%s"
    values = (teacher_id,)
    result = db.fetch_one(query, values)
    db.close()
    if result:
        return Teacher(*result)
    return None

@staticmethod
def get_all() -> list[Teacher]:
    db = Database()
    query = "SELECT * FROM teachers"
    result = db.exec_query(query)
    teachers = []
    for row in result:
        teachers.append(Teacher(*row))
    db.close()
    return teachers