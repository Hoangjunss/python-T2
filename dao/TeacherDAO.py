from database.ConnectDB import Database
from models.Teacher import Teacher

@staticmethod
def save(teacher: Teacher):
    db = Database()
    query = "INSERT INTO teacher (id, fullname, gender, status, address, email, phone, department_id, username, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s,%s)"
    values = (teacher.id, teacher.fullname, teacher.gender, teacher.status, teacher.address, teacher.email, teacher.phone, teacher.department_id, teacher.username, teacher.password)
    db.exec_query(query, values)
    db.close()

@staticmethod
def update(teacher: Teacher):
    db = Database()
    query = "UPDATE teacher SET fullname=%s, gender=%s, status=%s, address=%s, email=%s, phone=%s, department_id=%s ,username=%s,password=%s WHERE id=%s"
    values = (teacher.fullname, teacher.gender, teacher.status, teacher.address, teacher.email, teacher.phone, teacher.department_id,teacher.username,teacher.password, teacher.id)
    db.exec_query(query, values)
    db.close()

@staticmethod
def delete(teacher_id: int):
    db = Database()
    query = "DELETE FROM teacher WHERE id=%s"
    values = (teacher_id,)
    db.exec_query(query, values)
    db.close()

@staticmethod
def get_by_id(teacher_id: int) -> Teacher:
    db = Database()
    query = "SELECT id, fullname, gender, status, address, email, phone, department_id, username, password FROM teacher WHERE id=%s"
    values = (teacher_id,)
    result = db.fetch_one(query, values)
    db.close()
    if result:
        return Teacher(
            id=result['id'],
            fullname=result['fullname'],
            gender=result['gender'],
            status=result['status'],
            address=result['address'],
            email=result['email'],
            phone=result['phone'],
            department_id=result['department_id'],
            username=result['username'],
            password=result['password']
        )
    return None

@staticmethod
def get_all() -> list[Teacher]:
    db = Database()
    query = "SELECT id, fullname, gender, status, address, email, phone, department_id, username, password FROM teacher"
    result = db.fetch_all(query)
    teachers = []
    for row in result:
        teachers.append(Teacher(
            id=row['id'],
            fullname=row['fullname'],
            gender=row['gender'],
            status=row['status'],
            address=row['address'],
            email=row['email'],
            phone=row['phone'],
            department_id=row['department_id'],
            username=row['username'],
            password=row['password']
        ))
    db.close()
    return teachers

@staticmethod
def get_by_username(username: str) -> Teacher:
    db = Database()
    query = "SELECT id, fullname, gender, status, address, email, phone, department_id, username, password FROM teacher WHERE username=%s"
    values = (username,)
    result = db.fetch_one(query, values)
    db.close()
    if result:
        return Teacher(
            id=result['id'],
            fullname=result['fullname'],
            gender=result['gender'],
            status=result['status'],
            address=result['address'],
            email=result['email'],
            phone=result['phone'],
            department_id=result['department_id'],
            username=result['username'],
            password=result['password']
        )
    return None

@staticmethod
def get_by_username_and_password(username: str, password: str) -> Teacher:
    db = Database()
    query = "SELECT id, fullname, gender, status, address, email, phone, department_id, username, password FROM teacher WHERE username=%s AND password=%s"
    values = (username, password)
    result = db.fetch_one(query, values)
    db.close()
    if result:
        return Teacher(
            id=result['id'],
            fullname=result['fullname'],
            gender=result['gender'],
            status=result['status'],
            address=result['address'],
            email=result['email'],
            phone=result['phone'],
            department_id=result['department_id'],
            username=result['username'],
            password=result['password']
        )
    return None


@staticmethod
def get_by_department_id(department_id: int) -> list[Teacher]:
    db = Database()
    query = "SELECT id, fullname, gender, status, address, email, phone, username, password FROM teacher WHERE department_id=%s"
    values = (department_id,)
    result = db.fetch_all(query, values)
    teachers = []
    for row in result:
        teachers.append(Teacher(
            id=row['id'],
            fullname=row['fullname'],
            gender=row['gender'],
            status=row['status'],
            address=row['address'],
            email=row['email'],
            phone=row['phone'],
            username=row['username'],
            password=row['password']
        ))
    db.close()
    return teachers