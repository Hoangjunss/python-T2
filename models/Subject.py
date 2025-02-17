from database.ConnectDB import Database

class Subject:
    def __init__(self, 
                id=None, 
                name=None, 
                numberOfLessons=None):
        self.id = id
        self.name = name
        self.numberOfLessons = numberOfLessons

    def __str__(self):
        return f"Subject(id={self.id}, name='{self.name}', numberOfLessons={self.numberOfLessons})"

    @staticmethod
    def save(subject):
        db = Database()
        query = f"""
            INSERT INTO Subject (name, numberOfLessons)
            VALUES ('{subject.name}', {subject.numberOfLessons});
        """
        db.exec_query(query)
        db.close()

    @staticmethod
    def get_all():
        db = Database()
        query = "SELECT * FROM Subject"
        result = db.fetch_all(query)
        subjects = []
        for row in result:
            subjects.append(Subject(*row))
        db.close()
        return subjects

    @staticmethod
    def get_by_id(subject_id):
        db = Database()
        query = f"SELECT * FROM Subject WHERE id = {subject_id}"
        result = db.fetch_one(query)
        if result:
            subject = Subject(*result[0])
            db.close()
            return subject
        db.close()
        return None

    @staticmethod
    def update(subject):
        db = Database()
        query = f"""
            UPDATE Subject
            SET name = '{subject.name}', numberOfLessons = {subject.numberOfLessons}
            WHERE id = {subject.id};
        """
        db.exec_query(query)
        db.close()

    @staticmethod
    def delete(subject_id):
        db = Database()
        query = f"DELETE FROM Subject WHERE id = {subject_id};"
        db.exec_query(query)
        db.close()
