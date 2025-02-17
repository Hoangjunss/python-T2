from database.ConnectDB import Database

class Attendances:
    def __init__(self, id, class_id, student_id, status, checkin_time):
        self.id = id
        self.class_id = class_id
        self.student_id = student_id
        self.status = status
        self.checkin_time = checkin_time

    def __str__(self):
        return (f"Attendances(id={self.id}, class_id={self.class_id}, student_id={self.student_id}, "
                f"status='{self.status}', checkin_time='{self.checkin_time}')")

    @staticmethod
    def save(attendances):
        db = Database()
        query = f"""
            INSERT INTO Attendances (class_id, student_id, status, checkin_time)
            VALUES ({attendances.class_id}, {attendances.student_id}, '{attendances.status}', '{attendances.checkin_time}');
        """
        db.exec_query(query)
        db.close()

    @staticmethod
    def get_all():
        db = Database()
        query = "SELECT * FROM Attendances"
        result = db.fetch_all(query)
        attendances = []
        for row in result:
            attendances.append(Attendances(*row))
        db.close()
        return attendances

    @staticmethod
    def get_by_id(attendances_id):
        db = Database()
        query = f"SELECT * FROM Attendances WHERE id = {attendances_id}"
        result = db.fetch_one(query)
        if result:
            attendances = Attendances(*result[0])
            db.close()
            return attendances
        db.close()
        return None

    @staticmethod
    def update(attendances):
        db = Database()
        query = f"""
            UPDATE Attendances
            SET class_id = {attendances.class_id},
                student_id = {attendances.student_id},
                status = '{attendances.status}',
                checkin_time = '{attendances.checkin_time}'
            WHERE id = {attendances.id};
        """
        db.exec_query(query)
        db.close()

    @staticmethod
    def delete(attendances_id):
        db = Database()
        query = f"DELETE FROM RollCall WHERE id = {attendances_id};"
        db.exec_query(query)
        db.close()
