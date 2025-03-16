from database.ConnectDB import Database

class Department:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"Department(id={self.id}, name='{self.name}')"
    
    @staticmethod
    def save(department):
        db = Database()
        query = f"INSERT INTO departments (id, name) VALUES ({department.id}, '{department.name}')"
        db.exec_query(query)
        db.close()
    
    @staticmethod
    def get_all_departments():
        db = Database()
        query = "SELECT * FROM Department"
        result = db.fetch_all(query)
        department = []
        for row in result:
            department.append(Department(*row))
        db.close()
        return department
    
    @staticmethod
    def get_department_by_id(department_id):
        db = Database()
        query = f"SELECT * FROM Department WHERE id = {department_id}"
        result = db.fetch_one(query)
        if result:
            department = Department(*result)
            db.close()
            return department
        db.close()
        return None
    
    @staticmethod
    def update(department):
        db = Database()
        query = f"UPDATE departments SET name = '{department.name}' WHERE id = {department.id}"
        db.exec_query(query)
        db.close()

    @staticmethod
    def delete(department_id):
        db = Database()
        query = f"DELETE FROM departments WHERE id = {department_id}"
        db.exec_query(query)
        db.close()

    @staticmethod
    def count_students_by_department(department_id):
        db = Database()
        query = "SELECT COUNT(*) as total_student FROM student WHERE departmentID = %s"
        result = db.fetch_one(query, (department_id,))
        if result:
            db.close()
            return result[0]
        db.close()  
        return 0
        
