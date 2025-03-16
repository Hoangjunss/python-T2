from database.ConnectDB import Database
from models import Schedule

@staticmethod
def save(schedule):
    db = Database()
    sql = "INSERT INTO (id, departmentID, semesterID, description) VALUES (%s, %s, %s, %s)"
    values = (schedule.id, schedule.departmentID, schedule.semesterID, schedule.description)
    db.exec_query(sql, values)
    db.close()

@staticmethod
def update(schedule):
    db = Database()
    sql = "UPDATE Schedule SET departmentID=%s, semesterID=%s, description=%s WHERE id=%s"
    values = (schedule.departmentID, schedule.semesterID, schedule.description, schedule.id)
    db.exec_query(sql, values)
    db.close()

@staticmethod
def delete(scheduleId):
    db = Database()
    sql = "DELETE FROM Schedule WHERE id=%s"
    values = (scheduleId,)
    db.exec_query(sql, values)
    db.close()

@staticmethod
def get_all():
    db = Database()
    sql = "SELECT * FROM Schedule"
    results = db.fetch_all(sql)
    schedules = []
    for row in results:
        schedules.append(Schedule(*row))
    db.close()
    return schedules

@staticmethod
def get_by_id(scheduleId):
    db = Database()
    sql = "SELECT * FROM Schedule WHERE id=%s"
    result = db.fetch_one(sql, (scheduleId,))
    if result:
        db.close()
        return Schedule(*result)
    db.close()
    return None