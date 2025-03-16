from database.ConnectDB import Database
from models import Subject


@staticmethod
def save(subject):
    db = Database()
    sql = """
        INSERT INTO Subject (name, numberOfLessons)
        VALUES (%s, %s)
    """
    values = (subject.name, subject.numberOfLessons)
    db.exec_query(sql, values)
    db.close()

@staticmethod
def update(subject):
    db = Database()
    sql = """
        UPDATE Subject
        SET name = %s, numberOfLessons = %s
        WHERE id = %s
    """
    values = (subject.name, subject.numberOfLessons, subject.id)
    db.exec_query(sql, values)
    db.close()

@staticmethod
def delete(subject_id):
    db = Database()
    sql = "DELETE FROM Subject WHERE id = %s"
    values = (subject_id,)
    db.exec_query(sql, values)
    db.close()

@staticmethod
def get_all():
    db = Database()
    sql = "SELECT * FROM Subject"
    result = db.fetch_all(sql)
    subjects = []
    for row in result:
        subjects.append(Subject(*row))
    db.close()
    return subjects

@staticmethod
def get_by_id(subject_id):
    db = Database()
    sql = "SELECT * FROM Subject WHERE id = %s"
    result = db.fetch_one(sql, (subject_id,))
    db.close()
    if result:
        return Subject(*result)
    return None

