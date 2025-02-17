from ConnectDB import Database

class Courses:
    def __init__(self, course_id, course_code, course_name, credits, department_id):
        self.course_id = course_id
        self.course_code = course_code
        self.course_name = course_name
        self.credits = credits
        self.department_id = department_id

    def __str__(self):
        return f"Course ID: {self.course_id}, Course Code: {self.course_code}, Course Name: {self.course_name}, Credits: {self.credits}, Department ID: {self.department_id}"
    
    @staticmethod
    def find_by_id(self, id):
        db = Database()
        query = "SELECT * FROM courses WHERE course_id = %s"
        result = db.exec_query(query, (id,))
        db.close()
        return result[0] if result else None
    
    @staticmethod
    def get_all():
        db = Database()
        query = "SELECT * FROM Courses"
        result = db.exec_query(query)
        db.close()
        return [Courses(*row) for row in result]
    
    