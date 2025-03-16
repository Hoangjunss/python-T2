from database.ConnectDB import Database
from models import Semester

@staticmethod
def save(semester):
    db = Database()
    sql = "INSERT INTO Semester (id, name, startdate, enddate) VALUES (%s, %s, %s, %s)"
    values = (semester.id, semester.name, semester.startdate, semester.enddate)
    db.exec_query(sql, values)
    db.close()

@staticmethod
def update(semester):
    db = Database()
    sql = "UPDATE Semester SET name=%s, startdate=%s, enddate=%s WHERE id=%s"
    values = (semester.name, semester.startdate, semester.enddate, semester.id)
    db.exec_query(sql, values)
    db.close()

@staticmethod
def delete(semester_id):
    db = Database()
    sql = "DELETE FROM Semester WHERE id=%s"
    values = (semester_id,)
    db.exec_query(sql, values)
    db.close()

@staticmethod
def get_all():
    db = Database()
    sql = "SELECT * FROM Semester"
    results = db.fetch_all(sql)
    semesters = []
    for row in results:
        semesters.append(Semester(*row))
    db.close()
    return semesters
    
@staticmethod
def get_by_id(semester_id):
    db = Database()
    sql = "SELECT * FROM Semester WHERE id=%s"
    result = db.fetch_one(sql, (semester_id,))
    db.close()
    if result:
        return Semester(*result)
    return None

