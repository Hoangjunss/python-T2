from database.ConnectDB import Database
from models.Class import Class

@staticmethod
def save(edu_class: Class):
    db = Database()
    sql = "INSERT INTO Class (id, name, grade_level, teacher_id, academic_year, room, total_student, description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (edu_class.id, edu_class.name, edu_class.grade_level, edu_class.teacher_id, edu_class.academic_year, edu_class.room, edu_class.total_student, edu_class.description)
    db.execute_sql(sql, values)
    db.close()

@staticmethod
def update(edu_class: Class):
    db = Database()
    sql = "UPDATE Class SET name=%s, grade_level=%s, teacher_id=%s, academic_year=%s, room=%s, total_student=%s, description=%s WHERE id=%s"
    values = (edu_class.name, edu_class.grade_level, edu_class.teacher_id, edu_class.academic_year, edu_class.room, edu_class.total_student, edu_class.description, edu_class.id)
    db.exec_query(sql, values)
    db.close()

@staticmethod
def delete(id: int):
    db = Database()
    sql = "DELETE FROM Class WHERE id=%s"
    values = (id,)
    db.exec_query(sql, values)
    db.close()

@staticmethod
def get_all() -> list[Class]:
    db = Database()
    sql = "SELECT * FROM Class"
    results = db.fetch_all(sql)
    edu_class = []
    for row in results:
        edu_class.append(Class(*row))
    db.close()
    return edu_class

@staticmethod
def get_by_id(id: int) -> Class:
    db = Database()
    sql = "SELECT * FROM Class WHERE id=%s"
    values = (id,)
    result = db.fetch_one(sql, values)
    if result:
        db.close()
        return Class(*result)
    db.close()
    return None