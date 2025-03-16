class Class:
    def __init__(self, 
                id=None, 
                name=None, 
                grade_level=None, 
                teacher_id=None, 
                academic_year=None, 
                room=None, 
                total_student=None, 
                description=None):
        self.id = id
        self.name = name
        self.grade_level = grade_level
        self.teacher_id = teacher_id
        self.academic_year = academic_year
        self.room = room
        self.total_student = total_student
        self.description = description

    def __str__(self):
        return f"Class(id = {self.id}, name = {self.name}, grade_level = {self.grade_level}, teacher_id = {self.teacher_id}, academic_academic = {self.academic_year}, room = {self.room}, total_student = {self.total_student}, description = {self.description})"
