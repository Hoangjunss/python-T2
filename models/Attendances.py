
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
