import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox
from gui.MainPage import MainPage
from gui.Diemdanhsinhvien import DiemDanhSinhVien
# from dao import TeacherDAO
# from database import ConnectDB

class FormLoginApp:

    @staticmethod
    def connect_database():
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "13524679",
            database = "student_information_management"
        )
        return conn

    def update_password(self):
        try:
            conn = self.connect_database()

            cursor = conn.cursor()
            update_query = "UPDATE TEACHER SET password = phone WHERE password IS NULL"
            cursor.execute(update_query)
            conn.commit()

            print(f"Đã cập nhật {cursor.rowcount} giáo viên.")
        except mysql.connector.Error as e:
            print(f" Lỗi khi cập nhật: {e}")
        finally:
                cursor.close()
                conn.close()

    def check_login(self):
        username = self.userNameTeacher.get()
        password = self.passwordTeacher.get()

        try:
            conn = self.connect_database()
            cursor = conn.cursor(dictionary=True)

            cursor.execute("SELECT id FROM TEACHER WHERE username=%s AND password=%s", (username, password))
            result = cursor.fetchone()

            if result:
                teacherId = result['id']
                messagebox.showinfo("Thông báo", "Đăng nhập thành công")
                print(f"Đăng nhập thành công.")
                # Đóng form login
                self.root.destroy()
                # Mở MainPage
                main_page = MainPage(teacherId)
                main_page.mainloop()
            else:
                messagebox.showerror("Lỗi", "Đăng nhập không thành công")
                print(f"Đăng nhập không thành công.")

        except mysql.connector.Error as e:
            messagebox.showerror("Lỗi", f"Lỗi kết nối database: {str(e)}")
            print(f"Lỗi kết nối database: {e}")
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals():
                conn.close()

    def __init__(self, root):
        self.root = root
        self.root.title("Welcome")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.geometry(f"{screen_width}x{screen_height}")

        self.frames = {}
        self.create_frames(screen_width, screen_height)
        self.show_frame("welcome")

    def create_frames(self, screen_width, screen_height):
        # Frame: Trang chủ
        self.frames["welcome"] = tk.Frame(self.root, bg="white")
        self.frames["welcome"].place(x=0, y=0, width=screen_width, height=screen_height)

        # Frame: Giáo viên
        self.frames["teacher"] = tk.Frame(self.root, bg="white")
        self.frames["teacher"].place(x=0, y=0, width=screen_width, height=screen_height)

        # Frame: Sinh viên
        self.frames["student"] = tk.Frame(self.root, bg="white")
        self.frames["student"].place(x=0, y=0, width=screen_width, height=screen_height)

        self.build_welcome_frame(screen_width, screen_height)
        self.build_teacher_frame(screen_width, screen_height)
        self.build_student_frame(screen_width, screen_height)

    def open_DDSV(self):
        # Thay vì tạo instance mới và gọi mainloop ngay lập tức
        # Chỉ chuyển sang form DiemDanhSinhVien
        self.root.destroy()
        DDSV = DiemDanhSinhVien(on_back=self.show_login)
        DDSV.mainloop()

    def show_login(self):
        # Hàm callback để quay lại form login
        root = tk.Tk()
        app = FormLoginApp(root)    
        root.mainloop()

    def show_frame(self, frame_name):
        self.frames[frame_name].tkraise()
        


    def build_welcome_frame(self, w, h):
        frame = self.frames["welcome"]

        bg = Image.open(r"Dataset/image_form/imgForm.jpg")
        bg = bg.resize((w, h), Image.Resampling.LANCZOS)
        self.bg_welcome_img = ImageTk.PhotoImage(bg)
        tk.Label(frame, image=self.bg_welcome_img).place(x=0, y=0, relwidth=1, relheight=1)

        tk.Label(frame, text="Trường Đại học Sài Gòn", font=("Times New Roman", 40), fg="red").place(x=480, y=200)
        tk.Button(frame, text="Bạn là Giáo Viên", font=("Times New Roman", 30), fg="red", bd=0,
                  command=lambda: self.show_frame("teacher")).place(x=330, y=350)
        tk.Button(frame, text="Bạn là Sinh Viên", font=("Times New Roman", 30), fg="red", bd=0,
                  command=lambda: self.open_DDSV()).place(x=900, y=350)

    def build_teacher_frame(self, w, h):
        frame = self.frames["teacher"]
        #self.update_password()

        bg = Image.open(r"Dataset/image_form/imgForm.jpg")
        bg = bg.resize((w, h), Image.Resampling.LANCZOS)
        self.bg_teacher_img = ImageTk.PhotoImage(bg)
        tk.Label(frame, image=self.bg_teacher_img).place(x=0, y=0, relwidth=1, relheight=1)

        tk.Label(frame, text="Chào mừng giáo viên Trường Đại học Sài Gòn", font=("Times New Roman", 40), fg="red").place(x=270, y=150)
        tk.Label(frame, text="Đăng nhập", font=("Times New Roman", 30)).place(x=650, y=250)
        tk.Label(frame, text="Tên đăng nhập: ", font=("Times New Roman", 27)).place(x=350, y=350)
        tk.Label(frame, text="Mật khẩu: ", font=("Times New Roman", 27)).place(x=420, y=450)

        self.userNameTeacher = tk.Entry(frame, font=("Times New Roman", 25), width=30)
        self.userNameTeacher.place(x=600, y=350)
        self.passwordTeacher = tk.Entry(frame, font=("Times New Roman", 25), width=30, show="*")
        self.passwordTeacher.place(x=600, y=450)

        tk.Button(frame, text="Truy cập", font=("Times New Roman", 25), fg="red", bd=0, command=lambda:self.check_login()).place(x=670, y=530)
        tk.Button(frame, text="Quay lại trang chủ", font=("Times New Roman", 20), bd=0,
                  command=lambda: self.show_frame("welcome")).place(x=30, y=30)

    def build_student_frame(self, w, h):
        frame = self.frames["student"]

        bg = Image.open(r"Dataset/image_form/imgForm.jpg")
        bg = bg.resize((w, h), Image.Resampling.LANCZOS)
        self.bg_student_img = ImageTk.PhotoImage(bg)
        tk.Label(frame, image=self.bg_student_img).place(x=0, y=0, relwidth=1, relheight=1)

        tk.Label(frame, text="Chào mừng sinh viên Trường Đại học Sài Gòn", font=("Times New Roman", 40), fg="red").place(x=270, y=150)
        tk.Label(frame, text="Đăng nhập", font=("Times New Roman", 30)).place(x=650, y=250)
        tk.Label(frame, text="Tên đăng nhập: ", font=("Times New Roman", 27)).place(x=350, y=350)
        tk.Label(frame, text="Mật khẩu: ", font=("Times New Roman", 27)).place(x=420, y=450)

        tk.Entry(frame, font=("Times New Roman", 25), width=30).place(x=600, y=350)
        tk.Entry(frame, font=("Times New Roman", 25), width=30, show="*").place(x=600, y=450)

        tk.Button(frame, text="Truy cập", font=("Times New Roman", 25), fg="red", bd=0).place(x=670, y=530)
        tk.Button(frame, text="Quay lại trang chủ", font=("Times New Roman", 20), bd=0,
                  command=lambda: self.show_frame("welcome")).place(x=30, y=30)


if __name__ == "__main__":
    root = tk.Tk()
    app = FormLoginApp(root)    
    root.mainloop()
