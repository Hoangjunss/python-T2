from database.ConnectDB import Database


@staticmethod
def delete_by_student_id(student_id: int) -> None:
    db = Database()
    sql = "DELETE FROM faceendcoding WHERE student_id=%s"
    db.exec_query(sql, (student_id,))
    db.close()