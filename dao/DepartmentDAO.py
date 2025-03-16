from database.ConnectDB import Database
from models import Department

@staticmethod
def save(department):
    db = Database()
    query = "INSERT INTO departments (id, name) VALUES (%s, %s)"
    values = (department.id, department.name)
    db.exec_query(query, values)
    db.close()

@staticmethod
def update(department):
    db = Database()
    query = "UPDATE departments SET name = %s WHERE id = %s"
    values = (department.name, department.id)
    db.exec_query(query, values)
    db.close()

@staticmethod
def delete(department_id):
    db = Database()
    query = "DELETE FROM departments WHERE id = %s"
    values = (department_id,)
    db.exec_query(query, values)
    db.close()

@staticmethod
def get_all():
    db = Database()
    query = "SELECT * FROM departments"
    result = db.fetch_all(query)
    department = []
    for row in result:
        department.append(Department(*row))
    db.close()
    return department

@staticmethod
def get_by_id(department_id):
    db = Database()
    query = f"SELECT * FROM departments WHERE id = {department_id}"
    result = db.fetch_one(query)
    if result:
        db.close()
        return Department(*result)
    db.close()
    return None

@staticmethod
def count_students_by_department(department_id):
    db = Database()
    query = "SELECT COUNT(*) as total_student FROM student WHERE departmentID = %s"
    result = db.fetch_one(query, (department_id,))
    if result:
        db.close()
        return Department(*result)
    db.close()  
    return None
        