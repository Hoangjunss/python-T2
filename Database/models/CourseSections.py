from ConnectDB import Database

class CourseSections:
    def __init__(self, section_id, course_id, lecturer_id, room_number, start_date, end_date):
        self.section_id = section_id
        self.course_id = course_id
        self.lecturer_id = lecturer_id
        self.room_number = room_number
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        return f"CourseSections(section_id='{self.section_id}', course_id='{self.course_id}', lecturer_id='{self.lecturer_id}', room_number='{self.room_number}', start_date='{self.start_date}', end_date='{self.end_date}')"
    
    @staticmethod
    def get_all():
        db = Database()
        result = db.fetch_all("SELECT * FROM course_sections")
        db.close()
        return [CourseSections(*row) for row in result]
    
    @staticmethod
    def get_by_id(section_id):
        db = Database()
        result = db.fetch_one("SELECT * FROM course_sections WHERE section_id = %s", (section_id,))
        db.close()
        return CourseSections(*result) if result else None
        
    