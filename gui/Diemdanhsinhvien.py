import os
import sys
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime
import python_train_face.webcam as webcam


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from dao import AttendancesDAO

class DiemDanhSinhVien(tk.Tk):
    def __init__(self, on_back=None):
        super().__init__()
        self.title("Điểm danh sinh viên")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")
        
        # Lưu callback function
        self.on_back = on_back
        
        # Khởi tạo giao diện
        self.create_widgets()
        
        # Load dữ liệu
        self.load_attendance_data()
        
    def load_attendance_data(self):
        try:
            # Lấy dữ liệu từ DAO sử dụng StudentAttendenceDTO
            attendances = AttendancesDAO.get_attendance_list()
            
            # Xóa dữ liệu cũ trong bảng
            for item in self.table.get_children():
                self.table.delete(item)
                
            # Thêm dữ liệu mới vào bảng
            for attendance in attendances:
                # Format thời gian điểm danh
                checkin_time = attendance.checkin_time.strftime('%H:%M:%S %d/%m/%Y') if attendance.checkin_time else ''
                
                self.table.insert('', 'end', values=(
                    attendance.id,
                    attendance.fullname,
                    checkin_time,
                    attendance.class_name
                ))
                
        except Exception as e:
            print(f"Lỗi khi tải dữ liệu: {e}")
        
    def create_widgets(self):
        # Frame chính
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill="both", expand=True)
        
        # Nút quay lại
        self.back_button = tk.Button(
            self.main_frame,
            text="Quay lại",
            font=("Times New Roman", 15),
            bg="#34495e",
            fg="white",
            command=self.go_back
        )
        self.back_button.place(x=30, y=30)
        
        # Tiêu đề
        self.title_label = tk.Label(
            self.main_frame, 
            text="Điểm danh sinh viên", 
            font=("Times New Roman", 25, "bold"), 
            fg="red"
        )
        self.title_label.place(x=50, y=50)
        
        # Frame chứa các nút
        self.button_frame = tk.Frame(self.main_frame)
        self.button_frame.pack(pady=20)
        
        # Nút điểm danh
        self.attendance_button = tk.Button(
            self.button_frame,
            text="Điểm danh", 
            font=("Times New Roman", 25, "bold"), 
            bg="white", 
            fg="black",
            command=self.diem_danh
        )
        self.attendance_button.pack(side=tk.LEFT, padx=10)
        
        # Nút refresh
        self.refresh_button = tk.Button(
            self.button_frame,
            text="Làm mới", 
            font=("Times New Roman", 25, "bold"), 
            bg="#2ecc71", 
            fg="white",
            command=self.refresh_data
        )
        self.refresh_button.pack(side=tk.LEFT, padx=10)
        
        # Bảng dữ liệu
        self.create_table()
        
    def create_table(self):
        # Tạo bảng
        self.table = ttk.Treeview(
            self.main_frame, 
            columns=("ID", "Họ và tên", "Thời gian điểm danh", "Lớp"), 
            show="headings"
        )
        
        # Thiết lập các cột
        self.table.heading("ID", text="ID")
        self.table.heading("Họ và tên", text="Họ và tên")
        self.table.heading("Thời gian điểm danh", text="Thời gian điểm danh")
        self.table.heading("Lớp", text="Lớp")
        
        # Thiết lập độ rộng cột
        self.table.column("ID", width=100, anchor="center")
        self.table.column("Họ và tên", width=200, anchor="center")
        self.table.column("Thời gian điểm danh", width=200, anchor="center")
        self.table.column("Lớp", width=150, anchor="center")
        
        # Hiển thị bảng
        self.table.pack(expand=True, fill="both")
        
    def diem_danh(self):
        """Mở camera để điểm danh"""
        webcam.detect_face_from_webcam_mtcnn()
        # Sau khi đóng camera, cập nhật dữ liệu điểm danh
        self.load_attendance_data()
        
    def refresh_data(self):
        """Làm mới dữ liệu điểm danh"""
        self.load_attendance_data()
        
    def go_back(self):
        """Quay lại form login"""
        self.destroy()
        if self.on_back:
            self.on_back()
        else:
            # Nếu không có callback, tạo form login mới
            root = tk.Tk()
            from gui.FormLogin import FormLoginApp
            app = FormLoginApp(root)    
            root.mainloop()

if __name__ == "__main__":
    app = DiemDanhSinhVien()
    app.mainloop()