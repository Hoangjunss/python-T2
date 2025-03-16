from database.ConnectDB import Database
from models.Subject import Subject


@staticmethod
def save(subject: Subject):
    db = Database()
    sql = """
        INSERT INTO Subject (id, name, numberOfLessons)
        VALUES (%s, %s, %s)
    """
    values = (subject.id, subject.name, subject.numberOfLessons)
    db.exec_query(sql, values)
    db.close()

@staticmethod
def update(subject: Subject):
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
def delete(subject_id: int):
    db = Database()
    sql = "DELETE FROM Subject WHERE id = %s"
    values = (subject_id,)
    db.exec_query(sql, values)
    db.close()

@staticmethod
def get_all() -> list[Subject]:
    db = Database()
    sql = "SELECT * FROM Subject"
    result = db.fetch_all(sql)
    subjects = []
    for row in result:
        subjects.append(Subject(*row))
    db.close()
    return subjects

@staticmethod
def get_by_id(subject_id: int) -> Subject:
    db = Database()
    sql = "SELECT * FROM Subject WHERE id = %s"
    result = db.fetch_one(sql, (subject_id,))
    db.close()
    if result:
        return Subject(*result)
    return None

