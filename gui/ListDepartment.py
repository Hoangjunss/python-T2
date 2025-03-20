import tkinter as tk
from tkinter import ttk

window = tk.Tk()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window.title("Khoa")
window.geometry(f"{screen_width}x{screen_height}")

frame = tk.Frame(window, bg = "white")
frame.place(x = 0, y = 0, width = screen_width, height = screen_height)

nameUniversity = tk.Label(frame, text = "Trường Đại học Sài Gòn", font = ("Times New Roman", 13), fg = "black", bg = "white")
nameUniversity.place(x = 0, y = 0)

titleManageSchedule = tk.Label(frame, text = "Quản lí lịch học khoa", font = ("Times New Roman", 25), fg = "black", bg = "white")
titleManageSchedule.place(x = 650 , y = 25)

mainTitle = tk.Label(frame, text = "Khoa Công Nghệ Thông Tin", font = ("Times New Roman", 20,"italic"), fg = "red", bg = "white")
mainTitle.place(x = 100, y = 75)

titleDean = tk.Label(frame, text = "Trưởng Khoa: ", font = ("Times New Roman", 20), fg = "red", bg = "white")
titleDean.place(x = 550, y = 75)

nameDean = tk.Label(frame, text = "Nguyễn Văn A", font = ("Times New Roman", 20), fg = "black", bg = "white")
nameDean.place(x = 720, y = 75)

list = ttk.Treeview(frame)
list.place(x = 100, y = 130)

styleList = ttk.Style()
styleList.configure("Treeview", rowheight = 60, font = ("Times New Roman", 16))
styleList.configure("Treeview.Heading", font = ("Times New Roman", 18, "bold"), foreground = "red", background = "red")

list["column"] = ("Học Kỳ", "Năm học - Niên khóa", "Chi tiết năm học")
list.column("#0", width = 100, anchor = "center")
list.column("Học Kỳ", width = 200, anchor = "center")
list.column("Năm học - Niên khóa", width = 300, anchor = "center")
list.column("Chi tiết năm học", width = 400, anchor = "center")

list.heading("#0", text = "ID", anchor = "center")
list.heading("Học Kỳ", text = "Học Kỳ", anchor = "center")
list.heading("Năm học - Niên khóa", text = "Năm học - Niên khóa", anchor = "center")
list.heading("Chi tiết năm học", text = "Chi tiết năm học", anchor = "center")
list.tag_configure("header", font = ("Times New Roman", 20, "bold"), background = "red", foreground = "white")

list.insert("", "end",text = "001", values = ("Học Kỳ I", "2023-2024", "Chi tiết"))
list.insert("", "end",text = "002", values = ("Học Kỳ II", "2023-2024", "Chi tiết"))
list.insert("", "end",text = "003", values = ("Học Kỳ I", "2024-2025", "Chi tiết"))

buttonAddSchedule = tk.Button(frame, text = "Thêm lịch học",font = ("Times New Roman", 17), bd = 0, bg = "red", fg = "white", width = 15)
buttonAddSchedule.place(x = 1200, y = 130)

buttonEraseSchedule = tk.Button(frame, text = "Xóa lịch học", font = ("Times New Roman", 17), bd = 0, bg = "red", fg = "white", width = 15)
buttonEraseSchedule.place(x = 1200, y = 200)

frame.mainloop()