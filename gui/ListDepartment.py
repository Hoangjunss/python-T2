import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from models.Department import Department
from models.Semester import Semester
from models.Teacher import Teacher
from dao import DepartmentDAO, TeacherDAO, SemesterDAO
from gui.ListSchedule import ScheduleViewer

class ScheduleManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Khoa")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}")

        self.frame = tk.Frame(self.root, bg="white")
        self.frame.place(x=0, y=0, width=screen_width, height=screen_height)

        self.create_widgets()

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

    def create_widgets(self):
        # Labels
        tk.Label(self.frame, text="Trường Đại học Sài Gòn", font=("Times New Roman", 13), fg="black", bg="white").place(x=0, y=0)

        self.department_data = self.fetch_departments()
        self.selected_department = tk.StringVar()
        self.department_combobox = ttk.Combobox(self.frame, textvariable=self.selected_department, state="readonly", width=30)
        self.department_combobox['values'] = [f"{d.name}" for d in self.department_data]
        if self.department_data:
            self.selected_department.set(self.department_data[0].name)  # Chọn tên khoa đầu tiên
        self.department_combobox.place(x=900, y=30)
        self.department_combobox.bind("<<ComboboxSelected>>", self.on_combobox_change)


        self.teacher = self.fetch_teacher_by_department_id(self.department_data[0].dean_id)
        self.teacher_name = tk.StringVar()
        self.teacher_name.set(self.teacher.fullname)
        self.department_name = self.department_data[0].name
        self.label_department_name = tk.Label(self.frame, text=self.department_name, font=("Times New Roman", 20, "italic"), fg="red", bg="white").place(x=100, y=75)
        tk.Label(self.frame, text="Trưởng Khoa:", font=("Times New Roman", 20), fg="red", bg="white").place(x=550, y=75)
        self.label_teacher_name = tk.Label(self.frame, textvariable=self.teacher_name, font=("Times New Roman", 20), fg="black", bg="white")
        self.label_teacher_name.place(x=720, y=75)

        # Treeview
        self.list = ttk.Treeview(self.frame)
        self.list.place(x=100, y=130)

        styleList = ttk.Style()
        styleList.configure("Treeview", rowheight=60, font=("Times New Roman", 16))
        styleList.configure("Treeview.Heading", font=("Times New Roman", 18, "bold"), foreground="red", background="red")

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
        tk.Button(self.frame, text="Xem lịch học", font=("Times New Roman", 17), bd=0, bg="red", fg="white", width=15, command=self.view_schedule).place(x=1200, y=130)
        tk.Button(self.frame, text="Thêm lịch học", font=("Times New Roman", 17), bd=0, bg="red", fg="white", width=15, command=self.add_schedule).place(x=1200, y=200)
        tk.Button(self.frame, text="Xóa lịch học", font=("Times New Roman", 17), bd=0, bg="red", fg="white", width=15, command=self.erase_schedule).place(x=1200, y=270)



    def populate_data(self, department_id):
        # print(self.get_all_schedule())
        list_semester = self.fetch_semester_by_department_id(department_id)
        for semester in list_semester:
            self.list.insert("", "end", text=semester.id, values=(semester.name, semester.startdate, semester.enddate))
        

    def view_schedule(self):
        print("Xem Lịch học")
        
        selected_items = self.list.selection()
        if selected_items:
            selected_item = selected_items[0]

            semester_id = self.list.item(selected_item, "text")
            values = self.list.item(selected_item, "values")

            selected_index = self.department_combobox.current()
            if selected_index >= 0:
                department = self.department_data[selected_index]
                departmentID = department.id
                self.viewer = ScheduleViewer(self.frame, departmentID, semester_id)
            else:
                messagebox.showwarning("Cảnh báo", "Vui lòng chọn khoa hợp lệ.")
        else:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn dòng trong bảng.")



    def add_schedule(self):
        print("Thêm lịch học")

    def erase_schedule(self):
        print("Xóa lịch học")



if __name__ == "__main__":
    root = tk.Tk()
    app = ScheduleManager(root)
    root.mainloop()
