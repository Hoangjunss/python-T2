import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="student_information_management"
        )
        self.cursor = self.conn.cursor()

    def exec_query(self, query, values=None):
        try:
            self.cursor.execute(query, values or ())
            self.conn.commit() 
        except mysql.connector.Error as e:
            self.conn.rollback() 
            print("Database error:", e)
            raise e 


    def fetch_all(self, query, values=None):
        self.cursor.execute(query, values or ())
        return self.cursor.fetchall()

    def fetch_one(self, query, values=None):
        self.cursor.execute(query, values or ())
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.conn.close()