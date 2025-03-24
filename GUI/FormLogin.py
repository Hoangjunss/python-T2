import tkinter as tk 
from tkinter import ttk
from PIL import Image, ImageTk
# from PIL import ImageResampling 
window= tk.Tk()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window.title("Welcome")
window.geometry(f"{screen_width}x{screen_height}")

frame = tk.Frame(window, bg = "white")
frame.place(x = 0, y = 0, width = screen_width, height = screen_height)

frameTeacher = tk.Frame(window, bg = "white")
frameTeacher.place(x = 0, y = 0, width = screen_width, height = screen_height)

frameStudent = tk.Frame(window, bg = "white")
frameStudent.place(x = 0, y = 0, width = screen_width, height = screen_height)

imageFormWelcome = Image.open("D:\\Python\\python-T2\\Dataset\\image_form\\imgForm.jpg")
imageFormWelcome = imageFormWelcome.resize((screen_width, screen_height), Image.Resampling.LANCZOS)

imageBackground = ImageTk.PhotoImage(imageFormWelcome)

imageForm = tk.Label(frame, image = imageBackground)
imageForm.place(x = 0, y = 0, relwidth=1,relheight=1)
imageForm.lower()

titleWelcome = tk.Label(frame, text = "Trường Đại học Sài Gòn", font = ("Times New Roman", 40), borderwidth=0, fg = "red")
titleWelcome.place(x = 480, y = 200)

buttonTeacher = tk.Button(frame, text = "Bạn là Giáo Viên", font = ("Times New Roman", 30),fg = "red", borderwidth=0, bd = "0",command=lambda: frameTeacher.tkraise())
buttonTeacher.place(x = 330, y = 350)

buttonStudent = tk.Button(frame, font = ("Times New Roman", 30), text = "Bạn là Sinh Viên", fg = "red", borderwidth=0, bd = "0",command=lambda: frameStudent.tkraise())
buttonStudent.place(x = 900, y = 350)

imageLoginTeacher = Image.open("D:\\Python\\python-T2\\Dataset\\image_form\\imgForm.jpg")
imageLoginTeacher = imageLoginTeacher.resize((screen_width, screen_height), Image.Resampling.LANCZOS)

imageBackgroundTeacher = ImageTk.PhotoImage(imageLoginTeacher)

imageFormLoginTeacher = tk.Label(frameTeacher, image = imageBackgroundTeacher)
imageFormLoginTeacher.place(x = 0, y = 0, relwidth=1,relheight=1)
imageFormLoginTeacher.lower()

titleWelcomeTeacher = tk.Label(frameTeacher, text = "Chào mừng giáo viên Trường Đại học Sài gòn", font = ("Times New Roman", 40), fg = "red")
titleWelcomeTeacher.place(x = 270, y = 150)

titleLoginTeacher = tk.Label(frameTeacher, text = "Đăng nhập", font = ("Times New Roman", 30), fg = "black")
titleLoginTeacher.place(x = 650, y = 250)

usernameTeacher = tk.Label(frameTeacher, text = "Tên đăng nhập: ",font = ("Times New Roman", 27), fg = "black")
passwordTeacher = tk.Label(frameTeacher, text = "Mật khẩu: ", font = ("Times New Roman", 27), fg = "black")
textUsernameTeacher = tk.Entry(frameTeacher, font = ("Times New Roman", 25), fg = "black", width = 30, borderwidth = 1)
textPasswordTeacher = tk.Entry(frameTeacher, font = ("Times New Roman", 25), fg = "black", width = 30, borderwidth = 1, show = "*")

usernameTeacher.place(x = 350, y =350)
passwordTeacher.place(x = 420, y = 450)
textUsernameTeacher.place(x = 600, y = 350)
textPasswordTeacher.place(x = 600, y = 450)

buttonLoginTeacher = tk.Button(frameTeacher, text = "Truy cập", font = ("Times New Roman",25), fg = "red", bd = "0")
buttonLoginTeacher.place(x = 670, y = 530)

buttonBackHome = tk.Button(frameTeacher, text = "Quay lại trang chủ", font = ("Times New Roman", 20), fg = "black",bd = "0", command=lambda:frame.tkraise())
buttonBackHome.place(x = 30, y = 30)

imageLoginStudent = Image.open("D:\\Python\\python-T2\\Dataset\\image_form\\imgForm.jpg")
imageLoginStudent = imageLoginStudent.resize((screen_width, screen_height), Image.Resampling.LANCZOS)

imageBackgroundStudent = ImageTk.PhotoImage(imageLoginStudent)

imageFormLoginStudent = tk.Label(frameStudent, image = imageBackgroundStudent)
imageFormLoginStudent.place(x = 0, y = 0, relwidth=1,relheight=1)
imageFormLoginStudent.lower()

titleWelcomeStudent = tk.Label(frameStudent, text = "Chào mừng sinh viên Trường Đại học Sài gòn", font = ("Times New Roman", 40), fg = "red")
titleWelcomeStudent.place(x = 270, y = 150)

titleLoginStudent = tk.Label(frameStudent, text = "Đăng nhập", font = ("Times New Roman", 30), fg = "black")
titleLoginStudent.place(x = 650, y = 250)

usernameStudent = tk.Label(frameStudent, text = "Tên đăng nhập: ",font = ("Times New Roman", 27), fg = "black")
passwordStudent = tk.Label(frameStudent, text = "Mật khẩu: ", font = ("Times New Roman", 27), fg = "black")
textUsernameStudent = tk.Entry(frameStudent, font = ("Times New Roman", 25), fg = "black", width = 30, borderwidth = 1)
textPasswordStudent = tk.Entry(frameStudent, font = ("Times New Roman", 25), fg = "black", width = 30, borderwidth = 1, show = "*")

usernameStudent.place(x = 350, y =350)
passwordStudent.place(x = 420, y = 450)
textUsernameStudent.place(x = 600, y = 350)
textPasswordStudent.place(x = 600, y = 450)

buttonLoginStudent = tk.Button(frameStudent, text = "Truy cập", font = ("Times New Roman",25), fg = "red", bd = "0")
buttonLoginStudent.place(x = 670, y = 530)

buttonBackHome = tk.Button(frameStudent, text = "Quay lại trang chủ", font = ("Times New Roman", 20), fg = "black",bd = "0", command=lambda:frame.tkraise())
buttonBackHome.place(x = 30, y = 30)

frame.tkraise()
window.mainloop()

