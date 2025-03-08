from database.ConnectDB import Database

class Semester:
    def __init__(self, id, name, startdate, enddate):
        self.id = id
        self.name = name
        self.startdate = startdate
        self.enddate = enddate

    def __str__(self):
        return f"Semester(id={self.id}, name='{self.name}', startdate={self.startdate}, enddate={self.enddate})"
    
    @staticmethod
    def save(semester):
        db = Database()
        query = f"""
            INSERT INTO Semester (name, startdate, enddate)
            VALUES ('{semester.name}', '{semester.startdate}', '{semester.enddate}');
        """
        db.exec_query(query)
        db.close()

    @staticmethod
    def get_all():
        db = Database()
        query = "SELECT * FROM Semester"
        result = db.fetch_all(query)
        semesters = []
        for row in result:
            semesters.append(Semester(*row))
        db.close()
        return semesters
    
    @staticmethod
    def get_by_id(semester_id):
        db = Database()
        query = f"SELECT * FROM Semester WHERE id = {semester_id}"
        result = db.fetch_one(query)
        if result:
            db.close()
            return Semester(*result)
        db.close()

    @staticmethod
    def update(semester):
        db = Database()
        query = f"""
            UPDATE Semester
            SET name='{semester.name}', startdate='{semester.startdate}', enddate='{semester.enddate}'
            WHERE id={semester.id};
        """
        db.exec_query(query)
        db.close()

    @staticmethod
    def delete(semester_id):
        db = Database()
        query = f"DELETE FROM Semester WHERE id = {semester_id};"
        db.exec_query(query)
        db.close()