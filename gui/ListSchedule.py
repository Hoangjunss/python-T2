import tkinter as tk
from tkinter import ttk
import random

window = tk.Tk()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window.geometry(f"{screen_width}x{screen_height}")
window.title("Lịch học khoa")

frame = tk.Frame(window, bg = "white")
frame.place(x = 0, y = 0, width =screen_width, height = screen_height)

nameUniversity = tk.Label(frame, text = "Trường Đại học Sài Gòn", font = ("Times New Roman", 13), fg = "black", bg = "white")
nameUniversity.place(x = 0, y = 0)

titleManageSchedule = tk.Label(frame, text = "Quản lí lịch học khoa: ", font = ("Times New Roman", 23), bg = "white", fg = "red")
titleManageSchedule.place(x = 450, y = 20)

nameDepartment = tk.Label(frame, text = "Khoa Công Nghệ Thông Tin", font = ("Times New Roman", 23), bg = "white", fg = "red")
nameDepartment.place(x = 740, y = 20)

titleScheduleDepartment = tk.Label(frame, text = "Khoa Công Nghệ Thông Tin", font= ("Times New Roman", 20) , bg = "white", fg = "red")
titleScheduleDepartment.place(x =100, y = 65)

listSchedule = ttk.Treeview(frame)
listSchedule.place(x = 100, y = 110)

listSchedule["column"] = ("Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5", "Thứ 6", "Thứ 7", "Chủ nhật")
listSchedule.column("#0", width = 150, anchor = "center")
listSchedule.column("Thứ 2", width = 180 , anchor = "center")
listSchedule.column("Thứ 3", width = 180, anchor = "center")
listSchedule.column("Thứ 4", width = 180, anchor = "center")
listSchedule.column("Thứ 5", width = 180, anchor = "center")
listSchedule.column("Thứ 6", width = 180, anchor = "center")
listSchedule.column("Thứ 7", width = 180, anchor = "center")
listSchedule.column("Chủ nhật", width = 130, anchor = "center")

columns = ["Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5", "Thứ 6", "Thứ 7", "Chủ nhật"]
listSchedule.heading("#0", text = "Giờ/Thứ", anchor = "center")
listSchedule.heading("Thứ 2", text = "Thứ 2", anchor = "center")
listSchedule.heading("Thứ 3", text = "Thứ 3", anchor = "center")
listSchedule.heading("Thứ 4", text = "Thứ 4", anchor = "center")
listSchedule.heading("Thứ 5", text = "Thứ 5", anchor = "center")
listSchedule.heading("Thứ 6", text = "Thứ 6", anchor = "center")
listSchedule.heading("Thứ 7", text = "Thứ 7", anchor = "center")
listSchedule.heading("Chủ nhật", text = "Chủ nhật", anchor = "center")

styleListSchedule = ttk.Style()
styleListSchedule.configure("Treeview", rowheight = 60, font = ("Times New Roman", 16))
styleListSchedule.configure("Treeview.Heading", font = ("Times New Roman", 18, "bold"), foreground = "red", background = "blue")

listTime = ["7.50","8.40","9.50","10.40","11.30","13.50","14.40","15.50","16.40","17.30"]
subjects = [
    "Lập trình Python", "Cấu trúc dữ liệu & Giải thuật", "Hệ điều hành", "Lập trình Web",
    "Cơ sở dữ liệu", "Mạng máy tính", "Trí tuệ nhân tạo", "Học máy", "Phát triển ứng dụng di động",
    "Lập trình Java", "Khoa học dữ liệu", "Bảo mật mạng", "Phát triển phần mềm", "Điện toán đám mây",
    "Kỹ thuật lập trình", "Hệ thống nhúng", "Blockchain", "Công nghệ phần mềm", "Xử lý ảnh",
    "Phân tích dữ liệu"
]

# Thêm dữ liệu vào Treeview
for time in listTime:
    row_values = [random.choice(subjects) for _ in range(len(columns) - 1)] + ["Nghỉ"]
    listSchedule.insert("", "end", text=time, values=row_values)

window.mainloop()