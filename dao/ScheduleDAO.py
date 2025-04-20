from database.ConnectDB import Database
from models.Schedule import Schedule

@staticmethod
def save(schedule: Schedule):
    db = Database()
    sql = "INSERT INTO Schedule (id, departmentID, semesterID, description) VALUES (%s, %s, %s, %s)"
    values = (schedule.id, schedule.departmentId, schedule.semesterId, schedule.description)
    db.exec_query(sql, values)
    db.close()

@staticmethod
def update(schedule: Schedule):
    db = Database()
    sql = "UPDATE Schedule SET departmentID=%s, semesterID=%s, description=%s WHERE id=%s"
    values = (schedule.departmentId, schedule.semesterId, schedule.description, schedule.id)
    db.exec_query(sql, values)
    db.close()

@staticmethod
def delete(scheduleId: int):
    db = Database()
    sql = "DELETE FROM Schedule WHERE id=%s"
    values = (scheduleId,)
    db.exec_query(sql, values)
    db.close()

@staticmethod
def get_all() -> list[Schedule]:
    db = Database()
    sql = "SELECT id, departmentID, semesterID, description FROM Schedule"
    results = db.fetch_all(sql)
    schedules = []
    for row in results:
        schedules.append(Schedule(
            id=row['id'],
            departmentId=row['departmentID'],
            semesterId=row['semesterID'],
            description=row['description']
        ))
    db.close()
    return schedules

@staticmethod
def get_by_id(scheduleId: int) -> Schedule:
    db = Database()
    sql = "SELECT id, departmentID, semesterID, description FROM Schedule WHERE id=%s"
    result = db.fetch_one(sql, (scheduleId,))
    if result:
        db.close()
        return Schedule(
            id=result['id'],
            departmentId=result['departmentID'],
            semesterId=result['semesterID'],
            description=result['description']
        )
    db.close()
    return None

@staticmethod
def get_by_department_id(departmentId: int) -> list[Schedule]:
    db = Database()
    sql = "SELECT id, departmentID, semesterID, description FROM Schedule WHERE departmentID=%s"
    results = db.fetch_all(sql, (departmentId,))
    schedules = []
    for row in results:
        schedules.append(Schedule(
            id=row['id'],
            departmentId=row['departmentID'],
            semesterId=row['semesterID'],
            description=row['description']
        ))
    db.close()
    return schedules

@staticmethod
def get_by_semester_id(semesterId: int) -> list[Schedule]:
    db = Database()
    sql = "SELECT id, departmentID, semesterID, description FROM Schedule WHERE semesterID=%s"
    results = db.fetch_all(sql, (semesterId,))
    schedules = []
    for row in results:
        schedules.append(Schedule(
            id=row['id'],
            departmentId=row['departmentID'],
            semesterId=row['semesterID'],
            description=row['description']
        ))
    db.close()
    return schedules