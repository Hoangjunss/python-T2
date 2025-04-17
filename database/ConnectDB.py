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
        try:
            self.cursor.execute(query, values or ())
            if self.cursor.description:  # Đây là SELECT → cần fetch
                result = self.cursor.fetchall()
                return result
            else:  # Đây là INSERT, UPDATE, DELETE → commit
                self.conn.commit()
                return None
        except mysql.connector.Error as e:
            self.conn.rollback()
            print("Database error:", e)
            raise e

    def fetch_all(self, query, values=None):
        try:
            self.cursor.execute(query, values or ())
            return self.cursor.fetchall()
        except mysql.connector.Error as e:
            print("Database error (fetch_all):", e)
            raise e

    def fetch_one(self, query, values=None):
        try:
            self.cursor.execute(query, values or ())
            return self.cursor.fetchone()
        except mysql.connector.Error as e:
            print("Database error (fetch_one):", e)
            raise e

    def close(self):
        self.cursor.close()
        self.conn.close()
