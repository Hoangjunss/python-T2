from database.ConnectDB import Database

class SchoolClass:
    def __init__(self, 
                id=None, 
                name=None, 
                grade_level=None, 
                homeroom_teacher_name=None, 
                academic_year=None, 
                room=None, 
                total_student=None, 
                description=None):
        self.id = id
        self.name = name
        self.grade_level = grade_level
        self.homeroom_teacher_name = homeroom_teacher_name
        self.academic_year = academic_year
        self.room = room
        self.total_student = total_student
        self.description = description

    def __str__(self):
        return f"Class(id = {self.id}, name = {self.name}, grade_level = {self.grade_level}, 
                    homeroom_teacher_name = {self.homeroom_teacher_name}, academic_academic = {self.academic_year}, 
                    room = {self.room}, total_student = {self.total_student}, description = {self.description})"

    @staticmethod
    def save(school_class):
        db = Database()
        query = f"""
            INSERT INTO Class (name, grade_level, homeroom_teacher_name, academic_year, room, total_student, description)
            VALUES ('{school_class.name}', {school_class.grade_level}, '{school_class.homeroom_teacher_name}',
                    '{school_class.academic_year}', '{school_class.room}', {school_class.total_student},
                    '{school_class.description}');
        """
        db.exec_query(query)
        db.close()

    @staticmethod
    def get_all():
        db = Database()
        query = "SELECT * FROM Class"
        result = db.fetch_all(query)
        classes = []
        for row in result:
            classes.append(SchoolClass(*row))
        db.close()
        return classes

    @staticmethod
    def get_by_id(class_id):
        db = Database()
        query = f"SELECT * FROM Class WHERE id = {class_id}"
        result = db.fetch_one(query)
        if result:
            school_class = SchoolClass(*result[0])
            db.close()
            return school_class
        db.close()
        return None

    @staticmethod
    def update(school_class):
        db = Database()
        query = f"""
            UPDATE Class
            SET name = '{school_class.name}',
                grade_level = {school_class.grade_level},
                homeroom_teacher_name = '{school_class.homeroom_teacher_name}',
                academic_year = '{school_class.academic_year}',
                room = '{school_class.room}',
                total_student = {school_class.total_student},
                description = '{school_class.description}'
            WHERE id = {school_class.id};
        """
        db.exec_query(query)
        db.close()

    @staticmethod
    def delete(class_id):
        db = Database()
        query = f"DELETE FROM Class WHERE id = {class_id};"
        db.exec_query(query)
        db.close()
        