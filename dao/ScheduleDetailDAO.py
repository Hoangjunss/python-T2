from database.ConnectDB import Database
from models.ScheduleDetail import ScheduleDetail

@staticmethod
def save(schedule_details: ScheduleDetail):
    db = Database()
    sql = "INSERT INTO ScheduleDetail (id, scheduleId, dayOfWeek, startTime, endTime) VALUES (%s, %s, %s, %s, %s)"
    values = (schedule_details.id, schedule_details.scheduleId, schedule_details.dayOfWeek, schedule_details.startTime, schedule_details.endTime)
    db.exec_query(sql, values)
    db.close()

@staticmethod
def update(schedule_details: ScheduleDetail):
    db = Database()
    sql = "UPDATE ScheduleDetail SET scheduleId=%s, dayOfWeek=%s, startTime=%s, endTime=%s WHERE id=%s"
    values = (schedule_details.scheduleId, schedule_details.dayOfWeek, schedule_details.startTime, schedule_details.endTime, schedule_details.id)
    db.exec_query(sql, values)
    db.close()

@staticmethod
def delete(schedule_details_id: int):
    db = Database()
    sql = "DELETE FROM ScheduleDetail WHERE id=%s"
    values = (schedule_details_id,)
    db.exec_query(sql, values)
    db.close()

@staticmethod
def get_all() -> list[ScheduleDetail]:
    db = Database()
    sql = "SELECT id, scheduleId, dayOfWeek, startTime, endTime FROM ScheduleDetail"
    result = db.fetch_all(sql)
    schedule_details = []
    for row in result:
        schedule_details.append(ScheduleDetail(
            id=row['id'],
            scheduleId=row['scheduleId'],
            dayOfWeek=row['dayOfWeek'],
            startTime=row['startTime'],
            endTime=row['endTime']
        ))
    db.close()
    return schedule_details

@staticmethod
def get_by_id(schedule_id) -> ScheduleDetail:
    db = Database()
    sql = "SELECT id, scheduleId, dayOfWeek, startTime, endTime FROM ScheduleDetail WHERE id=%s"
    values = (schedule_id,)
    result = db.fetch_one(sql, values)
    if result:
        db.close()
        return ScheduleDetail(
            id=result['id'],
            scheduleId=result['scheduleId'],
            dayOfWeek=result['dayOfWeek'],
            startTime=result['startTime'],
            endTime=result['endTime']
        )
    db.close()
    return None

@staticmethod
def get_by_schedule_id(schedule_id) -> list[ScheduleDetail]:
    db = Database()
    sql = "SELECT id, scheduleId, dayOfWeek, startTime, endTime FROM ScheduleDetail WHERE scheduleId=%s"
    values = (schedule_id,)
    result = db.fetch_all(sql, values)
    schedule_details = []
    for row in result:
        schedule_details.append(ScheduleDetail(
            id=row['id'],
            scheduleId=row['scheduleId'],
            dayOfWeek=row['dayOfWeek'],
            startTime=row['startTime'],
            endTime=row['endTime']
        ))
    db.close()
    return schedule_details