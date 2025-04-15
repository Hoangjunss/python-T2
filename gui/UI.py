import sys
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import uuid
from PIL import Image, ImageTk
import cv2
import os
from tkinter import ttk
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from dao import ClassDAO, DepartmentDAO, StudentDAO, TeacherDAO
from models.Students import Student
from models.Teacher import Teacher
from models.Department import Department
from models.Class import Class

# Load model nhận diện khuôn mặt (Haar Cascade)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

class AddStudentGUI(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Thêm sinh viên")
        self.geometry("1200x600")
        self.configure(bg="white")
        self.create_widget()  # Gọi phương thức để hiển thị các widget


    def fetch_all_department(self)-> list[Department]:
        return DepartmentDAO.get_all()
    
    def fetch_all_class(self)-> list[Class]:
        return ClassDAO.get_all()

    def on_combobox_change(self, event):
        selected_index = self.department_combobox.current()
        if selected_index >= 0:
            department = self.department_data[selected_index]
            print(f"Bạn đã chọn: ID = {department.id}, Tên Khoa = {department.name}")

            self.department_name =department.name

    
    def generate_unique_id(self):
        return int(uuid.uuid4().int % (2**29))

    def saveStudent(self):
      
        self.fullname = self.textName.get()

        student = Student(
            id= self.generate_unique_id(),
            fullname=self.fullname,
            gender=self.gender_combobox.get(),
            # dateOfBirth=self.textBirth.get(),
            academicYear=self.textBranch.get(),
            address=self.textAddress.get("1.0", "end-1c"),
            ethnicity= self.textEthnicity.get(),
            religion= self.textReligion.get(),
            departmentId=self.department_map.get(self.selected_department.get()),
            class_id= self.class_map.get(self.selected_class.get())
        )
        print(student)
        StudentDAO.save(student)
        self.TrainImages()

    def TakeImages(self):        
            cam = cv2.VideoCapture(0)
            harcascadePath = "gui/haarcascade_frontalface_default.xml" # model phát hiện khuôn mặt haarcascade
            detector=cv2.CascadeClassifier(harcascadePath)
            self.id=self.generate_unique_id()
            sampleNum=0
            while(True):
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5)
                for (x,y,w,h) in faces:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)        

                    sampleNum=sampleNum+1

                    cv2.imwrite("gui\TrainingImage\ "+ self.textName.get() +"."+ str(self.id)+'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w]) #luu anh train vao folder

                    cv2.imshow('frame',img)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                elif sampleNum>100: #luu anh cho den khi dc 100 anh
                    break
            cam.release()
            cv2.destroyAllWindows() 
       
    def getImagesAndLabels(self, path):
        #get the path of all the files in the folder
        imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
        #print(imagePaths)
        
        #create empth face list
        faces=[]
        #create empty ID list
        Ids=[]
        #now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            #loading the image and converting it to gray scale
            pilImage=Image.open(imagePath).convert('L')
            #Now we are converting the PIL image into numpy array
            imageNp=np.array(pilImage,'uint8')
            #getting the Id from the image
            Id=int(os.path.split(imagePath)[-1].split(".")[1])
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(Id)        
        return faces,Ids


    def TrainImages(self):
        print("Training Images...")
        recognizer = cv2.face_LBPHFaceRecognizer.create()
        harcascadePath = "gui/haarcascade_frontalface_default.xml"
        detector =cv2.CascadeClassifier(harcascadePath)
        faces,Id = self.getImagesAndLabels("gui/TrainingImage")
        recognizer.train(faces, np.array(Id))
        recognizer.save("gui/TrainingImageLabel\Trainner.yml") # lưu model mới train vào thư mục
        res = "Train thành công"#+",".join(str(f) for f in Id)

    


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

        # labelID = tk.Label(frame, text ="Mã số sinh viên: ", font =("Times New Roman", 20))
        # labelID.config(bg = "white")
        # labelID.place(x =15, y = 60)

        labelName = tk.Label(frame, text="Tên sinh viên: ", font =("Times New Roman", 20))
        labelName.place(x = 15, y =100)
        labelName.config(bg= "white")

        labelBranch = tk.Label(frame, text = "Khóa học:", font =("Times New Roman", 20))
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

        labelPhoneNumber = tk.Label(frame, text = "Dân tộc: ", font =("Times New Roman", 20))
        labelPhoneNumber.place(x =15 , y = 340)
        labelPhoneNumber.config(bg ="white")

        labelIdentify = tk.Label(frame, text ="Tôn giáo: ", font =("Times New Roman", 20))
        labelIdentify.place(x = 15, y = 380)
        labelIdentify.config(bg = "white")

        labelAddress = tk.Label(frame, text ="Địa chỉ: ", font = ("Times New Roman", 20))
        labelAddress.place(x = 15, y =420)
        labelAddress.config(bg ="white")

        # labelNationaly = tk.Label(frame, text ="Quốc tịch: ", font = ("Times New Roman", 20))
        # labelNationaly.place(x = 15, y =490)
        # labelNationaly.config(bg ="white")

        # textID = tk.Entry(frame, font =("Times New Roman", 20), width = 30,borderwidth =1)
        # textID.place(x = 250, y = 60)
        # textID.insert(tk.END, "3123410083")
        # textID.config(state = tk.DISABLED)

        buttonFaceId = tk.Button(frame, text = "Nhận diện khuôn mặt sinh viên", font = ("Times New Roman", 15), height = 2, bd = 0, bg = "white", fg= "red", command=self.open_camera)
        # buttonChangeID = tk.Button(frame, text = "Sửa", font = ("Times New Roman", 15),height = 1, bd = 0, bg = "white", fg = "blue", highlightthickness = 1, highlightbackground = "blue")
        # buttonChangeID.place(x = 685, y = 62)


        self.textName = tk.Entry(frame, font =("Times New Roman", 20), width =30, bg ="white",borderwidth =1)
        self.textName.place(x = 250, y =100)

        buttonChangeName = tk.Button(frame, text = "Sửa", font = ("Times New Roman", 15), height = 1, bd = 0, bg = "white", fg = "blue"
                                    , highlightthickness = 1, highlightbackground = "blue")
        buttonChangeName.place(x = 685, y = 102)

        self.textBranch = tk.Entry(frame, font=("Times New Roman", 20), width =30, bg ="white",borderwidth =1)
        self.textBranch.place(x = 250, y =140)

        buttonChangeBranch = tk.Button(frame, text = "Sửa", font = ("Times New Roman", 15), height = 1, bd = 0, bg = "white", fg = "blue"
                                    , highlightthickness = 1, highlightbackground = "blue")
        buttonChangeBranch.place(x = 685, y = 142)

        """_department_
        """
        self.department_data = self.fetch_all_department()  # Lấy danh sách từ DB

        self.selected_department = tk.StringVar()
        self.department_combobox = ttk.Combobox(frame, textvariable=self.selected_department, state="readonly", width=30)

        # Lưu dictionary map giữa name và id
        self.department_map = {d.name: d.id for d in self.department_data}
        self.department_combobox['values'] = list(self.department_map.keys())

        if self.department_data:
            first_department = self.department_data[0].name
            self.selected_department.set(first_department)  # Chọn tên khoa đầu tiên

        self.department_combobox.place(x=250, y=180)
        self.department_combobox.bind("<<ComboboxSelected>>", self.on_combobox_change)


        # textDepartment = tk.Entry(frame, font =("Times New Roman", 20), width =30, bg ="white",borderwidth =1)
        # textDepartment.place(x = 250, y =180)

        # buttonChangeDepartment = tk.Button(frame, text = "Sửa", font = ("Times New Roman", 15), height = 1, bd = 0, bg = "white", fg = "blue"
        #                                 , highlightthickness = 1, highlightbackground = "blue")
        # buttonChangeDepartment.place(x = 685, y = 182)

        """_department_
        """
        # Lấy danh sách lớp từ database
        self.class_data = self.fetch_all_class()

        self.selected_class = tk.StringVar()
        self.class_combobox = ttk.Combobox(frame, textvariable=self.selected_class, state="readonly", width=30)

        # Lưu dictionary map giữa name và id
        self.class_map = {c.name: c.id for c in self.class_data}
        self.class_combobox['values'] = list(self.class_map.keys())

        # Chọn giá trị mặc định
        if self.class_data:
            first_class = self.class_data[0].name
            self.selected_class.set(first_class)

        self.class_combobox.place(x=250, y=220)
        self.class_combobox.bind("<<ComboboxSelected>>", self.on_combobox_change)



        """_class_
        """
        # textClass = tk.Entry(frame, font=("Times New Roman", 20), width =30, bg ="white",borderwidth =1)
        # textClass.place(x = 250, y =220)

        # buttonChangeClass = tk.Button(frame, text = "Sửa", font = ("Times New Roman", 15), height = 1, bd = 0, bg = "white", fg = "blue"
        #                             , highlightthickness = 1, highlightbackground = "blue")
        # buttonChangeClass.place(x = 685, y = 222)

        """_class_
        """

        self.textBirth = tk.Entry(frame, font =("Times New Roman", 20), width =30, bg ="white",borderwidth =1)
        self.textBirth.place(x = 250, y =260)

        buttonChangeBirth = tk.Button(frame, text = "Sửa", font = ("Times New Roman", 15), height = 1, bd = 0, bg = "white", fg = "blue"
                                    , highlightthickness = 1, highlightbackground = "blue")
        buttonChangeBirth.place(x = 685, y = 262)


        self.gender_combobox = ttk.Combobox(frame,text="Giới tính", state="readonly", width=30)
        self.gender_combobox['values'] = ["Nam", "Nữ"]
        self.gender_combobox.place(x = 250, y =300)
        self.gender_combobox.bind("<<ComboboxSelected>>", self.on_combobox_change)

        # textSex = tk.Entry(frame, font =("Times New Roman", 20), width =30, bg ="white",borderwidth =1)
        # textSex.place(x = 250, y =300)

        # buttonChangeSex = tk.Button(frame, text = "Sửa", font = ("Times New Roman", 15), height = 1, bd = 0, bg = "white", fg = "blue"
        #                             , highlightthickness = 1, highlightbackground = "blue")
        # buttonChangeSex.place(x = 685, y = 302)

        self.textEthnicity = tk.Entry(frame, font =("Times New Roman", 20), width =30, bg ="white",borderwidth =1)
        self.textEthnicity.place(x = 250, y =340)

        buttonChangePhone = tk.Button(frame, text = "Sửa", font = ("Times New Roman", 15), height = 1, bd = 0, bg = "white", fg = "blue"
                                    , highlightthickness = 1, highlightbackground = "blue")
        buttonChangePhone.place(x = 685, y = 342)

        self.textReligion = tk.Entry(frame, font = ("Times New Roman", 20), width = 30, borderwidth =1)
        self.textReligion.place(x =250, y = 380)

        buttonChangeIdentify = tk.Button(frame, text = "Sửa", font = ("Times New Roman", 15), height = 1, bd = 0, bg = "white", fg = "blue"
                                        , highlightthickness = 1, highlightbackground = "blue")
        buttonChangeIdentify.place(x = 685, y = 382)

        self.textAddress = tk.Text(frame, font = ("Times New Roman", 20),width = 30, height = 2, borderwidth =1)
        self.textAddress.place(x =250 , y = 420)

        buttonChangeAddress = tk.Button(frame, text = "Sửa", font = ("Times New Roman", 15), height = 1, bd = 0, bg = "white", fg = "blue"
                                        , highlightthickness = 1, highlightbackground = "blue")
        buttonChangeAddress.place(x = 685, y = 422)

        # self.textNationaly = tk.Entry(frame, font = ("Times New Roman", 20),width = 30, height = 2, borderwidth =1)
        # self.textNationaly.place(x =250 , y = 490)
        # buttonChangeNationaly = tk.Button(frame, text = "Sửa", font = ("Times New Roman", 15), height = 1, bd = 0, bg = "white", fg = "blue"
        #                                 , highlightthickness = 1, highlightbackground = "blue")
        # buttonChangeNationaly.place(x = 685, y = 492)

        # buttonImgStudent = tk.Button(frame, text ="Ảnh sinh viên", font = ("Times New Roman", 20), bg ="white", fg = "black", bd = 0)
        # buttonImgStudent.place(x =870, y =290)
        # imgStudent = tk.Label(frame, bg = "white")
        # imgStudent.place(x = 860, y = 90)
        # buttonImgStudent.config(command=lambda: self.open_image(imgStudent))


        buttonAdd = tk.Button(frame, text ="Thêm sinh viên", font =("Times New Roman", 15), width = 11, height =2, bd = 0,bg="white", fg="red", command=self.saveStudent)
        buttonAdd.place(x = 800, y = 500)
        buttonAdd.bind("<Enter>", self.on_mouse_enter)
        buttonAdd.bind("<Leave>", self.on_mouse_leave)

        buttonFaceId = tk.Button(frame, text = "Nhận diện khuôn mặt sinh viên", font = ("Times New Roman", 15), height = 2, bd = 0, bg = "white", fg= "red", command = self.TakeImages)
        buttonFaceId.place(x = 830, y = 350)
        buttonFaceId.bind("<Enter>", self.on_mouse_enter)
        buttonFaceId.bind("<Leave>", self.on_mouse_leave)

class AddTeacherGUI(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Thêm Giáo viên")
        self.geometry("1200x600")
        self.configure(bg="white")
        self.create_widget()  # Gọi phương thức để hiển thị các widget


    def fetch_all_department(self)-> list[Department]:
        return DepartmentDAO.get_all()
    
    def fetch_all_class(self)-> list[Class]:
        return ClassDAO.get_all()

    def on_combobox_change(self, event):
        selected_index = self.department_combobox.current()
        if selected_index >= 0:
            department = self.department_data[selected_index]
            print(f"Bạn đã chọn: ID = {department.id}, Tên Khoa = {department.name}")

            self.department_name =department.name

    
    def generate_unique_id(self):
        return int(uuid.uuid4().int % (2**29))

    def save_teacher(self):
      
        self.fullname = self.textName.get()

        teacher = Teacher(
            id=self.generate_unique_id(),
            fullname=self.fullname,
            gender=self.gender_combobox.get(),
            status="true",  # giả sử bạn có combobox cho trạng thái
            address=self.textAddress.get("1.0", "end-1c"),
            email=self.textEmail.get(),
            phone=self.textPhone.get(),
            department_id=self.department_map.get(self.selected_department.get()),
            username=self.textUsername.get()
    )
        TeacherDAO.save(teacher)
       

    def addBorderButton(self, button):
        button.update_idletasks()
        button_width = button.winfo_width()
        button_height = button.winfo_height()

        border = tk.Canvas(button.master, height = 1, width = button_width, bg = "blue", bd = 0, highlightthickness = 0)
        border.place(x = button.winfo_x(), y = button_height + button.winfo_y())

    def on_button_click(self, entry):
        entry.config(state = tk.NORMAL)

    def on_mouse_enter(self, event):
        event.widget.config(bg = "red")
        event.widget.config(fg = "white")
    def on_mouse_leave(self, event):
        event.widget.config(bg ="white")
        event.widget.config(fg = "red")


    def create_widget(self):
        frame = tk.Frame(self, bg="white")
        frame.place(x=0, y=0, width=1200, height=600)

        titleAdd = tk.Label(frame, text="Quản lý thêm giáo viên", font=("Times New Roman", 25), bg="white")
        titleAdd.place(x=340, y=5)

        labelName = tk.Label(frame, text="Họ tên giáo viên:", font=("Times New Roman", 20), bg="white")
        labelName.place(x=15, y=60)

        labelGender = tk.Label(frame, text="Giới tính:", font=("Times New Roman", 20), bg="white")
        labelGender.place(x=15, y=100)

        labelStatus = tk.Label(frame, text="Tình trạng:", font=("Times New Roman", 20), bg="white")
        labelStatus.place(x=15, y=140)

        labelAddress = tk.Label(frame, text="Địa chỉ:", font=("Times New Roman", 20), bg="white")
        labelAddress.place(x=15, y=180)

        labelEmail = tk.Label(frame, text="Email:", font=("Times New Roman", 20), bg="white")
        labelEmail.place(x=15, y=260)

        labelPhone = tk.Label(frame, text="Số điện thoại:", font=("Times New Roman", 20), bg="white")
        labelPhone.place(x=15, y=300)

        labelDepartment = tk.Label(frame, text="Khoa:", font=("Times New Roman", 20), bg="white")
        labelDepartment.place(x=15, y=340)

        labelUsername = tk.Label(frame, text="Tên đăng nhập:", font=("Times New Roman", 20), bg="white")
        labelUsername.place(x=15, y=380)

        # Các ô nhập
        self.textName = tk.Entry(frame, font=("Times New Roman", 20), width=30, bg="white")
        self.textName.place(x=250, y=60)

        self.gender_combobox = ttk.Combobox(frame, state="readonly", width=30)
        self.gender_combobox['values'] = ["Nam", "Nữ"]
        self.gender_combobox.place(x=250, y=100)

        self.textStatus = tk.Entry(frame, font=("Times New Roman", 20), width=30, bg="white")
        self.textStatus.place(x=250, y=140)

        self.textAddress = tk.Text(frame, font=("Times New Roman", 20), width=30, height=2, bg="white")
        self.textAddress.place(x=250, y=180)

        self.textEmail = tk.Entry(frame, font=("Times New Roman", 20), width=30, bg="white")
        self.textEmail.place(x=250, y=260)

        self.textPhone = tk.Entry(frame, font=("Times New Roman", 20), width=30, bg="white")
        self.textPhone.place(x=250, y=300)

        self.department_data = self.fetch_all_department()
        self.selected_department = tk.StringVar()
        self.department_combobox = ttk.Combobox(frame, textvariable=self.selected_department, state="readonly", width=30)
        self.department_map = {d.name: d.id for d in self.department_data}
        self.department_combobox['values'] = list(self.department_map.keys())
        if self.department_data:
            self.selected_department.set(self.department_data[0].name)
        self.department_combobox.place(x=250, y=340)

        self.textUsername = tk.Entry(frame, font=("Times New Roman", 20), width=30, bg="white")
        self.textUsername.place(x=250, y=380)

        # Nút thêm giáo viên
        buttonAdd = tk.Button(frame, text="Thêm giáo viên", font=("Times New Roman", 15), width=15, height=2, bd=0,
                            bg="white", fg="red", command=self.save_teacher)
        buttonAdd.place(x=800, y=500)
        buttonAdd.bind("<Enter>", self.on_mouse_enter)
        buttonAdd.bind("<Leave>", self.on_mouse_leave)
