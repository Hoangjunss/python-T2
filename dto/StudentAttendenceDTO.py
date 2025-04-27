class StudentAttendenceDTO:
    def __init__(self, id, fullname, checkin_time, class_name):
        self.id = id
        self.fullname = fullname
        self.checkin_time = checkin_time
        self.class_name = class_name

    def __str__(self):
        return f"StudentAttendenceDTO(id={self.id}, fullname={self.fullname}, checkin_time={self.checkin_time}, class_name={self.class_name})"

    def __repr__(self):
        return self.__str__()
