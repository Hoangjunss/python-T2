import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import os

# Load model nhận diện khuôn mặt (Haar Cascade)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

class AddStudentGUI(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Thêm sinh viên")
        self.geometry("1200x600")
        self.configure(bg="white")
        self.create_widget()  # Gọi phương thức để hiển thị các widget


    def open_camera(self):
        cap = cv2.VideoCapture(0)  # Mở camera

        if not cap.isOpened():
            print("Không thể mở camera!")
            return

        while True:
            ret, frame = cap.read()  # Đọc khung hình từ camera
            if not ret:
                print("Không thể nhận khung hình!")
                break

            # Chuyển ảnh sang xám để tăng hiệu suất nhận diện
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Nhận diện khuôn mặt
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(50, 50))

            # Vẽ hình chữ nhật xung quanh khuôn mặt
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)  # (x, y) là góc trái trên, (x+w, y+h) là góc phải dưới

            # Hiển thị hình ảnh có nhận diện
            cv2.imshow("Nhận diện khuôn mặt", frame)

            # Nhấn phím 'q' để thoát
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()  # Giải phóng camera
        cv2.destroyAllWindows()  # Đóng cửa sổ OpenCV

    # Create Bottom Line Entry
    def createBottomBorder(self,frame, localY):
        lineBottom = tk.Canvas(frame, width = 30, height =20)
        lineBottom.place(x = 190, y = localY)
        lineBottom.create_line(0, 300, 300, 25, width=2, fill="black")
        entry = tk.Entry(frame, font=("Arial", 14), bd=0, highlightthickness=0, relief="flat")
        entry.place(x=0, y=0)  # Đặt Entry trên canvas, chính giữa

        return entry

    def on_mouse_enter(self, event):
        event.widget.config(bg = "red")
        event.widget.config(fg = "white")
    def on_mouse_leave(self, event):
        event.widget.config(bg ="white")
        event.widget.config(fg = "red")


    def open_image(self, label):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")]  # Lọc chỉ chọn ảnh
        )
        if file_path:  # Nếu chọn ảnh
            img = Image.open(file_path)  # Mở ảnh
            imgSize = img.resize((200, 200),Image.LANCZOS)  # Thay đổi kích thước (tuỳ chỉnh)
            img_tk = ImageTk.PhotoImage(imgSize)  # Chuyển sang định dạng Tkinter

            label.config(image=img_tk)  # Gán ảnh vào label
            label.image = img_tk  # Giữ tham chiếu để không bị xoá bởi garbage collection

    def addBorderButton(self, button):
        button.update_idletasks()
        button_width = button.winfo_width()
        button_height = button.winfo_height()

        border = tk.Canvas(button.master, height = 1, width = button_width, bg = "blue", bd = 0, highlightthickness = 0)
        border.place(x = button.winfo_x(), y = button_height + button.winfo_y())

    def on_button_click(self, entry):
        entry.config(state = tk.NORMAL)

    def create_widget(self):
        frame = tk.Frame(self, bg="white")

        # Frame chứa các nút bấm
        frame.place(x=0,y=0,width =1200,height =600)

        titleAdd = tk.Label(frame, text = "Quản lí thêm sinh viên", font =("Times New Roman", 25))
        titleAdd.place(x = 340, y = 5)
        titleAdd.config(bg="white")

        labelID = tk.Label(frame, text ="Mã số sinh viên: ", font =("Times New Roman", 20))
        labelID.config(bg = "white")
        labelID.place(x =15, y = 60)

        labelName = tk.Label(frame, text="Tên sinh viên: ", font =("Times New Roman", 20))
        labelName.place(x = 15, y =100)
        labelName.config(bg= "white")

        labelBranch = tk.Label(frame, text = "Ngành học:", font =("Times New Roman", 20))
        labelBranch.config(bg ="white")
        labelBranch.place(x = 15, y =140)

        labelDepartment = tk.Label(frame, text ="Khoa: ", font = ("Times New Roman", 20))
        labelDepartment.config(bg ="white")
        labelDepartment.place(x =15, y =180)

        labelClass = tk.Label(frame, text = "Lớp: ", font =("Times New Roman", 20))
        labelClass.place(x = 15, y = 220)
        labelClass.config(bg = "white")

        labelBirth = tk.Label(frame, text ="Ngày sinh: ", font = ("Times New Roman", 20))
        labelBirth.place(x =15, y = 260)
        labelBirth.config(bg = "white")

        labelSex = tk.Label(frame, text = "Giới tính: ", font =("Times New Roman", 20))
        labelSex.place(x =15, y =300)
        labelSex.config(bg ="white")

        labelPhoneNumber = tk.Label(frame, text = "Số điện thoại: ", font =("Times New Roman", 20))
        labelPhoneNumber.place(x =15 , y = 340)
        labelPhoneNumber.config(bg ="white")

        labelIdentify = tk.Label(frame, text ="Căn cước công dân: ", font =("Times New Roman", 20))
        labelIdentify.place(x = 15, y = 380)
        labelIdentify.config(bg = "white")

        labelAddress = tk.Label(frame, text ="Địa chỉ: ", font = ("Times New Roman", 20))
        labelAddress.place(x = 15, y =420)
        labelAddress.config(bg ="white")

        textID = tk.Entry(frame, font =("Times New Roman", 20), width = 30,borderwidth =1)
        textID.place(x = 250, y = 60)
        textID.insert(tk.END, "3123410083")
        textID.config(state = tk.DISABLED)

        buttonFaceId = tk.Button(frame, text = "Nhận diện khuôn mặt sinh viên", font = ("Times New Roman", 15), height = 2, bd = 0, bg = "white", fg= "red", command=self.open_camera)
        buttonChangeID = tk.Button(frame, text = "Sửa", font = ("Times New Roman", 15),height = 1, bd = 0, bg = "white", fg = "blue", highlightthickness = 1, highlightbackground = "blue")
        buttonChangeID.place(x = 685, y = 62)


        textName = tk.Entry(frame, font =("Times New Roman", 20), width =30, bg ="white",borderwidth =1)
        textName.place(x = 250, y =100)

        buttonChangeName = tk.Button(frame, text = "Sửa", font = ("Times New Roman", 15), height = 1, bd = 0, bg = "white", fg = "blue"
                                    , highlightthickness = 1, highlightbackground = "blue")
        buttonChangeName.place(x = 685, y = 102)

        textBranch = tk.Entry(frame, font=("Times New Roman", 20), width =30, bg ="white",borderwidth =1)
        textBranch.place(x = 250, y =140)

        buttonChangeBranch = tk.Button(frame, text = "Sửa", font = ("Times New Roman", 15), height = 1, bd = 0, bg = "white", fg = "blue"
                                    , highlightthickness = 1, highlightbackground = "blue")
        buttonChangeBranch.place(x = 685, y = 142)

        textDepartment = tk.Entry(frame, font =("Times New Roman", 20), width =30, bg ="white",borderwidth =1)
        textDepartment.place(x = 250, y =180)

        buttonChangeDepartment = tk.Button(frame, text = "Sửa", font = ("Times New Roman", 15), height = 1, bd = 0, bg = "white", fg = "blue"
                                        , highlightthickness = 1, highlightbackground = "blue")
        buttonChangeDepartment.place(x = 685, y = 182)

        textClass = tk.Entry(frame, font=("Times New Roman", 20), width =30, bg ="white",borderwidth =1)
        textClass.place(x = 250, y =220)

        buttonChangeClass = tk.Button(frame, text = "Sửa", font = ("Times New Roman", 15), height = 1, bd = 0, bg = "white", fg = "blue"
                                    , highlightthickness = 1, highlightbackground = "blue")
        buttonChangeClass.place(x = 685, y = 222)

        textBirth = tk.Entry(frame, font =("Times New Roman", 20), width =30, bg ="white",borderwidth =1)
        textBirth.place(x = 250, y =260)

        buttonChangeBirth = tk.Button(frame, text = "Sửa", font = ("Times New Roman", 15), height = 1, bd = 0, bg = "white", fg = "blue"
                                    , highlightthickness = 1, highlightbackground = "blue")
        buttonChangeBirth.place(x = 685, y = 262)

        textSex = tk.Entry(frame, font =("Times New Roman", 20), width =30, bg ="white",borderwidth =1)
        textSex.place(x = 250, y =300)

        buttonChangeSex = tk.Button(frame, text = "Sửa", font = ("Times New Roman", 15), height = 1, bd = 0, bg = "white", fg = "blue"
                                    , highlightthickness = 1, highlightbackground = "blue")
        buttonChangeSex.place(x = 685, y = 302)

        textPhoneNumber = tk.Entry(frame, font =("Times New Roman", 20), width =30, bg ="white",borderwidth =1)
        textPhoneNumber.place(x = 250, y =340)

        buttonChangePhone = tk.Button(frame, text = "Sửa", font = ("Times New Roman", 15), height = 1, bd = 0, bg = "white", fg = "blue"
                                    , highlightthickness = 1, highlightbackground = "blue")
        buttonChangePhone.place(x = 685, y = 342)

        textIdentify = tk.Entry(frame, font = ("Times New Roman", 20), width = 30, borderwidth =1)
        textIdentify.place(x =250, y = 380)

        buttonChangeIdentify = tk.Button(frame, text = "Sửa", font = ("Times New Roman", 15), height = 1, bd = 0, bg = "white", fg = "blue"
                                        , highlightthickness = 1, highlightbackground = "blue")
        buttonChangeIdentify.place(x = 685, y = 382)

        textAddress = tk.Text(frame, font = ("Times New Roman", 20),width = 30, height = 2, borderwidth =1)
        textAddress.place(x =250 , y = 420)

        buttonChangeAddress = tk.Button(frame, text = "Sửa", font = ("Times New Roman", 15), height = 1, bd = 0, bg = "white", fg = "blue"
                                        , highlightthickness = 1, highlightbackground = "blue")
        buttonChangeAddress.place(x = 685, y = 422)

        buttonImgStudent = tk.Button(frame, text ="Ảnh sinh viên", font = ("Times New Roman", 20), bg ="white", fg = "black", bd = 0)
        buttonImgStudent.place(x =870, y =290)
        imgStudent = tk.Label(frame, bg = "white")
        imgStudent.place(x = 860, y = 90)
        buttonImgStudent.config(command=lambda: self.open_image(imgStudent))


        buttonAdd = tk.Button(frame, text ="Thêm sinh viên", font =("Times New Roman", 15), width = 11, height =2, bd = 0,bg="white", fg="red")
        buttonAdd.place(x = 800, y = 500)
        buttonAdd.bind("<Enter>", self.on_mouse_enter)
        buttonAdd.bind("<Leave>", self.on_mouse_leave)

        buttonFaceId = tk.Button(frame, text = "Nhận diện khuôn mặt sinh viên", font = ("Times New Roman", 15), height = 2, bd = 0, bg = "white", fg= "red", command = self.open_camera)
        buttonFaceId.place(x = 830, y = 350)
        buttonFaceId.bind("<Enter>", self.on_mouse_enter)
        buttonFaceId.bind("<Leave>", self.on_mouse_leave)