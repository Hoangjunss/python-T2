class Semester:
    def __init__(self, id, name, startdate, enddate):
        self.id = id
        self.name = name
        self.startdate = startdate
        self.enddate = enddate

    def __str__(self):
        return f"Semester(id={self.id}, name='{self.name}', startdate={self.startdate}, enddate={self.enddate})"
