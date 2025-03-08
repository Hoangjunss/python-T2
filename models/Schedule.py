from database.ConnectDB import Database

class Schedule:
    def __init__(self, id, departmentId, semesterId, description):
        self.id = id
        self.departmentId = departmentId
        self.semesterId = semesterId
        self.description = description  

    def __str__(self):
        return f"Schedule(id={self.id}, departmentId={self.departmentId}, semesterId={self.semesterId}, description={self.description})"
        
    @staticmethod
    def save(schedule):
        db = Database()
        query = f""" INSERT INTO schedule(id, departmentID, semesterID, description) VALUES (
            {schedule.id}, {schedule.departmentId}, {schedule.semesterId}, {schedule.description}
        ) """
        db.exec_query(query)
        db.close()

    @staticmethod
    def get_all():
        db = Database()
        query = "SELECT * FROM schedule"
        result = db.fetch_all(query)
        schedules = []
        for row in result:
            schedules.append(Schedule(*row))
        db.close()
        return schedules
    
    @staticmethod
    def get_by_id(scheduleId):
        db = Database()
        query = f"SELECT * FROM schedule WHERE id = {scheduleId}"
        result = db.fetch_one(query)
        if result:
            schedule = Schedule(*result)
            db.close()
            return schedule
        db.close()

    @staticmethod
    def update(schedule):
        db = Database()
        query = f""" UPDATE schedule SET departmentId = {schedule.departmentId}, semesterId = {schedule.semesterId}, description = {schedule.description} 
            WHERE id = {schedule.id} 
        """
        db.exec_query(query)
        db.close()

    def delete(scheduleId):
        db = Database()
        query = f"DELETE FROM schedule WHERE id = {scheduleId}"
        db.exec_query(query)
        db.close()