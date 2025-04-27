import os
import sys
import tkinter as tk

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from gui.DiemDanh import DiemDanh
from gui.DepartmentGUI import DepartmentGUI
from gui.ListTeacher import Teacher_List
from gui.StudentGUI import Student_List


class MainPage(tk.Tk):
    def __init__(self, teacherId=None):
        super().__init__()
        self.teacherId = teacherId
        if self.teacherId:
            print(f"Teacher ID: {self.teacherId}")
        self.title("Student Management System")
        self.geometry("1050x700")

        # Khởi tạo thuộc tính current_page
        self.current_page = None

        #Menu
        self.sidebar = tk.Frame(self, width=150, bg="#2c3e50")
        self.sidebar.pack(side="left", fill="y")


        self.main_content = tk.Frame(self)
        self.main_content.pack(side="right", expand=True, fill="both")

        # Logor/tiêu đề sidebar
        self.logo_label = tk.Label(self.sidebar, text="MENU", bg="#2c3e50", fg="white", font=("Helvetica", 16, "bold"))
        self.logo_label.pack(pady=20)

        # Nút menu
        self.menu_buttons = [
            # ("🏫 Danh sách SV", self.show_student_list),
            ("➕ Sinh viên", self.StudentGUI),
            ("👩‍🏫 Giáo viên", self.TeacherGUI),
            ("Khoa", self.DepartmentGUI),
            ("🗓️ Điểm danh", self.DiemDanh),
            ("🚪 Thoát", self.quit_program)
        ]

        for text, command in self.menu_buttons:
            btn = tk.Button(self.sidebar, text=text, command=command, bg="#34495e", fg="white", width=15,
                            font=("Helvetica", 12), relief="flat", padx=10, pady=10)
            btn.pack(fill="x", padx=10, pady=5)
    
    def test(self):
        """Hàm kiểm tra."""
        print("Test function called")

    def clear_main_content(self):
        """Xóa nội dung hiện tại trong main_content."""
        if self.current_page:
            self.current_page.destroy()
            self.current_page = None

    def StudentGUI(self):
        """Hiển thị giao diện Sinh Viên."""
        self.clear_main_content()  # Xóa nội dung hiện tại
        self.current_page = Student_List(self.main_content)  # Tạo giao diện mới
        self.current_page.pack(fill="both", expand=True)
    
    def TeacherGUI(self):
        """Hiển thị giao diện Giáo Viên."""
        self.clear_main_content()
        self.current_page = Teacher_List(self.main_content)  # Tạo giao diện mới
        self.current_page.pack(fill="both", expand=True)

    def DepartmentGUI(self):
        """Hiển thị giao diện Khoa."""
        self.clear_main_content()
        self.current_page = DepartmentGUI(self.main_content)  # Tạo giao diện mới
        self.current_page.pack(fill="both", expand=True)

    def DiemDanh(self):
        """Hiển thị giao diện Điểm Danh."""
        self.clear_main_content()
        self.current_page = DiemDanh(self.main_content, self.teacherId)
        self.current_page.pack(fill="both", expand=True)

    def quit_program(self):
        """Thoát chương trình."""
        self.destroy()

    
if __name__ == "__main__":
    app = MainPage()
    app.mainloop()