from dao.StudentDAO import StudentDAO

from models.Students import Student

class TestDAO:
    def __init__(self):
        print("Test class initialized.")
        self.student_dao = StudentDAO()

    def save(self):
        try:
            student = Student(id=23453, fullname="John Doe")
            
            self.student_dao.save()
            print("Student saved successfully.")
        except Exception as e:
            print(f"Error while saving student: {e}")


