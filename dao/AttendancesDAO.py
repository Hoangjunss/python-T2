from database.ConnectDB import Database
from models.Attendances import Attendances

@staticmethod
def save(attendances: Attendances):
    db = Database()
    sql = "INSERT INTO Attendances(id, class_id, student_id, status, checkin_time) VALUES (%s, %s, %s, %s, %s)"
    values = (attendances.id, attendances.class_id, attendances.student_id, attendances.status, attendances.checkin_time)
    db.exec_query(sql, values)
    db.close()

@staticmethod
def update(attendances: Attendances):
    db = Database()
    sql = "UPDATE Attendances SET class_id=%s, student_id=%s, status=%s, checkin_time=%s WHERE id=%s"
    values = (attendances.class_id, attendances.student_id, attendances.status, attendances.checkin_time, attendances.id)
    db.exec_query(sql, values)
    db.close()

@staticmethod
def delete(id: int):
    db = Database()
    sql = "DELETE FROM Attendances WHERE id=%s"
    values = (id,)
    db.exec_query(sql, values)
    db.close()

@staticmethod
def get_all() -> list[Attendances]:
    db = Database()
    sql = "SELECT * FROM Attendances"
    result = db.fetch_all(sql)
    attendances = []
    for row in result:
        attendances.append(Attendances(*row))
    db.close()
    return attendances

@staticmethod
def get_by_id(id: int) -> Attendances:
    db = Database()
    sql = "SELECT * FROM Attendances WHERE id=%s"
    result = db.fetch_one(sql, (id,))
    if result:
        db.close()
        return Attendances(*result)
    db.close()
    return None

@staticmethod
def get_by_student_id(student_id: int) -> list[Attendances]:
    db = Database()
    sql = "SELECT * FROM Attendances WHERE student_id=%s"
    result = db.fetch_all(sql, (student_id,))
    attendances = []
    for row in result:
        attendances.append(Attendances(*row))
    db.close()
    return attendances

@staticmethod
def get_by_class_id(class_id: int) -> list[Attendances]:
    db = Database()
    sql = "SELECT * FROM Attendances WHERE class_id=%s"
    result = db.fetch_one(sql, (class_id,))
    attendances = []
    for row in result:
        attendances.append(Attendances(*row))
    return attendances

@staticmethod
def get_addtendent_by_time(time=None, classid=None, studentid=None) -> list[Attendances]:
    db = Database()
        
    if time:
        sql = "SELECT * FROM Attendances WHERE DATE(checkin_time) = DATE(%s)"
        values = (time,)
    else:
        sql = "SELECT * FROM Attendances WHERE DATE(checkin_time) = CURDATE()"
        values = ()

    if classid:
        sql += " AND class_id = %s"
        values += (classid,)

    if studentid:
        sql += " AND student_id = %s"
        values += (studentid,)
        
    try:
        result = db.fetch_all(sql, values)
        attendances = [Attendances(*row) for row in result]
        return attendances
    except Exception as e:
        print(f"Error while fetching attendance: {e}")
        return []
    finally:
        db.close()
