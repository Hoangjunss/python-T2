import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="13524679",
            database="student_information_management"
        )
        self.cursor = self.conn.cursor()

    def exec_query(self, query, values=None):
        self.cursor.execute(query, values or ())
        self.conn.commit()
        self.cursor.close() 
        self.cursor = self.conn.cursor()

    def fetch_all(self, query, values=None):
        self.cursor.execute(query, values or ())
        return self.cursor.fetchall()

    def fetch_one(self, query, values=None):
        self.cursor.execute(query, values or ())
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.conn.close()