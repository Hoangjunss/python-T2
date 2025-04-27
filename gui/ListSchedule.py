import tkinter as tk
from tkinter import ttk
import random

class ScheduleViewer:
    def __init__(self, parent_frame, departmentID=None, semester_id=None):
        self.frame = parent_frame
        self.subjects = [
            "Lập trình Python", "Cấu trúc dữ liệu & Giải thuật", "Hệ điều hành", "Lập trình Web",
            "Cơ sở dữ liệu", "Mạng máy tính", "Trí tuệ nhân tạo", "Học máy", "Phát triển ứng dụng di động",
            "Lập trình Java", "Khoa học dữ liệu", "Bảo mật mạng", "Phát triển phần mềm", "Điện toán đám mây",
            "Kỹ thuật lập trình", "Hệ thống nhúng", "Blockchain", "Công nghệ phần mềm", "Xử lý ảnh",
            "Phân tích dữ liệu"
        ]
        self.columns = ["Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5", "Thứ 6", "Thứ 7", "Chủ nhật"]
        self.listTime = ["7.50", "8.40", "9.50", "10.40", "11.30", "13.50", "14.40", "15.50", "16.40", "17.30"]

        self.listSchedule = ttk.Treeview(self.frame)
        self.setup_schedule_treeview()
        if departmentID and semester_id:
            self.populate_schedule

    def setup_schedule_treeview(self):
        self.listSchedule.place(x=100, y=110)
        self.listSchedule["column"] = tuple(self.columns)
        self.listSchedule.column("#0", width=150, anchor="center")

        for col in self.columns:
            self.listSchedule.column(col, width=180, anchor="center")
            self.listSchedule.heading(col, text=col, anchor="center")

        self.listSchedule.column("Chủ nhật", width=130)
        self.listSchedule.heading("#0", text="Giờ/Thứ", anchor="center")

        styleListSchedule = ttk.Style()
        styleListSchedule.configure("Treeview", rowheight=60, font=("Arial", 16))
        styleListSchedule.configure("Treeview.Heading", font=("Arial", 18, "bold"),
                                    foreground="red", background="blue")

    def populate_schedule(self, department_id, semester_id):
        self.clear_treeview()
        # Giả lập dữ liệu theo department_id (bạn có thể thay bằng truy vấn thực)
        for time in self.listTime:
            row_values = [random.choice(self.subjects) for _ in range(len(self.columns) - 1)] + ["Nghỉ"]
            self.listSchedule.insert("", "end", text=time, values=row_values)

    def clear_treeview(self):
        for i in self.listSchedule.get_children():
            self.listSchedule.delete(i)
