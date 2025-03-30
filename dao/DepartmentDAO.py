from database.ConnectDB import Database
from models.Department import Department

@staticmethod
def save(department: Department):
    db = Database()
    query = "INSERT INTO department (id, name, dean_id) VALUES (%s, %s, %s)"
    values = (department.id, department.name, department.dean_id)
    db.exec_query(query, values)
    db.close()

@staticmethod
def update(department: Department):
    db = Database()
    query = "UPDATE department SET name = %s, dean_id = %s WHERE id = %s"
    values = (department.name, department.dean_id, department.id)
    db.exec_query(query, values)
    db.close()

@staticmethod
def delete(department_id: int):
    db = Database()
    query = "DELETE FROM department WHERE id = %s"
    values = (department_id,)
    db.exec_query(query, values)
    db.close()

@staticmethod
def get_all() -> list[Department]:
    db = Database()
    query = "SELECT * FROM department"
    result = db.fetch_all(query)
    department = []
    for row in result:
        department.append(Department(*row))
    db.close()
    return department

@staticmethod
def get_by_id(department_id: int) -> Department:
    db = Database()
    query = f"SELECT * FROM department WHERE id = {department_id}"
    result = db.fetch_one(query)
    if result:
        db.close()
        return Department(*result)
    db.close()
    return None

@staticmethod
def count_students_by_department(department_id: int) -> int:
    db = Database()
    query = "SELECT COUNT(*) as total_student FROM student WHERE departmentID = %s"
    result = db.fetch_one(query, (department_id,))
    if result:
        db.close()
        return result
    db.close()  
    return None
        