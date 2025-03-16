from database.ConnectDB import Database
from models import ScheduleDetail

@staticmethod
def save(schedule_details):
    db = Database()
    sql = "INSERT INTO ScheduleDetail (id, scheduleId, dayOfWeek, startTime, endTime) VALUES (%s, %s, %s, %s)"
    values = (schedule_details.id, schedule_details.scheduleId, schedule_details.dayOfWeek, schedule_details.startTime, schedule_details.endTime)
    db.exec_query(sql, values)
    db.close()

@staticmethod
def update(schedule_details):
    db = Database()
    sql = "UPDATE ScheduleDetail SET scheduleId=%s, dayOfWeek=%s, startTime=%s, endTime=%s WHERE id=%s"
    values = (schedule_details.scheduleId, schedule_details.dayOfWeek, schedule_details.startTime, schedule_details.endTime, schedule_details.id)
    db.exec_query(sql, values)
    db.close()

@staticmethod
def delete(schedule_details_id):
    db = Database()
    sql = "DELETE FROM ScheduleDetail WHERE id=%s"
    values = (schedule_details_id,)
    db.exec_query(sql, values)
    db.close()

@staticmethod
def get_all():
    db = Database()
    sql = "SELECT * FROM ScheduleDetail"
    result = db.exec_query(sql)
    schedule_details = []
    for row in result:
        schedule_details.append(ScheduleDetail(*row))
    db.close()
    return result

@staticmethod
def get_by_id(schedule_id):
    db = Database()
    sql = "SELECT * FROM ScheduleDetail WHERE id=%s"
    values = (schedule_id,)
    result = db.exec_query(sql, values)
    if result:
        db.close()
        return ScheduleDetail(*result)
    db.close()
    return None