from database.ConnectDB import Database
from dto.StudentAttendenceDTO import StudentAttendenceDTO
from models.Attendances import Attendances

@staticmethod
def save(attendances: Attendances):
    db = Database()


    class_id_row = db.fetch_one(
        "SELECT class_id FROM Student WHERE id = %s", (attendances.student_id,)
    )
    class_id = class_id_row["class_id"] if class_id_row else None

    sql = """
        INSERT INTO Attendances (id, class_id, student_id, scheduledetail_id, status, checkin_time)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (
        attendances.id,
        class_id,
        attendances.student_id,
        attendances.scheduledetail_id,
        attendances.status,
        attendances.checkin_time,
    )

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
def delete_by_student_id(student_id: int):
    db = Database()
    sql = "DELETE FROM Attendances WHERE student_id=%s"
    values = (student_id,)
    db.exec_query(sql, values)
    db.close()

@staticmethod
def get_all() -> list[Attendances]:
    db = Database()
    sql = "SELECT id, class_id, student_id, status, checkin_time, scheduledetail_id FROM attendances"
    result = db.fetch_all(sql)
    attendances = []
    for row in result:
        attendances.append(Attendances(
            id=row['id'],
            class_id=row['class_id'],
            student_id=row['student_id'],
            status=row['status'],
            checkin_time=row['checkin_time'],
            scheduledetail_id=row['scheduledetail_id']
        ))
    db.close()
    return attendances

@staticmethod
def get_by_id(id: int) -> Attendances:
    db = Database()
    sql = "SELECT id, class_id, student_id, status, checkin_time, scheduledetail_id FROM Attendances WHERE id=%s"
    result = db.fetch_one(sql, (id,))
    if result:
        db.close()
        return Attendances(
            id=result['id'],
            class_id=result['class_id'],
            student_id=result['student_id'],
            status=result['status'],
            checkin_time=result['checkin_time'],
            scheduledetail_id=result['scheduledetail_id']
        )
    db.close()
    return None

@staticmethod
def get_by_student_id(student_id: int) -> list[Attendances]:
    db = Database()
    sql = "SELECT id, class_id, student_id, status, checkin_time, scheduledetail_id FROM Attendances WHERE student_id=%s"
    result = db.fetch_all(sql, (student_id,))
    attendances = []
    for row in result:
        attendances.append(Attendances(
            id=row['id'],
            class_id=row['class_id'],
            student_id=row['student_id'],
            status=row['status'],
            checkin_time=row['checkin_time'],
            scheduledetail_id=row['scheduledetail_id']
        ))
    db.close()
    return attendances

@staticmethod
def get_by_class_id(class_id: int) -> list[Attendances]:
    db = Database()
    sql = "SELECT id, class_id, student_id, status, checkin_time, scheduledetail_id FROM Attendances WHERE class_id=%s"
    result = db.fetch_one(sql, (class_id,))
    attendances = []
    for row in result:
        attendances.append(Attendances(
            id=row['id'],
            class_id=row['class_id'],
            student_id=row['student_id'],
            status=row['status'],
            checkin_time=row['checkin_time'],
            scheduledetail_id=row['scheduledetail_id']
        ))
    return attendances

@staticmethod
def get_addtendent_by_time(time=None, departmentid=None, studentid=None, teacherid=None) -> list[Attendances]:
    db = Database()
        
    if time:
        sql = "SELECT id, class_id, student_id, status, checkin_time, scheduledetail_id FROM Attendances WHERE DATE(checkin_time) = DATE(%s)"
        values = (time,)
    else:
        sql = "SELECT id, class_id, student_id, status, checkin_time, scheduledetail_id FROM Attendances WHERE DATE(checkin_time) = CURDATE()"
        values = ()

    if teacherid:
        sql += " AND student_id IN (SELECT id FROM student WHERE teacherid = %s)"
        values += (teacherid,)

    if departmentid:
        sql += " AND student_id IN (SELECT id FROM student WHERE departmentID = %s)"
        values += (departmentid,)

    if studentid:
        sql += " AND student_id = %s"
        values += (studentid,)
        
    try:
        result = db.fetch_all(sql, values)
        attendances = [Attendances(
            id=row['id'],
            class_id=row['class_id'],
            student_id=row['student_id'],
            status=row['status'],
            checkin_time=row['checkin_time'],
            scheduledetail_id=row['scheduledetail_id']
        ) for row in result]
        return attendances
    except Exception as e:
        print(f"Error while fetching attendance: {e}")
        return []
    finally:
        db.close()

@staticmethod
def count_attendance_by_time(time=None, departmentid=None,) -> int:
    db = Database()
    if time:
        sql = "SELECT COUNT(*) as total_student FROM attendances WHERE DATE(checkin_time) = DATE(%s)"
        values = (time,)
    else:
        sql = "SELECT COUNT(*) as total_student FROM attendances WHERE DATE(checkin_time) = CURDATE()"
        values = ()
    if departmentid:
        sql += " AND student_id IN (SELECT id FROM student WHERE departmentID = %s)"
        values += (departmentid,)
    result = db.fetch_one(sql, values)
    if result:
        db.close()
        return result['total_student']
    else:
        db.close()
        return None
        

@staticmethod
def get_attendance_list(time=None) -> list[StudentAttendenceDTO]:
    db = Database()
    if time:
        sql = "SELECT s.id, s.fullname, a.checkin_time, d.name as department_name FROM student s INNER JOIN attendances a ON s.id = a.student_id INNER JOIN department d ON s.`departmentID` = d.id WHERE DATE(a.checkin_time) = DATE(%s) ORDER BY a.checkin_time DESC"
        values = (time,)
    else:   
        sql = "SELECT s.id, s.fullname, a.checkin_time, d.name as department_name FROM student s INNER JOIN attendances a ON s.id = a.student_id INNER JOIN department d ON s.`departmentID` = d.id WHERE DATE(a.checkin_time) = CURDATE() ORDER BY a.checkin_time DESC"
        values = ()
    result = db.fetch_all(sql, values)
    student_attendance_list = []
    for row in result:
        student_attendance_list.append(StudentAttendenceDTO(row['id'], row['fullname'], row['checkin_time'], row['department_name']))
    db.close()
    return student_attendance_list

