from database.ConnectDB import Database
from models import Attendances

@staticmethod
def save(attendances):
    db = Database()
    sql = "INSERT INTO Attendances(id, class_id, student_id, status, checkin_time) VALUES (%s, %s, %s, %s, %s)"
    values = (attendances.id, attendances.class_id, attendances.student_id, attendances.status, attendances.checkin_time)
    db.exec_query(sql, values)
    db.close()

@staticmethod
def update(attendances):
    db = Database()
    sql = "UPDATE Attendances SET class_id=%s, student_id=%s, status=%s, checkin_time=%s WHERE id=%s"
    values = (attendances.class_id, attendances.student_id, attendances.status, attendances.checkin_time, attendances.id)
    db.exec_query(sql, values)
    db.close()

@staticmethod
def delete(id):
    db = Database()
    sql = "DELETE FROM Attendances WHERE id=%s"
    values = (id,)
    db.exec_query(sql, values)
    db.close()

@staticmethod
def get_all():
    db = Database()
    sql = "SELECT * FROM Attendances"
    result = db.fetch_all(sql)
    attendances = []
    for row in result:
        attendances.append(Attendances(*row))
    db.close()
    return attendances

@staticmethod
def get_by_id(id):
    db = Database()
    sql = "SELECT * FROM Attendances WHERE id=%s"
    result = db.fetch_one(sql, (id,))
    if result:
        db.close()
        return Attendances(*result)
    db.close()
    return None
