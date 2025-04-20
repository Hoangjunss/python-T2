import os
import sys
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from gui.DepartmentScheduleFrame import DepartmentScheduleFrame
from models.Department import Department
from models.Semester import Semester
from models.Teacher import Teacher
from dao import DepartmentDAO, TeacherDAO, SemesterDAO
from gui.ListSchedule import ScheduleViewer

class ScheduleManager(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.configure(bg="white")
        self.create_widgets()

    def create_widgets(self):
        # Labels
        tk.Label(self, text="Trường Đại học Sài Gòn", font=("Arial", 13), fg="black", bg="white").place(x=0, y=0)

        self.department_data = self.fetch_departments()
        self.selected_department = tk.StringVar()
        self.department_combobox = ttk.Combobox(self, textvariable=self.selected_department, state="readonly", width=30)
        self.department_combobox['values'] = [f"{d.name}" for d in self.department_data]
        if self.department_data:
            self.selected_department.set(self.department_data[0].name)  # Chọn tên khoa đầu tiên
        self.department_combobox.place(x=900, y=30)
        self.department_combobox.bind("<<ComboboxSelected>>", self.on_combobox_change)


        self.teacher = self.fetch_teacher_by_department_id(self.department_data[0].dean_id)
        self.teacher_name = tk.StringVar()
        self.teacher_name.set(self.teacher.fullname)
        self.department_name = self.department_data[0].name
        self.label_department_name = tk.Label(self, text=self.department_name, font=("Arial", 20, "italic"), fg="red", bg="white").place(x=100, y=75)
        tk.Label(self, text="Trưởng Khoa:", font=("Arial", 20), fg="red", bg="white").place(x=550, y=75)
        self.label_teacher_name = tk.Label(self, textvariable=self.teacher_name, font=("Arial", 20), fg="black", bg="white")
        self.label_teacher_name.place(x=720, y=75)

        # Treeview
        self.list = ttk.Treeview(self)
        self.list.place(x=100, y=130)

        styleList = ttk.Style()
        styleList.configure("Treeview", rowheight=60, font=("Arial", 16))
        styleList.configure("Treeview.Heading", font=("Arial", 18, "bold"), foreground="red", background="red")

        self.list["columns"] = ("Học Kỳ", "Ngày bắt đầu", "Ngày kết thúc")
        self.list.column("#0", width=100, anchor="center")
        self.list.column("Học Kỳ", width=200, anchor="center")
        self.list.column("Ngày bắt đầu", width=300, anchor="center")
        self.list.column("Ngày kết thúc", width=400, anchor="center")

        self.list.heading("#0", text="ID", anchor="center")
        self.list.heading("Học Kỳ", text="Học Kỳ", anchor="center")
        self.list.heading("Ngày bắt đầu", text="Ngày bắt đầu", anchor="center")
        self.list.heading("Ngày kết thúc", text="Ngày kết thúc", anchor="center")

        self.populate_data(self.department_data[0].id)

        # Buttons
        tk.Button(self, text="Xem lịch học", font=("Arial", 17), bd=0, bg="red", fg="white", width=15, command=self.view_schedule).place(x=1200, y=130)
        tk.Button(self, text="Thêm lịch học", font=("Arial", 17), bd=0, bg="red", fg="white", width=15, command=self.add_schedule).place(x=1200, y=200)
        tk.Button(self, text="Xóa lịch học", font=("Arial", 17), bd=0, bg="red", fg="white", width=15, command=self.erase_schedule).place(x=1200, y=270)

    def on_combobox_change(self, event):
        selected_index = self.department_combobox.current()
        if selected_index >= 0:
            department = self.department_data[selected_index]
            teacher = self.fetch_teacher_by_department_id(department.id)
            print(f"Bạn đã chọn: ID = {department.id}, Tên Khoa = {department.name}")

            self.department_name =department.name
            self.teacher_name.set(self.teacher.fullname)

    def fetch_teacher_by_department_id(self, department_id) -> Teacher:
        teachers = TeacherDAO.get_by_id(department_id)
        return teachers

    def fetch_departments(self) -> list[Department]:
        return DepartmentDAO.get_all()
    
    def fetch_semester_by_department_id(self, department_id) -> list[Semester]:
        semesters = SemesterDAO.get_by_department_id(department_id)
        return semesters


    def populate_data(self, department_id):
        # Xóa dữ liệu cũ
        for item in self.list.get_children():
            self.list.delete(item)

        # Thêm dữ liệu mới
        list_semester = self.fetch_semester_by_department_id(department_id)
        for semester in list_semester:
            self.list.insert("", "end", text=semester.id, values=(semester.name, semester.startdate, semester.enddate))

    def view_schedule(self):
        print("Xem Lịch học")
        
        # selected_items = self.list.selection()
        # if selected_items:
        #     selected_item = selected_items[0]

        #     semester_id = self.list.item(selected_item, "text")
        #     values = self.list.item(selected_item, "values")

        #     selected_index = self.department_combobox.current()
        #     if selected_index >= 0:
        #         department = self.department_data[selected_index]
        #         departmentID = department.id
        #         self.viewer = ScheduleViewer(self, departmentID, semester_id)
        #     else:
        #         messagebox.showwarning("Cảnh báo", "Vui lòng chọn khoa hợp lệ.")
        # else:
        #     messagebox.showwarning("Cảnh báo", "Vui lòng chọn dòng trong bảng.")
        self.viewer = DepartmentScheduleFrame(self, 1)



    def add_schedule(self):
        print("Thêm lịch học")

    def erase_schedule(self):
        print("Xóa lịch học")



if __name__ == "__main__":
    app = ScheduleManager()
    app.mainloop()
