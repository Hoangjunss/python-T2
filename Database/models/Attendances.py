from ConnectDB import Database

class Attendances:
    def __init__(self, attendance_id, session_id, status, recorded_at, image_recorded):
        self.attendance_id = attendance_id
        self.session_id = session_id
        self.status = status
        self.recorded_at = recorded_at
        self.image_recorded = image_recorded

    def __str__(self):
        return f"Attendances(attendance_id={self.attendance_id}, session_id={self.session_id}, status={self.status}, recorded_at={self.recorded_at}, image_recorded={self.image_recorded})"
    
    @staticmethod
    def get_all():
        db = Database()
        query = "SELECT * FROM attendances"
        return db.fetch_all(query)
    
    @staticmethod
    def get_by_student_id(student_id):
        db = Database()
        query = f"SELECT * FROM attendances WHERE student_id = {student_id}"
        return db.fetch_all(query)
        
    @staticmethod
    def find_by_session_id(session_id):
        db = Database()
        query = f"SELECT * FROM attendances WHERE session_id = {session_id}"
        return db.fetch_all(query)