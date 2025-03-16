
class ScheduleDetail: 
    def __init__(self, id, scheduleId, dayOfWeek, startTime, endTime):
        self.id = id
        self.scheduleId = scheduleId
        self.dayOfWeek = dayOfWeek
        self.startTime = startTime
        self.endTime = endTime

    def __str__(self):
        return f"ScheduleDetail(id={self.id}, scheduleId={self.scheduleId}, dayOfWeek='{self.dayOfWeek}', startTime='{self.startTime}', endTime='{self.endTime}')"
    