import tkinter as tk
from tkinter import ttk, messagebox
from models.Students import Student

class StudentApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Student CRUD Application")
        self.geometry("1000x600")
        self.selected_student_id = None
        self.create_widgets()
        self.refresh_student_list()

    def create_widgets(self):
        # Frame cho các entry input
        frame_input = tk.Frame(self)
        frame_input.pack(padx=10, pady=10, fill="x")

        labels = ["Full Name", "Gender", "Status", "Date of Birth (YYYY-MM-DD)",
                  "Academic Year", "Address", "Ethnicity", "Religion", "Nationality"]
        self.entries = {}

        for i, label in enumerate(labels):
            lbl = tk.Label(frame_input, text=label)
            lbl.grid(row=i, column=0, sticky="e", padx=5, pady=5)
            entry = tk.Entry(frame_input, width=50)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.entries[label] = entry

        # Frame cho các nút CRUD
        frame_buttons = tk.Frame(self)
        frame_buttons.pack(padx=10, pady=10)

        btn_add = tk.Button(frame_buttons, text="Add Student", command=self.add_student)
        btn_add.grid(row=0, column=0, padx=5)
        btn_update = tk.Button(frame_buttons, text="Update Student", command=self.update_student)
        btn_update.grid(row=0, column=1, padx=5)
        btn_delete = tk.Button(frame_buttons, text="Delete Student", command=self.delete_student)
        btn_delete.grid(row=0, column=2, padx=5)
        btn_clear = tk.Button(frame_buttons, text="Clear Fields", command=self.clear_fields)
        btn_clear.grid(row=0, column=3, padx=5)
        btn_refresh = tk.Button(frame_buttons, text="Refresh List", command=self.refresh_student_list)
        btn_refresh.grid(row=0, column=4, padx=5)


        # Treeview để hiển thị danh sách student
        columns = ("ID", "FullName", "Gender", "Status", "DOB", "AcademicYear", "Address", "Ethnicity", "Religion", "Nationality")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        self.tree.pack(padx=10, pady=10, fill="both", expand=True)

        # Ràng buộc sự kiện chọn dòng
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)


    def add_student(self):
        student = Student(
            id=None,
            fullname=self.entries["Full Name"].get(),
            gender=self.entries["Gender"].get(),
            status=self.entries["Status"].get(),
            dateOfBirth=self.entries["Date of Birth (YYYY-MM-DD)"].get(),
            academicYear=self.entries["Academic Year"].get(),
            address=self.entries["Address"].get(),
            ethnicity=self.entries["Ethnicity"].get(),
            religion=self.entries["Religion"].get(),
            nationality=self.entries["Nationality"].get()
        )
        try:
            Student.save(student)
            messagebox.showinfo("Success", "Student added successfully!")
            self.refresh_student_list()
            self.clear_fields()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_student(self):
        if not self.selected_student_id:
            messagebox.showwarning("Warning", "Please select a student to update!")
            return
        student = Student(
            id=self.selected_student_id,
            fullname=self.entries["Full Name"].get(),
            gender=self.entries["Gender"].get(),
            status=self.entries["Status"].get(),
            dateOfBirth=self.entries["Date of Birth (YYYY-MM-DD)"].get(),
            academicYear=self.entries["Academic Year"].get(),
            address=self.entries["Address"].get(),
            ethnicity=self.entries["Ethnicity"].get(),
            religion=self.entries["Religion"].get(),
            nationality=self.entries["Nationality"].get()
        )
        try:
            Student.update(student)
            messagebox.showinfo("Success", "Student updated successfully!")
            self.refresh_student_list()
            self.clear_fields()
            self.selected_student_id = None
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_student(self):
        if not self.selected_student_id:
            messagebox.showwarning("Warning", "Please select a student to delete!")
            return
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this student?"):
            try:
                Student.delete(self.selected_student_id)
                messagebox.showinfo("Success", "Student deleted successfully!")
                self.refresh_student_list()
                self.clear_fields()
                self.selected_student_id = None
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def refresh_student_list(self):
        # Xóa hết nội dung hiện tại
        for item in self.tree.get_children():
            self.tree.delete(item)
        try:
            print("Student.py")
            students = Student.get_all()
            for stu in students:
                self.tree.insert("", "end", values=(
                    stu.id,
                    stu.fullname,
                    stu.gender,
                    stu.status,
                    stu.dateOfBirth,
                    stu.academicYear,
                    stu.address,
                    stu.ethnicity,
                    stu.religion,
                    stu.nationality
                ))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear_fields(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.selected_student_id = None

    def on_tree_select(self, event):
        selected = self.tree.focus()
        if selected:
            values = self.tree.item(selected, 'values')
            self.selected_student_id = values[0]
            self.entries["Full Name"].delete(0, tk.END)
            self.entries["Full Name"].insert(0, values[1])
            self.entries["Gender"].delete(0, tk.END)
            self.entries["Gender"].insert(0, values[2])
            self.entries["Status"].delete(0, tk.END)
            self.entries["Status"].insert(0, values[3])
            self.entries["Date of Birth (YYYY-MM-DD)"].delete(0, tk.END)
            self.entries["Date of Birth (YYYY-MM-DD)"].insert(0, values[4])
            self.entries["Academic Year"].delete(0, tk.END)
            self.entries["Academic Year"].insert(0, values[5])
            self.entries["Address"].delete(0, tk.END)
            self.entries["Address"].insert(0, values[6])
            self.entries["Ethnicity"].delete(0, tk.END)
            self.entries["Ethnicity"].insert(0, values[7])
            self.entries["Religion"].delete(0, tk.END)
            self.entries["Religion"].insert(0, values[8])
            self.entries["Nationality"].delete(0, tk.END)
            self.entries["Nationality"].insert(0, values[9])

if __name__ == "__main__":
    app = StudentApp()
    app.mainloop()
