class Schedule:
    def __init__(self, id, departmentId, semesterId, description):
        self.id = id
        self.departmentId = departmentId
        self.semesterId = semesterId
        self.description = description  

    def __str__(self):
        return f"Schedule(id={self.id}, departmentId={self.departmentId}, semesterId={self.semesterId}, description={self.description})"
      