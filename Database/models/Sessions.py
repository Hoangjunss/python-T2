from ConnectDB import Database

class Sessions:
    def __init__(self, session_id, section_id, session_date, topic, is_cancelled):
        self.session_id = session_id
        self.section_id = section_id
        self.session_date = session_date
        self.topic = topic
        self.is_cancelled = is_cancelled

    def __str__(self):
        return f"Session ID: {self.session_id}, Section ID: {self.section_id}, Session Date: {self.session_date}, Topic: {self.topic}, Is Cancelled: {self.is_cancelled}"
    
    @staticmethod
    def get_all():
        db = Database()
        sessions = []
        result = db.fetch_all("SELECT * FROM sessions")
        for row in result:
            sessions.append(Sessions(row[0], row[1], row[2], row[3], row[4]))
        db.close()
        return sessions

    @staticmethod
    def get_by_id(session_id):
        db = Database()
        session = db.fetch_one("SELECT * FROM sessions WHERE session_id = %s", (session_id,))
        if session:
            return Sessions(session[0], session[1], session[2], session[3], session[4])
        db.close()
        return None