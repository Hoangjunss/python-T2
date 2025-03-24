import tkinter as tk
from tkinter import Image, ttk, messagebox
from PIL import Image, ImageTk
import sys
import os
import cv2,os
import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from dao import AttendancesDAO, ClassDAO, DepartmentDAO, StudentDAO
import datetime
import time


from dao.TestDAO import TestDAO
from models.Students import Student
from models.Attendances import Attendances
class DiemDanh(tk.Tk):
    def __init__(self):
        super().__init__()
        self.DiemDanh()
        self.refresh_list()
        self.mainloop()

    def DiemDanh(self):
        self.title('Phần Mềm Điểm Danh Sinh Viên Bằng Nhận Diện Khuôn Mặt')
        self.geometry('850x650')

        frame_top = tk.Frame(self)
        frame_top.pack(fill=tk.X, padx=10, pady=10)

        label_title = tk.Label(frame_top, text="Điểm danh", font=("Arial", 14, 'bold'))
        label_title.pack(anchor="w")

        btn_diem_danh = tk.Button(frame_top, text="Điểm danh nhe",width=20, command= self.diem_danh)
        btn_diem_danh.pack(side=tk.RIGHT, padx=10, pady=10)

        #Phần dưới (bảng và các nút)
        frame_bottom = tk.Frame(self)
        frame_bottom.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Table
        frame_table = tk.Frame(frame_bottom)
        frame_table.pack(side=tk.LEFT, expand="true", fill=tk.BOTH, padx=5)

        columns = ("STT", "MSSV", "Họ tên", "Ngày sinh", "Giới tính", "Thời gian", "Trạng thái")
        self.tree = ttk.Treeview(frame_table, columns=columns, show="headings")

        for col in columns:
            self.tree.heading(col, text=col, command=lambda _col=col: self.treeview_sort_column(_col, False))
            self.tree.column(col, anchor="center")

        self.tree.column("STT", width=30)
        self.tree.column("MSSV", width=80)
        self.tree.column("Họ tên", width=200)
        self.tree.column("Ngày sinh", width=120)
        self.tree.column("Giới tính", width=80)
        self.tree.column("Thời gian", width=120)
        self.tree.column("Trạng thái", width=120)

        # Tạo Scrollbar
        scrollbar = ttk.Scrollbar(frame_table, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Đặt Treeview và Scrollbar vào Frame
        self.tree.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


    def refresh_list(self):
        # Xóa hết nội dung hiện tại
        for item in self.tree.get_children():
            self.tree.delete(item)
        i=1
        try:
            print(AttendancesDAO.get_all())
            attendance = AttendancesDAO.get_all()
            for at in attendance:
                student_info = StudentDAO.get_by_id(at.student_id)
                self.tree.insert("", "end", values=(
                    i,
                    student_info.id,
                    student_info.fullname,
                    student_info.dateOfBirth,
                    student_info.gender,
                    at.checkin_time,
                    at.status

                ))
                i += 1
        except Exception as e:
            print(f'Error: {e}')
            messagebox.showerror('Error', str(e))

    def treeview_sort_column(self, col, reverse):
        l = []
        for k in self.tree.get_children(''):
            try:
                val = float(self.tree.set(k, col))  # Thử chuyển đổi thành số thực
            except ValueError:
                val = self.tree.set(k, col)  # Nếu không phải số, giữ nguyên chuỗi
            l.append((val, k))

        l.sort(reverse=reverse)

        for index, (val, k) in enumerate(l):
            self.tree.move(k, '', index)

        self.tree.heading(col, command=lambda: self.treeview_sort_column(col, not reverse))
    
    def diem_danh(self):
        recognizer = cv2.face.LBPHFaceRecognizer_create()#cv2.createLBPHFaceRecognizer()
        recognizer.read("TrainingImageLabel\Trainner.yml")
        harcascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(harcascadePath);    
        # df=pd.read_csv("StudentDetails\StudentDetails.csv")
        cam = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_SIMPLEX        
        col_names =  ['Id','Name','Date','Time']
        attendance = pd.DataFrame(columns = col_names)    
        while True:
            ret, im =cam.read()
            gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
            faces=faceCascade.detectMultiScale(gray, 1.2,5)    
            for(x,y,w,h) in faces:
                cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
                Id, conf = recognizer.predict(gray[y:y+h,x:x+w])                                   
                if(conf < 50):
                    student=StudentDAO.get_by_id(Id)
                    ts = time.time()      
                    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                   # aa=df.loc[df['Id'] == Id]['Name'].values
                    tt=str(Id)+"-"+student.fullname
                    attendance.loc[len(attendance)] = [Id,student.fullname,date,timeStamp]
                    attendances=Attendances(id=None, class_id=student.class_id, student_id=student.id, status="Điểm danh thành công", checkin_time=timeStamp)
                    AttendancesDAO.save(attendances=attendances)
                    
                else:
                    Id='Unknown'                
                    tt=str(Id)             
                cv2.putText(im,str(tt),(x,y+h), font, 1,(255,255,255),2)        
            attendance=attendance.drop_duplicates(subset=['Id'],keep='first')    
            cv2.imshow('im',im) 
            if (cv2.waitKey(1)==ord('q')):
                break
        cam.release()
        cv2.destroyAllWindows()
        self.refresh_list()
        
if __name__ == '__main__':
    app = DiemDanh()
    app.mainloop()