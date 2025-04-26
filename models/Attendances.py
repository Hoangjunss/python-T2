
class Attendances:
    def __init__(self, id=None, class_id=None, student_id=None, status=None, checkin_time=None, scheduledetail_id=None):
        self.id = id
        self.class_id = class_id
        self.student_id = student_id
        self.status = status
        self.checkin_time = checkin_time
        self.scheduledetail_id = scheduledetail_id

    def __str__(self):
        return (f"Attendances(id={self.id}, class_id={self.class_id}, student_id={self.student_id}, "
                f"status='{self.status}', checkin_time='{self.checkin_time}')")
