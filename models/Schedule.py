from database.ConnectDB import Database

class Schedule:
    def __init__(self, id, departmentId, semesterId):
        self.id = id
        self.departmentId = departmentId
        self.semesterId = semesterId

    def __str__(self):
        return f"Schedule(id={self.id}, departmentId={self.departmentId}, semesterId={self.semesterId})"
        