import os
import sys
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime

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
            # Lấy dữ liệu từ DAO
            attendances = AttendancesDAO.get_all()
            
            # Xóa dữ liệu cũ trong bảng
            for item in self.table.get_children():
                self.table.delete(item)
                
            # Thêm dữ liệu mới vào bảng
            for i, attendance in enumerate(attendances, 1):
                # Format ngày sinh
                dob = attendance.student.date_of_birth.strftime('%d/%m/%Y') if attendance.student.date_of_birth else ''
                
                # Format thời gian điểm danh
                checkin_time = attendance.checkin_time.strftime('%H:%M:%S %d/%m/%Y') if attendance.checkin_time else ''
                
                # Format giới tính
                gender = 'Nam' if attendance.student.gender == 1 else 'Nữ' if attendance.student.gender == 0 else ''
                
                # Format trạng thái
                status = 'Có mặt' if attendance.status == 1 else 'Vắng mặt' if attendance.status == 0 else 'Điểm danh muộn'
                
                self.table.insert('', 'end', values=(
                    i,
                    attendance.student.student_id,
                    attendance.student.full_name,
                    dob,
                    gender,
                    checkin_time,
                    status
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
        
        # Nút điểm danh
        self.attendance_button = tk.Button(
            self.main_frame,
            text="Điểm danh", 
            font=("Times New Roman", 25, "bold"), 
            bg="white", 
            fg="black",
            command=self.diem_danh
        )
        self.attendance_button.pack(padx=100, pady=50)
        
        # Bảng dữ liệu
        self.create_table()
        
    def create_table(self):
        # Tạo bảng
        self.table = ttk.Treeview(
            self.main_frame, 
            columns=("STT", "MSSV", "Họ và tên", "Ngày sinh", "Giới tính", "Thời gian", "Trạng thái"), 
            show="headings"
        )
        
        # Thiết lập các cột
        self.table.heading("STT", text="STT")
        self.table.heading("MSSV", text="MSSV")
        self.table.heading("Họ và tên", text="Họ và tên")
        self.table.heading("Ngày sinh", text="Ngày sinh")
        self.table.heading("Giới tính", text="Giới tính")
        self.table.heading("Thời gian", text="Thời gian")
        self.table.heading("Trạng thái", text="Trạng thái")
        
        # Thiết lập độ rộng cột
        self.table.column("STT", width=100, anchor="center")
        self.table.column("MSSV", width=100, anchor="center")
        self.table.column("Họ và tên", width=170, anchor="center")
        self.table.column("Ngày sinh", width=100, anchor="center")
        self.table.column("Giới tính", width=100, anchor="center")
        self.table.column("Thời gian", width=150, anchor="center")
        self.table.column("Trạng thái", width=150, anchor="center")
        
        # Hiển thị bảng
        self.table.pack(expand=True, fill="both")
        
    def diem_danh(self):
        # TODO: Implement attendance logic here
        pass
        
    def go_back(self):
        """Quay lại form login"""
        self.destroy()
        if self.on_back:
            self.on_back()

if __name__ == "__main__":
    app = DiemDanhSinhVien()
    app.mainloop()