import uuid
from database.ConnectDB import Database

class ScheduleDetail: 
    def __init__(self, id, scheduleId, dayOfWeek, startTime, endTime):
        self.id = id
        self.scheduleId = scheduleId
        self.dayOfWeek = dayOfWeek
        self.startTime = startTime
        self.endTime = endTime

    def __str__(self):
        return f"ScheduleDetail(id={self.id}, scheduleId={self.scheduleId}, dayOfWeek='{self.dayOfWeek}', startTime='{self.startTime}', endTime='{self.endTime}')"
    
    @staticmethod
    def save(schedule):
        db = Database()
        query = f"""
            INSERT INTO ScheduleDetail (id, scheduleId, dayOfWeek, startTime, endTime)
            VALUES ('{schedule.id}', '{schedule.scheduleId}', '{schedule.dayOfWeek}', '{schedule.startTime}', '{schedule.endTime}');
        """
        db.exec_query(query)
        db.close()

    @staticmethod
    def get_all():
        db = Database()
        query = "SELECT * FROM ScheduleDetail"
        result = db.fetch_all(query)
        scheduleDetail = []
        for row in result:
            scheduleDetail.append(ScheduleDetail(*row))
        db.close()
        return scheduleDetail
    
    @staticmethod
    def get_by_id(scheduleDetailId):
        db = Database()
        query = f"SELECT * FROM ScheduleDetail WHERE id = '{scheduleDetailId}'"
        result = db.fetch_one(query)
        if result:
            scheduleDetail = ScheduleDetail(*result)
            db.close()
            return scheduleDetail
        db.close()
        return None
    
    @staticmethod
    def update(scheduledetail):
        db = Database()
        query = f"""
            UPDATE scheduledetail SET scheduleID={scheduledetail.scheduleID}, 
            dayOfWeek='{scheduledetail.dayOfWeek}', startTime='{scheduledetail.startTime}', endTime='{scheduledetail.endTime}'
            WHERE id = '{scheduledetail.id}';
            """
        db.exec_query(query)
        db.close()

    @staticmethod
    def delete(scheduledetailId):
        db = Database()
        query = f"DELETE FROM ScheduleDetail WHERE id = '{scheduledetailId}'"
        db.exec_query(query)
        db.close()

    def get_generation_id():
        u = uuid.uuid4()
        msb = u.int >> 64
        result = msb & 0xFFFFFFFF
        if result >= 0x80000000:
            result -= 0x100000000
        return result
    
